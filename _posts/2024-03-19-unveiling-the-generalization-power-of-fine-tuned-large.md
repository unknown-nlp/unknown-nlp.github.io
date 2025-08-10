---
categories:
  - paper-reviews
date: "2024-03-19 00:00:00"
description: 논문 리뷰 - ICL, Generalization, Fine-tuning 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
  - classification
  - fine-tuning
  - generalization
  - icl
  - language-model
  - llm
  - paper-review
thumbnail: assets/img/posts/2024-03-19-unveiling-the-generalization-power-of-fine-tuned-large/thumbnail.jpg
title: Unveiling the Generalization Power of Fine-Tuned Large Language Models
---

**논문 정보**

- **Date**: 2024-03-19
- **Reviewer**: 전민진
- **Property**: ICL, Generalization, Fine-tuning

## Abstract

- LLM은 다양한 task를 수행할 수 있는 능력이 있음이 밝혀졌고, 이러한 모델을 domain-specific dataset에 fine-tuning했을 때 fine-tuning을 하지 않았을 때 보다 좋은 성능을 보임

- finetuning이 LLM의 generalization ability에 내재적으로 어떤 영향을 끼치는지 알아보고자 함

- 5가지 task의 다양한 데이터셋을 활용해서 실험 진행, 결과는 다음과 같음

- generation task에 한해, fine-tuning시 ICL 전략을 곁들이면, 기존의 fine-tuning에 비해 모델의 generalization ability가 향상될 수 있음

## Introduction

- 이전에 fine-tuning을 했을 때 모델의 generalization ability에 관한 여러 연구들이 존재

- 본 논문에서는 task-specific한 fine-tuning이 어떻게 LLM의 generalization ability에 영향을 끼치는지에 대한 연구를 진행

- 모델의 일반화 성능을 높이기 위해, ICL 전략을 fine-tuning에 덧붙인 방법론을 추가적으로 실험

## Related Work

- ICL은 모델의 내재된 parametric knowledge를 극대화, context를 이해해 답변을 생성하도록 함

- FT와 ICL은 specialization과 generalization사이의 trade-off 관계를 조절

- few-shot FT와 ICL은 OOD test set에 대해 유사한 generalization을 보여줌

- 이전에도 fine-tuning동안 in-context example를 사용하는 것이 length generalization에 도움이 된다는 연구가 있었음

## Evaluation Design

- task-specific한 fine-tuning이 LLM의 generalization ability에 끼치는 영향을 분석

- Evaluation Benchmarks

- Experimental Setup

## Results and Findings

- Same Task , In-domain Datasets

- Same Task, Out-of-domain Datasets

- Different Tasks(2K로 학습)

- FTICL

## Conclusion

- generation task 혹은 classification task의 특성에 따라 finetuning 후 finetuned model의 generalization ability가 다른 양상을 띔

- FT시 input을 ICL처럼 주는 FTICL방법이 generation task에서 모델의 generalization ability를 향상시킴

민진 정리

- finetuning은 모델의 generalization ability를 저하시킨다

- Cross task setting의 경우 어지간한 finetuned model보다 ICL setting의 성능이 높다

- finetuning할 때 input을 ICL처럼 주면, (generation task한정, classification은 애매) same task&out domain setting과 cross task setting에서 성능이 높아진다.

총평

- 문제 자체는 흥미로운데, 실험 결과에 따른 해석이 너무 자의적이라고 생각

- finetuning이 생각보다 generation task에서 일반화가 안되는게 신기했음

- ICL.. 살짝 무시했었는데.. 몇몇 task를 제외하곤 뛰어난 방법론이었다..
