---
categories:
  - paper-reviews
date: "2025-08-05 00:00:00"
description: 논문 리뷰
giscus_comments: true
layout: post
related_posts: false
tags:
  - attention
  - embedding
  - fine-tuning
  - gpt
  - language-model
  - llm
  - paper-review
thumbnail: assets/img/posts/2025-08-05-impact-of-fine-tuning-methods-on-memorization-in/thumbnail.jpg
title: Impact of Fine-Tuning Methods on Memorization in Large Language Models
---

**논문 정보**

- **Date**: 2025-08-05
- **Reviewer**: hyowon Cho

많은 연구들이 LLM이 사전학습 단계에서 학습 데이터를 외우는 이슈에 대해서 보고하고 있는 한편, finetuning에 대해서 비슷한 연구는 놀라울 정도로 적다.

하지만, finetuning도 당연히 모델 대부의 업데이트와 때때로는 구조적인 변화까지도 이루어지기 때문에, finetuning의 memorization level에 대한 연구도 필요하다.

그렇다면, 존재하는 다양한 finetuning 방법에 따른 memorization of fineuning data의 영향력은 어떻게 되는가?

해당 연구는 이를 시험하기 위해 우선 finetuning 방법을 크게 두 가지로 구분한다:

1. Parameter-based finetuning: 모델 파라 바꿈

1. Prompt-based fine-tuning: 모델 파라 고정, soft token/prefix embedding…

결과적으로 두 카테고리를 고루 포함한 5가지 방법을 시험했고,

평가는 다양한 MIAs(membership inference attacks )로 했고,

데이터는 Wikitext, WebNLG, Xsum 세 가지로 했다 (좀 적긴하네요)

간단하고 빠르게 다음으로 넘어갑시다

# Fine-Tuning Methods

- Parameter-based fine-tuning

- Prompt-based fine-tuning: task-specific prompts only

# Memorization and MIAs

- 사용된 MIA 기법과 점수 계산 방식:

# Experimental Setup

- 데이터

- 평가

- 모델

- Evaluation Metrics

- Implementation Details

# Results and Observations

## Memorization across Tuning Methods

> Does the choice of finetuning strategy affect how much a model memorizes its training data for fine tuning?

> Observation ♯1: (당연)

{% include figure.liquid loading="eager" path="assets/img/posts/2025-08-05-impact-of-fine-tuning-methods-on-memorization-in/image_000.png" class="img-fluid rounded z-depth-1" %}

모든 방법론은 validation PPL기준으로 성능 좋았음.

하지만, prompt-based methods 는 parameter-based 보다 외우는 성능 떨어짐 (당연)

> Observation ♯2:

{% include figure.liquid loading="eager" path="assets/img/posts/2025-08-05-impact-of-fine-tuning-methods-on-memorization-in/image_001.png" class="img-fluid rounded z-depth-1" %}

## Why Prompt-Based Fine-Tuning Exhibits Low Memorization

prompt-based fine-tuning introduces a bias into the model’s attention mechanism indirectly via
the soft prompt or prefix, rather than altering the attention mechanism itself.

- **Prefix Tuning 수식 (Petrov et al., 2024)**

- 결과적으로 **표현 공간의 이동(shift) < 적음** → 학습, 비학습 샘플 분포 차이가 작아 MIA가 어렵다.

이 가설을 확인하기 위해:

distributions of non-membership and membership examples on the LLaMA2-7B를 세 세팅에서 비교함:

1. pre-trained model,

1. fine-tuned with LoRA

1. fine-tuned with prefix tuning

{% include figure.liquid loading="eager" path="assets/img/posts/2025-08-05-impact-of-fine-tuning-methods-on-memorization-in/image_002.png" class="img-fluid rounded z-depth-1" %}

LoRA는 membership and non-membership samples 사이 분포 차이가 큰데, prefix tuning은 미미하다는 것을 알 수 있음

## Performance in Different Tuning Paradigms

{% include figure.liquid loading="eager" path="assets/img/posts/2025-08-05-impact-of-fine-tuning-methods-on-memorization-in/image_003.png" class="img-fluid rounded z-depth-1" %}

두 방법론이 최종적으로는 비슷한 PPL을 가졌음에도 불구하고, Learning trajactories는 꽤나 달랐음

parameterbased fine-tuning:

- decreases over the first few epochs

- later increases due to overfitting, before eventually converging

prompt-based fine-tuning:

- slightly decreasing validation PPL throughout training,

- converging without the overfitting-induced rise

이는 아까도 이야기 했듯이, 후자가 internal sample distribution of the model을 바꾸는 것이 아니라 단순히 다운스트림 태스크에 쪼끔 더 나은 bias를 추가하는 정도임을 다시한번 보인다

# Discussion

## Regarding Model Scale

모델 사이즈가 memorization에 중요한 영향력을 줄 것임.

→ To what extent does model size influence memorization under different fine-tuning strategies?

> Observation ♯3

four variants of the GPT-2 architecture:

- GPT-2 (124M),

- GPT-2 Medium (345M),

- GPT2 Large (762M),

- GPT-2 XL (1.5B).

LLaMA2-7B vs LLaMA3-1B

{% include figure.liquid loading="eager" path="assets/img/posts/2025-08-05-impact-of-fine-tuning-methods-on-memorization-in/image_004.png" class="img-fluid rounded z-depth-1" %}

요약: 파라미터 바꾸는 애들은 모델 크기 커질수록 더 잘 외웠는데 반대는 미미하더라 (low sensitivity of prompt tuning to model scale)

특히, gpt2의 경우나 1B 스케일에서 LoRA는 사실상 거의 못외움

## Impact of Downstream Tasks

> Observation ♯4
> Prompt-based tuning leads to stronger memorization in structured tasks than in other downstream tasks.

다운스트림 태스크의 종류에 따라서도 다를 수 있음. 이를 위 LLaMA2-7B를 다양한 방법을 통해 학습시키고 LOSS attack against에 대해서 각각을 평가해봄

{% include figure.liquid loading="eager" path="assets/img/posts/2025-08-05-impact-of-fine-tuning-methods-on-memorization-in/image_005.png" class="img-fluid rounded z-depth-1" %}

Prompt-based 만 봤을 때, WebNLG가 다른 것들에 비해서 성능이 높다

아마도 구조화된 pattern학습에는 유리한 것 같다
