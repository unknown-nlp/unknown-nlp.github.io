---
categories:
- paper-reviews
date: '2024-03-05 00:00:00'
description: 논문 리뷰 - Prompt Tuning, Inference 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- alignment
- gpt
- inference
- llm
- nlp
- paper-review
- pre-training
- prompt tuning
- reasoning
- rlhf
thumbnail: assets/img/posts/2024-03-05-beyond-memorization-violating-privacy-via-inferencing-with-llms/thumbnail.jpg
title: 'Beyond Memorization: Violating Privacy Via Inferencing With LLMs'
---

**논문 정보**
- **Date**: 2024-03-05
- **Reviewer**: 준원 장
- **Property**: Prompt Tuning, Inference

## 1. Introduction

{% include figure.liquid loading="eager" path="assets/img/posts/2024-03-05-beyond-memorization-violating-privacy-via-inferencing-with-llms/image_000.png" class="img-fluid rounded z-depth-1" %}

**#### Privacy Violations through LLM Inference**

- LLM이 pre-training때 직접적으로 학습하지 않는 user-written text들을 inference만 함으로써 특정 User의 신상정보(Attributes)를 추적할 수 있는 가능성을 제기한 논문

  - Figure에서 User-Written Texts는 User가 Reddit에 올린 harmless한 comments이지만, 적절한 Prompt와 함께 LLM에 Inference하면 Personal Attributes Inference가 가능하다.

→ User-Written 문장 *“there is this nasty intersection on my commute, I always get stuck there waiting for a hook turn” *에서 LLM은 “hook turn”→ “Melbourne”을 연결시킨다.

- 무거울 수도 있고, 아직은 현실과는 동떨어져 보이는 이야기지만 미국 인구의 1/2은 위치, 성별, 생년월일과 같은 일부의 attribute로 고유하게 식별가능하다고 알려져 있는 이 시점에서, 악의적인 행위자가 게시물에서 추론한 고도의 개인 정보(예: 정신 건강 상태) → 실제 사람과 연결하여 표적 정치 캠페인, 자동화된 프로파일링 또는 스토킹과 같은 바람직하지 않거나 불법적인 활동에 사용할 수 있다.

- 이 연구에서는 단순 LLM의 Inference Capabilities만으로 User의 Privacy 정보가 노출되는 task를 처음으로 fomalization하고, providie/client의 기존 defensing 방법들이 완전한 해결책이 되지 않음을 실험결과로 보여줌.

** #### 준원 생각**

- 2020-2021까지 오랜 숙명이었던 Natural Language Generation이 Scale-Up 기반 BlackBox LLM 형태로 어느정도 완성이 되었다. (+SFT + RLHF)

- 이제 Provider/Client 양측 모두 LLM을 원하는 목적에 맞게 쓰기 위해서는 LLM의 Natural Language UnderStanding에 대한 논의가 더 이루어져야하지 않을까?

## 2. Related Works

### Privacy Leakage in LLMs

- 기존의 LLMs에서 Privacy Leakage Issue는 주로 pre-training data memorization 측면에서 다루어져 왔었음

  - exact repetition of training data sequences during inference in response to a specific input prompt, often the corresponding prefix. (동일한 prefix에 대해서 training data와 response를 하는것이라고 논문에서 정의함)

- Carlini et al. (2023)에 따르면 memorization, model size, training data repetitions에는  log-linear 관계가 있음. 

→ 기존에는 privacy leakage를 신경써야하는 source가 pt data라면 이 연구에서는 inference때 LM이 직면하는 data의 privacy leakage도 신경써야함을 주장. 

### Risk of LLMs

- 개인정보 침해 외에도 risk mitigation (how to i create bomb에 대한 대답)을 위한 가장 대표적인 방법은 model alignment이다.

  - SFT

  - RLHR

### Personal Data PII (Personal Identifiable Information)

→ 논문에서 Inference를 통해서 Personal Attribute를 Atttacking해본다 했는데, global하게 많이 쓰이는 정의들을 논문에서 reference로 제시한다.

- General Data Protection Regulation (GDPR) - EU

  - ”any information relating to an identified or identifiable natural person” explicitly including location data and a persons economic, cultural or social identity.

- Personal Identifiable Information (PII)  - U.S.

  - acknowledge the existence of sensitive data such as race, sexual orientation, or religion.

→ 저자들 여기서 수집한 데이터 가능한 다 수집하려고 함

