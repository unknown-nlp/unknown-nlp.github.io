---
categories:
- paper-reviews
date: '2025-02-04 00:00:00'
description: 논문 리뷰
giscus_comments: true
layout: post
related_posts: false
tags:
- attention
- language-model
- neural
- paper-review
- transformer
thumbnail: assets/img/posts/2025-02-04-titans-learning-to-memorize-at-test-time/thumbnail.jpg
title: 'Titans: Learning to Memorize at Test Time'
---

**논문 정보**
- **Date**: 2025-02-04
- **Reviewer**: 준원 장

## 1. Introduction

- Transformer

- Overcome the scalability issue of Transformers

- Limitation of recurrent neural network 

- Memory Perspective

- 위의 논의들을 바탕으로 논문에서는 5개 RQ를 던짐

## 2. Preliminaries

### Notations

- Input: x ∈ ℝ^{(N×d_m)}

- Neural Network Module: \mathcal{M} 

- Attention Mask: M

- Segment

- Neural Network

### Backgrounds

- Transformers

- Efficient Attentions (linear attentions)

- RNN

> 결국 sequence가 길어짐에 따라 모델이 forwarding 하면서 풀어야 하는 문제는 2개로 좁혀짐 (memory module을 잘 추가해야 하는건 여기에선 당연한 문제)

1. forget mechanism을 잘 추가해 memory 적재를 줄이느냐? (xLSTM, Mamaba2)

1. write operation를 improving시키냐? (뭐 논문 설명을 보면 잘 지우면서 write시키냐, 병렬처리학습이 가능하냐로 설명함)

## 3. Learning to Memorize at Test Time

### 3.1 Long-term Memory

→ memorization이 가능한 learning function, 데이터가 들어오면 해당 데이터를 모듈이 어떻게 저장하는지에 대한 방법을 학습

- **Learning Process and Surprise Metric.**

- **Objective.**

- **Forgetting Mechanism.**

- **Memory Architecture.**

- **Retrieving a Memory.**

### 3.2 How to Parallelize the Long-term Memory Training

→ long-term memory module 학습시에 긴 sequence를 parallel하게 학습할 수 있다.를 수식적으로 보여준 부분

- \mathcal{M}_0에서 학습시작

- t': 0

- t: b

- \beta_i = \prod_{j=1}^i(1-\alpha_j)

 →각 청크(rank)에 관련된 행렬을 저장함으로 분산학습 가능

→ 각 chunk에 대한 u_t를 구해놓고 recurrent하게 `surprise` value값 구하기 가능

### 3.3 Persistent Memory

→ 학습 가능하지만 input-independent한 파라미터 세트를 사용하여 task-related memory로 활용하고자 함

(여기서부터 2016-2019 모델링 연구 느낌 너무 강함;;;)

- prefix/prompt tuning처럼 sequence앞에 task-specific learnable (inference에서는 fix인) parameter를 도입

- 그럼 저자들은 이 module을 왜 도입했냐?

## 4 How to Incorporate Memory?

→ 아래 모든 framework에서 core를 neural network/lm정도로 생각하고 따라가면 된다. 

→ 또한 아래의 모든 framework가 test time에 어떻게 동작하는지를 기준으로 따라가자.

### 4.1 Memory as a Context (MAC)

{% include figure.liquid loading="eager" path="assets/img/posts/2025-02-04-titans-learning-to-memorize-at-test-time/image_000.png" class="img-fluid rounded z-depth-1" %}

→ S^{(i)} \ (i = 1,\ldots,N/C) : sequence를 고정 크기 세그먼트만 처리하는 시스템

1. h_t = \mathcal{M}_{t-1}^*(\mathbf{q}_t) : memory module에서 고정 세그먼트와 유사한 past information retrieve

1. \tilde{S}^{(t)} = [p_1 \quad p_2 \quad \cdots \quad p_{N_p}] | h_t | S^{(t)} \\ y_t = \text{Attn}(\tilde{S}^{(t)}) : persistent memory, past information, 고정 segment를 neural network에 forwarding해서 attention

1. \mathcal{M}_t = \mathcal{M}_{t-1}(y_t) : attention output을 활용해 long-term memory module을 update

1. o_t = y_t \otimes \mathcal{M}_t^*(y_t) : update되 memory module에 attention output을 통과한 후 이를 기존 attention output과 tensor곱 연산 해 최종 output 계산

⇒ 해당 구조의 가장 큰 장점은 attention이 current/longterm에 동시에 attention을 주기 때문에 어떤 정보가 유용한지 파악 후 메모리 용량을 관리하기에 용이하다는 것

### 4.2 Gated Memory (MAG)

{% include figure.liquid loading="eager" path="assets/img/posts/2025-02-04-titans-learning-to-memorize-at-test-time/image_001.png" class="img-fluid rounded z-depth-1" %}

→ 이전처럼 memory module이 current input에 의해 update되긴 하지만 attention에 활용되지는 않음

1. \tilde{x} = [p_1 \quad p_2 \quad \cdots \quad p_{N_p}] | x

1. y = \text{SW-Attn}^*(\tilde{x}) : sliding window attention으로 attention 처리

1. o = y \otimes \mathcal{M}(\tilde{x}) 

### 4.3 Memory as a Layer (MAL)

{% include figure.liquid loading="eager" path="assets/img/posts/2025-02-04-titans-learning-to-memorize-at-test-time/image_002.png" class="img-fluid rounded z-depth-1" %}

→ attention과 neural memory module이 본인들이 설계한 의도를 100% 활용하지 못하도록 설계된 구조.

1. \tilde{x} = [p_1 \quad p_2 \quad \cdots \quad p_{N_p}] | x

1. y = \mathcal{M}(\tilde{x})

1. o = \text{SW-Attn}(y)

→ attention의 장점을 활용못하니 attention 부분을 neural memory module로 바꾼 LMM로 또 다른 실험을 해봤다고 함.

## 5. Experiments

### 5.1 Experimental Setup

- Models

- Training

### 5.2 Results - Language Modeling

{% include figure.liquid loading="eager" path="assets/img/posts/2025-02-04-titans-learning-to-memorize-at-test-time/image_003.png" class="img-fluid rounded z-depth-1" %}

→ attention이 들어간 모델: hybrid model → *표기

→ attention을 안썼는데 가장 성능이 좋은 model → **model**

→ attention을 활용했는데 가장 성능이 좋은 model → **model**

- Titan이 전반적으로 성능이 가장 좋다.

- Mamba, Mamba2, and Gated DeltaNet도 gating mechanism을 쓰지만 본인들의 neural & deep memory가 더 효용이 높다고 하는데 attention 때문에 잘나온게 아닌가?라는 듦.
