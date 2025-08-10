---
categories:
  - paper-reviews
date: "2024-07-23 00:00:00"
description: 논문 리뷰 - Reasoning, Reinforcement Learning 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
  - alignment
  - llm
  - paper-review
  - reasoning
  - reinforcement learning
thumbnail: assets/img/posts/2024-07-23-step-dpo-step-wise-preference-optimization-for-long/thumbnail.jpg
title: "Step-DPO : Step-wise preference optimization for long-chain reasoning of LLMs"
---

**논문 정보**

- **Date**: 2024-07-23
- **Reviewer**: 전민진
- **Property**: Reasoning, Reinforcement Learning

## Abstract

- 기존 LLM이 mathematical reasoning를 푸는 것은 큰 challenge, 이를 개선하기 위해 human feedback을 바탕으로 모델의 robustness와 factuality를 향상시키려 함

- 이러한 방법론 중 하나인 DPO의 경우, 틀린 답변에서 디테일한 에러를 식별하기 어렵다는 한계가 존재

- 이를 개선하기 위해, 전체적으로 답변을 평가하기 보다 각각의 reasoning step에 대해 preference optimization을 하는 방법론인 Step-DPO를 제안

- 실험 결과, 기존의 DPO보다 더 높은 성능을 보이고, 특히 Qwen2-72B-Instruct에 적용했을 때, MATH, GSM8K데이터셋에 대해 각각 70.8%(+1.4), 94.0%(+1.6)의 성능을 보임

{% include figure.liquid loading="eager" path="assets/img/posts/2024-07-23-step-dpo-step-wise-preference-optimization-for-long/image_000.png" class="img-fluid rounded z-depth-1" %}

## Introduction

- 기존에는 alignment를 강화하기 위한 SFT 단계에서의 여러 data augmentation techinque들이 제안됨

- 하지만 이러한 SFT 과정에서 hallunication을 야기할 수 있음

- 최근, DPO가 여러 chat benchmark에서는 효과적이었으나, long-chain mathematical reasoning에서는 저조한 성능 향상을 보임

- 본 논문에선, Step-DPO를 소개, 중간의 각 reasoning step을 preference optimization의 basic unit으로 상정

## Related Works

- Mathematical reasoning

## Step-DPO

{% include figure.liquid loading="eager" path="assets/img/posts/2024-07-23-step-dpo-step-wise-preference-optimization-for-long/image_001.png" class="img-fluid rounded z-depth-1" %}

### Step-wise formulation

- DPO

- Step-DPO

### In-distribution data construction

- Step-DPO로 학습하기 위해선 step-wise preference dataset이 필요

- 이를 위해 3가지 단계(error collection, step localization, rectification)로 구성된 파이프라인을 제안

## Experiments

### Experimental setup

- Network architecture

- Dataset

- Implementation Details

### Result

{% include figure.liquid loading="eager" path="assets/img/posts/2024-07-23-step-dpo-step-wise-preference-optimization-for-long/image_002.png" class="img-fluid rounded z-depth-1" %}

- 어떤 크기의 모델이든, Step-DPO를 했을 때 성능이 향상됨

{% include figure.liquid loading="eager" path="assets/img/posts/2024-07-23-step-dpo-step-wise-preference-optimization-for-long/image_003.png" class="img-fluid rounded z-depth-1" %}

- AIME 2024, Odyssey-MATH에 대한 실험..?이라고 하는데 자세한게 안나와 있음. 암튼 DPO보다 우월한 성능을 보인다!

{% include figure.liquid loading="eager" path="assets/img/posts/2024-07-23-step-dpo-step-wise-preference-optimization-for-long/image_004.png" class="img-fluid rounded z-depth-1" %}

- 이 장표 역시 MATH test datset에 대한 DPO와 step-DPO의 성능을 보여줌

### Ablation study

- Out-of-Distribution vs In-Distribution Data

{% include figure.liquid loading="eager" path="assets/img/posts/2024-07-23-step-dpo-step-wise-preference-optimization-for-long/image_005.png" class="img-fluid rounded z-depth-1" %}

### Demonstrations

- Step-DPO로 학습하니까 reasoning step에서 detailed error가 발생하지 않았다!

{% include figure.liquid loading="eager" path="assets/img/posts/2024-07-23-step-dpo-step-wise-preference-optimization-for-long/image_006.png" class="img-fluid rounded z-depth-1" %}

## Summary

- 최종 답만을 기반으로 DPO를 하는 것이 아니라, 중간 과정도 신경쓰는 step-DPO를 제안

- 모델 크기, 종류와 상관없이 step-DPO를 사용하는 것이 성능 향상에 도움이 됨

- 아이디어 자체는 훌륭하나 아직 쓰는중?이라 그런지 실험이 살짝 부실

- 어떻게 reasoning step 중간에서 feedback을 줄 수 있을지가 궁금했는데, 이런식으로 간단?하게 해결할 수 있다는 것을 알게됨.
