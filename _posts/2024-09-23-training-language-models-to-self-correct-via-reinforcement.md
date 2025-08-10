---
categories:
- paper-reviews
date: '2024-09-23 00:00:00'
description: 논문 리뷰 - Reinforcement Learning, AGI 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- agi
- alignment
- fine-tuning
- language-model
- llm
- paper-review
- reinforcement learning
- reinforcement-learning
- vision
thumbnail: assets/img/posts/2024-09-23-training-language-models-to-self-correct-via-reinforcement/thumbnail.jpg
title: Training Language Models to Self-Correct via Reinforcement Learning
---

**논문 정보**
- **Date**: 2024-09-23
- **Reviewer**: 준원 장
- **Property**: Reinforcement Learning, AGI

## 1. Introduction

- 최근에 베포된 LLM은 ‘알고리즘=문제수행능력’을 안정적으로 진행하지 못함 ⇒ test time query에 대해서 LLM이 자체적으로 생성한 response를 ‘self-correct’하고 best-possible final response을 생성하는 action을 취하지 못함.

- 논문에서는 LLM이 위와 같이 어려운 문제를 풀때 “on-the-fly” setting으로 mistake를 해결하는 방법론을 연구하고자 함.

- 그렇다면 기존 연구에서는 어떻게 LLM에서 self-correction abilities를 주입했을까?

- 저자들은 실험 가능한 2개의 baseline의 한계를 제시하면서 새로운 방법론을 제시함

- 이를 해결하기 위해 논문에서는 

## 2. Related Works

**#### Prompting for intrinsic self-correction**

- self-correction 과정중에 oracle answer을 활용하는 한계

- first response를 생성할때는 weak prompt를 사용하고, self-correction시에는 strong prompt를 사용해 overestimate 문제

**#### Fine-tuning for intrinsic self-correction**

- oracle feedback (revisions directly from human annotators & human)을 SFT에 직접적으로 활용한다는 한계

⇒ 본 연구는 learner가 직접 생성하는 training data만을 활용

## 3. Preliminaries and Problem Setup

> **Problem Define**: External Feedback이 없는 intrinsic self-correction’ setup

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-23-training-language-models-to-self-correct-via-reinforcement/image_000.png" class="img-fluid rounded z-depth-1" %}

- Setting

- Standard SFT나 일반적인 RL tuning과는 달리, 여러 턴을 동시에 학습.

- 중간 턴 응답 ŷ_{1:t}은 final reward의 intermediate context를 위해 간접적으로 supervised tuning됨.

- **A base RL approach for fine-tuning LLMs**

- **Metric**

## 4. Supervised Fine-Tuning on Self-Generated Data is Insufficient for Self-Correction

** #### ‘Intrinsic Self-Correction’ Setting이니 외부 model의 feedback 없이 base-model을 가지고 self correction하는 SFT하는 방법론을 돌려보면 어떨까?**

- Baselines SFT

### 4.1. Analysis Setup: Methods and Dataset Construction

- STaR ⇒ (1) base model로 two-turn self-correction traces를 생성함. (2) second attempts가 successfully하게 first attempt의 incorrect responses를 revise할 경우에만 filter

- Welleck et al. (2023) ⇒ (1) base model로 two-turn self-correction traces를 생성함. (2) first attempts에서 pairing incorrect responses with correct ones 후 generates “synthetic” repair traces

### 4.2. Empirical Findings

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-23-training-language-models-to-self-correct-via-reinforcement/image_001.png" class="img-fluid rounded z-depth-1" %}

- Pair-SFT로 학습하면 base-model 대비 의도한 self-correction 행동경향성이 도출됨. (Δ(t1, t2)의 증가, incorrect → correct의 증가 correct → incorrect의 감소)

- STaR의 경우 오히려 self-correction이 전혀 일어나지 않고 있는데, 저자들은 ‘revision trajectories’가 limited된 space여서 그렇다고 함 (사실 뭔말인지 모르겠..)

- Table 1에서 가장 큰 문제는 Correct를 Incorrect로 바꿔버린다는 것 **(준원 생각: 사실상 self-correction이 아니라 그냥 무작위로 alignment를 하는것으로 보임)**, 저자들은 이런 경향성을 억지로 지워버리고자 2번째 attempts 모두에 대해서 correct response로 학습하는 Table2 결과를 내놓음

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-23-training-language-models-to-self-correct-via-reinforcement/image_002.png" class="img-fluid rounded z-depth-1" %}

