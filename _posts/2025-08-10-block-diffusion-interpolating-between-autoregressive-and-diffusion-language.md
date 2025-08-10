---
categories:
  - paper-reviews
date: "2025-08-10 00:00:00"
description: 논문 리뷰 - DiffusionLM, LLM 관련 연구
giscus_comments: true
layout: post
related_posts: false
slug: 2025-08-10-block-diffusion-interpolating-between-autoregressive-and-diffusion-language
tags:
  - attention
  - diffusion
  - diffusionlm
  - language-model
  - llm
  - paper-review
  - transformer
title: "BLOCK DIFFUSION: INTERPOLATING BETWEEN AUTOREGRESSIVE AND DIFFUSION LANGUAGE
  MODELS"
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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/45b8f6de-b2b2-47cc-ac8b-8d268aa97e24/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R27ZVFKX%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGh3%2FVK8MxTZGWx8EIBPmzCC5B9Ex0Tk3YZUSo3qieJ0AiAF76nYDUcXmMJxHcjpA3wWo6J0DMA7AzOJDqmdCd1GdiqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6vTN%2FFvE7Q0qm3efKtwDoyRuNj8qCRSyr1D14k3QpH06%2BTqB1NJDMawNN%2Fd3eftUsqQMWsBUHlPW4fS7IZjzzsxfXyzTywvEGNXzOacqhROjhhqwIEHcQmuEzva%2Fq7sr93JFgFylhZNH5i6030B31Xrmy3QhFWx1ox%2BHmqyBwEvDp5fgDc3y0obpigKNRXJdQPnqk5BfkjeY%2B4z3pjbi9EzidjaW0Tgq5NWsoYiP%2BCql12BhwLFqnitpfIgAfwUIW1ga54TNzkYtm8BZIO3kA8BfobLJqGKsJ535ZeoBwII9VygJkhQVuQK7ToFr0re9yRxYUIjvu2wCZK7L89QVMHmGa1hWE1CD6zMz2RJziMDhNLOD2cbT%2BMaRDzP0ubhCrMQP5p5s7Fu6FhwOvKyh7xE0x3UUB6WgAI95izKGjf9nYb2gu1dufZ5iHcCUUcmErlAvM2fuPeZrNrw5zgHt6MTeJvU0T9XRCFrpT%2FM3cv8ZMfLPovzSSqm12eqSIQQCY1u%2BEkggeiklKUmowkQZIybTZfL2NiUVbRvsL6%2FsXCfY4iG%2BfCSl9kV4XQktZ7rgyzeiVBfsqM58ss1RtYvgohtBnEPkNbLMA%2FEDWXjlAwH29dZD9IvBTYTEBA6nmZ%2FCGeO33BuH%2FOvShbsw49PhxAY6pgEDK3W91VDJVlBdn20fWQTpstqSNvGyPdZ8A4z7%2BZRuMgND6myHrcaFSCQbeVvPvpt0sfYlo%2BwcXZOf1KenC1Itq1%2BOLMMD%2FQMYjBQIu8tJukAvzMAmw9sZxMd9x%2FBv9fbRAjhk9aHILudzdRO%2B8HNdfxWsYLTWnXmvvGA1NVxq5qkaIIEAmet7Tez8O7s51S18MeVQFYhtTZFOMCX06grZ5pIYrLUL&X-Amz-Signature=6ab3db514270a66f8b9e5246e2f9f7726e598f39f34b022dd6db71bb2b000c01&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

- 이상적인 diffusion model p*{\theta}는 q의 역방향이므로 D3PM에서는 아래 수식으로 p*{\theta}를 정의

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

- Transformer x*\theta를 사용해 파라미터화: p*\theta(x^b | x_t^b, x^{<b})

- Block들에 대해 병렬적 학습을 가능하게 함 (block-causal attention mask)

- x*\theta의 학습: block b 내에서 x*\theta^b(x_t^b, x^{<b}) → L' 길이의 결과 예측

→ 아래 K, V 캐시 수식을 보시면 모델을 이해하기 쉬움!

**K, V caching**

- recomputing을 막기 위한 block 단위 caching

### EFFICIENT TRAINING AND SAMPLING ALGORITHMS

**Training**

