---
categories:
- paper-reviews
date: '2025-03-04 00:00:00'
description: 논문 리뷰 - Retrieval, Embeddings 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- attention
- bert
- embedding
- embeddings
- neural
- paper-review
- retrieval
thumbnail: assets/img/posts/2025-03-04-contextual-document-embeddings/thumbnail.jpg
title: Contextual Document Embeddings
---

**논문 정보**
- **Date**: 2025-03-04
- **Reviewer**: 상엽
- **Property**: Retrieval, Embeddings

# Introduction

- **Statistical approaches**: BM25 → **Neural method**: *dual encoder*

- **neural model**에 없는 Statistical approach만이 가진 장점: **prior corpus 통계치**를 알 수 있다는 것

- **연구 목표: dense encoder를 통한 contextualization of document embeddings**

1. **Contextual training procudure**

1. **Architecture**

# Background

**Text retrieval**

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/35a2dde0-027f-484f-83bd-425176b222b5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6B5Q7QS%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCbO9u9eQrPecO3%2BL4EzvKNHpcUQ3HacgUAZz7kN5m41QIgFb3u3CsY%2BgWpx6FKeZsMNthdT5AVmEUKKeHNWe3RWngqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNoIyA0eq143BmGPGCrcA9cfsKJnTILxA5eKojkSWz6SAS2112kPY%2BqKniB94yi6QcF8S2ju0prsmlywMVtZJ271BBsi4fe8t7RtSWtwEYfFYbNXHxYziAbiw8wT2DpHBtBsWnRXHff%2BlUcHUkuppUp%2FgxVV2znA6tT4gRU93nvLp0NkMd5puqaxNHM2W0TD%2FdcwTRmPN%2BhGwGmlgZk6zvY6Me%2BwNzZ9T%2BT6KFgDRBXT79mtk3pW7ELw7dDf%2BUn8zJzmlPvc69tMVjFT5%2Bh61lD0yuGkJ3yxLsfQuUxJrwpvsBd6BcAiCYBurTxMspsn4T%2FVFQO38K6mmeG7sZFBmkBop90FpD%2BbyDXToHUFHVr7Mb3pCbw40%2B8uPbFh8gdJa0euT9KmNwibfwACP0RXr2iNUiz548HvwUb3V8iEr9p5YUVXfqYfItBjP7fqOemqfmlE%2BZ2oBDzgU5OHB%2Fiv3wPcMCRasA3ZanWirsXZ4%2BkE%2Fj9Z7vXpsA3HKvsh97zDXDNLe2prsFTkmnKe5E%2BcYF3ki%2BUFA71UPiJAZ%2BbOZKeKFGb9WnLensMEUFyTSEj3toyFcr7LgmSm8osN1OdSbsOkkcCPBDZ%2BKVtvx8qh%2FeUAHQJNDBZ360w2X2ipdoNNdCet2FzrDBi8sP2jMPn%2B4cQGOqUBaIn2UXop7%2F1K%2Bo4izCdwNPi5yGOTBQ7TbPTI8k0Qsx0XWSemb18zEaJcfxRUwHYRw3DO75iS9DQ%2BsitRDBh6p%2F45%2B6CnLBm89GRIUoNNSgNlxdx%2B0wWWnkespGrmRr9nNkWxRXFMWO9pj%2BfKNYUTJNmi1R%2Bqo3U7Zx8evBFbasopizJZfmMG8TAZUQ1%2Btz%2BKxtQW2V6UwK9NabpvGprD6kYaUzw1&X-Amz-Signature=97203b1bd642fc8901c77e6afefbc3358ed39bf7a6ac6cb7a01fc3f500be5389&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Vector retrieval methods

- Statistical Retrieval

# Method

일반적인 Retrieval 모델 학습은 여러 도메인을 가진 대량의 데이터를 활용하게 되므로 특정 도메인의 통계적 특성을 모델이 알 수가 없음.

### Contextual Training with Adversarial Contrastive Learning

- 일반 도메인에서 NFL은 적은 문서에 등장하여 가치가 있는 단어일지라도 검색 대상 데이터가 Sports 도메인일 경우 해당 단어는 상대적으로 흔한 단어가 됨. → 가중치가 낮아짐.

- **Meta-learning-style objectives**: 도메인 선정 → 관련 예시를 샘플링

### Contextual Document Embedding (CDE)

- **contextualization을 architecture에 직접적으로 주입하자.**

