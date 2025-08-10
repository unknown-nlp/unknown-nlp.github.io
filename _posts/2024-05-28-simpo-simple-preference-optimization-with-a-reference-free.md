---
categories:
- paper-reviews
date: '2024-05-28 00:00:00'
description: 논문 리뷰 - Alignment, RLHF 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- alignment
- paper-review
- rlhf
thumbnail: assets/img/posts/2024-05-28-simpo-simple-preference-optimization-with-a-reference-free/thumbnail.jpg
title: 'SimPO: Simple Preference Optimization with a Reference-Free Reward'
---

**논문 정보**
- **Date**: 2024-05-28
- **Reviewer**: 건우 김
- **Property**: Alignment, RLHF

# **SimPO: Simple Preference Optimization with a Reference-Free Reward**

## 1. Introduction

LM이 Human intention과 alignment를 형성하기 위해서는 (helpful, honest, harmless), human feedback으로 부터 학습하는 것이 효율적임. 이전 classical RLHF (e.g. PPO)는 좋은 성능을 보여주긴 하지만 아시다시피 multi-stage procedure (Training reward model + Optimize policy model)이 필요함.

최근에는 DPO와 같이 simpler offline preference algorithm이 많이 소개됨. DPO는 reward function을 reparameterize하여 preference data로 부터 policy model을 directly 학습시켜 별도의 reward model이 필요가 없음. (simplicity & training stability 보장)

DPO에서 implicit reward는 current policy model과 SFT model의 response의 likelihood의 log ratio로 구성이 되어 있음. 

→ 하지만, 연구진들은 DPO reward 식은 policy model에 의해 생성되는 response의 average log likelihood를 통해 inference를 진행한다는 점에서 discrepancy가 존재하여 suboptimal performance를 보인다고 가정함.

본 연구에서는, DPO 보다 더 simple하고 효과적인 offline preference optimization algorithm인 SimPO를 소개함. 이 알고리즘의 핵심은 reward function을 generation metric과 align을 시킨 점이다.

{% include figure.liquid loading="eager" path="assets/img/posts/2024-05-28-simpo-simple-preference-optimization-with-a-reference-free/image_000.png" class="img-fluid rounded z-depth-1" %}

SimPO는 크게 두 가지 components가 있음

1. **length-normalized reward**: policy model을 이용하여 response 내에 있는 모든 Token들의 log probability의 평균 값을 통해 산출

1. **target reward margin**: winning / losing responses 간의 reward difference를 보장함

저자가 정리하는 SimPO의 3가지 주요 properties

- **Simplicity**: 별도의 reference model이 필요하지 않음.

- **Significant performance advantage**: DPO와 variants( KTO, DPO-R, ORPO et.c)과 비교해도 consistent하게 instruction-following benchmarks에서 가장 높은 성능을 보여줌

- **Minimal length exploitation**: SFT나 DPO에 비해 response length가 짤음

## 2. SimPO: Simple Preference Optimization

### 2.1 Background: DPO

DPO는 reward function (r)을 다음과 같이 reparameterize함.

- pi_theta: policy model

- pi_ref: reference policy (SFT model)

- Z(x): partition function

{% include figure.liquid loading="eager" path="assets/img/posts/2024-05-28-simpo-simple-preference-optimization-with-a-reference-free/image_001.png" class="img-fluid rounded z-depth-1" %}

위 reward function을 Bradley-Terry (BT) ranking objective에 적용하면, 

{% include figure.liquid loading="eager" path="assets/img/posts/2024-05-28-simpo-simple-preference-optimization-with-a-reference-free/image_002.png" class="img-fluid rounded z-depth-1" %}

아래와 같이 도출됨.

{% include figure.liquid loading="eager" path="assets/img/posts/2024-05-28-simpo-simple-preference-optimization-with-a-reference-free/image_003.png" class="img-fluid rounded z-depth-1" %}

### 2.2 A Simple Reference-Free Reward Aligned with Generation

**Discrepancy between reward and generation for DPO**

