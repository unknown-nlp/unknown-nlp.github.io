---
categories:
- paper-reviews
date: '2025-03-11 00:00:00'
description: 논문 리뷰
giscus_comments: true
layout: post
related_posts: false
tags:
- attention
- classification
- fine-tuning
- llm
- paper-review
- transformer
thumbnail: assets/img/posts/2025-03-11-when-is-task-vector-provably-effective-for-model/thumbnail.jpg
title: 'WHEN IS TASK VECTOR Provably EFFECTIVE FOR MODEL EDITING? A GENERALIZATION
  ANALYSIS OF

  NONLINEAR TRANSFORMERS'
---

**논문 정보**
- **Date**: 2025-03-11
- **Reviewer**: hyowon Cho

# 1. Intro

LLM의 학습 연산 및 메모리 비용 문제를 해결하기 위한 방법론으로 대표적인 것은 PEFT이지만, 간혹 Task Vector를 이용한 접근법들이 등장하고 있다. 

태스크 벡터 기법은 다음과 같이 작동한다:

1. **단순한 태스크에서 사전 학습 모델을 미세 조정하여 태스크 벡터를 생성** → 이는 미세 조정된 모델과 사전 학습 모델 간의 가중치 차이를 나타냄.

1. **보다 복잡한 태스크를 처리하기 위해 여러 태스크 벡터를 선형 조합하여 모델을 수정** → 복잡한 태스크에 대한 추가 미세 조정 없이 효율적인 적응이 가능함.

이 방법은 **선형 조합만으로도 다양한 다운스트림 태스크에 적응할 수 있는 장점**이 있으며, 다음과 같은 특성을 보인다:

- **태스크 벡터 추가** → 해당 태스크 성능 향상

- **태스크 벡터 제거** → 특정 태스크의 지식 제거 (unlearning)

- **적절한 조합** → 라벨 데이터 없이도 유사한 관계를 가진 새로운 태스크(out-of-domain task)에 일반화 가능

- 또한, **저차원(low-rank) 또는 희소(sparse) 태스크 벡터를 사용하면 성능을 유지하면서도 효율성을 더욱 향상**할 수 있음

태스크 벡터의 실용적 성공에도 불구하고, 이에 대한 **이론적 분석은 아직 충분하지 않음**. 특히, 다음과 같은 질문이 제기된다:

> 태스크 벡터가 멀티태스크 학습, unlearning, 및 out-of-domain generalization를** *****언제, 왜*** 성공적으로 수행할 수 있는가?

오늘 소개할 논문은 **비선형 Transformer 모델에서 태스크 벡터(task arithmetic)의 이론적 일반화 분석을 최초로 수행**하며, multi-task learning, unlearning, out-of-domain generalization에 대한 이론적 근거를 제공한다. 

특히, **binary classification 태스크**를 대상으로 태스크 벡터 효과가 산술적 하이퍼파라미터(arithmetic hyperparameters)에 어떻게 의존하는지를 정량적으로 분석한다. 

비록 분석은 **단순화된 단일 헤드(single-head) 및 단일 층(one-layer) 비선형 Transformer**을 기반으로 하지만, 이론적 통찰은 실제 아키텍처에서도 검증된다. 

(건우 연구에 태스크 벡터가 활용된다고 들어서, 선행 연구 참고용으로 가져왔습니다🙌)

논문의 contribution은 다음과 같다:

1. task addition 및 task negation에 대한 세밀한 특성 학습 분석

1. 태스크 벡터를 활용한 out-of-domain generalization에 대한 최초의 이론적 보장 제공

1. 태스크 벡터의 low-rank approximation 및 magnitude-based pruning에 대한 이론적 정당화

## Related Works

### **Weight interpolation technique**

- 가중치 보간 또는 모델 병합(model merging)은 여러 모델의 가중치를 선형적으로 보간(interpolation) 하는 기법

- 이 기법은 서로 다른 다운스트림 태스크에서 미세 조정된 모델 또는 다른 하이퍼파라미터로 학습된 모델을 병합하는 방법으로 활용됨 (model soups)

- 실험적으로, 가중치 보간은 모델을 더 넓은 최적점(wider optima)으로 유도하여 일반화 성능을 향상할 수 있으며 단일 태스크(single-task) 및 멀티태스크(multi-task) 성능에서 기존 미세 조정(fine-tuning) 방법을 능가할 수도 있음.

- 태스크 벡터 접근법은 이러한 가중치 보간의 특수한 형태로 볼 수 있으며, 태스크 벡터에 대한 선형 연산(linear operations)을 수행하는 방식.

### **Feature learning analysis for Transformers**.

- 최근 연구들은 Transformer의 최적화 및 일반화 성능을 특성 학습(feature learning) 관점에서 분석.

- 신경망이 학습 과정에서 중요한 특징을 점차적으로 학습하고, 불필요한 특징을 배제하는 과정을 설명하는 프레임워크를 따름.

- 하지만, 병합된 모델에 대한 논의는 전혀 이루어지지 않음

# 2. TASK VECTOR: DEFINITION AND OBSERVATIONS

## 2.1 PRELIMINARIES

신경망 f: X \times \Theta \to Y 는 입력 X \in X 를 받아 출력 y \in Y 를 생성하며, \Psi \in \Theta 는 모델의 파라미터를 나타낸다.