- 모든 block은 x\_\theta의 forward pass를 두 번 거쳐야 함 (x_t^b, x^b) → 계산의 효율화 필요

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/eb4721a8-a676-45e2-b3f2-97af33df40a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R27ZVFKX%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGh3%2FVK8MxTZGWx8EIBPmzCC5B9Ex0Tk3YZUSo3qieJ0AiAF76nYDUcXmMJxHcjpA3wWo6J0DMA7AzOJDqmdCd1GdiqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6vTN%2FFvE7Q0qm3efKtwDoyRuNj8qCRSyr1D14k3QpH06%2BTqB1NJDMawNN%2Fd3eftUsqQMWsBUHlPW4fS7IZjzzsxfXyzTywvEGNXzOacqhROjhhqwIEHcQmuEzva%2Fq7sr93JFgFylhZNH5i6030B31Xrmy3QhFWx1ox%2BHmqyBwEvDp5fgDc3y0obpigKNRXJdQPnqk5BfkjeY%2B4z3pjbi9EzidjaW0Tgq5NWsoYiP%2BCql12BhwLFqnitpfIgAfwUIW1ga54TNzkYtm8BZIO3kA8BfobLJqGKsJ535ZeoBwII9VygJkhQVuQK7ToFr0re9yRxYUIjvu2wCZK7L89QVMHmGa1hWE1CD6zMz2RJziMDhNLOD2cbT%2BMaRDzP0ubhCrMQP5p5s7Fu6FhwOvKyh7xE0x3UUB6WgAI95izKGjf9nYb2gu1dufZ5iHcCUUcmErlAvM2fuPeZrNrw5zgHt6MTeJvU0T9XRCFrpT%2FM3cv8ZMfLPovzSSqm12eqSIQQCY1u%2BEkggeiklKUmowkQZIybTZfL2NiUVbRvsL6%2FsXCfY4iG%2BfCSl9kV4XQktZ7rgyzeiVBfsqM58ss1RtYvgohtBnEPkNbLMA%2FEDWXjlAwH29dZD9IvBTYTEBA6nmZ%2FCGeO33BuH%2FOvShbsw49PhxAY6pgEDK3W91VDJVlBdn20fWQTpstqSNvGyPdZ8A4z7%2BZRuMgND6myHrcaFSCQbeVvPvpt0sfYlo%2BwcXZOf1KenC1Itq1%2BOLMMD%2FQMYjBQIu8tJukAvzMAmw9sZxMd9x%2FBv9fbRAjhk9aHILudzdRO%2B8HNdfxWsYLTWnXmvvGA1NVxq5qkaIIEAmet7Tez8O7s51S18MeVQFYhtTZFOMCX06grZ5pIYrLUL&X-Amz-Signature=5cf63f629c543e86d11c4b3feac5c6a5a59d961072eb63d65d4268a5d1e9c165&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

1. Block 별로 noise level sampling

1. 각 block에 대해 noisy input x\_{t_b}^b 생성

1. \left(\emptyset, \mathbf{K}^{1: B}, \mathbf{V}^{1: B}\right) \leftarrow \mathbf{x}\_\theta(\mathbf{x}): 원본 x를 이용해 K, V cache 미리 다 계산하기

1. 모든 b에 대해 x^b\_{\text{logit}} 계산

**Sampling**

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/58c6f097-5e59-4fe3-ad19-c252725e2e29/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R27ZVFKX%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGh3%2FVK8MxTZGWx8EIBPmzCC5B9Ex0Tk3YZUSo3qieJ0AiAF76nYDUcXmMJxHcjpA3wWo6J0DMA7AzOJDqmdCd1GdiqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6vTN%2FFvE7Q0qm3efKtwDoyRuNj8qCRSyr1D14k3QpH06%2BTqB1NJDMawNN%2Fd3eftUsqQMWsBUHlPW4fS7IZjzzsxfXyzTywvEGNXzOacqhROjhhqwIEHcQmuEzva%2Fq7sr93JFgFylhZNH5i6030B31Xrmy3QhFWx1ox%2BHmqyBwEvDp5fgDc3y0obpigKNRXJdQPnqk5BfkjeY%2B4z3pjbi9EzidjaW0Tgq5NWsoYiP%2BCql12BhwLFqnitpfIgAfwUIW1ga54TNzkYtm8BZIO3kA8BfobLJqGKsJ535ZeoBwII9VygJkhQVuQK7ToFr0re9yRxYUIjvu2wCZK7L89QVMHmGa1hWE1CD6zMz2RJziMDhNLOD2cbT%2BMaRDzP0ubhCrMQP5p5s7Fu6FhwOvKyh7xE0x3UUB6WgAI95izKGjf9nYb2gu1dufZ5iHcCUUcmErlAvM2fuPeZrNrw5zgHt6MTeJvU0T9XRCFrpT%2FM3cv8ZMfLPovzSSqm12eqSIQQCY1u%2BEkggeiklKUmowkQZIybTZfL2NiUVbRvsL6%2FsXCfY4iG%2BfCSl9kV4XQktZ7rgyzeiVBfsqM58ss1RtYvgohtBnEPkNbLMA%2FEDWXjlAwH29dZD9IvBTYTEBA6nmZ%2FCGeO33BuH%2FOvShbsw49PhxAY6pgEDK3W91VDJVlBdn20fWQTpstqSNvGyPdZ8A4z7%2BZRuMgND6myHrcaFSCQbeVvPvpt0sfYlo%2BwcXZOf1KenC1Itq1%2BOLMMD%2FQMYjBQIu8tJukAvzMAmw9sZxMd9x%2FBv9fbRAjhk9aHILudzdRO%2B8HNdfxWsYLTWnXmvvGA1NVxq5qkaIIEAmet7Tez8O7s51S18MeVQFYhtTZFOMCX06grZ5pIYrLUL&X-Amz-Signature=f4ea61d54bf2b7a7b469db57d5ce92b4eaf77a64dd7a53856f1540e57f0cbd0f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

