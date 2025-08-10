---
categories: paper-reviews
date: '2025-08-05 00:00:00'
description: ' 논문 리뷰 - BLOCK DIFFUSION: INTERPOLATING BETWEEN AUTOREGRESSIVE AND DIFFUSION
  LANGUAGE MODELS'
giscus_comments: true
layout: post
related_posts: false
tags: llm paper-review nlp
title: 'BLOCK DIFFUSION: INTERPOLATING BETWEEN AUTOREGRESSIVE AND DIFFUSION LANGUAGE
  MODELS'
---

**논문 정보**
- **Date**: 2025-08-05
- **Reviewer**: 상엽
- **Property**: DiffusionLM, LLM

## Introduction

**Diffusion 모델이 가진 한계점**

1. 현재 대부분의 diffusion 모델의 경우 **고정된 길이의 답변**만을 생성.

1. Bidirectional context를 사용하기 때문에 **KV 캐시와 같이 AR 추론에서 효율적인 방법들을 사용할 수 없음**.

1. Standard metric (e.g. perplexity)에서 **여전히 낮은 성능**을 보임.

<span style='color:yellow_background'>→ </span><span style='color:yellow_background'>**Block Discrete Denoising Diffusion Language Models (BD3-LMs)**</span>

<br/>

<span style='color:yellow_background'>**BD3-LMs**</span>

Interpolation between discrete diffusion and autoregressive model

- Block diffusion model: semi-autoregressive model

- **Inter-Block**: Block을 생성하는 과정은 AR 과정으로 모델링

- **Intra-Block**: 이전 block이 주어질 경우, 현재 block 내부는 discrete diffusion 과정으로 모델링

<br/>

<span style='color:yellow_background'>**Block Diffusion 모델이 가진 Two challenges를 발견: 핵심!!**</span>

- Block diffusion을 학습하기 위해서 두 번의 forward pass가 필요함. → 계산량 증가

- 높은 gradient variance로 인한 성능 저하

→ 지금은 이해가 어려우니 뒤에서 확인

<br/>

**Contribution**

- Block discrete diffusion language model 제안. **기존 diffusion 모델과 달리 variable-length generation과 KV caching을 지원**

- 학습 시 토큰 배치를 효율적으로 활용할 수 있도록 block diffusion model을 위한 **훈련 알고리즘 제안** (Challenge 1)

- Gradient variance가 diffusion 모델 성능의 제한 요소임을 밝힘 + 데이터 기반 **노이즈 스케줄**로 해결 (Challenge 2)

- **성능 향상**!

<br/>

<br/>

## BACKGROUND: LANGUAGE MODELING PARADIGMS

### **notation**

$$ \mathcal{V}=\left\{\mathbf{x} \in\{0,1\}^V: \sum_i \mathbf{x}_i=1\right\} \subset \Delta^V $$

- scalar discrete random variables with V categories as ‘one-hot’ column

- $ \Delta^V $: simplex 공간

- $ m \in \mathcal{V} $: [MASK] token’s one-hot vector

<br/>

### **AUTOREGRESSIVE MODELS**

$$ \log p_{\theta}(\mathbf{x}) = \sum_{\ell=1}^{L} \log p_{\theta}(\mathbf{x}^{\ell} | \mathbf{x}^{<\ell}) $$

### <span style='color:yellow_background'>**DISCRETE DENOISING DIFFUSION PROBABILISTIC MODELS (D3PM)**</span>

- $ p $: denoising, $ q $: noising

- $ s(j) = (j-1)/T $, $ t(j) = j/T $ (이후에 j는 생략!)

	- 알파벳 순서대로 s가 앞 t가 뒤, s → t 과정은 noise를 더하는 과정

- <span style='color:yellow_background'>D3PM framework: q를 Markov forward process, 각각의 토큰에 대해 독립적으로 아래의 식을 진행</span>

	$$ \mathbf{x}^{\ell}: q\left(\mathbf{x}_t^{\ell} \mid \mathbf{x}_s^{\ell}\right)=\operatorname{Cat}\left(\mathbf{x}_t^{\ell} ; Q_t \mathbf{x}_s^{\ell}\right) \text { where } Q_t \in \mathbb{R}^{V \times V} $$

	- $ Q_t $의 예시

		- Uniform replacement

		$$ Q_t(i, j)= \begin{cases}1-\beta_t, & j=i \\ \beta_t /(V-1), & j \neq i\end{cases} $$

		- <span style='color:yellow_background'>**Masking 기반**</span>: $ \beta_t $ 확률로 [MASK]  토큰으로 변경

