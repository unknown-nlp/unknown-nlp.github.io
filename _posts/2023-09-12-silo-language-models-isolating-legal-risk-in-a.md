---
categories:
  - paper-reviews
date: "2023-09-12 00:00:00"
description: "논문 리뷰 - LM, Retrieval, \bDomain Adaptation 관련 연구"
giscus_comments: true
layout: post
related_posts: false
tags:
  - "\bdomain adaptation"
  - language-model
  - llm
  - lm
  - paper-review
  - retrieval
thumbnail: assets/img/posts/2023-09-12-silo-language-models-isolating-legal-risk-in-a/thumbnail.jpg
title: "SILO LANGUAGE MODELS: ISOLATING LEGAL RISK IN A NONPARAMETRIC DATASTORE"
---

**논문 정보**

- **Date**: 2023-09-12
- **Reviewer**: 김재희
- **Property**: LM, Retrieval, Domain Adaptation

## 1. Intro

- Pretrained LM의 Domain Adaptation 능력을 평가

- 학습 데이터 및 Retrieve-and-Augment 방법론에 따라 Domain 별 성능 평가 진행

- 논문에서 제기하는 RQ : 저작권, 보안 이슈에서 자유로운 LLM을 학습/이용하는 상황을 가정할 때, Inference 성능 극대화할 수 있는 방법은 무엇일까?

{% include figure.liquid loading="eager" path="assets/img/posts/2023-09-12-silo-language-models-isolating-legal-risk-in-a/image_000.png" class="img-fluid rounded z-depth-1" %}

## 2. Problem Setup

1. 기존의 Pretrain Corpus 수집 방법 : 저작권에 대해 비교적 큰 신경 X

1. 최근의 Pretrain Corpus 수집 방법 : 법적 문제(저작권)에 자유로운 수집이 점차 부상하고 있는 문제점

## 3. Datasets & Pretrained Models

- PLM의 학습 도메인 or risk를 엄격히 통제하기 위해 다양한 버전의 데이터로 모델을 pretrain함

### 도메인 별 데이터셋

{% include figure.liquid loading="eager" path="assets/img/posts/2023-09-12-silo-language-models-isolating-legal-risk-in-a/image_001.png" class="img-fluid rounded z-depth-1" %}

- 각 도메인 별 copyright이 다양하게 분포

- 각 도메인 및 copyright 별 데이터 크기(BPE Tokens)가 다양

### Copyright 별 데이터셋

{% include figure.liquid loading="eager" path="assets/img/posts/2023-09-12-silo-language-models-isolating-legal-risk-in-a/image_002.png" class="img-fluid rounded z-depth-1" %}

- copyright 유형을 3가지로 구분

- 카피라이트 별 데이터 분포 특성 (재희)

### Pretrained LM

3가지 데이터 상황 별 LLM을 학습 및 평가 진행

- 모델 구조 : LLAMA 구조 그대로 활용

- 모델 크기 : 1.3B

- 비교 모델 : Pythia (PILE 데이터로 학습된 1.3B 모델)

- 모든 모델이 비슷한 Compute을 소요하여 훈련

### 모델 별 PPL 평가 결과

{% include figure.liquid loading="eager" path="assets/img/posts/2023-09-12-silo-language-models-isolating-legal-risk-in-a/image_003.png" class="img-fluid rounded z-depth-1" %}

- 파란색 : in-domain/노란색 : out-of-domain but trained on relevant data/빨간색 : out-of-domain

- in-domain : 모든 모델이 in-domain에서 우수한 성능을 보이고 있음

- 노란색 : out-of-domain임에도 완전한 ood(빨간색) 대비 좋은 성능을 보이는 모습

- MIMIC-III : 의료 도메인 데이터, 모든 모델의 성능이 좋지 못한 모습

**⇒ 학습 데이터와 평가 데이터 간의 n-gram overlap 지표와 ppl 지표가 매우 높은 상관관계(-0.72)를 보이고 있음**

**⇒ 학습 데이터와 평가 데이터 간의 Domain 일치 여부가 성능에 큰 영향을 미침**

{% include figure.liquid loading="eager" path="assets/img/posts/2023-09-12-silo-language-models-isolating-legal-risk-in-a/image_004.png" class="img-fluid rounded z-depth-1" %}

## 4. Augmented Methods

- OOD 도메인의 성능을 높이기 위해 KNN-LM과 Retrieval-In-Context LM (Augmented-LM, RIC LM) 두가지 방법론 이용

### KNN-LM