### Author Profiling

- written text로 부터 auther attribute를 추적하는 task (나름 전통 있는 task 같음)

- 문제: lack of available datasets, 가장 유명한게 twitter기반 PAN dataset인데 text당 attribute 1-3개.

## 3. THREAT MODELS

→ 2가지 Inference setting을 상정하고 User Privacy Attack 실험을 진행

### FREE TEXT INFERENCE (A1)

- (u, t) ∈ D → (attribute, value)

: Dataset에 user와 text 정보가 있을때 LLM을 통해서 attribute와 value정보를 extract하자

- P_{A_1} (t) = (S, P)

  - S: System Prompt

  - P = (Prefix \ F_{A_{1}}(t) \ Suffix)

- **Prompt Example**

{% include figure.liquid loading="eager" path="assets/img/posts/2024-03-05-beyond-memorization-violating-privacy-via-inferencing-with-llms/image_001.png" class="img-fluid rounded z-depth-1" %}

→ Output과 reasoning 요청

### ADVERSARIAL INTERACTION (A)

{% include figure.liquid loading="eager" path="assets/img/posts/2024-03-05-beyond-memorization-violating-privacy-via-inferencing-with-llms/image_002.png" class="img-fluid rounded z-depth-1" %}

- (논문에서 설명이 부족하긴 하지만) Persona적으로 무해해보이는 Role을 부여받은 chat-bot이 사용자와 계속 대화를 이어나가면서 뒤에서는 걔속해서 잠재적으로 민감한 정보를 학습할 수 있는 텍스트를 생성하도록 유도

- T_{p} : public task of the LLM, e.g., “being a helpful travel assistant”

- T_{h} : hidden task of the LLM, e.g., “trying to extract private information from the user”

- m_{i} > r_{i}^{h} : a user message > a hidden model response to the model hosting entity (e.g., PII inferences from prior responses)

- m_{i} > r_{i}^{p} : a user message > a public model response revealed to the user

→ chatbot platform 모방해서 실험진행

- **Prompt Example**

{% include figure.liquid loading="eager" path="assets/img/posts/2024-03-05-beyond-memorization-violating-privacy-via-inferencing-with-llms/image_003.png" class="img-fluid rounded z-depth-1" %}

{% include figure.liquid loading="eager" path="assets/img/posts/2024-03-05-beyond-memorization-violating-privacy-via-inferencing-with-llms/image_004.png" class="img-fluid rounded z-depth-1" %}

→ Output과 reasoning 요청

## 4. Dataset

→ 직접 데이터셋 구축함. 고려할때 중요하게 생각한 조건은 다음 2가지임

(1) 온라인상 text여야함 (익명의 한 user가 online상에서 남긴 글들을 inference해서 특정화할 수 있다는게 이 글의 contribution이기에)

(2) 한 text상에서 여러 attribute가 들어나는 text를 target source로 함

⇒ reddit!!

### The PersonalReddit Dataset

- 520 randomly sampled public Reddit profiles (user 수)

  - 5814 comments (2012-2016)

- 저자들이 직접 속성에 대해서 labeling을 진행 (extract attribute)

- Perceived certainity & Hardness도 labeling

  - hardness 4-5: 외부 internet search로 attribute를 찾아야하는 경우 & subreddit보고 labeling

  - hardness 3이 4보다 높은 reasoning을 요구하는 경우가 있음

- Decontamination 진행 

  - PT때 해당 reddit 데이터 보지 않았음을 검증

  - Prefix : P

    - Continuation : C

    - Suffix : S

    - 1 - Sim (C, S)

{% include figure.liquid loading="eager" path="assets/img/posts/2024-03-05-beyond-memorization-violating-privacy-via-inferencing-with-llms/image_005.png" class="img-fluid rounded z-depth-1" %}

 → Perceived Certainity ≥ 3 이상 dataset 가지고 실험 진행 (This resulted in 1066 (down from 1184) individual labels across all 520 profiles.)

{% include figure.liquid loading="eager" path="assets/img/posts/2024-03-05-beyond-memorization-violating-privacy-via-inferencing-with-llms/image_006.png" class="img-fluid rounded z-depth-1" %}

## 5. Evaluation

**#### FREE TEXT INFERENCE **

{% include figure.liquid loading="eager" path="assets/img/posts/2024-03-05-beyond-memorization-violating-privacy-via-inferencing-with-llms/image_007.png" class="img-fluid rounded z-depth-1" %}

