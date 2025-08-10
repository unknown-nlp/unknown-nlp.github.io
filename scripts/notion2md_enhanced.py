#!/usr/bin/env python3
"""
notion2md 패키지를 활용한 고급 노션 → ai-folio 블로그 변환기

사용법:
    1. 패키지 설치: pip install notion2md notion-client PyYAML
    2. 토큰 설정: export NOTION_TOKEN="your_token"
    3. python scripts/notion2md_enhanced.py --database-id "24dbac48c8d34705ba7d2ac1317274ec"

장점:
    - notion2md의 안정성 + ai-folio 특화 기능
    - 더 나은 블록 변환 (테이블, 복잡한 구조 지원)
    - 검증된 이미지 다운로드
"""

import os
import re
import json
import argparse
import tempfile
import shutil
from datetime import datetime
from pathlib import Path
import time

# notion2md 패키지 사용
try:
    from notion2md.exporter.block import StringExporter
    from notion_client import Client
    NOTION2MD_AVAILABLE = True
except ImportError:
    print("❌ 필요한 패키지가 설치되지 않았습니다!")
    print("   설치 명령: pip install notion2md notion-client PyYAML")
    NOTION2MD_AVAILABLE = False

# 우리가 만든 변환 함수들
from notion_converter import create_front_matter, improve_markdown_readability

