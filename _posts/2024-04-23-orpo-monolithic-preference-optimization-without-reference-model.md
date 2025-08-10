---
categories:
  - paper-reviews
date: "2024-04-23 00:00:00"
description: 논문 리뷰 - Alignment 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
  - alignment
  - fine-tuning
  - paper-review
  - reinforcement-learning
  - rlhf
thumbnail: assets/img/posts/2024-04-23-orpo-monolithic-preference-optimization-without-reference-model/thumbnail.jpg
title: "ORPO: Monolithic Preference Optimization without Reference Model"
---

**논문 정보**

- **Date**: 2024-04-23
- **Reviewer**: 건우 김
- **Property**: Alignment

# Abstract

최근에 LM에 preference alignment에 supervised fine-tuning (SFT)가 많이 활용되고 있음. 본 연구에서 minor한 disfavored generations style로 SFT 중에 penalty를 주는 것이 preference-alignment에 다다르기에 충분하다는 것을 보여줌.

- ORPO algorithm은 기존 방법론과 달리 preference alignment tuning 단계 및 reference model이 별도로 필요하지 않음

- Odds ratio가 125M~7B 크기 model의 SFT에서 favored / disfavored style을 구분 짓는데 적절하다는 것을 실험 및 이론적으로 증명함.

# Introduction

Large corpus로 학습한 PLMs이 general-domain applications에 사용되기 위해서는 instruction tuning 혹은 preference alignment 과정이 필요함.

본 연구에서 pairwise preference dataset이 model alignment에 있어 SFT에 어떤 영향을 주는지 확인하고, 새로운 효과적인 preference alignment algorithm을 제안함.

# Related Works

### Alignment with Reinforcement Learning (RLHF)

- **SFT Training**

- **Reward model Training**

- **RLHF Training**

### Alignment without Reward Model (DPO)

Reward modeling 단계를 preference learning에 포함시켜 별도의 reward model이 필요없이 alignment 학습 가능

1. **SFT Training** (위와 동일)

1. **DPO Training**

### Alignment with Supervised Fine-Tuning

LIMA (2023)와 같이 Human-aligned model을 소량의 high quality dataset (filtered dataset)만 가지고 SFT로 만들 수 있다는 연구들도 등장함

→ SFT의 effectiveness를 보여주긴 했지만, 아직까지 preference alignment를 SFT에 통합 시키는 것에 대한 theoretical background가 부족

# The Role of Supervised Fine-tuning

Preference alignment에서 Initial stage로 사용되는 SFT의 loss function과 preference comprehension ability에 대한 분석

- Cross-Entropy Loss

SFT는 PLM을 특정 domain에 맞춰 학습 시킬때 주요 역할을 담당하는데, 이는 undesirable style로 token을 생성하는 것에 대한 Likelihood를 높이는 문제가 존재함 (아래 Figure 확인).

위 figure에서 Rejected response에 대한 log probability 값이 (unwanted generation에 대한 penalty 부재로 인해) 학습할 수록 계속 커지는 것이 관찰됨.

→ 따라서, SFT의 domain adaptaion을 유지하며 unwanted generation styles을 완화시키는 방법이 필요함

- **Penalizing Undesired Generations**

### Odds Ratio Preference Optimization (ORPO)

Odds ratio 기반의 penalty를 기존 CE Loss와 결합하여 Favored response와 disfavored response 간의 style 차이를 구분이 가능

{% include figure.liquid loading="eager" path="assets/img/posts/2024-04-23-orpo-monolithic-preference-optimization-without-reference-model/image_000.png" class="img-fluid rounded z-depth-1" %}

{% include figure.liquid loading="eager" path="assets/img/posts/2024-04-23-orpo-monolithic-preference-optimization-without-reference-model/image_001.png" class="img-fluid rounded z-depth-1" %}

직관적으로 odds(y|x)=k 가 의미하는 것은 model이 output sequence y를 생성하는 확률이 그렇지 않은 경우보다 k배 높음을 의미하기에,

{% include figure.liquid loading="eager" path="assets/img/posts/2024-04-23-orpo-monolithic-preference-optimization-without-reference-model/image_002.png" class="img-fluid rounded z-depth-1" %}

가 의미하는 바를 ‘model이 rejected response보다 chosen response를 얼마만큼 더 잘 생성하는 정도’로 볼 수 있음.

- **ORPO’s objective function**

- **Gradient of ORPO**

{% include figure.liquid loading="eager" path="assets/img/posts/2024-04-23-orpo-monolithic-preference-optimization-without-reference-model/image_003.png" class="img-fluid rounded z-depth-1" %}

- Penalize wrong prediction

- Contrasts between chosen and rejected responses

# Experimental Settings

- Model

- Training dataset

- Reward Models

- Leaderboard evaluation

# Results and Analysis

- **Single-turn instruction following **

- **Multi-turn instruction following**

- **Reward win-rate**

- **Reward Distribution**

# Discussion

{% include figure.liquid loading="eager" path="assets/img/posts/2024-04-23-orpo-monolithic-preference-optimization-without-reference-model/image_004.png" class="img-fluid rounded z-depth-1" %}

- ORPO는 SFT의 domain adpaptaion을 잘 유지하며 OR이 unwanted generation token에 대한 Penalty를 잘 주고 있는 것을 볼 수 있음.

- 학습이 진행됨에 따라 odds ratio 값도 점점 커짐 → penalty를 잘 줌

# Conclusion

- Reference-free monolithic preference alignment method인 ORPO을 제안

- RLHF, DPO 대비 비교적 간단하고 효과적인 방법으로 preference alignment 학습이 가능