- 왜 그럴까? \mathbb{E}\_{t\sim\mathcal{U}[0,1]}q(x_t^\ell=m|x^\ell) = 0.5 기본적으로 학습에 사용하는 token의 수가 절반으로 줄기 때문에 variance가 커지는 것

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/700e7811-3ef0-4009-9169-95751d4f79aa/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R27ZVFKX%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGh3%2FVK8MxTZGWx8EIBPmzCC5B9Ex0Tk3YZUSo3qieJ0AiAF76nYDUcXmMJxHcjpA3wWo6J0DMA7AzOJDqmdCd1GdiqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6vTN%2FFvE7Q0qm3efKtwDoyRuNj8qCRSyr1D14k3QpH06%2BTqB1NJDMawNN%2Fd3eftUsqQMWsBUHlPW4fS7IZjzzsxfXyzTywvEGNXzOacqhROjhhqwIEHcQmuEzva%2Fq7sr93JFgFylhZNH5i6030B31Xrmy3QhFWx1ox%2BHmqyBwEvDp5fgDc3y0obpigKNRXJdQPnqk5BfkjeY%2B4z3pjbi9EzidjaW0Tgq5NWsoYiP%2BCql12BhwLFqnitpfIgAfwUIW1ga54TNzkYtm8BZIO3kA8BfobLJqGKsJ535ZeoBwII9VygJkhQVuQK7ToFr0re9yRxYUIjvu2wCZK7L89QVMHmGa1hWE1CD6zMz2RJziMDhNLOD2cbT%2BMaRDzP0ubhCrMQP5p5s7Fu6FhwOvKyh7xE0x3UUB6WgAI95izKGjf9nYb2gu1dufZ5iHcCUUcmErlAvM2fuPeZrNrw5zgHt6MTeJvU0T9XRCFrpT%2FM3cv8ZMfLPovzSSqm12eqSIQQCY1u%2BEkggeiklKUmowkQZIybTZfL2NiUVbRvsL6%2FsXCfY4iG%2BfCSl9kV4XQktZ7rgyzeiVBfsqM58ss1RtYvgohtBnEPkNbLMA%2FEDWXjlAwH29dZD9IvBTYTEBA6nmZ%2FCGeO33BuH%2FOvShbsw49PhxAY6pgEDK3W91VDJVlBdn20fWQTpstqSNvGyPdZ8A4z7%2BZRuMgND6myHrcaFSCQbeVvPvpt0sfYlo%2BwcXZOf1KenC1Itq1%2BOLMMD%2FQMYjBQIu8tJukAvzMAmw9sZxMd9x%2FBv9fbRAjhk9aHILudzdRO%2B8HNdfxWsYLTWnXmvvGA1NVxq5qkaIIEAmet7Tez8O7s51S18MeVQFYhtTZFOMCX06grZ5pIYrLUL&X-Amz-Signature=5bdf4d742efc53fad469b072da9b4ab09540645608e2412ecab16ef2e7f8b9c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- tuned schedule: q(x_t^\ell = m | x^\ell) = 1

### DIFFUSION GAP FROM HIGH VARIANCE TRAINING

- Case study를 넘어 L^\ell \geq 1인 케이스로 확장하고 싶음!

- Batch size를 K라고 할 때, batch of sequence \text{X} = [x^{(1)},x^{(1)},...,x^{(K)}], with each \text{x}^{(k)} \overset{\text{iid}}{\sim} q(x)

- **NELBO estimator**

- **Variance of the gradient estimator**
