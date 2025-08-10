---
categories:
- paper-reviews
date: '2024-04-30 00:00:00'
description: 논문 리뷰 - Evaluation Metric, RL 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- alignment
- diffusion
- evaluation metric
- generative
- language-model
- paper-review
- reinforcement-learning
- rl
- vision
thumbnail: assets/img/posts/2024-04-30-training-diffusion-modelse-with-reinforcement-learning/thumbnail.jpg
title: Training diffusion modelse with reinforcement learning
---

**논문 정보**
- **Date**: 2024-04-30
- **Reviewer**: 전민진
- **Property**: Evaluation Metric, RL

**한 줄 요약 : diffusion모델을 강화학습으로 원하는 obejective(그림 실사화, 압축 잘되는 그림 등)에 바로 최적화하자!**

## Abstract

- diffusion models은 log-likelihood objective를 근사시켜 학습하는 flexible generative models

- diffusion모델로 사람들이 원하는 목표는 human-perceived image quality or drug effectiveness와 같은 downstream objective

- denoising과정을 multi-step decision-making problem으로 보고, policy gradient algorithm을 접목하는 방법론을 제안, 이를 DDPO(denoising diffusion policy optimization)이라 명명

- 해당 방법론을 적용할 경우, prompting으로 표현하기 어려운 image compressibility나 human feedback에서 파생되는 aesthetic quality를 objective로 adaptation 가능

## Introduction

- diffusion model의 핵심 아이디어는 sequential denoising process를 통해 단순한 prior distribution을 여러 번 변형시켜서 target distribution으로 만드는 것

- 하지만 대부분의 diffusion model 활용 사례는 likelihood에 직접적인 관련이 있지 않고, 오히려 downstream objective과 연관이 있음

- 따라서, 본 논문에서는 data distribution을 matching하는 것보단 이러한 objective를 바로 만족하도록 diffusion model을 학습하는 문제에 초점을 둠

- denoising을 multi-step decision-making task로 보는 방법론을 제안, 전체 denoising process 과정을 근사한 likelihood를 사용하는 것이 아니라 각 denoising step에서의 정확한 likelihood를 사용

- 본 논문의 저자들은 큰 text-to-image diffusion model을 finetuning하는데에 해당 알고리즘을 적용

- 본 논문의 contribution은 다음과 같음

## Related Work

- Diffusion probailistic models

- Controllable generation with diffusion models

- Reinforcement learning from human feedback

- Diffusion models as sequential decision-making processes

## Preliminaries

- Diffusion models

- Markov decision processes and reinforcement learning

## Reinforceement learning training of diffusion models

- Problem statement

- Reward-weighted regression

- Denoising diffuion policy optimization

- policy gradient estimation

## Reward functions for text-to-image diffusion

- Compessibility and Incompessibility

- Aesthetic quality

- Automated prompt alignment with vision-language models

## Experimiental evaluation

실험의 목표는 RL algorithm을 사용해 diffufsion model을 다양한 user-specified objective와 align이 되도록 finetuning, 그 효과를 평가하는 것

1. DDPO의 여러 버전과 RWR의 비교

1. VLM을 manually하게 명시하기 어려운 reward를 최적화 하는데 사용할 수 있는가?

1. RL finetuning의 효과는 finetuning시에 보지 못한 prompt에 대해서도 적용될 수 있는가?

- Experiment details

- Algorithm comparision

- Automated prompt alignment

- Generalization

## Discussion and Limitations

- denoising diffuion model을 바로 다양한 reward function에 최적화할 수 있는 RL기반의 framework를 제안

- iterative denoising procedure를 multi-step decision-making problem으로 보고, policy gradient algorithm을 설계, 효율적으로 diffusion model을 학습

- DDPO는 prompt로 명시하기 어렵고, 프로그래밍 적으로 평가하기 어려운 taks에 대해서 매우 효과적으로 최적화 하는 방법론

- 향후 과제로, 
