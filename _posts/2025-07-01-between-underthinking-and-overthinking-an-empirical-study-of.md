---
categories:
- paper-reviews
date: '2025-07-01 00:00:00'
description: 논문 리뷰 - Reasoning 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- llm
- paper-review
- reasoning
thumbnail: assets/img/posts/2025-07-01-between-underthinking-and-overthinking-an-empirical-study-of/thumbnail.jpg
title: 'Between Underthinking and Overthinking: An Empirical Study of Reasoning Length
  and correctness in LLMs'
---

**논문 정보**
- **Date**: 2025-07-01
- **Reviewer**: 준원 장
- **Property**: Reasoning

## 1. Introduction

- Test-time scaling is trending, but **longer reasoning is not always better.**

- Reasoning와 accuracy가 항상 상관관계를 이루지 않는다는 최신연구 존재 (Xie et al., 2025; Jin et al., 2024; Wu et al., 2025)

- 여튼, 이러한 흐름에 따라 최근에 나온 용어

- 그래서 논문은 DeepSeek-1.5B-Distill과 DeepScaler-1.5B-Preview를 가지고 reasoning length와 accuracy를 가지고 체계적인 분석을 수행하겠다!

## 2. Related Work

⇒ lengthy reasoning 문제를 관측하고, 이를 해결하기 위한 학습방법론들

- **Concise thinking**

- **Adaptive thinking**

- **Optimal Thinking**

## 3. Experimental Setting

- Model

- Dataset

- Params.

- Notations

## 4. Sample-Level Analysis

→ q는 고정하고 길이가 다른 10개 completion을 비교해 length와 accuracy의 직접 상관을 조사

- 난이도에 대한 변인을 고정하고 length ↔ accuracy 관계만 볼 수 있음

### Non-Linear Relationship of Sample Length and Correctness

{% include figure.liquid loading="eager" path="assets/img/posts/2025-07-01-between-underthinking-and-overthinking-an-empirical-study-of/image_000.png" class="img-fluid rounded z-depth-1" %}

- L_r, Acc_r: r번째로 짧은 reasoning path의 평균 length/accuracy

- consistent non-monotonic trend 관찰

(준원 뇌피셜: 일단 R1은 (1) MATH 관련 데이터는 외워서 풀것 같기 때문에 temp=1.0, top_p=1로 줘서 decoding path 길어지면 degen 발생했을것으로 예상 (2) GSM8K 유사 난이도는 거의 외웠을것이고 + 상대적으로 쉽기 때문에 1~1.5K thinking budget내로는 거의 비슷할거 같음..)

{% include figure.liquid loading="eager" path="assets/img/posts/2025-07-01-between-underthinking-and-overthinking-an-empirical-study-of/image_001.png" class="img-fluid rounded z-depth-1" %}

- 초록: q에 대한 정답 completion중 가장 짧은 거

- 파랑: q에 대한 정답 completion중 가장 긴거

- 빨강: q에 대한 오답 completion중 가장 짧은 거

- 노랑: q에 대한 정답 completion중 가장 긴거

- R1-Preview는 MATH, GSM8K 모두 80% 이상의 질문에서 가장 짧은 샘플로 정답을 생성할 수 있음을 보임

- most length한 completion중에 correct response도 있지만 incorrect response도 존재 (논문 해석 이상..)

## 5. Question-Level Analysis

{% include figure.liquid loading="eager" path="assets/img/posts/2025-07-01-between-underthinking-and-overthinking-an-empirical-study-of/image_002.png" class="img-fluid rounded z-depth-1" %}

- 단순하게 문제 난이도를 틀림 여부로 볼때, incorrect response가 어떤 조합에서든 response 길이가 더 길었음

{% include figure.liquid loading="eager" path="assets/img/posts/2025-07-01-between-underthinking-and-overthinking-an-empirical-study-of/image_003.png" class="img-fluid rounded z-depth-1" %}

- N-completion별로 difficulty를 분류

⇒ 그러나 (1) 문제가 어려워서 lengthy한지 (2) length해져서 틀린건지 판단이 어려움

{% include figure.liquid loading="eager" path="assets/img/posts/2025-07-01-between-underthinking-and-overthinking-an-empirical-study-of/image_004.png" class="img-fluid rounded z-depth-1" %}

- Q^{easy}_{\cap} = Q^{easy}_{i} \cap Q^{easy}_{j}

- Q^{easy}_{i/j} = Q^{easy}_{i} /  Q^{easy}_{j} > M_i  에서만 쉬운 문제

- Q^{easy}_{j/i} = Q^{easy}_{j} /  Q^{easy}_{i} > M_j에서만 쉬운 문제 

- 보편적으로 쉬운 문제가 아니라 another model’s advantage set (다른모델에서 쉬운 문제)에서 오히려 lengthy generation을 보임

- signficant로 보면 M_i  → M_j-Adv Set을 풀때 보다 lengthy해짐

{% include figure.liquid loading="eager" path="assets/img/posts/2025-07-01-between-underthinking-and-overthinking-an-empirical-study-of/image_005.png" class="img-fluid rounded z-depth-1" %}

- hard question에서는 Q^{hard}_{\cap}에서 보다 another model’s advantage set에서 lengthy해질 것을 기대했으나 그렇진 않음

{% include figure.liquid loading="eager" path="assets/img/posts/2025-07-01-between-underthinking-and-overthinking-an-empirical-study-of/image_006.png" class="img-fluid rounded z-depth-1" %}

- (어떻게 실험했는지는 모르겠는데..) token length가 짧아질수록 accuracy가 올라간다. 

- 위에 실험을 기반으로 token legnth가 짧으니 확률적으로 당연히 accuracy가 높은 답변일수록 PPL도 낮을 것

## 6. Effect of Length Preference Optimization

- 지금까지 지적된 문제들을 해결하기 위해 correct/length-balanced reward-based RL등이 소개되었음

- 이를 위해 이전에 drive-out한 직관들을 가지고 간단한 실험을 진행.

{% include figure.liquid loading="eager" path="assets/img/posts/2025-07-01-between-underthinking-and-overthinking-an-empirical-study-of/image_007.png" class="img-fluid rounded z-depth-1" %}

- training step을 반복할수록 accuracy 변동폭은 적으나 average token length 30%에서 60% 감소

{% include figure.liquid loading="eager" path="assets/img/posts/2025-07-01-between-underthinking-and-overthinking-an-empirical-study-of/image_008.png" class="img-fluid rounded z-depth-1" %}

- SimPO가 진행됨에 따라 incorrect response의 생성이 줄어들었다.

## 7. Conclusion &  Limitation

- generation length와 final answer correctness에 대해서 심도 있는 분석

- LM의 크기가 너무 작고, benchmark가 너무 쉬움…
