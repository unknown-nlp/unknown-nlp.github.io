#!/usr/bin/env python3
"""
마크다운 파일의 가독성을 개선하는 스크립트

사용법:
    python scripts/markdown_improver.py --input "input.md" --output "output.md"
    python scripts/markdown_improver.py --input "input.md"  # 같은 파일에 덮어쓰기
"""

import re
import argparse
from pathlib import Path

def improve_markdown_readability(content):
    """
    마크다운의 가독성을 대폭 개선하는 함수
    """
    
    # 1. 제목 계층 구조 정리
    content = fix_heading_hierarchy(content)
    
    # 2. 리스트 구조 개선
    content = improve_lists(content)
    
    # 3. 코드 블록 정리
    content = improve_code_blocks(content)
    
    # 4. 테이블 정리
    content = improve_tables(content)
    
    # 5. 강조 표시 일관성 개선
    content = improve_emphasis(content)
    
    # 6. 링크 정리
    content = improve_links(content)
    
    # 7. 공백 및 줄바꿈 정리
    content = fix_spacing(content)
    
    # 8. 인용구 개선
    content = improve_quotes(content)
    
    # 9. 특수 섹션 강조
    content = enhance_special_sections(content)
    
    # 10. 한국어 텍스트 개선
    content = improve_korean_text(content)
    
    return content.strip()

def fix_heading_hierarchy(content):
    """제목 계층 구조 정리"""
    lines = content.split('\n')
    result = []
    
    for line in lines:
        # 제목 레벨 정리 (너무 깊은 제목 방지)
        if line.strip().startswith('#'):
            # 7레벨 이상의 제목을 6레벨로 제한
            if line.startswith('#######'):
                line = re.sub(r'^#{7,}', '######', line)
            
            # 제목과 # 사이에 공백 확보
            line = re.sub(r'^(#{1,6})([^#\s])', r'\1 \2', line)
            
            # 제목 끝의 불필요한 # 제거
            line = re.sub(r'\s*#+\s*$', '', line)
        
        result.append(line)
    
    return '\n'.join(result)

