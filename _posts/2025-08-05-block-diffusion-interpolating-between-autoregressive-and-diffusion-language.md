---
categories:
- paper-reviews
date: '2025-08-05 00:00:00'
description: 논문 리뷰 - DiffusionLM, LLM 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- attention
- diffusion
- diffusionlm
- language-model
- llm
- paper-review
- transformer
thumbnail: assets/img/posts/2025-08-05-block-diffusion-interpolating-between-autoregressive-and-diffusion-language/thumbnail.jpg
title: 'BLOCK DIFFUSION: INTERPOLATING BETWEEN AUTOREGRESSIVE AND DIFFUSION LANGUAGE
  MODELS'
---

**논문 정보**
- **Date**: 2025-08-05
- **Reviewer**: 상엽
- **Property**: DiffusionLM, LLM

## Introduction

**Diffusion 모델이 가진 한계점**

1. 현재 대부분의 diffusion 모델의 경우 **고정된 길이의 답변**만을 생성.

1. Bidirectional context를 사용하기 때문에 **KV 캐시와 같이 AR 추론에서 효율적인 방법들을 사용할 수 없음**.

1. Standard metric (e.g. perplexity)에서 **여전히 낮은 성능**을 보임.

→ **Block Discrete Denoising Diffusion Language Models (BD3-LMs)**

**BD3-LMs**

Interpolation between discrete diffusion and autoregressive model

- Block diffusion model: semi-autoregressive model

- **Inter-Block**: Block을 생성하는 과정은 AR 과정으로 모델링

- **Intra-Block**: 이전 block이 주어질 경우, 현재 block 내부는 discrete diffusion 과정으로 모델링

**Block Diffusion 모델이 가진 Two challenges를 발견: 핵심!!**

- Block diffusion을 학습하기 위해서 두 번의 forward pass가 필요함. → 계산량 증가

- 높은 gradient variance로 인한 성능 저하

→ 지금은 이해가 어려우니 뒤에서 확인

**Contribution**

- Block discrete diffusion language model 제안. **기존 diffusion 모델과 달리 variable-length generation과 KV caching을 지원**

- 학습 시 토큰 배치를 효율적으로 활용할 수 있도록 block diffusion model을 위한 **훈련 알고리즘 제안** (Challenge 1)

- Gradient variance가 diffusion 모델 성능의 제한 요소임을 밝힘 + 데이터 기반 **노이즈 스케줄**로 해결 (Challenge 2)

- **성능 향상**!

{% include figure.liquid loading="eager" path="assets/img/posts/2025-08-05-block-diffusion-interpolating-between-autoregressive-and-diffusion-language/image_000.png" class="img-fluid rounded z-depth-1" %}

## BACKGROUND: LANGUAGE MODELING PARADIGMS

### **notation**

- scalar discrete random variables with V categories as ‘one-hot’ column

- \Delta^V: simplex 공간

- m \in \mathcal{V}: [MASK] token’s one-hot vector

### **AUTOREGRESSIVE MODELS**

### **DISCRETE DENOISING DIFFUSION PROBABILISTIC MODELS (D3PM)**

- p: denoising, q: noising

- s(j) = (j-1)/T, t(j) = j/T (이후에 j는 생략!)

- D3PM framework: q를 Markov forward process, 각각의 토큰에 대해 독립적으로 아래의 식을 진행

- 이상적인 diffusion model p_{\theta}는 q의 역방향이므로 D3PM에서는 아래 수식으로 p_{\theta}를 정의

- **Negative ELBO (NELBO)를 이용해 학습**

- 1, 2항: noise, denoise 과정에서의 샘플의 일치 정도

- 3항 얼마나 noise를 잘 만들었는가

## BLOCK DIFFUSION LANGUAGE MODELING

### BLOCK DIFFUSION DISTRIBUTIONS AND MODEL ARCHITECTURES

**Block Definition**

- 길이 L'이 되게 B개의 block으로 만들기 (x^b: x^{(b-1)L':bL'} \in \{1,...,B\})

