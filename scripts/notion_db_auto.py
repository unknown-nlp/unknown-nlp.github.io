#!/usr/bin/env python3
"""
노션 데이터베이스 URL → ai-folio 블로그 완전 자동화

사용법:
    1. 노션 API 토큰 설정: export NOTION_TOKEN="your_token"
    2. python scripts/notion_db_auto.py --database-url "https://notion.so/..."
    
특징:
    - 노션 DB URL만 있으면 완전 자동화
    - API 기반으로 실시간 동기화 가능
    - 이미지 자동 다운로드
    - ai-folio 완전 호환
"""

import os
import re
import requests
import argparse
from pathlib import Path
from datetime import datetime
import time
import yaml

try:
    from notion_client import Client
    NOTION_CLIENT_AVAILABLE = True
except ImportError:
    print("❌ notion-client가 설치되지 않았습니다!")
    print("   설치 명령: pip install notion-client")
    NOTION_CLIENT_AVAILABLE = False

# 로컬 유틸리티 함수들 import
from markdown_utils import (
    extract_metadata_from_content,
    generate_tags_from_content,
    create_front_matter,
    create_metadata_section,
    generate_slug_from_title
)

class NotionDatabaseProcessor:
    def __init__(self, token):
        """
        노션 데이터베이스 프로세서 초기화
        
        Args:
            token (str): 노션 API 토큰
        """
        if not NOTION_CLIENT_AVAILABLE:
            raise ImportError("notion-client 패키지가 필요합니다")
        
        self.notion = Client(auth=token)
        self.token = token
        self.downloaded_images = {}  # URL -> 로컬 파일명 매핑
    
    def extract_database_id_from_url(self, url):
        """
        노션 URL에서 데이터베이스 ID 추출
        
        Args:
            url (str): 노션 데이터베이스 URL
            
        Returns:
            str: 데이터베이스 ID
        """
        # 다양한 노션 URL 패턴 처리
        patterns = [
            r'/([a-f0-9]{32})\?',  # ?v= 앞의 ID
            r'/([a-f0-9]{32})$',   # URL 끝의 ID
            r'/([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})',  # UUID 형식
        ]
        
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                db_id = match.group(1).replace('-', '')
                return db_id
        
        raise ValueError(f"URL에서 데이터베이스 ID를 찾을 수 없습니다: {url}")
    
    def get_database_pages(self, database_id):
        """
        데이터베이스의 모든 페이지 가져오기
        
        Args:
            database_id (str): 데이터베이스 ID
            
        Returns:
            list: 페이지 리스트
        """
        print(f"📖 데이터베이스에서 페이지들을 가져오는 중...")
        
        pages = []
        start_cursor = None
        
        while True:
            try:
                response = self.notion.databases.query(
                    database_id=database_id,
                    start_cursor=start_cursor,
                    page_size=100
                )
                
                pages.extend(response["results"])
                
                if not response["has_more"]:
                    break
                    
                start_cursor = response["next_cursor"]
                time.sleep(0.1)  # API 제한 방지
                
            except Exception as e:
                print(f"❌ 페이지 가져오기 실패: {e}")
                break
        
        print(f"✅ 총 {len(pages)}개의 페이지를 찾았습니다!")
        return pages
    
    def extract_page_metadata(self, page):
        """
        페이지에서 메타데이터 추출
        
        Args:
            page (dict): 노션 페이지 객체
            
        Returns:
            dict: 추출된 메타데이터
        """
        properties = page.get("properties", {})
        metadata = {
            "id": page["id"],
            "title": "Unknown Paper",
            "venue": "",
            "date": "",
            "person": "",
            "property": "",
            "created_time": page.get("created_time", ""),
            "last_edited_time": page.get("last_edited_time", "")
        }
        
        # 제목 추출
        title_props = ["이름", "Name", "Title", "name", "title"]
        for prop_name in title_props:
            title_prop = properties.get(prop_name)
            if title_prop and title_prop.get("title"):
                title_text = ""
                for text_obj in title_prop["title"]:
                    title_text += text_obj.get("plain_text", "")
                metadata["title"] = title_text.strip()
                break
        
        # Venue 추출
        venue_prop = properties.get("Venue")
        if venue_prop:
            if venue_prop["type"] == "select" and venue_prop.get("select"):
                metadata["venue"] = venue_prop["select"]["name"]
            elif venue_prop["type"] == "rich_text" and venue_prop.get("rich_text"):
                venue_text = ""
                for text_obj in venue_prop["rich_text"]:
                    venue_text += text_obj.get("plain_text", "")
                metadata["venue"] = venue_text.strip()
        
        # Date 추출
        date_prop = properties.get("Date")
        if date_prop and date_prop.get("date"):
            metadata["date"] = date_prop["date"]["start"]
        
        # Person 추출
        person_prop = properties.get("Person")
        if person_prop:
            if person_prop["type"] == "people" and person_prop.get("people"):
                names = []
                for person in person_prop["people"]:
                    names.append(person.get("name", ""))
                metadata["person"] = ", ".join(names)
            elif person_prop["type"] == "rich_text" and person_prop.get("rich_text"):
                person_text = ""
                for text_obj in person_prop["rich_text"]:
                    person_text += text_obj.get("plain_text", "")
                metadata["person"] = person_text.strip()
        
        # Property 추출
        property_prop = properties.get("Property")
        if property_prop:
            if property_prop["type"] == "multi_select" and property_prop.get("multi_select"):
                properties_list = []
                for prop in property_prop["multi_select"]:
                    properties_list.append(prop["name"])
                metadata["property"] = ", ".join(properties_list)
            elif property_prop["type"] == "select" and property_prop.get("select"):
                metadata["property"] = property_prop["select"]["name"]
        
        return metadata
    
    def get_page_content(self, page_id, slug=None):
        """
        페이지 내용을 마크다운으로 변환
        
        Args:
            page_id (str): 페이지 ID
            slug (str): 포스트 슬러그 (이미지 다운로드용)
            
        Returns:
            str: 마크다운 내용
        """
        try:
            blocks = self.notion.blocks.children.list(block_id=page_id)
            return self.blocks_to_markdown(blocks["results"], slug)
        except Exception as e:
            print(f"   ❌ 페이지 내용 가져오기 실패: {e}")
            return ""
    
    def blocks_to_markdown(self, blocks, slug=None):
        """
        노션 블록을 마크다운으로 변환 (기본적인 변환)
        
        Args:
            blocks (list): 노션 블록 리스트
            slug (str): 포스트 슬러그 (이미지 다운로드용)
            
        Returns:
            str: 마크다운 텍스트
        """
        markdown_content = []
        image_counter = 0
        
        for block in blocks:
            block_type = block["type"]
            
            if block_type == "paragraph":
                text = self.extract_text_from_rich_text(block["paragraph"]["rich_text"])
                if text.strip():
                    markdown_content.append(text + "\n")
            
            elif block_type == "heading_1":
                text = self.extract_text_from_rich_text(block["heading_1"]["rich_text"])
                markdown_content.append(f"# {text}\n")
            
            elif block_type == "heading_2":
                text = self.extract_text_from_rich_text(block["heading_2"]["rich_text"])
                markdown_content.append(f"## {text}\n")
            
            elif block_type == "heading_3":
                text = self.extract_text_from_rich_text(block["heading_3"]["rich_text"])
                markdown_content.append(f"### {text}\n")
            
            elif block_type == "bulleted_list_item":
                text = self.extract_text_from_rich_text(block["bulleted_list_item"]["rich_text"])
                markdown_content.append(f"- {text}\n")
            
            elif block_type == "numbered_list_item":
                text = self.extract_text_from_rich_text(block["numbered_list_item"]["rich_text"])
                markdown_content.append(f"1. {text}\n")
            
            elif block_type == "code":
                text = self.extract_text_from_rich_text(block["code"]["rich_text"])
                language = block["code"].get("language", "")
                markdown_content.append(f"```{language}\n{text}\n```\n")
            
            elif block_type == "quote":
                text = self.extract_text_from_rich_text(block["quote"]["rich_text"])
                markdown_content.append(f"> {text}\n")
            
            elif block_type == "image":
                image_url = block["image"].get("file", {}).get("url", "")
                if image_url and slug:
                    # 이미지 다운로드 및 경로 변환
                    filename = self.download_image(image_url, slug, image_counter)
                    if filename:
                        if filename.startswith("external:"):
                            # 외부 URL인 경우 원본 URL 사용
                            actual_url = filename[9:]  # "external:" 제거
                            print(f"   ⚠️  외부 URL 사용: {actual_url[:50]}...")
                            markdown_content.append(f"![Image]({actual_url})\n")
                        else:
                            # 로컬 파일인 경우 al-folio 형식으로 변환
                            al_folio_tag = f'{{% include figure.liquid loading="eager" path="assets/img/posts/{slug}/{filename}" class="img-fluid rounded z-depth-1" %}}'
                            markdown_content.append(f"{al_folio_tag}\n")
                        image_counter += 1
                    else:
                        # 다운로드 실패시 원본 URL 유지
                        print(f"   ⚠️  이미지 다운로드 실패, 원본 URL 사용")
                        markdown_content.append(f"![Image]({image_url})\n")
                elif image_url:
                    # slug가 없는 경우 원본 URL 사용
                    markdown_content.append(f"![Image]({image_url})\n")
            
            # 다른 블록 타입들은 필요에 따라 추가
        
        return "\n".join(markdown_content)
    
    def extract_text_from_rich_text(self, rich_text_array):
        """
        노션 rich text에서 순수 텍스트 추출
        
        Args:
            rich_text_array (list): 노션 rich text 배열
            
        Returns:
            str: 추출된 텍스트
        """
        text_parts = []
        for text_obj in rich_text_array:
            plain_text = text_obj.get("plain_text", "")
            
            # 스타일 적용
            if text_obj.get("annotations", {}).get("bold"):
                plain_text = f"**{plain_text}**"
            if text_obj.get("annotations", {}).get("italic"):
                plain_text = f"*{plain_text}*"
            if text_obj.get("annotations", {}).get("code"):
                plain_text = f"`{plain_text}`"
            
            text_parts.append(plain_text)
        
        return "".join(text_parts)
    
    def get_image_from_notion_block(self, block):
        """
        노션 블록에서 이미지 정보를 추출
        
        Args:
            block (dict): 노션 이미지 블록
            
        Returns:
            dict: 이미지 정보 (url, caption 등)
        """
        image_info = {}
        
        if block["type"] == "image":
            image_data = block["image"]
            
            # 파일 URL 추출
            if image_data.get("file"):
                image_info["url"] = image_data["file"]["url"]
                image_info["type"] = "file"
            elif image_data.get("external"):
                image_info["url"] = image_data["external"]["url"]
                image_info["type"] = "external"
            
            # 캡션 추출
            caption_parts = []
            for caption in image_data.get("caption", []):
                caption_parts.append(caption.get("plain_text", ""))
            image_info["caption"] = " ".join(caption_parts)
            
        return image_info
    
    def download_image(self, image_url, slug, image_index=0):
        """
        노션 이미지를 다운로드하여 로컬에 저장
        
        Args:
            image_url (str): 노션 이미지 URL
            slug (str): 포스트 슬러그
            image_index (int): 이미지 인덱스 (같은 포스트 내 순서)
            
        Returns:
            str: 로컬 이미지 파일명 (실패시 None)
        """
        try:
            # 이미지 폴더 생성
            image_dir = Path(f"assets/img/posts/{slug}")
            image_dir.mkdir(parents=True, exist_ok=True)
            
            # 노션 이미지 URL은 특별한 처리가 필요함
            # 노션 S3 URL의 경우 Authorization 헤더 없이 요청
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            # 노션 파일 URL인지 확인
            if 'prod-files-secure.s3' in image_url or 'notion.so' in image_url:
                # 노션 파일의 경우 Authorization 헤더 제거
                print(f"   🔗 노션 파일 URL 감지: {image_url[:50]}...")
                response = requests.get(image_url, headers=headers, stream=True, timeout=30)
            else:
                # 일반 이미지 URL의 경우 노션 API 헤더 사용
                headers['Authorization'] = f'Bearer {self.token}'
                headers['Notion-Version'] = '2022-06-28'
                response = requests.get(image_url, headers=headers, stream=True, timeout=30)
            
            response.raise_for_status()
            
            # 파일 확장자 추출
            content_type = response.headers.get('content-type', '')
            url_ext = ''
            
            # URL에서 확장자 추출 시도
            import urllib.parse
            parsed_url = urllib.parse.urlparse(image_url)
            url_path = parsed_url.path.lower()
            
            if url_path.endswith('.jpg') or url_path.endswith('.jpeg'):
                url_ext = '.jpg'
            elif url_path.endswith('.png'):
                url_ext = '.png'
            elif url_path.endswith('.gif'):
                url_ext = '.gif'
            elif url_path.endswith('.webp'):
                url_ext = '.webp'
            elif url_path.endswith('.svg'):
                url_ext = '.svg'
            
            # Content-Type에서 확장자 추출
            if not url_ext:
                if 'jpeg' in content_type or 'jpg' in content_type:
                    url_ext = '.jpg'
                elif 'png' in content_type:
                    url_ext = '.png'
                elif 'gif' in content_type:
                    url_ext = '.gif'
                elif 'webp' in content_type:
                    url_ext = '.webp'
                elif 'svg' in content_type:
                    url_ext = '.svg'
                else:
                    url_ext = '.jpg'  # 기본값을 jpg로 변경
            
            # 파일명 생성
            filename = f"image_{image_index:03d}{url_ext}"
            file_path = image_dir / filename
            
            # 파일 저장
            with open(file_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:  # 빈 청크 필터링
                        f.write(chunk)
            
            # 파일 크기 확인
            file_size = file_path.stat().st_size
            if file_size == 0:
                print(f"   ⚠️  빈 파일이 다운로드됨: {filename}")
                file_path.unlink()  # 빈 파일 삭제
                return None
            
            print(f"   📷 다운로드 완료: {filename} ({file_size:,} bytes)")
            return filename
            
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 400:
                print(f"   ⚠️  이미지 URL 접근 불가 (400 Bad Request)")
                print(f"      노션 이미지는 임시 URL일 수 있습니다: {image_url[:80]}...")
                # 400 에러의 경우 원본 URL을 그대로 사용하도록 반환
                return f"external:{image_url}"
            else:
                print(f"   ❌ HTTP 에러: {e}")
                return None
        except Exception as e:
            print(f"   ❌ 이미지 다운로드 실패: {e}")
            return None
    
    def convert_page_to_blog(self, page, output_date):
        """
        노션 페이지를 ai-folio 블로그 포스트로 변환
        
        Args:
            page (dict): 노션 페이지
            output_date (str): 출력 날짜 - 메타데이터에 날짜가 없을 때 사용
            
        Returns:
            tuple: (생성된 파일 경로, 성공 여부)
        """
        # 메타데이터 추출
        metadata = self.extract_page_metadata(page)
        title = metadata["title"]
        
        print(f"   📝 제목: {title}")
        
        # 날짜 결정 (메타데이터 우선, 없으면 제공된 날짜 사용)
        final_date = output_date
        if metadata.get("date") and metadata["date"].strip():
            meta_date = metadata["date"].strip()
            try:
                # 간단한 날짜 파싱 (YYYY-MM-DD 형식 위주)
                if re.match(r'\d{4}-\d{2}-\d{2}', meta_date):
                    final_date = meta_date[:10]  # YYYY-MM-DD 부분만 추출
                    print(f"   📅 메타데이터 날짜 사용: {final_date}")
                else:
                    print(f"   ⚠️  메타데이터 날짜 형식 인식 불가 ({meta_date}), 제공된 날짜 사용: {output_date}")
            except Exception:
                print(f"   ⚠️  메타데이터 날짜 처리 실패, 제공된 날짜 사용: {output_date}")
        else:
            print(f"   📅 제공된 날짜 사용: {final_date}")
        
        # 슬러그 생성
        slug = generate_slug_from_title(title, final_date)
        print(f"   🔗 슬러그: {slug}")
        
        # 페이지 내용 가져오기 (슬러그 전달)
        content = self.get_page_content(page["id"], slug)
        if not content.strip():
            print(f"   ⚠️  내용이 없는 페이지입니다.")
            return None, False
        
        # 태그 생성
        tags = generate_tags_from_content(title, content, metadata)
        print(f"   🏷️  태그: {', '.join(tags)}")
        
        # Front matter 생성
        front_matter = create_front_matter(title, final_date, tags, metadata, slug)
        
        # 메타데이터 섹션 생성
        metadata_section = create_metadata_section(metadata)
        
        # 최종 내용 구성
        yaml_front_matter = "---\n" + yaml.dump(front_matter, default_flow_style=False, allow_unicode=True) + "---\n"
        final_content = yaml_front_matter + metadata_section + "\n" + content
        
        # 블로그 포스트 파일 생성
        output_file = Path(f"_posts/{slug}.md")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(final_content)
        
        print(f"   ✅ 변환 완료: {output_file}")
        
        return str(output_file), True

def process_notion_database(database_url, token, start_date=None):
    """
    노션 데이터베이스를 처리해서 ai-folio 블로그로 변환
    
    Args:
        database_url (str): 노션 데이터베이스 URL
        token (str): 노션 API 토큰
        start_date (str, optional): 시작 날짜
    """
    print("🚀 노션 데이터베이스 자동 변환 시작!")
    
    processor = NotionDatabaseProcessor(token)
    
    # URL에서 데이터베이스 ID 추출
    try:
        database_id = processor.extract_database_id_from_url(database_url)
        print(f"📋 데이터베이스 ID: {database_id}")
    except ValueError as e:
        print(f"❌ {e}")
        return
    
    # 데이터베이스 페이지들 가져오기
    pages = processor.get_database_pages(database_id)
    
    if not pages:
        print("❌ 가져올 페이지가 없습니다.")
        return
    
    if not start_date:
        start_date = datetime.now().strftime("%Y-%m-%d")
    
    success_count = 0
    failed_count = 0
    
    for i, page in enumerate(pages):
        try:
            # 날짜를 하루씩 증가시켜서 순서 유지 (안전한 방법)
            from datetime import timedelta
            start_dt = datetime.strptime(start_date, "%Y-%m-%d")
            current_dt = start_dt + timedelta(days=i)
            date_str = current_dt.strftime("%Y-%m-%d")
            
            print(f"\n📖 [{i+1}/{len(pages)}] 페이지 처리 중...")
            
            output_file, success = processor.convert_page_to_blog(page, date_str)
            if success:
                success_count += 1
            else:
                failed_count += 1
            
            # API 제한 방지
            time.sleep(0.3)
            
        except Exception as e:
            print(f"   ❌ 페이지 처리 실패: {e}")
            failed_count += 1
            continue
    
    print(f"\n🎉 변환 완료!")
    print(f"   ✅ 성공: {success_count}개")
    print(f"   ❌ 실패: {failed_count}개")
    print(f"   📁 총 처리: {len(pages)}개")

def main():
    if not NOTION_CLIENT_AVAILABLE:
        return 1
    
    parser = argparse.ArgumentParser(description='노션 데이터베이스 → ai-folio 블로그 자동 변환기')
    parser.add_argument('--database-url', required=True, help='노션 데이터베이스 URL')
    parser.add_argument('--token', help='노션 API 토큰')
    parser.add_argument('--start-date', help='시작 날짜 (YYYY-MM-DD)')
    
    args = parser.parse_args()
    
    token = args.token or os.getenv('NOTION_TOKEN')
    if not token:
        print("❌ 노션 API 토큰이 필요합니다!")
        print("   방법 1: --token 파라미터")
        print("   방법 2: export NOTION_TOKEN='your_token'")
        print("   방법 3: https://developers.notion.com/에서 Integration 생성")
        return 1
    
    try:
        process_notion_database(
            database_url=args.database_url,
            token=token,
            start_date=args.start_date
        )
    except Exception as e:
        print(f"❌ 변환 중 오류 발생: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main()) 