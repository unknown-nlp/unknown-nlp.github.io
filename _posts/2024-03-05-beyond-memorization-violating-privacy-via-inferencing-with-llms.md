---
categories:
  - paper-reviews
date: "2024-03-05 00:00:00"
description: 논문 리뷰 - Prompt Tuning, Inference 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
  - alignment
  - gpt
  - inference
  - llm
  - paper-review
  - pre-training
  - prompt tuning
  - reasoning
  - rlhf
thumbnail: assets/img/posts/2024-03-05-beyond-memorization-violating-privacy-via-inferencing-with-llms/thumbnail.jpg
title: "Beyond Memorization: Violating Privacy Via Inferencing With LLMs"
---

**논문 정보**

- **Date**: 2024-03-05
- **Reviewer**: 준원 장
- **Property**: Prompt Tuning, Inference

## 1. Introduction

{% include figure.liquid loading="eager" path="assets/img/posts/2024-03-05-beyond-memorization-violating-privacy-via-inferencing-with-llms/image_000.png" class="img-fluid rounded z-depth-1" %}

**#### Privacy Violations through LLM Inference**

- LLM이 pre-training때 직접적으로 학습하지 않는 user-written text들을 inference만 함으로써 특정 User의 신상정보(Attributes)를 추적할 수 있는 가능성을 제기한 논문

- 무거울 수도 있고, 아직은 현실과는 동떨어져 보이는 이야기지만 미국 인구의 1/2은 위치, 성별, 생년월일과 같은 일부의 attribute로 고유하게 식별가능하다고 알려져 있는 이 시점에서, 악의적인 행위자가 게시물에서 추론한 고도의 개인 정보(예: 정신 건강 상태) → 실제 사람과 연결하여 표적 정치 캠페인, 자동화된 프로파일링 또는 스토킹과 같은 바람직하지 않거나 불법적인 활동에 사용할 수 있다.

- 이 연구에서는 단순 LLM의 Inference Capabilities만으로 User의 Privacy 정보가 노출되는 task를 처음으로 fomalization하고, providie/client의 기존 defensing 방법들이 완전한 해결책이 되지 않음을 실험결과로 보여줌.

** #### 준원 생각**

- 2020-2021까지 오랜 숙명이었던 Natural Language Generation이 Scale-Up 기반 BlackBox LLM 형태로 어느정도 완성이 되었다. (+SFT + RLHF)

- 이제 Provider/Client 양측 모두 LLM을 원하는 목적에 맞게 쓰기 위해서는 LLM의 Natural Language UnderStanding에 대한 논의가 더 이루어져야하지 않을까?

## 2. Related Works

### Privacy Leakage in LLMs

- 기존의 LLMs에서 Privacy Leakage Issue는 주로 pre-training data memorization 측면에서 다루어져 왔었음

- Carlini et al. (2023)에 따르면 memorization, model size, training data repetitions에는 log-linear 관계가 있음.

→ 기존에는 privacy leakage를 신경써야하는 source가 pt data라면 이 연구에서는 inference때 LM이 직면하는 data의 privacy leakage도 신경써야함을 주장.

### Risk of LLMs

- 개인정보 침해 외에도 risk mitigation (how to i create bomb에 대한 대답)을 위한 가장 대표적인 방법은 model alignment이다.

### Personal Data PII (Personal Identifiable Information)

→ 논문에서 Inference를 통해서 Personal Attribute를 Atttacking해본다 했는데, global하게 많이 쓰이는 정의들을 논문에서 reference로 제시한다.

- General Data Protection Regulation (GDPR) - EU

- Personal Identifiable Information (PII) - U.S.

→ 저자들 여기서 수집한 데이터 가능한 다 수집하려고 함

### Author Profiling

- written text로 부터 auther attribute를 추적하는 task (나름 전통 있는 task 같음)

- 문제: lack of available datasets, 가장 유명한게 twitter기반 PAN dataset인데 text당 attribute 1-3개.

## 3. THREAT MODELS

→ 2가지 Inference setting을 상정하고 User Privacy Attack 실험을 진행

### FREE TEXT INFERENCE (A1)

- (u, t) ∈ D → (attribute, value)

- P\_{A_1} (t) = (S, P)

→ Output과 reasoning 요청

### ADVERSARIAL INTERACTION (A)

{% include figure.liquid loading="eager" path="assets/img/posts/2024-03-05-beyond-memorization-violating-privacy-via-inferencing-with-llms/image_001.png" class="img-fluid rounded z-depth-1" %}

- (논문에서 설명이 부족하긴 하지만) Persona적으로 무해해보이는 Role을 부여받은 chat-bot이 사용자와 계속 대화를 이어나가면서 뒤에서는 걔속해서 잠재적으로 민감한 정보를 학습할 수 있는 텍스트를 생성하도록 유도