- (제안한 방법론 SCoRe도 거의 변화가 없긴한데..) STaR D+, SFT D는 base model 대비 edit distance (first vs second response)의 차이가 거의 없는 것을 알 수 있습니다. 

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-23-training-language-models-to-self-correct-via-reinforcement/image_003.png" class="img-fluid rounded z-depth-1" %}

-  STaR D+와는 달리 SFT D는 training과 evaluation에서 edit distance (first vs second response)의 분포 차이가 많이 남.

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-23-training-language-models-to-self-correct-via-reinforcement/image_004.png" class="img-fluid rounded z-depth-1" %}

-  Pair-SFT에 대한 ablation

- Pair-SFT에서 Training때처럼 fixed validation set으로 validation을 진행하면 성능이 지속적으로 유지되는 것을 알 수 있음

### Takeaways: Insufficiency of SFT (previous method)

1. STaR D+는 distribution shift에는 강건한 대신 one mode of correction에만 collapse된다는 한계가 존재함.

1. Pair-SFT는 distribution shift가 있어 인해 (exploration은 좋아지나: 어찌저찌 성능은 좋아지나) 정작 LM의 first attempts에 대한 self correction 능력이 저하된다.

## 5. SCoRe: Self-Correction via Multi-Turn Reinforcement Learning

### Key Challenges

- 위의 mulit-turn RL을 활용해 학습을 진행하면 distributional shift를 해결할 수 있는건 수식적으로 당연

- 실험을 진행

- (left) first response과 second response의 train acc가 같은 방향으로 계속 움직이는 걸 알 수 있음

- (right) 초록색 선을 보면 first response대비 second response가 얼마나 다른 answer를 생성하는가?인데, 학습을 지속할 수록 coupling된 정답을 생성하는 것을 알 수 있음

### Why does this happens?

- Data distribution내에서 LM이 취할 수 있는 optimal action은 2가지.

**⇒ Overparameterization된 LLM은 (Data distribution내에서 1,2가 둘다 최적이라고 리워드가 설계되어있고 그걸 그대로 학습을 하면) 1.에 대한 정책을 제대로 학습하지 못할 수도 있음.**

**⇒ 과거의 주어진 attempts에 대해서 self-correcting하는 최적의 방법이 아니라, 현재 주어진 response를 개선하는 next response를 생성하라고 model에게 학습시켜야 함. **

### Method 

Objective

1. (비유를 들면 prior distribution을 깔아줌으로써) LM이 first attempt distribution하에서 second distribution을 생성하도록 학습 

1. reward-shaping을 통해 bias model to self-correct

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-23-training-language-models-to-self-correct-via-reinforcement/image_005.png" class="img-fluid rounded z-depth-1" %}

### 5.1. Stage I: Training a Model Initialization to Prevent Collapse

- one-mode collapse를 방지하기 위해 RL로 학습 진행

- second response에서 높은 reward revision이 이루어지도록 하는 동시에 KLD를 사용하여 first response distribution이 base-model 최대한 가깝게 제한함

### 5.2. Stage II: Multi-Turn RL with Reward Shaping

- first response와 second response에 대한 reward sum을 max하도록 training

- Reward shaping to incentivize self-correction

## 6. Experimental Evaluation

- **Tasks &. Models**

- **Results**

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-23-training-language-models-to-self-correct-via-reinforcement/image_006.png" class="img-fluid rounded z-depth-1" %}

- base model 대비 Δ(t1, t2)  15.6%,   Accuracy@t2 23.0% 증가

- 가장 고무적인건 의도한 self-correction이 동작한다는 점

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-23-training-language-models-to-self-correct-via-reinforcement/image_007.png" class="img-fluid rounded z-depth-1" %}

- Pair-SFT같은 경우 offline setting에서만 성능이 좋은 반면, SCoRe는 self-generated setting에서 self-correction(12.2% intrinsic self-correction delta)을 통해 성능 증가를 가져오는 것을 알 수 있음

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-23-training-language-models-to-self-correct-via-reinforcement/image_008.png" class="img-fluid rounded z-depth-1" %}

- (w/o m.t.t) single turn으로 학습을 진행하면 당연히 Accuracy@t1은 높지만 그 외의 지표는 떨어지고,

- (w/o s1, rs) stage 1이나 reward shaping을 제거하면 의도한 self-correction을 수행하지 못해  Accuracy@t2와 net increase acc 역시 하락하는 것을 확인할 수 있다.

- (w STaR) 마지막으로 stage 2에서 on-policy가 아닌 offline data로 학습하면 distributional shift때문에 spurious solution을 학습해 성능이 하락한다고 논문에서 설명하고 있다.

## 7. Discussion

- 논문에서도 언급하지만 1 round 이상 iterative correction 못한 것을 limitation으로 이야기하고 있음
