---
categories:
  - paper-reviews
date: "2023-01-19 00:00:00"
description: 논문 리뷰 - QA, NER, Knowledge 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
  - bert
  - embedding
  - fine-tuning
  - knowledge
  - language-model
  - ner
  - paper-review
  - pre-training
  - qa
  - transformer
  - vision
thumbnail: assets/img/posts/2023-01-19-kala-knowledge-augmented-language-model-adaptation/thumbnail.jpg
title: "KALA: Knowledge-Augmented Language Model Adaptation"
---

**논문 정보**

- **Date**: 2023-01-19
- **Reviewer**: yukyung lee
- **Property**: QA, NER, Knowledge

## 0. Abstract

- Simple fine-tuning of PLMs, on the other hand, might be suboptimal for domain-specific tasks because they cannot possibly cover knowledge from all domains

- Adaptive pre-training of PLM can help LM obtain domain-specific knowledge  
  → require large training cost
  → catastrophic forgeting of general knowledge

- KALA

## 1. Introduction

**1) 논문이 다루는 task**

- Adaptation the PLMs to specific domains (distributions over the language characterizing a given topic or genre)

**2) 해당 task에서 기존 연구 한계점**

{% include figure.liquid loading="eager" path="assets/img/posts/2023-01-19-kala-knowledge-augmented-language-model-adaptation/image_000.png" class="img-fluid rounded z-depth-1" %}

- Computationally inefficient: 데이터 양이 증가함에 따라 더 많은 메모리와 computational cost가 필요함

- forgetting general knowledge: performance degradation

**3) 제안 방법론 요약**

{% include figure.liquid loading="eager" path="assets/img/posts/2023-01-19-kala-knowledge-augmented-language-model-adaptation/image_001.png" class="img-fluid rounded z-depth-1" %}

- entities and relations는 domain specific knowledge를 위해 중요한 요소

- Entity memory bank와 Knowledge Graph를 활용하며, 이때 KG는 factual relationshop을 사용하기 위함

- Knowledge conditioned Feature Modulation (KFM)를 제안하며, 이는 PLM과 retrieved knowledge representation을 적절하게 결합하기 위함

- Contributions

## 2. Related Work

### 1) Language Model Adaptation

domain-specific corpus adaptation

- BioBERT

- Dont stop pretraining - DAPT, TAPT

: large amount of computational cost for pre-training

### 2) Knowledge-aware LM

Integrate external knowledge into PLMs

Pretraining based

- ERNIE

- KnowBERT

- Entity-as-Experts

- LUKE

- ERICA

## 3. Proposed Method

## 3.1 Problem Statement

**Learning objective (Only require general knowledge)**

: sub optimal for tackling domain-specific tasks (general knowledge는 domain-specific task를 풀이하기 위해 필요한 지식들을 모두 포함하지 않으므로)

{% include figure.liquid loading="eager" path="assets/img/posts/2023-01-19-kala-knowledge-augmented-language-model-adaptation/image_002.png" class="img-fluid rounded z-depth-1" %}

**Learning objective (Augments PLM conditioned on domain knowledge)**

{% include figure.liquid loading="eager" path="assets/img/posts/2023-01-19-kala-knowledge-augmented-language-model-adaptation/image_003.png" class="img-fluid rounded z-depth-1" %}

- **Definition 1: Entity and Mention**

- **Definition 2: Entity Memory**

- **Definition 3: Knowledge Graph**

## 3.2 Knowledge-conditioned Feature Modulation on Transformer

{% include figure.liquid loading="eager" path="assets/img/posts/2023-01-19-kala-knowledge-augmented-language-model-adaptation/image_004.png" class="img-fluid rounded z-depth-1" %}

- PLM에 domain-specific knowledge를 augment하는 방법 설명하는 파트

- iterleave the knowledge from h with the pre-trainied parameters

## 3.3 Relational Retrieval from Entity Memory

- entity만 retrieve 하게 될 경우 한계점을 가짐

- two entities 사이의 relational information도 고려해주기 위해 Relational Retrieval도 함께 수행함

- GNN을 통해 3.1에서 정의한 entity memory의 entity embedding을 보강해줌
  : 이때 neighborhood aggregation scheme을 사용함

- score는 all neighbors를 모두 고려하여 normalize되고 softmax를 취해서 사용함

{% include figure.liquid loading="eager" path="assets/img/posts/2023-01-19-kala-knowledge-augmented-language-model-adaptation/image_005.png" class="img-fluid rounded z-depth-1" %}

- entity embedding과 score를 결합하여 사용하는 형태임

- 최종 Entitiy embedding은 바로 위의 GNN 기반의 수식으로 대체되며, entity, relation, kg까지 모두 고려한 embedding을 생성할 수 있게 됨

- unseen entity또한 위의 과정을 통해 단순한 zero vector로 표현되지 않기 때문에 훨씬 더 효과적으로 처리할 수 있게됨

## 4. 실험 및 결과

### Dataset

Domain-specific NER, QA Datasets

### Baseline

Finetuning, TAPT, DAPT, Other knowledge models

- Point-wise option : entity memory만을 사용해서 retrieval 하고 knowledge graph를 사용하지 않은 옵션

- relational: entity memory에서 relational retrieval을 수행함

### 실험 결과

**실험 1 : QA에서 KALA의 효과**

- Finetuning 보다 약 1.2점 상능효과 있음

- DAPT로 유사 domain 다 사용하는 방법보다 target dataset의 entity를 weak supervision으로 사용하는것이 유용함

- relational (GNN 사용한 부분)은 특정 데이터셋에서 성능향상을 보임

{% include figure.liquid loading="eager" path="assets/img/posts/2023-01-19-kala-knowledge-augmented-language-model-adaptation/image_006.png" class="img-fluid rounded z-depth-1" %}

{% include figure.liquid loading="eager" path="assets/img/posts/2023-01-19-kala-knowledge-augmented-language-model-adaptation/image_007.png" class="img-fluid rounded z-depth-1" %}

**실험 2: NER에서 KALA의 효과**

- finetuning 보다 약 1~2점 효과가 있음

- 효과는 실험 1과 유사함

{% include figure.liquid loading="eager" path="assets/img/posts/2023-01-19-kala-knowledge-augmented-language-model-adaptation/image_008.png" class="img-fluid rounded z-depth-1" %}

**실험 3: gamma, beta에 대한 추가 실험**

- KFM layer에 대한 성능 차이

- layer norm 횟수도 함께 실험했음

- 두가지를 모두 사용하는것이 가장 효과적이었음

→ knowledge integration을 적절하게 해준것으로 해석할 수 있음

**실험 4: knowledge integration architecture과의 비교**

- knowledge integration 모델들과의 비교

- Adapter의 성능이 돋보였음

{% include figure.liquid loading="eager" path="assets/img/posts/2023-01-19-kala-knowledge-augmented-language-model-adaptation/image_009.png" class="img-fluid rounded z-depth-1" %}

**실험 5: seen/ unseen 데이터에 대한 성능 비교**

- KALA의 unseen entity가 test set에 등장해도 성능이 크게 저하되지 않음

- 저자들은 KALA가 unseen entity를 seen entity와 가깝게 embed함으로서 성능을 유지할 수 있다고 주장함

- 여기서 놀라운것은 WNUT에서의 DAPT 성능

{% include figure.liquid loading="eager" path="assets/img/posts/2023-01-19-kala-knowledge-augmented-language-model-adaptation/image_010.png" class="img-fluid rounded z-depth-1" %}

**실험 6: token에 대한 case study**

- “##on”이라는 token이 각 entity별로 다른 위치에 임베딩 되는것을 볼 수 있음
