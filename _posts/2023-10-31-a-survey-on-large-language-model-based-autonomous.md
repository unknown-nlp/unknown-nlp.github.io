---
categories:
  - paper-reviews
date: "2023-10-31 00:00:00"
description: 논문 리뷰 - Autonomous-Agents 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
  - alignment
  - autonomous-agents
  - fine-tuning
  - language-model
  - llm
  - paper-review
  - transformer
thumbnail: assets/img/posts/2023-10-31-a-survey-on-large-language-model-based-autonomous/thumbnail.jpg
title: A Survey on Large Language Model based Autonomous Agents
---

**논문 정보**

- **Date**: 2023-10-31
- **Reviewer**: 건우 김
- **Property**: Autonomous-Agents

# Abstract

이전까지 Autonomous agent는 제한된 환경에서 제한된 knowledge를 가지고 agent를 training시키는 것에 초점이 맞추어져 와서 사람이 학습하는 과정과 다른 점이 많았기 때문에, agent가 human-like decision을 수행하기는 어려워 왔음. 하지만 human-level intelligence의 가능성을 보여준 최근 LLM의 등장으로 인해 LLM-based autonomous agents들이 연구가 많이 되어 왔고, 본 연구에서는 해당 연구의 전반적인 내용을 다음과 같이 정리함.

- LLM-based autonomous agents의 **구성**을 설명

- LLM-based autonomous agents를 다양한 **application**에 적용한 사례

- LLM-based autonomous agents를 어떻게 **평가**하는지

# 1. Introduction

사람들이 흔히 말하는 AGI를 달성하기 위해서는 self-directed planning과 action을 통해 task를 수행하는 autonomous agents가 필수적이라는 말이 많았음. 이전 연구들은 주로 agents가 heuristic한 policy를 기반으로 제한된 환경에서 action을 수행하는 식으로 이루어졌는데, abstract에서 언급한 내용과 동일하게 이는 human learning process와 많이 다르기 때문에 접근 자체가 잘못된다는 평가를 많이 받고 있음 → human-level decision process를 모방하지 못함

최근에 LLM 연구가 많이 진행이 되며, LLM이 human-like intelligence를 갖고 있다고 보고 있음. 이 능력을 통해 autonmous agents를 구축할 때, LLM을 central controller로 두고 아래와 같은 연구가 많이 진행됨.

{% include figure.liquid loading="eager" path="assets/img/posts/2023-10-31-a-survey-on-large-language-model-based-autonomous/image_000.png" class="img-fluid rounded z-depth-1" %}

LLM-based autonomous agents들의 정리가 되었던 적이 없었기에, 본 연구에서 세가지 관점으로 다음 내용을 정리하고자 함.

1. **construction of LLM-based autonomous agents**

1. **application of LLM-based autonomous agents**

1. **evaluation of LLM-based autonomous agents**

# 2. LLM-based autonomous Agent Construction

LLM을 autonomouns agent로 사용하기 위해서 아래 두 가지 내용이 중요함

1. LLMs을 더 잘 사용하기 위해 적절한 architecture는 무엇인가?

1. 특정 task를 달성하기 위해 어떻게 agent의 능력을 어떻게 끌어올릴까?

## 2.1 Agent Architecture Design

LLM이 다양한 task를 수행할 수 있게 하기 위해 QA format을 사용했지만, autonomous agent는 사람처럼 특정 역할을 이행하고 환경으로부터 자동으로 인식하고 학습해야 한다는 점에서 QA와는 다소 거리가 멀다.

→ traditional LLM과 autonomous agent의 이런 간극을 채우기 위한 **rational agent architecture**를 구상해야 하며, 최근 연구들은 LLM을 autonmous agent 역할을 수행할 수 있게 하기 위해 다양한 모듈을 개발함. 본 연구에서 이러한 모듈을 구성하는 unified framework를 제안함.

{% include figure.liquid loading="eager" path="assets/img/posts/2023-10-31-a-survey-on-large-language-model-based-autonomous/image_001.png" class="img-fluid rounded z-depth-1" %}

4가지 모듈이 소개되며, 각 module의 주요 기능을 간략하게 소개하면

- **profiling module**: agent의 역할을 확인

- **memory and palnning modules**: agent를 dynamic enviornment에 던져 이전 행동을 기반으로 미래의 action을 설계할 수 있게함

- **action module**: agent의 decision을 특정 output의 형태로 반환시킴

### 2.1.1 Profiling Module

Profiling module은 agent role의 profile을 prompt 형식으로 나타나게 함으로써 LLM behavior에 영향을 준다. Profile은 주로 (age, gender, career, psychology info)등을 포함하며 agent의 성격과 social 정보를 형성함. → profile을 만드는데 3가지 방법이 주로 사용됨

- **Handcrafting Method**: 사람이 직접 agent profiles을 구축하는 방법으로 flexible하다는 점은 용이하지만, agent의 수가 많을 때 labor-intensive하다는 단점 존재

- **LLM-generation Method**: LLM을 통해 agent profile을 생성함. agent의 수가 많아도 사용할 수 있긴 하지만, generated profiles에 대한 precise control이 어렵다는 단점 존재

- **Dataset Alignment Method**: real-world dataset을 통해 agent profile을 얻음. 실제 human 정보를 natural language prompt를 통해 구성하고, 이를 활용하여 agent를 프로파일링 진행

### 2.1.2 Memory Module

