---
categories:
  - paper-reviews
date: "2025-02-04 00:00:00"
description: 논문 리뷰
giscus_comments: true
layout: post
related_posts: false
tags:
  - attention
  - bert
  - llm
  - paper-review
  - transformer
thumbnail: assets/img/posts/2025-02-04-ssm-hippo-lssl-s4-mamba-mamba2/thumbnail.jpg
title: SSM → HIPPO → LSSL → S4 → Mamba → Mamba2
---

**논문 정보**

- **Date**: 2025-02-04
- **Reviewer**: hyowon Cho

# BackGround

Google titans 모델이 등장하자마자 뜨거운 관심을 모으고 있습니다. 가장 큰 특징이라고 한다면, 헤게모니 아키텍쳐인 transformer가 아닌 sequential modeling을 베이스로 하는 아키텍쳐를 사용해서 transformer에 준하는 성능을 내고 있다는 것입니다.

이러한 관점이 titans에서 처음으로 시작된 것은 아닙니다. titans 이전에 State Space Model(SSM)을 활용한 mamba 모델이 sequential modeling의 주류를 차지하고 있었습니다. (titans에서도 mamba-based model들을 주 baseline 모델로 언급합니다)

> [State Space Model 기반의 efficient architecture 의 계보]

**HIPPO → LSSL → S4 → Mamba → Mamba2 → Samba, …**

개인적으로 대단한 것은 HIPPO부터 Mamba2까지 모두 CMU에 계신 Albert Gu 교수님이 모두 1저자로 작성하셨다는 것입니다. 따라서, 해당 흐름을 좇다보면 Albert Gu가 어떠한 아이디어를 기반으로 어떠한 한계를 해결하고자했는지 이해하기 용이할 것입니다.

따라서, 본 발표에서는 SSM의 개념을 소개하고, HIPPO부터 Mamba2까지 Albert Gu 교수님의 머릿속을 탐방해보는 시간을 가지도록 하겠습니다.

SSM으로 대표되는 sequential model들을 설명하기 이전에 먼저, 왜 transformer 이외의 아키텍쳐 연구가 필요한지 알아보겠습니다.

## 왜 Transformer 이외의 아키텍쳐가 필요한가

### **기존 Transformer의 문제점: Inference Cost**

Transformer는 Attention 메커니즘은 다음과 같은 특징을 가집니다:

- Attention은 근본적으로 전체 시퀀스에 대한 정보를 축약해 전달받는 것이 아닌, 각각의 정보에 알아서 접근하는 시스템. 따라서, 이전 time-step에 대한 모델의 예측값은 다음 time-stpe의 모델의 예측 값과 상관없음

- **Training**

- **Inference**

이러한 문제를 해결하기 위해 많은 연구자들이 Linear Attention과 같은 다양한 방법을 제안했지만, 대부분은Transformer만큼의 성능을 내지 못했습니다. 또한, Streaming LLM과 같은 방식으로 inference cost를 낮추기 위한 연구들도 다양하게 존재하지만, 근본적인 해결이 되지는 않았죠.

### 대항마: **Sequential** Models

연구자들은 다시 Recurrent model들을 살펴보기 시작합니다. Transformer가 Recurrent 모델의 대안으로 등장한 만큼, 둘은 상반된 장점과 단점을 가집니다.

Recurrent model들은 모두 알다시피 학습 속도가 매우 느리고, 한정된 공간에 정보를 저장하다보니 해당 지식을 유지하는데 문제가 있습니다:

- 하나하나 보기보다는 한정된 메모리에 시퀀스 정보를 잘 모아놓는 방식. 이전 t-1에 대한 메모리가 t의 입력으로 필요함

- **Training**

- **Inference**

즉, Recurrent 모델이 transformer의 대항마로써 인정받기 위해서는 다음의 두 가지 문제를 해결해야 합니다.

1. **‘어떻게 한정된 공간 안에 정보를 잘 집어넣어 성능을 transformer만큼 유지할 것인가’ **

1. **‘\*\***어떻게 학습 속도를 빠르게 만들 것인가’\*\*

그리고 이 두 가지를 해결할 수 있는 실마리가 바로 다음과 같습니다:

1. 한정된 공간 내 지식 압축→ Structured SSM

1. 훈련 속도 → Parallel Scan

그렇다면 Structured SSM이 무엇인지 알아보기 위해 SSM이 무엇인지부터 개념을 잡아봅시다

# **State Space Model (SSM)**

## Overview

{% include figure.liquid loading="eager" path="assets/img/posts/2025-02-04-ssm-hippo-lssl-s4-mamba-mamba2/image_000.png" class="img-fluid rounded z-depth-1" %}

`State Space Model(SSM)`은 본래 제어 이론에서 유래한 모델로, 시스템의 상태(state)와 출력을 수학적으로 정의한 것입니다.

해당 모델은 **연속적인 시간 흐름**에 따라 시스템의 상태를 모델링합니다. 즉, **(1) 시간에 따라 결정되는 함수**와 **(2) 0번째 시점부터 t-1번째까지의 입력**이 주어질 때, t번째의 출력을 예측하기 위한 시스템이라고 보시면 됩니다.

이 모델은 입력 데이터(_x_)를 받아 상태(_h_)를 계산한 후 이를 출력(_y_)으로 변환하는 위의 두 가지 주요 방정식으로 정의됩니다.

이때 **A**와 **B**는 연속적 시스템을 표현하는 중요한 매트릭스들로, **시간에 따른 시스템의 상태 변화**를 기술합니다.

- **A**: 상태 변화를 결정하는 매트릭스. 이전 상태 *Xt*−1에 곱해져서 시스템의 상태가 어떻게 변하는지 정의합니다.

