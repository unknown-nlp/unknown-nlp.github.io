---
categories:
- paper-reviews
date: '2024-09-02 00:00:00'
description: 논문 리뷰 - ICL, Safety 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- alignment
- fine-tuning
- icl
- llm
- paper-review
- safety
thumbnail: assets/img/posts/2024-09-02-many-shot-jailbreaking/thumbnail.jpg
title: Many-shot jailbreaking
---

**논문 정보**
- **Date**: 2024-09-02
- **Reviewer**: 상엽
- **Property**: ICL, Safety

## Introduction

컨텍스트의 길이의 증가 : 4K → 10M

증가 된 컨텍스트는 새로운 공격 방법을 만들어 낼 수 있음: **Many-shot jailbreaking (MSJ)**

→ Few-shot jailbreaking을 Many-shot으로 확장

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-02-many-shot-jailbreaking/image_000.png" class="img-fluid rounded z-depth-1" %}

**MSJ: **Aligned LLM 모델이 일반적으로 거절할 Question-Answer 조합을 Context에 제시 (few → many), 답변해서는 안될 내용에 대해서 답변할 수 있게끔 하는 공격 기법

**Contributions**

- MSJ의 효과성에 대한 검증

- Scaling trends에 대해 분석

- 공격 기법을 완화할 방어 기법에 대한 평가

## Attack Setup

- Generating attack strings

- Attack string formatting

## Empirical Effectiveness of MSJ

평가

- freuquency of successful jailbreaks (refusal classifer (claude 2.0이용, 98%의 정확도))

- Negative log-likelihoods

### 1. Effectiveness of many-shot attacks across tasks

- **Malicious use-cases**: 악의적인 사용 사례, 위에서 정의한 4가지 유형 (유저 중심 평가)

- **Malevolent personality eval**

- Opportunities to insult

**결과**

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-02-many-shot-jailbreaking/image_001.png" class="img-fluid rounded z-depth-1" %}

- 세 가지 모두에서 MSJ가 효과를 보임.

- 토큰을 계속 증가시켜도 효과가 계속 증가함, 비슷하게 계속 NLL이 감소함을 보임.

### 2. **Effectiveness across models**

Figure 2M: 모든 모델에서 효과를 보이는 것을 확인할 수 있었음.

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-02-many-shot-jailbreaking/image_002.png" class="img-fluid rounded z-depth-1" %}

- 싸이코패스같은 반응을 보인 비율: 128개가 되면 모든 모델에 대해서 100%로 수렴

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-02-many-shot-jailbreaking/image_003.png" class="img-fluid rounded z-depth-1" %}

### 3. **Effectiveness across changes in formatting**

- 기존 방식: user/assistant 세팅으로 예제 제시

- Figure 3R: NLL 값 자체에는 큰 영향을 주지만 기울기는 거의 변화가 없음.

- 다른 방식이 더 큰 효과를 보이는 것을 확인할 수 있었음. → 변경된 프롬프트가 alignment fine-tuning 때 사용된 형태가 아니어서 더 취약하지 않을까 추측

### 4. **Robustness to mismatch from target topic**

- **MSJ에서 사용되는 예시를 만들 정도로 지식이 있다면 왜 jailbreaking을 해야하는가?**

- 다른 topic을 활용하는 것에 대한 효과를 검증

- Figure 3L: 타겟 쿼리는 deception

- deception을 제외한 다른 모든 카테고리를 활용할 때 성능이 변화없이 우수함을 확인

- 다른 카테고리에서도 비슷하게 나타남.

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-02-many-shot-jailbreaking/image_004.png" class="img-fluid rounded z-depth-1" %}

→ Many-shot의 다양성 확보를 통해 universial jailbreak가 가능할수도!

### 5. Composition with other jailbreaks

- 다른 jailbreaking 방법과의 결합 시 성능의 변화 → 물론 더 효과적이다!

- 공격 기법

- 위의 공격 기법을 각각의 예시에 추가

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-02-many-shot-jailbreaking/image_005.png" class="img-fluid rounded z-depth-1" %}

- black box setting에서는 확실한 효과를 보임.

- white box setting에서는 # of shots에 따라 다른 효과를 가짐. GCG가 현재 Many-shot 세팅에 최적화되어 있지 않아서 그런듯하다.

→ 전반적으로 jailbreaking 기법과의 결합은 개선된 효과를 보인다고 주장

## Scaling Laws for MSJ

- In context에서 예시의 수와 효과의 관계를 확인

- 필요한 예시의 수와 공격 효과가 power laws를 따름 → 공격 성공을 위해 필요한 예시 수를 파악

### 가설 1. Power laws are ubiquitous in ICL

- MSJ의 메커니즘이 일반적인 ICL의 메커니즘과 비슷할 것이다. (유사한 power law를 보일 것이다.)

- Harmfulness와 무관한 데이터에 대해서 평가

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-02-many-shot-jailbreaking/image_006.png" class="img-fluid rounded z-depth-1" %}

→ 유사한 효과를 보임. MSJ는 ICL의 효과와 관련성이 있다.

**Beyond Standard Power Laws!**

- Bounded power law scaling

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-02-many-shot-jailbreaking/image_007.png" class="img-fluid rounded z-depth-1" %}

- 모델 크기와도 결합한 Double scaling laws도 제시

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-02-many-shot-jailbreaking/image_008.png" class="img-fluid rounded z-depth-1" %}

### **가설 2: Dependence of power laws on model size**

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-02-many-shot-jailbreaking/image_009.png" class="img-fluid rounded z-depth-1" %}

- Claude 2.0 family에 실험 진행

- 더 큰 모델이 더 적은 sample을 필요로 한다. → 큰 모델이 MSJ에 더 취약하다.

## Understanding Mitigations Against MSJ

- 방어기법에 대해서 연구, power law의 관점에서 절편과 기울기를 판단

### Mitigating via alignment finetuning

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-02-many-shot-jailbreaking/image_010.png" class="img-fluid rounded z-depth-1" %}

- 일반적인 LLM alignment 방식인 Supervised fine-tuning과 RL을 scaling하면 개선이 될까?

- 절편은 증가하지만 기울기는 변화를 주지 못함. (zero-shot 공격에 대해서는 방어하지만 MSJ의 효과를 막지 못함.)

- 해당 방법의 절편 감소는 Examples의 증가를 의미하긴 하지만 다른 공격 방식들과 결합 시 (다른 jailbreaking 사용, Q/A로 변경 등) 절편을 내리는 효과를 보인 공격들이 있음.

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-02-many-shot-jailbreaking/image_011.png" class="img-fluid rounded z-depth-1" %}

- 학습 데이터를 MSJ의 방어에 맞춰 변화를 주면 효과적일 것인가?

- 실험은 30-shot MSJ까지만 실험 (전체적으로 예시의 수가 줄었음.)

**공통점**: Supervised fine-tuning & RL 

- 절편은 변화시키지만 기울기 변화는 역시 없다. (MSJ에 대한 효과가 없다고 볼 수 있다.)

### Prompt-Based Mitigations

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-02-many-shot-jailbreaking/image_012.png" class="img-fluid rounded z-depth-1" %}

- ICD: 유해한 질문에 대한 거절 예시 (20개) 추가

- CWD: 어시스턴트 모델이 jailbreaking하지 않도록 경고하는 텍스를 앞 뒤에 추가.
