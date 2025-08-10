---
categories:
  - paper-reviews
date: "2024-01-16 00:00:00"
description: 논문 리뷰
giscus_comments: true
layout: post
related_posts: false
tags:
  - alignment
  - language-model
  - llm
  - paper-review
thumbnail: assets/img/posts/2024-01-16-benchmarking-cognitive-biases-in-large-language-models-as/thumbnail.jpg
title: BENCHMARKING COGNITIVE BIASES IN LARGE LANGUAGE MODELS AS EVALUATORS
---

**논문 정보**

- **Date**: 2024-01-16
- **Reviewer**: yukyung lee

# 0. Abstract

- 최근 LLM을 automatic evaluator로 사용하는 연구들이 제안되고 있음

- 하지만 본 논문은 LLM을 evaluator로 사용할 때 congnitive bias가 생길 수 있다는 점을 지적하며, Cognitive bias benchmark for llm as evaluator라는 새로운 데이터셋을 발표함

- CoBBLER는 llm evaluation output에서 발생할 수 있는 6가지 cognitive bias들을 평가할 수 있음 (예를들어 자기 자신이 만든 아웃풋에 훨씬 더 선호도가 높은 egocentric bias를 포함)

- 이 논문의 주장은 “LLM을 text quality evaluator”로 사용하기에 어려움이 있다는 점을 지적하며, human과 machine 사이의 correlation을 테스트 함

# 1. Introduction

- Motivation

- Method

## 5.2 Model size

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-16-benchmarking-cognitive-biases-in-large-language-models-as/image_000.png" class="img-fluid rounded z-depth-1" %}

- 빨간 선은 random threshold를 의미함

- 빨간선 위의 모델들은 각 bias에 영향을 받는것을 의미함

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-16-benchmarking-cognitive-biases-in-large-language-models-as/image_001.png" class="img-fluid rounded z-depth-1" %}

- bias 점수가 높다 → bias 문제가 있다

- valid response 점수가 높다 → 잘 답변한 응답의 비율 이므로 좋은 모델임

## 5.3 Agreement with human preference

- human과 model 사이의 RBO 점수는 0.496이며, 이를 통해 둘 사이의 alignment가 크지 않음을 알 수 있음

# 6. Conclusion

- Evaluator로서의 LLM을 평가하기 위해 cognitibe bias를 분석하는 cobbler를 제안함

- 이는 implicit bias, induced bias를 모두 내포하였으며 llm을 evaluator로 사용하는 것의 위험성을 보여줌

- llm 평가는 bias 되어 있기 때문에 evaluator로서의 의문점을 제기하였으며, 사람 평가는 llm 보다는 상대적으로 낮은 cognitive bias를 나타낸다고 평가함

[Opinions]

- 평가 세팅이 완전하지는 않은 것 같음. 하지만 완벽한 평가를 하기 힘든 주제라 생각함

- comparsion 평가를 15개 모델에 대해 수행하는것에 회의적인 의견을 가짐 (평가 모델의 개수가 많아질 수록 평가의 품질은 낮아질 수 밖에 없기 때문임)

- 학부생이 1저자인 논문이라 인상적임
