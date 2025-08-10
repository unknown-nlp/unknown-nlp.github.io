---
categories:
  - paper-reviews
date: "2024-04-13 00:00:00"
description: 논문 리뷰 - LM, LLM, Efficient Training, Pre-training 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
  - efficient training
  - language-model
  - llm
  - lm
  - neural
  - paper-review
  - pre-training
  - vision
thumbnail: assets/img/posts/2024-04-13-scaling-laws-for-data-filtering-data-curation-cannot/thumbnail.jpg
title: "Scaling Laws for Data Filtering—

  Data Curation cannot be Compute Agnostic"
---

**논문 정보**

- **Date**: 2024-04-13
- **Reviewer**: yukyung lee
- **Property**: LM, LLM, Efficient Training, Pre-training

https://arxiv.org/abs/2404.07177

# tl;dr

{% include figure.liquid loading="eager" path="assets/img/posts/2024-04-13-scaling-laws-for-data-filtering-data-curation-cannot/image_000.png" class="img-fluid rounded z-depth-1" %}

**(a) The Dynamic Problem of Data Filtering**

**(b) Scaling laws for data filtering**

## 0. Abstract

- Vision-language model을 학습할 때 carefully curated web data를 활용하여 매우 오랜시간동안 훈련됨 (trained for thousands of GPU hours)

- Data curation은 raw scraped data로 부터 high-quality 데이터의 subset을 보존하는 방식으로 발전해옴 - LAION 데이터의 경우 10%의 데이터만 보존함

- 하지만 이러한 전략들은 일반적으로 사용할 수 있는 training compute를 고려하지 않고 개발됨

- 본 논문에서는 training compute와 독립적으로 filtering에 대한 결정을 내리는것이 suboptimal하다는 것을 지적

- QQT를 다루기 위해, 기존 문헌에서 간과된 web data의 homogeneous nature를 고려한 neural scaling law를 소개함

- 제안하는 scaling law는

- 제안하는 scaling law는 다양한 compute에서 최고의 성능을 달성하기 위해 최적의 data pool을 큐레이션할 수 있게 함

## 1. Introduction

- Foundation model pre-training을 더 많은 데이터 / compute / parameter로 scaling up 하는 것은 ML community에 high-performing model을 제공해주었음

- 기존 연구들은 neural scaling law에 따라서 예측된 model performance의 향상 가능성에 따라 scale up을 결정하는 것에 포커스 맞추어옴

- 최근에는 “data”가 closed model의 성능 향상에 영향을 주는 secret source로 받아들여지고 있음

- Web data는 방대하지만 high quality data는 한정되어 있음

- 해당 논문에서는 limited high quality data와 대량으로 활용할 수 있는 low quality data의 trade off를 고려하여 scaling law를 결정 — **_quality-quantity tradeoff (QQT)_**

{% include figure.liquid loading="eager" path="assets/img/posts/2024-04-13-scaling-laws-for-data-filtering-data-curation-cannot/image_001.png" class="img-fluid rounded z-depth-1" %}

- Data curation 과정에서 compute를 고려해야 함

## 2. Related Work

이 부분은 Introduction과 겹치는 부분이 많아서 발표에서 제외

- data filtering에 대한 기존 방법론

- lm / downstream task / CLIP에서의 scaling law를 설명하고 있음

## 3. Data Filtering for a Compute Budget

### 1) Experimental setup

- VLM (CLIP)을 학습하기 위해 large initial pool이 준비되어 있음을 가정

- 다양한 compute budget에서의 data filtering 효과를 확인하고자 함

아래의 종류로 구분된 setting을 가짐

- base unfiltered pool: medium scale — Datacamp 벤치마크 사용

### 2) When “good” data performs worse

- (start from) LAION 필터링 전략을 사용하여 LAION 데이터셋을 얻음.

- Good data is better at low compute budget

- Data filtering hurts at high compute budget

### 3) Data filtering must be compute-aware

{% include figure.liquid loading="eager" path="assets/img/posts/2024-04-13-scaling-laws-for-data-filtering-data-curation-cannot/image_002.png" class="img-fluid rounded z-depth-1" %}

- 2)를 통해 LAION filtering은 compute budget이 증가할수록 gain이 줄어듦을 알 수 있었음