- Likelihood over block

block 내에서 reverse diffusion 프로세스 적용

- block이 constraint인 것을 제외하면 preliminaries의 수식과 동일!

**Learning Objective**

NELBO를 적용해 위와 같이 학습 목적함수 정의, 이것도 Sum을 제외하곤 전부 같음!

**Denoiser model**

- Transformer x_\theta를 사용해 파라미터화: p_\theta(x^b | x_t^b, x^{<b})

- Block들에 대해 병렬적 학습을 가능하게 함 (block-causal attention mask)

- x_\theta의 학습: block b 내에서 x_\theta^b(x_t^b, x^{<b}) → L' 길이의 결과 예측

→ 아래 K, V 캐시 수식을 보시면 모델을 이해하기 쉬움!

**K, V caching**

- recomputing을 막기 위한 block 단위 caching

### EFFICIENT TRAINING AND SAMPLING ALGORITHMS

**Training**

- 모든 block은 x_\theta의 forward pass를 두 번 거쳐야 함 (x_t^b, x^b) → 계산의 효율화 필요

{% include figure.liquid loading="eager" path="assets/img/posts/2025-08-05-block-diffusion-interpolating-between-autoregressive-and-diffusion-language/image_001.png" class="img-fluid rounded z-depth-1" %}

1. Block 별로 noise level sampling

1. 각 block에 대해 noisy input x_{t_b}^b 생성

1. \left(\emptyset, \mathbf{K}^{1: B}, \mathbf{V}^{1: B}\right) \leftarrow \mathbf{x}_\theta(\mathbf{x}): 원본 x를 이용해 K, V cache 미리 다 계산하기

1. 모든 b에 대해 x^b_{\text{logit}} 계산

**Sampling**

{% include figure.liquid loading="eager" path="assets/img/posts/2025-08-05-block-diffusion-interpolating-between-autoregressive-and-diffusion-language/image_002.png" class="img-fluid rounded z-depth-1" %}

- Block 단위의 순차적 샘플링, K, V 캐싱 가능 ← AR의 장점

- arbitrary length 생성 가능 ← AR의 장점

- block 내부에선 Parallel하게 생성 가능 ← Diffusion의 장점

## UNDERSTANDING LIKELIHOOD GAPS BETWEEN DIFFUSION & AR MODELS

### MASKED BD3-LMS

- 최근 가장 큰 효과를 보이고 있는 masking noise process를 적용

- Per-token noise process 

- 목적 함수 (Sahoo et al. (2024b)의 SUBS-parameterization denoising 모델 철학을 따름!!)

### CASE STUDY: SINGLE TOKEN GENERATION

- L^\prime = 1인 경우, MASKED BD3-LMS의 목적함수는 autoregressive NLL과 동등함.

- 학습 목표의 기대값이 같음에도 불구하고 perplexity gap (=높은 학습 variance)가 존재함을 확인

- 왜 그럴까?  \mathbb{E}_{t\sim\mathcal{U}[0,1]}q(x_t^\ell=m|x^\ell) = 0.5 기본적으로 학습에 사용하는 token의 수가 절반으로 줄기 때문에 variance가 커지는 것

{% include figure.liquid loading="eager" path="assets/img/posts/2025-08-05-block-diffusion-interpolating-between-autoregressive-and-diffusion-language/image_003.png" class="img-fluid rounded z-depth-1" %}

- tuned schedule: q(x_t^\ell = m | x^\ell) = 1

### DIFFUSION GAP FROM HIGH VARIANCE TRAINING

- Case study를 넘어 L^\ell \geq 1인 케이스로 확장하고 싶음!

- Batch size를 K라고 할 때, batch of sequence \text{X} = [x^{(1)},x^{(1)},...,x^{(K)}], with each \text{x}^{(k)} \overset{\text{iid}}{\sim} q(x)

- **NELBO estimator**

- **Variance of the gradient estimator**
