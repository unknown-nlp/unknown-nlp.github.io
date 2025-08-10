---
categories:
  - paper-reviews
date: "2024-05-27 00:00:00"
description: 논문 리뷰 - RLHF 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
  - alignment
  - classification
  - fine-tuning
  - llm
  - paper-review
  - rlhf
thumbnail: assets/img/posts/2024-05-27-understanding-the-performance-gap-between-online-and-offline/thumbnail.jpg
title: Understanding the performance gap between online and offline alignment algorithms
---

**논문 정보**

- **Date**: 2024-05-27
- **Reviewer**: 전민진
- **Property**: RLHF

## Abstract

- RLHF은 요즘 LLM alignment를 위한 근본 방법론으로 자리 잡음

- RLHF를 크게 online, offline alignmnt algorithm으로 나눠서, 둘의 성능 차이가 어떠한 원인에서 발생하는지 분석해보고자 함

## Preliminary

- **on-policy, off-policy, online, offline**

## Introduction

> **_Is online RL necessary for AI alignment?_**

- offline RL(DPO)같은 방법론의 경우 online RLHF에 비해서 훨씬 간단하고 연산량도 적음

- 과연 offline RL로도 충분히 alingment가 가능한지를 분석

- online vs offline algorithms

## Comparing online and offline performance under Goodhart’s law

- 우선 online과 offline alignment method가 성능 차이가 나는지를 확인

- 면밀한 비교를 위해 둘다 IPO loss 사용, 차이는 \mu = \pi\_\theta(online), \mu = D(offline)

{% include figure.liquid loading="eager" path="assets/img/posts/2024-05-27-understanding-the-performance-gap-between-online-and-offline/image_000.png" class="img-fluid rounded z-depth-1" %}

- Online achieves better budget and performance trade-off than offline

## Hypotheses for the performance discrepancy

같은 데이터셋으로 학습하는데 왜 on, offline 모델이 성능 차이가 나는지 확인하기 위해 가설 설정

- Hypothesis 1 : Data coverage

- Hypothesis 2 : sub-optimal offlifne dataset

- Hypothesis 3 : Better classification better performance

- Hypothesis 4 : Non-contrastive loss function

- Hypothesis 5 : Scaling policy is all you need

\***\* 실험 세팅**

- controlled setting to study KL vs. performance trade-off

- supervised fine-tuning

- evaluation

- hyper-parameter

## Investigating the hypotheses

### Hypothesis 1 : Data coverage

: on, off의 성능 차는 데이터의 다양성에서 기인할 것

⇒ online 학습에서 사용되는 데이터셋을 shuffle, 이를 바탕으로 offline 학습을 해보자

(shuffle안하면 online과 똑같음)

{% include figure.liquid loading="eager" path="assets/img/posts/2024-05-27-understanding-the-performance-gap-between-online-and-offline/image_001.png" class="img-fluid rounded z-depth-1" %}

- offline with d_online-shufflfe이 offline에 비해 근소한 성능 향상을 보였으나, 기존과 큰 차이 없었음

- 결론 : data coverage때문은 아님

### Hypothesis 2 : Sub-optimal offline dataset

: offline dataset이 sub-optimal해서 offline 성능이 낮은 것이다

{% include figure.liquid loading="eager" path="assets/img/posts/2024-05-27-understanding-the-performance-gap-between-online-and-offline/image_002.png" class="img-fluid rounded z-depth-1" %}

- red dot : online policy로 4k step만큼 학습한 모델로 response sampling, golden preference로 다시 라벨링한 데이터로 학습

- 실험 결과, 성능에 도움 안됨

### Hypothesis 3 : Better classification, better performance

: preference classification을 잘하면, policy의 성능이 높을 것이다

→ 1) proxy preference model이 policy를 classifier로 쓰는 것보다 높은 classification 성능을 보일 것

    2) online과 offline의 성능 차이는 이러한 classification accuracy의 차이에서 기인했을 수도 있다

\*\* policy는 preference classifier라고 볼 수 있음

{% include figure.liquid loading="eager" path="assets/img/posts/2024-05-27-understanding-the-performance-gap-between-online-and-offline/image_003.png" class="img-fluid rounded z-depth-1" %}

