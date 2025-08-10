---
categories:
- paper-reviews
date: '2025-08-20 00:00:00'
description: 논문 리뷰 - DiffusionLM, Pre-training 관련 연구
giscus_comments: true
layout: post
related_posts: false
slug: 2025-08-20-diffusion-language-model-mathematical-foundations-inference-optimization
tags:
- bert
- diffusion
- diffusionlm
- language-model
- paper-review
- pre-training
title: Diffusion Language Model-Mathematical foundations & inference optimization
---

**논문 정보**
- **Date**: 2025-01-02
- **Reviewer**: 김재희
- **Property**: DiffusionLM, Pre-training

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/957d5b53-7f78-4268-aef0-e138690a817f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUSPEJOG%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF%2FcMu%2BjxdEEKxK7thbanYSR%2F5nuRQ9LFZ%2BAsD5%2B0z8WAiB3b4PgVmORLdXLnDJSN7WQYQQ1cyARxD%2B%2BtULSe048kSqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMloMHX8dKTW8Mti5rKtwDKxyeFUSDGIMQxZ4UktgQLecXeqB6deZoNkGE3Gc43k3iFl7Xzqm8O19XPGlxzHGKxxukKURmk20rbgdku59wlWXaXOL3Abe0MoHJPJg7omTUgiPlxtNmF8ROwImyTS9V08gkBIrWLJp2YsbottTo%2ByxwI%2FHkL%2BUSjXFbw2Ptr%2BuDfAZXVXAfr2NDOsd6Fb9QaIb7bdUqqVTG%2BAyWmYWRfD95ZaWLe93KgSWegJacFI0b0nvL3rKl9zEY1fDDH3WyqYBo9X6770gaUtyzUuQZC0iARewvlMmWUSS3PMOZmE%2FJMG9yWtFhmrYWM9KKoN8giqHXI8uo6cbDRQ9oHj%2B%2Fd9i0RjMJBGFr%2FkY0vqqYqApyzU8ItKqzFheYmgFNHnDiKIHC8mfj7asezq%2F1cA%2FwQLy7YxcgSTy3OS%2BH8CNVXa%2FeUBs4q9C%2B7VMB0dSP6SdbufsEbAXLXqPhfkkH4DrUxW1NWMxmFBYxo46tu6fT7tdL5Y2ukwvqgFzyfhROLNhqVI0SijJCIB%2FGMg4Ii7tI9eA4fd0JjC1fxSVFKHDvgPqZxM0%2Fffd2Jq9eACCT9wyzxQyD3CZicxsBKyXnKVnHmPcMkGygg71GKalX5SLLgFdzhHT1Hb63AS6Ba%2B4wv9PhxAY6pgFzS6knBXGQUbq6geceDNB3nMamkMCGREbts5SqP8OMzOiC7ewq5Qs82fMOQilIdk52Tw7wLoqJdmAui7WXfhypj6zm6AcJscIveyahZoXzdeNEs95iqtxLMB9f%2BVOJ4Xsk2u7YrCgFesrYe5Ed1aETfjHgHqbJYFfjL4RCO0IWzrzueygDRa7BXh3B%2Bp3%2Fe7V997P4qaLV8cW2TbZ0c1h%2Foga%2B9ZXW&X-Amz-Signature=5260869981df8791a4c868d5074bfd2b1a868914ec60b97877281b087bc8ea8a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# Preliminary

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/c599ee51-549c-4cff-910c-da532df44548/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUSPEJOG%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF%2FcMu%2BjxdEEKxK7thbanYSR%2F5nuRQ9LFZ%2BAsD5%2B0z8WAiB3b4PgVmORLdXLnDJSN7WQYQQ1cyARxD%2B%2BtULSe048kSqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMloMHX8dKTW8Mti5rKtwDKxyeFUSDGIMQxZ4UktgQLecXeqB6deZoNkGE3Gc43k3iFl7Xzqm8O19XPGlxzHGKxxukKURmk20rbgdku59wlWXaXOL3Abe0MoHJPJg7omTUgiPlxtNmF8ROwImyTS9V08gkBIrWLJp2YsbottTo%2ByxwI%2FHkL%2BUSjXFbw2Ptr%2BuDfAZXVXAfr2NDOsd6Fb9QaIb7bdUqqVTG%2BAyWmYWRfD95ZaWLe93KgSWegJacFI0b0nvL3rKl9zEY1fDDH3WyqYBo9X6770gaUtyzUuQZC0iARewvlMmWUSS3PMOZmE%2FJMG9yWtFhmrYWM9KKoN8giqHXI8uo6cbDRQ9oHj%2B%2Fd9i0RjMJBGFr%2FkY0vqqYqApyzU8ItKqzFheYmgFNHnDiKIHC8mfj7asezq%2F1cA%2FwQLy7YxcgSTy3OS%2BH8CNVXa%2FeUBs4q9C%2B7VMB0dSP6SdbufsEbAXLXqPhfkkH4DrUxW1NWMxmFBYxo46tu6fT7tdL5Y2ukwvqgFzyfhROLNhqVI0SijJCIB%2FGMg4Ii7tI9eA4fd0JjC1fxSVFKHDvgPqZxM0%2Fffd2Jq9eACCT9wyzxQyD3CZicxsBKyXnKVnHmPcMkGygg71GKalX5SLLgFdzhHT1Hb63AS6Ba%2B4wv9PhxAY6pgFzS6knBXGQUbq6geceDNB3nMamkMCGREbts5SqP8OMzOiC7ewq5Qs82fMOQilIdk52Tw7wLoqJdmAui7WXfhypj6zm6AcJscIveyahZoXzdeNEs95iqtxLMB9f%2BVOJ4Xsk2u7YrCgFesrYe5Ed1aETfjHgHqbJYFfjL4RCO0IWzrzueygDRa7BXh3B%2Bp3%2Fe7V997P4qaLV8cW2TbZ0c1h%2Foga%2B9ZXW&X-Amz-Signature=e5475294ff023b0a646c0c2c996df5c8cd306e793c9ba76c1bdbd81ff13bdcf1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Forward process: 원본 데이터에 대해 일정 비율의 노이즈를 입력하여 훼손하는 과정

