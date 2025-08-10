# 노션 API 설정 및 사용 가이드

노션 데이터베이스에서 모든 논문 리뷰를 자동으로 가져와서 ai-folio 블로그로 변환하는 방법을 안내합니다.

## 🔧 1단계: 노션 API 설정

### 1.1 노션 Integration 생성

1. [Notion Developers](https://developers.notion.com/) 페이지 방문
2. "My integrations" 클릭
3. "New integration" 버튼 클릭
4. Integration 정보 입력:
   - **Name**: `AI-Folio Blog Converter` (원하는 이름)
   - **Associated workspace**: 본인의 워크스페이스 선택
   - **Type**: Internal
5. "Submit" 클릭
6. **Internal Integration Token**을 복사해서 안전한 곳에 보관

### 1.2 데이터베이스에 권한 부여

1. 노션에서 논문 리뷰 데이터베이스 페이지로 이동
2. 페이지 우상단의 "..." (More) 메뉴 클릭
3. "Add connections" 클릭
4. 방금 생성한 Integration 선택
5. "Confirm" 클릭

### 1.3 데이터베이스 ID 확인

노션 데이터베이스 URL에서 ID를 추출합니다:

```
https://notion.so/workspace/24dbac48c8d34705ba7d2ac1317274ec?v=16fbfee8209780bd8fe4000c1dc16371
```

여기서 데이터베이스 ID는: `24dbac48c8d34705ba7d2ac1317274ec`

## 📦 2단계: 필요한 패키지 설치

```bash
pip install notion-client requests PyYAML
```

## 🚀 3단계: 환경 변수 설정

### macOS/Linux:
```bash
export NOTION_TOKEN="your_integration_token_here"
```

### Windows:
```cmd
set NOTION_TOKEN=your_integration_token_here
```

### 영구 설정 (macOS/Linux):
```bash
echo 'export NOTION_TOKEN="your_integration_token_here"' >> ~/.bashrc
# 또는 ~/.zshrc (zsh 사용자)
source ~/.bashrc
```

## 🎯 4단계: 스크립트 실행

### 전체 데이터베이스 변환:
```bash
python scripts/notion_database_fetcher.py \
  --database-id "24dbac48c8d34705ba7d2ac1317274ec"
```

### 날짜 범위 지정:
```bash
python scripts/notion_database_fetcher.py \
  --database-id "24dbac48c8d34705ba7d2ac1317274ec" \
  --start-date "2024-01-01" \
  --end-date "2024-12-31"
```

### 토큰을 직접 전달:
```bash
python scripts/notion_database_fetcher.py \
  --database-id "24dbac48c8d34705ba7d2ac1317274ec" \
  --token "your_token_here"
```

## 📋 스크립트가 처리하는 내용

### 자동 추출되는 메타데이터:
- **제목** (이름/Name/Title 속성)
- **Venue** (Select 또는 Text 타입)
- **Date** (Date 타입)
- **Person** (People 또는 Text 타입)
- **Property** (Multi-select 또는 Select 타입)

### 지원되는 노션 블록 타입:
- ✅ 제목 (Heading 1, 2, 3)
- ✅ 문단 (Paragraph)
- ✅ 리스트 (Bulleted, Numbered)
- ✅ 코드 블록 (Code)
- ✅ 인용구 (Quote)
- ✅ 구분선 (Divider)
- ✅ 이미지 (Image) - 자동 다운로드
- ✅ 서식 (Bold, Italic, Code, Strikethrough)
- ✅ 링크 (Link)

## 🎨 결과물

변환이 완료되면 다음과 같은 구조가 생성됩니다:

```
📁 프로젝트 루트/
├── 📁 _posts/
│   ├── 📄 2024-01-15-attention-is-all-you-need.md
│   ├── 📄 2024-02-20-bert-pre-training.md
│   └── 📄 2024-03-10-gpt-improving-language.md
├── 📁 assets/img/posts/
│   ├── 📁 2024-01-15-attention-is-all-you-need/
│   │   ├── 🖼️ image_0.png
│   │   └── 🖼️ image_1.png
│   ├── 📁 2024-02-20-bert-pre-training/
│   └── 📁 2024-03-10-gpt-improving-language/
```

## ⚡ 자동화 예시

정기적으로 새로운 논문을 동기화하려면:

```bash
#!/bin/bash
# sync_notion_papers.sh

echo "🔄 노션 데이터베이스 동기화 시작..."

# 최근 1주일간의 논문만 가져오기
WEEK_AGO=$(date -d "7 days ago" +%Y-%m-%d)
TODAY=$(date +%Y-%m-%d)

python scripts/notion_database_fetcher.py \
  --database-id "24dbac48c8d34705ba7d2ac1317274ec" \
  --start-date "$WEEK_AGO" \
  --end-date "$TODAY"

echo "✅ 동기화 완료!"

# Jekyll 서버 재시작 (선택사항)
# pkill -f jekyll
# bundle exec jekyll serve --detach
```

## 🔍 문제 해결

### 자주 발생하는 오류들:

#### 1. "Unauthorized" 오류
```
❌ 페이지 가져오기 실패: Unauthorized
```
**해결방법**:
- 노션 Integration Token이 올바른지 확인
- 데이터베이스에 Integration 권한이 부여되었는지 확인

#### 2. "Object not found" 오류
```
❌ 페이지 가져오기 실패: Object not found
```
**해결방법**:
- 데이터베이스 ID가 올바른지 확인
- 데이터베이스가 삭제되지 않았는지 확인

#### 3. "Rate limited" 오류
```
❌ API 제한에 걸렸습니다
```
**해결방법**:
- 잠시 기다린 후 다시 실행
- 스크립트에 내장된 지연 시간이 자동으로 처리

#### 4. 이미지 다운로드 실패
```
❌ 이미지 다운로드 실패
```
**해결방법**:
- 네트워크 연결 확인
- 노션 이미지 URL 만료 (24시간 후 만료됨)

## 🎛️ 고급 설정

### 배치 크기 조정:
스크립트에서 `page_size` 값을 조정하여 한 번에 가져오는 페이지 수를 변경할 수 있습니다.

### API 지연 시간 조정:
네트워크가 느린 경우 `time.sleep()` 값을 늘려서 안정성을 높일 수 있습니다.

### 커스텀 속성 추가:
노션 데이터베이스에 새로운 속성을 추가한 경우, `extract_page_metadata()` 함수를 수정하여 해당 속성을 추출할 수 있습니다.

## 📞 지원

문제가 발생하거나 새로운 기능이 필요하면 언제든 말씀해주세요! 🙋‍♂️ 