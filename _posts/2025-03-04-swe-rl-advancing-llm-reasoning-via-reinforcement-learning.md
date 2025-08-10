---
categories:
- paper-reviews
date: '2025-03-04 00:00:00'
description: 논문 리뷰 - RL 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- gpt
- llm
- paper-review
- reasoning
- reinforcement-learning
- rl
thumbnail: assets/img/posts/2025-03-04-swe-rl-advancing-llm-reasoning-via-reinforcement-learning/thumbnail.jpg
title: 'SWE-RL: Advancing LLM Reasoning via Reinforcement Learning on Open Software
  Evolution'
---

**논문 정보**
- **Date**: 2025-03-04
- **Reviewer**: 전민진
- **Property**: RL

## Abstract

- DeepSeek-R1 출시 이후, RL이 모델의 일반적인 reasoning ability 끌어올릴 수 있다는 잠재력이 증명됨

- 간단한 rule-based reward(정답과 모델이 생성한 답변과의 유사도)을 활용해서 학습, SWE-RL은 in-domain뿐만 아니라 out-of-domain에서도 뛰어난 성능을 보임

{% include figure.liquid loading="eager" path="assets/img/posts/2025-03-04-swe-rl-advancing-llm-reasoning-via-reinforcement-learning/image_000.png" class="img-fluid rounded z-depth-1" %}

## Introduction

- DeepSeek-R1은 rule-based RL이 용이한 도메인에 대해서만 학습, 실험 진행

- SE task에 대해서 LLM을 향상시키는 첫번째 RL method, SWE-RL을 제안

## SWE-RL

{% include figure.liquid loading="eager" path="assets/img/posts/2025-03-04-swe-rl-advancing-llm-reasoning-via-reinforcement-learning/image_001.png" class="img-fluid rounded z-depth-1" %}

### Raw pull request data curation

- Github events and clones

- PR data aggregation ⇒ 자세한 내용은 원문 참고.. 이해 못했음..

- Relevant files prediction 

- Data filtering

### Reward modeling

{% include figure.liquid loading="eager" path="assets/img/posts/2025-03-04-swe-rl-advancing-llm-reasoning-via-reinforcement-learning/image_002.png" class="img-fluid rounded z-depth-1" %}

- logic-RL과 유사하게 system prompt넣어줌, format이 틀릴 경우 -1을, 맞을 경우 정답과의 유사도를 계산해 reward를 줌

- loss식은 GRPO와 동일

- SWE-RL에서의 학습을 살펴보면, 학습데이터에는 내재적으로 bug 진단, 수정사항 생성 task 2가지 정도만 커버

### Aha Moments and generalized reasoning capabilities

- SWE-RL에서도 아하모먼트(심화된 reasoning ability)가 나타남, 특히 SE task에서 필요한 reasoning ability가 아니라 범용적인 reasoning ability(self reflection, exploring multiple approaches, divide-and-conquer)등이 발현됨

{% include figure.liquid loading="eager" path="assets/img/posts/2025-03-04-swe-rl-advancing-llm-reasoning-via-reinforcement-learning/image_003.png" class="img-fluid rounded z-depth-1" %}

## Evaluation

### Experimental Setup

- Training configs

- Scaffolding

- Evaluation setup

- SFT baseline

### Main results

{% include figure.liquid loading="eager" path="assets/img/posts/2025-03-04-swe-rl-advancing-llm-reasoning-via-reinforcement-learning/image_004.png" class="img-fluid rounded z-depth-1" %}

- GPT-4o 혹은 Claude-3.5-Sonnet의 결과를 Distillation한 Lingma-SWE-GPT, SWE-Gym, SWE-Fixer 등을 비교군으로 사용

- distillation data 구축 없이도 성능 압도

### Baseline comparison

{% include figure.liquid loading="eager" path="assets/img/posts/2025-03-04-swe-rl-advancing-llm-reasoning-via-reinforcement-learning/image_005.png" class="img-fluid rounded z-depth-1" %}

- Repair performance에 집중해 성능 분석

- Llama-3.3모델은 20개 샘플링해서 다수결해도 formatting에 어려움을 겪음

- RL은 formatting도 잘하면서 repair performance도 우수

### Scaling analysis with more samples

{% include figure.liquid loading="eager" path="assets/img/posts/2025-03-04-swe-rl-advancing-llm-reasoning-via-reinforcement-learning/image_006.png" class="img-fluid rounded z-depth-1" %}

- repair sample, test sample의 수를 조절하면서 성능 비교

- 어느정도 큰 수가 되면 성능이 수렴

### Generalizability of RL

- SWE-bench 외에도 function coding, library use, code reasoning등의 code 도메인의 다른 task에서도 성능이 향상됨

- 대단한건 MATH 성능이 크게 향상, MMLU 성능을 잃지 않음..!!!

{% include figure.liquid loading="eager" path="assets/img/posts/2025-03-04-swe-rl-advancing-llm-reasoning-via-reinforcement-learning/image_007.png" class="img-fluid rounded z-depth-1" %}

### Reward ablation

- reward를 0-1사이의 continuous값이 아니라 discrete한 값으로 주었을 때의 결과

- continuous가 낫다!

{% include figure.liquid loading="eager" path="assets/img/posts/2025-03-04-swe-rl-advancing-llm-reasoning-via-reinforcement-learning/image_008.png" class="img-fluid rounded z-depth-1" %}