- Backward process: t번 훼손된 데이터에 대하여 s번 훼손된 데이터로 복원하는 과정 (t > s)

- training objective function

# MDLM(Masked Diffusion Language Model)

## 텍스트 도메인의 특징 (뇌피셜)

1. text: 매우 고밀도의 정보가 보존된 도메인. 이미지와 다르게 정보량이 거의 없는 변수가 적음

1. discrete: 단어는 존재하거나, 존재하지 않는 binary한 변수임

## 수식 전개 Discrete Diffusion

\textit{V} =  [사과, 존맛탱, mask]

입력문장: 사과 존맛탱

### forward process: 노이즈를 주입, actual token → mask

q\left(\mathbf{z}_t \mid \mathbf{x}\right)=\operatorname{Cat}\left(\mathbf{z}_t ; \alpha_t \mathbf{x}+\left(1-\alpha_t\right) \boldsymbol{\pi}\right)

- Terms

- 설명

⇒ 매 시점마다 점차 많은 토큰들이 mask 토큰으로 전환됨

### reverse posterior: 노이즈를 복원, mask → actual token

reverse posterior

q\left(\mathbf{z}_s \mid \mathbf{z}_t, \mathbf{x}\right)=\operatorname{Cat}\left(\mathbf{z}_s ;\frac{\left[\alpha_{t \mid s} \mathbf{z}_t+\left(1-\alpha_{t \mid s}\right) \mathbf{1} \boldsymbol{\pi}^{\top} \mathbf{z}_t\right] \odot\left[\alpha_s \mathbf{x}+\left(1-\alpha_s\right) \boldsymbol{\pi}\right]}{\alpha_t \mathbf{z}_t^{\top} \mathbf{x}+\left(1-\alpha_t\right) \mathbf{z}_t^{\top} \boldsymbol{\pi}}\right)

- t step에서 이전 시점 s(<t)까지 노이즈를 복원하기 위한 추정 확률 

## Masked Diffusion

### forward masking process

q\left(\mathbf{z}_t \mid \mathbf{x}\right)=\operatorname{Cat}\left(\mathbf{z}_t ; \alpha_t \mathbf{x}+\left(1-\alpha_t\right) \boldsymbol{m}\right)

- discrete diffusion에서 \pi가 m으로 변한 것 외에 차이 없습니다. 

### reverse posterior: 실제 loss 식을 산출하기 위해 필요한 항

q\left(\mathbf{z}_s \mid \mathbf{z}_t, \mathbf{x}\right)= \begin{cases}\operatorname{Cat}\left(\mathbf{z}_s ; \mathbf{z}_t\right) & \mathbf{z}_t \neq \mathbf{m} \\ \operatorname{Cat}\left(\mathbf{z}_s ; \frac{\left(1-\alpha_s\right) \mathbf{m}+\left(\alpha_s-\alpha_t\right) \mathbf{x}}{1-\alpha_t}\right) & \mathbf{z}_t=\mathbf{m}\end{cases}

- \textbf{z}_t \neq \textbf{m}: step t에서 원본토큰이라면 → 그대로 유지

- \textbf{z} = \textbf{m}: step t에서 masking token이라면 → step s에서 t 사이에서 masking되었을 확률 산출

### MDLM의 상황에 맞춘 2가지 property

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/4a949d85-7216-447e-845e-2f8c8b60316a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUSPEJOG%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF%2FcMu%2BjxdEEKxK7thbanYSR%2F5nuRQ9LFZ%2BAsD5%2B0z8WAiB3b4PgVmORLdXLnDJSN7WQYQQ1cyARxD%2B%2BtULSe048kSqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMloMHX8dKTW8Mti5rKtwDKxyeFUSDGIMQxZ4UktgQLecXeqB6deZoNkGE3Gc43k3iFl7Xzqm8O19XPGlxzHGKxxukKURmk20rbgdku59wlWXaXOL3Abe0MoHJPJg7omTUgiPlxtNmF8ROwImyTS9V08gkBIrWLJp2YsbottTo%2ByxwI%2FHkL%2BUSjXFbw2Ptr%2BuDfAZXVXAfr2NDOsd6Fb9QaIb7bdUqqVTG%2BAyWmYWRfD95ZaWLe93KgSWegJacFI0b0nvL3rKl9zEY1fDDH3WyqYBo9X6770gaUtyzUuQZC0iARewvlMmWUSS3PMOZmE%2FJMG9yWtFhmrYWM9KKoN8giqHXI8uo6cbDRQ9oHj%2B%2Fd9i0RjMJBGFr%2FkY0vqqYqApyzU8ItKqzFheYmgFNHnDiKIHC8mfj7asezq%2F1cA%2FwQLy7YxcgSTy3OS%2BH8CNVXa%2FeUBs4q9C%2B7VMB0dSP6SdbufsEbAXLXqPhfkkH4DrUxW1NWMxmFBYxo46tu6fT7tdL5Y2ukwvqgFzyfhROLNhqVI0SijJCIB%2FGMg4Ii7tI9eA4fd0JjC1fxSVFKHDvgPqZxM0%2Fffd2Jq9eACCT9wyzxQyD3CZicxsBKyXnKVnHmPcMkGygg71GKalX5SLLgFdzhHT1Hb63AS6Ba%2B4wv9PhxAY6pgFzS6knBXGQUbq6geceDNB3nMamkMCGREbts5SqP8OMzOiC7ewq5Qs82fMOQilIdk52Tw7wLoqJdmAui7WXfhypj6zm6AcJscIveyahZoXzdeNEs95iqtxLMB9f%2BVOJ4Xsk2u7YrCgFesrYe5Ed1aETfjHgHqbJYFfjL4RCO0IWzrzueygDRa7BXh3B%2Bp3%2Fe7V997P4qaLV8cW2TbZ0c1h%2Foga%2B9ZXW&X-Amz-Signature=b1eeddc287fd755ef4e024bec27ae65cb87c39dd9cea26d67c195955ef20bc58&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

