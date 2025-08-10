---
categories:
- paper-reviews
date: '2024-06-11 00:00:00'
description: 논문 리뷰 - Natural Language Generation 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- attention
- embedding
- gpt
- language-model
- llm
- natural language generation
- paper-review
thumbnail: assets/img/posts/2024-06-11-contextual-position-encoding-learning-to-count-whats-important/thumbnail.jpg
title: 'Contextual Position Encoding: Learning to Count What’s Important'
---

**논문 정보**
- **Date**: 2024-06-11
- **Reviewer**: 김재희
- **Property**: Natural Language Generation

## 1. Intro

- Positional Encoding: Self Attn 시 처리되는 각 토큰들에 대해 위치 정보를 삽입하는 것 

- 왜 필요하쥬?

- Absolute PE: Attention is All You Need 방식

- Relative PE: 다양한 Encoder 및 Enc-Dec 모델 등에서 많이 사용되는 방식

- Rotary PE: 더 최근에 많이 사용되는 방식

## 2. Motivation

### Problem Definition

sequence: yyyy**x**yy**y** → x

- 마지막 시점에서 query에 대해 두 토큰 **x**와 **y**에 대한 token의 attention 관계 

- 마지막 시점에서 query와 두 토큰 **x**(i번째 이전 시점)와 **y**(j번째 이전 시점)의 positional encoding의 attention 관계

- query에 대해서 **x**와 **y**가 가지는 attention의 비 

- 현재 시점과의 self attn과 이전 i번째 시점과의 attn 차이의 minimum bound

- 마지막 시점의 **y**과 **x** 토큰의 attention 값의 차이 (position과 token 모두 고려시)

### Toy Experiments on Current LLM

{% include figure.liquid loading="eager" path="assets/img/posts/2024-06-11-contextual-position-encoding-learning-to-count-whats-important/image_000.png" class="img-fluid rounded z-depth-1" %}

- LLaMA와 GPT에게 두 문장을 제공

## 3. How It Works?

{% include figure.liquid loading="eager" path="assets/img/posts/2024-06-11-contextual-position-encoding-learning-to-count-whats-important/image_001.png" class="img-fluid rounded z-depth-1" %}

- Gating을 이용하여 각 시점의 토큰이 현재 query와 유의미한 관련성이 있는지 계산

- 현재 시점에서 과거로 가면서 gate를 통과한 값을 sum하여 position 값 생성

→ token의 상대 거리마다 다른 position 값이 생성 X, 매우 sparse하게 유의미한 정보 처리를 위해 중요한 단위로 positional encoding 값 생성 가능

- 각 key 토큰의 시점 별 position 값에 대해 positional encoding값 적용

{% include figure.liquid loading="eager" path="assets/img/posts/2024-06-11-contextual-position-encoding-learning-to-count-whats-important/image_002.png" class="img-fluid rounded z-depth-1" %}

→ 문장 단위 정보가 중요한 경우: 문장 별로 다른 position 생성

→ 문서 단위 정보가 중요한 경우: 문서 별 다른 position 생성

→ 단어 단위 정보가 중요한 경우 : 단어 별 다른 position 생성

### Computation Issue

- CoPE 방식의 경우 3가지 Computation Cost 발생

## 4. Experiments

### Flip-Flop

{% include figure.liquid loading="eager" path="assets/img/posts/2024-06-11-contextual-position-encoding-learning-to-count-whats-important/image_003.png" class="img-fluid rounded z-depth-1" %}

- 컴퓨터 메모리에 데이터를 저장하는 것과 유사하게 간단한 sequence 구성하는 toy experiment

- 명령 종류

- 해당 태스크 해결을 위해서 모델은 ignore 명령어를 무시하고 write 토큰에 대해 매우 높은 attention을 부여해야 함

- 학습: 매우 작은 모델(h: 256, head: 4, layer:4)에 대해 학습 데이터로 10k step 학습 진행

**실험 결과**

- Absolute PE: In/Out-of-Domain 모두 매우 안좋은 성능 달성

- RoPE: In에서는 높은 성능 달성 but OOD에서 Absolute PE 수준의 성능 저하 발생

- CoPE: OOD에서도 양호한 성능 관찰

### Selective Copy

{% include figure.liquid loading="eager" path="assets/img/posts/2024-06-11-contextual-position-encoding-learning-to-count-whats-important/image_004.png" class="img-fluid rounded z-depth-1" %}

- 입력된 토큰 중 특정 토큰을 제외하고 출력하는 태스크

- 입력 문장에 대해 이해하고 추론하는 능력 요구

- example: D**BB**CF**B**F**B**E → DCFFE

- ID: 256 **B **토큰 포함

- Dense OOD: 128 **B **토큰 포함

- Sparse OOD: 512 **B **토큰 포함

### 실험결과

- Absolute PE: OOD에 대해 제대로 추론하지 못하는 모습 

- RoPE: OOD에 대해 제대로 추론하지 못하는 모습

- CoPE: OOD와 ID 모두 잘 수행하며 일반화 성능 보유

### Language Modeling

{% include figure.liquid loading="eager" path="assets/img/posts/2024-06-11-contextual-position-encoding-learning-to-count-whats-important/image_005.png" class="img-fluid rounded z-depth-1" %}

- GPT-2 모델 구조를 이용하여 Wikitext와 Code 데이터 각각에 대해 훈련 및 평가 진행

- Context Length: 1024

- Wikitext와 Code 모두에 대해 높은 성능 달성 확인

{% include figure.liquid loading="eager" path="assets/img/posts/2024-06-11-contextual-position-encoding-learning-to-count-whats-important/image_006.png" class="img-fluid rounded z-depth-1" %}

- WikiText 데이터에 대해 학습 Context Length보다 긴 Context에 대한 평가 진행

- CoPE의 경우 여러 토큰에 대해 동일 position 부여가 가능

- Relative PE: 학습 길이를 넘어가자 ppl이 미친듯이 솟구치는 모습 관찰 가능

- Relative-capped: 학습된 길이 이상의 token 길이 차에 대해 최대 길이 차를 부여하는 방식 (CoPE와 비슷한 예외처리)

- CoPE: 학습된 길이를 넘어서도 충분히 좋은 성능 관찰 가능

### 정성 결과

{% include figure.liquid loading="eager" path="assets/img/posts/2024-06-11-contextual-position-encoding-learning-to-count-whats-important/image_007.png" class="img-fluid rounded z-depth-1" %}

- CoPE를 적용한 경우의 attention map 시각화

- 각 문장 및 문단 별로 attention이 잘 가해지는 모습 확인 가능

- 동일 모델임에도 이와 같은 결과가 가능한 이유

## 7. Conclusion

- position 정보가 꼭 token 단위로 삽입될 필요가 없다는 개념 제안

- position encoding 시 token의 representation을 이용하여 생성하는 방식 제안

- 기존 positional encoding 방식 대비 length generalization 우수함 입증

### Limitations (재희)

- RoPE 및 Relative Positional Embedding 대비 성능 개선 폭이 크지 않음. 

- Long Context에 robust함을 보이기에는 최근 연구들 대비 실험한 text context length가 너무 짧음 

- 실제 동작 여부는 아마 향후 llm 적용 등을 통해 확인할 수 있을듯. 
