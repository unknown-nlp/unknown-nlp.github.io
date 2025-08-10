---
categories:
- paper-reviews
date: '2024-02-20 00:00:00'
description: 논문 리뷰
giscus_comments: true
layout: post
related_posts: false
tags:
- detection
- language-model
- llm
- paper-review
thumbnail: assets/img/posts/2024-02-20-knowledge-card-filling-llms-knowledge-gaps-with-plug/thumbnail.jpg
title: 'KNOWLEDGE CARD: FILLING LLMS’ KNOWLEDGE GAPS WITH PLUG-IN SPECIALIZED LANGUAGE
  MODELS'
---

**논문 정보**
- **Date**: 2024-02-20
- **Reviewer**: 전민진

# Abstract

- LLM은 static general-purpose model로, 재학습하거나 자주 업데이트하기 어려움

- 이를 위해, Knowledge card, general-purse LLM에 새로운, 관련된 지식을 plug-in할 수 있는 modular framework를 제안

- 실험 결과, 6가지 데이터셋에서 SOTA 달성 

# Introduction

- LLM은 knowledge-intensive task와 context에서 어려움을 겪고 있음

- 이를 해결하기 위한 방법으로, retrieval augmentation, generated knowledge prompting이 제안됨

- 하지만 이러한 방법론들은 knowledge의 2가지 특성을 반영하기 어려움

# Related works

- Retrieval-Augmented Language Models

- Generated Knowledge Prompting

- Modular Language Models

# Proposed Method

{% include figure.liquid loading="eager" path="assets/img/posts/2024-02-20-knowledge-card-filling-llms-knowledge-gaps-with-plug/image_000.png" class="img-fluid rounded z-depth-1" %}

- Knowledge cards

- Knowledge selectors

- Knowledge intergration

# Experiment Settings

- Implementation

- Tasks and Datasetss

- Baselines

# Results

- MMLU

- Misinformation Detection

- MidtermQA

{% include figure.liquid loading="eager" path="assets/img/posts/2024-02-20-knowledge-card-filling-llms-knowledge-gaps-with-plug/image_001.png" class="img-fluid rounded z-depth-1" %}

- Patching LLM Knowledge

- Knowledge Selctor Study

- Retireval vs Specialized LMs

- Knowledge Stream Analysis

- LLM Compatibility

- Yes/No in Top-Down

# Conclusion

- knowledge를 모듈화, LLM에 plug-in해 knowledge intensive task를 푸는 프레임워크 knowledge card를 제안

- 기존의 방법론 보다 성능이 뛰어나고, 정보 업데이트 및 특정 도메인 정보 추가가 용이하다는 강점을 지님

- 단점은 프레임워크를 구성하는 세부 모델이 너무 많음

- 얻는 성능 대비 cost가 너무 큼

- 상용화하긴 어렵지만, 그동안 factuality를 위해 진행되어 온 모든 모델을 잘 조합해서 성능이 높은 프레임워크?를 선보인 느낌

- 강점이 확실히 크긴 해서, 이렇게 필요한 정보만 업데이트할 수 있는 방식의 무언가..가 있으면 좋을거 같음.. 시도는 좋았다!