def improve_lists(content):
    """리스트 구조 개선"""
    lines = content.split('\n')
    result = []
    in_list = False
    
    for i, line in enumerate(lines):
        # 리스트 마커 통일 (*, +를 -로)
        if re.match(r'^\s*[\*\+]\s+', line):
            line = re.sub(r'^(\s*)[\*\+](\s+)', r'\1-\2', line)
        
        # 번호 리스트 정리
        if re.match(r'^\s*\d+\.\s+', line):
            # 번호와 내용 사이 공백 정리
            line = re.sub(r'^(\s*\d+\.)\s+', r'\1 ', line)
        
        # 리스트 항목 들여쓰기 정리
        if re.match(r'^\s*[-\*\+]\s+', line):
            in_list = True
            # 들여쓰기 공백을 2의 배수로 정리
            indent_match = re.match(r'^(\s*)', line)
            if indent_match:
                indent = len(indent_match.group(1))
                normalized_indent = (indent // 2) * 2
                line = ' ' * normalized_indent + line.lstrip()
        elif in_list and line.strip() == '':
            # 리스트 중간의 빈 줄 유지
            pass
        elif in_list and not re.match(r'^\s*[-\*\+\d]', line) and line.strip():
            # 리스트가 끝났음을 감지
            in_list = False
        
        result.append(line)
    
    return '\n'.join(result)

def improve_code_blocks(content):
    """코드 블록 정리"""
    # 코드 블록 전후 줄바꿈 정리
    content = re.sub(r'\n+```', '\n\n```', content)
    content = re.sub(r'```\n+', '```\n\n', content)
    
    # 인라인 코드 정리
    content = re.sub(r'`([^`]+)`', lambda m: f'`{m.group(1).strip()}`', content)
    
    # 코드 블록 언어 지정 정리
    content = re.sub(r'```(\w+)\n', r'```\1\n', content)
    
    return content

def improve_tables(content):
    """테이블 정리"""
    lines = content.split('\n')
    result = []
    
    for line in lines:
        # 테이블 행 정리
        if '|' in line and not line.strip().startswith('|'):
            # 테이블 행 시작에 | 추가
            if re.match(r'^\s*[^|]*\|', line):
                line = '|' + line
        
        # 테이블 행 끝에 | 추가
        if '|' in line and not line.strip().endswith('|'):
            line = line.rstrip() + '|'
        
        result.append(line)
    
    return '\n'.join(result)

def improve_emphasis(content):
    """강조 표시 일관성 개선"""
    # 볼드 강조 정리
    content = re.sub(r'\*\*([^*]+)\*\*', r'**\1**', content)
    content = re.sub(r'__([^_]+)__', r'**\1**', content)  # __를 **로 통일
    
    # 이탤릭 강조 정리
    content = re.sub(r'\b_([^_\s][^_]*[^_\s])_\b', r'*\1*', content)  # _를 *로 통일
    
    # 중첩된 강조 정리
    content = re.sub(r'\*\*\*([^*]+)\*\*\*', r'***\1***', content)
    
    return content

def improve_links(content):
    """링크 정리"""
    # 링크 텍스트와 URL 정리
    content = re.sub(r'\[([^\]]+)\]\(\s*([^)]+)\s*\)', r'[\1](\2)', content)
    
    # 자동 링크 정리
    content = re.sub(r'<(https?://[^>]+)>', r'\1', content)
    
    return content

def fix_spacing(content):
    """공백 및 줄바꿈 정리"""
    # 연속된 공백 정리
    content = re.sub(r'[ \t]+', ' ', content)
    
    # 줄 끝 공백 제거
    content = re.sub(r'[ \t]+$', '', content, flags=re.MULTILINE)
    
    # 연속된 빈 줄 정리 (3개 이상을 2개로)
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # 제목 전후 공백 정리
    content = re.sub(r'\n+(#{1,6}\s[^\n]+)\n*', r'\n\n\1\n\n', content)
    
    # 섹션 구분선 전후 공백 정리
    content = re.sub(r'\n*(-{3,}|={3,}|\*{3,})\n*', r'\n\n\1\n\n', content)
    
    return content

def improve_quotes(content):
    """인용구 개선"""
    lines = content.split('\n')
    result = []
    
    for line in lines:
        # 인용구 마커 정리
        if line.strip().startswith('>'):
            # > 뒤에 공백 확보
            line = re.sub(r'^(\s*>+)([^>\s])', r'\1 \2', line)
        
        result.append(line)
    
    return '\n'.join(result)

def enhance_special_sections(content):
    """특수 섹션 강조"""
    # 주요 키워드를 헤더로 변환
    special_keywords = [
        r'(Key Insights?|Main Findings?|Conclusion|결론|핵심 발견|주요 인사이트)',
        r'(Abstract|요약|초록)',
        r'(Introduction|서론|도입)',
        r'(Methodology|방법론|방법)',
        r'(Results?|결과)',
        r'(Discussion|토론|논의)',
        r'(Limitation|한계점?)',
        r'(Future Work|향후 연구|미래 연구)'
    ]
    
    for pattern in special_keywords:
        # 단독으로 있는 키워드를 헤더로 변환
        content = re.sub(f'^{pattern}:\s*$', r'### \1', content, flags=re.MULTILINE | re.IGNORECASE)
        content = re.sub(f'^{pattern}\s*$', r'### \1', content, flags=re.MULTILINE | re.IGNORECASE)
    
    # Insight 번호 매기기
    content = re.sub(r'^(\s*[-\*]\s*)(Insight\s+\d+)', r'\1**\2**', content, flags=re.MULTILINE | re.IGNORECASE)
    
    return content

def improve_korean_text(content):
    """한국어 텍스트 개선"""
    # 한국어와 영어/숫자 사이 공백 추가 (선택적)
    # content = re.sub(r'([가-힣])([A-Za-z0-9])', r'\1 \2', content)
    # content = re.sub(r'([A-Za-z0-9])([가-힣])', r'\1 \2', content)
    
    # 한국어 문장부호 정리
    content = re.sub(r'([가-힣])\s*,\s*', r'\1, ', content)
    content = re.sub(r'([가-힣])\s*\.\s*', r'\1. ', content)
    
    # 불필요한 공백 제거
    content = re.sub(r'([가-힣])\s+([가-힣])', lambda m: f'{m.group(1)}{m.group(2)}' if len(m.group(0)) > 3 else m.group(0), content)
    
    return content

def add_table_of_contents(content):
    """목차 자동 생성 (선택적)"""
    lines = content.split('\n')
    headers = []
    
    for line in lines:
        if line.strip().startswith('#'):
            level = len(re.match(r'^#+', line.strip()).group(0))
            title = re.sub(r'^#+\s*', '', line.strip())
            headers.append((level, title))
    
    if len(headers) > 3:  # 헤더가 3개 이상일 때만 목차 생성
        toc = ["## 목차\n"]
        for level, title in headers[1:]:  # 첫 번째 헤더(제목)는 제외
            indent = "  " * (level - 2)
            toc.append(f"{indent}- [{title}](#{title.lower().replace(' ', '-')})")
        
        toc_text = '\n'.join(toc) + '\n\n'
        
        # 첫 번째 헤더 다음에 목차 삽입
        if headers:
            first_header_line = None
            for i, line in enumerate(lines):
                if line.strip().startswith('#'):
                    first_header_line = i
                    break
            
            if first_header_line is not None and first_header_line < len(lines) - 1:
                lines.insert(first_header_line + 1, toc_text)
    
    return '\n'.join(lines)

def process_file(input_file, output_file=None, add_toc=False):
    """
    마크다운 파일 처리
    
    Args:
        input_file (str): 입력 파일 경로
        output_file (str, optional): 출력 파일 경로 (None이면 입력 파일에 덮어쓰기)
        add_toc (bool): 목차 추가 여부
    """
    input_path = Path(input_file)
    if not input_path.exists():
        raise FileNotFoundError(f"입력 파일을 찾을 수 없습니다: {input_file}")
    
    # 파일 읽기
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 가독성 개선
    improved_content = improve_markdown_readability(content)
    
    # 목차 추가 (선택적)
    if add_toc:
        improved_content = add_table_of_contents(improved_content)
    
    # 출력 파일 결정
    if output_file is None:
        output_path = input_path
    else:
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # 파일 쓰기
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(improved_content)
    
    print(f"✅ 마크다운 개선 완료!")
    print(f"📄 입력: {input_path}")
    print(f"📄 출력: {output_path}")
    
    # 개선사항 통계
    original_lines = content.count('\n')
    improved_lines = improved_content.count('\n')
    
    print(f"📊 통계:")
    print(f"   - 원본 줄 수: {original_lines}")
    print(f"   - 개선 후 줄 수: {improved_lines}")
    print(f"   - 파일 크기: {len(improved_content):,} 바이트")

def main():
    parser = argparse.ArgumentParser(description='마크다운 파일의 가독성을 개선합니다')
    parser.add_argument('--input', '-i', required=True, help='입력 마크다운 파일 경로')
    parser.add_argument('--output', '-o', help='출력 파일 경로 (생략시 입력 파일에 덮어쓰기)')
    parser.add_argument('--add-toc', action='store_true', help='목차 자동 생성')
    
    args = parser.parse_args()
    
    try:
        process_file(
            input_file=args.input,
            output_file=args.output,
            add_toc=args.add_toc
        )
    except Exception as e:
        print(f"❌ 처리 중 오류 발생: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main()) 