1. Zero Masking Probabilities: <\textbf{x}, \textbf{m}>=0임. 즉, 원본 토큰 중에는 masking token이 사용되지 않음

1. Carry-Over Unmasking: step t에서 복원(unmasking)된 토큰은 이후 모델의 복원 과정에서 수정되지 않음

### Rao-Balckwellized Likelihood Bounds

diffusion loss를 산출하듯이 본래 학습할 discrete-time diffusion의 loss의 lower bound를 산출하면 아래와 같음

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/e3eaf5eb-6db5-477d-b805-db48e101bff0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUSPEJOG%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF%2FcMu%2BjxdEEKxK7thbanYSR%2F5nuRQ9LFZ%2BAsD5%2B0z8WAiB3b4PgVmORLdXLnDJSN7WQYQQ1cyARxD%2B%2BtULSe048kSqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMloMHX8dKTW8Mti5rKtwDKxyeFUSDGIMQxZ4UktgQLecXeqB6deZoNkGE3Gc43k3iFl7Xzqm8O19XPGlxzHGKxxukKURmk20rbgdku59wlWXaXOL3Abe0MoHJPJg7omTUgiPlxtNmF8ROwImyTS9V08gkBIrWLJp2YsbottTo%2ByxwI%2FHkL%2BUSjXFbw2Ptr%2BuDfAZXVXAfr2NDOsd6Fb9QaIb7bdUqqVTG%2BAyWmYWRfD95ZaWLe93KgSWegJacFI0b0nvL3rKl9zEY1fDDH3WyqYBo9X6770gaUtyzUuQZC0iARewvlMmWUSS3PMOZmE%2FJMG9yWtFhmrYWM9KKoN8giqHXI8uo6cbDRQ9oHj%2B%2Fd9i0RjMJBGFr%2FkY0vqqYqApyzU8ItKqzFheYmgFNHnDiKIHC8mfj7asezq%2F1cA%2FwQLy7YxcgSTy3OS%2BH8CNVXa%2FeUBs4q9C%2B7VMB0dSP6SdbufsEbAXLXqPhfkkH4DrUxW1NWMxmFBYxo46tu6fT7tdL5Y2ukwvqgFzyfhROLNhqVI0SijJCIB%2FGMg4Ii7tI9eA4fd0JjC1fxSVFKHDvgPqZxM0%2Fffd2Jq9eACCT9wyzxQyD3CZicxsBKyXnKVnHmPcMkGygg71GKalX5SLLgFdzhHT1Hb63AS6Ba%2B4wv9PhxAY6pgFzS6knBXGQUbq6geceDNB3nMamkMCGREbts5SqP8OMzOiC7ewq5Qs82fMOQilIdk52Tw7wLoqJdmAui7WXfhypj6zm6AcJscIveyahZoXzdeNEs95iqtxLMB9f%2BVOJ4Xsk2u7YrCgFesrYe5Ed1aETfjHgHqbJYFfjL4RCO0IWzrzueygDRa7BXh3B%2Bp3%2Fe7V997P4qaLV8cW2TbZ0c1h%2Foga%2B9ZXW&X-Amz-Signature=52e077d947e8e23b5008c5eadccfc4461359e5f5d152be9d105990899a5579b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Continuous-Time Likelihood Bounds

기존 연구에서 정리하기로 T \to \infin로 정의할 경우 더욱 tight한 lower bound를 산출할 수 있음

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/047cc652-b041-4100-b946-d255f67fcf9f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUSPEJOG%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF%2FcMu%2BjxdEEKxK7thbanYSR%2F5nuRQ9LFZ%2BAsD5%2B0z8WAiB3b4PgVmORLdXLnDJSN7WQYQQ1cyARxD%2B%2BtULSe048kSqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMloMHX8dKTW8Mti5rKtwDKxyeFUSDGIMQxZ4UktgQLecXeqB6deZoNkGE3Gc43k3iFl7Xzqm8O19XPGlxzHGKxxukKURmk20rbgdku59wlWXaXOL3Abe0MoHJPJg7omTUgiPlxtNmF8ROwImyTS9V08gkBIrWLJp2YsbottTo%2ByxwI%2FHkL%2BUSjXFbw2Ptr%2BuDfAZXVXAfr2NDOsd6Fb9QaIb7bdUqqVTG%2BAyWmYWRfD95ZaWLe93KgSWegJacFI0b0nvL3rKl9zEY1fDDH3WyqYBo9X6770gaUtyzUuQZC0iARewvlMmWUSS3PMOZmE%2FJMG9yWtFhmrYWM9KKoN8giqHXI8uo6cbDRQ9oHj%2B%2Fd9i0RjMJBGFr%2FkY0vqqYqApyzU8ItKqzFheYmgFNHnDiKIHC8mfj7asezq%2F1cA%2FwQLy7YxcgSTy3OS%2BH8CNVXa%2FeUBs4q9C%2B7VMB0dSP6SdbufsEbAXLXqPhfkkH4DrUxW1NWMxmFBYxo46tu6fT7tdL5Y2ukwvqgFzyfhROLNhqVI0SijJCIB%2FGMg4Ii7tI9eA4fd0JjC1fxSVFKHDvgPqZxM0%2Fffd2Jq9eACCT9wyzxQyD3CZicxsBKyXnKVnHmPcMkGygg71GKalX5SLLgFdzhHT1Hb63AS6Ba%2B4wv9PhxAY6pgFzS6knBXGQUbq6geceDNB3nMamkMCGREbts5SqP8OMzOiC7ewq5Qs82fMOQilIdk52Tw7wLoqJdmAui7WXfhypj6zm6AcJscIveyahZoXzdeNEs95iqtxLMB9f%2BVOJ4Xsk2u7YrCgFesrYe5Ed1aETfjHgHqbJYFfjL4RCO0IWzrzueygDRa7BXh3B%2Bp3%2Fe7V997P4qaLV8cW2TbZ0c1h%2Foga%2B9ZXW&X-Amz-Signature=69cdd2842e98668ede9394c41e36d0f0eee678cf5b5b5beec471e93e04880353&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Masked Diffusion Language Models

