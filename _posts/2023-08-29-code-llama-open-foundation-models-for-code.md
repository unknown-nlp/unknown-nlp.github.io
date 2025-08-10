---
categories:
  - paper-reviews
date: "2023-08-29 00:00:00"
description: 논문 리뷰 - LLM 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
  - fine-tuning
  - llm
  - paper-review
  - pre-training
thumbnail: assets/img/posts/2023-08-29-code-llama-open-foundation-models-for-code/thumbnail.jpg
title: "Code Llama: Open Foundation Models for Code"
---

**논문 정보**

- **Date**: 2023-08-29
- **Reviewer**: hyowon Cho
- **Property**: LLM

# Introduction

domain-specific dataset을 이용해서 application에 특화된 모델을 만드는 것은 보편적인 방법이다. 이러한 추세는 언어모델을 이용하여 코드를 작성하는데까지도 이어졌다. 예를 들어, code completion, debugging, generating documentation과 같은 작업을 수행할 수 있다.

이번 발표에서는 Meta AI에서 공개한 Code Llama에 대한 리뷰를 진행한다. 해당 모델의 의의는 크게 두 가지, 제일 성능이 좋다는 것과 repository-level의 긴 context를 받아서 처리할 수 있다는 것이다.

실제 예시를 살펴보면 꽤나 좋은 성능을 내고 있다는 것을 확인할 수 있다.

요약된 특징은 다음과 같다:

1. Code-training from foundation models

1. Infilling

1. Long input contexts.

1. Instruction fine-tuning.

이 외에도 해당 paper에서는 다른 code-based LLM들과의 비교를 진행하고, 우리가 궁금할법한 다양한 ablation study를 진행한다.

# Technical Details

### The Code Llama models family

- Code Llama

- Code Llama - Python:

- Code Llama - Instruct:

### Dataset

- Natural Language Related to Code

- Natural Language

### Infilling

Infilling을 위한 데이터들은 다음과 같이 구성된다.

먼저 모든 데이터들은 prefix-middle-suffix로 나눠진다. (splitting locations are sampled independently from a uniform distribution over the document length.)

이후, 전체 데이터의 절반은 prefix-suffix-middle (PSM) format, 나머지 절반은 suffix-prefix-middle (SPM) format으로 구성한다.

suffix, prefix, middle의 시작과 infilling span의 끝을 표기하기 위한 토큰이 추가된다.

이렇게 재배열된 데이터에 대한 auto-regressive training을 수행한다.

전체 데이터의 90퍼센트는 Infilling, 나머지는 일반 auto-regressive수행한다.

### Long context fine-tuning

Code Llama에서는 최대 16,384 tokens을 다루기 위한 long context fine-tuning (LCFT) stage를 제안한다.

이들이 제안하는 방법은 다음과 같다:

- Problem

- Solution: Change base period

### Instruction fine-tuning

instruction fine-tuned models Code Llama - Instruct은 Code Llama에 다음의 데이터셋을 이용하여 finetuning한 모델이다.

1. Proprietary dataset

1. Self-instruct

1. Rehearsal.

### Training details

- batch size of 4M tokens

- Long context fine-tuning

# Results

### Code generation

- description-to-code generation benchmarks for Python:

**The value of model specialization.**

- Llama 2 vs Code Llama

- Code Llama vs Code Llama - Python

**Unnatural model.**

- unnatural instructions (Honovich et al. (2023))을 이용해 finetune

- indicative of the improvements that can be reached with a small set of high-quality coding data.

APPS benchmark는 위에서 소개된 벤치마크보다 더 어려운 태스크.

- Code Llama - Python models은 introductory and interview level 태스크에서 성능 저하를 보였다. 즉, 프롬프트 자체를 이해하는 것이 solution을 내는 것보다 어렵다는 것을 Imply.

- Code Llama - Python은 competition-level problems, solution 자체를 더 구하기 어려운 태스크, 에서 더 좋은 성능을 보였다.

**Scaling of specialized models.** specialized 모델들을 기준으로, 크기가 크면 언제나 성능이 더 좋았다.

### Multilingual evaluation

Python 이외에 Multilingual 성능 또한 평가한다.

- MultiPL-E (Cassano et al., 2022)

mono-lingual setting과 비슷한 결과를 확인할 수 있다.

- Code Llama models clearly outperform Llama 2 models of the same size on code generation in any language,

- Code Llama 7B outperforms Llama 2 70B.

- 다른 publicly available models과 비교해도 확실한 성능

- Code Llama -Python 30B는 Code Llama 30B보다 성능이 살짝 좋지 않았으나, Code Llama - Python 7B and 13B는 더 나았음.

multilingual pre-training의 영향력을 확인하기 위해 언어별 correlations을 찍어본 결과이다.

- C++, C#, Java, PHP 사이 high correlation on model performance.

- Python, Bash 사이 high correlation on model performance.

- **Lastly, as expected the bigger and more expressive the models, the higher the correlation between the performance across all different languages.**

### Infilling evaluations

### Long context evaluations

perplexity, synthetic retrieval task, code completion with long source code files

- Perplexity during extrapolation.

- Key retrieval.

- Single line completion.

- Performance impact on short contexts.

# Ablation Studies

### Fine tuning Llama 2 vs. training from scratch on code

(4b)를 보면, 거의 절반 차이를 보이는 것을 확인할 수 있다. 즉, fineuning이 훨씬 낫다는 것 강조!
