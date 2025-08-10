---
categories:
- paper-reviews
date: '2025-06-17 00:00:00'
description: 논문 리뷰 - Text Generation, DiffusionLM 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- diffusion
- diffusionlm
- fine-tuning
- gpt
- language-model
- llm
- paper-review
- reasoning
- text generation
- transformer
- vision
thumbnail: assets/img/posts/2025-06-17-diffusion-of-thought-chain-of-thought-reasoning-in/thumbnail.jpg
title: 'Diffusion of Thought: Chain-of-Thought Reasoning in Diffusion Language Models'
---

**논문 정보**
- **Date**: 2025-06-17
- **Reviewer**: 상엽
- **Property**: Text Generation, DiffusionLM

https://huggingface.co/blog/ProCreations/diffusion-language-model?utm_source=chatgpt.com

## Introduction

**도입 배경**

- LLM의 엄청난 성장 → Chain-of-Thought (CoT)와 같은 Reasoning이 핵심 기법으로 부상

- CoT는 중간 추론 단계를** autoregressive 방식**으로 생성하여 **LLM의 추론 능력을 향상**시킴

- 하지만 **기존 CoT의 한계점**들이 존재

**Diffusion Model의 등장**

- Vision 영역에서의 성공에 이어 텍스트 처리 분야에서도 주목받기 시작

- **Why?** Autoregressive model 대비 고유한 강점을 보유

- **Pre-trained diffusion language model** → Plaid, SEDD 등 (최근에는 Llama3-8B 정도 수준의 LlaDA 모델 등장)

**RQ**

**Diffusion of Thoughts (DoT) 제안**

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/cbee75df-cc0f-4355-b2bd-7609cbbb1f9b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SJJ5N7B%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113434Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgNg3tG7UZZqN7Sl0st7rUrcfW567mkoHNCApa19nqfQIgb8kAKIy4WfuTvX%2B1u30h%2FhADlqQUPe%2Bss1lWwg9okVEqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKqsgJd6o11ExIW4AircA%2FOpYrgShwwauKB%2B4xxIM2ueNmdd45asDAgLKdKU2gjp2rFbpTa0bJmo86uhJSiubaldNonpjlG0k5yWe2tJrxQj7UiPkcxBShQTLGYh5aWnS%2BkHmz2JqVzMsk0Y%2F6RHTPPU5bw2Uz%2BKH1yVj5LzS9S9u99OklnVh86NnwfQx304ddfWQTU%2FBePUkabQEEKdYcn7LYLi15OPdtVN8p7mZx669nd230%2FMCUBIzMKPyjx3or5jpNQhbxTMa8t8XgWTeX0pebKpXv1Lu1WFCyxbJFPnW8sR5DbzdEy8GvmTweqsfJUH7tlOi0GlV519rz3q3dd00NuMA2U4y%2FrjKi%2BWJ6uMIGtT9pBWkT0uNH1M3QIn%2F0C9xi%2B5T%2BjuQIFVCxtejDp7kllVkSqEva923IewjJ%2BMeMgPi9dNfsbENMeWVO4pFYF0J8CtBhxiEINqoGNHFQWThh%2BBwkxWcTp%2FsgUvwvSd83nPlDHTuA3uAAMD94EO%2Fl95dxhxjiINuCDmmMRaIWL9A%2Bj%2FV8NSLTvs%2BE1Ek4kIqXjFbYKg%2B97nP1otcX9BbJ5IP09dATbqd%2Ba8stbZ8GBIEF%2BYkkLm9WsB8lEGpGMzvJjfCOowWwxdHHJU6i%2B%2FbWgWy231rbWi6A4NMLr%2B4cQGOqUBkUQi51rdYmjBJrcw%2BsYjt3hW9kB6vafqHpniyZBVtycaqK76lTDHfJeNYQ7C9W3vnvSySlrbCl1cT%2BX83iQYmwQ24OmgGkGdjkf2o45ymFHSowEsdi1ihRdm03TW3KcQ7swIMhcU6LEyAyk7a%2Ftux%2Bw9at%2FpwlBQP3esGDV9Jx4PwctWceqzRGIdLTl2y6V9WlYZNa8e1cLYOKq9z5jWAE9VU2WZ&X-Amz-Signature=695db8b81f39f3a1f8c8307644ba556aff1d95b8c8cccc8e8912b405b1c86216&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- **Diffusion model에 특화된 inherent chain-of-thought 방법 제안**

- 핵심 특징

## Preliminaries

**기본 개념**

- Forward process

- Reverse process

- Text generation을 위한 diffusion 모델의 종류

**Seq2Seq Generation (e.g. DiffuSeq)**

- 입력-출력 sequence를 single sequence로 처리: \mathbf{w}^{z}=\mathbf{w}^{[x; y]}

