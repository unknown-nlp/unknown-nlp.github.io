#!/usr/bin/env python3
"""
마크다운 유틸리티 함수들
ai-folio 블로그를 위한 마크다운 처리 도구
"""

import re
import yaml
from datetime import datetime
from pathlib import Path

def improve_markdown_readability(content):
    """
    마크다운의 가독성을 개선하는 함수
    
    Args:
        content (str): 원본 마크다운 내용
        
    Returns:
        str: 개선된 마크다운 내용
    """
    # 1. 제목 정리 (첫 번째 # 제목 제거 - front matter에서 처리)
    content = re.sub(r'^# .+\n', '', content, flags=re.MULTILINE)
    
    # 2. 메타데이터 섹션 정리 (Venue, Date, Person 등)
    metadata_pattern = r'(Venue|Date|Person|Files & media|Property):\s*(.+)'
    content = re.sub(metadata_pattern + r'\n?', '', content, flags=re.MULTILINE)
    
    # 3. 연속된 줄바꿈 정리 (3개 이상의 연속된 줄바꿈을 2개로)
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # 4. 리스트 항목 개선
    content = re.sub(r'^[\*\+]\s+', '- ', content, flags=re.MULTILINE)
    
    # 5. 코드 블록과 인용구 주변 공백 정리
    content = re.sub(r'\n+```', '\n\n```', content)
    content = re.sub(r'```\n+', '```\n\n', content)
    
    # 6. 강조 표시 개선
    content = re.sub(r'\*\*([^*]+)\*\*', r'**\1**', content)
    
    # 7. 특수 섹션 강화
    content = enhance_special_sections(content)
    
    # 8. 이미지 참조를 ai-folio 형식으로 변환
    content = convert_image_references(content)
    
    return content.strip()

def enhance_special_sections(content):
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

def convert_image_references(content):
    """
    이미지 참조를 ai-folio 형식으로 변환
    
    Args:
        content (str): 마크다운 내용
        
    Returns:
        str: 변환된 마크다운 내용
    """
    # 노션 스타일의 이미지 참조를 ai-folio 형식으로 변환
    def replace_image_ref(match):
        filename = match.group(1) if match.group(1) else match.group(2)
        # 파일명에서 공백을 제거하거나 변환할 수 있음
        clean_filename = filename.strip()
        return f'{{% include figure.liquid loading="eager" path="assets/img/posts/{{{{ page.slug }}}}/{clean_filename}" class="img-fluid rounded z-depth-1" %}}'
    
    # 다양한 이미지 참조 패턴 처리
    patterns = [
        r'!\[.*?\]\(([^)]+\.(?:png|jpg|jpeg|gif|webp))\)',  # ![alt](image.png)
        r'!\[\]\(([^)]+\.(?:png|jpg|jpeg|gif|webp))\)',     # ![](image.png)
    ]
    
    for pattern in patterns:
        content = re.sub(pattern, replace_image_ref, content, flags=re.IGNORECASE)
    
    return content

def extract_metadata_from_content(content):
    """
    마크다운 내용에서 메타데이터 추출
    
    Args:
        content (str): 마크다운 내용
        
    Returns:
        dict: 추출된 메타데이터
    """
    metadata = {
        "venue": "",
        "date": "",
        "person": "",
        "property": "",
        "files_media": ""
    }
    
    # 메타데이터 패턴 매칭
    patterns = {
        "venue": r'Venue:\s*(.+)',
        "date": r'Date:\s*(.+)',
        "person": r'Person:\s*(.+)',
        "property": r'Property:\s*(.+)',
        "files_media": r'Files & media:\s*(.+)'
    }
    
    for key, pattern in patterns.items():
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            metadata[key] = match.group(1).strip()
    
    return metadata

def generate_tags_from_content(title, content, metadata):
    """
    제목과 내용을 분석해서 태그 자동 생성
    
    Args:
        title (str): 논문 제목
        content (str): 마크다운 내용
        metadata (dict): 메타데이터
        
    Returns:
        list: 생성된 태그 리스트
    """
    tags = set()
    
    # 기본 태그
    tags.add("paper-review")
    
    # Property에서 태그 추출
    if metadata.get("property"):
        property_tags = [tag.strip().lower() for tag in metadata["property"].split(",")]
        tags.update(property_tags)
    
    # 제목에서 키워드 추출
    title_lower = title.lower()
    
    # AI/ML 관련 키워드
    ai_keywords = [
        "transformer", "attention", "bert", "gpt", "llm", "language model",
        "neural", "deep learning", "machine learning", "nlp", "multimodal",
        "reinforcement learning", "diffusion", "embedding", "reasoning",
        "fine-tuning", "pre-training", "alignment", "rlhf"
    ]
    
    for keyword in ai_keywords:
        if keyword in title_lower or keyword in content.lower():
            # 공백을 하이픈으로 변경
            tag = keyword.replace(" ", "-")
            tags.add(tag)
    
    # Venue 태그 추가
    if metadata.get("venue"):
        venue = metadata["venue"].lower().strip()
        if venue:
            tags.add(venue)
    
    return sorted(list(tags))

def create_front_matter(title, date, tags, metadata, slug):
    """
    Jekyll front matter 생성
    
    Args:
        title (str): 포스트 제목
        date (str): 포스트 날짜
        tags (list): 태그 리스트
        metadata (dict): 추출된 메타데이터
        slug (str): URL 슬러그
        
    Returns:
        dict: front matter 딕셔너리
    """
    # 설명 생성
    venue = metadata.get("venue", "")
    description = f"{venue} 논문 리뷰" if venue else "논문 리뷰"
    if metadata.get("property"):
        description += f" - {metadata['property']} 관련 연구"
    
    front_matter = {
        "layout": "post",
        "title": title,
        "date": f"{date} 00:00:00",
        "description": description,
        "tags": tags,
        "categories": ["paper-reviews"],
        "giscus_comments": True,
        "related_posts": False,
        "slug": slug
    }
    
    return front_matter

def create_metadata_section(metadata):
    """
    논문 정보 섹션 생성
    
    Args:
        metadata (dict): 메타데이터
        
    Returns:
        str: 마크다운 형식의 메타데이터 섹션
    """
    section = "\n**논문 정보**\n"
    
    if metadata.get("venue"):
        section += f"- **Venue**: {metadata['venue']}\n"
    if metadata.get("date"):
        section += f"- **Date**: {metadata['date']}\n"
    if metadata.get("person"):
        section += f"- **Reviewer**: {metadata['person']}\n"
    if metadata.get("files_media"):
        section += f"- **Paper Link**: {metadata['files_media']}\n"
    if metadata.get("property"):
        section += f"- **Property**: {metadata['property']}\n"
    
    return section

def generate_slug_from_title(title, date):
    """
    제목과 날짜로부터 URL 슬러그 생성
    
    Args:
        title (str): 논문 제목
        date (str): 날짜 (YYYY-MM-DD)
        
    Returns:
        str: 생성된 슬러그
    """
    # 제목을 소문자로 변환하고 특수문자 제거
    slug = re.sub(r'[^a-zA-Z0-9\s-]', '', title.lower())
    slug = re.sub(r'\s+', '-', slug).strip('-')
    
    # 너무 긴 경우 단축
    if len(slug) > 50:
        words = slug.split('-')
        slug = '-'.join(words[:8])  # 처음 8개 단어만
    
    return f"{date}-{slug}"

if __name__ == "__main__":
    # 테스트용
    print("마크다운 유틸리티 모듈이 로드되었습니다.") 