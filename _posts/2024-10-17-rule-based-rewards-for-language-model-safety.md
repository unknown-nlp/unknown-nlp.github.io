---
categories:
- paper-reviews
date: '2024-10-17 00:00:00'
description: 논문 리뷰
giscus_comments: true
layout: post
related_posts: false
tags:
- gpt
- language-model
- llm
- paper-review
- rlhf
thumbnail: assets/img/posts/2024-10-17-rule-based-rewards-for-language-model-safety/thumbnail.jpg
title: Rule Based Rewards for Language Model Safety
---

**논문 정보**
- **Date**: 2024-10-17
- **Reviewer**: 준원 장

## 1. Introduction

- Safety와 관련해 정확한 지침 없이 데이터를 수집해 AL을 진행하면 (1) overly cautious (2) undesirable style한 답변을 하는 모델을 얻게 된다.

- 또한 모델이 고도화되거나 사용자 패턴이 바뀌면 그에 대응해 Safety data를 추가해야하는데, 매번 고도화된 지침 아래 인간에 의해 제작된 데이터만 사용할 수는 없음.

- 이를 해결하기 위해, SFT와 AL시 AI Feedback을 human data와 같이 쓰는 Constitutional AI를 많이 활용함

- 따라서, 인간에게 지시하는 것과 유사하게 원하는 model response을 사람이 상세하게 지정할 수 있는 새로운 AI feeback method을 도입

## 2. Related Work

- RLHF

- RLAIF

## 3. Method

- 해당 연구에서는 LLM의 SFT → RLHF의 기본 프레임크를 따름. 아래는 논문에서 활용할 기본적인 데이터와 모델 프레임 워크

- 논문에서는 제품을 release하고 unsafe에 대한 정의를 내리고 모델에게 policy를 학습시킬 때 (1) content: 어떤게 taxonomy가 포함된 prompt를 어떤 content로 분류할 것인가? (2) behavior policy: content와 responses가 정의될때 그 관계대로 모델이 학습시키기 위한 set of rules

### Rule-Based Rewards for Safety

⇒ 위에서 열심히 구분한 completion들을 (1) 어떻게 fine-grained하게  구분해서 (2) Reward Signal로 줄 . 수있냐?가 가장 큰 관건이나, openai는 heuristic과 자원으로 해결

- **Propositions and Rules**

{% include figure.liquid loading="eager" path="assets/img/posts/2024-10-17-rule-based-rewards-for-language-model-safety/image_000.png" class="img-fluid rounded z-depth-1" %}

- **A Small Set of Human Labelled Data for Prompt Tuning:  **

- **Synthetic Comparison Data For Weight Fitting**

- **Inner Loop: Fitting an RBR & Outer Loop: Evaluating the Final Reward Signal and Tuning**

## 4. Results

- 설명이 너무 없음… ;;;

- 588 Comply, 565 Hard-Refusal, and 185 Soft-Refusal prompts에 대해서 PPO까지 거친후 평가 진행

- Metric

- Evaluation을 위해서 RBR FT & GPT prompting, etc 활용

{% include figure.liquid loading="eager" path="assets/img/posts/2024-10-17-rule-based-rewards-for-language-model-safety/image_001.png" class="img-fluid rounded z-depth-1" %}

- human ppo는 overref의 희생으로 unsafe의 향상을 얻는데 rule-based만 설계해주면 그렇지 않다.

- human rm에 rbr+ppo reward를 더해주면 usefulness 개선이 뚜렷함 (b: 연그린)

- human-match rbr: rbr 학습데이터를 518개로 줄이니 성능저하

{% include figure.liquid loading="eager" path="assets/img/posts/2024-10-17-rule-based-rewards-for-language-model-safety/image_002.png" class="img-fluid rounded z-depth-1" %}

⇒ medium policy & large reward model

- (a) RBR 사이즈 커질수록 1. safe는 꾸준히 잘 구분함 2. overrefuse는 개선 3. hard refusal은 갑자기 감소했다가 증가

- (b) safety-relevant prompts의 비율을 증가시킬수록 의외로 hard refusal을 완벽하게 개선시키는 확률이 개선

- (c) 무시

## 5. Conclusion

- 설명이 너무 없는… 페이퍼

- 의외로 heuristic을 잘 설계하면 좋은 align signal을 줄 수 있다?