- Left-aligned mask [\mathbf{0};\mathbf{1}]로 x, y를 구분

- **Partial noising**: mask value가 1인 부분에만 noise 적용

## Diffusion-of-Thoughts

- Notation: s (problem statement), a (answer), p_{\theta}^{LM} (language model)

- Answer-only generation model: \mathbf{a}\sim p_\theta^{\textit{LM}}(\mathbf{a}|\mathbf{s})

- CoT: \mathbf{a}\sim p_\theta^{\textit{LM}}(\mathbf{a}|\mathbf{s}, \mathbf{r}_{1\dots n})

- implicit CoT: \mathbf{a}\sim p_\theta^{\textit{iCoT}}(\mathbf{a}|\mathbf{s}, \mathbf{z}_{1\dots n})

- DoT: \mathbf{a}\sim p_\theta^{\textit{DoT}}(\mathbf{a}|\mathbf{s}, \mathbf{z}_t)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/7bde22d3-df55-4fed-824e-ed43cf2b175e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SJJ5N7B%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113434Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgNg3tG7UZZqN7Sl0st7rUrcfW567mkoHNCApa19nqfQIgb8kAKIy4WfuTvX%2B1u30h%2FhADlqQUPe%2Bss1lWwg9okVEqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKqsgJd6o11ExIW4AircA%2FOpYrgShwwauKB%2B4xxIM2ueNmdd45asDAgLKdKU2gjp2rFbpTa0bJmo86uhJSiubaldNonpjlG0k5yWe2tJrxQj7UiPkcxBShQTLGYh5aWnS%2BkHmz2JqVzMsk0Y%2F6RHTPPU5bw2Uz%2BKH1yVj5LzS9S9u99OklnVh86NnwfQx304ddfWQTU%2FBePUkabQEEKdYcn7LYLi15OPdtVN8p7mZx669nd230%2FMCUBIzMKPyjx3or5jpNQhbxTMa8t8XgWTeX0pebKpXv1Lu1WFCyxbJFPnW8sR5DbzdEy8GvmTweqsfJUH7tlOi0GlV519rz3q3dd00NuMA2U4y%2FrjKi%2BWJ6uMIGtT9pBWkT0uNH1M3QIn%2F0C9xi%2B5T%2BjuQIFVCxtejDp7kllVkSqEva923IewjJ%2BMeMgPi9dNfsbENMeWVO4pFYF0J8CtBhxiEINqoGNHFQWThh%2BBwkxWcTp%2FsgUvwvSd83nPlDHTuA3uAAMD94EO%2Fl95dxhxjiINuCDmmMRaIWL9A%2Bj%2FV8NSLTvs%2BE1Ek4kIqXjFbYKg%2B97nP1otcX9BbJ5IP09dATbqd%2Ba8stbZ8GBIEF%2BYkkLm9WsB8lEGpGMzvJjfCOowWwxdHHJU6i%2B%2FbWgWy231rbWi6A4NMLr%2B4cQGOqUBkUQi51rdYmjBJrcw%2BsYjt3hW9kB6vafqHpniyZBVtycaqK76lTDHfJeNYQ7C9W3vnvSySlrbCl1cT%2BX83iQYmwQ24OmgGkGdjkf2o45ymFHSowEsdi1ihRdm03TW3KcQ7swIMhcU6LEyAyk7a%2Ftux%2Bw9at%2FpwlBQP3esGDV9Jx4PwctWceqzRGIdLTl2y6V9WlYZNa8e1cLYOKq9z5jWAE9VU2WZ&X-Amz-Signature=37540cb9592e31c72013b741fe754b14c50e984cae3527cd450df928258d06ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### DoT Modeling

- **Gradient-based token guidance의 한계**

**→ DiffuSeq-style classifier-free conditioning 채택**

→ continuous 방식의 DiffuSeq-style이 가진 장점이 무엇인가?

**Multi-pass DoT (MP-DoT)**

- Causal inductive bias 도입 thought-by-thought 방식으로 rationales을 생성하는 방법 제안

- **Process**:

- 이후 rationale이 이전 rationale들을 더 강한 condition signal로 이용할 수 있음.

### Training

**Scheduled Sampling**

- Diffusion 모델이 denoising을 하는 과정에서 이미 self-correcting 능력이 있다고 할 수 있음. → Sampling 과정을 통해 이를 더욱 발전

- Training과 inference 간의 **exposure bias**가 error를 발생시킨다고 생각

- Any timesteps: s, t, u that satisfy 1 < s < t < u < T

- **해결책**: 추론 단계를 모방하기 위해 \epsilon_i 확률로 다음과 같이 forward step에서 만들어진 z를 활용

**Coupled Sampling**

- Multi-pass DoT에서 rationale에 쌓이는 error accumulation 문제 해결

