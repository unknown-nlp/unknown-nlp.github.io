---
categories:
- paper-reviews
date: '2024-07-30 00:00:00'
description: 논문 리뷰 - Retrieval, ICL, In Context Learning 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- attention
- bert
- icl
- in context learning
- language-model
- llm
- paper-review
- retrieval
thumbnail: assets/img/posts/2024-07-30-in-context-retrieval-augmented-language-models/thumbnail.jpg
title: In-Context Retrieval-Augmented Language Models
---

**논문 정보**
- **Date**: 2024-07-30
- **Reviewer**: 김재희
- **Property**: Retrieval, ICL, In Context Learning

# 1. Intro

## 1-1. Contributions

2023년 01월에 발표된 논문이라는 점을 감안

- 전반적인 논문의 서술은 최근 활발히 사용되는 RAG 프레임워크에서 크게 다르지 않음

## 1-2. TL;DR

1. Off-the-shelf Retriever 역시 Reader 성능 향상에 도움을 준다. 

1. Retriever의 종류(sparse, dense)와 관계없이 성능 향상에 도움을 준다. 

1. stride는 적절히 짧게, retrieved passage의 수는 많을수록 성능 향상에 도움이 된다. 

1. Reranker는 당연하게도 도움이 된다. 

> RALM의 Design Choice는 초록색 글씨로 표시하였습니다. 

# 2. Related Works

## 2-1. Retriever-Augmented Generation(RAG)

{% include figure.liquid loading="eager" path="assets/img/posts/2024-07-30-in-context-retrieval-augmented-language-models/image_000.png" class="img-fluid rounded z-depth-1" %}

- Knowledge Intensive Task 시 외부 Document를 적절히 이용하도록 Retriever를 이용하는 방법론 제안

- Retriever(query encoder)와 Generator(T5)를 동시에 훈련하는 학습 방법론 제안

### 2-1-1. 학습 방법

1. Retriever 훈련: Knowledge Intensive Dataset(NQ, TriviaQA)으로 훈련된 DPR 모델 이용

1. End-to-End 훈련: (Retrieve된 document k개, relevance score k개, Generation Prob)을 이용하여 Generator와 Retriever 훈련

### 2-1-2. 성능

- 다양한 Knowledge Intensive Task에서 기존 방법론 대비 높은 성능 달성

## 2-2. **Improving language models by retrieving from trillions of tokens(RETRO)**

{% include figure.liquid loading="eager" path="assets/img/posts/2024-07-30-in-context-retrieval-augmented-language-models/image_001.png" class="img-fluid rounded z-depth-1" %}

- RAG를 확장하여 다양한 일반 태스크에 적용할 수 있는 프레임워크 제안

- Retriever(BERT)를 Freeze하고 query와 가장 가까운 문서의 representation에 대한 attention(Chunked Cross-Attention)구조 제안

### 2-2-1. 성능

{% include figure.liquid loading="eager" path="assets/img/posts/2024-07-30-in-context-retrieval-augmented-language-models/image_002.png" class="img-fluid rounded z-depth-1" %}

- 모델 크기(million to billion)에 관계없이 일관된 성능 개선 관찰

- Retriever 사용 여부(on/off)가 성능 개선에 큰 영향을 미치는 것 확인

## 2-3. 요약

**2023년의 상황**

- LLaMA의 등장 이후 Open Source LLM에 대한 연구 진행

- Million Scale의 RAG 프레임워크 연구들이 끝물을 향해 가고 있음

- LLM에 RAG 프레임워크 적용이 활발히 시작되던 시기

# 3. Methods

## 3-1. In-Context RALM(Retriever-Augmented Language Modeling)

### 3-1-1. Language Modeling

- Prefix(x_{<i})를 바탕으로 현재 시점(i)의 토큰 분포를 생성하는 작업

### 3-1-2. Naive In-Context RALM

- 기존 LM에 Retriever 추가

- \mathcal{R}_{\mathcal{C}}(x_{<i}): Prefix를 query로 Retriever 수행한 Top-k document

- 매 시점마다 다음 과정 수행

## 3-2. RALM Design Choices

### 3-2-1. Retrieval Stride(s)

- Naive RALM: 매 토큰마다 Retrieval 진행

- Retrieval Stride(s): retrieval을 수행할 간격

- n_s(=n/s): 전체 text length가 n일 때, retrieval 횟수

- s의 크기는 속도(연산량)과 성능 간 trade-off 관계

### 3-2-2. Retrieval Query Length(\ell)

- Naive RALM: 현재까지 생성된 모든 text를 query로 사용

- q_j^{s, \ell}:=x_{s \cdot j-\ell+1}, \ldots, x_{s \cdot j}: 현재까지 생성된 토큰 중 직전 \ell 길이의 토큰만 query로 활용

## 3-3. Reranking

### 3-3-1. LM as Zero-Shot Rerankers

- LM을 학습없이 Reranker로 활용하는 방법론 제시

- k: Top-k개의 Retrieved Document

- Objective: k개의 Document 중 성능 개선에 도움을 줄 수 있는 top-1 doc을 rerank

- 입력된 text의 일부를 validation data로 활용

- reranking: 입력 텍스트의 마지막 s'개 토큰 PPL을 최소화하는 document 탐색 작업

### 3-3-2. Training LM-dedicated Rerankers

- RoBERTa를 훈련하여 Reranker로 활용하는 방안 제시

- Relevance Score: Reranker의 score를 normalize하여 사용

- Training Objectives: PPL을 낮추는 Document의 Relevance Score를 높이도록 학습

# 4. Experiments

## 4-1. Experiment Setup

### 4-1-1. Datasets

1. **Language Modeling(Perplexity)**

1. **Open-Domain Question Answering(Exact Match)**

### 4-1-2. Models

1. **Language Models**

1. **Retriever**

1. **Reranker**

## 4-2. Effectiveness of Retriever

### 4-2-1. 모델 별 RALM 적용 시 성능 변화(s=4, l=32)

{% include figure.liquid loading="eager" path="assets/img/posts/2024-07-30-in-context-retrieval-augmented-language-models/image_003.png" class="img-fluid rounded z-depth-1" %}

***모델 크기와 관계없이 RALM 적용 시 성능이 개선됨***

- BM25: RETRO 및 RAG와 다르게 LM과 함께 학습된 Retriever X, Sparse Retriever

- 모든 모델에서 RALM 적용 시 PPL이 개선되는 모습

- 큰 모델 w/o Retriever < 작은 모델 w/ Retriever