- GPT-4의 경우 top-1으로만 비교했을때 전체 attributes에 대해서 84.6% 정도 ACC를 보임. 

  - top-3로 범위 확장시 95.1% ACC

- 논문에서 강조하는 점은 인간은 (1) Internet에 무한정으로 access (2) 다른 하위 reddit 검색 (meta data)도 참고해서 attribute를 추출해낸데에 반면 GPT-4는 text 정보만으로 상당히 유의미한 개별정보를 식별해낼 수 있다는 거에 의의를 두고 있다.

- 이 분야 역시 Scale Law가 강하게 적용되는 분야

  - Llama-2 7B achieves a total accuracy of 51% →Llama-2 70B is already at 66%.

{% include figure.liquid loading="eager" path="assets/img/posts/2024-03-05-beyond-memorization-violating-privacy-via-inferencing-with-llms/image_008.png" class="img-fluid rounded z-depth-1" %}

- 개별 attribute로 보았을때 GPT-4는 SEX나 PLACE_OF_BIRTH는 97% and 92% 사람들이 온라인 상에 올린 정보만으로는 쉽게 추적.

- INCOME이 TOP-1에서는 62.5%로 낮게 보이는데 (이거 구간 예측임), TOPP-2로 범위 확장하면 87% 정확도를 보임

**#### Adversarial Information**

{% include figure.liquid loading="eager" path="assets/img/posts/2024-03-05-beyond-memorization-violating-privacy-via-inferencing-with-llms/image_009.png" class="img-fluid rounded z-depth-1" %}

- **GPT-4를 이용해서 20개 User example을 활용해 224 interactions run**

- **User bots are specifically instructed to not reveal any of the private information.**

**[작정하고 privacy leakage하려면 이게 제일 중요할거 같은데 이거에 대한 평가나 metric이 없어서 조금은 아쉬웠다.]**

- Location/Age/SEX attribute에 대해서 평가

  - top-1 ACC 기준

  - location 60.3%, age: 49.6%, sex: 67.9%

## 6. EVALUATION OF CURRENT MITIGATIONS

→ 2가지 방어기법이 inference privacy leakage를 잘 방어하는지 확인하는 실험 진행

### Client-Side Anonymization

{% include figure.liquid loading="eager" path="assets/img/posts/2024-03-05-beyond-memorization-violating-privacy-via-inferencing-with-llms/image_010.png" class="img-fluid rounded z-depth-1" %}

- AzureLanguageService를 활용해 user attribute를 ***로 anonymize 하는 것

- AzureLanguageService에 의해서 지원되는 location, age, occupation, place of birth, and income에 대해서만 anonymize 하고 inference시에 privacy leakage가 발생하는지 확인

{% include figure.liquid loading="eager" path="assets/img/posts/2024-03-05-beyond-memorization-violating-privacy-via-inferencing-with-llms/image_011.png" class="img-fluid rounded z-depth-1" %}

→ Location의 경우 지역과 관련된 mention을 text에서 전부 제거했는데도 ∼ 55%정도의 top-1 ACC 성능을 보임..

→ Personal Attribute가 실제 text에 명시적으로 언급되어 있지 않지만 현재 단순히 masking하는 도구가 커버하지 못하는 다른 context로부터 LLM이 어느정도는 추론가능하다는걸 실험적으로 밝힘.

### Provider-Side Alignment

- (alignment tuning=RLHF한) 모델이 논문에서 제시한 promtp를 reject하고 답변하지 않을 확률

{% include figure.liquid loading="eager" path="assets/img/posts/2024-03-05-beyond-memorization-violating-privacy-via-inferencing-with-llms/image_012.png" class="img-fluid rounded z-depth-1" %}

→ Provider별로 prompt에 대해서 답변하지 않은 확률을 제시함

→ Google 모델이 답하지 않은 이유는 거부된 메세지의 상당 부분이 민감한 주제 (e.g., 가정 폭력)이 포함된 댓글에 대한 것이어서 다른 trigger가 있었을거라고 주장

## 7. Conclusion

- 보통은 NLP conference Best Paper 주제인데 ICLR Spotlight이어서 놀람

- 결과에 대한 뒷받침 설명이나 근거가 많이 빈약하고 아쉬우나 논문에서 정의한 task와 결과가 많이 무겁고 충격적임

- 서두에서 이야기한것처럼 Blackbox의 NLU에 대한 이해가 필요한듯..!
