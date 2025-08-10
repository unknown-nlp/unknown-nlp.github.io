---
categories:
- paper-reviews
date: '2024-02-13 00:00:00'
description: 논문 리뷰
giscus_comments: true
layout: post
related_posts: false
tags:
- attention
- language-model
- llm
- paper-review
- pre-training
- reasoning
thumbnail: assets/img/posts/2024-02-13-llm-augmented-llms-expanding-capabilities-through-composition/thumbnail.jpg
title: 'LLM AUGMENTED LLMS:

  EXPANDING CAPABILITIES THROUGH COMPOSITION'
---

**논문 정보**
- **Date**: 2024-02-13
- **Reviewer**: 준원 장

## 1. Introduction

- Foundation LLM이 commonsense & factual reasoning, world knowledge,  coherent language generation 능력을 보유 → FT로 domain expert LLM을 만들어서 활용

- 하지만 한번 FT해서 domain expert LLM (code understanding, low-resource language understanding)으로 instance를 변경하면 cross domain에서 활용 불가

- Foundation capabilities를 가지고 있는 anchor LLM과 하나의 domain에 보다 특화된 augment LLM(사이즈가 작은)을 결합해 효율적으로 Foundation LLM을 운영하면서 두 모델의 capabilities를 결합할 수 있는 간단한 방법론 제시

# Model Merging # Model composition # Knowledge Distillation 

## 2. Related Works

- Parameter Efficient Tuning

  - Foundation LLM을 원하는 Target Domain에 가장 효율적으로 학습시키는 방법은 LoRA weight을 도입해 학습시키는 것

  - 그러나 LoRA weight의 rank가 낮기 때문에 Foundation LLM의 original corpus에 포함되지 않는 long-tail domain KG를 학습시킬때 제한적일 수 있음

→ 해당 논문에서는 Target Domain에 학습된 (보다 사이즈가 작은) augment LLM이 있다고 가정하고 이 모델을 활용하고자 함

- Model Merging

  - Task vector averaging (or Model Output averaging)

    - 각 LLM이 target domain/task에 잘 align되어야 유효함

  - Model Weight Averaging

    - 같은 weight dimension을 가지거나, 동일한 pre-trained objective로 학습한 LLM이어야 유효함

- Model and Task Compositionality

  - 기존 Enc-Dec구조에서 많이 상용되고 mulit-modal에서 활용되는 Model 간의 cross attention을 LLM에 끌어와보겠다

## 3. COMPOSITION TO AUGMENT LANGUAGE MODELS (CALM)

{% include figure.liquid loading="eager" path="assets/img/posts/2024-02-13-llm-augmented-llms-expanding-capabilities-through-composition/image_000.png" class="img-fluid rounded z-depth-1" %}

### Notation

- Anchor model (Foundation Model, 일반적으로 MMLU와 같은 전반적인 영역에서 검증된 성능을 보이는 모델): M_{B} 

- Augmenting model (Domain Specific sLLM, 특정 domain에 FT된 small scale LLM): M_{A} 

- Additional learnable parameter: \theta_{C} 

- Set of examples for learning composition: D_{C} 

- Goal → learn a composition: M_{A \bigoplus B} =f(M_{A} ,M_{B}, \theta_{C}, D_{C})

### Assumption

(준원) Domain expert M_{A}가 존재해야함, LLM 2개 올릴 GPU vram

1. M_{A}, M_{B}에 대한 weight 접근, forward, backward가 자유로움

1. M_{A}, M_{B}의 weight 변경 불가

1. M_{A}, M_{B}의 pre-training weight, state, hyperparameter 접근 불가

1. Target composition domain(2개의 모델을 활용해서 달성하고자 하는 이중도메인)에 대한 few examples(D_{C} )가 존재한다. (굉장히 강력함)

- D_{C} 를 엄밀하게 구성하는것은 실제로 거의 불가능에 가까움

- 목표는  M_{A}, M_{B}의 capababilities를 composed model에 잘 녹이는 dataset이어야함

(M_{A}이 specialize된 task,  M_{B}이 specialized된 task를 딱 나누고 그 교집합을 가져와야하기 때문)

  - (예시)

t_{1} : key → value로 mapping하는 task

t_{2} : 사칙연산 

D_{C}:  key를 value로 mapping하고 사칙연산

  - 논문에서는 rough하게 t_{1 \cup 2}을  D_{C} 의 superset 그 일부를 D_{C} 로 사용함.

### Modeling

#### Main Target: D_{C} 를 가지고 composition target domain에 대해서 학습

