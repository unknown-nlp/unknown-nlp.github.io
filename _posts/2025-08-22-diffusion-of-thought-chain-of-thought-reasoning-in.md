---
categories:
  - paper-reviews
date: "2025-08-22 00:00:00"
description: 논문 리뷰 - Text Generation, DiffusionLM 관련 연구
giscus_comments: true
layout: post
related_posts: false
slug: 2025-08-22-diffusion-of-thought-chain-of-thought-reasoning-in
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
title: "Diffusion of Thought: Chain-of-Thought Reasoning in Diffusion Language Models"
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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/cbee75df-cc0f-4355-b2bd-7609cbbb1f9b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667W7SH7ZO%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGrKdUh4zK2PX%2BlUfCZE7SG5hQLJjq%2FJ%2FAgVDjh6e%2FkPAiAHK52zT6h7%2BHjfxOzGpameGmLebn3crDOu9ZOtb2zCCCqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMciuMO0ESAebMPDngKtwDI361zBDNI2XgLi7Y6aoMJQED00tySwcDLItmtnOIwodADBrm7Tnt5KV29ZwoZUceDoSeT0dPdPd9vGDrJGHQ7O6KlMwBdKRzArx%2B1oggvTLmcKpfTRhbZUnNXzSLwoBResdUgPWY1lPRro5IqVG9aZjoBhM6U%2FinCnuQW%2FvY84%2FsYx86yznr4FNt2TfR6zk3SynXKrxxNt4yPjd3Oj3dRmxwjAxYskX%2B7%2BiiKkY0e0m3CH%2Bp1e%2FdVsUGYBkovT1y7PQompQvyutw2LTmsnC9vdMfwAtJfEIoCPTEjMEY3XAyaLlcu6U42dMivMFkuADP4bSqR4iI5xt2yQI82vM4PaW1vbc4%2FkctgjK4yEq4D7tRweSHzP6vS9ROevvL8mMmhZPwYhdZNIZqFNfC%2FdiVBuBrx5F4ytfKIYFuAFEjnAgmFXwAw%2B6Xb7qL%2Bl%2FuPbDmXzAOANcYnu4OYNC2DWsl5n0kp24kfWOcj3ydVYQ%2Fa9uc0AmiYnx4WmF9%2Bwlcm21dxHpy48EMUV6z0Prqt4emENCqLVbMw0NjADRCD%2FvZWSL8Erw%2FX7p%2FXtx36CHqsPBfJcxBTdrpwhaxV0WuU0TFKweFjvbT%2BWiafzcetOmuhJ63WR6CiSM%2BTKZr8OswhNThxAY6pgEeGc1T%2FV319yhlHIpB%2BPNgObRCRff%2Fsuf%2FETRdGiPJNcDW4Iw15%2BiJrAAnSo%2FApp8dcMjYuKRSTX%2FqhScf%2FP%2BX1KRcBuq4%2BvmWoyah3Zonhqsz9mAgLTKqItnr%2BNMPvZVtUk83wv3wckpEln2pSDjw95rY%2BTRoh2nM8GebmWcVHEI1gu%2FRRkpgMCk6jGFLkevjMlQfWM4sLPCUsfZQUYAXjGUuZBfQ&X-Amz-Signature=9eed353d21461f454b484ae6caacc622570b8dcd5435aeb05f6ba6a7751467d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

- Notation: s (problem statement), a (answer), p\_{\theta}^{LM} (language model)

- Answer-only generation model: \mathbf{a}\sim p\_\theta^{\textit{LM}}(\mathbf{a}|\mathbf{s})

- CoT: \mathbf{a}\sim p*\theta^{\textit{LM}}(\mathbf{a}|\mathbf{s}, \mathbf{r}*{1\dots n})

- implicit CoT: \mathbf{a}\sim p*\theta^{\textit{iCoT}}(\mathbf{a}|\mathbf{s}, \mathbf{z}*{1\dots n})

