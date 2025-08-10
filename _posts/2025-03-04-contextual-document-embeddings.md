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

{% include figure.liquid loading="eager" path="assets/img/posts/2025-03-04-contextual-document-embeddings/image_000.png" class="img-fluid rounded z-depth-1" %}

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

{% include figure.liquid loading="eager" path="assets/img/posts/2025-03-04-contextual-document-embeddings/image_001.png" class="img-fluid rounded z-depth-1" %}

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

{% include figure.liquid loading="eager" path="assets/img/posts/2025-03-04-contextual-document-embeddings/image_002.png" class="img-fluid rounded z-depth-1" %}

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

{% include figure.liquid loading="eager" path="assets/img/posts/2025-03-04-contextual-document-embeddings/image_003.png" class="img-fluid rounded z-depth-1" %}

- Archictecture에서도 Contextual을 넣는 것이 일반적으로 더 좋았음.

# Analysis

**How hard are our clusters?**

{% include figure.liquid loading="eager" path="assets/img/posts/2025-03-04-contextual-document-embeddings/image_004.png" class="img-fluid rounded z-depth-1" %}

- 큰 배치는 더 쉬운 non-negative example을 가져옴 (난이도가 낮음.)

- cluster size를 감소시키는 것은 난이도를 높임.

**Which contextual documents help?**

{% include figure.liquid loading="eager" path="assets/img/posts/2025-03-04-contextual-document-embeddings/image_005.png" class="img-fluid rounded z-depth-1" %}

- Contextual Documents 도메인을 다르게 해서 실험 진행. (Y-axis: input)

- NDCG 값이 기존 최고 점수와 1%p 이내의 경우, 하이라이트