- Augmenting model에서 Layer |L_{A}| = N_{A}=n개 선정

- Anchor model에서 Layer |L_{B}| = N_{B}=n개 선정

- Layer개수는 각 Model에서 선정된 Layer들간 간격이 일정하도록

  - (l_2 - l_1) = \cdots = (l_n - l_{n-1}) = \frac{N}{n}

1. Project Augment hidden representation to anchor dimension

{% include figure.liquid loading="eager" path="assets/img/posts/2024-02-13-llm-augmented-llms-expanding-capabilities-through-composition/image_001.png" class="img-fluid rounded z-depth-1" %}

1. Cross-attention between projected  augment hidden representation (Key, Value) and anchor hidden representation (Query)

1. Residual Connection

→ 다음 composition layer input으로 들어감.

#### Training

- Auto-regressive model과 동일하게 x_{t+1} = x_t \oplus y_t이 학습에 활용되나 두 모델이 계속 updated된 input을 forwarding해주어야 하기 때문에 매번 representation은 refresh됨

#### Composing Multiple Model

- 1개의 anchor model과 N개의 augment model에 대해서 각각 cross attention할 수 있다.. 라고 하면서 future work로 넘김..

## 4.  Experiments

- 3개의 domain에서 augmenting model이 foundation anchor model가 capabilities를 잘 결합하는지 검증

- Configuration

  - augmenting model: PaLM-XXS

  - foundation model: PaLM-2XS/ PaLM-S

  - N_{A.B}/n=4

- 실험은 기본적으로 다음의 틀을 따름

  -  augmenting model을 domain specific dataset D_{?}에 Continual Pre-training

  - compositional target example set인 D_{C}을 구축

  - CALM을 D_{C}에 training

### 4.1.  KEY-VALUE ARITHMETIC

-  PaLM-XXS에 있는 25K vocab(2-6chars)을 [1, 25K] INT로 mapping한 Key-value pair 구축

- 3-6 keys에 대해서 addition (+), subtraction (−), and multiplication (×) 연산 수행

- 3개 데이터셋 구축

(1) KV-Substitution (D_KV-SUBS) : mapping  

(<K1> + <K2> − <K3>, 10 + 22 − 24) 

→ 전체를 Augment model Continual Pre-training

→ 20% 크기를 D_{C} 구축에 활용

(2) KV-Arithmetic (D_KV-MATH) : mapping & arithmetic 

(<K1> + <K2> − <K3>, 8)

→ Evaluate Composition Target Domain

(3) Numeric-Arithmetic (D_NUM-MATH): arithmetic

(10 + 22 − 24, 8)

**#### Results**

{% include figure.liquid loading="eager" path="assets/img/posts/2024-02-13-llm-augmented-llms-expanding-capabilities-through-composition/image_002.png" class="img-fluid rounded z-depth-1" %}

- KV-Substitution를 학습하지 못한 Anchor는 아예 풀지 못하는 경향성을 보임, 반면 연산은 어느정도 수행함.

- CALM으로 KV-Substitution에 어느정도 fitting된 model의 도움을 받아 KV-Substitution을 조금만 학습하면 각 모델의 장점을 활용해서 composition target domain에서 좋은 성능을 보임.

### 4.2. LOW-RESOURCE LANGUAGE INCLUSIVITY

-  PaLM-XXS를 Next Thousand Languages (NTL)에 있는 low-resource language에 training → augment model 구축

- 같은 low-resource language의 ~5%를 가지고 CALM을 학습할 D_{C} (=D_{NTL} )을 구축

- Evaluation Task

  - Translation Non ENG > ENG (5shot)

  - Non ENG math grade school word problem. 

    - high resource

    - low resource (google translate)

**#### Results - t**ranslation Non ENG > ENG (5shot)

{% include figure.liquid loading="eager" path="assets/img/posts/2024-02-13-llm-augmented-llms-expanding-capabilities-through-composition/image_003.png" class="img-fluid rounded z-depth-1" %}

- M_{B}^{NTL}은 D_{NTL}로  anchor 모델을 직접 학습한 모델

-  아직 anchor모델을 직접 continual pre-training했을때 비해서 성능이 좋지는 못하나, 적은 trainable parameter로는 좋은 성능을 보여줌

- 175/192에서 augment model (애매하게 작성했는데 D_{NTL}로 학습한거 아닌거 같음)보다 성능 향상있었다고 함.

- 논문에 computational cost에 대한 비교나 설명을 명확하게 이야기 안해줬다는 아쉬움…!