앞에서 언급한  DPO에서 reward와 generation 간의 discrepancy에 집중을 해봄. 

{% include figure.liquid loading="eager" path="assets/img/posts/2024-05-28-simpo-simple-preference-optimization-with-a-reference-free/image_004.png" class="img-fluid rounded z-depth-1" %}

해당 implicit reward는 두가지 한계점이 존재함

1. 별도의 reference model (pi_ref)가 필요하기 때문에, 추가적인 memory/computational cost가 요구됨

1. Training 단계에서 사용되는 reward와 inference 단계에서 generation metric에 사용되는 reward 간의 discrepancy가 존재함.

**Length-normalized reward formulation**

위에서 언급한 DPO의 문제점을 고려해보면, reward function이 likelihood metric과 align이 되도록 다음과 같이 다시 구성해야한다. 

{% include figure.liquid loading="eager" path="assets/img/posts/2024-05-28-simpo-simple-preference-optimization-with-a-reference-free/image_005.png" class="img-fluid rounded z-depth-1" %}

- 여기서 length normalization term을 지우게 되면, lower-quality with longer sequence를 생성하도록 bias가 생길 수 있음.

- reference model을 없애며, computation/memory efficient한 점을 보여줌

### 2.3 The SimPO Objective

**Target reward margin**

Bradley-Terry objective에 target reward margin term (r)을 추가해주며 winning response에 대한 reward가 losing response보다 최소한 r 만큼 차이 나도록 보장해줌.

{% include figure.liquid loading="eager" path="assets/img/posts/2024-05-28-simpo-simple-preference-optimization-with-a-reference-free/image_006.png" class="img-fluid rounded z-depth-1" %}

**Objective function**

위에선 언급한 내용들을 종합하여 최종 SimPO objective function은 다음과 같이 전개할 수 있음.

{% include figure.liquid loading="eager" path="assets/img/posts/2024-05-28-simpo-simple-preference-optimization-with-a-reference-free/image_007.png" class="img-fluid rounded z-depth-1" %}

## 3. Experimental Setup

모든 실험은 Llama3-8B, Mistral-7B 각각에 대해 Base, Instruct setting으로 진행이됨.

**Base**: Zephyr와 동일하게 사용

1. init model (llama, mistral) 을 SFT 모델로 학습

1.  preference optimization 진행

**Instruct**: off-the-shelf instruction-tuned model을 SFT model로 사용

**Evaluation benchmarks**

- MT-Bench

- AlpacaEval 2

- Arena-Hard v0.1

**Baselines**

{% include figure.liquid loading="eager" path="assets/img/posts/2024-05-28-simpo-simple-preference-optimization-with-a-reference-free/image_008.png" class="img-fluid rounded z-depth-1" %}

- fair한 비교를 위해 각 baseline에 대해서 Hypermarameter tuning을 많이 진행함

- 결론부터 말하면, variants of DPO들은 일반 DPO보다 성능이 구림 

## 4. Experimental Results

### 4.1 Main Results and Ablations

{% include figure.liquid loading="eager" path="assets/img/posts/2024-05-28-simpo-simple-preference-optimization-with-a-reference-free/image_009.png" class="img-fluid rounded z-depth-1" %}

- SimPO는 existing methods 대비 consistent하게 높은 성능을 보여줌

- MT-Bench에서 점수들이 다 비슷한 점수대에 있는 이유는, benchamrk 자체가 데이터셋이 적어 randomness 요인으로 차이가 난 것

- 당연하게도** Instruct** 세팅에서 performance gain이 비약적으로 보임

- SimPO에서 제안하는 components는 다 매우 중요함

## 5. Conclusion

- DPO의 reward term에서 reference model을 없애며 average log probability를 implicit한 Reward로 사용한 새로운 preference alignment 방법인 SimPO를 소개함.

- 방법도 간단하고 실험 결과도 (ORPO 대비) 매우 훌륭하지만, Appendix를 보면 huggingface leaderboard 결과가 sota는 아님.
