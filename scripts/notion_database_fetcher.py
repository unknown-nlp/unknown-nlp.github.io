#!/usr/bin/env python3
"""
노션 데이터베이스에서 모든 논문 리뷰를 가져와서 ai-folio 블로그로 변환하는 스크립트

사용법:
    1. 노션 API 토큰 설정: export NOTION_TOKEN="your_token"
    2. python scripts/notion_database_fetcher.py --database-id "24dbac48c8d34705ba7d2ac1317274ec"

필요한 패키지:
    pip install notion-client requests-html markdown
"""

import os
import re
import json
import argparse
from datetime import datetime, timedelta
from pathlib import Path
import requests
from notion_client import Client
import time

# 로컬 변환 함수들 import
from notion_converter import convert_notion_to_blog, improve_markdown_readability

class NotionDatabaseFetcher:
    def __init__(self, token):
        """
        노션 클라이언트 초기화
        
        Args:
            token (str): 노션 API 토큰
        """
        self.notion = Client(auth=token)
        
    def get_database_pages(self, database_id):
        """
        데이터베이스의 모든 페이지 가져오기
        
        Args:
            database_id (str): 노션 데이터베이스 ID
            
        Returns:
            list: 페이지 목록
        """
        print(f"📖 데이터베이스 {database_id}에서 페이지들을 가져오는 중...")
        
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
        title_prop = properties.get("이름") or properties.get("Name") or properties.get("Title")
        if title_prop and title_prop.get("title"):
            title_text = ""
            for text_obj in title_prop["title"]:
                title_text += text_obj.get("plain_text", "")
            metadata["title"] = title_text.strip()
        
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
    
    def get_page_content(self, page_id):
        """
        페이지 내용을 마크다운으로 변환
        
        Args:
            page_id (str): 페이지 ID
            
        Returns:
            str: 마크다운 내용
        """
        try:
            blocks = self.get_all_blocks(page_id)
            markdown_content = self.blocks_to_markdown(blocks)
            return markdown_content
        except Exception as e:
            print(f"❌ 페이지 {page_id} 내용 가져오기 실패: {e}")
            return ""
    
    def get_all_blocks(self, block_id):
        """
        블록의 모든 자식 블록들을 재귀적으로 가져오기
        
        Args:
            block_id (str): 블록 ID
            
        Returns:
            list: 모든 블록 목록
        """
        blocks = []
        start_cursor = None
        
        while True:
            try:
                response = self.notion.blocks.children.list(
                    block_id=block_id,
                    start_cursor=start_cursor,
                    page_size=100
                )
                
                current_blocks = response["results"]
                
                # 자식 블록이 있는 경우 재귀적으로 가져오기
                for block in current_blocks:
                    if block.get("has_children"):
                        child_blocks = self.get_all_blocks(block["id"])
                        block["children"] = child_blocks
                
                blocks.extend(current_blocks)
                
                if not response["has_more"]:
                    break
                    
                start_cursor = response["next_cursor"]
                time.sleep(0.1)  # API 제한 방지
                
            except Exception as e:
                print(f"❌ 블록 가져오기 실패: {e}")
                break
        
        return blocks
    
    def blocks_to_markdown(self, blocks):
        """
        노션 블록들을 마크다운으로 변환
        
        Args:
            blocks (list): 노션 블록 목록
            
        Returns:
            str: 마크다운 텍스트
        """
        markdown_lines = []
        
        for block in blocks:
            block_type = block.get("type")
            
            if block_type == "paragraph":
                text = self.rich_text_to_markdown(block["paragraph"]["rich_text"])
                if text.strip():
                    markdown_lines.append(text)
                    markdown_lines.append("")
            
            elif block_type == "heading_1":
                text = self.rich_text_to_markdown(block["heading_1"]["rich_text"])
                markdown_lines.append(f"# {text}")
                markdown_lines.append("")
            
            elif block_type == "heading_2":
                text = self.rich_text_to_markdown(block["heading_2"]["rich_text"])
                markdown_lines.append(f"## {text}")
                markdown_lines.append("")
            
            elif block_type == "heading_3":
                text = self.rich_text_to_markdown(block["heading_3"]["rich_text"])
                markdown_lines.append(f"### {text}")
                markdown_lines.append("")
            
            elif block_type == "bulleted_list_item":
                text = self.rich_text_to_markdown(block["bulleted_list_item"]["rich_text"])
                markdown_lines.append(f"- {text}")
                
                # 자식 항목 처리
                if block.get("children"):
                    child_markdown = self.blocks_to_markdown(block["children"])
                    child_lines = child_markdown.split('\n')
                    for child_line in child_lines:
                        if child_line.strip():
                            markdown_lines.append(f"  {child_line}")
            
            elif block_type == "numbered_list_item":
                text = self.rich_text_to_markdown(block["numbered_list_item"]["rich_text"])
                markdown_lines.append(f"1. {text}")
                
                # 자식 항목 처리
                if block.get("children"):
                    child_markdown = self.blocks_to_markdown(block["children"])
                    child_lines = child_markdown.split('\n')
                    for child_line in child_lines:
                        if child_line.strip():
                            markdown_lines.append(f"   {child_line}")
            
            elif block_type == "code":
                language = block["code"].get("language", "")
                text = self.rich_text_to_markdown(block["code"]["rich_text"])
                markdown_lines.append(f"```{language}")
                markdown_lines.append(text)
                markdown_lines.append("```")
                markdown_lines.append("")
            
            elif block_type == "quote":
                text = self.rich_text_to_markdown(block["quote"]["rich_text"])
                lines = text.split('\n')
                for line in lines:
                    markdown_lines.append(f"> {line}")
                markdown_lines.append("")
            
            elif block_type == "divider":
                markdown_lines.append("---")
                markdown_lines.append("")
            
            elif block_type == "image":
                image_url = ""
                if block["image"]["type"] == "external":
                    image_url = block["image"]["external"]["url"]
                elif block["image"]["type"] == "file":
                    image_url = block["image"]["file"]["url"]
                
                if image_url:
                    # 이미지 파일명 생성
                    image_name = f"image_{len(markdown_lines)}.png"
                    markdown_lines.append(f"![image]({image_name})")
                    markdown_lines.append("")
        
        return '\n'.join(markdown_lines)
    
    def rich_text_to_markdown(self, rich_text_list):
        """
        노션 rich text를 마크다운으로 변환
        
        Args:
            rich_text_list (list): 노션 rich text 목록
            
        Returns:
            str: 마크다운 텍스트
        """
        result = ""
        
        for text_obj in rich_text_list:
            text = text_obj.get("plain_text", "")
            annotations = text_obj.get("annotations", {})
            
            # 포맷팅 적용
            if annotations.get("bold"):
                text = f"**{text}**"
            if annotations.get("italic"):
                text = f"*{text}*"
            if annotations.get("strikethrough"):
                text = f"~~{text}~~"
            if annotations.get("code"):
                text = f"`{text}`"
            
            # 링크 처리
            if text_obj.get("href"):
                text = f"[{text}]({text_obj['href']})"
            
            result += text
        
        return result
    
    def download_images(self, page_id, blocks, output_dir):
        """
        페이지의 이미지들을 다운로드
        
        Args:
            page_id (str): 페이지 ID
            blocks (list): 블록 목록
            output_dir (Path): 출력 디렉토리
        """
        image_count = 0
        
        for block in blocks:
            if block.get("type") == "image":
                image_url = ""
                if block["image"]["type"] == "external":
                    image_url = block["image"]["external"]["url"]
                elif block["image"]["type"] == "file":
                    image_url = block["image"]["file"]["url"]
                
                if image_url:
                    try:
                        # 이미지 다운로드
                        response = requests.get(image_url, timeout=30)
                        response.raise_for_status()
                        
                        # 파일 확장자 추측
                        content_type = response.headers.get('content-type', '')
                        if 'png' in content_type:
                            ext = '.png'
                        elif 'jpeg' in content_type or 'jpg' in content_type:
                            ext = '.jpg'
                        elif 'gif' in content_type:
                            ext = '.gif'
                        else:
                            ext = '.png'  # 기본값
                        
                        image_name = f"image_{image_count}{ext}"
                        image_path = output_dir / image_name
                        
                        with open(image_path, 'wb') as f:
                            f.write(response.content)
                        
                        print(f"   📷 이미지 다운로드: {image_name}")
                        image_count += 1
                        
                    except Exception as e:
                        print(f"   ❌ 이미지 다운로드 실패: {e}")
            
            # 자식 블록의 이미지도 처리
            if block.get("children"):
                self.download_images(page_id, block["children"], output_dir)
    
    def create_blog_post(self, metadata, content, output_date=None):
        """
        블로그 포스트 생성
        
        Args:
            metadata (dict): 페이지 메타데이터
            content (str): 마크다운 내용
            output_date (str, optional): 출력 날짜
            
        Returns:
            tuple: (생성된 파일 경로, 이미지 디렉토리 경로)
        """
        # 날짜 설정
        if not output_date:
            if metadata.get("date"):
                output_date = metadata["date"]
            else:
                # created_time에서 날짜 추출
                created_time = metadata.get("created_time", "")
                if created_time:
                    output_date = created_time[:10]  # YYYY-MM-DD 형식
                else:
                    output_date = datetime.now().strftime("%Y-%m-%d")
        
        # 슬러그 생성
        title = metadata.get("title", "unknown-paper")
        slug = re.sub(r'[^a-zA-Z0-9\s-]', '', title.lower())
        slug = re.sub(r'\s+', '-', slug).strip('-')
        post_slug = f"{output_date}-{slug}"
        
        # 임시 디렉토리 생성
        temp_dir = Path("temp_notion_export") / post_slug
        temp_dir.mkdir(parents=True, exist_ok=True)
        
        # 메타데이터를 노션 형식으로 포맷팅
        notion_header = f"# {metadata['title']}\n\n"
        if metadata.get("venue"):
            notion_header += f"Venue: {metadata['venue']}\n"
        if metadata.get("date"):
            notion_header += f"Date: {metadata['date']}\n"
        if metadata.get("person"):
            notion_header += f"Person: {metadata['person']}\n"
        if metadata.get("property"):
            notion_header += f"Property: {metadata['property']}\n"
        
        notion_header += "\n---\n\n"
        
        full_content = notion_header + content
        
        # 임시 마크다운 파일 생성
        temp_md_file = temp_dir / f"{post_slug}.md"
        with open(temp_md_file, 'w', encoding='utf-8') as f:
            f.write(full_content)
        
        # 이미지 다운로드 (실제 구현에서는 블록 정보 필요)
        # 여기서는 기본적인 구조만 생성
        
        print(f"📄 블로그 포스트 생성: {metadata['title']}")
        print(f"   📁 임시 디렉토리: {temp_dir}")
        
        return str(temp_md_file), str(temp_dir)