\*\*preference model은 policy를 classifier로 쓰는거보다 더 expressive version이라고 볼 수 있음

> > 왜지??? 그냥 likelihood가 아니라 score를 학습하도록 해서? 잘 모르겠다…

{% include figure.liquid loading="eager" path="assets/img/posts/2024-05-27-understanding-the-performance-gap-between-online-and-offline/image_004.png" class="img-fluid rounded z-depth-1" %}

- 실험 세팅

- 실험 결과, 학습할수록 on-policy dataset이 기존의 preference dataset과 멀어짐

{% include figure.liquid loading="eager" path="assets/img/posts/2024-05-27-understanding-the-performance-gap-between-online-and-offline/image_005.png" class="img-fluid rounded z-depth-1" %}

- classifier 성능에 따른 policy자체의 성능(win rate)에 관한 장표

- 실험 결과, classifier의 성능과 policy 자체의 성능은 큰 연관성이 없었다..

{% include figure.liquid loading="eager" path="assets/img/posts/2024-05-27-understanding-the-performance-gap-between-online-and-offline/image_006.png" class="img-fluid rounded z-depth-1" %}

- 각 방법론의 학습 정도에 따른 classifier 성능과, D_golden에서 y_w의 relative log probs를 측정

- (figure 8, top row) online의 classification accuracy가 낮은 것을 확인할 수 있음

- (figure 8, bottom row) offline방식의 경우 winning response의 logit을 높이는 방식이 아니라 둘다 logit을 낮추되, losing response의 logit을 훨씬 크게 낮추는 방식으로 학습

### Hypothesis 4 : Non-contrastive loss function

: off가 on보다 성능이 낮은 이유는 loss function이 contrastive 구조이기 때문

→ 데이터의 품질에 더 많은 영향을 받음

⇒ loss fuction을 SFT느낌으로 바꿔서 실험해보자

{% include figure.liquid loading="eager" path="assets/img/posts/2024-05-27-understanding-the-performance-gap-between-online-and-offline/image_007.png" class="img-fluid rounded z-depth-1" %}

{% include figure.liquid loading="eager" path="assets/img/posts/2024-05-27-understanding-the-performance-gap-between-online-and-offline/image_008.png" class="img-fluid rounded z-depth-1" %}

- Bo2에서도 on,offline의 성능 차이는 비슷

- chat arena sxs에서는 Bo2를 사용한 on, off성능이 유사

### Hypothesis 5 : Non-contrastive loss function

: policy model을 scaling up → 3B, 11B로도 학습 (자원때문에 batch size 낮춤)

{% include figure.liquid loading="eager" path="assets/img/posts/2024-05-27-understanding-the-performance-gap-between-online-and-offline/image_009.png" class="img-fluid rounded z-depth-1" %}

- scaling up하면 model의 peak성능이 높아지긴 함

- scaling up해서 실험한 결과, 모델이 작을 때와 유사하게 overoptimization문제를 발견

{% include figure.liquid loading="eager" path="assets/img/posts/2024-05-27-understanding-the-performance-gap-between-online-and-offline/image_010.png" class="img-fluid rounded z-depth-1" %}

- 모델 크기를 키웠더니 offine with D_online-shuffle 성능이 크게 향상되긴 함

## Making the dataset more on-policy improves offline learning

어떻게 데이터셋을 구축해야 offline learning의 성능을 향상시킬 수 있을까? 에 대한 ablation study

- 3가지 버전의 데이터셋을 구축

{% include figure.liquid loading="eager" path="assets/img/posts/2024-05-27-understanding-the-performance-gap-between-online-and-offline/image_011.png" class="img-fluid rounded z-depth-1" %}

- 실험 결과, 학습데이터가 어느정도 SFT와 분포가 유사해야 잘 작동

- 응답 간의 퀄 차이만으로는 성능이 향상되지 않았음

## Summary

- Online과 offline의 성능을 budget 측면에서 비교했을 때, online이 성능이 우월

- 요즘 하도 다양한 RL방법론이 등장하고 있어서, 이들 사이에 차이가 발생해 성능이 차이나는지 분석하는 것도.. 좋을듯