- 이 현상은 LAION 필터링 방법에만 해당하는 것이 아니라 반복된 샘플의 utility가 감소한다는 저자들의 직관과도 동일함

- CLIP 점수 필터링과 T-MARS 방법을 포함한 최신의 데이터 필터링 방법들의 성능을 다양한 컴퓨트 예산에서 분석 진행함

## 4. Scaling Laws for Data Filtering

### 1) Utility 정의

- scaling law에 대한 기존 연구들은 n개의 샘플로 학습한 후의 모델 오차를 y = an^b + d로 추정함

{% include figure.liquid loading="eager" path="assets/img/posts/2024-04-13-scaling-laws-for-data-filtering-data-curation-cannot/image_003.png" class="img-fluid rounded z-depth-1" %}

### 2) 반복에 대한 Utility

- CLIP 스타일의 사전학습은 동일한 데이터에 대해 여러 epoch 동안 수행되나, 샘플이 여러번 반복될 때 utility의 변화에 대한 이해는 부족함

- 샘플이 학습에 등장하는 횟수에 따라 utility가 지수적으로 감소한다는 것을 가정함

{% include figure.liquid loading="eager" path="assets/img/posts/2024-04-13-scaling-laws-for-data-filtering-data-curation-cannot/image_004.png" class="img-fluid rounded z-depth-1" %}

- k번씩 n개 샘플을 본 후의 모델 손실에 대한 closed form은 아래와 같음

{% include figure.liquid loading="eager" path="assets/img/posts/2024-04-13-scaling-laws-for-data-filtering-data-curation-cannot/image_005.png" class="img-fluid rounded z-depth-1" %}

- summary of parameter

### 3) The case of heterogeneous web data

- 서로 다른 품질의 데이터가 존재하는 경우에 대한 논의

- web data는 일반적으로 다양한 subset으로 분할될 수 있으며, 각각의 subset은 고유한 parameter들을 가짐 (utility parameter들을 의미)

- 대규모 학습은 여러개의 data bucket의 조합에 대해 수행됨

- 어떻게 효과적으로 데이터 믹스의 손실을 추정할 수 있을까?

Theorem 1.

- p개의 데이터 pool S_1^n . . . S_p^n이 무작위로 균일하게 샘플링되었을 때, 각각의 utility 및 반복 파라미터가 (b_1, τ_1) . . . (b_p, τ_p)로 주어진다면, 각 bucket의 새로운 repetition half-life 는 τ̂ = p · τ

- 추가로 k번째 반복에서 조합된 pool의 utility 값 b\_(eff)^((k))는 개별 utility 값의 가중 평균

{% include figure.liquid loading="eager" path="assets/img/posts/2024-04-13-scaling-laws-for-data-filtering-data-curation-cannot/image_006.png" class="img-fluid rounded z-depth-1" %}

## 5. Fitting scaling curves for various data utility pool

Experiment setting

- 128M image-caption pair로 구성된 DataComp medium 사용

- T-MARS, CLIP score를 활용하여 data들의 utility 추정치로 사용하고 이를 기준으로 web 데이터를 순위 매김

## 6. Results: Estimating the Scaling Laws for

Data Combinations under QQT

- section 5에서는 다양한 quality의 pool에 대해 각각의 parameter를 도출했음

- section 6의 목표는 주어진 학습 compute에 대해 가장 효과적인 데이터 큐레이션 전략을 결정하는 것

- Fig 5 / 10은 ImageNet에서의 성능을 평가하여 서로 다른 데이터 조합에 대한 scaling curve를 보여줌

{% include figure.liquid loading="eager" path="assets/img/posts/2024-04-13-scaling-laws-for-data-filtering-data-curation-cannot/image_007.png" class="img-fluid rounded z-depth-1" %}

- 이전 연구들에서는 다양한 크기의 ViT 모델을 다양한 크기의 data pool로 학습함

- 이전 연구의 저자들이 제안 했던 방식(fit scaling laws)은 small dataset을 학습한 경우 매우 높은 error를 보였음

- 따라서 논문의 저자들은 이전 연구의 모델들에 본 논문의 scaling law를 적용하여 성능을 예측하였음

- Figure 6:

## 7. Conclusion

- scaling curve 자체를 fitting하여 data curation을 할 수 있는 전략을 제안함

- compute power에 따라 적절한 data curation을 진행해야 한다는 점을 보여줌