- Sparse retrieval 모델과 같이 corpus에 직접적으로 접근할 수 있는 encoder 모델을 만들자.

1. BM25와 같이 Corpus의 통계치만을 제공하자.

1. 전체 문서에 대한 접근 권한을 가지되 cross attention과 같은 형태로 문서를 선별하자. (Garnelo et al., 2018: small scale) ← Large dataset에서 한계

→ **corpus statistics를 배우되 효과적으로 계산할 수 있는 middleground 방법을 제안**

- Morris et al., 2023의 연구에서 documnet embeddings이 충분한 lexical inforamtion을 갖고 있음.

- corpus subset을 미리 임베딩해 만들어 활용한다면 lexical 정보를 encdoing에서 활용하는 것이 아닌가?

- Two-stage process를 통해  contextualized embedding을 생성

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/2d710029-1ddb-483a-b615-a9d390c9d09c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6B5Q7QS%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCbO9u9eQrPecO3%2BL4EzvKNHpcUQ3HacgUAZz7kN5m41QIgFb3u3CsY%2BgWpx6FKeZsMNthdT5AVmEUKKeHNWe3RWngqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNoIyA0eq143BmGPGCrcA9cfsKJnTILxA5eKojkSWz6SAS2112kPY%2BqKniB94yi6QcF8S2ju0prsmlywMVtZJ271BBsi4fe8t7RtSWtwEYfFYbNXHxYziAbiw8wT2DpHBtBsWnRXHff%2BlUcHUkuppUp%2FgxVV2znA6tT4gRU93nvLp0NkMd5puqaxNHM2W0TD%2FdcwTRmPN%2BhGwGmlgZk6zvY6Me%2BwNzZ9T%2BT6KFgDRBXT79mtk3pW7ELw7dDf%2BUn8zJzmlPvc69tMVjFT5%2Bh61lD0yuGkJ3yxLsfQuUxJrwpvsBd6BcAiCYBurTxMspsn4T%2FVFQO38K6mmeG7sZFBmkBop90FpD%2BbyDXToHUFHVr7Mb3pCbw40%2B8uPbFh8gdJa0euT9KmNwibfwACP0RXr2iNUiz548HvwUb3V8iEr9p5YUVXfqYfItBjP7fqOemqfmlE%2BZ2oBDzgU5OHB%2Fiv3wPcMCRasA3ZanWirsXZ4%2BkE%2Fj9Z7vXpsA3HKvsh97zDXDNLe2prsFTkmnKe5E%2BcYF3ki%2BUFA71UPiJAZ%2BbOZKeKFGb9WnLensMEUFyTSEj3toyFcr7LgmSm8osN1OdSbsOkkcCPBDZ%2BKVtvx8qh%2FeUAHQJNDBZ360w2X2ipdoNNdCet2FzrDBi8sP2jMPn%2B4cQGOqUBaIn2UXop7%2F1K%2Bo4izCdwNPi5yGOTBQ7TbPTI8k0Qsx0XWSemb18zEaJcfxRUwHYRw3DO75iS9DQ%2BsitRDBh6p%2F45%2B6CnLBm89GRIUoNNSgNlxdx%2B0wWWnkespGrmRr9nNkWxRXFMWO9pj%2BfKNYUTJNmi1R%2Bqo3U7Zx8evBFbasopizJZfmMG8TAZUQ1%2Btz%2BKxtQW2V6UwK9NabpvGprD6kYaUzw1&X-Amz-Signature=3f0a202a6ea1f8570980ca008799367b860ef4772ebe3920dd076e2af81506f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**First stage: ***Gather and embed context*

- Context documents: d^1, ..., d^J \in \mathcal{D}가 있을 때, 임베딩 모델을 사용해 만든 임베딩을 concat하여 Embedding sequence M_1(d^1)...M_1(d^J) 획득

**Second stage: ***Embed document with additional context tokens*

- document d'의 임베딩을 일 계산하기 위해 contextual embedding sequence와 결합하여 다음을 계산

- Query도 유사하게 계산

- Contextual embedding implementation

**Embedding without context**

- Training 시, 모델의 generalization을 향상하기 위해 p 확률로 특정 context embedding M_1(d^*)을  null token으로 바꾸는 sequence dropout을 활용.

- Test 시, context를 활용할 수 없을 경우 null tokens을 활용

**Position-agnostic embedding**

- Document의 순서는 무관하기에 모든 postionality를 제거

- \mathcal{D}에 상응하는 position에 positional embedding을 뺌.