Environment에서 얻은 정보들을 저장하고 future action을 수행하기 위해 recoreded memories를 활용함으로써 memory module은 agent가 experience 혹은 self-evolve 등의 정보를 축적하고 consistent, reasonable, effective 한 방식으로 행동하게 도와줌. 이것이 Traditional LLM과 가장 다른 핵심적인 요소이며, memory module을 통해 agent의 과거 행동을 축적하며, 이를 바탕으로 dynamic environment 상황에서 agent가 새로이 학습하고 일을 수행할 수 있음.

Memory module을 구성하는 주요 요인들은 아래와 같음.

- **Memory Structures**: 인간의 memory process를 다루는 방식으로 설계됨. 인간은 오감을 통해 input을 받아 들여 short-term memory와 long-term memory로 저장함. Memory structure를 design할 때, Transformer 모형의 context window를 short-term memory로 보고 external vector storage를 long-term memory로 봄

- **Memory Formats: **Memory storage 형태에 따른 종

- **Memory Operations:** memory module이 agent가 environment와 소통하여 얻은 지식을 축적하게 하는데, environment와 소통하는 것이 주로 세 가지 operation을 통해 이루어짐.

### 2.1.3 Planning Module

사람들도 복잡한 문제를 만나면, 작은 여러 문제로 쪼개어 각각 푸는 경향이 있음. 이 module 역시 agent로 하여금 더 합리적으로 행동하게 하기 위해 planning을 사용함.

{% include figure.liquid loading="eager" path="assets/img/posts/2023-10-31-a-survey-on-large-language-model-based-autonomous/image_002.png" class="img-fluid rounded z-depth-1" %}

- **Planning without Feedback**: future behavior에 영향이 갈만한 어떠한 feedback도 받지 않는 경우

- **Planning with Feedback:** Real world에서 복잡한 task를 풀기 위해 agent는 long-horizon planning을 만들 필요가 있음. Feedback이 없는 planning module은 다음과 같은 문제점들이 있음

### 2.1.4 Action Module

Action module은 agent의 decision을 특정 outcome 형태로 변환해주는 역할을 담당함. 이 모듈은 앞에서 다룬 profile, memory, plannning 세 가지 modules에 의해 영향을 받음. 저자는 아래 네 가지 내용을 중심으로 action module을 설명함.

- **Action Goal**: agent는 다양한 objective를 기반으로 action을 수행하는데, 아래 대표적인 케이스가 있음

- **Action Production**: input-output이 직접적으로 연관되어 있는 일반적인 LLM과 다르게, agent는 다른 sources를 통해 action을 수행함. 두 가지 종류의 action production strategies로 구분 지음

- **Action Space**: agent가 수행할 수 있는 action의 집합을 external / internal 관점으로 나누어 볼 수 있

- **Action Impact:** 말 그대로 action의 결과를 지칭하며, 아래와 같이 세 가지 영향만 다룸

## **2.2 Agent Capability Acquistion**

2.1에서 agent가 사람처럼 일을 수행하기 위해 agent architecture를 어떻게 구성하는지 다룸. 여기서는 agent가 task-specific 능력을 향상시키는 방법들에 대해서 다룸. (w/ fine-tuning, w/o fine-tuning)

1. **Capability Acquistion with Fine-tuning**

1. **Capability Acquistion without Fine-tuning**

# **3. LLM-based Autonomous Agent Application**

{% include figure.liquid loading="eager" path="assets/img/posts/2023-10-31-a-survey-on-large-language-model-based-autonomous/image_003.png" class="img-fluid rounded z-depth-1" %}

정말 다양한 분야의 연구 및 모델들이 소개되어 왔음

{% include figure.liquid loading="eager" path="assets/img/posts/2023-10-31-a-survey-on-large-language-model-based-autonomous/image_004.png" class="img-fluid rounded z-depth-1" %}

# 4. LLM-based Autonmous Agent Evaluation

## 4.1 Subjective Evaluation

- Human Annotation: 사람이 agents들이 생성한 response에 대해 직접 scoring, ranking 등 평가

- Turing Test: 사람이 agent와 사람이 생성한 response 중 더 사람 같은 것을 선택하는 방법

## 4.2 Objective Evaluation

Objective evaluation을 수행하기 위해서는 아래 세 가지 주요 내용들을 (metrics, protocols, benchmakrs) 살펴야 함.

1. Metrics

1. Protocols: 위에 metrics을 어떤 상황에서 사용하는지 중요함

1. Benchmarks: 지금까지 Minecraft, ALFWorld와 같은 benchmark에서 agent의 성능을 평가함.

22년 7월부터 23년 8월까지 Evaluation strategy에 대해 정리된 Table이며, 생각보다 연구가 많이 됨

{% include figure.liquid loading="eager" path="assets/img/posts/2023-10-31-a-survey-on-large-language-model-based-autonomous/image_005.png" class="img-fluid rounded z-depth-1" %}

# 5. Challenges

- Role-playing Capability

- Genearlized Human Alignment

- Prompts Robust

- Hallucination

- Knowledge Boundary

- Efficiency

# Conclusion

최근에 언급이 많이 되고 있는 LLM-based autonomous agents에 대한 survey paper를 review 했고, 논문은 construction, application, evaluation 크게 세 갈래의 주제로 작성됨.

읽어 보니 LLM-based autonomous agents가 완전히 새로운 분야라기 보다는 LLM을 활용해서 simulation에 적합한 agent를 만드는 것으로 우리가 기존에 알고 있는 내용들로 충분히 이해가 가능.

따라서, 기존 LLMs에서 자주 연구되던 내용들이 Autonomous Agents에도 직접적으로 영향을 끼치므로 앞으로 LLMs skills + autonomous agents 다 중요하게 봐야 한다고 생각함.
