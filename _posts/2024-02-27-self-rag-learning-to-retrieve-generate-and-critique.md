---
categories:
  - paper-reviews
date: "2024-02-27 00:00:00"
description: 논문 리뷰 - Retrieval, Natural Language Generation 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
  - gpt
  - language-model
  - llm
  - natural language generation
  - paper-review
  - reasoning
  - retrieval
  - rlhf
thumbnail: assets/img/posts/2024-02-27-self-rag-learning-to-retrieve-generate-and-critique/thumbnail.jpg
title: "SELF-RAG: LEARNING TO RETRIEVE, GENERATE, AND CRITIQUE THROUGH SELF-REFLECTION"
---

**논문 정보**

- **Date**: 2024-02-27
- **Reviewer**: 상엽
- **Property**: Retrieval, Natural Language Generation

# Introduction

- LLM의 발전에도 불구하고 Factual error는 발생

{% include figure.liquid loading="eager" path="assets/img/posts/2024-02-27-self-rag-learning-to-retrieve-generate-and-critique/image_000.png" class="img-fluid rounded z-depth-1" %}

- RAG : 관련 문서 retrieval → Knowledge-intensive task에서 factual error 감소 확인

하지만 여전히 몇 가지 문제점이 있음.

- RAG 기술은 LLM의 성능에 악영향을 미칠 가능성이 있음.

→ Self-Reflective Retrieval-augmented Generation (SELF-RAG)

- via on-demand retrieval and self-reflection.

**How?**

- generation process에서 task output generation과 retrieval 여부와 결과를 평가하는 reflection token 생성을 동시에 하겠다.

- **Reflection tokens**

절차

1. input이 주어지면 생성 시작

1. 생성 과정 중 Retrieval을 하는 것이 도움이 될지 안될지 판단, 만약 retrieval이 필요하다고 판단된다면 retrieval token을 생성 (on demand)

1. 동시에 multiple retrieved passages를 평가 (relevance, support)

1. factuality and overall quality 관점에서 최선의 passage 선정.

차이점

- 항상 고정된 개수의 document를 추출하는 RAG와는 달리 **retrieval을 조절할 수 있음**.

- SELF-RAG는 support에 대한 **self assesment를 진행**하기 때문에 citation을 제공할 수 있음. → fact verification을 쉽게 함.

# Related work

**RAG (Retrieval Augmented Generation)**의 첫 등장 이후 많은 variation들이 생기고 있음.

- inference 시 retrieval 후 결과값 생성

- training 시 retrieval 결과 포함하여 학습

- adaptively retrieve passages for generation on top of a proprietary LLM

**Training and generating with critics**

- RLHF (reward 모델과 비교하는 내용을 계속 작성하더라…)

- LLM의 결과를 평가해 수정 및 생성하는 이전 논문들

# SELF-RAG: LEARNING TO RETRIEVE, GENERATE AND CRITIQUE

**Reflection tokens**

{% include figure.liquid loading="eager" path="assets/img/posts/2024-02-27-self-rag-learning-to-retrieve-generate-and-critique/image_001.png" class="img-fluid rounded z-depth-1" %}

output’s relevance, support, or completeness를 평가

### PROBLEM FORMALIZATION AND OVERVIEW

x : given input

\mathcal{M} : language model

y : textual outputs consisting of multiple segments [y_1, ..., y_T] (original token + reflection token)

**Inference overview**

{% include figure.liquid loading="eager" path="assets/img/posts/2024-02-27-self-rag-learning-to-retrieve-generate-and-critique/image_002.png" class="img-fluid rounded z-depth-1" %}

x가 주어졌을 때 모든 generation 과정 y\_{<t}에 대해서 모델은 retrieval 여부를 판단

- retrieval이 필요없을 경우 : standard LM과 똑같이 next output segment prediction 진행

- retrieval이 필요할 경우

**Training overview**

{% include figure.liquid loading="eager" path="assets/img/posts/2024-02-27-self-rag-learning-to-retrieve-generate-and-critique/image_003.png" class="img-fluid rounded z-depth-1" %}

- Data collections (\mathcal{D\_{critic}}) : GPT-4를 이용해 reflection token을 포함한 데이터 수집

- Learning critic model \mathcal{C} : \mathcal{D\_{critic}} 데이터를 이용해 reflection token 생성 학습 (일종의 reward 모델)

- Training generator \mathcal{M} : critic model을 이용해 input에 reflection token 생성 (offline으로 사전에 진행)한 데이터를 이용해 일반적인 generation task 학습

### SELF-RAG TRAINING

**TRAINING THE CRITIC MODEL**

- Data collection for critic model : \mathcal{D\_{critic}}

- Critic learning

**TRAINING THE GENERATOR MODEL**

- **Data collection for generator : \*\***\mathcal{D\_{gen}}\*\*

- **Generator learning**

### SELF-RAG INFERENCE

- reflection token을 이용한 SELF-RAG는 controllable함.

- task의 특징에 맞춰 retireval의 빈도를 조절할 수 있음.

**Adaptive retrieval with threshold**

- retrieval 여부에 대한 threshold를 설정

**Tree-decoding with critique tokens**

- 매 Segment에 대해 Retrieval 결정 → K개의 passage retrieval 진행 → \mathcal{M}을 K개 passage에 병렬적으로 적용.

- segment-level beam search 진행

- 각 segment의 score는 다음과 같이 계산

# Experiments

### Task and Datasets

다양한 모델과 downstream task 비교 overall correctness, factuality, and fluency.

zero-shot evaluations 진행

**Closed-set tasks**

- **fact verification dataset **about public health (**PubHealth**; Zhang et al. 2023)

- **multiple-choice reasoning dataset **created from scientific exams (**ARC-Challenge**; Clark et al. 2018).

→ test set 정확도로 평가

**Short-form generations tasks**

two open-domain question answering (QA) datasets (factual knowledge에 대한 질문에 답변)

- PopQA (Mallen et al., 2023)

- TriviaQA-unfiltered (Joshi et al., 2017)

→ gold answer가 생성한 정답에 포함되어 있는지 여부로 평가 (following Mallen et al. (2023); Schick et al. (2023).)

**Long-form generation tasks**

biography generation task

- FactScore (Min et al., 2023)로 평가

long-form QA task

- ALCE-ASQA dataset

- correctness (str-em), fluency based on MAUVE, citation precision and recall

### BASELINES

**Baselines without retrievals. **