- **B**: 입력을 상태로 변환하는 매트릭스. 입력 *Ut*를 받아 상태에 반영하는 역할을 합니다.

{% include figure.liquid loading="eager" path="assets/img/posts/2025-02-04-ssm-hippo-lssl-s4-mamba-mamba2/image_001.png" class="img-fluid rounded z-depth-1" %}

입력 u(t)와 출력 y(t) 사이를 이어주는 **_latent space의 feature x(t)_** (hidden vector)를 구하자!

즉, SSM은 **시스템의 입력을 고차원의 잠재 공간(latent space)으로 변환하여 처리**하는 방식으로 동작합니다.

## Details

즉, 우리가 구하고자 하는 것은 **_latent space의 feature x(t)_** (hidden vector)인 state. state는 다음과 같이 정의된다:

- **state**

SSM의 가장 큰 특징은 RNN과 CNN의 장점을 결합함으로써 기존 recurrent model들의 단점을 극복하고 있다는 것인데요,

**SSM은 크게 3가지 Representation으로 표현될 수 있습니다:**

{% include figure.liquid loading="eager" path="assets/img/posts/2025-02-04-ssm-hippo-lssl-s4-mamba-mamba2/image_002.png" class="img-fluid rounded z-depth-1" %}

### 1. **Continuous Representation**

가장 먼저 SSM은 `연속 표현(continuous Representation)`을 처리할 수 있으며, 이를 통해 시퀀스 데이터의 연속성을 자연스럽게 모델링할 수 있습니다.

{% include figure.liquid loading="eager" path="assets/img/posts/2025-02-04-ssm-hippo-lssl-s4-mamba-mamba2/image_003.png" class="img-fluid rounded z-depth-1" %}

LTI(linear and time-invariant) 시스템에서는 시스템의 현재 상태를 기술하는 방정식인 **상태 방정식(State equation) **을 1차 선형미분방정식으로 표현 가능합니다.

{% include figure.liquid loading="eager" path="assets/img/posts/2025-02-04-ssm-hippo-lssl-s4-mamba-mamba2/image_004.png" class="img-fluid rounded z-depth-1" %}

{% include figure.liquid loading="eager" path="assets/img/posts/2025-02-04-ssm-hippo-lssl-s4-mamba-mamba2/image_005.png" class="img-fluid rounded z-depth-1" %}

비슷한 방식으로 출력값을 표현할 수도 있습니다:

{% include figure.liquid loading="eager" path="assets/img/posts/2025-02-04-ssm-hippo-lssl-s4-mamba-mamba2/image_006.png" class="img-fluid rounded z-depth-1" %}

따라서, LTI system을 standard state space form으로 표현하는 모델은 다음과 같습니다:

{% include figure.liquid loading="eager" path="assets/img/posts/2025-02-04-ssm-hippo-lssl-s4-mamba-mamba2/image_007.png" class="img-fluid rounded z-depth-1" %}

여기서 각 행렬들의 역할은 다음과 같습니다:

- A: 기존 메모리 변환 → 메모리 업데이트

- B: 입력 변환 → 메모리 업데이트

- C: 기존 지식+새로운 입력을 이용해 업데이트한 새로운 메모리를 이용해 출력값 만드는 변환

이렇게 하면, A,B,C,D를 통해서, 앞서 이야기한 u(t)→y(t)를 이어주는 continuous한 flow h(t) (혹은x(t))를 모델링할 수 있습니다.

{% include figure.liquid loading="eager" path="assets/img/posts/2025-02-04-ssm-hippo-lssl-s4-mamba-mamba2/image_008.png" class="img-fluid rounded z-depth-1" %}

하지만, 여기서 반환되는 y는 연속된 시계열 표현(continuous-time representation)입니다. 이를 이산적인 단위를 가지는 시퀀스에서 사용하기 위해서는 discretization 작업을 수행해야 합니다.

### 2. **Recurrent Representation**

{% include figure.liquid loading="eager" path="assets/img/posts/2025-02-04-ssm-hippo-lssl-s4-mamba-mamba2/image_009.png" class="img-fluid rounded z-depth-1" %}

State equation은 continuous flow를 모델링하는 과정. 즉, SSM을 텍스트 차원에서 활용하기 위해서는, **연속 시스템에서 이산 시스템으로의 변환**이 필요합니다.

{% include figure.liquid loading="eager" path="assets/img/posts/2025-02-04-ssm-hippo-lssl-s4-mamba-mamba2/image_010.png" class="img-fluid rounded z-depth-1" %}

이산화를 하는데는 여러가지 방법이 있지만, 가장 간단한 방식으로는 다음과 같이, 각 시점에서 상태 공간의 변화를 나타내는 SSM 방식으로 치환할 수 있습니다:

- _h_(_t_)=**A̅**⋅*h*(*t*−1)+**B̅**⋅*x*(_t_)

- _y_(_t_)=*C*⋅*h*(_t_)

확인할 수 있듯, Recurrent Representation은 상태 공간 모델에서 순차적으로 상태 _h_(_t_) 를 업데이트하는 구조입니다.

즉, t번째 시간 단계에서의 상태 _h_(_t_)는 이전 상태 _h_(*t*−1)에 의존합니다.

{% include figure.liquid loading="eager" path="assets/img/posts/2025-02-04-ssm-hippo-lssl-s4-mamba-mamba2/image_011.png" class="img-fluid rounded z-depth-1" %}

이제 이산화한 결과를 살펴보면 다음과 같이 각각의 T=0, T=1, T=2에 대해서 이전 time t-1의 *h(t-1)*의 input과 현시점 *x(t)*의 input을 받아서 *h(t)*를 도출하고 이를 통해 *y(t)*를 재귀적으로 호출하는 것을 볼 수 있습니다.
