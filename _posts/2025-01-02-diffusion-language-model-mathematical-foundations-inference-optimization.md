---
categories:
- paper-reviews
date: '2025-01-02 00:00:00'
description: 논문 리뷰 - DiffusionLM, Pre-training 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- bert
- diffusion
- diffusionlm
- language-model
- paper-review
- pre-training
thumbnail: assets/img/posts/2025-01-02-diffusion-language-model-mathematical-foundations-inference-optimization/thumbnail.jpg
title: Diffusion Language Model-Mathematical foundations & inference optimization
---

**논문 정보**
- **Date**: 2025-01-02
- **Reviewer**: 김재희
- **Property**: DiffusionLM, Pre-training

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-02-diffusion-language-model-mathematical-foundations-inference-optimization/image_000.png" class="img-fluid rounded z-depth-1" %}

# Preliminary

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-02-diffusion-language-model-mathematical-foundations-inference-optimization/image_001.png" class="img-fluid rounded z-depth-1" %}

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

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-02-diffusion-language-model-mathematical-foundations-inference-optimization/image_002.png" class="img-fluid rounded z-depth-1" %}

1. Zero Masking Probabilities: <\textbf{x}, \textbf{m}>=0임. 즉, 원본 토큰 중에는 masking token이 사용되지 않음

1. Carry-Over Unmasking: step t에서 복원(unmasking)된 토큰은 이후 모델의 복원 과정에서 수정되지 않음

### Rao-Balckwellized Likelihood Bounds

diffusion loss를 산출하듯이 본래 학습할 discrete-time diffusion의 loss의 lower bound를 산출하면 아래와 같음

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-02-diffusion-language-model-mathematical-foundations-inference-optimization/image_003.png" class="img-fluid rounded z-depth-1" %}

### Continuous-Time Likelihood Bounds

기존 연구에서 정리하기로 T \to \infin로 정의할 경우 더욱 tight한 lower bound를 산출할 수 있음

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-02-diffusion-language-model-mathematical-foundations-inference-optimization/image_004.png" class="img-fluid rounded z-depth-1" %}

### Masked Diffusion Language Models

앞에서 정의된 tight한 lower bound를 language modeling 상황으로 가져오기 위해 아래 가정들을 적용할 수 있음

1. \textbf{x}^{1:L}: L개의 token sequence

1. \textbf{x}^\textit{l}: \textit{l}번째 토큰

1. forward와 backward 모두 각 토큰들이 독립적으로 진행

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-02-diffusion-language-model-mathematical-foundations-inference-optimization/image_005.png" class="img-fluid rounded z-depth-1" %}

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-02-diffusion-language-model-mathematical-foundations-inference-optimization/image_006.png" class="img-fluid rounded z-depth-1" %}

- \textbf{x}^\textit{l}_\theta(\textbf{z}_t^{1:L}, t): t번째 step에서의 시퀀스에 대한 모델의 예측 문장, masking된 토큰을 예측하여 복원한 문장문

- \log<\textbf{x}^\textit{l}_\theta(\textbf{z}_t^{1:L}, t), \textbf{x}^\textit{l}>: loglikelihood, 갑자기요…?!

- 이때 \alpha_s 가 사라진 것을 확인할 수 있음

### Training Algorithm

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-02-diffusion-language-model-mathematical-foundations-inference-optimization/image_007.png" class="img-fluid rounded z-depth-1" %}

1. 데이터 sampling

1. step sampling

1. 이전 step 대비 추가적으로 \alpha_t 비율을 masking한  masked input 산출

1. weighted sum of MLM loss 형식으로 update

## Actual Inference

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-02-diffusion-language-model-mathematical-foundations-inference-optimization/image_008.png" class="img-fluid rounded z-depth-1" %}

해당 수식을 통해 실제 생성이 이루어지게 됨

1. \textbf{z}_t = \textbf{m}: t step에서 mask 토큰으로 입력된 위치에 대해서만 예측 수행

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-02-diffusion-language-model-mathematical-foundations-inference-optimization/image_009.png" class="img-fluid rounded z-depth-1" %}

1. \frac{(1-\alpha_s)\textbf{m} + (\alpha_s - \alpha_t)\textbf{x}_\theta(\textbf{z}_t, t)}{1-\alpha_t} = \frac{1-\alpha_s}{1-\alpha_t}\textbf{m} + \frac{\alpha_s-\alpha_t}{1-\alpha_t}\textbf{x}_\theta(\textbf{z}_t, t): 모든 mask 토큰 위치에서 예측된 확률분포 중에서 \frac{1-\alpha_s}{1-\alpha_t} 비율은 다시 masking으로 돌림

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-02-diffusion-language-model-mathematical-foundations-inference-optimization/image_010.png" class="img-fluid rounded z-depth-1" %}

⇒ 매 iteration 마다 \frac{\alpha_s - \alpha_t}{1-\alpha_t}만큼의 토큰이 복원되면서 생성

# Experiments

### 1. Perplexity evaluation

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-02-diffusion-language-model-mathematical-foundations-inference-optimization/image_011.png" class="img-fluid rounded z-depth-1" %}

- 동일한 corpus를 이용하여 autoregressive model과 MDLM을 학습시켜 비교

### 2. Training NLL

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-02-diffusion-language-model-mathematical-foundations-inference-optimization/image_012.png" class="img-fluid rounded z-depth-1" %}

- 기존 DDLM(SEDD)보다 훨씬 안정적인 NLL을 보이며 학습

### 3. Zero-shot Perplexity

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-02-diffusion-language-model-mathematical-foundations-inference-optimization/image_013.png" class="img-fluid rounded z-depth-1" %}

- 다양한 분야에 대하여 AR과 근접한 수준의 성능 달성

### 4. Downstream Task

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-02-diffusion-language-model-mathematical-foundations-inference-optimization/image_014.png" class="img-fluid rounded z-depth-1" %}

- BERT를 MDLM으로 일부 finetune한 결과로 비교

# conclusion
