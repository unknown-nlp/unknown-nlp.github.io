---
categories:
- paper-reviews
date: '2025-03-25 00:00:00'
description: 논문 리뷰 - Reinforcement Learning, SFT 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- fine-tuning
- language-model
- llm
- paper-review
- reasoning
- reinforcement learning
- reinforcement-learning
- rlhf
- sft
thumbnail: assets/img/posts/2025-03-25-reft-reasoning-with-reinforced-fine-tuning/thumbnail.jpg
title: 'ReFT: Reasoning with Reinforced Fine-Tuning'
---

**논문 정보**
- **Date**: 2025-03-25
- **Reviewer**: 김재희
- **Property**: Reinforcement Learning, SFT

## 1. Intro

## preliminaries

### PPO

- Original RLHF Objectives

- PPO Objectives

### RLHF

{% include figure.liquid loading="eager" path="assets/img/posts/2025-03-25-reft-reasoning-with-reinforced-fine-tuning/image_000.png" class="img-fluid rounded z-depth-1" %}

**Training language models to follow instructions with human feedback**

- 방법론 목표: instruction을 따르는 “안전”하고 “사실적”이며 “믿을만”한 출력을 내도록 학습

### What makes reinforcement learning effective in LLM paradigm?

{% include figure.liquid loading="eager" path="assets/img/posts/2025-03-25-reft-reasoning-with-reinforced-fine-tuning/image_001.png" class="img-fluid rounded z-depth-1" %}

- diversity of trajactory: 질문과 정답은 하나지만, 과정은 다양하니까.

## 2. Method

### Main Research Question

{% include figure.liquid loading="eager" path="assets/img/posts/2025-03-25-reft-reasoning-with-reinforced-fine-tuning/image_002.png" class="img-fluid rounded z-depth-1" %}

- 논문 요약

### Notations

- CoT ( \textbf{e}): CoT trajactory including final answer

- state: all tokens including question and generated so far

- policy model( \pi_\theta): 학습 대상 모델 

### Objectives

- SFT

- RL: RLHF 수식과 동일합니다. 

{% include figure.liquid loading="eager" path="assets/img/posts/2025-03-25-reft-reasoning-with-reinforced-fine-tuning/image_003.png" class="img-fluid rounded z-depth-1" %}

- value loss: Value model의 linear 학습을 위해 쓰이는듯

### Algorithm

{% include figure.liquid loading="eager" path="assets/img/posts/2025-03-25-reft-reasoning-with-reinforced-fine-tuning/image_004.png" class="img-fluid rounded z-depth-1" %}

### Dataset

- SFT 때 활용된 데이터를 그대로 활용 가능

### Reward function

- fine-tuning을 위해 가장 중요한 설계 요소

- 논문에서는 단순하게 접근

### Training Reward Model 

### Reranking & Majority Voting

학습된 모델에 대한 추가적인 성능 개선 방법론

- Reranking: test query 당 100개의 generation 진행

- majority voting: test query 당 100개의 generation 진행

## 3. Baselines

- SFT: 기존에 마련된 학습 데이터를 활용하여 SFT 학습

- Offline Self-training: SFT (warm up) 학습이 된 모델 이용

- Online Self-training: 학습 과정 중인 모델에 대해 offline과 동일하게 생성 → filtering → SFT 진행

### Hyperparameters

**ReFT**

- 8 x A100 80GB

- SFT epoch: 2

- RLHF epoch: 300 → 지속적으로 성능이 개선되어서 학습을 오래 시켰다고 표현

**SFT**

- epoch: 40 → 성능 개선이 없어 여기서 중단했다고 표현

**Offline Self-training**

- SFT epoch: 40

- self-training epoch: 20 → 성능 개선이 없어 여기서 중단했다고 표현

## 4. Experiments

### Reasoning type

- N-CoT: reasoning을 자연어로 진행

- P-CoT: reasoning을 코드로 진행

### Answer Type

- GSM8K, SVAMP: numeric, 실제 정답 숫자 예측 태스크

- MathQA: multiple choice, 4지선다

### Main Result

{% include figure.liquid loading="eager" path="assets/img/posts/2025-03-25-reft-reasoning-with-reinforced-fine-tuning/image_005.png" class="img-fluid rounded z-depth-1" %}

- ReFT

- Self-training

### Reward Hacking for MathQA

- MathQA: 4지선다 예측 문제

- MathQA를 직접 정답 숫자 예측 문제로 전환하여 실험 진행

### Majority Voting & Reward Reranking

{% include figure.liquid loading="eager" path="assets/img/posts/2025-03-25-reft-reasoning-with-reinforced-fine-tuning/image_006.png" class="img-fluid rounded z-depth-1" %}

- 추가 데이터 annotation을 이용하지 않고도 annotated data를 활용하는 방법론들과 유사한 성능 도출

### ReFT w/ small models

- RLHF 프레임워크의 핵심

### Ablation Study

- KL coefficient 를 지우면 LLM의 본래 파라미터에서 멀어져서 학습이 실패

- 별도의 value model을 사용하는 경우 더 빠르게 모델이 수렴하는 것을 확인

{% include figure.liquid loading="eager" path="assets/img/posts/2025-03-25-reft-reasoning-with-reinforced-fine-tuning/image_007.png" class="img-fluid rounded z-depth-1" %}

### Human Evaluation

- reasoning의 품질이 얼마나 좋은지 3가지 척도(Logic, Naming, Compactness)로 평가 진행

- ReFT가 더 나은 모습을 보임

{% include figure.liquid loading="eager" path="assets/img/posts/2025-03-25-reft-reasoning-with-reinforced-fine-tuning/image_008.png" class="img-fluid rounded z-depth-1" %}

### When ReFT surpasses SFT?

{% include figure.liquid loading="eager" path="assets/img/posts/2025-03-25-reft-reasoning-with-reinforced-fine-tuning/image_009.png" class="img-fluid rounded z-depth-1" %}

- SFT warmup step을 달리하며 실험 진행 