- T\_{p} : public task of the LLM, e.g., “being a helpful travel assistant”

- T\_{h} : hidden task of the LLM, e.g., “trying to extract private information from the user”

- m*{i} > r*{i}^{h} : a user message > a hidden model response to the model hosting entity (e.g., PII inferences from prior responses)

- m*{i} > r*{i}^{p} : a user message > a public model response revealed to the user

→ chatbot platform 모방해서 실험진행

→ Output과 reasoning 요청

## 4. Dataset

→ 직접 데이터셋 구축함. 고려할때 중요하게 생각한 조건은 다음 2가지임

(1) 온라인상 text여야함 (익명의 한 user가 online상에서 남긴 글들을 inference해서 특정화할 수 있다는게 이 글의 contribution이기에)

(2) 한 text상에서 여러 attribute가 들어나는 text를 target source로 함

⇒ reddit!!

### The PersonalReddit Dataset

- 520 randomly sampled public Reddit profiles (user 수)

- 저자들이 직접 속성에 대해서 labeling을 진행 (extract attribute)

- Perceived certainity & Hardness도 labeling

- Decontamination 진행

→ Perceived Certainity ≥ 3 이상 dataset 가지고 실험 진행 (This resulted in 1066 (down from 1184) individual labels across all 520 profiles.)

{% include figure.liquid loading="eager" path="assets/img/posts/2024-03-05-beyond-memorization-violating-privacy-via-inferencing-with-llms/image_002.png" class="img-fluid rounded z-depth-1" %}

## 5. Evaluation

**#### FREE TEXT INFERENCE **

{% include figure.liquid loading="eager" path="assets/img/posts/2024-03-05-beyond-memorization-violating-privacy-via-inferencing-with-llms/image_003.png" class="img-fluid rounded z-depth-1" %}

- GPT-4의 경우 top-1으로만 비교했을때 전체 attributes에 대해서 84.6% 정도 ACC를 보임.

- 논문에서 강조하는 점은 인간은 (1) Internet에 무한정으로 access (2) 다른 하위 reddit 검색 (meta data)도 참고해서 attribute를 추출해낸데에 반면 GPT-4는 text 정보만으로 상당히 유의미한 개별정보를 식별해낼 수 있다는 거에 의의를 두고 있다.

- 이 분야 역시 Scale Law가 강하게 적용되는 분야

{% include figure.liquid loading="eager" path="assets/img/posts/2024-03-05-beyond-memorization-violating-privacy-via-inferencing-with-llms/image_004.png" class="img-fluid rounded z-depth-1" %}

- 개별 attribute로 보았을때 GPT-4는 SEX나 PLACE_OF_BIRTH는 97% and 92% 사람들이 온라인 상에 올린 정보만으로는 쉽게 추적.

- INCOME이 TOP-1에서는 62.5%로 낮게 보이는데 (이거 구간 예측임), TOPP-2로 범위 확장하면 87% 정확도를 보임

**#### Adversarial Information**

{% include figure.liquid loading="eager" path="assets/img/posts/2024-03-05-beyond-memorization-violating-privacy-via-inferencing-with-llms/image_005.png" class="img-fluid rounded z-depth-1" %}

- **GPT-4를 이용해서 20개 User example을 활용해 224 interactions run**

- **User bots are specifically instructed to not reveal any of the private information.**

- Location/Age/SEX attribute에 대해서 평가

## 6. EVALUATION OF CURRENT MITIGATIONS

→ 2가지 방어기법이 inference privacy leakage를 잘 방어하는지 확인하는 실험 진행

### Client-Side Anonymization

{% include figure.liquid loading="eager" path="assets/img/posts/2024-03-05-beyond-memorization-violating-privacy-via-inferencing-with-llms/image_006.png" class="img-fluid rounded z-depth-1" %}

- AzureLanguageService를 활용해 user attribute를 \*\*\*로 anonymize 하는 것

- AzureLanguageService에 의해서 지원되는 location, age, occupation, place of birth, and income에 대해서만 anonymize 하고 inference시에 privacy leakage가 발생하는지 확인

{% include figure.liquid loading="eager" path="assets/img/posts/2024-03-05-beyond-memorization-violating-privacy-via-inferencing-with-llms/image_007.png" class="img-fluid rounded z-depth-1" %}

→ Location의 경우 지역과 관련된 mention을 text에서 전부 제거했는데도 ∼ 55%정도의 top-1 ACC 성능을 보임..

→ Personal Attribute가 실제 text에 명시적으로 언급되어 있지 않지만 현재 단순히 masking하는 도구가 커버하지 못하는 다른 context로부터 LLM이 어느정도는 추론가능하다는걸 실험적으로 밝힘.

### Provider-Side Alignment

- (alignment tuning=RLHF한) 모델이 논문에서 제시한 promtp를 reject하고 답변하지 않을 확률
