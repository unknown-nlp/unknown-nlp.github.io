# 노션 → ai-folio 블로그 변환 도구 모음

이 폴더에는 노션에서 ai-folio 블로그로 변환하는 **3가지 방법**이 포함되어 있습니다. 각각의 장단점을 비교해서 상황에 맞는 도구를 선택하세요!

## 📁 파일 구성

### 🛠️ 변환 도구들
1. **`notion_converter.py`** - 수동 export용 기본 변환기
2. **`notion_database_fetcher.py`** - 완전 자체 개발 DB 변환기  
3. **`notion2md_enhanced.py`** - notion2md 기반 고급 변환기 ⭐ **추천**

### 📚 유틸리티
- **`markdown_improver.py`** - 마크다운 가독성 개선 전용 도구
- **`setup_notion_api.md`** - 노션 API 설정 가이드
- **`README.md`** - 이 파일

## 🚀 변환 방법 비교

| 특징 | 기본 변환기 | 자체 개발 DB | notion2md 고급 | 
|------|-------------|-------------|----------------|
| **설치 복잡도** | 간단 | 보통 | 보통 |
| **안정성** | 보통 | 보통 | 높음 ⭐ |
| **기능 완성도** | 기본 | 높음 | 최고 ⭐ |
| **블록 지원** | 기본적 | 기본적 | 모든 블록 ⭐ |
| **이미지 처리** | 수동 복사 | 기본 다운로드 | 완전 자동 ⭐ |
| **DB 자동화** | ❌ | ✅ | ✅ |
| **커스터마이즈** | 쉬움 | 쉬움 | 보통 |

## 🎯 사용법 가이드

### 🥇 **추천: notion2md 고급 변환기**

가장 안정적이고 기능이 완전한 방법입니다.

```bash
# 1. 패키지 설치
pip install notion2md notion-client PyYAML

# 2. 환경 변수 설정
export NOTION_TOKEN="your_integration_token"

# 3. 전체 데이터베이스 변환
python scripts/notion2md_enhanced.py \
  --database-id "24dbac48c8d34705ba7d2ac1317274ec"

# 4. 날짜 범위 지정
python scripts/notion2md_enhanced.py \
  --database-id "24dbac48c8d34705ba7d2ac1317274ec" \
  --start-date "2024-01-01" \
  --end-date "2024-12-31"
```