앞에서 정의된 tight한 lower bound를 language modeling 상황으로 가져오기 위해 아래 가정들을 적용할 수 있음

1. \textbf{x}^{1:L}: L개의 token sequence

1. \textbf{x}^\textit{l}: \textit{l}번째 토큰

1. forward와 backward 모두 각 토큰들이 독립적으로 진행

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/86b0ed88-f0e4-47b2-94af-5fcf1d863627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUSPEJOG%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF%2FcMu%2BjxdEEKxK7thbanYSR%2F5nuRQ9LFZ%2BAsD5%2B0z8WAiB3b4PgVmORLdXLnDJSN7WQYQQ1cyARxD%2B%2BtULSe048kSqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMloMHX8dKTW8Mti5rKtwDKxyeFUSDGIMQxZ4UktgQLecXeqB6deZoNkGE3Gc43k3iFl7Xzqm8O19XPGlxzHGKxxukKURmk20rbgdku59wlWXaXOL3Abe0MoHJPJg7omTUgiPlxtNmF8ROwImyTS9V08gkBIrWLJp2YsbottTo%2ByxwI%2FHkL%2BUSjXFbw2Ptr%2BuDfAZXVXAfr2NDOsd6Fb9QaIb7bdUqqVTG%2BAyWmYWRfD95ZaWLe93KgSWegJacFI0b0nvL3rKl9zEY1fDDH3WyqYBo9X6770gaUtyzUuQZC0iARewvlMmWUSS3PMOZmE%2FJMG9yWtFhmrYWM9KKoN8giqHXI8uo6cbDRQ9oHj%2B%2Fd9i0RjMJBGFr%2FkY0vqqYqApyzU8ItKqzFheYmgFNHnDiKIHC8mfj7asezq%2F1cA%2FwQLy7YxcgSTy3OS%2BH8CNVXa%2FeUBs4q9C%2B7VMB0dSP6SdbufsEbAXLXqPhfkkH4DrUxW1NWMxmFBYxo46tu6fT7tdL5Y2ukwvqgFzyfhROLNhqVI0SijJCIB%2FGMg4Ii7tI9eA4fd0JjC1fxSVFKHDvgPqZxM0%2Fffd2Jq9eACCT9wyzxQyD3CZicxsBKyXnKVnHmPcMkGygg71GKalX5SLLgFdzhHT1Hb63AS6Ba%2B4wv9PhxAY6pgFzS6knBXGQUbq6geceDNB3nMamkMCGREbts5SqP8OMzOiC7ewq5Qs82fMOQilIdk52Tw7wLoqJdmAui7WXfhypj6zm6AcJscIveyahZoXzdeNEs95iqtxLMB9f%2BVOJ4Xsk2u7YrCgFesrYe5Ed1aETfjHgHqbJYFfjL4RCO0IWzrzueygDRa7BXh3B%2Bp3%2Fe7V997P4qaLV8cW2TbZ0c1h%2Foga%2B9ZXW&X-Amz-Signature=e0deeab75f3fbffaa66f5435db581573c3c53d36d607e9155fddecff1f83e787&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/21f1eebf-a486-4a9b-a8c6-5ef25daa6960/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUSPEJOG%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF%2FcMu%2BjxdEEKxK7thbanYSR%2F5nuRQ9LFZ%2BAsD5%2B0z8WAiB3b4PgVmORLdXLnDJSN7WQYQQ1cyARxD%2B%2BtULSe048kSqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMloMHX8dKTW8Mti5rKtwDKxyeFUSDGIMQxZ4UktgQLecXeqB6deZoNkGE3Gc43k3iFl7Xzqm8O19XPGlxzHGKxxukKURmk20rbgdku59wlWXaXOL3Abe0MoHJPJg7omTUgiPlxtNmF8ROwImyTS9V08gkBIrWLJp2YsbottTo%2ByxwI%2FHkL%2BUSjXFbw2Ptr%2BuDfAZXVXAfr2NDOsd6Fb9QaIb7bdUqqVTG%2BAyWmYWRfD95ZaWLe93KgSWegJacFI0b0nvL3rKl9zEY1fDDH3WyqYBo9X6770gaUtyzUuQZC0iARewvlMmWUSS3PMOZmE%2FJMG9yWtFhmrYWM9KKoN8giqHXI8uo6cbDRQ9oHj%2B%2Fd9i0RjMJBGFr%2FkY0vqqYqApyzU8ItKqzFheYmgFNHnDiKIHC8mfj7asezq%2F1cA%2FwQLy7YxcgSTy3OS%2BH8CNVXa%2FeUBs4q9C%2B7VMB0dSP6SdbufsEbAXLXqPhfkkH4DrUxW1NWMxmFBYxo46tu6fT7tdL5Y2ukwvqgFzyfhROLNhqVI0SijJCIB%2FGMg4Ii7tI9eA4fd0JjC1fxSVFKHDvgPqZxM0%2Fffd2Jq9eACCT9wyzxQyD3CZicxsBKyXnKVnHmPcMkGygg71GKalX5SLLgFdzhHT1Hb63AS6Ba%2B4wv9PhxAY6pgFzS6knBXGQUbq6geceDNB3nMamkMCGREbts5SqP8OMzOiC7ewq5Qs82fMOQilIdk52Tw7wLoqJdmAui7WXfhypj6zm6AcJscIveyahZoXzdeNEs95iqtxLMB9f%2BVOJ4Xsk2u7YrCgFesrYe5Ed1aETfjHgHqbJYFfjL4RCO0IWzrzueygDRa7BXh3B%2Bp3%2Fe7V997P4qaLV8cW2TbZ0c1h%2Foga%2B9ZXW&X-Amz-Signature=631bf7067f7c36e431289fb9ea82aca9e8657e5e6303d22c7521b54728893f8d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- \textbf{x}^\textit{l}_\theta(\textbf{z}_t^{1:L}, t): t번째 step에서의 시퀀스에 대한 모델의 예측 문장, masking된 토큰을 예측하여 복원한 문장문

