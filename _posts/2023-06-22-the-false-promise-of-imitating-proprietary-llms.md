---
categories:
  - paper-reviews
date: "2023-06-22 00:00:00"
description: 논문 리뷰 - sLLM, LLM, Evaluation Metric 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
  - evaluation metric
  - gpt
  - llm
  - paper-review
  - sllm
thumbnail: assets/img/posts/2023-06-22-the-false-promise-of-imitating-proprietary-llms/thumbnail.jpg
title: The False Promise of Imitating Proprietary LLMs
---

**논문 정보**

- **Date**: 2023-06-22
- **Reviewer**: 김재희
- **Property**: sLLM, LLM, Evaluation Metric

## 1. Intro

> 단순히 데이터를 확보해서 sLLM을 SFT 방식으로 훈련하는 것은 **정말로** 모델이 해당 태스크에 대한 성능을 확보하지 못함.

### sLLM

{% include figure.liquid loading="eager" path="assets/img/posts/2023-06-22-the-false-promise-of-imitating-proprietary-llms/image_000.png" class="img-fluid rounded z-depth-1" %}

- 최근 LLaMA, Alpaca, Vicuna 등을 비롯해 정말 많은 sLLM들이 등장하고 있음

- 해당 모델들이 가지는 임팩트는 다음과 같음

### Self Instuct

{% include figure.liquid loading="eager" path="assets/img/posts/2023-06-22-the-false-promise-of-imitating-proprietary-llms/image_001.png" class="img-fluid rounded z-depth-1" %}

- 특히 데이터 수집 시 Self Instruct 등의 방법론을 이용하는 것이 일반적

- Self Instruct는 공개된 LLM 서비스를 이용하여 데이터를 구축하는 방법론

- Self Instruct 기반 방법론을 분류하면 크게 두가지 흐름

- 두 방식 모두 결국 LLM의 지식을 Distillation 하는 방향

### False Promise

{% include figure.liquid loading="eager" path="assets/img/posts/2023-06-22-the-false-promise-of-imitating-proprietary-llms/image_002.png" class="img-fluid rounded z-depth-1" %}

- 본 논문의 저자들은 이러한 SelfInstruct + SFT 방식으로 학습된 모델의 유효성에 대해 의문을 제기함

- 이는 두가지 측면으로 구분

### Contribution

- 본 논문은 이러한 최근 현상을 1) 지적하면서 2) sLLM 학습의 요소들을 분리하여 분석하고 3) 향후 sLLM 개선 연구의 방향에 대해 제안하고 있음

## 2. Evaluation

- 해당 논문에서는 3가지 평가 방식 도입

- Metric : 기존 데이터셋에서 제공하는 Metric을 이용하여 평가

- GPT-4 : ChatGPT에게 Imitation Model과 ChatGPT가 생성한 문장을 입력하고, 선호도를 출력하도록 Prompt 구성

- Human : Amazon Turk를 이용하여 70명의 응답자에게 두 모델이 생성한 문장 중 더 나은 문장을 고르도록 요구

> 해당 논문에서는 모든 데이터셋의 모든 평가 방식의 평균을 담고 있음

## 4. Dataset

- 본 논문에서는 두가지 목적에 따라 Dataset 구축을 구분하여 사용

1. Task-Speicific Imitation : 특정 태스트에 대해서 sLLM이 LLM의 성능을 따라잡도록 학습하기 위한 데이터셋 구축

1. Broad-coverage Imitation : 실제 LLM 서비스처럼 광범위한 태스크들을 수행할 수 있는 범용적 목적의 sLLM 학습을 위한 데이터셋 구축

- SharGPT-Mix의 경우 기존에 연구목적으로 구축되었던 Prompt 데이터셋인 NaturalInstructions 보다 높은 품질을 가지고 있다고 주장

## 5. 모델

1. Broad-Coverage Imatation

{% include figure.liquid loading="eager" path="assets/img/posts/2023-06-22-the-false-promise-of-imitating-proprietary-llms/image_003.png" class="img-fluid rounded z-depth-1" %}

- 특정 태스크에 대한 성능 측정

- 학습 데이터의 크기와 모델 크기를 늘리는 실험 진행

- 모델의 크기를 늘리는 실험 진행

1. Broad Model - Broad Task

1. Targeted Data에 대한 학습

- sLLM은 스타일을 학습

## 6. 결론

- 요약하면 결국 : 범용 목적의 모델은 아직 sLLM으로 도달할 수 있는지 의문이다.

- Human Evaluation에 대한 문제점을 지적한 점은 좋은 듯

- base 모델의 성능이 좋아야 Imitation 자체가 잘 진행된다고 귀결됨

- LLM 개발하는 대기업 측면에서 오히려 걱정할 지점이 많아진다고 생각