**장점:**
- ✅ 검증된 [notion2md](https://github.com/echo724/notion2md) 패키지 기반 (732⭐)
- ✅ 모든 노션 블록 타입 지원 (테이블, 복잡한 구조 등)
- ✅ 완전 자동 이미지 다운로드
- ✅ AI-folio 완전 최적화 (태그, front matter 등)
- ✅ 데이터베이스 전체 자동 변환

### 🥈 자체 개발 DB 변환기

완전히 우리가 만든 순수 구현입니다.

```bash
# 1. 패키지 설치  
pip install notion-client PyYAML

# 2. 실행
python scripts/notion_database_fetcher.py \
  --database-id "24dbac48c8d34705ba7d2ac1317274ec"
```

**장점:**
- ✅ 외부 의존성 최소화
- ✅ 완전 커스터마이즈 가능
- ✅ AI-folio 완전 최적화

**단점:**
- ⚠️ 복잡한 노션 블록 지원 제한
- ⚠️ 이미지 다운로드 안정성 낮음

### 🥉 기본 변환기 (수동 export)

노션에서 수동으로 export한 파일 변환용입니다.

```bash
# 1. 노션에서 "Markdown & CSV"로 export
# 2. 실행
python scripts/notion_converter.py \
  --notion-dir "notion/paper_folder/" \
  --date "2025-01-02"
```

**장점:**
- ✅ 가장 간단한 설정
- ✅ API 토큰 불필요

**단점:**
- ❌ 수동 작업 필요
- ❌ 데이터베이스 자동화 불가

## 📋 변환 과정 상세

### 모든 변환기 공통 기능:

1. **Jekyll Front Matter 생성**
   - layout, title, date, description
   - 자동 태그 생성 (NLP, transformer, attention 등)
   - 카테고리 설정 (paper-reviews)

2. **AI-folio 최적화**
   - 이미지를 `{% include figure.liquid %}` 형식으로 변환
   - responsive 이미지 지원
   - 적절한 CSS 클래스 적용

3. **가독성 개선**
   - 제목 계층 구조 정리
   - 리스트 마커 통일
   - 코드 블록 정리
   - 특수 섹션 강화 (🔍 Key Insights, 🎯 Conclusion 등)

4. **메타데이터 처리**
   - Venue, Date, Person, Property 자동 추출
   - 논문 정보 섹션 생성

## 🎨 결과물 구조

변환 완료 후 생성되는 파일 구조:

```
📁 프로젝트 루트/
├── 📁 _posts/
│   ├── 📄 2025-01-02-attention-is-all-you-need.md
│   ├── 📄 2025-01-03-bert-pre-training.md
│   └── 📄 2025-01-04-gpt-language-models.md
├── 📁 assets/img/posts/
│   ├── 📁 2025-01-02-attention-is-all-you-need/
│   │   ├── 🖼️ image.png
│   │   ├── 🖼️ figure_1.png
│   │   └── 🖼️ architecture.png
│   ├── 📁 2025-01-03-bert-pre-training/
│   └── 📁 2025-01-04-gpt-language-models/
```

## 🛠️ 개별 도구 사용법

### 마크다운 가독성 개선만 하고 싶다면:

```bash
# 단일 파일 개선
python scripts/markdown_improver.py --input "paper.md"

# 목차 추가
python scripts/markdown_improver.py --input "paper.md" --add-toc

# 모든 포스트 개선
for file in _posts/*.md; do
  python scripts/markdown_improver.py --input "$file"
done
```

## ⚡ 자동화 스크립트

### 정기 동기화 (notion2md 기반)

```bash
#!/bin/bash
# auto_sync_papers.sh

echo "🔄 주간 논문 동기화 시작..."

# 최근 1주일 논문만 가져오기
WEEK_AGO=$(date -d "7 days ago" +%Y-%m-%d)
TODAY=$(date +%Y-%m-%d)

python scripts/notion2md_enhanced.py \
  --database-id "24dbac48c8d34705ba7d2ac1317274ec" \
  --start-date "$WEEK_AGO" \
  --end-date "$TODAY"

# Jekyll 재시작
echo "🔄 Jekyll 서버 재시작..."
pkill -f jekyll
nohup bundle exec jekyll serve --detach &

echo "✅ 동기화 완료!"
```

### cron으로 자동화

```bash
# 매주 일요일 오전 9시에 실행
0 9 * * 0 /path/to/auto_sync_papers.sh
```

## 📦 필요한 패키지 설치

### notion2md 고급 변환기 (추천):
```bash
pip install notion2md notion-client PyYAML requests
```

### 자체 개발 변환기:
```bash
pip install notion-client PyYAML requests
```

### 기본 변환기:
```bash
pip install PyYAML
```

## 🔧 API 설정

노션 API 설정이 필요한 경우 `setup_notion_api.md`를 참고하세요:

1. [Notion Developers](https://developers.notion.com/)에서 Integration 생성
2. 데이터베이스에 권한 부여
3. 환경 변수 설정: `export NOTION_TOKEN="your_token"`

## 🔍 문제 해결

### 자주 발생하는 문제:

**Q: notion2md_enhanced.py에서 "ImportError" 발생**
A: `pip install notion2md notion-client`로 패키지를 설치하세요.

**Q: "Unauthorized" 오류**
A: 노션 API 토큰과 데이터베이스 권한을 확인하세요.

**Q: 이미지가 표시되지 않음**
A: Jekyll 서버를 재시작하고 이미지 파일이 올바른 위치에 있는지 확인하세요.

**Q: 변환 속도가 느림**
A: `time.sleep()` 값을 줄이거나 배치 크기를 늘려보세요.

## 🎖️ 권장 워크플로

1. **초기 설정**: notion2md 고급 변환기로 전체 DB 변환
2. **일상 사용**: 새 논문 추가 시 자동화 스크립트 실행
3. **세부 조정**: 필요시 markdown_improver로 개별 파일 개선
4. **커스터마이즈**: 특별한 요구사항이 있으면 자체 개발 변환기 수정

## 📞 지원

문제가 발생하거나 새로운 기능이 필요하면 언제든 말씀해주세요! 🙋‍♂️

각 도구의 장단점을 고려해서 상황에 맞는 최적의 변환기를 선택하시기 바랍니다. **대부분의 경우 notion2md 고급 변환기를 추천**합니다! 🚀 