- \log<\textbf{x}^\textit{l}_\theta(\textbf{z}_t^{1:L}, t), \textbf{x}^\textit{l}>: loglikelihood, 갑자기요…?!

- 이때 \alpha_s 가 사라진 것을 확인할 수 있음

### Training Algorithm

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/2900feab-6cf6-486d-83b8-26816f816a5e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUSPEJOG%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF%2FcMu%2BjxdEEKxK7thbanYSR%2F5nuRQ9LFZ%2BAsD5%2B0z8WAiB3b4PgVmORLdXLnDJSN7WQYQQ1cyARxD%2B%2BtULSe048kSqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMloMHX8dKTW8Mti5rKtwDKxyeFUSDGIMQxZ4UktgQLecXeqB6deZoNkGE3Gc43k3iFl7Xzqm8O19XPGlxzHGKxxukKURmk20rbgdku59wlWXaXOL3Abe0MoHJPJg7omTUgiPlxtNmF8ROwImyTS9V08gkBIrWLJp2YsbottTo%2ByxwI%2FHkL%2BUSjXFbw2Ptr%2BuDfAZXVXAfr2NDOsd6Fb9QaIb7bdUqqVTG%2BAyWmYWRfD95ZaWLe93KgSWegJacFI0b0nvL3rKl9zEY1fDDH3WyqYBo9X6770gaUtyzUuQZC0iARewvlMmWUSS3PMOZmE%2FJMG9yWtFhmrYWM9KKoN8giqHXI8uo6cbDRQ9oHj%2B%2Fd9i0RjMJBGFr%2FkY0vqqYqApyzU8ItKqzFheYmgFNHnDiKIHC8mfj7asezq%2F1cA%2FwQLy7YxcgSTy3OS%2BH8CNVXa%2FeUBs4q9C%2B7VMB0dSP6SdbufsEbAXLXqPhfkkH4DrUxW1NWMxmFBYxo46tu6fT7tdL5Y2ukwvqgFzyfhROLNhqVI0SijJCIB%2FGMg4Ii7tI9eA4fd0JjC1fxSVFKHDvgPqZxM0%2Fffd2Jq9eACCT9wyzxQyD3CZicxsBKyXnKVnHmPcMkGygg71GKalX5SLLgFdzhHT1Hb63AS6Ba%2B4wv9PhxAY6pgFzS6knBXGQUbq6geceDNB3nMamkMCGREbts5SqP8OMzOiC7ewq5Qs82fMOQilIdk52Tw7wLoqJdmAui7WXfhypj6zm6AcJscIveyahZoXzdeNEs95iqtxLMB9f%2BVOJ4Xsk2u7YrCgFesrYe5Ed1aETfjHgHqbJYFfjL4RCO0IWzrzueygDRa7BXh3B%2Bp3%2Fe7V997P4qaLV8cW2TbZ0c1h%2Foga%2B9ZXW&X-Amz-Signature=7033d83fdc36491f8b7c4aef5a1ed8d34c05bdc1fbbf90083d632fd5d48ba30a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

1. 데이터 sampling

1. step sampling

1. 이전 step 대비 추가적으로 \alpha_t 비율을 masking한  masked input 산출

1. weighted sum of MLM loss 형식으로 update

## Actual Inference

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/d2e666a0-4261-49de-857b-871b0c42a118/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUSPEJOG%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF%2FcMu%2BjxdEEKxK7thbanYSR%2F5nuRQ9LFZ%2BAsD5%2B0z8WAiB3b4PgVmORLdXLnDJSN7WQYQQ1cyARxD%2B%2BtULSe048kSqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMloMHX8dKTW8Mti5rKtwDKxyeFUSDGIMQxZ4UktgQLecXeqB6deZoNkGE3Gc43k3iFl7Xzqm8O19XPGlxzHGKxxukKURmk20rbgdku59wlWXaXOL3Abe0MoHJPJg7omTUgiPlxtNmF8ROwImyTS9V08gkBIrWLJp2YsbottTo%2ByxwI%2FHkL%2BUSjXFbw2Ptr%2BuDfAZXVXAfr2NDOsd6Fb9QaIb7bdUqqVTG%2BAyWmYWRfD95ZaWLe93KgSWegJacFI0b0nvL3rKl9zEY1fDDH3WyqYBo9X6770gaUtyzUuQZC0iARewvlMmWUSS3PMOZmE%2FJMG9yWtFhmrYWM9KKoN8giqHXI8uo6cbDRQ9oHj%2B%2Fd9i0RjMJBGFr%2FkY0vqqYqApyzU8ItKqzFheYmgFNHnDiKIHC8mfj7asezq%2F1cA%2FwQLy7YxcgSTy3OS%2BH8CNVXa%2FeUBs4q9C%2B7VMB0dSP6SdbufsEbAXLXqPhfkkH4DrUxW1NWMxmFBYxo46tu6fT7tdL5Y2ukwvqgFzyfhROLNhqVI0SijJCIB%2FGMg4Ii7tI9eA4fd0JjC1fxSVFKHDvgPqZxM0%2Fffd2Jq9eACCT9wyzxQyD3CZicxsBKyXnKVnHmPcMkGygg71GKalX5SLLgFdzhHT1Hb63AS6Ba%2B4wv9PhxAY6pgFzS6knBXGQUbq6geceDNB3nMamkMCGREbts5SqP8OMzOiC7ewq5Qs82fMOQilIdk52Tw7wLoqJdmAui7WXfhypj6zm6AcJscIveyahZoXzdeNEs95iqtxLMB9f%2BVOJ4Xsk2u7YrCgFesrYe5Ed1aETfjHgHqbJYFfjL4RCO0IWzrzueygDRa7BXh3B%2Bp3%2Fe7V997P4qaLV8cW2TbZ0c1h%2Foga%2B9ZXW&X-Amz-Signature=315c6a3dcd8538b9f31dc1e101b44d271b2ba71372195fa778f64495e5eca0d5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