- 이상적인 diffusion model $ p_{\theta} $는 $ q $의 역방향이므로 D3PM에서는 아래 수식으로 $ p_{\theta} $를 정의

	$$ p_\theta\left(\mathbf{x}_s \mid \mathbf{x}_t\right)=\prod_{\ell=1}^L p_\theta\left(\mathbf{x}_s^{\ell} \mid \mathbf{x}_t\right)=\sum_{\mathbf{x}}\left[\prod_{\ell=1}^L q\left(\mathbf{x}_s^{\ell} \mid \mathbf{x}_t^{\ell}, \mathbf{x}^{\ell}\right) p_\theta\left(\mathbf{x}^{\ell} \mid \mathbf{x}_t\right)\right] $$

	- 1단계 denoising 과정 = 개별 토큰 위치에 대한 denoise는 독립 과정 = $ x^\ell $ 근사

	- $ x^{\ell} $ (원본 텍스트)가 주어진다면 q를 활용해 $ x_t^\ell \rightarrow x_s^\ell $을 완전히 복구할 수 있음.

	- denoise 과정에서 $ x^\ell $이 주어지지 않으므로 $ p $로 근사:  $ p_\theta\left(\mathbf{x}^{\ell} \mid \mathbf{x}_t\right) $

- **Negative ELBO (NELBO)를 이용해 학습**

$$ \mathcal{L}(\mathbf{x} ; \theta)=\mathbb{E}_q\left[-\log p_\theta\left(\mathbf{x} \mid \mathbf{x}_{t(1)}\right)+\sum_{j=1}^T D_{\mathrm{KL}}\left[q\left(\mathbf{x}_{s(j)} \mid \mathbf{x}_{t(j)}, \mathbf{x}\right) \| p_\theta\left(\mathbf{x}_{s(j)} \mid \mathbf{x}_{t(j)}\right)\right]+D_{\mathrm{KL}}\left[q\left(\mathbf{x}_{t(T)} \mid \mathbf{x}\right) \| p_\theta\left(\mathbf{x}_{t(T)} \right)\right]\right] $$

- 1, 2항: noise, denoise 과정에서의 샘플의 일치 정도

- 3항 얼마나 noise를 잘 만들었는가

<br/>

## BLOCK DIFFUSION LANGUAGE MODELING

### BLOCK DIFFUSION DISTRIBUTIONS AND MODEL ARCHITECTURES

<span style='color:yellow_background'>**Block Definition**</span>

- 길이 $ L' $이 되게 $ B $개의 block으로 만들기 ($ x^b: x^{(b-1)L':bL'} \in \{1,...,B\} $)

- Likelihood over block

	$$ \log p_\theta(\mathbf{x})=\sum_{b=1}^B \log p_\theta\left(\mathbf{x}^b \mid \mathbf{x}^{<b}\right) $$

block 내에서 reverse diffusion 프로세스 적용

$$
p_{\theta}(\mathbf{x}_s^b | \mathbf{x}_t^b, \mathbf{x}^{<b}) = \sum_{\mathbf{x}^b} q(\mathbf{x}_s^b | \mathbf{x}_t^b, \mathbf{x}^b) p_{\theta}(\mathbf{x}^b | \mathbf{x}_t^b, \mathbf{x}^{<b}) $$

- block이 constraint인 것을 제외하면 preliminaries의 수식과 동일!

<br/>

<span style='color:yellow_background'>**Learning Objective**</span>

$$
- \log p_\theta(\mathbf{x}) \leq \mathcal{L}_{\text{BD}}(\mathbf{x}; \theta) := \sum_{b=1}^{B} \mathcal{L}(\mathbf{x}^b, \mathbf{x}^{<b}; \theta) $$

NELBO를 적용해 위와 같이 학습 목적함수 정의, 이것도 Sum을 제외하곤 전부 같음!

