---
categories:
  - paper-reviews
date: "2025-06-03 00:00:00"
description: 논문 리뷰 - Reinforcement Learning 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
  - language-model
  - llm
  - paper-review
  - reinforcement learning
  - reinforcement-learning
thumbnail: assets/img/posts/2025-06-03-reinforcement-learning-finetunes-small-subnetworks-in-large-language/thumbnail.jpg
title: Reinforcement Learning Finetunes Small Subnetworks in Large Language Models
---

**논문 정보**

- **Date**: 2025-06-03
- **Reviewer**: 준원 장
- **Property**: Reinforcement Learning

## 1. Introduction

- 대부분의 연구에서 RL 수행 시 전체 파라미터에 대한 full finetuning이 일반적으로 적용된다고 주장한다.

{% include figure.liquid loading="eager" path="assets/img/posts/2025-06-03-reinforcement-learning-finetunes-small-subnetworks-in-large-language/image_000.png" class="img-fluid rounded z-depth-1" %}

→ RL과 SFT단계에서 누적된 그래디언트를 비교한 것으로, RL 단계의 업데이트는 대부분 희소한 반면, SFT 단계에서는 훨씬 밀도 높은 업데이트가 발생했음을 보여준다.

(무작위 시드, 훈련 데이터 구성 및 순서, 그리고 서로 다른 RL 알고리즘에 따라 학습된 서브네트워크들 간에도 강한 일관성이 관찰)

- θ\_{init}

- θ\_{full}: parameters after full RL finetuning from the initial model

- m ∈ {0,1}^{|θ\_{init}|}

- m*i = 1 \rightarrow (θ*{init} - θ\_{full})\_i ≠ 0

- m ⊙ ∇θ L(θ) : θ*{full}을 학습했을때와 같은 데이터로 θ*{init}때와 똑같이 학습

> **VS. LoRA**

- LoRA와 달리 subspace상에서 벡터공간을 학습시키는게 아니라, 적은 수의 파라미터를 업데이트를 하지만 파라미터 행렬이 표현할 수 있는 전체 부분공간에 근접하게 학습된다는 점에서 새로운 발견을 시사한다.

- 인위적으로 추가한 파라미터가 아닌, 자연스럽게 형성된 subnetwork을 finetuning함으로써 전체 모델 수준의 성능을 재현하거나 능가할 수 있음을 보여준다.

⇒ RL은 최적화를 일관되게 활성화되는 소규모 subnetwork에 집중시키며, 나머지 파라미터는 사실상 비활성 상태로 유지된다.

## 2. Related Work

### Lottery Ticket Hypothesis (ICLR, 2019)

- dense NN 내에 전체 모델의 성능을 단독으로 재현할 수 있는 희소한 subnetwork가 존재함을 주장

- LLM시대에서는 모델을 재학습하지 않고도 catastrophic forgetting을 완화할 수 있는 task specific subnetwork를 식별 (e.g., ties-merging)

- 사전학습된 언어모델 내 특정 지식을 인코딩하는 데 핵심적인 sparse subnetwork가 존재한다는 것도 실험적으로 밝혀냄

- 해당 ‘winning tickets’를 활용하여 학습 효율을 향상시키려는 시도들도 이루어지고 있음

> **VS. LTH**

- LTH는 pruning를 통해 ‘winning tickets’을 식별하는 반면, 본 연구는 (학습을 통해) 자연적으로 발생하는 subnetwork에 주목한다.

- LTH는 최종 모델의 성능이 재현 가능함을 보였지만, 본 연구는 성능뿐 아니라 **실질적으로 동일한 파라미터 값을 가진 모델**이 복원 가능함을 보여준다.

- LTH는 초기화 상태에서 학습된 모델을 대상으로 하는 반면, 본 연구는 사전학습된 LLM을 기반으로 finetuning하는 과정에 초점을 맞춘다.

### Background

### Update Sparsity

{% include figure.liquid loading="eager" path="assets/img/posts/2025-06-03-reinforcement-learning-finetunes-small-subnetworks-in-large-language/image_001.png" class="img-fluid rounded z-depth-1" %}

- θ\_{0}: ft 이전의 파라미터

- θ\_{1}: ft 이후의 파라미터

- ||\cdot ||\_{0}: non-zero 원소의 개수

**_ bfloat16 값이 절대 차이 10⁻⁵ 이하일 경우 동일한 값으로 간주 _**

### Learning from in-distribution data

- 논문에서 언급하는 ‘in-distribution’은 current policy와 분포가 유사한 data로 학습하는것

