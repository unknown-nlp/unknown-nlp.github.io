---
categories:
- paper-reviews
date: '2024-10-03 00:00:00'
description: 논문 리뷰 - Knowledge Distillation 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- gpt
- knowledge distillation
- llm
- paper-review
- reasoning
- vision
thumbnail: assets/img/posts/2024-10-03-qcrd-quality-guided-contrastive-rationale-distillation-for-large/thumbnail.jpg
title: 'QCRD: Quality-guided Contrastive Rationale Distillation for Large Lanauge
  Models'
---

**논문 정보**
- **Date**: 2024-10-03
- **Reviewer**: 전민진
- **Property**: Knowledge Distillation

## Abstract

- LLM은 좋은 성능을 갖고 있으나 resource 제한, inference 효율성 등으로 다양한  application에서 사용되기엔 한계가 존재

- 최근 LLM을 기반으로 한 knowledge distillatinon으로 smaller, task-specific한 모델을 학습하는 여러 방법론이 제안 됨

- 하지만 기존 연구들은 knowledge의 disversity와 quality에 크게 집중하지 않음. 

- 본 논문에서는 constrative knowledge learning을 통한 reasoning capability 향상을 목표로 하는 quality-guided contrstive rationale distillation(QCRD)을 제안

- 실험 결과, 기존의 distillation method보다 뛰어난 성능을 보임

## Introduction

- LLM의 모델 크기가 커지면서 reasoning ability가 발생 → 이를 이용해 작은 모델을 학습하자

- 이를 해소하기 위한 다양한 방법이 제안

- 본 논문에서는, Quality-guided Contrastive Rationale Disilltation(QCRD)을 제안

- QCRD의 우수성을 입증하기 위해서, T5-base(220M), small(60M)을 student로 사용해 실험 진행, 여러 벤치마크 데이터셋에서 우수한 성능을 보임

## Related Work

- Multi-task learning with LLM generated ratioanles

- Contrastive learning for LLMs

## Methodology

{% include figure.liquid loading="eager" path="assets/img/posts/2024-10-03-qcrd-quality-guided-contrastive-rationale-distillation-for-large/image_000.png" class="img-fluid rounded z-depth-1" %}

- QCRD는 3가지 파트로 구성이 되어 있음

**Multi-task learning framework for the student model**

- 이전 연구와 유사하게 prefix를 활용해서 small model이 다양한 형태의 output을 생성할 수 있도록 학습

**Generation of contrastive knowledge**

- Positive sample

- Negative sample

**Constrastive knowledge distillation**

- Train a discriminator to judge rationales

- Quality-guided contrastive distillation

- Training loss

## Experiments

**Datasets**

- SVAMP : arithmetic word problem solving

- CQA : commonsense QA

- e-SNLI, ANLI : NLI

- rationale을 GPT-3.5-turbo로 생성

**Implementation details**

- T5-base(220M),T-small(60M)사용

- \alpha_1,\alpha_2,\alpha_3은 실험적으로 0.5으로 세팅 \alpha_3은 매 iteration마다 0.9를 곱함

- \beta=0.2,\delta=3

- LLM temp 0.7로 5번 샘플링, small model은 5-iteration-before model에서 temp 1.5로 1개 샘플링

**Baselines**

- Fintuning 

- Single-supervision : teacher model이 예측한 label을 맞추도록 학습

- DSS : multi task learning with label prediction and rationale generation

- MI : DSS기반에 prediction label과 rationale사이의 mutual information이 최대화하도록 task 추가

**Experimental result**

- Experiments across four benchmarks

- Distillation with LLM labels

- Distillation with smaller datasets

- Ablation study on QCRD

## Discussion

- Different contrastive distillation schemes

- influence of negative sample

- Assessment for generated rationales

- Distribution of rationale quality scores

## Conclusion

- Contrastive learning을 CoT distillation에 접목한 최초의 논문!
