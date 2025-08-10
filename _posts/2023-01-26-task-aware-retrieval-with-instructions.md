---
categories:
- paper-reviews
date: '2023-01-26 00:00:00'
description: 논문 리뷰 - Retrieval, Instruction Tuning 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- bert
- instruction tuning
- llm
- nlp
- paper-review
- retrieval
thumbnail: assets/img/posts/2023-01-26-task-aware-retrieval-with-instructions/thumbnail.jpg
title: Task-aware Retrieval with Instructions
---

**논문 정보**
- **Date**: 2023-01-26
- **Reviewer**: 건우 김
- **Property**: Retrieval, Instruction Tuning

# 1. Introduction

**Information Retrieval: **the task of finding ***relevant ***documents from a large colection of texts

- **Relevance**

- ***Retrieval with instructions***: explicitly하게 User의 의도를 자연어로 구성된 description을 통해 모델링하는 task → 이 task의 목표는 query와 relevant하면서 instruction에 잘 반영된 document를 찾는 것이다.

# 2. Background and Related Work

### Zero-shot training of retrievers

### Instruction tuning

- 대부분의 Instruction을 따른 LLMs들은 generation이 목적인 architecture를 주로 갖고 있는데 (encoder-decoder, decoder-only), 수 백만 건의 documents를 encoding을 해야하는 retrieval task에는 부적절함

### Retrieval with descriptions

- 이전에 retrieval module에 description을 활용한 연구는 title을 활용한 baseline에 비해 살짝 좋은 성능을 보임

- 최근에 와서 BERT 기반 LMs들이 등장하면서 더 풍부한 linguistic context를 잡아낼 수 있음

# 3. Task Formulation

- ***Retrieval with instructions (New Task)***

- Given, 

# 4. BERRI: Collections of Instruction-annotated    Retrieval Tasks

- BERRI (Bank of Explicit RetRieval Instructions): retrieval dataset + other NLP datasets

- BERRI에서 각 task는 하나의 corpus와, k개의 query 그리고 하나의 instruction으로 이루어진다. 각 task의 하나의 instance는 query (q), gold documents (d^+), negative documents (d^-)과 하나의 explicit한 intent t가 있다.

- Instruction Tuning에서 informative + diverse한 instructions들이 주된 성공 요인으로 꼽히는데, retrieval task에서 다음을 만족하는 instruction을 설계하기 위해 다음과 같은 scheme을 만듬.

- **Dataset Collection**

# 5. TART: Multi-task Instructed Retriever

- TART (TAsk-aware ReTriever): BERRI dataset을 기반으로 multi-task instruction tuning을 통해 학습한 single unified retriever

- **TART-dual**: DPR과 동일한 구조를 갖고 있어 DPR이 갖는 장/단점 동일

- **TART-full**: 다들 아시다시피 dual-encoder는 query와 document가 독립적으로 처리되기 때문에, limited interactions이 있음. 다른 cross-encdoer 구조의 retriever와 마찬가지로 query와 document를 함께 입력하여 relevance 계산. 그런데 수 백만 건의 document에 대해 학습하기에 매우 cost가 비싸기 때문에, 

- **Knowledge distillation from TART-full to TART-dual**

# 6. Experiments

- **Zero-shot retrieval**

- **X^2 ****-Retrieval (Cross-task Cross-domain Retrieval)**

- **Baselines**

- **Experimental Settings**

# 7. Results

- **Zero-shot Evaluation Results**

- **X^2****-Retreival Evaluation Results**

# 8. Analysis

- **Effects of Instruction at training and inference**

- **Effects of dataset scale + Effects of model scale **

     → 모델 크기 크면 좋고 + 데이터셋 number/domain/task 많으면 좋다

- **Effects of carefully-designed negative samples**

# 9. Dicussion and Conclusion

- **실제 동일 query에 있어 instruction을 다르게 주면 retrieve되는 text는 다름**

- **정성 평가 예시 (물론 체리피킹)**

- **NLP에서 최초로 Instruction Tuning을 retrieval task에 접목 시킨 paper**

- **dramatic한 performance gain이 있지는 않았지만, 방향을 제시한 것에 있어서 의의가 있음**
