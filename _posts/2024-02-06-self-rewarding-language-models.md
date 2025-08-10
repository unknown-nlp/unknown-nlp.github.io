---
categories:
- paper-reviews
date: '2024-02-06 00:00:00'
description: 논문 리뷰 - Instruction Tuning 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- alignment
- fine-tuning
- instruction tuning
- language-model
- llm
- paper-review
- reasoning
- reinforcement-learning
- rlhf
thumbnail: assets/img/posts/2024-02-06-self-rewarding-language-models/thumbnail.jpg
title: Self-Rewarding Language Models
---

**논문 정보**
- **Date**: 2024-02-06
- **Reviewer**: 상엽
- **Property**: Instruction Tuning

# Introduction

**Self-Rewarding Language Models**

- LLM 자체가 reward를 계산하는 LLM-as-a-Judge 모델

human preference와 LLM을 align 시키는 것은 instruction following performance를 큰 폭으로 향상시킬 수 있음. 

아래는 대표적은 예시

- RLHF (Reinforcement Learning from Human Feedback) : 

- DPO (Direct Preference Optimization)

- **Self-Rewarding**

{% include figure.liquid loading="eager" path="assets/img/posts/2024-02-06-self-rewarding-language-models/image_000.png" class="img-fluid rounded z-depth-1" %}

Iterative DPO procss를 이용해 학습

1. Starting from seed model (Llama 70b, fine-tuned on Open Assistant)

1. 아래 Iteration 진행

→ Instruction following performance 향상

→ 학습 과정에서 reward model이 지속적으로 업데이트 가능!!

# Self-Rewarding Language Models

준비물

- base pretrained language model

- small amount of human-annotated seed data

아래 두 가지 능력을 모두 갖춘 모델을 만들자.

1. **Instruction following**: given a prompt that describes a user request, the ability to **generate a high quality, helpful (and harmless) response. **(원래의 task도 잘하며)

1. **Self-Instruction creation**: the ability to **generate and evaluate new instruction- following examples** to add to its own training set. (reward까지 가능한)

### Initialization

아래 두 데이터를 모두 이용해서 fine-tuning 진행.

**Instruction Fine-Tuning (IFT) data**

- human-authored (instruction prompt, response) general instruction following examples

- Supervised fine-tuning (SFT)에 이용

- perfect score (여기선 5점)을 받은 response들만 데이터셋에 추가

**Evaluation Fine-Tuning (EFT) data.**

- (evaluation instruction prompt, evaluation result response) examples

- LLM-as-a-Judge prompt 사용

- DPO를 이용한 학습이 아닌 supervised fine-tuning에 사용된다는 것이 이후 preference data와 차이점.

- 필수적이진 않다고 하나 성능적으로 도움이 되었기 때문에 사용한다고 함. (이게 필수적이란 말인 거 같은데)

- Justification (CoT reasoning) → final score (0~5점)으로 구성 됨.

### Self-Instruction Creation

학습하며 자신의 training data를 스스로 수정할 수 있는 모델. 아래의 3단계 절차로 진행

1. **Generate a new prompt** : IFT 데이터 샘플링을 통해 few-shot example 제공, 새로운 prompt x_i 생성

1. **Generate candidate responses** : N개의 candidate response 생성 \{y_{i}^{1},...,y_{i}^{N}\}

1. Evaluate candidate responses: 동일 모델에서 LLM-as-a-Judge ability 이용 N개의 candiate에 대해 reward 평가 진행. (r_{i}^{n} \in [0, 5])

### Instruction Following Training

AI (Self-)Feedback을 통한 추가 학습 데이터 생성

**AI Feedback Training**

- Prefereence pairs

- Positive example only

→ preference pairs를 사용할 때 더 좋은 성능을 보였음.

### Overall Self-Alignment Algorithm

M_1,...,M_T : a series of model where each successive model t uses augmented training data created by the t − 1th model

\text{AIFT}(M_T) : AI Feedback Training data created using model Mt.

M0 : Base pretrained LLM with no fine-tuning.

M1 : Initialized with M0, then fine-tuned on the IFT+EFT seed data using SFT.

M2 : Initialized with M1, then trained with AIFT(M1) data using DPO.

M3 : Initialized with M2, then trained with AIFT(M2) data using DPO.

(This iterative training resembles the procedure used in Pairwise Cringe Optimization and Iterative DPO introduced in Xu et al. [2023]; however, an external fixed reward model was used in that work.) 

{% include figure.liquid loading="eager" path="assets/img/posts/2024-02-06-self-rewarding-language-models/image_001.png" class="img-fluid rounded z-depth-1" %}

# Experiment

Llama 2 70B를 base 모델로 이용.

### **Seed Training Data**

- IFT Seed Data

- EFT Seed Data

### **Evaluation Metrics**

- Instruction Following

- Reward Modeling

### **Training Details**

**Instruction folowing training**

- SFT

- DPO

**Self-Instrction creation**

- Generation of new prompts : fixed Llama 2-Chat 70B with 8-shot prompting

- the other parts of the creation pipeline (generating the response, and evaluating it) use the model being trained. 

# Results

### Instruction Following Ability

**EFT+IFT seed training performs similarly to IFT alone**

- ** Iteration 1 (M1, **IFT + EFT data) vs SFT Baseline (Only IFT data)

→ 긍정적인 결과 : EFT 데이터를 학습해 reward 모델링을 진행해도 다른 task의 ability가 떨어지지 않는다.

→ 계속 iteration을 진행하자!

**Iteration 2 (M2) improves over Iteration 1 (M1) and SFT Baseline **

- Iteration 2 (M2) vs Iteration 1 (M1)

- Iteration 2 (M2) vs  SFT baseline

M2에서부턴 명확한 성능 향상을 확인할 수 있음.

**Iteration 3 (M3) improves over Iteration 2 (M2) **

- Iteration 3 (M3) vs Iteration 2 (M2) 

- Iteration 3 (M3) vs SFT baseline

→ M3는 M2와 비교해도 상당한 향상이 있었음.
