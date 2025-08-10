---
categories:
- paper-reviews
date: '2024-08-13 00:00:00'
description: 논문 리뷰 - Reasoning, Explainability 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- explainability
- gpt
- language-model
- llm
- paper-review
- pre-training
- reasoning
thumbnail: assets/img/posts/2024-08-13-physics-of-language-models-part-21-grade-school/thumbnail.jpg
title: 'Physics of Language Models: Part 2.1, Grade-School Math and the Hidden Reasoning
  Process'
---

**논문 정보**
- **Date**: 2024-08-13
- **Reviewer**: 준원 장
- **Property**: Reasoning, Explainability

## 1. Introduction

### Motivation

- small language models (GPT2 in this paper)의 GSM8K, its augmentation의 성능을 향상시키는 기존의 연구는 많았음.

- 논문에서는 단순한 성능 향상이 아닌 보다 근본적인 질문을 해결하고자 함. 

- 이를 위해 6개의 RQ를 수립하고, 이를 검증하기 위한 굉장히 통제적인 실험을 진행함

### Research Question

1. LM은 진정으로 추론 능력을 개발할 수 있을까?, 아니면 단순히 템플릿을 기억하는 것일까?

1. LM의 hidden (mental) reasoning process는 무엇일까? (hidden state에서는 어떤 semantic이 형성되었는가? ⇒ Explainability를 위한 질문)

1. LM은 모델은 인간과 유사 혹은 다른 방식으로 수학 문제를 해결할까?

1.  GSM8K와 같은 데이터셋에 훈련된 LM은 GSM8K 문제를 해결하는 데 필요한 것을 넘어서는 추론 능력을 학습할 수 있을까? (⇒ Generalization에 대한 질문)

1. 어떤  hidden (mental) reasoning process이 추론 오류를 범하게 만들까?

1. GSM8K 수준의 수학 문제를 효과적으로 해결할 수 있는 LM은 얼마나 크거나 깊어야 할까?

⇒ 각 RQ에 1:1로 대응되는 해답을 내놓지는 않지만, 논문 전반에 걸쳐 위에 대한 대답을 하고 있음

### Pre-Training From the Scratch

- 논문에서는 통제적인 실험을 위해 아래를 근거 삼아 from the scratch LM을 실험에 활용함

## 2. Result 1: Data Generation

> Betty is saving money for a new wallet which costs 100. Betty has only half of the money she needs. Her parents decided to give her 15 for that purpose, and her grandparents twice as much as her parents. How much more money does Betty need to buy the wallet?

- “Betty’s current money = 0.5 × cost of the wallet” , “money given by grandparents = 2 × money given by parents.”처럼 GSM8K가 다변수로 엮여있는 방정식을 설계하는게 Data Generation의 목표

- GSM8K를 흉내내는 데이터셋이기에, LM이 학습되면서 (저자들이 정의한) 아래의 dependency를 학습하도록 dataset generation framework를 설계하였음

- Data Generation은 parameter(미지수)간의 hierarchy를 기준으로 그래프 설립 → 문제 생성의 순을 따름

## 3. Result 2-3: Summarize Model’s Behavior Process

- LM 학습은 GPT2 small을 일정 training step을 만족시킬만큼 데이터셋을 합성해 진행

{% include figure.liquid loading="eager" path="assets/img/posts/2024-08-13-physics-of-language-models-part-21-grade-school/image_000.png" class="img-fluid rounded z-depth-1" %}

> **Result 2**

- 논문에서는 2가지 Reasoning Skill을 정의

{% include figure.liquid loading="eager" path="assets/img/posts/2024-08-13-physics-of-language-models-part-21-grade-school/image_001.png" class="img-fluid rounded z-depth-1" %}

[correct solution마다 생성된 unnecessary params / operations의 수]

> **Result 3**

## 4. Result 4-5: Discover Model’s Mental Process

- LM이 hidden state에서 인간처럼 인지적인 논리작용이 이루어지는지를 확인하기 위해 Probing Setup을 설계해서 실험

- 인간의 인지작용해서 자연스럽게 계산될 다음의 함수를 사전 지정

- Probing Process & Example

- pretrained weights에서 성능이 기인했음을 보기 위해 random initialized model에도 linear classifier학습을 진행

{% include figure.liquid loading="eager" path="assets/img/posts/2024-08-13-physics-of-language-models-part-21-grade-school/image_002.png" class="img-fluid rounded z-depth-1" %}

> **Result 4**

{% include figure.liquid loading="eager" path="assets/img/posts/2024-08-13-physics-of-language-models-part-21-grade-school/image_003.png" class="img-fluid rounded z-depth-1" %}

> **Result 5**

## 5. Result 6: Explain Model’s Mistakes

- Reasoning process의 mistake를 2가지 질문을 통해 해석하고자 함.

1. When does the model answer correctly but include unnecessary parameter?

1. What causes incorrect answers?

> **Result 6**

## 6. Result 7-8: Depth vs. Reasoning Length

- LM의 layer와 size(head hidden dim)을 늘려가면서 성능변화 추이를 확인

{% include figure.liquid loading="eager" path="assets/img/posts/2024-08-13-physics-of-language-models-part-21-grade-school/image_004.png" class="img-fluid rounded z-depth-1" %}

> **Result 7**

{% include figure.liquid loading="eager" path="assets/img/posts/2024-08-13-physics-of-language-models-part-21-grade-school/image_005.png" class="img-fluid rounded z-depth-1" %}

- x축: A가 문제로 부터 떨어진 거리, y축: Layer별로 necc()결과

> **Result 8**

## 7. Conclusion

- 통제된 실험을 통해 LM이 reasoning process를 진정으로 학습할 수 있는지 (generalization), hidden reasoning processes probing을 통해 인간과 얼마나 유사한 인지작용을 하는지 검증

- 다소 pattern따기 쉬운 데이터셋임으로, 엄청나게 학습을 시키면 probing성능을 사실상 어느정도 높게 나오는게 당연하다고 보임.

- 그럼에도, LM의 generalization (OOD performance)의 실험적 증명 + LM이 token에서 어떤 정보를 학습할 수 있는지를 보여 solution을 생성한건 굉장히 고무적

- 오히려 (LLM시대에 들어오면서 더 어쩔 수 없는 Data Contamination을 인정하고) reasoning task에 한정된 LM이 아닌 General LLM에서 이 논문에서 밝힌 경향을 동일하게 보이는지도 궁금함.