해당 수식을 통해 실제 생성이 이루어지게 됨

1. \textbf{z}_t = \textbf{m}: t step에서 mask 토큰으로 입력된 위치에 대해서만 예측 수행

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/444ac4d9-3787-4636-ad4b-914abf9b6cbf/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUSPEJOG%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF%2FcMu%2BjxdEEKxK7thbanYSR%2F5nuRQ9LFZ%2BAsD5%2B0z8WAiB3b4PgVmORLdXLnDJSN7WQYQQ1cyARxD%2B%2BtULSe048kSqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMloMHX8dKTW8Mti5rKtwDKxyeFUSDGIMQxZ4UktgQLecXeqB6deZoNkGE3Gc43k3iFl7Xzqm8O19XPGlxzHGKxxukKURmk20rbgdku59wlWXaXOL3Abe0MoHJPJg7omTUgiPlxtNmF8ROwImyTS9V08gkBIrWLJp2YsbottTo%2ByxwI%2FHkL%2BUSjXFbw2Ptr%2BuDfAZXVXAfr2NDOsd6Fb9QaIb7bdUqqVTG%2BAyWmYWRfD95ZaWLe93KgSWegJacFI0b0nvL3rKl9zEY1fDDH3WyqYBo9X6770gaUtyzUuQZC0iARewvlMmWUSS3PMOZmE%2FJMG9yWtFhmrYWM9KKoN8giqHXI8uo6cbDRQ9oHj%2B%2Fd9i0RjMJBGFr%2FkY0vqqYqApyzU8ItKqzFheYmgFNHnDiKIHC8mfj7asezq%2F1cA%2FwQLy7YxcgSTy3OS%2BH8CNVXa%2FeUBs4q9C%2B7VMB0dSP6SdbufsEbAXLXqPhfkkH4DrUxW1NWMxmFBYxo46tu6fT7tdL5Y2ukwvqgFzyfhROLNhqVI0SijJCIB%2FGMg4Ii7tI9eA4fd0JjC1fxSVFKHDvgPqZxM0%2Fffd2Jq9eACCT9wyzxQyD3CZicxsBKyXnKVnHmPcMkGygg71GKalX5SLLgFdzhHT1Hb63AS6Ba%2B4wv9PhxAY6pgFzS6knBXGQUbq6geceDNB3nMamkMCGREbts5SqP8OMzOiC7ewq5Qs82fMOQilIdk52Tw7wLoqJdmAui7WXfhypj6zm6AcJscIveyahZoXzdeNEs95iqtxLMB9f%2BVOJ4Xsk2u7YrCgFesrYe5Ed1aETfjHgHqbJYFfjL4RCO0IWzrzueygDRa7BXh3B%2Bp3%2Fe7V997P4qaLV8cW2TbZ0c1h%2Foga%2B9ZXW&X-Amz-Signature=54291ebd4187c8be849d7ef4463b261ba15f619fe3eef671afad9b629f3f86ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

1. \frac{(1-\alpha_s)\textbf{m} + (\alpha_s - \alpha_t)\textbf{x}_\theta(\textbf{z}_t, t)}{1-\alpha_t} = \frac{1-\alpha_s}{1-\alpha_t}\textbf{m} + \frac{\alpha_s-\alpha_t}{1-\alpha_t}\textbf{x}_\theta(\textbf{z}_t, t): 모든 mask 토큰 위치에서 예측된 확률분포 중에서 \frac{1-\alpha_s}{1-\alpha_t} 비율은 다시 masking으로 돌림

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/f46d1e04-1de1-49d7-b53a-e7f95a2aba5e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUSPEJOG%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF%2FcMu%2BjxdEEKxK7thbanYSR%2F5nuRQ9LFZ%2BAsD5%2B0z8WAiB3b4PgVmORLdXLnDJSN7WQYQQ1cyARxD%2B%2BtULSe048kSqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMloMHX8dKTW8Mti5rKtwDKxyeFUSDGIMQxZ4UktgQLecXeqB6deZoNkGE3Gc43k3iFl7Xzqm8O19XPGlxzHGKxxukKURmk20rbgdku59wlWXaXOL3Abe0MoHJPJg7omTUgiPlxtNmF8ROwImyTS9V08gkBIrWLJp2YsbottTo%2ByxwI%2FHkL%2BUSjXFbw2Ptr%2BuDfAZXVXAfr2NDOsd6Fb9QaIb7bdUqqVTG%2BAyWmYWRfD95ZaWLe93KgSWegJacFI0b0nvL3rKl9zEY1fDDH3WyqYBo9X6770gaUtyzUuQZC0iARewvlMmWUSS3PMOZmE%2FJMG9yWtFhmrYWM9KKoN8giqHXI8uo6cbDRQ9oHj%2B%2Fd9i0RjMJBGFr%2FkY0vqqYqApyzU8ItKqzFheYmgFNHnDiKIHC8mfj7asezq%2F1cA%2FwQLy7YxcgSTy3OS%2BH8CNVXa%2FeUBs4q9C%2B7VMB0dSP6SdbufsEbAXLXqPhfkkH4DrUxW1NWMxmFBYxo46tu6fT7tdL5Y2ukwvqgFzyfhROLNhqVI0SijJCIB%2FGMg4Ii7tI9eA4fd0JjC1fxSVFKHDvgPqZxM0%2Fffd2Jq9eACCT9wyzxQyD3CZicxsBKyXnKVnHmPcMkGygg71GKalX5SLLgFdzhHT1Hb63AS6Ba%2B4wv9PhxAY6pgFzS6knBXGQUbq6geceDNB3nMamkMCGREbts5SqP8OMzOiC7ewq5Qs82fMOQilIdk52Tw7wLoqJdmAui7WXfhypj6zm6AcJscIveyahZoXzdeNEs95iqtxLMB9f%2BVOJ4Xsk2u7YrCgFesrYe5Ed1aETfjHgHqbJYFfjL4RCO0IWzrzueygDRa7BXh3B%2Bp3%2Fe7V997P4qaLV8cW2TbZ0c1h%2Foga%2B9ZXW&X-Amz-Signature=69e6da427de62c26c96a1f3fcdbca20c0424c4ebe7eb716704ce943bc300213c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

