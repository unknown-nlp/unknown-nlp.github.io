# 노션 → ai-folio 블로그 변환 설정 가이드

## 🚀 빠른 시작

### 1단계: 노션에서 Export

1. 노션 페이지에서 **"..."** 메뉴 클릭
2. **"Export"** 선택
3. **"Markdown & CSV"** 형식 선택
4. **"Export"** 클릭하여 다운로드

### 2단계: 파일 변환

```bash
# 단일 파일 변환
python3 scripts/notion_to_blog.py --notion-file "paper.md" --date "2025-01-02"

# 여러 파일 일괄 변환
python3 scripts/notion_to_blog.py --notion-dir "notion_exports/" --date "2025-01-01" --batch
```

### 3단계: 확인

```bash
# Jekyll 서버 실행
bundle exec jekyll serve

# 브라우저에서 확인
open http://localhost:4000
```

## 📁 파일 구조

### 노션 Export 구조

```
downloads/
├── Paper Title.md                    ← 마크다운 파일
└── Paper Title/                      ← 이미지 폴더
    ├── image1.png
    ├── image2.png
    └── ...
```

### 변환 후 ai-folio 구조

```
_posts/
└── 2025-01-02-paper-title.md        ← 블로그 포스트

assets/img/posts/
└── 2025-01-02-paper-title/          ← 이미지들
    ├── image1.png
    ├── image2.png
    └── ...
```

## 💡 팁

### 좋은 노션 페이지 구조

```markdown
# 논문 제목

Venue: ACL 2024
Date: 2024년 8월 10일  
Person: 홍길동
Property: NLP, Transformer

## Abstract

논문 요약...

## Key Insights

주요 인사이트...

## Methodology

방법론...

## Conclusion

결론...
```

### 커스터마이즈

```bash
# 커스텀 제목으로 변환
python3 scripts/notion_to_blog.py --notion-file "paper.md" --title "내가 정한 제목" --date "2025-01-02"
```

## 🔧 문제 해결

### 이미지가 표시되지 않을 때

1. 이미지 파일이 제대로 복사되었는지 확인
2. Jekyll 서버 재시작
3. 브라우저 캐시 새로고침

### 마크다운이 깨질 때

1. 파일 인코딩이 UTF-8인지 확인
2. 특수문자가 있는지 확인
3. 제목에 특수문자가 없는지 확인

### 변환이 실패할 때

```bash
# 상세한 에러 메시지 확인
python3 scripts/notion_to_blog.py --notion-file "paper.md" --date "2025-01-02" -v
```

## 📞 도움말

- **markdown_utils.py**: 마크다운 처리 함수들
- **notion_to_blog.py**: 메인 변환 스크립트
- **README.md**: 전체 사용법

문제가 있으면 스크립트 코드를 직접 수정하거나 문의하세요! 🙋‍♂️
