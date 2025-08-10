---
categories:
- paper-reviews
date: '2024-01-30 00:00:00'
description: 논문 리뷰 - Knowledge Distillation 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- gpt
- knowledge distillation
- language-model
- llm
- paper-review
- reasoning
thumbnail: assets/img/posts/2024-01-30-lion-adversarial-distillation-of-proprietary-large-language-models/thumbnail.jpg
title: 'Lion: Adversarial Distillation of Proprietary Large Language Models'
---

**논문 정보**
- **Date**: 2024-01-30
- **Reviewer**: 전민진
- **Property**: Knowledge Distillation

## Abstract

- 지금까지 제안된 knowledge distillation 방법론은 student model의 답변과 teacher model의 답변 align되도록하는, unidirectional knowledge(teacher → student)에 초점을 둠

- 본 논문에서는 이러한 방법론들이 “feedback”을 학습 과정에 포함시킬 가능성을 간과했다고 지적

- 본 논문에서는 3단계(imitation, discrimination, generation)로 구성된 novel한 adversarial distillation framework를 제안

- 실험 결과, open-ended generation 능력이 ChatGPT에 상응할 뿐만 아니라, BIG-Bench Hard, AGIEval에서 기존의 instruction-tuned model를 능가하는 성능을 보여줌

## Introduction

- 최근, LLM이 새로운 task에 대한 zero-shot 성능을 보였지만, 대부분의 모델이 소유권이 있음

- proprietary “teacher” LLM으로부터 knowledge distillation을 하기 위해 teacher model의 답변과 student model의 답변을 aligning하는 방식을 사용

- 그러나 지금까지는 학습 과정에 “feedback”을 활용하려는 시도가 없었음

- adversarial knowledge distillation(AKD)에 영감을 얻어, proprietary LLM을 compact student model로 distilling하는 adversarial framework를 제안

- 하지만, 바로 AKD방법론은 teacher model의 weight나 gradient가 필요하기 때문에 현상황에 바로 적용할 순 없음

- 해당 프레임워크는 다음과 같은 단계로 구성

- Alpaca’s training data(175개의 사람이 작성한 seed instruction으로 생성된 데이터셋)으로 기반으로 해당 프레임워크를 3번 반복, 총 70K data로 student model을 학습(iteration한번에 6K data얻음)

- 실험 결과, instruction-tuned baseline model보다 뛰어난 성능 보임

- 본 논문의 핵심 contribution은 다음과 같음

## Related Work

- Knowledge Distillation

## Method

- 문제 정의

- Initialization

- **Imitation Stage**

- **Discrimination Stage**

- Generation Stage

- Min-Max Game Interpretation

## Experiments Settings

- Datasets

- Baseline

- Implementation Details

## Experimental Results

- Results for Open-ended Generation

- Results for Reasoning

## Analyses

- Ablation study

- The Learning Dynamics of Lion

- Case Studies

## Conclusion

- 본 논문에서는 proprietary LLM을 distill하기 위한 adversarial knowledge distillation framework을 제안

- 학습 결과, open-ended generation에선 ChatGPT와 상응하는 성능을, Reasoing task에서는 기존 SOTA모델인 Vicuna와 비슷한 성능을 보임

- Limitation
