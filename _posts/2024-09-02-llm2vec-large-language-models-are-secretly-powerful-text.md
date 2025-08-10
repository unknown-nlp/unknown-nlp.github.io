---
categories:
  - paper-reviews
date: "2024-09-02 00:00:00"
description: 논문 리뷰 - Embeddings, LLM 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
  - attention
  - bert
  - classification
  - embedding
  - embeddings
  - gpt
  - language-model
  - llm
  - paper-review
thumbnail: assets/img/posts/2024-09-02-llm2vec-large-language-models-are-secretly-powerful-text/thumbnail.jpg
title: "LLM2Vec: Large Language Models Are Secretly Powerful Text Encoders"
---

**논문 정보**

- **Date**: 2024-09-02
- **Reviewer**: 김재희
- **Property**: Embeddings, LLM

## 1. Intro

- BERT와 GPT 이후 이어진 Encoder vs Decoder 대전

- Embedding: 여전히 광범위한 태스크에서 활용

## 2. Method

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-02-llm2vec-large-language-models-are-secretly-powerful-text/image_000.png" class="img-fluid rounded z-depth-1" %}

**3단계 과정으로 구성**

### 2-1. Bidirectional Attention

**기존 Decoder only 모델의 Attention layer를 bi-Directional Attention으로 변경 **

### 2-2. MNTP(Masked Next Token Prediction)

**Decoder가 적절히 Embedding task를 학습하도록 유도**

1. 문장 내 임의의 토큰을 마스킹하고, 이전 시점의 representation으로 마스킹된 토큰을 예측

1. BERT의 MTP(Masked Token Prediction)과 GPT의 NTP(Next Token Prediction)의 중간 수준

### 2-3. Unsupervised Contrastive Learning

**Sentence Level의 Representation을 생성하도록 학습**

1. SimCSE 학습 방법론 이용

## 3. Experimental Setup

### Masking Token: “\_”

- Decoder model은 masking token이 없음

- 나는 바보가 아니다. → 나는 \_ 아니다.

### training step (1 A100)

- MNTP: 1,000 step, 100 minutes

- UCL: 1,000 step, 3 hours

### Training Method: LoRA

### Training Dataset

Wikipedia 데이터 이용: 모든 LLM의 사전학습에 포함

- MNTP: Wikitext-103

- UCL: Wikipedia sentences

## 4. Experiments

### 4-1. Word Level Tasks

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-02-llm2vec-large-language-models-are-secretly-powerful-text/image_001.png" class="img-fluid rounded z-depth-1" %}

- token 수준의 representation을 필요로 하는 Task

- 실험 모델

- 실험 해석

### 4-2. Sentence Level task

MTEB 벤치마크 내 15개 태스크에 대한 평균값

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-02-llm2vec-large-language-models-are-secretly-powerful-text/image_002.png" class="img-fluid rounded z-depth-1" %}

- Pooling 방법론과 관계없이 SimCSE가 가장 좋은 성능을 보임

- Mistial: Bidirectional Attn만 적용하더라도 성능 개선이 관찰되는 모습을 보임

### 4-3. MTEB Benchmark

- MTEB: Retrieval, Rerank, Clustering, Sentence Pair Classification, STS, Extractive Summarization 등 Encoder용 태스크에 대한 범용 벤치마크 데이터셋

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-02-llm2vec-large-language-models-are-secretly-powerful-text/image_003.png" class="img-fluid rounded z-depth-1" %}

- Echo Embedding: 동일 문장을 두번 반복하여 입력하고, 뒷 문장에서 Representation을 획득하는 방법

- Uni + Mean: Decoder 모델의 Representation에 대해 mean pooling 적용

- Bi + Mean: Decoder 모델에 대해 Bi Attn만 적용하고 모든 token에 대한 Mean pooling 이용

- LLM2Vec(w/o SimCSE): 거의 모든 태스크에서 Uni + Mean 대비 높은 성능 도출

- LLM2Vec: 매우 높은 성능 도출

### 4-4. Analysis 1(MNTP의 효과)

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-02-llm2vec-large-language-models-are-secretly-powerful-text/image_004.png" class="img-fluid rounded z-depth-1" %}

**LLM2Vec을 통해 학습되는 것은 무엇인가?**

- B, C: 비슷한 의미의 문장

- B, D: 다른 의미의 문장

- A 문장의 토큰에서 pooling하여 representation을 산출

- 모델 크기에 관계없이 MNTP 이후 pos와 Neg 간 거리가 벌어짐

### 4-5. Analysis 2(why Mistral works)

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-02-llm2vec-large-language-models-are-secretly-powerful-text/image_005.png" class="img-fluid rounded z-depth-1" %}

- 동일 데이터에 대한 original attention(llm)과 bi directional attention 시의 token/layer 단위 Representation 비교

## 5. Conclusion

- Decoder 모델을 Encoder로 전환하는 방법론 제안

- 단순: 1,000 step, 128 batch size, 1 a100 80GB면 충분히 학습이 됨

- 범용: MNTP + SimCSE로 학습된 모델은 범용적인 encoder로서 사용 가능

- Encoder Pretraian 시 scaling 효과가 없는 상황에서 Encoder 분야 향후 발전 방향
