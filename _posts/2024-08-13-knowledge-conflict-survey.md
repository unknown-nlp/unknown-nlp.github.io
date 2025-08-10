---
categories:
- paper-reviews
date: '2024-08-13 00:00:00'
description: 논문 리뷰
giscus_comments: true
layout: post
related_posts: false
tags:
- language-model
- llm
- paper-review
thumbnail: assets/img/posts/2024-08-13-knowledge-conflict-survey/thumbnail.jpg
title: Knowledge conflict survey
---

**논문 정보**
- **Date**: 2024-08-13
- **Reviewer**: yukyung lee

## 1. Introduction

***Definition of Knowledge Conflict***

- In-depth analysis of knowledge conflicts for LLM

- Three types of knowledge conflicts

- knowledge conflict가 일어나는 상황을 noise나 misinformation이 있는 상황에서 parametric knowledge와의 충돌로 보고있는듯 (abstract)

- 이 논문의 궁극적인 목표는 conflict를 해결해서 LLM의 robustness를 향상시키는 것으로 보임

***Key terms***

- Parametric knowledge (memory): LM’s world knowledge

- External contextual knowledge (context): user prompt, dialogues, retrieved documents

- knowledge conflict: The discrepancies among the contexts and the model’s parametric knowledge are referred to as knowledge conflicts

***Knowledge Conflict (Causes - Phenomenon- Behaviors)***

: lifecycle of knowledge conflicts as both a cause leading to various behaviors,
and an effect emerges from the intricate nature of knowledge

{% include figure.liquid loading="eager" path="assets/img/posts/2024-08-13-knowledge-conflict-survey/image_000.png" class="img-fluid rounded z-depth-1" %}

- Knowledge conflict is originally rooted in ODQA (answer→ short / yellow) 

- Timing relative to potential conflicts: pre-hoc, post-hoc strategies

***Taxonomy***

{% include figure.liquid loading="eager" path="assets/img/posts/2024-08-13-knowledge-conflict-survey/image_001.png" class="img-fluid rounded z-depth-1" %}

***Related Dataset***

{% include figure.liquid loading="eager" path="assets/img/posts/2024-08-13-knowledge-conflict-survey/image_002.png" class="img-fluid rounded z-depth-1" %}

## 2. Context-Memory Conflict

> *This static parametric knowledge stands in stark contrast to the dynamic nature of external information, which evolves at a rapid pace (De Cao et al., 2021; Kasai et al., 2022)*

{% include figure.liquid loading="eager" path="assets/img/posts/2024-08-13-knowledge-conflict-survey/image_003.png" class="img-fluid rounded z-depth-1" %}

- Causes: *Why do context-memory conflicts happen*?

- Analysis: *How do LLMs navigate context-memory conflicts?*

- Solution: * What strategies are there to deal with context-memory conflicts*?

## 3. Inter-Context Conflict

***Outdated Information***

- Facts can evolve !

- Some findings

***Solutions***

- Eliminating Conflict (유의미하게 참고할 것들은 없는듯)

- Improving Robustness 

## 4. Intra-Memory Conflict

{% include figure.liquid loading="eager" path="assets/img/posts/2024-08-13-knowledge-conflict-survey/image_004.png" class="img-fluid rounded z-depth-1" %}

- Definition: LLM의 **parametric knowledge 내부 **(latent representation)에서의 inconsistency들로 인해 발생되는 문제

- Causes: IM이 발생하는 원인은 어떤게 있을까?

- Analysis

- Solutions

## 5. Challenges and Future Directions

**Knowledge Conflicts in the Wild**

- Retrieval Augmented Language Model에서 자주 일어날 수 있는 상황

**Solution at a Finer Resolution**

- User query is important : subjective or debatable questions lead to conflicts

- the source of conflicting information can vary ; mis info/ outdated facts/ partially corrected data

- User expectation

**Evaluation on Downstream Tasks**

- 대부분의 연구들이 QA를 사용하는데, broder implication을 고려하여 다양한 task를 평가해봐야 한다고 주장

**Interplay among the Conflicts**

- internal knowledge inconsistency를 잘 잡아내는게 중요
