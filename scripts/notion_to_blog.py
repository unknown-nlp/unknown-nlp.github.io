#!/usr/bin/env python3
"""
노션 → ai-folio 블로그 변환기 (통합 버전)

간단하고 확실한 방법으로 노션 export 파일을 ai-folio 블로그로 변환

사용법:
    1. 노션에서 "Export" → "Markdown & CSV" 선택
    2. python scripts/notion_to_blog.py --notion-file "파일.md" --date "2025-01-02"
    
특징:
    - 단순하고 안정적
    - 명확한 에러 메시지  
    - 이미지 자동 복사
    - ai-folio 완전 호환
"""

import os
import re
import shutil
import argparse
from pathlib import Path
from datetime import datetime
import yaml

# 로컬 유틸리티 함수들 import
from markdown_utils import (
    improve_markdown_readability, 
    extract_metadata_from_content,
    generate_tags_from_content,
    create_front_matter,
    create_metadata_section,
    generate_slug_from_title
)

def find_notion_files(base_path):
    """
    노션 export 파일들을 찾는 함수
    
    Args:
        base_path (str): 검색할 기본 경로
        
    Returns:
        list: 찾은 마크다운 파일들의 리스트
    """
    base = Path(base_path)
    md_files = []
    
    if base.is_file() and base.suffix == '.md':
        # 직접 파일을 지정한 경우
        md_files.append(base)
    elif base.is_dir():
        # 디렉토리에서 .md 파일 찾기
        md_files = list(base.glob("*.md"))
        # 하위 디렉토리에서도 찾기
        md_files.extend(base.glob("**/*.md"))
    
    return md_files

def find_images_for_paper(md_file_path):
    """
    논문에 해당하는 이미지들을 찾는 함수
    
    Args:
        md_file_path (Path): 마크다운 파일 경로
        
    Returns:
        list: 찾은 이미지 파일들의 리스트
    """
    md_path = Path(md_file_path)
    images = []
    
    # 1. 같은 폴더에서 이미지 찾기
    if md_path.parent.exists():
        for ext in ['*.png', '*.jpg', '*.jpeg', '*.gif', '*.webp']:
            images.extend(md_path.parent.glob(ext))
    
    # 2. 같은 이름의 폴더에서 이미지 찾기
    # 예: paper.md → paper/ 폴더
    folder_name = md_path.stem
    image_folder = md_path.parent / folder_name
    if image_folder.exists():
        for ext in ['*.png', '*.jpg', '*.jpeg', '*.gif', '*.webp']:
            images.extend(image_folder.glob(ext))
    
    # 3. 파일명에서 ID 추출해서 해당 폴더 찾기
    # 예: "Paper Title 23fbfee8209780eda66cf72a1478b06a.md" → "Paper Title 23fbfee8209780eda66cf72a1478b06a/" 폴더
    potential_folders = list(md_path.parent.glob(f"{folder_name}*"))
    for folder in potential_folders:
        if folder.is_dir():
            for ext in ['*.png', '*.jpg', '*.jpeg', '*.gif', '*.webp']:
                images.extend(folder.glob(ext))
    
    return images

def copy_images_to_blog(images, target_slug):
    """
    이미지들을 블로그 폴더로 복사
    
    Args:
        images (list): 이미지 파일 경로 리스트
        target_slug (str): 타겟 슬러그 (예: "2025-01-02-paper-title")
        
    Returns:
        tuple: (복사된 이미지 수, 이미지 디렉토리 경로)
    """
    if not images:
        return 0, ""
    
    # 타겟 디렉토리 생성
    image_dir = Path(f"assets/img/posts/{target_slug}")
    image_dir.mkdir(parents=True, exist_ok=True)
    
    copied_count = 0
    for img_file in images:
        try:
            dest_file = image_dir / img_file.name
            shutil.copy2(img_file, dest_file)
            copied_count += 1
            print(f"   📷 복사: {img_file.name}")
        except Exception as e:
            print(f"   ❌ 이미지 복사 실패: {img_file.name} - {e}")
    
    return copied_count, str(image_dir)

def update_image_paths_in_content(content, target_slug):
    """
    마크다운 내용의 이미지 경로를 ai-folio 형식으로 업데이트
    
    Args:
        content (str): 마크다운 내용
        target_slug (str): 타겟 슬러그
        
    Returns:
        str: 업데이트된 마크다운 내용
    """
    def replace_image_path(match):
        filename = match.group(1)
        # 파일명 정리
        clean_filename = filename.strip()
        return f'{{% include figure.liquid loading="eager" path="assets/img/posts/{target_slug}/{clean_filename}" class="img-fluid rounded z-depth-1" %}}'
    
    # 다양한 이미지 참조 패턴 처리
    patterns = [
        r'!\[.*?\]\(([^)]+\.(?:png|jpg|jpeg|gif|webp))\)',  # ![alt](image.png)
        r'!\[\]\(([^)]+\.(?:png|jpg|jpeg|gif|webp))\)',     # ![](image.png)
    ]
    
    for pattern in patterns:
        content = re.sub(pattern, replace_image_path, content, flags=re.IGNORECASE)
    
    return content

