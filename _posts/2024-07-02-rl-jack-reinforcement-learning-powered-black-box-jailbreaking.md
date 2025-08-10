---
categories:
  - paper-reviews
date: "2024-07-02 00:00:00"
description: 논문 리뷰 - RL, Safety 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
  - alignment
  - fine-tuning
  - llm
  - paper-review
  - reinforcement-learning
  - rl
  - safety
thumbnail: assets/img/posts/2024-07-02-rl-jack-reinforcement-learning-powered-black-box-jailbreaking/thumbnail.jpg
title: "RL-JACK: Reinforcement Learning-powered Black-box

  Jailbreaking Attack against LLMs"
---

**논문 정보**

- **Date**: 2024-07-02
- **Reviewer**: 상엽
- **Property**: RL, Safety

# Introduction

도입 배경

- LLM의 엄청난 성과 → LLM의 데이터에 포함된 unsafe 내용으로 인해 LLM이 비윤리적인 답변을 함. → Safety alignment를 추가, unsafe 쿼리에 대한 답변 거부를 포함하는 내용으로 fine-tuning → Alignment 이후에도 여전히 실패 사례 존재 → Jailbreaking prompts!

Jailbreaking prompt

- 공격 방법 : 가상의 상황과 시나리오를 만든 후 비윤리적 질문을 추가.

- 기존 방법들의 한계점

→ Deep RL을 활용한 RL-JACK 제안

**RL-JACK**

- DRL agent는 jailbreaking generation과 refinement를 맡음.

- 기존에 존재하는 jailbreaking 방법을 선택하는 것을 action으로 설정, 현재 state에서 적절한 action을 선정하는 것이 목표

- reward 설계: continuous feedback이 가능한 reward 설계

- state transition 설계: 안정된 학습을 위해 state를 정의할 방법 설계

**Contributions**

- jailbreaking을 검색 문제로 정의함으로써 RL을 활용한 novel black-box jailbreaking 방법 제안

- 기존 SOTA 모델들과 비교했을 때 매우 큰 성능 향상을 보임.

- 아래 실험들을 통해 모델의 강점을 확인함.

# Key Techniques

### Threat Model and Problem Formulation

- Assumptions for attackers: black-box setup 가정

- 공격 목표

- Problem formulation

### Solve Jailbreaking with DRL

- 최적의 Prompt p_i를 찾는 작업은 일종의 searching problem이라고 생각

- 엄청나게 넓은 search space에 대해 다음 두 가지의 search 전략이 있음.

- 하지만 LLM 내부에 접근이 불가능하기 때문에 Deterministic 방법을 적용할 수가 없음. → Black-box setup에서 효과적인 deterministic search 방법으로 RL을 활용

DRL이 아무리 효과적이라 해도 시스템 디자인에 너무 의존적임.

초기 시도: 답변 거절 여부를 활용한 suffixes 토큰 추가

- 관련 여구: suffixes로 특정 토큰을 추가하는 것이 jailbreaking을 가능하게 하더라.

- RL agent의 역할 : jailbreaking suffixes를 추가

- harmful query q_i, 초기 prompt p_i^{(0)} → suffix로 추가할 토큰 선택 → p_i^{(1)} → Target LLM에 입력 → u_i^{(1)}→ reward 계산

- Reward는 Keyword match로 계산, llm의 결과가 거절을 의미하는 키워드나 phrases를 포함하는지 여부로 판단 (I’m sorry, I cannot, etc.) → 효과적이지 않았음.

- token 단위 RL 디자인의 문제 원인

→ 결론적으로 action space는 제한적이어야 하며 reward는 dense 해야 한다.

### Our Attack Overview

**Rationale for action design: large search space를 피하기**

- Helper LLM을 이용한 prompt generation 방법 제안

- 10개의 strategies를 선정 (Section 4.4)

**Rationale for reward design: meaningful dense rewards 방법**

- 실제 LLM의 답변이 harmful query에 대한 답변이 맞는지 여부로 판단

- 0, 1이 아닌 continous한 reward를 주기 위한 방법으로 pre-specified “reference”를 도입

- reward를 계산하기 위해 unaligned model을 이용. harmful question에 대한 답변(\hat{u_i})를 활용

- LLM을 이용한 reward 평가는 계산 비효율적, 고비용이라 제거 했다고 하는데 공감은 안됨. (오히려 aligned 되어 있어서 제대로 평가가 안될 수 있다는 게 더 좋은 이유일듯함.)

**System overview**

{% include figure.liquid loading="eager" path="assets/img/posts/2024-07-02-rl-jack-reinforcement-learning-powered-black-box-jailbreaking/image_000.png" class="img-fluid rounded z-depth-1" %}

- s^{(0)} : 초기 harmful query

- a^{(0)}: prompt 수정 전략 선택

- p^{(0)}: Helper LLM을 통한 prompt 수정 (+ query)

- R(u^{(0)}, \hat{u}) : reward 계산

### Attack Design Details

**RL formulation**

Markov Decision Process (MDP): \mathcal{M}=(\mathcal{S}, \mathcal{A}, \mathcal{T}, \mathcal{R}, \gamma)

- \mathcal{T}: \mathcal{S} \times \mathcal{A} \rightarrow \mathcal{S} : state transition function

- \mathcal{R}: \mathcal{S} \times \mathcal{A} \rightarrow R: reward function

- \mathbb{E}\left[\sum_{t=0}^T \gamma^t r^{(t)}\right] 를 최대로 하는 optimal policy 찾기

**State and action**

state

- 현 시점에 refined된 prompt p^{(t)} 다음 state s^{(t+1)}로 사용

- LLM의 답변을 state에 포함할 경우 state의 space가 너무 커지며 cost가 커지기 때문에 제외함. (실험이 있는지는 추후 확인해보자.)

action

- 아래의 pre-defined된 action과 instruction을 이용.

{% include figure.liquid loading="eager" path="assets/img/posts/2024-07-02-rl-jack-reinforcement-learning-powered-black-box-jailbreaking/image_001.png" class="img-fluid rounded z-depth-1" %}

**State transition**

- 이전 prompt를 state로 활용할 때 다양한 action들이 switch하는 것은 jailbreaking 생성 전략에 혼란을 줄 수 있음.

- state continuity를 위해 context를 추가하는 action (a_1,...a_7)에 대해서 교차 연산 추가

- Crossover: helper 모델을 활용할 때 두 결과물을 합치는 방식

**Reward**

- \Phi : text encoder

**Agent**

- text encoder + classifer 구조

**Termination and training algorithm**

- maximum time step T : 5

- reward threshold \tau : 0.75

- PPO 알고리즘 활용

- 일반적으로 advantage function A^{(t)} = R^{(t)} - V^{(t)} 으로 계산하는 것이 더 효과적이라고 하나 현재 연구에서는 Reward를 직접적으로 사용

**Launching attack with a trained agent**

- harmful query 제공 → action 선택 → Helper LLM에서 5개의 jailbreaking prompt 생성 → 성공 여부 판단 → 실패 시 재실행 (최대 5번까지)

# Evaluation

### Attack Effectiveness and Efficiency

- Dataset

- Target LLM, helper model, unaligned model

- Baselines

- Metric