- DoT: \mathbf{a}\sim p\_\theta^{\textit{DoT}}(\mathbf{a}|\mathbf{s}, \mathbf{z}\_t)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/7bde22d3-df55-4fed-824e-ed43cf2b175e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667W7SH7ZO%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGrKdUh4zK2PX%2BlUfCZE7SG5hQLJjq%2FJ%2FAgVDjh6e%2FkPAiAHK52zT6h7%2BHjfxOzGpameGmLebn3crDOu9ZOtb2zCCCqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMciuMO0ESAebMPDngKtwDI361zBDNI2XgLi7Y6aoMJQED00tySwcDLItmtnOIwodADBrm7Tnt5KV29ZwoZUceDoSeT0dPdPd9vGDrJGHQ7O6KlMwBdKRzArx%2B1oggvTLmcKpfTRhbZUnNXzSLwoBResdUgPWY1lPRro5IqVG9aZjoBhM6U%2FinCnuQW%2FvY84%2FsYx86yznr4FNt2TfR6zk3SynXKrxxNt4yPjd3Oj3dRmxwjAxYskX%2B7%2BiiKkY0e0m3CH%2Bp1e%2FdVsUGYBkovT1y7PQompQvyutw2LTmsnC9vdMfwAtJfEIoCPTEjMEY3XAyaLlcu6U42dMivMFkuADP4bSqR4iI5xt2yQI82vM4PaW1vbc4%2FkctgjK4yEq4D7tRweSHzP6vS9ROevvL8mMmhZPwYhdZNIZqFNfC%2FdiVBuBrx5F4ytfKIYFuAFEjnAgmFXwAw%2B6Xb7qL%2Bl%2FuPbDmXzAOANcYnu4OYNC2DWsl5n0kp24kfWOcj3ydVYQ%2Fa9uc0AmiYnx4WmF9%2Bwlcm21dxHpy48EMUV6z0Prqt4emENCqLVbMw0NjADRCD%2FvZWSL8Erw%2FX7p%2FXtx36CHqsPBfJcxBTdrpwhaxV0WuU0TFKweFjvbT%2BWiafzcetOmuhJ63WR6CiSM%2BTKZr8OswhNThxAY6pgEeGc1T%2FV319yhlHIpB%2BPNgObRCRff%2Fsuf%2FETRdGiPJNcDW4Iw15%2BiJrAAnSo%2FApp8dcMjYuKRSTX%2FqhScf%2FP%2BX1KRcBuq4%2BvmWoyah3Zonhqsz9mAgLTKqItnr%2BNMPvZVtUk83wv3wckpEln2pSDjw95rY%2BTRoh2nM8GebmWcVHEI1gu%2FRRkpgMCk6jGFLkevjMlQfWM4sLPCUsfZQUYAXjGUuZBfQ&X-Amz-Signature=59654f966a6a1d26f7bf497c375fc334ce532e08a7198d64f95e9e1d3d6b22c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

- 동일 문제 s에 대해 다양한 (r\_{i;1...n}, a_i)를 구함. (Diffusion 모델의 강점: noise seed만 다르게 해도 됨!)

- Majority vote:

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/1b55f68d-7994-4dad-9980-633a0f0ee17c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667W7SH7ZO%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGrKdUh4zK2PX%2BlUfCZE7SG5hQLJjq%2FJ%2FAgVDjh6e%2FkPAiAHK52zT6h7%2BHjfxOzGpameGmLebn3crDOu9ZOtb2zCCCqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMciuMO0ESAebMPDngKtwDI361zBDNI2XgLi7Y6aoMJQED00tySwcDLItmtnOIwodADBrm7Tnt5KV29ZwoZUceDoSeT0dPdPd9vGDrJGHQ7O6KlMwBdKRzArx%2B1oggvTLmcKpfTRhbZUnNXzSLwoBResdUgPWY1lPRro5IqVG9aZjoBhM6U%2FinCnuQW%2FvY84%2FsYx86yznr4FNt2TfR6zk3SynXKrxxNt4yPjd3Oj3dRmxwjAxYskX%2B7%2BiiKkY0e0m3CH%2Bp1e%2FdVsUGYBkovT1y7PQompQvyutw2LTmsnC9vdMfwAtJfEIoCPTEjMEY3XAyaLlcu6U42dMivMFkuADP4bSqR4iI5xt2yQI82vM4PaW1vbc4%2FkctgjK4yEq4D7tRweSHzP6vS9ROevvL8mMmhZPwYhdZNIZqFNfC%2FdiVBuBrx5F4ytfKIYFuAFEjnAgmFXwAw%2B6Xb7qL%2Bl%2FuPbDmXzAOANcYnu4OYNC2DWsl5n0kp24kfWOcj3ydVYQ%2Fa9uc0AmiYnx4WmF9%2Bwlcm21dxHpy48EMUV6z0Prqt4emENCqLVbMw0NjADRCD%2FvZWSL8Erw%2FX7p%2FXtx36CHqsPBfJcxBTdrpwhaxV0WuU0TFKweFjvbT%2BWiafzcetOmuhJ63WR6CiSM%2BTKZr8OswhNThxAY6pgEeGc1T%2FV319yhlHIpB%2BPNgObRCRff%2Fsuf%2FETRdGiPJNcDW4Iw15%2BiJrAAnSo%2FApp8dcMjYuKRSTX%2FqhScf%2FP%2BX1KRcBuq4%2BvmWoyah3Zonhqsz9mAgLTKqItnr%2BNMPvZVtUk83wv3wckpEln2pSDjw95rY%2BTRoh2nM8GebmWcVHEI1gu%2FRRkpgMCk6jGFLkevjMlQfWM4sLPCUsfZQUYAXjGUuZBfQ&X-Amz-Signature=4bb6a9853078d5ef8e72b1d4114a72c840c5b1b85a9c91613db1f75f2b87919a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