**#### Results - **Non ENG math grade school word problem. 

{% include figure.liquid loading="eager" path="assets/img/posts/2024-02-13-llm-augmented-llms-expanding-capabilities-through-composition/image_004.png" class="img-fluid rounded z-depth-1" %}

- Augment model이 어려워하는 task에서는 그나마 knowledge transfer하기 수월한 high-resource domain model로 compose하는게 더 효과적

  - low에서 18/25 CALM win

  - high에서 9/10 CALM win

- Anchor model을 target resource domain에 CL하면 forgetting 때문에 성능 저하가 일어나는것을 high/low 모두에서 확인할 수 있음 (제안한 방법론의 큰 장점)

### 4.3. CODE UNDERSTANDING AND GENERATION

- PaLM-XXS를 github opensrc에서 크롤링한 다양한 프로그래밍 언어에 training → augment model 구축

- 같은 github code의 ~7%를 가지고 CALM을 학습할 D_{C} (=D_{code} )을 구축

- augment: PaLM2-S

- Evaluation Task

  - Code-Completion (CC) (Zero-shot)

Given an initial set of lines of a code, the model is prompted to complete the code snippet.

  - Text-to-Code (T2C) (3-shot)

Given a textual context, the model is prompted to generate the corresponding code snippet.

  - Code-to-Text (C2T) (3-shot)

Given a code snippet, the goal is to generate a natural language explanation of the code.

**#### Results - **Non ENG math grade school word problem. 

{% include figure.liquid loading="eager" path="assets/img/posts/2024-02-13-llm-augmented-llms-expanding-capabilities-through-composition/image_005.png" class="img-fluid rounded z-depth-1" %}

- M_{B}^{Code}은 D_{Code}로  anchor 모델을 직접 학습한 모델

- Augment는 code→code에서 좋은 성능을 (FT의 효과), Anchor는 generalization 능력 덕에 text 이해를 요구하는 영역(T)에서 좋은 성능

- Anchor를 직접 학습한 M_{B}^{Code}가 CALM보다 코드 생성에 좋은 성능을 보여주나 catastrophic forgetting 때문에 모든 언어를 이해하고 텍스트를 생성해야하는 C2T에서 성능이 약화되는 경향을 보여줌.

→ CALM의 장점은 EXPERT 모델 둘을 (SOTA까지 올려가지 않더라도) 성능 깍지 않으면서 generalize하게 쓸 수 있다는데 있어보임 (준원)

### 4.4. Ablations

{% include figure.liquid loading="eager" path="assets/img/posts/2024-02-13-llm-augmented-llms-expanding-capabilities-through-composition/image_006.png" class="img-fluid rounded z-depth-1" %}

- \#>M_{B}: vanilla anchor보다 더 잘한 NTL내 언어개수

- augment model을 vanilla(=only pretrained)model로 변경하거나, random weight model로 대체

  -  vanilla augment model로 대체해도 성능 향상이 어느 정도 있다는 말은

→ unspecialized  model의 capabilities 중 어떤건 anchor model의 capabilities와 orthogonol하다는 것

→ anchor model도 어쩌면 undertrained되었다는 것 (준원)

  - 논문에서는 CALM의 contribution을 새로운 파라미터의 도입이 아니라 augment model의 활용임을 강조

- Encoder의 prefix representation으로 바꿔서 augment model을 활용해봤더니 성능 저하

- 동일한 파라미터 크기를 가지는 LoRA weight을 도입해 D_{C}로 학습한 후 성능을 측정.

  - 대부분의 task에서 LoRA가 성능이 낮음

(준원 뇌피셜)

  - LoRA가 task를 익히기에는 D_{C}랑 end-task랑 설계가 아주 많이 다른데 LoRA는 데이터셋에 맞게 모델 1개 내부의 hidden을 계속 바꿔가니깐 당연히 낮지 않을까?

CALM은 중간중간 필요한 hidden만 바꿔 갈아끼움 (조금 더 유연한 방법론이랄까)

  - computational cost가 훨씬 더 드는데 명시를 안해줬다는 아쉬움.. 이 있다..!

## 5. Conclusion

- Model merge, knowledge distillation등 다양한 분야를 아우르는 논문

- 아이디어 기발하고, soundness.

- parameter count나 computation overhead에 대한 설명이 appendix에 있는데 조금은 아쉽다.

- 위 부분이 해결되면 실용적으로 기여하는 부분이 클것으로 보임.

  - Anchor model: Foundation model

  - Augment model:  proprietary data and knowledge is stored in parametric models
