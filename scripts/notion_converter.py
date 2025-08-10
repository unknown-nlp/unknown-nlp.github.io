#!/usr/bin/env python3
"""
노션 파일을 ai-folio 블로그 포스트로 변환하는 스크립트

사용법:
    python scripts/notion_converter.py --notion-dir "notion/paper_name/" --date "2025-01-02" --title "논문제목"
"""

import os
import re
import shutil
import argparse
from datetime import datetime
from pathlib import Path
import yaml

def improve_markdown_readability(content):
    """
    노션 마크다운의 가독성을 개선하는 함수
    """
    # 1. 제목 정리 (첫 번째 # 제목 제거 - front matter에서 처리)
    content = re.sub(r'^# .+\n', '', content, flags=re.MULTILINE)
    
    # 2. 메타데이터 섹션 정리 (Venue, Date, Person 등)
    metadata_pattern = r'(Venue|Date|Person|Files & media|Property):\s*(.+)'
    metadata_matches = re.findall(metadata_pattern, content)
    
    # 메타데이터 섹션을 깔끔하게 정리
    if metadata_matches:
        content = re.sub(metadata_pattern + r'\n?', '', content, flags=re.MULTILINE)
    
    # 3. 연속된 줄바꿈 정리 (3개 이상의 연속된 줄바꿈을 2개로)
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # 4. 리스트 항목 개선
    # - 부호를 일관되게 하이픈(-)으로 통일
    content = re.sub(r'^[\*\+]\s+', '- ', content, flags=re.MULTILINE)
    
    # 5. 코드 블록과 인용구 주변 공백 정리
    content = re.sub(r'\n+```', '\n\n```', content)
    content = re.sub(r'```\n+', '```\n\n', content)
    
    # 6. 강조 표시 개선
    # **text** 형태의 볼드를 일관되게 정리
    content = re.sub(r'\*\*([^*]+)\*\*', r'**\1**', content)
    
    # 7. 섹션 구분선 개선
    content = re.sub(r'^-{3,}$', '---', content, flags=re.MULTILINE)
    
    # 8. 한국어와 영어 사이 공백 추가 (선택적)
    # content = re.sub(r'([가-힣])([A-Za-z])', r'\1 \2', content)
    # content = re.sub(r'([A-Za-z])([가-힣])', r'\1 \2', content)
    
    # 9. 불필요한 공백 제거
    content = re.sub(r'[ \t]+$', '', content, flags=re.MULTILINE)
    
    # 10. 인사이트/결론 섹션 강조
    content = re.sub(r'^(Key Insights?|Main [Ff]indings?|Conclusion):', r'### \1', content, flags=re.MULTILINE)
    content = re.sub(r'^(주요 인사이트|핵심 발견|결론):', r'### \1', content, flags=re.MULTILINE)
    
    return content.strip()

def extract_metadata_from_content(content):
    """
    노션 마크다운에서 메타데이터 추출
    """
    metadata = {}
    
    # 기본 메타데이터 패턴 매칭
    patterns = {
        'venue': r'Venue:\s*(.+)',
        'paper_date': r'Date:\s*(.+)',
        'reviewer': r'Person:\s*(.+)',
        'paper_link': r'Files & media:\s*(.+)',
        'property': r'Property:\s*(.+)'
    }
    
    for key, pattern in patterns.items():
        match = re.search(pattern, content)
        if match:
            metadata[key] = match.group(1).strip()
    
    # 제목 추출 (첫 번째 # 헤더)
    title_match = re.search(r'^# (.+)', content, re.MULTILINE)
    if title_match:
        metadata['title'] = title_match.group(1).strip()
    
    return metadata

def convert_image_paths(content, post_slug):
    """
    노션 이미지 경로를 ai-folio 형식으로 변환
    """
    # 노션 이미지 경로 패턴: ![image.png](폴더명/image.png)
    def replace_image_path(match):
        alt_text = match.group(1) if match.group(1) else "image"
        filename = match.group(3)
        # ai-folio 형식으로 변환
        return f'{{% include figure.liquid loading="eager" path="assets/img/posts/{post_slug}/{filename}" class="img-fluid rounded z-depth-1" %}}'
    
    # 이미지 패턴 매칭 및 교체
    content = re.sub(r'!\[([^\]]*)\]\([^/]+/([^)]+)\)', replace_image_path, content)
    content = re.sub(r'!\[([^\]]*)\]\(([^)]+\.(?:png|jpg|jpeg|gif|webp))\)', 
                     lambda m: f'{{% include figure.liquid loading="eager" path="assets/img/posts/{post_slug}/{m.group(2)}" class="img-fluid rounded z-depth-1" %}}', 
                     content)
    
    return content

