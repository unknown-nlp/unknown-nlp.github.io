---
categories:
- paper-reviews
date: '2024-03-26 00:00:00'
description: 논문 리뷰 - Retrieval 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- language-model
- llm
- paper-review
- reasoning
- retrieval
thumbnail: assets/img/posts/2024-03-26-search-in-the-chain-interactively-enhancing-large-language/thumbnail.jpg
title: 'Search-in-the-Chain: Interactively Enhancing Large Language Models with Search
  for Knowledge-intensive Tasks'
---

**논문 정보**
- **Date**: 2024-03-26
- **Reviewer**: 상엽
- **Property**: Retrieval

# Introduction

LLM의 여전한 한계

1. 다양한 지식들을 합쳐서 추론하는 것에 대한 어려움.

1. memorization of long-tail and real-time knowledge

1. hallucination

1. reference없이 context만으로 생성하는 것은 traceability가 떨어지면 신뢰하기 어려움.

→ Retrieval-augmented method는 위의 문제들을 외부 지식과 모델을 결함시킴으로써 일부 해결

Retrieval-agumneted method를 도입할 때 역시 문제 존재

C-1 : IR을 LLM reasoning process에 바로 이용하는 것은 LLM의 reasoning chain을 훼손할 때도 있음. (LLM이 local sub-question reason만 하기 때문에) ← IR의 결과물이 들어가기 때문에 발생하는 문제점 + sub-question에 집중한 reasoning 방식

C-2 : IR 결과 vs LLM 자체 지식의 충돌 → 잘못된 결과를 만들 가능성이 존재.

C-3 : reasoning direction을 수정할 방법이 없음. (조금 억지)

Search-in-the-Chain (SearChain) 제안

- IR-LLM interaction round를 여러 번 진행

- IR-LLM interaction : reasoning → (verification → completion) 반복 → tracing

- 그림을 보자.

{% include figure.liquid loading="eager" path="assets/img/posts/2024-03-26-search-in-the-chain-interactively-enhancing-large-language/image_000.png" class="img-fluid rounded z-depth-1" %}

1. CoQ를 만들기 위해 In-context learning 이용 복잡한 질문을 풀기 위한 IR-oriented query 형태로 분해해서 구성

1. 각 노드에 대해 IR과 상호작용 진행, 구체적으로 아래 두 단계를 선택적으로 반복

1. **tracing** : reasoning process를 만들고 각 reasoning step을 support하는 reference 선택

**Main contribution**

- We highlight the challenges in introducing IR into LLM from the perspectives of reasoning and knowledge. → ??? LLM에 IR을 도입할 때 있는 문제는 대체로 알던 거 아닌가?

- SearChain not only improves the knowledge-reasoning ability of LLM but also uses IR to identify and **give the knowledge that LLM really needs**. Besides, SearChain can **mark references to supporting documents** for the knowledge involved in the generated content.

- Interaction with IR in **SearChain forms a novel reasoning path: node-identify Depth-first Search on a tree**, which enables LLM to dynamically modify the direction of reasoning.

- Experiment shows that SearChain **outperforms state-of-the- art baselines** on complex knowledge-intensive tasks including multi- hop Q&A, slot filling,  fact checking and long-form Q&A. → SOTA

# Related work

# Method

### Chain-of Query Generation

- In-context learning 이용

- global reasoning chain for complex question

- Prompt

### Interaction with IR

- CoQ의 각 노드에 대해 IR을 이용해 다음의 작업을 반복 - verification, completion

- IR의 결과를 바탕으로 CoQ의 결과를 수정 → new branch of ToR (Tree of Reasoning)

- Top-1 retreived document를 supporting document로 이용

- 더 이상 노드에 대한 수정이 필요없어지면 라운드 종료

- correct reasoning path와 supporting document를 이용해 답변 생성

- Algorithm

**Verification**

- IR 결과를 바탕으로 CoQ 각 노드의 정답이 맞는지 확인

1. retrieved Top-1 document d_i → ODQA 데이터셋으로 학습된 reader(DPR) 이용해 answer g 추출

1. a_i와 g 비교

1. a_i와 g의 결과가 일치하지 않음  &  f > \theta (IR로 인한 성능 감소를 막기 위한 threshold)

**Completion**

- missing knowledge를 갖는 노드의 정답을 보충

- [Unsolved Query]에 대해 진행

- f값에 관계없이 다음 prompt 실행

- a_i → a^{\star}_{i} 변경 후, (q_i, a^{\star}_{i})를 root 노드로 하여 새로운 CoQ 진행

**Tracing**

- reasoning process 생성 및 각 노드에 대해 supporting document mark

- prompt

**Node-identify Depth-first Search**

- SearChain이 만드는 reasoing path

- Depth first search와 같이 정답이 해결되거나 unsolvable sub-question이 존재하면 계속 reasoning한다는 점에서 동일

- “node-identify” : 하나의 search direction이 끝날 때 parent node로 가는 것이 아니라 node verification과 completation을 통해 시작 node를 결정한다는 것이 다름.

- LLM - IR 상호작용을 통해 동적으로 reasoning direction을 결정

# Experiments

### Experimental setup

- Datasets

- Evaluation Metric

- Baselines

- implementation

### Main Results

{% include figure.liquid loading="eager" path="assets/img/posts/2024-03-26-search-in-the-chain-interactively-enhancing-large-language/image_001.png" class="img-fluid rounded z-depth-1" %}

- **Effect of Chain-of-Query**

- **Effect of interaction with IR**

### Analysis

**KnowledgeDecoupling**

- 4 multi-hop QA datasets의 knowledge source에 대해 분석

**Positive and Negative Effects of IR on LLM**

{% include figure.liquid loading="eager" path="assets/img/posts/2024-03-26-search-in-the-chain-interactively-enhancing-large-language/image_002.png" class="img-fluid rounded z-depth-1" %}

- (a) Positive

- (b) Negative

**CoQ vs Baselines in Reasoning**

성능 외 reasoning을 평가하기 위한 두 가지 측면 추가적으로 제시

{% include figure.liquid loading="eager" path="assets/img/posts/2024-03-26-search-in-the-chain-interactively-enhancing-large-language/image_003.png" class="img-fluid rounded z-depth-1" %}

- reasoning step의 수

- 어려운 sub-question 해결력

**SearChain vs New Bing in Tracing**

{% include figure.liquid loading="eager" path="assets/img/posts/2024-03-26-search-in-the-chain-interactively-enhancing-large-language/image_004.png" class="img-fluid rounded z-depth-1" %}

SearChain과 New bing search를 아래 두 가지 측면에서 비교

- Scope of Knowledge Coverage (SKC) [0, +]: 

- Accuracy of Marking Position (AMP) [0, 1]

**Efficiency Analysis**

{% include figure.liquid loading="eager" path="assets/img/posts/2024-03-26-search-in-the-chain-interactively-enhancing-large-language/image_005.png" class="img-fluid rounded z-depth-1" %}

n : LLM의 input
