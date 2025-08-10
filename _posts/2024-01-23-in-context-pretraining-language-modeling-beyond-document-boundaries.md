---
categories:
  - paper-reviews
date: "2024-01-23 00:00:00"
description: 논문 리뷰 - ICL, LLM, In Context Learning 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
  - icl
  - in context learning
  - language-model
  - llm
  - paper-review
thumbnail: assets/img/posts/2024-01-23-in-context-pretraining-language-modeling-beyond-document-boundaries/thumbnail.jpg
title: "IN-CONTEXT PRETRAINING: LANGUAGE MODELING BEYOND DOCUMENT BOUNDARIES"
---

**논문 정보**

- **Date**: 2024-01-23
- **Reviewer**: 김재희
- **Property**: ICL, LLM, In Context Learning

## 1. Intro

- Pretrain 단계에서 In-Context Learning을 반영할 수 있지 않을까?

- Pretrain 시 ICL 데이터 구축 방식

- ICL Pretrain 시 성능 변화

### 기존 Pretrain

- 학습 효율을 위해 Batch 내 Maximum Length를 맞추는 전략을 취함

- 이러한 전략은 랜덤한 Demonstration을 추가하여 Pretrain을 진행하는 방식

### ICL Pretrain

- ICL을 Pretrain 단계(Next Token Prediction)에 활용하기 위해서는 아래 사항 고려 필요

- Pretrain 단계이기 때문에 시간/메모리 소모가 적으면서 양질의 Demonstration 탐색 방법론 필요

## 2. Method

### Overview

- Pretrain Batch 구성 방식 외 다른 요소는 기존 LLM과 동일

- Common Crawl 데이터를 이용하여 Pretrain 진행

- Pretrain Data를 Chunk 단위로 분리

- 제안 방법론을 이용하여 유사한 데이터를 하나의 Pretrain Sample로 Concat하여 구성

- Pretrain!

### 제안 방법론

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-23-in-context-pretraining-language-modeling-beyond-document-boundaries/image_000.png" class="img-fluid rounded z-depth-1" %}

1. Finding Related Documents at Scale

1. Creating Input Contexts

1. 제안 방법론대로 Input을 구성할 경우 최대한 유사한 내용을 담은 문서들이 하나의 Input으로 구성될 수 있음

## 3. Experiments

### Setup

- Model Size : 0.3/0.7/1.5/7B

- Model Architecture : LLaMA, 기타 Hyperparam도 LLaMA를 따름

- Hardware : 128 A100

- Pretrain 소요 시간 : 7B 기준 9일

- 3가지 조건에 따라 Scratch부터 Pretrain 진행

- Search

### Results

1. Language Modeling : LM의 기본적인 성능 평가 (PPL)

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-23-in-context-pretraining-language-modeling-beyond-document-boundaries/image_001.png" class="img-fluid rounded z-depth-1" %}

- kNN은 Standard 대비 성능 저하 관찰

- 모델 크기, 데이터 종류와 관계없이 일관된 모습

- 이와 대조적으로 ICLM은 성능 개선 관찰

2. In Context Learning

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-23-in-context-pretraining-language-modeling-beyond-document-boundaries/image_002.png" class="img-fluid rounded z-depth-1" %}

- 두가지 태스크에 대한 ICL 능력 평가

3. Retrieval-Augmentation

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-23-in-context-pretraining-language-modeling-beyond-document-boundaries/image_003.png" class="img-fluid rounded z-depth-1" %}

- 최근들어 매우 중요해진 분야

- Closed : 성능 개선 X

- Open : 뚜렷한 성능 개선 관찰 가능

4. Factuality

## 4. Analysis

### Train Dynamics

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-23-in-context-pretraining-language-modeling-beyond-document-boundaries/image_004.png" class="img-fluid rounded z-depth-1" %}

- Loss는 초반부터 Standard부터 낮은 모습

- 학습 중 Downstream Task 성능

### Ablation and K-shot

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-23-in-context-pretraining-language-modeling-beyond-document-boundaries/image_005.png" class="img-fluid rounded z-depth-1" %}

- Ablation Study :

- K-Shot

## 7. Conclusion

- 엄격한 실험 환경 제한을 통해 효과적인 실험 수행

- Pretrain 시 비용이 (상대적으로) 매우 적은 Input 구성 방법론 제안

- ICLM의 In-Context Learning/RAG/Document 필요 태스크(QA) 등에서 높은 성능

- 모델 크기 및 태스크와 관계없이 꾸준히 높은 성능 리포팅

- 매우 다양한 Downstream Task에 대한 성능 리포팅을 통한 신뢰도 확보

- 참 말을 잘한다…

### Future Works

- Domain/Corpus 단위의 Relevant Document 수집 방법론

- Multilingual Retriever를 통한 언어별 Input 구성 방법론
