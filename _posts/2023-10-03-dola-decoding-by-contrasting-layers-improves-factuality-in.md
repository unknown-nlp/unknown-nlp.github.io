---
categories:
  - paper-reviews
date: "2023-10-03 00:00:00"
description: 논문 리뷰 - Factual Consistency, LLM, Calibrating 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
  - calibrating
  - factual consistency
  - language-model
  - llm
  - paper-review
  - transformer
thumbnail: assets/img/posts/2023-10-03-dola-decoding-by-contrasting-layers-improves-factuality-in/thumbnail.jpg
title: "DoLa: Decoding by Contrasting Layers Improves Factuality in Large Language
  Models"
---

**논문 정보**

- **Date**: 2023-10-03
- **Reviewer**: 김재희
- **Property**: Factual Consistency, LLM, Calibrating

## 1. Intro

- LLM의 Hallucination은 여전히 해결책이 보이지 않는 문제

- Hallucination을 줄이기 위한 연구 방향성 :

- 해당 연구는 기존 모델에 대해 추가적인 학습을 하지 않고도, 1) Hallucination이 발생하는 부분을 찾고 2) 이를 수정할 수 있는 Decoding 기법을 제안

- ROME 연구에서는 Transformer를 다음과 같이 분석

## 2. Method

- 해당 논문의 기본 아이디어 :

- 분포를 비교하는 것은 아래와 같은 수식을 통해 전개됨

## 3. How It Works?

{% include figure.liquid loading="eager" path="assets/img/posts/2023-10-03-dola-decoding-by-contrasting-layers-improves-factuality-in/image_000.png" class="img-fluid rounded z-depth-1" %}

- 위 그림은 각 토큰 별 출력 레이어의 vocab dist와 각 레이어의 분포 차이를 시각화 한것

- Pattern #1 : Factuality에 중요한 토큰은 높은 레이어까지 큰 변화를 보임

- Pattern #2 : Factuality에 중요하지 않은 조사 등은 중간 레이어부터 매우 작은 변화를 보임

## 4. Experiments

{% include figure.liquid loading="eager" path="assets/img/posts/2023-10-03-dola-decoding-by-contrasting-layers-improves-factuality-in/image_001.png" class="img-fluid rounded z-depth-1" %}

- Factuality 측면에서 별도의 학습없이도 SOTA의 성능을 달성하는 모습

- 다양한 지표에 있어서도 여전히 앞서는 모습을 보이고 있음

- 이전 연구인 Contrastive Decoding은 Information이 매우 떨어지는데, DoLa는 오히려 Information이 높아지는 모습

- LLaMa 모델에 DoLA 적용 유무에 따른 Auto Eval 결과

{% include figure.liquid loading="eager" path="assets/img/posts/2023-10-03-dola-decoding-by-contrasting-layers-improves-factuality-in/image_002.png" class="img-fluid rounded z-depth-1" %}

- DoLA 적용 여부에 다른 속도

## 7. Conclusion

- 추가 학습 없이도 Factuality를 향상시키는 Decoding 방법론 제안

- 모델이 어떻게 Factuality를 확보하는지 내부 레이어 분석을 통해 설명

- ROME을 많이 인용하고 있고, 아이디어의 기반으로 삼고 있음