def fetch_and_convert_database(database_id, token, start_date=None, end_date=None):
    """
    노션 데이터베이스의 모든 페이지를 가져와서 블로그 포스트로 변환
    
    Args:
        database_id (str): 노션 데이터베이스 ID
        token (str): 노션 API 토큰
        start_date (str, optional): 시작 날짜 (YYYY-MM-DD)
        end_date (str, optional): 종료 날짜 (YYYY-MM-DD)
    """
    print("🚀 노션 데이터베이스 변환 시작!")
    
    # 노션 클라이언트 초기화
    fetcher = NotionDatabaseFetcher(token)
    
    # 데이터베이스 페이지들 가져오기
    pages = fetcher.get_database_pages(database_id)
    
    if not pages:
        print("❌ 가져올 페이지가 없습니다.")
        return
    
    converted_count = 0
    failed_count = 0
    
    for i, page in enumerate(pages, 1):
        try:
            print(f"\n📖 [{i}/{len(pages)}] 페이지 처리 중...")
            
            # 메타데이터 추출
            metadata = fetcher.extract_page_metadata(page)
            print(f"   제목: {metadata['title']}")
            
            # 날짜 필터링
            page_date = metadata.get("date") or metadata.get("created_time", "")[:10]
            if start_date and page_date < start_date:
                print(f"   ⏭️  스킵 (날짜가 시작일보다 이전): {page_date}")
                continue
            if end_date and page_date > end_date:
                print(f"   ⏭️  스킵 (날짜가 종료일보다 이후): {page_date}")
                continue
            
            # 페이지 내용 가져오기
            content = fetcher.get_page_content(page["id"])
            
            if not content.strip():
                print("   ⚠️  내용이 없는 페이지입니다.")
                continue
            
            # 블로그 포스트 생성
            md_file, temp_dir = fetcher.create_blog_post(metadata, content)
            
            # notion_converter로 최종 변환
            try:
                from notion_converter import convert_notion_to_blog
                convert_notion_to_blog(
                    notion_dir=temp_dir,
                    output_date=page_date,
                    custom_title=metadata["title"]
                )
                converted_count += 1
                print(f"   ✅ 변환 완료!")
                
            except Exception as e:
                print(f"   ❌ 변환 실패: {e}")
                failed_count += 1
            
            # 임시 파일 정리
            import shutil
            if Path(temp_dir).exists():
                shutil.rmtree(temp_dir)
            
            # API 제한 방지
            time.sleep(0.3)
            
        except Exception as e:
            print(f"   ❌ 페이지 처리 실패: {e}")
            failed_count += 1
            continue
    
    print(f"\n🎉 변환 완료!")
    print(f"   ✅ 성공: {converted_count}개")
    print(f"   ❌ 실패: {failed_count}개")
    print(f"   📁 총 처리: {len(pages)}개")

def main():
    parser = argparse.ArgumentParser(description='노션 데이터베이스를 ai-folio 블로그로 변환')
    parser.add_argument('--database-id', required=True, help='노션 데이터베이스 ID')
    parser.add_argument('--token', help='노션 API 토큰 (환경변수 NOTION_TOKEN에서 가져옴)')
    parser.add_argument('--start-date', help='시작 날짜 (YYYY-MM-DD)')
    parser.add_argument('--end-date', help='종료 날짜 (YYYY-MM-DD)')
    
    args = parser.parse_args()
    
    # 토큰 가져오기
    token = args.token or os.getenv('NOTION_TOKEN')
    if not token:
        print("❌ 노션 API 토큰이 필요합니다!")
        print("   방법 1: --token 파라미터로 직접 전달")
        print("   방법 2: 환경변수 설정 - export NOTION_TOKEN='your_token'")
        return 1
    
    try:
        fetch_and_convert_database(
            database_id=args.database_id,
            token=token,
            start_date=args.start_date,
            end_date=args.end_date
        )
    except Exception as e:
        print(f"❌ 변환 중 오류 발생: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main()) 