**Two-stage gradient caching**

- GradCache의 two-stage version을 이용 → 더 큰 batch와 sequence를 활용 가능

1. first-stage와 second-stage를 gradient 없이 각각 계산 → Loss 계산

1. Second-stage에 대해서만 gradient 계산

1. Gradient 계산을 활성화하여 Second-stage 재실행 → Second-stage 업데이트

1. Gradient 계산을 활성화하여 First-stage 재실행 → First-stage 업데이트

# Experimental Setup

- 적합한 세팅을 찾기 위해 BEIR의 truncate 버전을 활용해 **small setting을 구성**

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/9f6742cd-7dd2-4310-8b5e-29c4afd2e0f4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6B5Q7QS%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCbO9u9eQrPecO3%2BL4EzvKNHpcUQ3HacgUAZz7kN5m41QIgFb3u3CsY%2BgWpx6FKeZsMNthdT5AVmEUKKeHNWe3RWngqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNoIyA0eq143BmGPGCrcA9cfsKJnTILxA5eKojkSWz6SAS2112kPY%2BqKniB94yi6QcF8S2ju0prsmlywMVtZJ271BBsi4fe8t7RtSWtwEYfFYbNXHxYziAbiw8wT2DpHBtBsWnRXHff%2BlUcHUkuppUp%2FgxVV2znA6tT4gRU93nvLp0NkMd5puqaxNHM2W0TD%2FdcwTRmPN%2BhGwGmlgZk6zvY6Me%2BwNzZ9T%2BT6KFgDRBXT79mtk3pW7ELw7dDf%2BUn8zJzmlPvc69tMVjFT5%2Bh61lD0yuGkJ3yxLsfQuUxJrwpvsBd6BcAiCYBurTxMspsn4T%2FVFQO38K6mmeG7sZFBmkBop90FpD%2BbyDXToHUFHVr7Mb3pCbw40%2B8uPbFh8gdJa0euT9KmNwibfwACP0RXr2iNUiz548HvwUb3V8iEr9p5YUVXfqYfItBjP7fqOemqfmlE%2BZ2oBDzgU5OHB%2Fiv3wPcMCRasA3ZanWirsXZ4%2BkE%2Fj9Z7vXpsA3HKvsh97zDXDNLe2prsFTkmnKe5E%2BcYF3ki%2BUFA71UPiJAZ%2BbOZKeKFGb9WnLensMEUFyTSEj3toyFcr7LgmSm8osN1OdSbsOkkcCPBDZ%2BKVtvx8qh%2FeUAHQJNDBZ360w2X2ipdoNNdCet2FzrDBi8sP2jMPn%2B4cQGOqUBaIn2UXop7%2F1K%2Bo4izCdwNPi5yGOTBQ7TbPTI8k0Qsx0XWSemb18zEaJcfxRUwHYRw3DO75iS9DQ%2BsitRDBh6p%2F45%2B6CnLBm89GRIUoNNSgNlxdx%2B0wWWnkespGrmRr9nNkWxRXFMWO9pj%2BfKNYUTJNmi1R%2Bqo3U7Zx8evBFbasopizJZfmMG8TAZUQ1%2Btz%2BKxtQW2V6UwK9NabpvGprD6kYaUzw1&X-Amz-Signature=e3b95ee07d2c365326c253165e1fc83d63c6e5d25a845ffcf2d4cfd1e9aad7fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Large setting에서도 small setting에서 찾은 하이퍼파라미터를 이용

- **Sequence length와 contextual token은 512개의 documents 사용**

**Training Data and Metrics**

- 텍스트 임베딩 학습: 웹 (레딧, 위키피디아)에서 크롤링한 24개의 datasets 활용

- Unsupervised training: 웹 (레딧, 위키피디아)에서 크롤링한 200M data 활용

- Supervised training: 1.8M human-written query-document pairs

**Implementation**

배치 partioning 때,

- GTR: documents와 queries 인코딩

- Faiss: clustering, 100 step, 3 attempts

- NomicBERT: pre-trained model backbone (137M) **for filtering**

**Training**

- M_1, M_2 : **nomic-embed-text-v1** ( Nussbaum et al., 2024) including flash attention

- Adam optimizer

- Contrastive loss, \tau: 0.02

- sequence dropout: 0.005

# Results

**Contextual batching**

- 클러스터링을 통한 batch 그룹 생성과 false negative filtering 이후, batch의 difficulty와 NDCG의 강한 상관관계 확인

