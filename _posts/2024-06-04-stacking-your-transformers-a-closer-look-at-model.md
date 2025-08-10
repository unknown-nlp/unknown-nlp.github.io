---
categories:
- paper-reviews
date: '2024-06-04 00:00:00'
description: "논문 리뷰 - LLM, \bPre-Training 관련 연구"
giscus_comments: true
layout: post
related_posts: false
tags:
- "\bpre-training"
- llm
- paper-review
- pre-training
- transformer
thumbnail: assets/img/posts/2024-06-04-stacking-your-transformers-a-closer-look-at-model/thumbnail.jpg
title: 'Stacking Your Transformers: A Closer Look at Model Growth for Efficient LLM
  Pre-Training'
---

**논문 정보**
- **Date**: 2024-06-04
- **Reviewer**: 김재희
- **Property**: LLM, Pre-Training

## 1. Intro

- TL;DR

- Related Works

## 2. Expansion Method 비교 실험

### Expansion methods

{% include figure.liquid loading="eager" path="assets/img/posts/2024-06-04-stacking-your-transformers-a-closer-look-at-model/image_000.png" class="img-fluid rounded z-depth-1" %}

- 총 4가지 파라미터 확장 방법론을 실험 대상으로 선정, dimension: (in, out)

1. vertical stacking: 학습된 작은 모델의 weight를 복사하여 초기값으로 활용

1. learnable expansion(G_learn): 학습된 작은 모델의 weight matrix에 대한 learnable parameter를 도입하여 확장된 weight matrix를 학습하는 방법론

1. zero init(G_zero): weight matrix의 파라미터 확장 시 random과 init을 함께 활용하는 방법론

1. random init(G_random): weight matrix의 파라미터 확장 시 모든 weight를 random으로 init하는 방법론

ffnn layer

- (d_model, d_model*4)

- relu

- (d_model*4, d_model)

### Training Small Model

- 초기 모델 학습 → expansion method를 적용하여 larger model 추가학습 진행

- 400M → Expansion Method → 1.1B (107.5B token)

- larger model 학습

- from scracth 모델 학습

### 실험 결과 

{% include figure.liquid loading="eager" path="assets/img/posts/2024-06-04-stacking-your-transformers-a-closer-look-at-model/image_001.png" class="img-fluid rounded z-depth-1" %}

- speed-up: scratch 모델과 동일 성능 도달을 위해 필요한 연산량(FLOPS)

- G_direct(up): 학습 속도 및 성능 측면 모두에서 타 방법론 및 scratch 성능 능가

- vertical stacking 방법론이 horizontal stacking 방법론보다 높은 성능 달성

- vertical stacking 시 zero가 random보다 높은 성능 달성

## 3. Delving Deeper Into Vertical Stacking

### growth factor(g)

- 기본 모델 M이 주어져 있을 때, stacking 횟수 인자

- Vertical Stacking이 가장 성능이 좋은 것으로 나타났음

### Scaling Model Size

- 3B와 7B larger model을 타겟으로 실험 진행

- 각각 (0.75B, 1.75B)를 가지는 기본 모델 훈련 진행 (w/ 10B token)

### 실험 결과

{% include figure.liquid loading="eager" path="assets/img/posts/2024-06-04-stacking-your-transformers-a-closer-look-at-model/image_002.png" class="img-fluid rounded z-depth-1" %}

- 3B

### Longer Train vs Scaling Effect

- Stack의 효과가 아니라, 단순하게 token을 더 많이 써서 학습해서 성능이 오른 것일수도 있음

- 400M 모델을 이용하여 410M vs 840M(410M 모델 stacking) 모델 간의 성능 차이 관찰

- 꾸준한 성능 차이 관찰

## 4. Scaling Law

### Toy Plotting

- 총 4개의 모델 학습 진행

- Chinchilla Scaling Law를 이용하여 Loss curve에 대한 fitting 시도

- 기존 Chinchilla Scaling Law 대비 Stack이 더 효율적으로 성능 개선이 가능함을 보임

## 7. Scaling Law

### Scaling Factor

- 기존의 데이터수 D, 연산량 N 이외에도 두가지 factor가 존재

- stacking 시점 d

- stacking 횟수 g

### Stacking 시점 d

{% include figure.liquid loading="eager" path="assets/img/posts/2024-06-04-stacking-your-transformers-a-closer-look-at-model/image_003.png" class="img-fluid rounded z-depth-1" %}

- stacking 횟수를 4로 고정하고 실험

### Stacking 횟수 g

{% include figure.liquid loading="eager" path="assets/img/posts/2024-06-04-stacking-your-transformers-a-closer-look-at-model/image_004.png" class="img-fluid rounded z-depth-1" %}

- 1.1B 모델과 3B의 base model을 이용하여 stacking 횟수를 달리하며 실험 진행

- 실험결과 모델 크기에 따라 차이가 존재

- 연산량에 따른 차이는 존재 X
