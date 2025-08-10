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

- Model Merging

- Model and Task Compositionality

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

### Modeling

#### Main Target: D_{C} 를 가지고 composition target domain에 대해서 학습

- Augmenting model에서 Layer |L_{A}| = N_{A}=n개 선정

- Anchor model에서 Layer |L_{B}| = N_{B}=n개 선정

- Layer개수는 각 Model에서 선정된 Layer들간 간격이 일정하도록

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

- 실험은 기본적으로 다음의 틀을 따름

### 4.1.  KEY-VALUE ARITHMETIC

-  PaLM-XXS에 있는 25K vocab(2-6chars)을 [1, 25K] INT로 mapping한 Key-value pair 구축

- 3-6 keys에 대해서 addition (+), subtraction (−), and multiplication (×) 연산 수행

- 3개 데이터셋 구축

(1) KV-Substitution (D_KV-SUBS) : mapping  

(2) KV-Arithmetic (D_KV-MATH) : mapping & arithmetic 

(3) Numeric-Arithmetic (D_NUM-MATH): arithmetic

**#### Results**

{% include figure.liquid loading="eager" path="assets/img/posts/2024-02-13-llm-augmented-llms-expanding-capabilities-through-composition/image_002.png" class="img-fluid rounded z-depth-1" %}

- KV-Substitution를 학습하지 못한 Anchor는 아예 풀지 못하는 경향성을 보임, 반면 연산은 어느정도 수행함.

- CALM으로 KV-Substitution에 어느정도 fitting된 model의 도움을 받아 KV-Substitution을 조금만 학습하면 각 모델의 장점을 활용해서 composition target domain에서 좋은 성능을 보임.

### 4.2. LOW-RESOURCE LANGUAGE INCLUSIVITY

-  PaLM-XXS를 Next Thousand Languages (NTL)에 있는 low-resource language에 training → augment model 구축

- 같은 low-resource language의 ~5%를 가지고 CALM을 학습할 D_{C} (=D_{NTL} )을 구축

- Evaluation Task

**#### Results - t**ranslation Non ENG > ENG (5shot)

{% include figure.liquid loading="eager" path="assets/img/posts/2024-02-13-llm-augmented-llms-expanding-capabilities-through-composition/image_003.png" class="img-fluid rounded z-depth-1" %}

- M_{B}^{NTL}은 D_{NTL}로  anchor 모델을 직접 학습한 모델

-  아직 anchor모델을 직접 continual pre-training했을때 비해서 성능이 좋지는 못하나, 적은 trainable parameter로는 좋은 성능을 보여줌

- 175/192에서 augment model (애매하게 작성했는데 D_{NTL}로 학습한거 아닌거 같음)보다 성능 향상있었다고 함.

- 논문에 computational cost에 대한 비교나 설명을 명확하게 이야기 안해줬다는 아쉬움…!

**#### Results - **Non ENG math grade school word problem. 

{% include figure.liquid loading="eager" path="assets/img/posts/2024-02-13-llm-augmented-llms-expanding-capabilities-through-composition/image_004.png" class="img-fluid rounded z-depth-1" %}

- Augment model이 어려워하는 task에서는 그나마 knowledge transfer하기 수월한 high-resource domain model로 compose하는게 더 효과적

- Anchor model을 target resource domain에 CL하면 forgetting 때문에 성능 저하가 일어나는것을 high/low 모두에서 확인할 수 있음 (제안한 방법론의 큰 장점)

### 4.3. CODE UNDERSTANDING AND GENERATION

- PaLM-XXS를 github opensrc에서 크롤링한 다양한 프로그래밍 언어에 training → augment model 구축

- 같은 github code의 ~7%를 가지고 CALM을 학습할 D_{C} (=D_{code} )을 구축

- augment: PaLM2-S

- Evaluation Task

**#### Results - **Non ENG math grade school word problem. 

{% include figure.liquid loading="eager" path="assets/img/posts/2024-02-13-llm-augmented-llms-expanding-capabilities-through-composition/image_005.png" class="img-fluid rounded z-depth-1" %}

- M_{B}^{Code}은 D_{Code}로  anchor 모델을 직접 학습한 모델

- Augment는 code→code에서 좋은 성능을 (FT의 효과), Anchor는 generalization 능력 덕에 text 이해를 요구하는 영역(T)에서 좋은 성능
