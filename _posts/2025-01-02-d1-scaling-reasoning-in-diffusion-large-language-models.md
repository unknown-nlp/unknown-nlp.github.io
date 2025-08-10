---
categories:
- paper-reviews
date: '2025-01-02 00:00:00'
description: 논문 리뷰 - DiffusionLM, SFT, Reinforcement Learning, Reasoning 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- diffusion
- diffusionlm
- language-model
- llm
- paper-review
- reasoning
- reinforcement learning
- reinforcement-learning
- sft
thumbnail: assets/img/posts/2025-01-02-d1-scaling-reasoning-in-diffusion-large-language-models/thumbnail.jpg
title: 'd1: Scaling Reasoning in Diffusion Large Language Models via Reinforcement
  Learning'
---

**논문 정보**
- **Date**: 2025-01-02
- **Reviewer**: 김재희
- **Property**: DiffusionLM, SFT, Reinforcement Learning, Reasoning

## 1. Intro

### 1.1 결론

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-02-d1-scaling-reasoning-in-diffusion-large-language-models/image_000.png" class="img-fluid rounded z-depth-1" %}

### 1.2 RL(GRPO)

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-02-d1-scaling-reasoning-in-diffusion-large-language-models/image_001.png" class="img-fluid rounded z-depth-1" %}

**특징: **

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-02-d1-scaling-reasoning-in-diffusion-large-language-models/image_002.png" class="img-fluid rounded z-depth-1" %}

- GRPO를 DDLM에 적용할 때 발생하는 문제점

### ⇒ 단순히 AR의 GRPO를 적용할 수 없음.

## 2. Method

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-02-d1-scaling-reasoning-in-diffusion-large-language-models/image_003.png" class="img-fluid rounded z-depth-1" %}

### 2.1 Mean Field Estimation

- 복잡한 상호작용을 가진 시스템의 기대값 계산을 단순화하기 위해 독립 확률 분포로 근사하는 방법론

- AR: 각 토큰의 생성이 이전 토큰에 종속적 

- DDLM: 각 토큰의 생성이 모든 다른 토큰에 종속적

### 2.1 Sequence-level Loglikelihood Estimation

- AR: 각 토큰의 loglikelihod로 분해 가능

- DDLM: 모든 토큰이 동시에 생성되어 적용 불가 

### 2.2 One-step Per-token loglikelihood estimation

- 기존 쿼리의 일부 토큰을 masking하고 전체 토큰의 loglikelihood를 그대로 사용

### 2.3 diffu-GRPO: Policy Gradient Optimization for Masked dLLMs

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-02-d1-scaling-reasoning-in-diffusion-large-language-models/image_004.png" class="img-fluid rounded z-depth-1" %}

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-02-d1-scaling-reasoning-in-diffusion-large-language-models/image_005.png" class="img-fluid rounded z-depth-1" %}

- 기존 GRPO와 다른 점: 쿼리의 일부 토큰을 masking

- 이외 점은 Mean Field Estimation을 통해 동일하게 구성됨 → 뭐여;;

- masking이 가져오는 이점

### 2.4 SFT

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-02-d1-scaling-reasoning-in-diffusion-large-language-models/image_006.png" class="img-fluid rounded z-depth-1" %}

- LLaDA에서 사용한 방식 그대로 활용

- 학습 데이터: s1K 데이터 사용

## 3. Experiments

### 3.0 Setup

- backbone: LLaDA-8B-Instruct, from scratch로 학습된 dLLM

- reward: correctness, formatting

- max len: 

### 3.1 Main 

- 각 데이터 별 별도 학습 진행 

- SFT와 diffu-GRPO의 효과 검증

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-02-d1-scaling-reasoning-in-diffusion-large-language-models/image_007.png" class="img-fluid rounded z-depth-1" %}

- SFT: 일부 지표에서 성능이 개선되는 모습을 보임

- diffu-GRPO: SFT보다 훨씬 큰 성능 개선을 **모든 지표**에서 보임

- SFT+diffu-GRPO: 최종적인 제안 방법론(d1)으로 훈련된 모델

### 3.2 Unified Model

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-02-d1-scaling-reasoning-in-diffusion-large-language-models/image_008.png" class="img-fluid rounded z-depth-1" %}

- 각각의 태스크로부터 동일한 크기의 데이터를 샘플링해서 함께 학습시키는 실험 세팅

- 놀랍게도 단일 모델보다 더 높은 성능을 달성

### 3.3 Code Domain

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-02-d1-scaling-reasoning-in-diffusion-large-language-models/image_009.png" class="img-fluid rounded z-depth-1" %}

- code domain에 대한 학습 및 평가 진행

- SFT: 오히려 성능이 떨어지는 모습을 보이고 있음

- diffu-GRPO: 바로 diffu-GRPO를 적용해도 성능이 대부분 개선되는 모습을 보임

### 3.4 beyond trained length

- 재밌는 현상은 rl 시 sampling max length가 256임에도 평가 시 512 토큰 생성시에 개선되는 모습을 보이는 점 (AR은 안 그런가…?)

- dLLM의 경우 학습 시 length에 overfit되지 않고 general reasoning strategy를 학습하는 것으로 보임

→ analysis 파트에서 계속

## 4. Analysis

### 4.1 Aha Moments

- 128,256의 길이 생성 시에는 aha moment가 보이지 않았음

- 512 길이를 생성시키자 aha moment 발현

### 4.2 Generation Length

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-02-d1-scaling-reasoning-in-diffusion-large-language-models/image_010.png" class="img-fluid rounded z-depth-1" %}

- max length를 달리하며 각 태스크별 생성 길이 측정

- (main) 학습된 길이(256)을 넘어 생성하여도 꾸준히 성능이 개선되는 모습을 보임

- Effective Tokens: 실제 생성된 sequence의 평균 길이 (AR과 다르게 max len 만큼 <mask>를 채워서 forwarding해서 이렇게 표현하나…?)

### 4.3 inner loop 횟수

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-02-d1-scaling-reasoning-in-diffusion-large-language-models/image_011.png" class="img-fluid rounded z-depth-1" %}

- prompt masking을 통해 inner loop 횟수를 증가시켜도 안정적인 학습 확인 가능

- inner loop iteration 동안 random하게 masking을 주는 것이 동일 masking보다 높은 성능 달성

- inner loop iteration을 늘리는 것이 실제 수렴 속도를 매우 빠르게 만듬

### 4.4 Masking Ratio

## 7. Conclusion

- Diffuion LM에서 RL을 위해 필요한 요소들을 잘 정의함

- 매우 단순하게 해결하여 성능 개선을 이끌어냄

- Diffusion LM의 RL 시 현상들에 대해 (거의) 최초로 분석한 논문

- scale이 너무 작아서 조금 더 큰 실험들에 대해 궁금하다.
