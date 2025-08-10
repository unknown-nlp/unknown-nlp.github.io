---
categories: paper-reviews
date: '2024-06-11 00:00:00'
description: ' 논문 리뷰 - Scaling Monosemanticity: Extracting Interpretable Features
  from Claude 3 Sonnet'
giscus_comments: true
layout: post
related_posts: false
tags: paper-review nlp
title: 'Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet'
---

**논문 정보**
- **Date**: 2024-06-11
- **Reviewer**: 상엽
- **Property**: LLM, Interpretability

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

[//]: # (unsupported is not supported)

AI safety에 관심이 매우 큰 anthropic

이전 연구 (Towards Monosemanticity: Decomposing Language Models With Dictionary Learning)에서  one-layer transformer에 Sparse AutoEncoder (SAE)를 이용해 monosemanric features를 복구할 수 있다는 사실을  발견

**이것이 실제로 SOTA transformer 모델에도 적용이 가능할 것인가?**

- 실제 어떤 컨셉과 feature를 연결지을 수 있다면 AI safety에 직접적인 연결이 가능할 것이다

<br/>

이번 논문에서는

- Anthropic’s medium-sized production model, Claude 3 Sonnet을 이용

- 기존보다 더 다양하고 큰  Sparse Autoencoder (SAE)를 활용해서 다양한 feature를 탐색

- Feature의 존재 확인 → Feature를 이용한 모델 행동 제어 확인

- Multilingual, Multimodal에서 역시 feature가 동일하게 잘 작용함을 확인

- 특히, Safety feature가 존재함을 확인할 수 있었음

- 향후 연구 및 모델 확장을 위한 SAE의 scaling law 실험 진행

	<br/>

<br/>

### Preliminaries

link : [https://transformer-circuits.pub/2022/toy_model/index.html#motivation](https://transformer-circuits.pub/2022/toy_model/index.html#motivation)

신경망은 입력된 데이터를 처리하여 특정 feature를 고차원 space에 방향(direction)으로 표현한다고 생각할 수 있음.

example

	- King - Man = Queen - Woman

	- Inception V1 초기 뉴런이 커브를 detect한다.

		<br/>

신경망의 내부 작동 방식을 이해하고 분석한다 (reverse engineering)의 관점에서 네트워크가 만드는 representation이 다음과 같은 특징을 가졌는지를 확인하는 것은 필수적임.

- Decomposability : Network representation은 독립적으로 이해될 수 있는 feature로 설명될 수 있다. (비슷한 특징을 가진 feature들은 특정 군집을 형성한다.)

	- 전체를 관측하지 않고도 해당하는 특성을 알 수 있게 한다. (Cluster, manifold 등)

	- 하지만 이런 특성 만으로는 reverse engineering이 불가능함. → 어떻게 이런 feature에 접근할 수 있는가? → **Linearity**

- Linearity : Feature는 방향에 의해 표현되어진다.

→ 위의 개념은 매우 추상적인 개념이라 명확한 증거, 증명을 찾을 수는 없지만 여러 차례 실험적 결과가 뒷받침해준다고 믿을 수 있지 않을까?

<br/>

위의 특성이 명확히 보이는 사례와 아닌 사례의 차이점은 어떻게 설명할 수 있을까?

- **Superposition:** 활성화 공간 내 (제한된 차원)에서 더 많은 의미를 표현하기 위해 여러 의미를 중첩적으로 가짐.

		- **Almost Orthogonal Vectors : **고차원 공간에서 exp(n) 개의 거의 수직인 벡터로 표현이 가능하다 (Johnson-Lindenstrauss lemma)

		- lemma 자체는 고차원 거리 → 저차원 거리가 거의 유지 된다.

		- n 차원보다 더 많은 표현을 의미할 수 있다로 해석하면 되는듯

	- **Compressed sensing :** 고차원 → 저차원 projection은 재복구가 불가능하지만 sparse 벡터에서는 때때로 recover가 가능하다.

	→ Almost orthogonal은 완전한 직교는 아니기 때문에 서로간의 간섭/노이즈가 발생하지만 sparsity가 크다면 그 영향은 적다.

	→ 결론적으로 Sparse한 Feature를 이용해

	- 차원보다 더 많은 컨셉을 (Almost Orthogonal Vectors)

	- 명확히 설명할 수 있다. (sparsity로 인해 reconstruction이 쉽다.)

	<br/>

### Dictionary learning

- 위의 결론에 대한 해답은 Sparse Autoencoder와 같은 dictionary learning 방식을 이용해 feature를 분석하는 것!

- Dictionary learning: 데이터를 보다 간단한 벡터들의 선형 결합으로 표현하는 것

- 현재까지 SAE를 이용한 연구는 매우 작은 모델을 분석하는 정도로 한정되어 있으며 이것이 SOTA 모델과 같은 LLM에서 어떤 양상을 보일지는 모른다 → 우리가 하겠다!

<br/>

## Sparse Autoencoders

Our SAE consists of two layers.

- Encoder: ReLU를 사용하는 linear transform을 통해 모델 activation을 고차원 layer (feature)로 mapping

- Decoder: feature를 다시 activation으로 복구

- Training

	1. model activation에 대해 scaler normalization 진행

	1. encoder : $ f_i(x)=\operatorname{ReLU}\left(\mathbf{W}_{i,}^{\text {enc }} \cdot \mathbf{x}+b_i^{\text {enc }}\right) $

	1. decoder : $ \hat{\mathbf{x}}=\mathbf{b}^{d e c}+\sum_{i=1}^F f_i(\mathbf{x}) \mathbf{W}_{., i}^{d e c} $

	1. $ \mathcal{L}=\mathbb{E}_{\mathbf{x}}\left[\|\mathbf{x}-\hat{\mathbf{x}}\|_2^2+\lambda \sum_i f_i(\mathbf{x}) \cdot\left\|\mathbf{W}_{\cdot, i}^{d e c}\right\|_2\right] $

	<br/>

### Our SAE experiments

[//]: # (column_list is not supported)

	[//]: # (column is not supported)

			[//]: # (column is not supported)

		- residual stream의 중간 레이어 activation을 활용 (MLP 이후)

	- MLP 레이어보다 크기가 작아 SAE 훈련 및 추론에 필요한 계산 비용이 더 적음.

	- Cross-layer superposition 문제를 완화시켜줌.

	- 중간 레이어가 더 흥미로운 abstract feature를 가질 확률이 높기 때문

- 1M, 4M, 34M의 feature들로 실험을 진행.

- scaling laws를 이용해 training step 결정

- L1 계수 : 5 사용

- 3가지 크기 feature 모두 활성화 된 non-zero feature는 300개가 안됨

- reconstruction은 model activation의 적어도 65%의 분산을 설명함.

$$ \text { Explained Variance Ratio }=1-\frac{\text { Variance of the Reconstruction Error }}{\text { Variance of the Original Data }} $$

- $ 10^7 $ token개 동안 활성화 되지 않은 feature를 dead feature로 정의

	- 1M : 2%

	- 4M : 35%

	- 34M : 65%

	<br/>

### Scaling Laws

- 추가적인 학습이 dictionary learning의 결과에 미치는 영향 파악

- 한정된 자원 내에서 가장 높은 성능을 달성하는 방법에 대해 파악

평가를 위해서는 가장 좋은 feature를 정의할 수 있어야 함.

	- 단순 reconstruction loss와 일치하지는 않음.

	- 정성적 평가 결과 L1 계수가 5일 때, 가장 interpretable feature를 추출하며 dead feature가 줄어든다는 것을 발견.

<br/>

L1: 5를  기준으로 실험 진행

- Compute 증가 → 기대 최소 Loss 감소 (power law)

<br/>

- features 수와 training step 각각에 대한 최소 Loss 역시 power law를 따름.

<br/>

쿼리 Feature와 유사도를 activation으로 정의

- Orange : 가장 강한 activation

- White : no activation

Documents와 feature의 유사도 값 중 최대값을 기준으로 문서들을 추출

<br/>

실제 interpretation 사례들을 추출할 수 있었음!

<br/>

하이라이트를 통해 feature가 해석력이 있음을 어느정도 알 수 있긴 하지만 명확한 검증을 위해 아래 항목들에 대한 정량적/정성적 분석을 실행함.

- **Specificity** : feature가 활성화되면 관련 개념이 (신뢰성 있게) 컨텍스트에 존재한다.

- **Influence on behavior** : 뉴런의 활성화를 조절하는 것이 downstream behavior에 영향을 미친다.

<br/>

**Specificity**

Opus를 이용해 아래 rubric을 기준으로 scoring 진행

- 0 – feature와 context는 완전히 무관하다.

- 1 – feature가 context와 관련성이 있지만 하이라이트 텍스트 근처에 없거나 모호하게만 관련성이 있다.

- 2 – feature가 하이라이트 텍스트 근처의 컨텍스트와 관련이 있거나 loosly related하다.

- 3 – feature가 하이라이트 텍스트에서 명확히 관련성이 있다.

<br/>

실험 결과

- 0을 제외한 Feature activation의 분포

- activation level에 해당하는 sample (Image, Text)를 random으로 추출

<br/>

The Golden Gate Bridge

[//]: # (column_list is not supported)

	[//]: # (column is not supported)

		- 유사한 다리 및 관광 명소

		- Bridge

	[//]: # (column is not supported)

		- 금문교

		- Golden gate bridge

<br/>

Brain Sciences

- Neuro science book & courses, cognitive science, psychology 등에서 활성화

→ text dataset으로만 학습했음에도 activation에 따른 이미지 retrieval 역시 잘되었다. (image와 text가 어떻게 모델로 결합되는지와 같은 내용은 공개 안함.)

<br/>

Multilinual에서도 비슷한 현상을 관측할 수 있었음.

<br/>

결론적으로 높은 활성을 보인 항목들에서는 일관성 있게 관련성 있는 텍스트와 이미지를 추출

낮은 활성값을 가진 항목에서는 유사 개념을 추출하긴 하지만 우리의 해석과 완전히 일치하지 않는 항목들을 추출하기도 함.

- almost orthogonal로 인한 간섭

- SAE가 우리 생각보다 discriminative한 representation을 만들지 못하는 것

어떤 이유든 높은 활성에서 해석이 명확하다는 점은 유의미하다.

하지만 이것만으로도 여전히 우리가 뽑은 feature의 유효성을 입증했다고 보기는 어렵다고 생각함.

<br/>

### Influence on Behavior

- Feature의 해석이 모델의 행동에 미치는 영향을 파악하기 위해 Feature steering 실험

- 관심있는 feature의 값을 인위적으로 올리거나 내리면서 실험 진행

- How?

	1. $ \hat{x} = \text{decoder}(\text{encoder}(x)) $

	1. $ x = \hat{x} + e $

	1. feature 계산 $ f=\text{encoder}(x) $

	1. 조정할 feature 계산 $ f \leftarrow f + \alpha f^{*} $

	1. $ x \leftarrow \text{decoder}(f) + e $

<br/>

- 각각의 activation값을 10x, 8x, 5x 했을 때 결과

	- 자기를 금문교로 정의

	- 좋아하는 과학이 neuro science로 변함.

	- 관광지 추천이 바뀜.

	- 짧은 답변 요구에도 infra를 답변에 추가함.

<br/>

- Feature steering이 매우 큰 효과가 있었다!

- 이는 모델의 태도, 선호도, 명시된 목표 및 편향을 수정하는 데 사용될 수 있으며 특정 오류를 유도하거나 모델의 안전 장치를 회피/강화하는 데 사용될 수 있음을 시사함.

- 앤트로픽은 이를 통해 안전한 AI를 만드는데 사용할 수 있을 거라고 함.

<br/>

## Sophisticated Features

위의 feature들 보다 조금 더 복잡한 개념 (코드의 정확성, 변수 유형 등)을 이해하고 있는지 확인

<br/>

### Code Error Feature

- 일부러 typo가 있는 코드를 제공

- code error feature activations

		- 이것이 정말로 코드 에러를 인지한 것인지 단순히 typo를 인식한 것인지를 알기 위해 일반 대화에서도 해당 feature를 확인

		→ 단순히 typo를 찾는 것은 아니고 실제로 code error를 인지한 것으로 보임.

- 그렇다면 더 복잡한 에러는 어떨까?

	- Divide by zero example

			- Invalid input

		- 더 복잡한 feature에 대해서도 steering 실험을 진행

		- 옳은 코드에 대해서도 에러를 만들어냄.

		- 틀린 코드에서도 정답을 만들어 냄.

		- >>>를 추가할 경우 에러가 없는 코드로 수정하는 코드를 작성함.

	<br/>

### Feature representing functions

- 코드 내 함수 정의와 코드 내 reference를 추적하는 것을 발견 (실제로 이렇게 적혀있긴 한데 내용을 보면 이해됨.)

		- Feature : Addition

	- 실제 함수가 호출 될 경우에만 Highlight

		- 합성 함수에서도 이를 인지하더라.

- Feature steering

		<br/>

	<br/>

## Feature vs. Neurons

- SAE에서 만든 Feature가 모델 자체의 Neuron보다 더 해석력이 있는 것이 맞을까?

	- SAE는 residual stream을 이용해 feature를 생성하는데 residual stream은 이전 MLP의 결과들을 사용하고 있음.

	- SAE가 아닌 모델 자체 뉴런에 이미 해석력이 있는 것은 아닐까?

- 랜덤 추출한 100만개의 feature의 활성화값과 이전 뉴런들의 활성화값의 피어슨 상관계수를 측정

	- 82%의 feature들에서 corr 0.3 이하

- 실제 activation 결과도 비교

	- specificity도 차이남.

		<br/>

	<br/>

## Exploring Feature Neighborhoods

cosine similarity를 기준으로 유사함을 정의, UMAP을 이용해 시각화 진행.

- 전체 링크

	- [https://transformer-circuits.pub/2024/scaling-monosemanticity/umap.html?targetId=34m_31164353](https://transformer-circuits.pub/2024/scaling-monosemanticity/umap.html?targetId=34m_31164353)

<br/>

Golden Gate Bridge Feature

- 가까운 곳에는 San Fancisco 지명들이 등장 먼 곳에는 좀 더 추상적인 관련성이 있는 다른 지역의 명소들이 군집해 있음.

- SAE의 크기가 증가함에 따라 각각의 Feature들이 좀 더 세분화되는 것을 확인할 수 있었음.

- 사이즈가 커질수록 이전에는 잡지 못했던 Feature도 찾아냈음. (Earthquake region)

<br/>

### Feature Categories

- person features

- country features

- basic code features

	- list position features

	<br/>

<br/>

## Feature as Computational Intermediates

Feature를 활용할 수 있는 또 다른 응용으로 모델이 출력을 생산하기까지의 중간 계산 과정을 분석하는 것.

<br/>

Example: Emotional Inferences

```json
John says, "I want to be alone right now." John feels
(completion: sad − happy)

```

- Ablation : 특정 feature의 영향을 줄였을 때 next token prediction에 가장 큰 영향을 주는지

	- 정답: sad, 오답: happy

		- 평균 activation score를 기준으로 상위 feature를 추출할 경우

	- 덜 유용함

	<br/>

<br/>

<br/>

```json
Fact: The capital of the state where Kobe Bryant played basketball is
(completion: Sacramento − Albany)

```

top-5 features

- A Kobe Bryant feature

- A California feature, which notably activates the most strongly on text after “California” is mentioned, rather than “California” itself

- A “capital” feature

- A Los Angeles feature

- A Los Angeles Lakers feature

<br/>

위의 결과와 비슷한 양상

<br/>

<br/>

## Searching for Specific Features

Feature들은 너무나 많기 때문에 이를 찾을 수 있는 방법에 대해 제안

<br/>

**Single prompts**

- 특정 개념과 관련한 단일 프롬프트를 제공하고 그 프롬프트에서 특정 토큰에 대해 가장 활성화되는 Feature를 찾음.

<br/>

**Prompt combinations**

- single prompt에서 Feature가 관심 개념과 관련이 없는 경우도 있었기 때문에 여러 프롬프트를 사용하는 방식을 활용

- 여러 프롬프트에서 동시에 활성화되는 것 + “negative” 프롬프트를 통해 활성화 되지 않는 것

<br/>

**Special cases**

- safety relevant feature의 경우, small dataset 구축 후, linear classifier를 이용해 가장 구별성이 높은 feature를 찾음.

<br/>

**Geometric methods**

- cosine similarity를 이용해 nearest neighbor feature들을 탐색

<br/>

**Attribution**

- 앞에서 설명했듯 next token prediction을 기준으로 feature 탐색

<br/>

<br/>

- LLM은 다양한 방식으로 악용될 여지가 있음.

- 이러한 모델 해석력에 대한 실험을 하게 된 가장 큰 동기가 이러한 위협으로부터 안전한 LLM을 만드는 것.

- 이전 결과들과 같이 Safety 관련 feature들의 존재를 확인할 수 있었고 모델의 행동 방식도 조절할 수 있음을 확인함.

<br/>

<br/>

### **Safety-relevant code features**

- unsafe code : 보안 취약성

- code error : 악의적인 버그 발생

- backdoor

	- 실제 안전성과 feature의 관계를 파악하기 위해 feature steering 진행

		- buffer overflow bug 발생

	<br/>

	### **Bias Features**

	- bias, racism, sexism, hatred, and slurs.

	- 구체적인 내용은 혐오스럽기 때문에 빼고 흥미로운 예시만 추가했다 함.

						- 간호사 == 여성, 왜그렇게 답변을 했는지에 대한 설명까지 추가함.

	- 이외에도 혐오 발언 등을 feature를 통해서 조절할 수 있었다 함.

	- x20에서는 인종 차별적 발언과 자기 혐오를 동반한 대화가 진행되더라….

	<br/>

	### **Sycophancy Features**

			- 무한 칭찬

<br/>

### **Deception, Power-seeking and Manipulation-related Features**

<br/>

### Criminal or Dangerous Content Features

<br/>

<br/>

- 현재 결과는 초기 단계이기 때문에 이러한 결과를 너무 과대하게 해석하는 것은 참자.

- Safety feature가 언제 활성화되며 이것이 model의 답변에 어떻게 영향을 주는지를 확인하는 것은 여전히 해결해야 될 부분이 많으며 anthropic이 현재 가지고 있는 연구 관심사들은 다음과 같은 게 있다.

	- What features activate on tokens we'd expect to signify **Claude's self-identity**? 

	- What features need to activate / remain inactive for Claude to give advice on producing **Chemical, Biological, Radiological or Nuclear (CBRN) weapons**? 

	- What features activate when we ask questions probing **Claude's goals and values**?

	- What features activate during **jailbreaks**?

	- What features activate when we ask Claude questions about **its subjective experience**?

	- etc.

- 긍정적인 부분

	- text로 학습된 SAE에서 이미지 활성화도 일관성 있는 결과를 보였다.

	- 구체적-추상적 개념 모두 가능했다. ex) 보안 취약점

- 부정적인 부분 (한계점)

	- 현재 결과가 모든 것을 대변할 수는 없음.

	- 명확한 학습 목표 즉, 평가 기준이 현재는 없음.

	- 근본적인 challenge

		- **Superposition:** 많은 feature들이 여러 레이어, attention 등에서 중첩되고 있으며 이를 해결할 방법은 현재 없다.

		- **모든 특징을 찾을 방법이 없다: 가능한 방법이 있다고 해도 비용적으로 불가능에 가깝다.**

		- **shrinkage**: L1 페널티를 이용한 sparsity 구현은 non-zero value를 underestimate하는 문제가 있으며 이것이 SAE의 성능을 크게 저하시킨다고 생각함. 이를 해결하기 위한 여러 연구들이 있으며 이를 활용해야할 것 같다.

		- etc.

		<br/>