⇒ 매 iteration 마다 \frac{\alpha_s - \alpha_t}{1-\alpha_t}만큼의 토큰이 복원되면서 생성

# Experiments

### 1. Perplexity evaluation

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/51d026ce-8e3f-4fd1-99d4-1e9edb825916/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUSPEJOG%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF%2FcMu%2BjxdEEKxK7thbanYSR%2F5nuRQ9LFZ%2BAsD5%2B0z8WAiB3b4PgVmORLdXLnDJSN7WQYQQ1cyARxD%2B%2BtULSe048kSqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMloMHX8dKTW8Mti5rKtwDKxyeFUSDGIMQxZ4UktgQLecXeqB6deZoNkGE3Gc43k3iFl7Xzqm8O19XPGlxzHGKxxukKURmk20rbgdku59wlWXaXOL3Abe0MoHJPJg7omTUgiPlxtNmF8ROwImyTS9V08gkBIrWLJp2YsbottTo%2ByxwI%2FHkL%2BUSjXFbw2Ptr%2BuDfAZXVXAfr2NDOsd6Fb9QaIb7bdUqqVTG%2BAyWmYWRfD95ZaWLe93KgSWegJacFI0b0nvL3rKl9zEY1fDDH3WyqYBo9X6770gaUtyzUuQZC0iARewvlMmWUSS3PMOZmE%2FJMG9yWtFhmrYWM9KKoN8giqHXI8uo6cbDRQ9oHj%2B%2Fd9i0RjMJBGFr%2FkY0vqqYqApyzU8ItKqzFheYmgFNHnDiKIHC8mfj7asezq%2F1cA%2FwQLy7YxcgSTy3OS%2BH8CNVXa%2FeUBs4q9C%2B7VMB0dSP6SdbufsEbAXLXqPhfkkH4DrUxW1NWMxmFBYxo46tu6fT7tdL5Y2ukwvqgFzyfhROLNhqVI0SijJCIB%2FGMg4Ii7tI9eA4fd0JjC1fxSVFKHDvgPqZxM0%2Fffd2Jq9eACCT9wyzxQyD3CZicxsBKyXnKVnHmPcMkGygg71GKalX5SLLgFdzhHT1Hb63AS6Ba%2B4wv9PhxAY6pgFzS6knBXGQUbq6geceDNB3nMamkMCGREbts5SqP8OMzOiC7ewq5Qs82fMOQilIdk52Tw7wLoqJdmAui7WXfhypj6zm6AcJscIveyahZoXzdeNEs95iqtxLMB9f%2BVOJ4Xsk2u7YrCgFesrYe5Ed1aETfjHgHqbJYFfjL4RCO0IWzrzueygDRa7BXh3B%2Bp3%2Fe7V997P4qaLV8cW2TbZ0c1h%2Foga%2B9ZXW&X-Amz-Signature=16baaf8af54c2ad8c9e4d527d9f5385176417c08fd8acbc48a6c80bfc84fa25d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 동일한 corpus를 이용하여 autoregressive model과 MDLM을 학습시켜 비교

### 2. Training NLL

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/2c10fdcc-8f02-458e-9b35-8ae60ad63344/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUSPEJOG%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF%2FcMu%2BjxdEEKxK7thbanYSR%2F5nuRQ9LFZ%2BAsD5%2B0z8WAiB3b4PgVmORLdXLnDJSN7WQYQQ1cyARxD%2B%2BtULSe048kSqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMloMHX8dKTW8Mti5rKtwDKxyeFUSDGIMQxZ4UktgQLecXeqB6deZoNkGE3Gc43k3iFl7Xzqm8O19XPGlxzHGKxxukKURmk20rbgdku59wlWXaXOL3Abe0MoHJPJg7omTUgiPlxtNmF8ROwImyTS9V08gkBIrWLJp2YsbottTo%2ByxwI%2FHkL%2BUSjXFbw2Ptr%2BuDfAZXVXAfr2NDOsd6Fb9QaIb7bdUqqVTG%2BAyWmYWRfD95ZaWLe93KgSWegJacFI0b0nvL3rKl9zEY1fDDH3WyqYBo9X6770gaUtyzUuQZC0iARewvlMmWUSS3PMOZmE%2FJMG9yWtFhmrYWM9KKoN8giqHXI8uo6cbDRQ9oHj%2B%2Fd9i0RjMJBGFr%2FkY0vqqYqApyzU8ItKqzFheYmgFNHnDiKIHC8mfj7asezq%2F1cA%2FwQLy7YxcgSTy3OS%2BH8CNVXa%2FeUBs4q9C%2B7VMB0dSP6SdbufsEbAXLXqPhfkkH4DrUxW1NWMxmFBYxo46tu6fT7tdL5Y2ukwvqgFzyfhROLNhqVI0SijJCIB%2FGMg4Ii7tI9eA4fd0JjC1fxSVFKHDvgPqZxM0%2Fffd2Jq9eACCT9wyzxQyD3CZicxsBKyXnKVnHmPcMkGygg71GKalX5SLLgFdzhHT1Hb63AS6Ba%2B4wv9PhxAY6pgFzS6knBXGQUbq6geceDNB3nMamkMCGREbts5SqP8OMzOiC7ewq5Qs82fMOQilIdk52Tw7wLoqJdmAui7WXfhypj6zm6AcJscIveyahZoXzdeNEs95iqtxLMB9f%2BVOJ4Xsk2u7YrCgFesrYe5Ed1aETfjHgHqbJYFfjL4RCO0IWzrzueygDRa7BXh3B%2Bp3%2Fe7V997P4qaLV8cW2TbZ0c1h%2Foga%2B9ZXW&X-Amz-Signature=aeaccdee7b14302c8e7aa2c8b0b1ca1c0270bcf736595cecc887a0d7ee7f78f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 기존 DDLM(SEDD)보다 훨씬 안정적인 NLL을 보이며 학습