- **Training 시 현재 thought뿐만 아니라 이전 thought들에도 확률적으로 noise 추가**

**Training Objective**

DoT 모델에 대해 두 가지 학습 방법을 사용

- from scratch

- fine-tuning from pre-trained diffusion model

**공통 Objective function:** Negative variational lower bound 최소화

- z_t를 denoising 함으로써 z_0를 복원하는 것을 배우는 것

- **Prior loss**

- **Diffusion loss**: 각 단계에서 얼마나 noise를 잘 제거하는가에 대한 탐색

- **Rounding loss**: 복원력 z_0 → \text{w}^z

### Inference Strategy

- diffusion 모델의 추론 flexibility는 큰 장점 → 어려운 문제일수록 더 많은 reasoning time을 가져야 함. → backward timestep T를 크게 가져가자! (이거 안되는 게 있나? 논문에서 autoregressive 방법에서 토큰 수를 조절하는 것은 더 어렵다고 주장.)

- **문제**: Continuous diffusion의 높은 timestep 요구사항 (예: Plaid 4096 timesteps)

→ ODE solver를 conditional form을 활용해 accelerate

- 이게 최종식인데 미분방정식 얘기가 나와서 아직은 모르겠습니다….

**Self-consistency Integration**

- Multiple sampling을 통한 다양한 reasoning pathway 생성

- 동일 문제 s에 대해 다양한 (r_{i;1...n}, a_i)를 구함. (Diffusion 모델의 강점: noise seed만 다르게 해도 됨!)

- Majority vote:

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/1b55f68d-7994-4dad-9980-633a0f0ee17c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SJJ5N7B%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113434Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgNg3tG7UZZqN7Sl0st7rUrcfW567mkoHNCApa19nqfQIgb8kAKIy4WfuTvX%2B1u30h%2FhADlqQUPe%2Bss1lWwg9okVEqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKqsgJd6o11ExIW4AircA%2FOpYrgShwwauKB%2B4xxIM2ueNmdd45asDAgLKdKU2gjp2rFbpTa0bJmo86uhJSiubaldNonpjlG0k5yWe2tJrxQj7UiPkcxBShQTLGYh5aWnS%2BkHmz2JqVzMsk0Y%2F6RHTPPU5bw2Uz%2BKH1yVj5LzS9S9u99OklnVh86NnwfQx304ddfWQTU%2FBePUkabQEEKdYcn7LYLi15OPdtVN8p7mZx669nd230%2FMCUBIzMKPyjx3or5jpNQhbxTMa8t8XgWTeX0pebKpXv1Lu1WFCyxbJFPnW8sR5DbzdEy8GvmTweqsfJUH7tlOi0GlV519rz3q3dd00NuMA2U4y%2FrjKi%2BWJ6uMIGtT9pBWkT0uNH1M3QIn%2F0C9xi%2B5T%2BjuQIFVCxtejDp7kllVkSqEva923IewjJ%2BMeMgPi9dNfsbENMeWVO4pFYF0J8CtBhxiEINqoGNHFQWThh%2BBwkxWcTp%2FsgUvwvSd83nPlDHTuA3uAAMD94EO%2Fl95dxhxjiINuCDmmMRaIWL9A%2Bj%2FV8NSLTvs%2BE1Ek4kIqXjFbYKg%2B97nP1otcX9BbJ5IP09dATbqd%2Ba8stbZ8GBIEF%2BYkkLm9WsB8lEGpGMzvJjfCOowWwxdHHJU6i%2B%2FbWgWy231rbWi6A4NMLr%2B4cQGOqUBkUQi51rdYmjBJrcw%2BsYjt3hW9kB6vafqHpniyZBVtycaqK76lTDHfJeNYQ7C9W3vnvSySlrbCl1cT%2BX83iQYmwQ24OmgGkGdjkf2o45ymFHSowEsdi1ihRdm03TW3KcQ7swIMhcU6LEyAyk7a%2Ftux%2Bw9at%2FpwlBQP3esGDV9Jx4PwctWceqzRGIdLTl2y6V9WlYZNa8e1cLYOKq9z5jWAE9VU2WZ&X-Amz-Signature=ce50238395c67cb52a7e4bd37eb2d819c8a2545773d1acba99af3d32a851ec44&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Evaluation

### Experimental Setup

**데이터셋 및 메트릭**

- **Simple reasoning**:

- **Complex reasoning**: GSM8K grade school math problems

**Base Model**

- **From scratch**: Following DiifuSeq (12-layer Transformer encoder, 124M)

- **Pre-trained model for fine-tuning**:

**Baseline**

- Answer-only, CoT, Implicit CoT

- GPT-2 (small 124M, medium 355M, large 774M)

- ChatGPT (gpt-3.5-turbo-1106) with 5-shot CoT
