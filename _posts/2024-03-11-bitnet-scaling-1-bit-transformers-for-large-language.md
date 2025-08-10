---
categories:
- paper-reviews
date: '2024-03-11 00:00:00'
description: 논문 리뷰 - LLM, Quantization 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- language-model
- llm
- paper-review
- quantization
- transformer
thumbnail: assets/img/posts/2024-03-11-bitnet-scaling-1-bit-transformers-for-large-language/thumbnail.jpg
title: 'BitNet: Scaling 1-bit Transformers for Large Language Models'
---

**논문 정보**
- **Date**: 2024-03-11
- **Reviewer**: 김재희
- **Property**: LLM, Quantization

The Era of 1-bit LLMs: All Large Language Models are in 1.58 Bits

## 1. Intro

### BitNet

- 1-Bit(1 or -1) parameter로 scratch부터 학습

- 기존 LLM 대비 적은 Inference/Train Cost를 가짐

- 기존 Post Quantization 방법론 대비 높은 성능 기록

### 1-Bit

- 1.58Bit(1,0,-1) parameter로 scratch부터 학습

- 동일 파라미터를 가지는 LLaMA 구조 대비 높거나 비슷한 성능 기록

- (1,0,-1)의 상태를 가지는 bit 구조를 이용한 하드웨어 설계를 통해 모델 학습/추론 파이프라인 최적화 방향성 제안

### 결론

- 정말 제대로 동작하는지 잘 모르겠음

- 최근 LLM과 엄밀한 비교 수행 X

- 1-Bit는 결국 더이상의 Quantization 불가

## 2. BitNet

### Architecture

{% include figure.liquid loading="eager" path="assets/img/posts/2024-03-11-bitnet-scaling-1-bit-transformers-for-large-language/image_000.png" class="img-fluid rounded z-depth-1" %}

- Transformer의 일부 레이어를 1-bit로 quantization하여 사용(original weight가 존재)

- BitLinear: 기존 Transformer 구조에서 연산량이 막대한 Linear Layer를 대체

- Pretrain 과정에서 Linear Layer의 연산량을 감소 및 속도 개선 가능

- Distributed Training: 

- Mixed Precision Training

- High Learning Rate

### Experiments

- FP16 Trasnformer와 비교

- Quantization Method와 비교 

- Energe Consumption 대비 성능 비교 (zero/few shot)

## 3. 1.58bit

### Architecture

- 1.58 bit…?

- 1.58bit: fp16과 비슷한 성능을 내면서 inference cost를 줄일 수 있는 방법

- Modification: BitLinear 구조 거의 그대로 활용

- 모델 구조: LLaMA configuration 사용

### Experiments

- LLaMA Configuration을 이용하여 FP16 Transformer/1.58B scratch부터 학습

- StableLM-3B에서 사용된 데이터 사용(data recipe)

- 메모리 및 latency와 PPL 간 비교

- 모델 크기에 따른 Memory 및 Latency 경향

- OpenSource LLM과 비교 

## 4. Conclusion

- BitNet 

- 1.58B
