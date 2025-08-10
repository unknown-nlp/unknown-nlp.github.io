---
categories:
- paper-reviews
date: '2024-01-16 00:00:00'
description: 논문 리뷰 - LLM 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- attention
- gpt
- llm
- paper-review
- pre-training
- reasoning
- transformer
thumbnail: assets/img/posts/2024-01-16-mistral-7b-mixtral-mixtral-of-experts/thumbnail.jpg
title: Mistral 7B & Mixtral (Mixtral of Experts)
---

**논문 정보**
- **Date**: 2024-01-16
- **Reviewer**: 준원 장
- **Property**: LLM

## 1. Mistral 7B

### Introduction

→ Higher Model Performance는 model size의 escalation을 필수로 요구하는 시대.

→ Scaling trends가 computational cost, inference latency로 deployment 환경에서 방해물이 되기 때문에 high-level performance와 efficiency를 동시에 달성할 수 있는 balanced model을 굽는게 필요.

- 이를 동시에 달성하는 Mistral 7B를 Apache 2.0 license로 베포함

- Mistral  7B는 Llama2 13B model을 측정한 모든 benchmark에서 이겼으며 mathematics와 code generation에서는 Llama1 34B보다도 좋은 성능을 보임.

- Mistral 7B는 기본적으로 Transformer Decoder Architecture를 채택하며 아래 2가지 techniques을 채택하여 efficiency를 달성

(+ vLLM inference server와 SkyPilot을 활용해서 cloud에서 쉽게 쓸 수 있도록 베포했다고 함…)

### **Architectural details**

**#### Overall Model Architecture**

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-16-mistral-7b-mixtral-mixtral-of-experts/image_000.png" class="img-fluid rounded z-depth-1" %}

**#### Sliding Window Attention**

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-16-mistral-7b-mixtral-mixtral-of-experts/image_001.png" class="img-fluid rounded z-depth-1" %}

→ Attention

- number of operations in vanilla attention is *quadratic* in the sequence length.

- memory increases *linearly* with the number of tokens.

→ Sliding Window Attention

- receptive field : k(attention layer) * w (window size)

- 이론적으로 4096*32 \approx 132k을 attention span으로 처리할 수 있는데, w=4096으로 두고 16K sequence을 Flash attention&Xformers을 적용해서 처리하면 vanllia attention대비 2배 빠른 성능을 보인다고 함.

→ Rolling Buffer Cache

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-16-mistral-7b-mixtral-mixtral-of-experts/image_002.png" class="img-fluid rounded z-depth-1" %}

- attention span이 고정되어 있다 = rolling buffer (데이터를 담는 공간) cache를 limit할 수 있다.

- (아마 가상화한) cache 메모리를 W로 설정한 다음 timestep i의 key, value 값을 cache memory에 저장하면서 cache 메모리를 효율적으로 사용할 수 있음.

- position는 ‘i mod W’로 두고 W보다 큰 token이 들어오면 cache memory를 overwritten해서 (e.g., 4097 % 4096 = 1 → 1번 position overwritten) cache 메모리가 커지는걸 방지할 수  있음.

- Sequence length가 길어질 때 model quality impact 영향 안미치고 처리가 가능하다고 함.

**#### Pre-fill and Chunking (GQA)**

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-16-mistral-7b-mixtral-mixtral-of-experts/image_003.png" class="img-fluid rounded z-depth-1" %}

- generation시에 token을 one-by-one으로 generation하는데 (as each token is conditioned on the previous ones) 

- 주어진 prompt는 미리 알기 때문에 cache에 prompt의 k,v값을 pre-fill해서 inference 속도를 향상시킬 수 있음.

- prompt가 크다면, chunk-size = window-size로 자르고 k,v를 계산하고 해당 chunck 내에서의 attention (third chunk in figure) 과 sliding window attention과 caching 사용한 attention(center block)을 동시에 사용해서 2W구간에 빠르게 연산처리.

### Results

→ Evaluation Pipeline을 직접 구축해서 Llama와 Mistral 7B를 아래의 benchmark에 재측정

- **Commonsense Reasoning (0-shot): **Hellaswag [28], Winogrande [21], PIQA [4], SIQA [22],
OpenbookQA [19], ARC-Easy, ARC-Challenge [9], CommonsenseQA [24]

- **World Knowledge (5-shot): **NaturalQuestions [16], TriviaQA [15]

- **Reading Comprehension (0-shot): **BoolQ [8], QuAC [7]

- **Math: **GSM8K [10] (8-shot) with maj@8 and MATH [13] (4-shot) with maj@4

- **Code: **Humaneval [5] (0-shot) and MBPP [2] (3-shot)

- **Popular aggregated results: **MMLU [12] (5-shot), BBH [23] (3-shot), and AGI Eval [29]
(3-5-shot, English multiple-choice questions only)

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-16-mistral-7b-mixtral-mixtral-of-experts/image_004.png" class="img-fluid rounded z-depth-1" %}

