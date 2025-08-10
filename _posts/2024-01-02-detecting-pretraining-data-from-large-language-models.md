---
categories:
  - paper-reviews
date: "2024-01-02 00:00:00"
description: 논문 리뷰 - LLM 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
  - detection
  - gpt
  - language-model
  - llm
  - paper-review
thumbnail: assets/img/posts/2024-01-02-detecting-pretraining-data-from-large-language-models/thumbnail.jpg
title: DETECTING PRETRAINING DATA FROM LARGE LANGUAGE MODELS
---

**논문 정보**

- **Date**: 2024-01-02
- **Reviewer**: 김재희
- **Property**: LLM

## 1. Intro

### Pretrain Data Detection

- LLM 활용에 있어 Pretrain Data Detection 필요성

### Membership Inference Attack (MIA)

- 특정 데이터에 대해 대상 모델의 학습 여부를 Inference 과정을 통하여 탐색하는 분야

- LLM에 대한 기존 방법론 적용의 어려움

## 2. WikiMIA : A Dynamic Evaluation Benchmark

- WimiMIA : LLM MIA 태스크를 위한 Benchmark 데이터셋 구축 및 공개

## 3. Proposed Methods : MIN-K% Prob

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-02-detecting-pretraining-data-from-large-language-models/image_000.png" class="img-fluid rounded z-depth-1" %}

### 가정

> 학습 때 사용되지 않은 데이터에 대해 inference 한다면 이상 단어(outlier words)를 포함하고 있으므로, 낮은 생성 확률을 가지고 있을 것이다.

- 매우 단순하고 직관적인 아이디어를 기반으로 각 샘플 당 Non-Member(pretrain 때 사용되지 않은 데이터)일 Score 산출

### 수식

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-02-detecting-pretraining-data-from-large-language-models/image_001.png" class="img-fluid rounded z-depth-1" %}

- 각 토큰 생성 확률의 평균

- 해당 스코어에 대한 Thresholding을 통해 MIA 태스크 수행 가능

## 4. Experiments 1 - Main

### Implementation Details and Setup

- WikiMIA 데이터에 대한 성능 리포팅

- Validation Set에 대해 Top-K Search → 20이 Best Hyperparam, 데이터셋별 tune 없이 고정하여 사용

- AUC 점수를 reporting하여 별도의 threshold 고정 X

### Result

- 타 방법론 대비 가장 높은 탐지 성능 기록

- 제안 방법론 유효성 입증

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-02-detecting-pretraining-data-from-large-language-models/image_002.png" class="img-fluid rounded z-depth-1" %}

### Analysis

- 평가 데이터 길이 및 모델 크기에 따른 성능 변화

- 모델 크기

- 데이터 길이

## 5. Experiments 2 - Detecting Copyrighted Books in Pretraining Data

### 개요

- LLM이 학습 데이터 내 copyright 문제가 있는 데이터 포함 여부 탐지 성능 측정

- 별도의 평가 데이터셋 구축

- GPT-3 내 저작권 이슈 데이터 확인

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-02-detecting-pretraining-data-from-large-language-models/image_003.png" class="img-fluid rounded z-depth-1" %}

- 왼쪽 : 평가 데이터에 대한 판별 성능(AUC)

- 오른쪽 : GPT-3의 저작권 이슈가 있는 데이터 학습 정도

## 6. Experiments 3 - Detecting Downstream Dataset Contamination

### 개요

- Downstream Task 데이터에 대한 학습 여부 탐지 성능 실험

- 모델 : LLaMA 7B

- 실험 방법 : 의도적으로 Downstream Task 데이터를 포함하는 Pretrain Corpus 구축 및 Continual Learning(Pretrain) 진행

### Result

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-02-detecting-pretraining-data-from-large-language-models/image_004.png" class="img-fluid rounded z-depth-1" %}

- 1 epoch만 학습되었음에도 86이상의 성능 리포팅

### Additional Experiments

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-02-detecting-pretraining-data-from-large-language-models/image_005.png" class="img-fluid rounded z-depth-1" %}

- 전체 pretrain corpus 크기에 따른 실험

- Corpus 내 Membership data 빈도에 따른 실험

- Learning Rate에 따른 실험

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-02-detecting-pretraining-data-from-large-language-models/image_006.png" class="img-fluid rounded z-depth-1" %}

## 7. Conclusion

### Summary

- LLM의 학습 데이터를 inference를 통해 판별하는 방법론 및 벤치마크 데이터셋 제안

- LLM의 Memorization 성능이 매우 강력하고 이를 통해 Detection이 쉬워지는 경향성 포착

- 단순히 PPL 등을 이용하기 보다는 Lowest K%를 이용하는 방법론의 유효성 입증

- Downstream Task Dataset과 Pretrain Corpus 데이터셋 간의 다른 경향성 포착

### Pros & Cons

- 요새 많이 주목받는 LLM Pretrain Corpus 분석 관련 연구

- 연구 주제 및 Research Question 설정이 매우 구체적임

- LLM의 Pretrain Corpus를 확신할 수 없는 상황에서 효율적/효과적 실험 환경 설정

- LLM의 Memorization 현상에 대한 향후 연구가 더 필요해 보임
