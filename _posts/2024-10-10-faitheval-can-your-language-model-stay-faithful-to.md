---
categories:
- paper-reviews
date: '2024-10-10 00:00:00'
description: 논문 리뷰 - Safety 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- language-model
- llm
- paper-review
- safety
thumbnail: assets/img/posts/2024-10-10-faitheval-can-your-language-model-stay-faithful-to/thumbnail.jpg
title: 'FAITHEVAL: CAN YOUR LANGUAGE MODEL STAY FAITHFUL TO CONTEXT, EVEN IF “THE
  MOON IS MADE OF MARSHMALLOWS”'
---

**논문 정보**
- **Date**: 2024-10-10
- **Reviewer**: 건우 김
- **Property**: Safety

**Faithfulness in LLM: **주어진 맥락에 대해 생성된 답변의 사실적 일관성

# Introduction

- RAG로 additional knowledge를 LLM에 integrate를 해도 hallucination은 아직도 critical challenge

- **Hallucination in LLM**

- RAG에서 Faithfulness hallucination를 다루기에는 retrieval process에서 문제가 있음 

- Existing hallucination benchmarks는 아래 문제들이 있음

- **FaithEval**: 아래 세가지 task로 LLM의 contextual faithfulness를 평가하기 위해 최초로 제안된 fine-grained and comprehensive benchmark (4.9k size)

{% include figure.liquid loading="eager" path="assets/img/posts/2024-10-10-faitheval-can-your-language-model-stay-faithful-to/image_000.png" class="img-fluid rounded z-depth-1" %}

# FaithEval Benchmark

### Task Overview

- 각 sample은 다음과 같은 구조를 갖음

{% include figure.liquid loading="eager" path="assets/img/posts/2024-10-10-faitheval-can-your-language-model-stay-faithful-to/image_001.png" class="img-fluid rounded z-depth-1" %}

1. **Unanswerable Context**: question에 대해 context가 relevant details은 갖고 있지만 answer를 도출하기 위한 정보가 없는 경우

1. **Inconsistent Context**: 동일한 question에 대해 paragraph(=doc)마다 서로 다른 answer가 있는 경우 (1.5k QA pairs)

1. **Counterfactual Context**: common sense와 상반되는 개념이 담긴 context가 있는 경우 

### Task Construction and Validation Framework

{% include figure.liquid loading="eager" path="assets/img/posts/2024-10-10-faitheval-can-your-language-model-stay-faithful-to/image_002.png" class="img-fluid rounded z-depth-1" %}

**Task Construction**

**Auto validation and human annotation**

- new context의 quality를 평가하기 위해 별도의  LLM을 사용하여 평가함

- Human annotation에 대해서도 평가를 하는데, task의 validation 난이도에 따라 다르게 평가함

### Evaluation

**Models **24.09.10까지 release된 최신 LLM들 사용 

- Open source

- Proprietary models

**Default Evaluation Scheme**

**Prompt for all tasks**: *You are an expert in retrieval-based question answering. Please respond with the exact answer, using only the information provided in the context*

- additional instruction for **Unanswerable Context task**: *If there is no information available from the context, the answer should be “unknown”*

- additional instruction for **Inconsistent Context task**: *If there is conflicting information or multiple answers in the context, the answer should be “conflict”*

**Evaluation metric: **Accuracy

# Main Results

### Unanswerable Context

→ no evidence supports the answer

- **Abstaining is challenging, even when explicitly instructed.**

### Inconsistent Context

- **Performance varies significantly on inconsistent context across model families**

### Counterfactual Context

→ evidence supports a counterfactual answer

- **Faithfulness remains a limitation for contextual LLMs**

# Discussion and Further Analysis

- **Performance breakdown for individual datasets**

- **A closer look at Inconsistent Context**

- **Sycophancy(=아첨) with task-specific instructions**

- **Does chain-of-thought prompting improve faithfulness?**

- **Strict vs. non-strict matching**

- **Impact of decoding strategies**

# Conclusion

- FaithEval이라는 contextual LLMs의 faithfulness를 평가하는 benchmark 소개함

- open-source 및 proprietary models에 대해서 깊은 분석을 진행하고, competitive LLMs도 context에 대해 faithful을 유지하는 능력이 부족한 것을 실험적으로 보여줌

- 의문 point: 실제 retrieval이 추출하는 text의 noise가 그 정도로 있는지.? credibility가 정말 낮은지?
