---
categories:
- paper-reviews
date: '2024-07-23 00:00:00'
description: 논문 리뷰 - Reasoning, Reinforcement Learning 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- language-model
- llm
- paper-review
- reasoning
- reinforcement learning
- reinforcement-learning
- vision
thumbnail: assets/img/posts/2024-07-23-training-large-language-models-for-reasoning-through-reverse/thumbnail.jpg
title: Training Large Language Models for Reasoning through Reverse Curriculum Reinforcement
  Learning
---

**논문 정보**
- **Date**: 2024-07-23
- **Reviewer**: 전민진
- **Property**: Reasoning, Reinforcement Learning

## Abstract

- Reasoning에서 RL의 challenge는 정답을 내는 action의 sequence를 식별하기 어렵다는 것

- 기존 방법인 output supervision(최종 답에 대해서만 reward 부여)은 sparse reward로 어느 시점에 error가 발생되는지 알 수 없음

- 반대로, step마다 reward를 부여하는 process supervision 방식의 경우 annotation비용이 너무 커진다는 단점 존재

>> 본 논문에서는 정답 rationale을 reverse curriculum방식으로 학습하여 이와 같은 문제를 해결하고자 함

## Introduction

- 기존에 LLM을 활용해 reasoning task를 풀 땐 rationale을 생성하도록 학습(step-by-step Chain-of-Thought manner)

- 하지만 SFT는 human demonstaration을 따라하도록 학습하게 되어 일반화를 하기 위해선 대량의, 다양한, 고품질의 annatation이 필요

- RL의 경우 exploration과 learning을 통해 reasoning을 향상 시키는 현실적인 대안으로 소개되어 옴

- process supervision은 모든 reasoning step에 적절한 feedback을 제공하지만 annotation비용이 너무 큼

- 본 논문에서는 R^3: Learning Reasoning through Reverse Curriculum Reinforcement Learning을 제안

- 실험 결과, mathematical reasoning, logical reasoning, NLI 등에서 기존 SFT, RL보다 높은 성능 보임

## Related works

- RL basic

- RL with outcome supervision

- RL with process supervision

## Proposed method

- outcome과 process supervision의 이점을 합치는 방법론을 모색하다 찾음

{% include figure.liquid loading="eager" path="assets/img/posts/2024-07-23-training-large-language-models-for-reasoning-through-reverse/image_000.png" class="img-fluid rounded z-depth-1" %}

- Start exploration from intermediate states of demonstration

- Reverse curriculum learning for step-level supervision

- Mixing start states for generalization

- Reward Design and Policy Optimization

- Algorithm

## Experiments

- Experimental Setup

- Results on CoT reasoning

- Results on P-CoT reasoning

- Ablation study

## Conclusion

- reverse curriculum RL방식으로 LLM의 reasoning ability를 향상시키는 방법론 제안

- 문제를 구체화하는거 까지는 멋졌는데… 방법론이 생각보다 막 좋은지는 모르겠다..