def create_front_matter(metadata, post_date, post_slug):
    """
    Jekyll front matter 생성
    """
    # 기본 태그 설정
    tags = ['paper-review']
    
    # Property에 따라 태그 추가
    if 'property' in metadata:
        prop = metadata['property'].lower()
        if 'nlp' in prop or 'lm' in prop:
            tags.append('nlp')
        if 'cv' in prop:
            tags.append('computer-vision')
        if 'ml' in prop:
            tags.append('machine-learning')
    
    # 제목에서 키워드 추출
    if 'title' in metadata:
        title_lower = metadata['title'].lower()
        if 'logit' in title_lower:
            tags.append('logits')
        if 'decoding' in title_lower:
            tags.append('decoding')
        if 'llm' in title_lower or 'language model' in title_lower:
            tags.append('llm')
        if 'transformer' in title_lower:
            tags.append('transformer')
        if 'attention' in title_lower:
            tags.append('attention')
    
    # 중복 제거
    tags = list(set(tags))
    
    front_matter = {
        'layout': 'post',
        'title': metadata.get('title', 'Paper Review'),
        'date': f"{post_date} 00:00:00",
        'description': f"{metadata.get('venue', 'Conference')} 논문 리뷰 - {metadata.get('title', '논문 제목')}",
        'tags': ' '.join(tags),
        'categories': 'paper-reviews',
        'giscus_comments': True,
        'related_posts': False
    }
    
    return front_matter

def convert_notion_to_blog(notion_dir, output_date, custom_title=None, custom_slug=None):
    """
    노션 디렉토리를 ai-folio 블로그 포스트로 변환
    
    Args:
        notion_dir (str): 노션 파일들이 있는 디렉토리 경로
        output_date (str): 블로그 포스트 날짜 (YYYY-MM-DD)
        custom_title (str, optional): 커스텀 제목
        custom_slug (str, optional): 커스텀 슬러그
    """
    notion_path = Path(notion_dir)
    if not notion_path.exists():
        raise FileNotFoundError(f"노션 디렉토리를 찾을 수 없습니다: {notion_dir}")
    
    # 마크다운 파일 찾기
    md_files = list(notion_path.glob("*.md"))
    if not md_files:
        raise FileNotFoundError(f"마크다운 파일을 찾을 수 없습니다: {notion_dir}")
    
    md_file = md_files[0]  # 첫 번째 마크다운 파일 사용
    
    # 마크다운 내용 읽기
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 메타데이터 추출
    metadata = extract_metadata_from_content(content)
    
    # 제목과 슬러그 설정
    if custom_title:
        metadata['title'] = custom_title
    
    title = metadata.get('title', md_file.stem)
    
    if custom_slug:
        post_slug = custom_slug
    else:
        # 제목에서 슬러그 생성
        post_slug = re.sub(r'[^a-zA-Z0-9\s-]', '', title.lower())
        post_slug = re.sub(r'\s+', '-', post_slug).strip('-')
        post_slug = f"{output_date}-{post_slug}"
    
    # 내용 개선
    improved_content = improve_markdown_readability(content)
    
    # 이미지 경로 변환
    converted_content = convert_image_paths(improved_content, post_slug)
    
    # Front matter 생성
    front_matter = create_front_matter(metadata, output_date, post_slug)
    
    # 메타데이터 섹션 추가
    metadata_section = "\n**논문 정보**\n"
    if 'venue' in metadata:
        metadata_section += f"- **Venue**: {metadata['venue']}\n"
    if 'paper_date' in metadata:
        metadata_section += f"- **Date**: {metadata['paper_date']}\n"
    if 'reviewer' in metadata:
        metadata_section += f"- **Reviewer**: {metadata['reviewer']}\n"
    if 'paper_link' in metadata:
        metadata_section += f"- **Paper Link**: [{metadata['paper_link']}]({metadata['paper_link']})\n"
    if 'property' in metadata:
        metadata_section += f"- **Property**: {metadata['property']}\n"
    
    # 최종 내용 구성
    yaml_front_matter = "---\n" + yaml.dump(front_matter, default_flow_style=False, allow_unicode=True) + "---\n"
    final_content = yaml_front_matter + metadata_section + "\n" + converted_content
    
    # 출력 파일 경로
    output_file = Path(f"_posts/{post_slug}.md")
    
    # 블로그 포스트 파일 생성
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    # 이미지 디렉토리 생성 및 복사
    image_output_dir = Path(f"assets/img/posts/{post_slug}")
    image_output_dir.mkdir(parents=True, exist_ok=True)
    
    # PNG, JPG, GIF 파일들 복사
    image_extensions = ['*.png', '*.jpg', '*.jpeg', '*.gif', '*.webp']
    copied_images = []
    
    for ext in image_extensions:
        for img_file in notion_path.glob(ext):
            dest_file = image_output_dir / img_file.name
            shutil.copy2(img_file, dest_file)
            copied_images.append(img_file.name)
    
    print(f"✅ 블로그 포스트 생성 완료!")
    print(f"📄 파일: {output_file}")
    print(f"🖼️  이미지 디렉토리: {image_output_dir}")
    print(f"📷 복사된 이미지: {len(copied_images)}개")
    if copied_images:
        for img in copied_images:
            print(f"   - {img}")
    
    return str(output_file), str(image_output_dir)

def main():
    parser = argparse.ArgumentParser(description='노션 파일을 ai-folio 블로그 포스트로 변환')
    parser.add_argument('--notion-dir', required=True, help='노션 파일이 있는 디렉토리 경로')
    parser.add_argument('--date', required=True, help='블로그 포스트 날짜 (YYYY-MM-DD)')
    parser.add_argument('--title', help='커스텀 제목')
    parser.add_argument('--slug', help='커스텀 슬러그')
    
    args = parser.parse_args()
    
    try:
        convert_notion_to_blog(
            notion_dir=args.notion_dir,
            output_date=args.date,
            custom_title=args.title,
            custom_slug=args.slug
        )
    except Exception as e:
        print(f"❌ 변환 중 오류 발생: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main()) 