### KL-divergence regularization and gradient clipping in RL

- policy model이 reference 모델로부터 과도하게 이탈하는 것을 방지하기 위해 널리 사용되는 두 가지 기법**KL Regularization 및 Gradient Clipping**

- 둘다 PPO, GRPO, PRIME에 차용되나 Update Sparsity에 미치는 영향은 제한적

## 3. RL Induces Sparse but Full-rank Updates; SFT Induces Dense Ones

### Experiment Setup

- Hugging Face에서 공개한 다양한 모델에 대해 RL 수행 전후의 Update Sparsity을 정량적으로 측정

- **사전학습 → 지도학습 기반 파인튜닝(SFT) → RL**의 3단계 파이프라인을 따르는 LLM의 ‘RL과 SFT’ 단계 분석 (DeepSeek-R1-Zero처럼 사전학습에서 RL로 바로 학습하는 LLM도 포함)

### Result

{% include figure.liquid loading="eager" path="assets/img/posts/2025-06-03-reinforcement-learning-finetunes-small-subnetworks-in-large-language/image_002.png" class="img-fluid rounded z-depth-1" %}

{% include figure.liquid loading="eager" path="assets/img/posts/2025-06-03-reinforcement-learning-finetunes-small-subnetworks-in-large-language/image_003.png" class="img-fluid rounded z-depth-1" %}

- (accumulated gradients로 측정이 살짝 다르긴 하지만) SFT는 6%-15% sparsity를 보임

- 이전 연구들에서 밝혀낸 바와 동일한 결론에 이름

{% include figure.liquid loading="eager" path="assets/img/posts/2025-06-03-reinforcement-learning-finetunes-small-subnetworks-in-large-language/image_004.png" class="img-fluid rounded z-depth-1" %}

- 위의 실험으로 자연스러운 질문은 이러한 업데이트가 **low-rank** 인지 여부일텐덴데,

- DPO, PRIME, GRPO 등 다양한 모델에서 각 레이어의 업데이트 행렬 (\Delta \theta)의 평균 rank를 구한결과, 대부분의 업데이트 행렬이 거의 (>99%)를 보이며, 이는 sparse update임에도 업데이트가 모델의 전체 표현력 공간을 거의 포괄한다는 사실을 증명

{% include figure.liquid loading="eager" path="assets/img/posts/2025-06-03-reinforcement-learning-finetunes-small-subnetworks-in-large-language/image_005.png" class="img-fluid rounded z-depth-1" %}

## 4. Finetuning the Subnetwork Alone Can Reproduce the Full-finetuned Model

- RL이 주로 소규모 subnetwork을 finetuning한다는 점에서, 해당 연구는 다음 두 가지 연구 질문에 대해, 기존의 Lottery Ticket Hypothesis을 확장하는 형태로 고찰:

### Experiment Setup

- θ: Tulu

- θ\_{full}: parameters after full RL finetuning from the initial model

- θ\_{sub}: parameters after subnetwork RL finetuning from the initial model

- RL

### Result

- DPO → θ*{full} & θ*{sub} : **94.0% 파라미터 동일**

- PRIME → θ*{full} & θ*{sub} : **90.5% 파라미터 동일**

- 허용 오차 기준을 10⁻⁴로 완화할 경우, 두 모델은 **100% 동일한 파라미터 값을 가짐**

{% include figure.liquid loading="eager" path="assets/img/posts/2025-06-03-reinforcement-learning-finetunes-small-subnetworks-in-large-language/image_006.png" class="img-fluid rounded z-depth-1" %}

{% include figure.liquid loading="eager" path="assets/img/posts/2025-06-03-reinforcement-learning-finetunes-small-subnetworks-in-large-language/image_007.png" class="img-fluid rounded z-depth-1" %}

⇒ 논문 서두에서 언급한 conjecture를 실험적으로 완벽하게 증명하며, RL 훈련에서의 sparse update을 명시적으로 활용한 **효율적인 학습 전략**에 대한 가능성을 열어둠.

(post hoc으로 찾아낸 sparse parameter를 미리 알아내는건 future work!)

## 5. Consistency of Subnetworks Across Seeds, Data, and Algorithms

⇒ subnetwork가 일관성 있는 결과를 보인다면, 해당 subnetwork가 특정 학습 조건에 의한 우연의 결과가 아니라, 사전학습 모델에 내재된 **일반화 가능하고 RL로 transfer 가능한 구조**임을 시사

### Experiment Setup

- I_1, I_2: 업데이트된 파라미터의 인덱스 집합