### 3. Zero-shot Perplexity

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/99480a95-157d-453b-9ddf-ba5927cb7298/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUSPEJOG%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF%2FcMu%2BjxdEEKxK7thbanYSR%2F5nuRQ9LFZ%2BAsD5%2B0z8WAiB3b4PgVmORLdXLnDJSN7WQYQQ1cyARxD%2B%2BtULSe048kSqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMloMHX8dKTW8Mti5rKtwDKxyeFUSDGIMQxZ4UktgQLecXeqB6deZoNkGE3Gc43k3iFl7Xzqm8O19XPGlxzHGKxxukKURmk20rbgdku59wlWXaXOL3Abe0MoHJPJg7omTUgiPlxtNmF8ROwImyTS9V08gkBIrWLJp2YsbottTo%2ByxwI%2FHkL%2BUSjXFbw2Ptr%2BuDfAZXVXAfr2NDOsd6Fb9QaIb7bdUqqVTG%2BAyWmYWRfD95ZaWLe93KgSWegJacFI0b0nvL3rKl9zEY1fDDH3WyqYBo9X6770gaUtyzUuQZC0iARewvlMmWUSS3PMOZmE%2FJMG9yWtFhmrYWM9KKoN8giqHXI8uo6cbDRQ9oHj%2B%2Fd9i0RjMJBGFr%2FkY0vqqYqApyzU8ItKqzFheYmgFNHnDiKIHC8mfj7asezq%2F1cA%2FwQLy7YxcgSTy3OS%2BH8CNVXa%2FeUBs4q9C%2B7VMB0dSP6SdbufsEbAXLXqPhfkkH4DrUxW1NWMxmFBYxo46tu6fT7tdL5Y2ukwvqgFzyfhROLNhqVI0SijJCIB%2FGMg4Ii7tI9eA4fd0JjC1fxSVFKHDvgPqZxM0%2Fffd2Jq9eACCT9wyzxQyD3CZicxsBKyXnKVnHmPcMkGygg71GKalX5SLLgFdzhHT1Hb63AS6Ba%2B4wv9PhxAY6pgFzS6knBXGQUbq6geceDNB3nMamkMCGREbts5SqP8OMzOiC7ewq5Qs82fMOQilIdk52Tw7wLoqJdmAui7WXfhypj6zm6AcJscIveyahZoXzdeNEs95iqtxLMB9f%2BVOJ4Xsk2u7YrCgFesrYe5Ed1aETfjHgHqbJYFfjL4RCO0IWzrzueygDRa7BXh3B%2Bp3%2Fe7V997P4qaLV8cW2TbZ0c1h%2Foga%2B9ZXW&X-Amz-Signature=fd7c5b31d14f5e2212e598cbd48a781b49c02aa8b1663862b8aacfe5b625dbd9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 다양한 분야에 대하여 AR과 근접한 수준의 성능 달성

### 4. Downstream Task

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/a06d904c-b3ef-4c4a-a841-868f41b432c9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUSPEJOG%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF%2FcMu%2BjxdEEKxK7thbanYSR%2F5nuRQ9LFZ%2BAsD5%2B0z8WAiB3b4PgVmORLdXLnDJSN7WQYQQ1cyARxD%2B%2BtULSe048kSqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMloMHX8dKTW8Mti5rKtwDKxyeFUSDGIMQxZ4UktgQLecXeqB6deZoNkGE3Gc43k3iFl7Xzqm8O19XPGlxzHGKxxukKURmk20rbgdku59wlWXaXOL3Abe0MoHJPJg7omTUgiPlxtNmF8ROwImyTS9V08gkBIrWLJp2YsbottTo%2ByxwI%2FHkL%2BUSjXFbw2Ptr%2BuDfAZXVXAfr2NDOsd6Fb9QaIb7bdUqqVTG%2BAyWmYWRfD95ZaWLe93KgSWegJacFI0b0nvL3rKl9zEY1fDDH3WyqYBo9X6770gaUtyzUuQZC0iARewvlMmWUSS3PMOZmE%2FJMG9yWtFhmrYWM9KKoN8giqHXI8uo6cbDRQ9oHj%2B%2Fd9i0RjMJBGFr%2FkY0vqqYqApyzU8ItKqzFheYmgFNHnDiKIHC8mfj7asezq%2F1cA%2FwQLy7YxcgSTy3OS%2BH8CNVXa%2FeUBs4q9C%2B7VMB0dSP6SdbufsEbAXLXqPhfkkH4DrUxW1NWMxmFBYxo46tu6fT7tdL5Y2ukwvqgFzyfhROLNhqVI0SijJCIB%2FGMg4Ii7tI9eA4fd0JjC1fxSVFKHDvgPqZxM0%2Fffd2Jq9eACCT9wyzxQyD3CZicxsBKyXnKVnHmPcMkGygg71GKalX5SLLgFdzhHT1Hb63AS6Ba%2B4wv9PhxAY6pgFzS6knBXGQUbq6geceDNB3nMamkMCGREbts5SqP8OMzOiC7ewq5Qs82fMOQilIdk52Tw7wLoqJdmAui7WXfhypj6zm6AcJscIveyahZoXzdeNEs95iqtxLMB9f%2BVOJ4Xsk2u7YrCgFesrYe5Ed1aETfjHgHqbJYFfjL4RCO0IWzrzueygDRa7BXh3B%2Bp3%2Fe7V997P4qaLV8cW2TbZ0c1h%2Foga%2B9ZXW&X-Amz-Signature=a188285524081a50179d19f5c398a7ea6032059200ea42ed82ed3041c0587b24&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- BERT를 MDLM으로 일부 finetune한 결과로 비교

# conclusion