- batch의 document reoredering 역시 difficulty를 올렸으며 성능에 긍정적 영향을 줌.

**Contextual architecture**

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/2b814005-a1c8-48d0-93e5-36d3980eed6a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6B5Q7QS%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCbO9u9eQrPecO3%2BL4EzvKNHpcUQ3HacgUAZz7kN5m41QIgFb3u3CsY%2BgWpx6FKeZsMNthdT5AVmEUKKeHNWe3RWngqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNoIyA0eq143BmGPGCrcA9cfsKJnTILxA5eKojkSWz6SAS2112kPY%2BqKniB94yi6QcF8S2ju0prsmlywMVtZJ271BBsi4fe8t7RtSWtwEYfFYbNXHxYziAbiw8wT2DpHBtBsWnRXHff%2BlUcHUkuppUp%2FgxVV2znA6tT4gRU93nvLp0NkMd5puqaxNHM2W0TD%2FdcwTRmPN%2BhGwGmlgZk6zvY6Me%2BwNzZ9T%2BT6KFgDRBXT79mtk3pW7ELw7dDf%2BUn8zJzmlPvc69tMVjFT5%2Bh61lD0yuGkJ3yxLsfQuUxJrwpvsBd6BcAiCYBurTxMspsn4T%2FVFQO38K6mmeG7sZFBmkBop90FpD%2BbyDXToHUFHVr7Mb3pCbw40%2B8uPbFh8gdJa0euT9KmNwibfwACP0RXr2iNUiz548HvwUb3V8iEr9p5YUVXfqYfItBjP7fqOemqfmlE%2BZ2oBDzgU5OHB%2Fiv3wPcMCRasA3ZanWirsXZ4%2BkE%2Fj9Z7vXpsA3HKvsh97zDXDNLe2prsFTkmnKe5E%2BcYF3ki%2BUFA71UPiJAZ%2BbOZKeKFGb9WnLensMEUFyTSEj3toyFcr7LgmSm8osN1OdSbsOkkcCPBDZ%2BKVtvx8qh%2FeUAHQJNDBZ360w2X2ipdoNNdCet2FzrDBi8sP2jMPn%2B4cQGOqUBaIn2UXop7%2F1K%2Bo4izCdwNPi5yGOTBQ7TbPTI8k0Qsx0XWSemb18zEaJcfxRUwHYRw3DO75iS9DQ%2BsitRDBh6p%2F45%2B6CnLBm89GRIUoNNSgNlxdx%2B0wWWnkespGrmRr9nNkWxRXFMWO9pj%2BfKNYUTJNmi1R%2Bqo3U7Zx8evBFbasopizJZfmMG8TAZUQ1%2Btz%2BKxtQW2V6UwK9NabpvGprD6kYaUzw1&X-Amz-Signature=414fe091ceb5135ed93dd9d541a8e6b31b7beed107407de4a26b3d485ccc122f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Archictecture에서도 Contextual을 넣는 것이 일반적으로 더 좋았음.

# Analysis

**How hard are our clusters?**

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/c68c2a02-360c-4548-a468-360e3688cc07/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6B5Q7QS%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCbO9u9eQrPecO3%2BL4EzvKNHpcUQ3HacgUAZz7kN5m41QIgFb3u3CsY%2BgWpx6FKeZsMNthdT5AVmEUKKeHNWe3RWngqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNoIyA0eq143BmGPGCrcA9cfsKJnTILxA5eKojkSWz6SAS2112kPY%2BqKniB94yi6QcF8S2ju0prsmlywMVtZJ271BBsi4fe8t7RtSWtwEYfFYbNXHxYziAbiw8wT2DpHBtBsWnRXHff%2BlUcHUkuppUp%2FgxVV2znA6tT4gRU93nvLp0NkMd5puqaxNHM2W0TD%2FdcwTRmPN%2BhGwGmlgZk6zvY6Me%2BwNzZ9T%2BT6KFgDRBXT79mtk3pW7ELw7dDf%2BUn8zJzmlPvc69tMVjFT5%2Bh61lD0yuGkJ3yxLsfQuUxJrwpvsBd6BcAiCYBurTxMspsn4T%2FVFQO38K6mmeG7sZFBmkBop90FpD%2BbyDXToHUFHVr7Mb3pCbw40%2B8uPbFh8gdJa0euT9KmNwibfwACP0RXr2iNUiz548HvwUb3V8iEr9p5YUVXfqYfItBjP7fqOemqfmlE%2BZ2oBDzgU5OHB%2Fiv3wPcMCRasA3ZanWirsXZ4%2BkE%2Fj9Z7vXpsA3HKvsh97zDXDNLe2prsFTkmnKe5E%2BcYF3ki%2BUFA71UPiJAZ%2BbOZKeKFGb9WnLensMEUFyTSEj3toyFcr7LgmSm8osN1OdSbsOkkcCPBDZ%2BKVtvx8qh%2FeUAHQJNDBZ360w2X2ipdoNNdCet2FzrDBi8sP2jMPn%2B4cQGOqUBaIn2UXop7%2F1K%2Bo4izCdwNPi5yGOTBQ7TbPTI8k0Qsx0XWSemb18zEaJcfxRUwHYRw3DO75iS9DQ%2BsitRDBh6p%2F45%2B6CnLBm89GRIUoNNSgNlxdx%2B0wWWnkespGrmRr9nNkWxRXFMWO9pj%2BfKNYUTJNmi1R%2Bqo3U7Zx8evBFbasopizJZfmMG8TAZUQ1%2Btz%2BKxtQW2V6UwK9NabpvGprD6kYaUzw1&X-Amz-Signature=e7f06813515bf8e68535ea964e246b5ee63e711bb74b8f440b1d70f849f7749f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 큰 배치는 더 쉬운 non-negative example을 가져옴 (난이도가 낮음.)