def convert_notion_to_blog(md_file, output_date, custom_title=None):
    """
    노션 마크다운 파일을 ai-folio 블로그 포스트로 변환
    
    Args:
        md_file (str): 노션 마크다운 파일 경로
        output_date (str): 블로그 포스트 날짜 (YYYY-MM-DD)
        custom_title (str, optional): 커스텀 제목
        
    Returns:
        tuple: (생성된 블로그 파일 경로, 이미지 디렉토리 경로)
    """
    md_path = Path(md_file)
    
    print(f"📖 변환 시작: {md_path.name}")
    
    # 1. 마크다운 파일 읽기
    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        raise Exception(f"파일 읽기 실패: {e}")
    
    if not content.strip():
        raise Exception("파일이 비어있습니다")
    
    # 2. 메타데이터 추출
    metadata = extract_metadata_from_content(content)
    print(f"   📋 메타데이터 추출 완료")
    
    # 3. 제목 결정
    if custom_title:
        title = custom_title
    else:
        # 첫 번째 # 제목 찾기
        title_match = re.search(r'^# (.+)', content, re.MULTILINE)
        if title_match:
            title = title_match.group(1).strip()
        else:
            # 파일명에서 제목 추출
            title = md_path.stem
            # ID 부분 제거 (예: "Paper Title 23fbfee8..." → "Paper Title")
            title = re.sub(r'\s+[a-f0-9]{32}$', '', title)
    
    print(f"   📝 제목: {title}")
    
    # 4. 슬러그 생성
    slug = generate_slug_from_title(title, output_date)
    print(f"   🔗 슬러그: {slug}")
    
    # 5. 이미지 찾기 및 복사
    images = find_images_for_paper(md_path)
    print(f"   🔍 이미지 발견: {len(images)}개")
    
    copied_count, image_dir = copy_images_to_blog(images, slug)
    if copied_count > 0:
        print(f"   ✅ 이미지 복사 완료: {copied_count}개")
    
    # 6. 마크다운 내용 개선
    improved_content = improve_markdown_readability(content)
    
    # 7. 이미지 경로 업데이트
    improved_content = update_image_paths_in_content(improved_content, slug)
    
    # 8. 태그 생성
    tags = generate_tags_from_content(title, improved_content, metadata)
    print(f"   🏷️  태그: {', '.join(tags)}")
    
    # 9. Front matter 생성
    front_matter = create_front_matter(title, output_date, tags, metadata, slug)
    
    # 10. 메타데이터 섹션 생성
    metadata_section = create_metadata_section(metadata)
    
    # 11. 최종 내용 구성
    yaml_front_matter = "---\n" + yaml.dump(front_matter, default_flow_style=False, allow_unicode=True) + "---\n"
    final_content = yaml_front_matter + metadata_section + "\n" + improved_content
    
    # 12. 블로그 포스트 파일 생성
    output_file = Path(f"_posts/{slug}.md")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    print(f"✅ 변환 완료!")
    print(f"📄 블로그 포스트: {output_file}")
    if image_dir:
        print(f"🖼️  이미지 폴더: {image_dir}")
    
    return str(output_file), image_dir

def batch_convert_notion_files(notion_path, start_date=None):
    """
    노션 파일들을 일괄 변환
    
    Args:
        notion_path (str): 노션 파일들이 있는 경로
        start_date (str, optional): 시작 날짜 (YYYY-MM-DD)
    """
    md_files = find_notion_files(notion_path)
    
    if not md_files:
        print(f"❌ 마크다운 파일을 찾을 수 없습니다: {notion_path}")
        return
    
    print(f"🔍 {len(md_files)}개의 마크다운 파일을 발견했습니다")
    
    if not start_date:
        start_date = datetime.now().strftime("%Y-%m-%d")
    
    success_count = 0
    failed_count = 0
    
    for i, md_file in enumerate(md_files):
        try:
            # 날짜를 하루씩 증가시켜서 순서 유지
            current_date = datetime.strptime(start_date, "%Y-%m-%d")
            current_date = current_date.replace(day=current_date.day + i)
            date_str = current_date.strftime("%Y-%m-%d")
            
            print(f"\n📖 [{i+1}/{len(md_files)}] 변환 중...")
            convert_notion_to_blog(md_file, date_str)
            success_count += 1
            
        except Exception as e:
            print(f"❌ 실패: {md_file.name} - {e}")
            failed_count += 1
    
    print(f"\n🎉 일괄 변환 완료!")
    print(f"   ✅ 성공: {success_count}개")
    print(f"   ❌ 실패: {failed_count}개")

def main():
    parser = argparse.ArgumentParser(description='노션 → ai-folio 블로그 변환기')
    parser.add_argument('--notion-file', '-f', help='노션 마크다운 파일 경로')
    parser.add_argument('--notion-dir', '-d', help='노션 파일들이 있는 디렉토리')
    parser.add_argument('--date', default=datetime.now().strftime("%Y-%m-%d"), 
                       help='블로그 포스트 날짜 (YYYY-MM-DD)')
    parser.add_argument('--title', help='커스텀 제목')
    parser.add_argument('--batch', action='store_true', help='일괄 변환 모드')
    
    args = parser.parse_args()
    
    if not args.notion_file and not args.notion_dir:
        print("❌ --notion-file 또는 --notion-dir 중 하나를 지정해주세요")
        return 1
    
    try:
        if args.batch or args.notion_dir:
            # 일괄 변환
            notion_path = args.notion_dir or args.notion_file
            batch_convert_notion_files(notion_path, args.date)
        else:
            # 단일 파일 변환
            convert_notion_to_blog(args.notion_file, args.date, args.title)
        
    except Exception as e:
        print(f"❌ 변환 중 오류 발생: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main()) 