- **\Psi^{(0)}**: 사전 학습된(pre-trained) 모델

- **\Psi^*_T**: 특정 태스크 T 에 대해 미세 조정된(fine-tuned) 모델

### 태스크 벡터(Task Vector) 정의

**정의 1.** 태스크 T 에 대한 **태스크 벡터 **\Delta \Psi_T 는 사전 학습 모델과 미세 조정 모델 간의 가중치 차이로 정의됨: 

즉, 특정 태스크에 대한 모델의 변화량을 나타내는 벡터임.

### **Task Arithmetic과 일반화**

- 주어진 **사전 학습 모델** \Psi^{(0)}와 여러 태스크 벡터 **{** {\Delta \Psi_{T_i}\}_{i \in V}}를 사용하여 **병합된 모델(merged model)** 을 구성할 수 있음:

- 손실 함수 l(X, y; \Psi) 를 사용하여 **태스크 ****T′**** 에 대한 일반화 오류**는 다음과 같이 정의됨: 

- **멀티태스크 학습 (Multi-Task Learning)**

- **학습 제거 (Unlearning)**

- **도메인 외 일반화 (Out-of-Domain Generalization)**

## 2.2 EMPIRICAL OBSERVATIONS

Colored-MNIST 데이터셋을 활용하여 태스크 간 관계를 분석

- **무관한 태스크 (Irrelevant Tasks)**

- **정렬된 태스크 (Aligned Tasks)**

- **상충하는 태스크 (Contradictory Tasks)**

### **모델 평가 방식**

- 두 개의 태스크 T1 과 T2 를 고려하여, 모델 \Psi = \Psi^{(0)} + \Delta \Psi_{T_1} + \lambda \Delta \Psi_{T_2} 의 성능을 측정.

### **주요 실험 결과 1**

{% include figure.liquid loading="eager" path="assets/img/posts/2025-03-11-when-is-task-vector-provably-effective-for-model/image_000.png" class="img-fluid rounded z-depth-1" %}

- **무관한 태스크 (Irrelevant Tasks)**

- **정렬된 태스크 (Aligned Tasks)**

- **상충하는 태스크 (Contradictory Tasks)**

그렇다면 질문이 생긴다:

💡 **핵심 질문(Q1): 태스크 간의 상관관계가 멀티태스크 학습과 학습 제거 성능에 미치는 영향은 어떻게 정량적으로 측정될 수 있는가?**

### 주요 실험 결과 2

- Colored-MNIST를 이용해 **새로운 태스크 T′** 를 구성

- \lambda_1, \lambda_2를 최적화하여 \Psi = \Psi^{(0)} + \lambda_1 \Delta \Psi_{T_1} + \lambda_2 \Delta \Psi_{T_2} 를 학습

- 실험 결과, **적절한 λ1,λ2 선택 시 개별 미세 조정된 모델보다 뛰어난 성능을 보임**

{% include figure.liquid loading="eager" path="assets/img/posts/2025-03-11-when-is-task-vector-provably-effective-for-model/image_001.png" class="img-fluid rounded z-depth-1" %}

💡 **핵심 질문(Q2): 태스크 벡터 연산이 도메인 외 일반화에서 효과적인 이유는 무엇이며, 최적의 λi 를 선택하는 방법은 무엇인가?**

# 3. A DEEP DIVE INTO TASK VECTORS

💡 **핵심 질문(Q1): 태스크 간의 상관관계가 멀티태스크 학습과 학습 제거 성능에 미치는 영향은 어떻게 정량적으로 측정될 수 있는가?**

💡 **핵심 질문(Q2): 태스크 벡터 연산이 도메인 외 일반화에서 효과적인 이유는 무엇이며, 최적의 λi 를 선택하는 방법은 무엇인가?**

이제 제안된 질문들을 해결함과 동시에

- 태스크 벡터를 수학적으로 formulate하고

- 멀티 태스크, 언러닝, OOD에 대한 이론적 분석을 수행해봅시다

- 또한, low-rank approximation & sparsification 방법이 성능을 유지하면서 계산 비용을 줄일 수 있음을 증명한다. 

## 3.1 Main Theoretical Insights

이 연구에서는 **이진 분류(binary classification) 태스크 집합**을 다룬다.

- 각 태스크의 레이블(label)은 판별적 토큰(discriminative tokens)과 그 반대되는 토큰(opposite tokens) 간의 다수결(majority voting)로 결정됨.

- 단일 층(one-layer) 및 단일 헤드(single-head) Transformer 모델을 분석 대상으로 함.

Major takeaways:

- **P1. 태스크 추가(Task Addition) 및 제거(Task Negation)의 정량적 분석**

- **P2. Out-of-Domain Generalization through Task Arithmetic**

- **P3. Low-Rank Approximation 및 Magnitude-Based Pruning가 모델 editing 성능을 유지함**

## 3.2 PROBLEM FORMULATION

### **데이터 및 모델 정의**

- 데이터 X = (x_1, x_2, \dots, x_P) \in \mathbb{R}^{d \times P}는 P 개의 토큰을 포함하며,

- 레이블 y∈{+1,−1} 는 스칼라 값.

### **Transformer 모델 구조**

본 연구에서는 **단일 층 Transformer**을 사용하며, 모델은 self-attention 레이어 1개와 2층 MLP으로 구성됨.

수학적으로 모델은 다음과 같이 표현된다:
