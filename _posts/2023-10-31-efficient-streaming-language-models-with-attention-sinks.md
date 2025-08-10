---
categories:
  - paper-reviews
date: "2023-10-31 00:00:00"
description: 논문 리뷰 - LLM 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
  - attention
  - language-model
  - llm
  - paper-review
thumbnail: assets/img/posts/2023-10-31-efficient-streaming-language-models-with-attention-sinks/thumbnail.jpg
title: EFFICIENT STREAMING LANGUAGE MODELS WITH ATTENTION SINKS
---

**논문 정보**

- **Date**: 2023-10-31
- **Reviewer**: 김재희
- **Property**: LLM

## 1. Intro

- Pretrained LM의 Max Length를 늘리는 방법론 제안

- Attention Mechanism 상 단순 Sliding Window 방식의 문제점 지적

## 2. Previous Works

- 매우 긴 입력값이 Pretrain LM에 주어질 경우 두가지 문제점 발생

- 긴 입력을 나누어 처리하는 방법론 역시 존재

{% include figure.liquid loading="eager" path="assets/img/posts/2023-10-31-efficient-streaming-language-models-with-attention-sinks/image_000.png" class="img-fluid rounded z-depth-1" %}

- Window Attention은 성능이 망가지는데, Sliding Window는 그렇지 않다…?

⇒ Long Context를 다루는 기존의 방법론들이 놓치는 무엇인가가 있는 느낌…

## 3. Attention Sink

{% include figure.liquid loading="eager" path="assets/img/posts/2023-10-31-efficient-streaming-language-models-with-attention-sinks/image_001.png" class="img-fluid rounded z-depth-1" %}

- Input과 관계없이 많은 양의 Attention이 첫 토큰으로 쏠리는 모습을 볼 수 있음

### What Makes Attention Sink

{% include figure.liquid loading="eager" path="assets/img/posts/2023-10-31-efficient-streaming-language-models-with-attention-sinks/image_002.png" class="img-fluid rounded z-depth-1" %}

- 위 현상의 원인을 분석하기 위해 2가지 가설 설정

- (x+y) 토큰 조합을 통한 성능 변화 관찰 실험

- 0 + 1024 : 현재 토큰 이전 1024개의 토큰을 이용(Sliding Window)

- 4 + 1020 : 첫 4개 토큰과 현재 토큰 이전 1020개의 토큰의 K, V 값에 대한 attention 수행

- 4”\n” + 1020 : 첫 4개의 토큰을 \n으로 설정하고 2번째 실험과 동일 실험

### Why Attention Goes into Sink Tokens?

- Attention Mechanism을 살펴볼 필요가 있음

- 현재 시점의 Query에서 이전 시점의 Key에 대한 Attention은 아래 식과 같음

- query는 Key들에 대해 Value을 나누어 받게 되는 형태

- 이때 SoftMax 함수에 의해 Query는 이전 시점의 값들에 대해 무조건 Attention을 주어야함

- 위 개념에 대한 아이디어는 올해 7월 블로그 글에 처음 개제됨

## 4. Experiments

### Length에 따른 방법론 별 성능 비교

{% include figure.liquid loading="eager" path="assets/img/posts/2023-10-31-efficient-streaming-language-models-with-attention-sinks/image_003.png" class="img-fluid rounded z-depth-1" %}

- 첫 K개의 토큰을 사용할 수 없어지는 시점부터 Dense Attention, Window Attention 모두 성능이 박살

- Sliding Window의 경우 안정적인 성능을 유지하는 모습

- StreamingLLM(본 논문에서 Attention Sink를 이용해 첫 K개 토큰을 계속 살리는 방법론)은 Sliding Window와 비슷한 성능을 유지

### Pretrain with Learnable Attention Sink

- 모델이 사전 학습 과정에서 첫 토큰들을 Attention Sink로 사용

- Vanilla 모델과 비교하여 Loss 및 Downstream Task 모두에서 살짝 더 좋은 성능을 보임.

{% include figure.liquid loading="eager" path="assets/img/posts/2023-10-31-efficient-streaming-language-models-with-attention-sinks/image_004.png" class="img-fluid rounded z-depth-1" %}

- 방법론 별 성능 차이 크지 않음

### StreamingEval

{% include figure.liquid loading="eager" path="assets/img/posts/2023-10-31-efficient-streaming-language-models-with-attention-sinks/image_005.png" class="img-fluid rounded z-depth-1" %}

- 기존의 QA 데이터셋(ARC)를 전처리하여 Streaming 환경처럼 만든 데이터셋

### Computation Efficiency

{% include figure.liquid loading="eager" path="assets/img/posts/2023-10-31-efficient-streaming-language-models-with-attention-sinks/image_006.png" class="img-fluid rounded z-depth-1" %}

- 결론적으로 Long Context를 다루는 방법 중 StreamingLLM과 Sliding Window만 유의미한 방법

- 연산량, Latency 등을 비교하면, Context Length가 길어질수록 매우 큰 차이를 보이고 있음

## 7. Conclusion

### Attention Sink

- Pretrained LM이 학습 과정에서 고정적으로 등장하는 첫 K개의 토큰에 필요없는 Attention을 버리는 현상

- Attention Mechanism의 특성 상 정보를 받을 필요가 없는 Attention은 의미적 관계와 관계없이 특정 토큰에 주어지게 됨

### StreamingLLM

- Attention Sink 현상을 이용하여 Long Context를 적절히 Handling 하는 방법론

- 기존 Window Attention에서 첫 K개의 토큰 K, V를 유지하는 방법론

### Contribution

- Long Context 상에서 성능 저하가 발생하지 않음

- Sliding Window에 비해 낮은 Computation Cost 발생

### Limitation

- 조금 더 다양한 Downstream Task에 대한 성능 비교 필요
