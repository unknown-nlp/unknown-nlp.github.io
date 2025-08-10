---
categories:
- paper-reviews
date: '2024-06-11 00:00:00'
description: 논문 리뷰 - LLM, Interpretability 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- interpretability
- language-model
- llm
- multimodal
- paper-review
- transformer
thumbnail: assets/img/posts/2024-06-11-scaling-monosemanticity-extracting-interpretable-features-from-claude-3/thumbnail.jpg
title: 'Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet'
---

**논문 정보**
- **Date**: 2024-06-11
- **Reviewer**: 상엽
- **Property**: LLM, Interpretability

# Introduction

AI safety에 관심이 매우 큰 anthropic

이전 연구 (Towards Monosemanticity: Decomposing Language Models With Dictionary Learning)에서  one-layer transformer에 Sparse AutoEncoder (SAE)를 이용해 monosemanric features를 복구할 수 있다는 사실을  발견

**이것이 실제로 SOTA transformer 모델에도 적용이 가능할 것인가?**

- 실제 어떤 컨셉과 feature를 연결지을 수 있다면 AI safety에 직접적인 연결이 가능할 것이다

이번 논문에서는

- Anthropic’s medium-sized production model, Claude 3 Sonnet을 이용

- 기존보다 더 다양하고 큰  Sparse Autoencoder (SAE)를 활용해서 다양한 feature를 탐색

- Feature의 존재 확인 → Feature를 이용한 모델 행동 제어 확인

- Multilingual, Multimodal에서 역시 feature가 동일하게 잘 작용함을 확인

- 특히, Safety feature가 존재함을 확인할 수 있었음

- 향후 연구 및 모델 확장을 위한 SAE의 scaling law 실험 진행

# **Scaling Dictionary Learning to Claude 3 Sonnet**

### Preliminaries

link : https://transformer-circuits.pub/2022/toy_model/index.html#motivation

신경망은 입력된 데이터를 처리하여 특정 feature를 고차원 space에 방향(direction)으로 표현한다고 생각할 수 있음.

example

신경망의 내부 작동 방식을 이해하고 분석한다 (reverse engineering)의 관점에서 네트워크가 만드는 representation이 다음과 같은 특징을 가졌는지를 확인하는 것은 필수적임.

- Decomposability : Network representation은 독립적으로 이해될 수 있는 feature로 설명될 수 있다. (비슷한 특징을 가진 feature들은 특정 군집을 형성한다.)

- Linearity : Feature는 방향에 의해 표현되어진다.

→ 위의 개념은 매우 추상적인 개념이라 명확한 증거, 증명을 찾을 수는 없지만 여러 차례 실험적 결과가 뒷받침해준다고 믿을 수 있지 않을까?

위의 특성이 명확히 보이는 사례와 아닌 사례의 차이점은 어떻게 설명할 수 있을까?

- **Superposition:** 활성화 공간 내 (제한된 차원)에서 더 많은 의미를 표현하기 위해 여러 의미를 중첩적으로 가짐.

→ 결론적으로 Sparse한 Feature를 이용해 

### Dictionary learning

- 위의 결론에 대한 해답은 Sparse Autoencoder와 같은 dictionary learning 방식을 이용해 feature를 분석하는 것!

- Dictionary learning: 데이터를 보다 간단한 벡터들의 선형 결합으로 표현하는 것

- 현재까지 SAE를 이용한 연구는 매우 작은 모델을 분석하는 정도로 한정되어 있으며 이것이 SOTA 모델과 같은 LLM에서 어떤 양상을 보일지는 모른다 → 우리가 하겠다!