- cluster size를 감소시키는 것은 난이도를 높임.

**Which contextual documents help?**

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/58046fb2-3e6a-4832-bb2e-77f6fad43e5f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6B5Q7QS%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCbO9u9eQrPecO3%2BL4EzvKNHpcUQ3HacgUAZz7kN5m41QIgFb3u3CsY%2BgWpx6FKeZsMNthdT5AVmEUKKeHNWe3RWngqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNoIyA0eq143BmGPGCrcA9cfsKJnTILxA5eKojkSWz6SAS2112kPY%2BqKniB94yi6QcF8S2ju0prsmlywMVtZJ271BBsi4fe8t7RtSWtwEYfFYbNXHxYziAbiw8wT2DpHBtBsWnRXHff%2BlUcHUkuppUp%2FgxVV2znA6tT4gRU93nvLp0NkMd5puqaxNHM2W0TD%2FdcwTRmPN%2BhGwGmlgZk6zvY6Me%2BwNzZ9T%2BT6KFgDRBXT79mtk3pW7ELw7dDf%2BUn8zJzmlPvc69tMVjFT5%2Bh61lD0yuGkJ3yxLsfQuUxJrwpvsBd6BcAiCYBurTxMspsn4T%2FVFQO38K6mmeG7sZFBmkBop90FpD%2BbyDXToHUFHVr7Mb3pCbw40%2B8uPbFh8gdJa0euT9KmNwibfwACP0RXr2iNUiz548HvwUb3V8iEr9p5YUVXfqYfItBjP7fqOemqfmlE%2BZ2oBDzgU5OHB%2Fiv3wPcMCRasA3ZanWirsXZ4%2BkE%2Fj9Z7vXpsA3HKvsh97zDXDNLe2prsFTkmnKe5E%2BcYF3ki%2BUFA71UPiJAZ%2BbOZKeKFGb9WnLensMEUFyTSEj3toyFcr7LgmSm8osN1OdSbsOkkcCPBDZ%2BKVtvx8qh%2FeUAHQJNDBZ360w2X2ipdoNNdCet2FzrDBi8sP2jMPn%2B4cQGOqUBaIn2UXop7%2F1K%2Bo4izCdwNPi5yGOTBQ7TbPTI8k0Qsx0XWSemb18zEaJcfxRUwHYRw3DO75iS9DQ%2BsitRDBh6p%2F45%2B6CnLBm89GRIUoNNSgNlxdx%2B0wWWnkespGrmRr9nNkWxRXFMWO9pj%2BfKNYUTJNmi1R%2Bqo3U7Zx8evBFbasopizJZfmMG8TAZUQ1%2Btz%2BKxtQW2V6UwK9NabpvGprD6kYaUzw1&X-Amz-Signature=995f73ddbac9e3470c4e55e4f9cfe7188e4f52e871861ac580ebefb5bd28d7a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Contextual Documents 도메인을 다르게 해서 실험 진행. (Y-axis: input)

- NDCG 값이 기존 최고 점수와 1%p 이내의 경우, 하이라이트