class EnhancedNotionConverter:
    def __init__(self, token):
        """
        강화된 노션 변환기 초기화
        
        Args:
            token (str): 노션 API 토큰
        """
        if not NOTION2MD_AVAILABLE:
            raise ImportError("notion2md 패키지가 필요합니다")
        
        self.notion = Client(auth=token)
        self.token = token
    
    def get_database_pages(self, database_id):
        """
        데이터베이스의 모든 페이지 가져오기 (기존 코드 재사용)
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
                time.sleep(0.1)
                
            except Exception as e:
                print(f"❌ 페이지 가져오기 실패: {e}")
                break
        
        print(f"✅ 총 {len(pages)}개의 페이지를 찾았습니다!")
        return pages
    
    def extract_page_metadata(self, page):
        """
        페이지에서 메타데이터 추출 (기존 코드 재사용)
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
    
    def export_page_with_notion2md(self, page_id, output_dir):
        """
        notion2md를 사용해서 페이지 내용과 이미지를 추출
        
        Args:
            page_id (str): 노션 페이지 ID
            output_dir (Path): 출력 디렉토리
            
        Returns:
            str: 마크다운 내용
        """
        try:
            print(f"   📄 notion2md로 내용 추출 중...")
            
            # StringExporter로 마크다운 텍스트 가져오기
            exporter = StringExporter(
                block_id=page_id,
                output_path=str(output_dir),
                download=True  # 이미지 자동 다운로드
            )
            
            markdown_content = exporter.export()
            
            print(f"   ✅ notion2md 추출 완료!")
            return markdown_content
            
        except Exception as e:
            print(f"   ❌ notion2md 추출 실패: {e}")
            return ""
    
    def enhance_markdown_for_aifolio(self, content, metadata, post_slug):
        """
        notion2md 출력을 ai-folio에 맞게 향상
        
        Args:
            content (str): notion2md에서 생성된 마크다운
            metadata (dict): 페이지 메타데이터
            post_slug (str): 포스트 슬러그
            
        Returns:
            str: 향상된 마크다운
        """
        print(f"   🔧 AI-folio 형식으로 향상 중...")
        
        # 1. 메타데이터 섹션 제거 (front matter에서 처리)
        content = re.sub(r'^#\s+.*?\n', '', content, flags=re.MULTILINE)
        
        # 2. 이미지 경로를 ai-folio 형식으로 변환
        def replace_image_path(match):
            filename = match.group(1)
            # ai-folio 형식으로 변환
            return f'{{% include figure.liquid loading="eager" path="assets/img/posts/{post_slug}/{filename}" class="img-fluid rounded z-depth-1" %}}'
        
        # notion2md의 이미지 패턴을 ai-folio 형식으로 변환
        content = re.sub(r'!\[.*?\]\(([^)]+)\)', replace_image_path, content)
        
        # 3. 기존 가독성 개선 함수 적용
        content = improve_markdown_readability(content)
        
        # 4. 특별한 섹션들 강화
        content = self.enhance_special_sections(content)
        
        print(f"   ✅ 향상 완료!")
        return content
    
    def enhance_special_sections(self, content):
        """
        논문 리뷰에 특화된 섹션들을 강화
        """
        # Key Insights를 더 눈에 띄게
        content = re.sub(
            r'^(Key Insights?):',
            r'## 🔍 \1',
            content,
            flags=re.MULTILINE | re.IGNORECASE
        )
        
        # Conclusion 강화
        content = re.sub(
            r'^(Conclusion|결론):',
            r'## 🎯 \1',
            content,
            flags=re.MULTILINE | re.IGNORECASE
        )
        
        # Abstract/요약 강화
        content = re.sub(
            r'^(Abstract|요약|초록):',
            r'## 📝 \1',
            content,
            flags=re.MULTILINE | re.IGNORECASE
        )
        
        # Methodology 강화
        content = re.sub(
            r'^(Methodology|방법론|방법):',
            r'## 🔬 \1',
            content,
            flags=re.MULTILINE | re.IGNORECASE
        )
        
        return content
    
    def create_aifolio_blog_post(self, metadata, content, output_date=None):
        """
        AI-folio 블로그 포스트 생성
        
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
                created_time = metadata.get("created_time", "")
                if created_time:
                    output_date = created_time[:10]
                else:
                    output_date = datetime.now().strftime("%Y-%m-%d")
        
        # 슬러그 생성
        title = metadata.get("title", "unknown-paper")
        slug = re.sub(r'[^a-zA-Z0-9\s-]', '', title.lower())
        slug = re.sub(r'\s+', '-', slug).strip('-')
        post_slug = f"{output_date}-{slug}"
        
        # Front matter 생성 (기존 함수 활용)
        front_matter = create_front_matter(metadata, output_date, post_slug)
        
        # 메타데이터 섹션 추가
        metadata_section = "\n**논문 정보**\n"
        if metadata.get("venue"):
            metadata_section += f"- **Venue**: {metadata['venue']}\n"
        if metadata.get("date"):
            metadata_section += f"- **Date**: {metadata['date']}\n"
        if metadata.get("person"):
            metadata_section += f"- **Reviewer**: {metadata['person']}\n"
        if metadata.get("property"):
            metadata_section += f"- **Property**: {metadata['property']}\n"
        
        # AI-folio 형식으로 마크다운 향상
        enhanced_content = self.enhance_markdown_for_aifolio(content, metadata, post_slug)
        
        # 최종 내용 구성
        import yaml
        yaml_front_matter = "---\n" + yaml.dump(front_matter, default_flow_style=False, allow_unicode=True) + "---\n"
        final_content = yaml_front_matter + metadata_section + "\n" + enhanced_content
        
        # 출력 파일 생성
        output_file = Path(f"_posts/{post_slug}.md")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(final_content)
        
        # 이미지 디렉토리 (notion2md가 자동 처리)
        image_dir = Path(f"assets/img/posts/{post_slug}")
        
        print(f"📄 블로그 포스트 생성 완료: {output_file}")
        
        return str(output_file), str(image_dir)

def convert_database_with_notion2md(database_id, token, start_date=None, end_date=None):
    """
    notion2md를 활용한 데이터베이스 변환
    
    Args:
        database_id (str): 노션 데이터베이스 ID
        token (str): 노션 API 토큰
        start_date (str, optional): 시작 날짜
        end_date (str, optional): 종료 날짜
    """
    print("🚀 notion2md 기반 데이터베이스 변환 시작!")
    
    converter = EnhancedNotionConverter(token)
    pages = converter.get_database_pages(database_id)
    
    if not pages:
        print("❌ 가져올 페이지가 없습니다.")
        return
    
    converted_count = 0
    failed_count = 0
    
    for i, page in enumerate(pages, 1):
        try:
            print(f"\n📖 [{i}/{len(pages)}] 페이지 처리 중...")
            
            # 메타데이터 추출
            metadata = converter.extract_page_metadata(page)
            print(f"   제목: {metadata['title']}")
            
            # 날짜 필터링
            page_date = metadata.get("date") or metadata.get("created_time", "")[:10]
            if start_date and page_date < start_date:
                print(f"   ⏭️  스킵 (날짜 필터): {page_date}")
                continue
            if end_date and page_date > end_date:
                print(f"   ⏭️  스킵 (날짜 필터): {page_date}")
                continue
            
            # 임시 디렉토리에서 notion2md로 내용 추출
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_path = Path(temp_dir)
                
                # notion2md로 마크다운과 이미지 추출
                content = converter.export_page_with_notion2md(page["id"], temp_path)
                
                if not content.strip():
                    print("   ⚠️  내용이 없는 페이지입니다.")
                    continue
                
                # AI-folio 블로그 포스트 생성
                post_file, image_dir = converter.create_aifolio_blog_post(
                    metadata, content, page_date
                )
                
                # 이미지 파일들을 적절한 위치로 이동
                image_dir_path = Path(image_dir)
                image_dir_path.mkdir(parents=True, exist_ok=True)
                
                # 임시 디렉토리에서 생성된 이미지들을 복사
                for img_file in temp_path.glob("*"):
                    if img_file.is_file() and img_file.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif', '.webp']:
                        dest_file = image_dir_path / img_file.name
                        shutil.copy2(img_file, dest_file)
                        print(f"   📷 이미지 복사: {img_file.name}")
                
                converted_count += 1
                print(f"   ✅ 변환 완료!")
            
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
    if not NOTION2MD_AVAILABLE:
        return 1
    
    parser = argparse.ArgumentParser(description='notion2md 기반 고급 노션 → ai-folio 변환기')
    parser.add_argument('--database-id', required=True, help='노션 데이터베이스 ID')
    parser.add_argument('--token', help='노션 API 토큰')
    parser.add_argument('--start-date', help='시작 날짜 (YYYY-MM-DD)')
    parser.add_argument('--end-date', help='종료 날짜 (YYYY-MM-DD)')
    
    args = parser.parse_args()
    
    token = args.token or os.getenv('NOTION_TOKEN')
    if not token:
        print("❌ 노션 API 토큰이 필요합니다!")
        print("   방법 1: --token 파라미터")
        print("   방법 2: export NOTION_TOKEN='your_token'")
        return 1
    
    try:
        convert_database_with_notion2md(
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