{% include figure.liquid loading="eager" path="assets/img/posts/2023-09-12-silo-language-models-isolating-legal-risk-in-a/image_005.png" class="img-fluid rounded z-depth-1" %}

- test 도메인의 훈련 데이터를 datastore로 설정하고, Retrieval과 생성을 Fusion하는 방법론

- 모델의 context vector를 key, 토큰을 value로 하여 생성 확률을 보정하는 방법론

- LM의 OOD 성능을 끌어올릴 수 있는 방법론으로 알려져 있음

- Retrival 과정에서 구해진 각 토큰과의 거리와 실제 모델의 생성 확률을 가중합하여 최종 생성확률 결정

Retrieval의 확률 변환 과정

{% include figure.liquid loading="eager" path="assets/img/posts/2023-09-12-silo-language-models-isolating-legal-risk-in-a/image_006.png" class="img-fluid rounded z-depth-1" %}

최종 생성 확률

{% include figure.liquid loading="eager" path="assets/img/posts/2023-09-12-silo-language-models-isolating-legal-risk-in-a/image_007.png" class="img-fluid rounded z-depth-1" %}

### RIC LM

- test 도메인의 훈련 데이터를 datastore로 설정하고, Retrieve된 text를 In-Context Learning으로서 활용하는 방법론

- Retriever : BM25, OOD Retrieval 시 가장 안정적인 성능을 보이는 방법론이기 때문에 선택한듯.

- ICL 시 사용되는 모든 M개의 Retrieved Text는 단순 concat을 통해 활용

## 5. Experiments

### Augmented Methods 적용 시 성능 변화

{% include figure.liquid loading="eager" path="assets/img/posts/2023-09-12-silo-language-models-isolating-legal-risk-in-a/image_008.png" class="img-fluid rounded z-depth-1" %}

- 기존 LLM에 Retrieval 모듈 추가 시 일관된 성능 향상 기록

- Pythia(In-Domain)과 성능 격차가 줄어드는 모습을 확인 가능

- 완전한 OOD(MIMIC-III) 의 경우에 더욱 큰 성능 향상을 기록하면서 Pythia보다 좋은 성능 기록

### Data Store 크기 별 성능 변화

- Data Store : Retrieval 대상이 되는 Train 데이터

- Data Store의 크기를 변화하면서 두 방법론의 성능 변화 관찰

- Data Store의 크기가 커질수록 성능이 향상되는 모습을 보임

- 일부 도메인에 대해서는 Pythia(In-Domain)보다 좋은 성능을 보이고 있음

- KNN이 RIC보다 거의 대부분 좋은 성능

### RIC vs KNN

- 두가지 가설 설정

- 1번 검증을 위해선 In-Domain에서 KNN이 RIC-LM보다 좋은 성능을 보여야함

- 2번 검증을 위해선 Datastore가 커질수록 KNN-LM의 성능 향상폭이 커야 함

### Retrieval을 통한 성능 향상 vs Retrieval을 통한 일반화 성능 향상

- 두가지 가설이 전체 성능 향상에 미치는 영향을 분석하기 위해 다음 실험 진행

- Retrieval와 LM으로 사용하는 모델을 달리하며 실험 진행

- 1번 (Pythia, Pythia) : Retrieval와 LM 모두 In-Domain인 경우에도 성능 향상을 보임

- 2번 (Pythia, Ours) : Retrieval는 OOD인 경우

- 3번 (Ours, Pythia) : LM만 OOD인 경우

- 4번 (Ours, Ours) : Retrieval와 LM 모두 OOD 인 경우

⇒ LM의 In-Domain 여부가 매우 중요한 요소

⇒ Retrieval 적용을 통한 성능 개선 역시 매우 뚜렷

⇒ 특히 OOD일 경우 Retrieval 적용을 통해 성능 개선 폭 뚜렷

⇒ 즉, Retrieval을 통한 성능 향상보다는 **Retrieval을 통한 일반화 성능 향상에 더 큰 비중이 있음. **

## 7. Conclusion

{% include figure.liquid loading="eager" path="assets/img/posts/2023-09-12-silo-language-models-isolating-legal-risk-in-a/image_009.png" class="img-fluid rounded z-depth-1" %}

### 민세원이 돌아왔구나…

- 사실 당연한 문제 상황이고, 당연한 결과물임

- 하지만 이를 저작권 문제와 결합시켜서 보다 엄밀한 문제 상황 제기

- k-NN은 근-본

- 민세원님 논문답게 분석과 워딩, 시각화가 무척 좋다…

- 결국 문제는 Retrieval을 언제 어떻게 결합하느냐…