→ (Evaluation Pipeline이 Llama 원문과는 다르지만) Llama 7, 13B보다 성능 훨씬 좋음

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-16-mistral-7b-mixtral-mixtral-of-experts/image_005.png" class="img-fluid rounded z-depth-1" %}

→ Code-Llama와 달리 MBPP(Code generation task)에서의 성능을 위해 나머지 task의 성능을 해치지 않음.

- Llama2 family군과 비교했을 때 동일한 size대비 Mistral은 어느정도의 성능을 보이는가?

**#### Instruction Finetuning**

- Hugging Face repository에 public하게 풀려있는 instruction sft dataset으로 sft를 진행. 

→ Llama2-13B보다 성능이 좋다.

## 2. Routing

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-16-mistral-7b-mixtral-mixtral-of-experts/image_006.png" class="img-fluid rounded z-depth-1" %}

- Routing이란, 컴퓨터 네트워크에서 정보나 데이터 패킷이 출발지부터 목적지까지 최적의 경로를 따라 전송되는 과정. 

- 우리가 인터넷에서 웹사이트를 방문하거나 이메일을 보낼 때, 그 정보는 여러 대의 컴퓨터나 스위치(Gateway, L2Access), 라우터 등을 거쳐 수신자에게 도달함.

- Routing은 이러한 네트워크 장비들이 각각의 정보 패킷을 어디로 보내야 할지를 결정하는 메커니즘을 뜻함. 우편 시스템이나 도로 교통망과 비슷함. (일종의 교차로? 고속도로의 톨게이트? 물류체계의 물류거점?을 기반으로 데이터가 유통되는 과정)

## 3. Mixtral 8X7B

### Introduction

→ Mistral 7B과 동일한 Apache 2.0 license 아래에 open-weight인 sparse mixture of experts model (SMoE)인 Mixtral 8X7B를 베포함.

→ Mixtral 8X7B는 대부분 benchmark에서 Llama2 70B와 latest gpt3.5보다 좋은 성능을 보임.

→ Decoder only model이며, 매 token마다 router network가 8개 중 2개의 expert만 active시켜서 연산을 시킨다는 점에서 늘어나는 parameter대비 실제로 연산하는 active하는 parameter는 적은 sparse model.

→ 32k context size를 활용한 Multilingual data로 pre-training.

→ chat-bot model은 SFT → DPO.

(Megablocks CUDA kernels을 통합해서 쓸 수 있게 해줬다라고 함… :: 뭔소리인지 모르겠…)

### **Architectural details**

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-16-mistral-7b-mixtral-mixtral-of-experts/image_007.png" class="img-fluid rounded z-depth-1" %}

**#### Overall Model Architecture**

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-16-mistral-7b-mixtral-mixtral-of-experts/image_008.png" class="img-fluid rounded z-depth-1" %}

→ Mistral과 다른점은 

- Fully dense context length of 32k tokens. (Sliding Window 적용 X)

- MLP layer가 SMoE Layer로 대체가 되었다.

**#### Sparse Mixture of Experts**

- n개의 Expert E가 아래와 같이 있다고 할 =때,

- MoE 식은 다음과 같이 작성할 수 있다. (x는 각 token)

- Gating Vector를 Sparse하게 만들면 → router가 sparse한 value를 갖는 Expert로 x를 forwarding 시킬 필요가 없음 → Experts에 대한 computation cost save

→ Total parameter count = n이 증가하더라도, K를 고정하면 individual token을 처리하는 active parameter count는 k는 증가하지 않음 (물론 network latency는 증가 당연히..)

- MoE Layer를 Efficient하게 처리하는 방법 

- Mixtral 8X7B는 MLP 대신 SwiGLU를 expert function E(x)로 활용함

### Results

→ Mistral 7B와 마찬가지로 Evaluation Pipeline을 직접 구축해서 Llama2와 Mistral 7B를 아래의 benchmark에 재측정

- **Commonsense Reasoning (0-shot): **Hellaswag [32], Winogrande [26], PIQA [3], SIQA [27],
OpenbookQA [22], ARC-Easy, ARC-Challenge [8], CommonsenseQA [30]

- **World Knowledge (5-shot): **NaturalQuestions [20], TriviaQA [19]

- **Reading Comprehension (0-shot): **BoolQ [7], QuAC [5]

- **Math: **GSM8K [9] (8-shot) with maj@8 and MATH [17] (4-shot) with maj@4

- **Code: **Humaneval [4] (0-shot) and MBPP [1] (3-shot)

- **Popular aggregated results: **MMLU [16] (5-shot), BBH [29] (3-shot), and AGI Eval [34]
(3-5-shot, English multiple-choice questions only)

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-16-mistral-7b-mixtral-mixtral-of-experts/image_009.png" class="img-fluid rounded z-depth-1" %}

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-16-mistral-7b-mixtral-mixtral-of-experts/image_010.png" class="img-fluid rounded z-depth-1" %}

→ Code generation & Math에서 특히 성능이 좋다.
