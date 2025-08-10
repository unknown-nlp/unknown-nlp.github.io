---
categories:
  - paper-reviews
date: "2023-09-12 00:00:00"
description: 논문 리뷰 - Knowledge Distillation 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
  - gpt
  - knowledge distillation
  - language-model
  - paper-review
thumbnail: assets/img/posts/2023-09-12-a-systematic-study-of-knowledge-distillation-for-natural/thumbnail.jpg
title: "A Systematic Study of Knowledge Distillation for Natural Language

  Generation with Pseudo-Target Training"
---

**논문 정보**

- **Date**: 2023-09-12
- **Reviewer**: 전민진
- **Property**: Knowledge Distillation

## 0. Abstract

- Natural Lnaguage Generation(NLG)의 경우, 많은 연산량과 저장 공간이 필요

- 실제 산업에 활용할 때 이를 효율적으로 압축해 사용할 수 있는지 보기 위해 knowledge distillation(KD) method에 집중해 여러 가지 실험을 진행, 최적의 KD setting을 제안

- 특히, NLG distillation의 특성상 exposure bias problem을 해소할 수 있는 방법론인 Joint-Teaching method를 제안

## 1. Introduction

- KD는 큰 모델에서 작은 모델로 knowledge를 transfer시키는 방법론으로, 일반적인 태스크에서 KD는 word-level 혹은 sequence-level로 적용될 수 있음

- KD 연구는 광범위하게 진행되어 왔지만, NLU task에 집중되거나, task agnostic language modeling에, specific generation task(e.g. NMT)에 국한됨

- 본 논문에서는 NLG를 위한 KD에 대해서 체계적으로 연구

- 메인 연구는 중간 크기의 labled data로 medium size LM을 fine-tune한 걸 teacher로 사용하는 상황을 가정으로 함

- 본 논문은 모델 구조를 비교하는 것을 시장으로, pruning, KD design decision, computational resource와 task performance사이의 tradeoff를 살펴보는 순서로 구성

- 이후로, word-level의 KD에서 teacher와 student에서 생성된 PT를 사용하는 방법론인 Joint-Teaching을 제안

- 마지막으로 GPT4를 활용해 huge LM을 할용해 small Encoder-decoder model을 KD하는 실험을 진행

- 주된 실험 결과는 다음과 같음

## 2. Related Work

- Exposure Bias

- Compression and Knowledge Distillation

## 3. Proposed Method

- Research Design

- Architectuures and Pruning - stage 1,2

- Objectives - stage 3

- Pesudo-Target(a.k.a sequence-level KD) - stage 4

- Unlabeled data - stage 5

- Multiple PTs - stage 6

- Sampling PTs - stage 7

- Joint Teacheing - stage 8

## 4. 실험 및 결과

### Task & Dataset

- 4가지 NLG task에 대해서 실험 진행

### Models and Pruning

- Decoder-only : GPT2, GPT-M, GPT-L, OPT-125M, OPT-350M 사용

- Encoder-decoder : T5-S, T5-L, BART-6, BART-L 사용

- Pruning : BART-6:6에서 pruning을 적용, encoder 혹은 decoder를 택해 맨 앞과 맨 뒤 레이어를 제외한 중간 레이어를 삭제

- KD stage(3-8)에서는 T5-S, T5-L, BART-2:6, BART-L 사용

### Evalution

- Task performance

- Computational Performance

### Result

- S1 : Encoder-decoder model이 Decoder-only model보다 NLG의 task-specific tuning에서 더 뛰어남

- S2 : decoder를 pruning하는게 더 낫다

- 아래 장표는 stage마다 성능을 나타내는 장표

- S3 : Logit KD를 main training objective로 사용하는게 낫다(A)

- S4 : Logits KD와 PT를 결합

- S5 : Unlabled data를 함께 썼을 때 성능이 좋아짐

- S6 : multiple PT에 student를 노출시키는게 도움이 됨

- S7 : PT를 생성할 때 sampling하는게 beam search보다 나음

- S8 : Joint-Teaching이 student를 향상시킴

- 위의 장표는 Joint-Teaching으로 학습했을 때의 성능을 나타냄

- Extreme setup : KD with GPT-4

## 5. Conclusion & Limitation

### Conclusion

- decoder가 pruning된 ED모델을 student로, Logit KD와 sampling한 PT를 활용한 Joint-Teaching방법이 성능이 어느 정도 방어되면서 가장 좋은 compression rate를 보여줌

### Limitation

- Using a medium size fine-tuned teacher

- The scope of our realistic setup

- Computational training cost

- Utilizing huge LMs
