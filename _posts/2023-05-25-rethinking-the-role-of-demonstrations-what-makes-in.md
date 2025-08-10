---
categories:
- paper-reviews
date: '2023-05-25 00:00:00'
description: 논문 리뷰 - LLM, ICL 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- icl
- language-model
- llm
- paper-review
thumbnail: assets/img/posts/2023-05-25-rethinking-the-role-of-demonstrations-what-makes-in/thumbnail.jpg
title: 'Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?'
---

**논문 정보**
- **Date**: 2023-05-25
- **Reviewer**: 건우 김
- **Property**: LLM, ICL

# Abstract

Large language models (LLMs)들이 in-context learning을 통해 downstream task에서 좋은 성능을 보인다는 사실은 유명하지만, model이 ***어떻게 ***학습을 하고 ***어떤 점***을 통해 성능을 내는지 확인하는 연구는 거의 없다. 본 논문에서 다양한 실험을 통해 처음으로 LLMs의 in-context learning이 ***어떻게 ***그리고 ***왜*** 작동을 하는 지에 대해서 수많은 실험을 통해 보여준다.

- **Key Aspects**

# Introduction

- LLMs은 few input-label pairs를 가지고 In-contex learning (ICL)을 통해 downstream tasks에서 꽤나 높은 성능을 보여줬지만, ***ICL이 왜 작동하고 어떻게 작동을 하는 지***에 대한 연구는 거의 없다.

{% include figure.liquid loading="eager" path="assets/img/posts/2023-05-25-rethinking-the-role-of-demonstrations-what-makes-in/image_000.png" class="img-fluid rounded z-depth-1" %}

- ground turth demonstration이 실제로 ICL에 효과적이지 않음을 실험적으로 보임

{% include figure.liquid loading="eager" path="assets/img/posts/2023-05-25-rethinking-the-role-of-demonstrations-what-makes-in/image_001.png" class="img-fluid rounded z-depth-1" %}

- Demonstations의 어느 부분이 performance에 직접적인 기여를 하는지 알아보는 실험을 진행

- 본 논문에서 ICL에 사용되는 ***demonstration***의 역할에 대해 이해하는 분석을 제시함.

# Related works

- LLMs, ICL 내용 생략

- 본 논문에서 처음으로 ICL이 zero-shot 보다 왜 성능이 좋게 나오는지 실험적으로 분석함

# Experimental Setup

- **Models**:  6 종류의 LM을 사용함 (only-decoder model)

# 1. Ground Truth Matters Little

### Gold labels vs Random labels

- **No demonstration**s: zero-shot setting

- **Demonstrations w/ gold labels**: ICL with *k *labeled examples

- **Demonstrations w/ ranodm lables**: ICL with *k* labeled examples (gold → random labels), 여기서 사용한 random labels이란 gold label과 동일한 set을 공유하고 있음. (완전 random 아님x)

{% include figure.liquid loading="eager" path="assets/img/posts/2023-05-25-rethinking-the-role-of-demonstrations-what-makes-in/image_002.png" class="img-fluid rounded z-depth-1" %}

- **Results and analysis**

### Ablations

- **Does the number of correct labels matter?**

- **Is the result consistent with varying k?**

- **Is the result consistent with better templates?**

# 2. Why *does *In-Context Learning work?

- 위에 실험에서 demonstration에서 GT input-label이 ICL의 performance gain에 큰 영향이 없는 것을 보여줌. 이번 실험에서 demonstrations에서 다른 어떤 요소들이 ICL의 performance gain에 영향을 주는지 확인.

{% include figure.liquid loading="eager" path="assets/img/posts/2023-05-25-rethinking-the-role-of-demonstrations-what-makes-in/image_003.png" class="img-fluid rounded z-depth-1" %}

- **Demonstraion의 4가지 aspects**

### Impact of the distribtuion of the input text

- out-of-domain distribtuion demonstrations 상황에서 실험

- **Results**

### Impact of the label space

- k개의 labels을 random한 English word를 사용해서 실험을 진행함. 

- **Results**

### Impact of input-label pairing

- Format의 형태를 바꿔가며 실험을 진행함. inputs과 labels의 pairing을 없애는 식으로 작은 변화만 줘서 format의 형태를 바꿈.

- **Results**

### Impact of meta-training

- 다른 models들과 다르게 MetaICL은 ICL을 목적 함수로 두어 학습시킨 모델이다.

# Discussion

### Does the model learn at test time?

- Learning의 대한 엄밀한 정의를 다음과 같이 두면, ‘caputring the input-label correspondence given in the training data’

- Learning을 넓은 의미로 해석하면

### Capacity of LMs

- model은 input-label demonstration에 의존하지 않으며 downstream task를 수행한 것을 실험에서 보임. 이를 통해 input-label correspondence 자체를 langauge modeling (pretraining)할 때 학습을 한 것으로 볼 수 있음. 

### Connection to instruction-following models

- (Instruction) natural language로 문제 설명을 설명하면 inference 과정에서 새로운 task를 수행 할 수 있다는 이전 연구들이 존재. → Demonstrations과 Instruction은 LM에게 있어 비슷한 역할 수행

- Instruction은 model로 하여금 model 갖고있는 capacity를 끌어올리는 것을 촉진 시킬 수는 있지만, 새로운 task를 학습 시키지는 못함.
