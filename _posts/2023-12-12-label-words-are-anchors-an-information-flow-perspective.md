---
categories:
- paper-reviews
date: '2023-12-12 00:00:00'
description: 논문 리뷰 - ICL, In Context Learning, LLM 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- attention
- classification
- icl
- in context learning
- llm
- paper-review
thumbnail: assets/img/posts/2023-12-12-label-words-are-anchors-an-information-flow-perspective/thumbnail.jpg
title: 'Label Words are Anchors: An Information Flow Perspective for Understanding
  In-Context Learning'
---

**논문 정보**
- **Date**: 2023-12-12
- **Reviewer**: 김재희
- **Property**: ICL, In Context Learning, LLM

## 1. Intro

- ICL 수행 시 각 demonstartion의 정보는 label words의 representation에 집중됨을 확인

- 발견된 현상을 이용하여 ICL의 성능을 개선하는 방법론 제시

- 얕은 레이어와 깊은 레이어의 역할

{% include figure.liquid loading="eager" path="assets/img/posts/2023-12-12-label-words-are-anchors-an-information-flow-perspective/image_000.png" class="img-fluid rounded z-depth-1" %}

## 2. Analysis

### 2.1. 가설 검증

- 본 논문이 관찰한 두가지 현상(deep/shallow layer)에 대한 직접적 검증 시도

- Saliency Score를 이용하여 예측에 각 단어의 영향력을 측정

- ICL 환경에서 입력을 세가지로 구분

- 위 3가지 입력에 따라 Saliency Score를 계산하게 됨 

- Input Text(w) → Label Words(p)

- Label Words(p) → Prediction(q)

- Input Text(w) → Input Text(w)

### 2.2 실험 환경

- 4개의 Text Classification Task 사용

- Model : 

### 2.3 Information Flow 실험

1. Layer 깊이에 따른 Information Flow

### 2.4 Loyalty 실험

- Isolation(Label Words) : Attention Map을 임의로 조정하여 Input Text → Label Word의 Attention을 막는 환경

- First/Last : 초기/후기 5개 레이어에 대해 Isolation을 수행 

- Random : Attention Map 내 임의의 attention을 조정

- Loyalty : 2가지 측면에서 Isolation에 따른 영향력 평가

- Label Word와 레이어 단위 별 영향력 평가

### 2.5 AUCROC 실험

- l번째 레이어의 예측 시점에 대한 각 Label Word와 실제 예측값 간의 높은 Correlation 관찰

- 위 가설에 대한 엄밀한 검증을 위해 AUROC 계산 실시

- 레이어가 깊어질 수록 AUROC 값이 커지는 경향성 확인

- 레이어가 깊어질수록 R_l값이 점차 커지는 모습 확인 

### 2.6 결론

- Label Word가 해당 Demonstration의 정보를 종합하고, 이를 예측에 전달하는 역할을 하는 모습 확인 

## 3. Proposed Method

- 앞선 분석을 바탕으로 직관적인 ICL 개선 방안 제안

- 앞선 분석의 결론

### 3.1 Anchor Re-weighting

- Attention Mechanism을 직접적인 예측 확률의 추정으로 간주

- 두가지 식을 치환하여, log prob으로 표현 가능(\textbf{q}_q / \sqrt{d} = \hat{\textbf{x}}, \textbf{k}_{p_i} - \textbf{k}_{p_C} = \beta_i )

- 위와 같은 식은 결국 logistic regression 식으로 표현이 됨

- 위 식에서 \beta_i는 original Attention Weight의 값, \beta_0가 직접적인 attention map의 수정이라고 볼 수 있음

- 우리는 학습 파라미터 \beta_0 에 대해서 아래와 같은 closed form을 통해 해결 가능한 최적화 가능

⇒ ICL을 Attention Matrix를 이용한 Logistic Regresseion으로 접근하여, LLM의 능력에 온전히 의존하지 않고, 외부에서 ICL을 수행하는 듯한 방법론

⇒ 추론과정 수행 이전에 train sample들에 대해 별도로 수행하여 진행할 수 있게 됨

### 3.2 Anchor-Only Context Compression

- 앞선 내용을 요약하면 ***모델이 예측 수행 시 Demonstration 중 Label Word에서만 정보를 취합하고 있음***

## 4. Experiments

### 4.1 [Anchor Re-Weighting] 실험 환경

- ICL 시 사용될 데이터 : Class 당 1개씩 샘플링

- Re-weighting을 위해 사용할 학습 데이터 : Class 당 4개씩 샘플링

- 비교 방법론 :

### 4.2 [Anchor Re-Weighting] 결과

- 개잘나옴;;

- ICL 방법론과 비교하고 있지만, 해당 방법론은 일반적인 ICL과 다르게 동작함

### 4.3 [Anchor-Only Context Compression] 실험 결과

- Text Anchor : Label Word를 직접 Inference Input 앞에 Concat

- Hidden Random : Label Word를 제외한 임의 토큰의 representation을 caching하여 활용

- Hidden Random-Top : Label Word를 제외한 임의 토큰을 20개 선별하고, 이 중 가장 좋은 성능을 낸 세팅 리포팅

- Hidden Anchor : Label Word의 Representation을 caching하여 이용(proposed method)

- 실험 데이터셋의 평균 결과치

- 제안 방법론이 가장 높은 성능 리포팅

{% include figure.liquid loading="eager" path="assets/img/posts/2023-12-12-label-words-are-anchors-an-information-flow-perspective/image_001.png" class="img-fluid rounded z-depth-1" %}

- 하지만 속도 측면에서는 Caching 전략이 유효

## 7. Conclusion

### Pros

- ICL에 대한 심도있는 분석과 설득력있는 주장

- 주장을 뒷받침하기 위한 다양한 분석

- 분석 결과를 이용한 ICL 개선 방법론 제시 및 큰 성능 개선 달성

- 분석 결과를 이용한 ICL 개선 방법론 제시 및 속도 개선 달성

- 엄밀한 Fair Comparison을 위한 실험 설정

- 주장하는 바를 뒷받침하는 Metric 제안 및 활용

- 깔끔한 논문 서술

- Appendix에 궁금할만한 결과물을 다 때려박음

### Cons

- 교묘하게 피해가는 Contribution

- 복잡한 구현 방식