<br/>

<span style='color:yellow_background'>**Denoiser model**</span>

- Transformer $ x_\theta $를 사용해 파라미터화: $ p_\theta(x^b | x_t^b, x^{<b}) $

	- given $ x^{<b} $: AR 특성 유지

	- $ x^b $ 예측: Denosing

- Block들에 대해 병렬적 학습을 가능하게 함 (block-causal attention mask)

- $ x_\theta $의 학습: block b 내에서 $ x_\theta^b(x_t^b, x^{<b}) $ → $ L' $ 길이의 결과 예측

→ 아래 K, V 캐시 수식을 보시면 모델을 이해하기 쉬움!

<br/>

<span style='color:yellow_background'>**K, V caching**</span>

$$ \mathbf{x}_{\text {logits }}^b, \mathbf{K}^b, \mathbf{V}^b \leftarrow \mathbf{x}_\theta^b\left(\mathbf{x}_t^b, \mathbf{K}^{1: b-1}, \mathbf{V}^{1: b-1}\right):=\mathbf{x}_\theta^b\left(\mathbf{x}_t^b, \mathbf{x}^{<b}\right) $$

- recomputing을 막기 위한 block 단위 caching

<br/>

### EFFICIENT TRAINING AND SAMPLING ALGORITHMS

<span style='color:yellow_background'>**Training**</span>

- 모든 block은 $ x_\theta $의 forward pass를 두 번 거쳐야 함 ($ x_t^b $, $ x^b $) → 계산의 효율화 필요

1. Block 별로 noise level sampling

1. 각 block에 대해 noisy input $ x_{t_b}^b $ 생성

1. $ \left(\emptyset, \mathbf{K}^{1: B}, \mathbf{V}^{1: B}\right) \leftarrow \mathbf{x}_\theta(\mathbf{x}) $: 원본 x를 이용해 K, V cache 미리 다 계산하기

1. 모든 b에 대해 $ x^b_{\text{logit}} $ 계산

	- Naive: B-times loop를 이용해 forward pass를 별도로 진행

	- Vectorized 방식

		- $ x_{\text {noisy }}=x_{t_1}^1 \oplus x_{t_2}^2 \oplus \cdots \oplus x_{t_B}^B $

		- $ x_{\text{noisy}} \oplus x $을 input으로 하여 한 번에 계산 How? attention mask를 이전 block만 조회하게끔 조절

<br/>

<span style='color:yellow_background'>**Sampling**</span>

- Block 단위의 순차적 샘플링, K, V 캐싱 가능 ← AR의 장점

- arbitrary length 생성 가능 ← AR의 장점

- block 내부에선 Parallel하게 생성 가능 ← Diffusion의 장점

<br/>

## UNDERSTANDING LIKELIHOOD GAPS BETWEEN DIFFUSION & AR MODELS

### MASKED BD3-LMS

- 최근 가장 큰 효과를 보이고 있는 masking noise process를 적용

- Per-token noise process

	$$ q\left(\mathbf{x}_t^{\ell} \mid \mathbf{x}^{\ell}\right)=\operatorname{Cat}\left(\mathbf{x}_t^{\ell} ; \alpha_t \mathbf{x}^{\ell}+\left(1-\alpha_t\right) \mathbf{m}\right) $$

	- $ \alpha_0=1 $ → linear scheduler→ $ \alpha_1=0 $

- <span style='color:yellow_background'>목적 함수 (Sahoo et al. (2024b)의 SUBS-parameterization denoising 모델 철학을 따름!!)</span>

	- **Zero Masking Probabilities**: clean sequence( $ x^\ell $)에는 mask를 포함하지 않음. (이건 아래의 조건을 위해 필요한듯합니다.)

	- **Carry-Over Unmasking**: $ x_t^\ell \neq m $인 경우 $ q\left(x_s^l=x_t^l \mid x_t^l \neq m\right)=1 $. 즉, unmaksed된 token은 다시 mask 되지 않음.

		- Denoising model 단순화: $ p_\theta\left(x_s^{\ell}=x_t^{\ell} \mid x_t^{\ell} \neq m\right)=1 $

	$$ -\log p_\theta(\mathbf{x}) \leq \mathcal{L}_{\mathrm{BD}}(\mathbf{x} ; \theta):=\sum_{b=1}^B \mathbb{E}_{t \sim[0,1]} \mathbb{E}_q \frac{\alpha_t^{\prime}}{1-\alpha_t} \log p_\theta\left(\mathbf{x}^b \mid \mathbf{x}_t^b, \mathbf{x}^{<b}\right) $$

	- $ \alpha_t = \prod_{\tau=1}^{t}(1 - \beta_\tau) $: t시점까지 mask되지 않고 살아남을 확률

	- <span style='color:yellow_background'>why?</span>

		- t 시점에서 mask transition matrix (noising 과정에서 i→ j로 변환)

			$$ \left[Q_t\right]_{i j}= \begin{cases}1 & \text { if } i=j=m \\ \alpha_t & \text { if } i=j \neq m \\ 1-\alpha_t & \text { if } j=m, i \neq m\end{cases} $$

			- 순서대로 mask는 mask 유지

			- 값을 그대로 가질 확률: $ \alpha_t $

			- token이 mask 될 확률: $ 1 - \alpha_t $

		- marginal $ Q_{t|s} $ (여기서 $ \alpha_{t|s} = \alpha_t/\alpha_s $)

			$$ \left[Q_{t \mid s}\right]_{i j}= \begin{cases}1 & \text { if } i=j=m \\ \alpha_{t \mid s} & \text { if } i=j \neq m \\ 1-\alpha_{t \mid s} & \text { if } j=m, i \neq m\end{cases} $$

		전개…… $ \mathcal{L}_{\text{diffusion}} $은 앞의 수식과 의미적으로 같습니다…..

		$$ \mathcal{L}_{\text{diffusion}} = \sum_{b=1}^{B} \mathbb{E}_t \mathbb{E}_q T \left[ \text{D}_{\text{KL}} \left[ q(\mathbf{x}_s^b|\mathbf{x}_t^b, \mathbf{x}^b) \Vert p_{\theta}(\mathbf{x}_s^b|\mathbf{x}_t^b, \mathbf{x}^{<b}) \right] \right] \\= \sum_{b=1}^{B} \mathbb{E}_t \mathbb{E}_q T \left[ \sum_{\ell=1}^{L'} \text{D}_{\text{KL}} \left[ q(\mathbf{x}_s^{b,\ell}|\mathbf{x}_t^{b,\ell}, \mathbf{x}^{b,\ell}) \Vert p_{\theta}(\mathbf{x}_s^{b,\ell}|\mathbf{x}_t^b, \mathbf{x}^{<b}) \right] \right] $$

		- 일단 여기까진 정의대로 가되 block 내 token 길이인 $ L' $으로 확장

		- KL divergence 정의에 의해 다음과 같이 전개 가능 (이건 ㄹㅇ KLD 정의)

			$$ \sum_{\ell=1}^{L^{\prime}} D_{\mathrm{KL}}\left(q \| p_\theta\right)=\sum_{\ell=1}^{L^{\prime}} \mathbb{E}_{q\left(x_s^{b, l} \mid x_t^{b, l}, x^{b, l}\right)}\left[\log q\left(x_s^{b, l} \mid x_t^{b, l}, x^{b, l}\right)-\log p_\theta\left(x_s^{b, l} \mid x_t^{b, l}, x^{<b}\right)\right] $$

		- $ \log{q} $ 부분은 학습과 무관하므로 제외

			$$ \sum_{\ell=1}^{L^{\prime}} \mathbb{E}_{q\left(x_s^{b, l} \mid x_t^{b, l}, x^{b, l}\right)}\left[-\log p_\theta\left(x_s^{b, l} \mid x_t^{b, l}, x^{<b}\right)\right] $$

			- $ q(x_s^{b,\ell} = x^{b,\ell} | x_t^{b,\ell} = m, x^{b,\ell}) = \frac{\alpha_s - \alpha_t}{1 - \alpha_t} $

			- $ q(x_s^{b,\ell} = m | x_t^{b,\ell} = m, x^{b,\ell}) = \frac{1 - \alpha_s}{1 - \alpha_t} $

			- $ q(x_s^{b,\ell} = x^{b,\ell} | x_t^{b,\ell} = x^{b,\ell}, x^{b,\ell}) = 1 $: 1이므로 뒤에 계산에서 제외

		- $ x_t^{b,\ell} $이 mask인 경우만 계산

			$$ \frac{\alpha_s - \alpha_t}{1 - \alpha_t}[- \log p_\theta(x_s^{b,\ell} = x^{b,\ell} | x_t^{b,\ell} = m, x^{<b})] + \frac{1 - \alpha_s}{1 - \alpha_t}[- \log p_\theta(x_s^{b,\ell} = m | x_t^{b,\ell} = m, x^{<b})] $$

		- 뒤에 항은 mask → mask는 상수라서 계산에서 제외

			$ = \sum_{b=1}^{B} \mathbb{E}_t \mathbb{E}_q T \left[ \sum_{\ell=1}^{L'} \frac{\alpha_t - \alpha_s}{1 - \alpha_t} \log p_\theta(x^{b,\ell} | x_t^{b,\ell}, x^{<b}) \right] $

			$ = \sum_{b=1}^{B} \mathbb{E}_t \mathbb{E}_q T \left[ \frac{\alpha_t - \alpha_s}{1 - \alpha_t} \log p_\theta(x^b | x_t^b, x^{<b}) \right] $

		 $ T \rarr \infin, T(\alpha_t - \alpha_s) = \alpha'_t $

<br/>

### CASE STUDY: SINGLE TOKEN GENERATION

- $ L^\prime $ = 1인 경우, MASKED BD3-LMS의 목적함수는 autoregressive NLL과 동등함.

	- <span style='color:yellow_background'>**직관적 핵석**</span>: block의 길이가 1이라면 한 토큰 단위 AR과 같음. → ??? 그래도 한 토큰 단위로 일어나는 diffusion 과정이 있는데? → mask로 intitialize 후, 원하는 다음 token을 찾는 과정이란 점에선 동일.

	- **수식 ok**

		$$ \begin{aligned}&-\log p(\mathbf{x}) \leq \sum_{b=1}^L \mathbb{E}_{t \sim[0,1]} \mathbb{E}_q\left[\frac{\alpha_t^{\prime}}{1-\alpha_t} \log p_\theta\left(\mathbf{x}^b \mid \mathbf{x}_t^b, \mathbf{x}^{<b}\right)\right] \\& \because \alpha_t^{\prime}=-1 \text { and } \alpha_t=1-t, \\&=-\sum_{b=1}^L \mathbb{E}_{t \sim[0,1]} \mathbb{E}_q {\left[\frac{1}{t} \log p_\theta\left(\mathbf{x}^b \mid \mathbf{x}_t^b, \mathbf{x}^{<b}\right)\right] } \\&=-\sum_{b=1}^L \mathbb{E}_{t \sim[0,1]} \frac{1}{t} \mathbb{E}_q\left[\log p_\theta\left(\mathbf{x}^b \mid \mathbf{x}_t^b, \mathbf{x}^{<b}\right)\right] \\& \text { Expanding } \mathbb{E}_q[.], \\&=-\sum_{b=1}^L \mathbb{E}_{t \sim[0,1]} \frac{1}{t} {\left[q\left(\mathbf{x}_t^b=\mathbf{m} \mid \mathbf{x}^b\right) \log p_\theta\left(\mathbf{x}^b \mid \mathbf{x}_t^b=\mathbf{m}, \mathbf{x}^{<b}\right)\right.} \\&\left.\quad+q\left(\mathbf{x}_t^b=\mathbf{x}^b \mid \mathbf{x}^b\right) \log p_\theta\left(\mathbf{x}^b \mid \mathbf{x}_t^b=\mathbf{x}^b, \mathbf{x}^{<b}\right)\right]\end{aligned} $$

		- linear scheduler에서 $ \alpha'_t, \alpha_t $의 정의는 위와 같음. 그 다음 전개 과정은 이해할 수 있을듯?

		- Expanding 부분은 Expatation of q를 제거 하기 위한 과정 q가 mask transition을 전제로 하므로 경우 (mask/unmask) 두 가지 확률에 대해서 전개

		- SUBS-parameterization 가정의 carry-over unmasking 특성으로 $ \log{p_\theta(x^b|x_t^b=x^b, x^{<b})} = 0 $

			$$ \begin{aligned}-\log p_\theta(\mathbf{x}) & \leq-\sum_{b=1}^L \mathbb{E}_{t \sim[0,1]} \frac{1}{t} q\left(\mathbf{x}_t^b=\mathbf{m} \mid \mathbf{x}^b\right) \log p_\theta\left(\mathbf{x}^b \mid \mathbf{x}_t^b=\mathbf{m}, \mathbf{x}^{<b}\right) \\& \because q\left(\mathbf{x}_t^b=\mathbf{m} \mid \mathbf{x}^b\right)=t, \text { we get: } \\& =-\sum_{b=1}^L \mathbb{E}_{t \sim[0,1]} \log p_\theta\left(\mathbf{x}^b \mid \mathbf{x}_t^b=\mathbf{m}, \mathbf{x}^{<b}\right)\\&
= -\sum_{b=1}^{L} \log p_\theta(\mathbf{x}^b \mid \mathbf{m}, \mathbf{x}^{<b})

\end{aligned} $$

			- $ q(x_t^b=m|x^b) = 1 - \alpha_t = 1 - (1 - t) = t $

			- $ t $는 상관없으니깐 삭제!

			- 최종 결과는 NLL 로스와 기대값이 같다!

- 학습 목표의 기대값이 같음에도 불구하고 perplexity gap (=높은 학습 variance)가 존재함을 확인

- 왜 그럴까?  $ \mathbb{E}_{t\sim\mathcal{U}[0,1]}q(x_t^\ell=m|x^\ell) $ = 0.5 기본적으로 학습에 사용하는 token의 수가 절반으로 줄기 때문에 variance가 커지는 것

- tuned schedule: $ q(x_t^\ell = m | x^\ell) $ = 1

	- 해당 schedule에서는 AR의 목적함수와 완전히 동일

	- PPL도 감소, NELBO의 분산도 감소

			<br/>

### DIFFUSION GAP FROM HIGH VARIANCE TRAINING

- Case study를 넘어 $ L^\ell \geq 1 $인 케이스로 확장하고 싶음!

	- NELBO는 이론적으로 t에 invariance (기존 연구 [ref](https://proceedings.neurips.cc/paper_files/paper/2024/file/eb0b13cc515724ab8015bc978fdde0ad-Paper-Conference.pdf): T가 무한히 커질수록 $ \alpha $값이 아닌 누적값에 의해서 기대값이 정의되기 때문… 이 이상의 이해는 포기)하기에 스케줄에 따른 기대값의 변화가 없어야 함.

	- 하지만 우리는 모든 연산을 한 번에 하는 것이 아닌 Batch 연산을 활용 → 이론적인 invariance가 깨짐

	→ Schedule에 따라 분산의 결과가 변하게 됨. → Schedule을 잘 만들어보자!

- Batch size를 $ K $라고 할 때, batch of sequence $ \text{X} = [x^{(1)},x^{(1)},...,x^{(K)}] $, with each $ \text{x}^{(k)} \overset{\text{iid}}{\sim} q(x) $

- <span style='color:yellow_background'>**NELBO estimator**</span>

	$$ \mathcal{L}_{\text{BD}}(\mathbf{X};\theta) := l(\mathbf{X};\theta) = \frac{1}{K} \sum_{k=1}^{K} \sum_{b=1}^{B} \frac{\alpha'_{t(k,b)}}{1 - \alpha_{t(k,b)}} \log p_{\theta} \left( \mathbf{x}^{(k),b} \mid \mathbf{x}_{t(k,b)}^{(k),b}, \mathbf{x}^{(k),<b} \right) $$

- <span style='color:yellow_background'>**Variance of the gradient estimator**</span>

	$$ \text{Var}_{\mathbf{X},t} \left[ \nabla_{\theta}l(\mathbf{X};\theta) \right] \approx \frac{1}{M-1} \sum_{m=1}^{M} \left\| \nabla_{\theta}l(\mathbf{X}^m;\theta) - \frac{1}{M} \sum_{m=1}^{M} \nabla_{\theta}l(\mathbf{X}^m;\theta) \right\|_2^2 $$

<br/>

## LOW-VARIANCE NOISE SCHEDULES FOR BD3-LMS

### INTUITION: AVOID EXTREME MASK RATES & CLIPPED SCHEDULES FOR LOW-VARIANCE GRADIENTS

- 이상적인 마스킹: 모델이 다양한 수준의 노이즈 [MASK]에서 원래대로 되돌리는 법을 배우는 것

- 극단적인 마스킹

	- 마스킹 토큰이 너무 적을 경우, 너무 쉬운 문제를 풀게 됨.

	- 모든 토큰이 마스킹 될 경우, 문맥 정보가 전혀 없음 빈도에 기반한 학습만 진행

→ 극단적인 부분을 날린 CLIP을 이용하자

→ sample mask rates: $  1 - \alpha_t \sim \mathcal{U}[\beta, \omega] $ for $ 0 \leq \beta, \omega \leq 1 $

<br/>

### DATA-DRIVEN CLIPPED SCHEDULES ACROSS BLOCK SIZES

- Block size ( $ L' $)에 따른 최적의 mask rate을 찾아보자.

- Gradient 분산을 최소화하기 위함이지만 아래 NELBO를 추정지로 하여 실험을 진행

	$$ \text{min}_{\beta,\omega} \text{Var}_{X,t}[\mathcal{L}(X; \theta, \beta, \omega)] $$

	- forward pass만으로 계산 가능

	- 실험 결과들에서 NELBO와 기울기 분산이 같은 경향성을 보임을 확인

- $ \beta, \omega $에 대해 grid search 진행

- Table 2에서 PPL과 NELBO과 상관성 보임을 재차 확인 + $ L' $에 따라 최적의 조합이 있음을 발견함.

<br/>

## EXPERIMENTS

- Pre-train: base BD3-LM ( $ L'=L $) for 850K gradient steps (순수 diffusion?)

- Fine-tune

	- 150K gradient steps on One Billion Words dataset (LM1B) and OpenWebText (OWT)

- $ L' $에 따라 다른 Clipped schedule 적용 (매 validation epoch 마다 최적의 $ \beta, \omega $ 조합을 찾음!)

<br/>

### LIKELIHOOD EVALUATION

[//]: # (column_list is not supported)

	[//]: # (column is not supported)

			[//]: # (column is not supported)

		- 다른 MDLM 모델 대비 perplexity이 향상됨

- Zero-shot validation perplexity 결과 Pubmed는 AR보다도 잘함.

- 대체로 다른 MDLM보단 PPL 값이 더 낮음.

<br/>

### SAMPLE QUALITY AND VARIABLE-LENGTH SEQUENCE GENERATION

- [EOS] 토큰을 생성하거나 sample quality가 급감 (the average entropy of the the last 256-token chunk is below 4)할 때까지 실험 진행

- SEDD 대비 최대 10배 더 긴 text 생성 가능함.

- GPT-2를 이용해 generative perplexity 측정, 효율성을 보기 위해 the number of generation steps (NFEs)

- 기존 Block Diffusion 대비해도 더 적은 step에서 높은  Gen PPL 달성

- 정성 분석은 Appendix D에 있음. AR과 유사할 정도의 퀄리티, 다른 DLM보단 좋더라

<br/>

### ABLATIONS

[//]: # (column_list is not supported)

	[//]: # (column is not supported)

		<span style='color:yellow_background'>**SELECTING NOISE SCHEDULES TO REDUCE TRAINING VARIANCE**</span>

				- $ L' $이 작을수록 heavier mask가 효과적

	[//]: # (column is not supported)

		<span style='color:yellow_background'>**EFFICIENCY OF TRAINING ALGORITHM**</span>

				- concat 활용하여 처리할 경우, sparse attention mask 활용

		- FlexAttention을 이용할 경우 Sparsity를 활용해 효율적 처리 가능

		- 20-25% 속도 향상 가능!

<br/>

<br/>

---

- 수학 공부 열심히 하자.

- 결과에서 힘이 많이 빠지긴 한다.

- 전개과정에서 이 정도는 해야 oral로 가는구나 벽느껴진다.