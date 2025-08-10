---
categories:
  - paper-reviews
date: "2025-01-21 00:00:00"
description: 논문 리뷰
giscus_comments: true
layout: post
related_posts: false
tags:
  - gpt
  - llm
  - paper-review
thumbnail: assets/img/posts/2025-01-21-agent-laboratory-using-llm-agents-as-research-assistants/thumbnail.jpg
title: "Agent Laboratory: Using LLM Agents as Research Assistants"
---

**논문 정보**

- **Date**: 2025-01-21
- **Reviewer**: 상엽

# Introduction

사람의 자원 한계로 인해 탐색할 수 없는 많은 리서치 분야가 있음.

LLM을 활용한 자동화를 통해 리서치 탐색의 영역을 획기적으로 늘릴 수 있음.

- **ResearchAgent (Baek et al. (2024))**

- **The AI Scientist (Lu et al. (2024a))**

→ Si et al. (2024)

**Agent Laboratory**

- Human idea + LLM을 활용한 보조 (사람의 feedback level은 다양하게 가능!)

- Human research idea → research report & code repository

**Contribution**

1. 개인의 리서치 역량을 향상시킬 수 있는 **오픈소스 LLM 모델 제공** (다양한 compute 레벨 지원)

1. 사람 평가 결과 (실험 및 리포트 quality, 유용성): **o1-preview > o1-mini > gpt-4o**

1. Neurips 점수 기준, 사람의 평가와 automated-evaluation의 점수 격차가 매우 컸음. → 평가를 위해서 **Human feedback이 필수적**임.

1. Overall score: **Co-pilot mode > autonomous mode**, Co-pilot 모드의 경우 experimental quality와 usefulness trade-off도 존재

1. The co-pilot 모드는 **utility와 usability에서 긍정적인 답변**을 받았고 사람들은 향후에도 사용하고 싶어함.

1. 비용과 추론 시간에 대한 분석 수행, 기존 모델 대비 **저렴한 비용**으로 작업 수행

1. **MLE-Bench에서 SOTA** 성능을 보이는 mle-solver 제안

# Agent Laboratory

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-21-agent-laboratory-using-llm-agents-as-research-assistants/image_000.png" class="img-fluid rounded z-depth-1" %}

3 Phases: (1) Literature Review, (2) Experimentation, and (3) Report Writing.

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-21-agent-laboratory-using-llm-agents-as-research-assistants/image_001.png" class="img-fluid rounded z-depth-1" %}

- role

- Task instruction

- command description

- context: 찾은 자료

- History: agent 행적

- …

### Literature Review

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-21-agent-laboratory-using-llm-agents-as-research-assistants/image_002.png" class="img-fluid rounded z-depth-1" %}

**Literature Review Phase**: 다음 단계 레퍼런스를 위해 관련 리서치 논문을 찾는 작업.

PhD agent: arXiv API를 활용해 아래 3가지 main actions을 수행.

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-21-agent-laboratory-using-llm-agents-as-research-assistants/image_003.png" class="img-fluid rounded z-depth-1" %}

- **_summary_**: agent에 의해 생성된 쿼리와 관련성이 높은 20개의 paper를 추출.

- **_full text_**: paper의 전체 content를 추출.

- **_add paper_**: summary와 full text를 이용해 curated review를 만듦.

- 위의 과정은 반복적으로 실행 (다수의 쿼리를 이용)하며 매 스텝에서 selection을 진행하여 최종적으로 N_max의 레퍼런스가 확보되면 종료

### Experimentation

**Plan Formulation phase: **literature review와 goal을 기반으로 하여 자세하고 실행가능한 리서치 계획을 세우는 작업

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-21-agent-laboratory-using-llm-agents-as-research-assistants/image_004.png" class="img-fluid rounded z-depth-1" %}

PhD & Postdoc agent: 대화를 통한 협업 진행

- 리서치 목표를 어떻게 달성할지에 대해 구체화

- 실험 구성 요소에 대한 설계 (머신러닝 모델)

- 어떤 데이터셋을 사용할 것인지 등

→ Consensus에 도달하면 Postdoc agent가 **plan** command를 실행하며 생성된 plan을 다음 단계로 전달

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-21-agent-laboratory-using-llm-agents-as-research-assistants/image_005.png" class="img-fluid rounded z-depth-1" %}

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-21-agent-laboratory-using-llm-agents-as-research-assistants/image_006.png" class="img-fluid rounded z-depth-1" %}

**Data Preparation phase**

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-21-agent-laboratory-using-llm-agents-as-research-assistants/image_007.png" class="img-fluid rounded z-depth-1" %}

목적: 실험 진행을 위한 데이터셋을 준비하는 코드를 작성

ML Engineer

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-21-agent-laboratory-using-llm-agents-as-research-assistants/image_008.png" class="img-fluid rounded z-depth-1" %}

- **Python **command를 활용해 코드를 실행

- HuggingFace dataset에 접근해 검색 실행 (**search HF** command)

SW Engineer

- code 최종 승인 후, **submit **command

- 최종 승인 전 python compiler를 통해 코드 실행, compile 관련 에러가 없어질 때까지 반복 실행

**Running Experiments phase**

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-21-agent-laboratory-using-llm-agents-as-research-assistants/image_009.png" class="img-fluid rounded z-depth-1" %}

ML Engineer: 이전 실험 계획을 수행하는 것이 목표

**mle-solver 활용**: 코드 생성, 테스트, 수정에 특화된 모듈

- 리서치 plan과 레퍼런스에서의 insight에 따라 initial code 작성 from scratch

- 절차 (top scoring program: 성능이 가장 높은 파일을 기준으로 수정, 대체 작업을 하는 것)

**Results Interpretation**

Phd & Postdoc agent간 토론을 통해 실험 결과로부터 유의미한 인사이트를 추출

### Report Writing

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-21-agent-laboratory-using-llm-agents-as-research-assistants/image_010.png" class="img-fluid rounded z-depth-1" %}

**Report Writing**

**PhD & Professor agent는 paper-solver를 활용해 최종 보고서를 작성하는 역할을 함.**

완전한 논문을 작성하는 것은 아니며 이전 결과물들을 readable한 형태로 정리하고 보고서로 만드는 것이 목적

1. Initial Report Scaffold

1. Arxiv Research

1. Report Editing

1. Paper Review

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-21-agent-laboratory-using-llm-agents-as-research-assistants/image_011.png" class="img-fluid rounded z-depth-1" %}

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-21-agent-laboratory-using-llm-agents-as-research-assistants/image_012.png" class="img-fluid rounded z-depth-1" %}

- 각 iteration을 돌 때 마다 글을 평가하기 위해 LLM을 활용한 자동화 된 리뷰 시스템을 활용

- Neurips 가이드라인을 기준으로 prompt를 구성

- ICLR 2022 논문을 평가할 시 인간 수준의 정확도를 보였음.

**Paper Refinement**

세 명의 reviewer agent를 활용해 peer review 단계를 모방, 각각의 평가에 대해 분석 후 Phd agent는 작성을 완료할지 이전 단계로 돌아가 글을 수정할지를 결정

### Autonomous vs Co-Pilot Mode

- Autonomous mode: 사람은 연구 아이디어만 제공

- Co-Pilot mode: 사람은 각 subtask별로 리뷰를 진행

# Results

## Autonomous Mode

### **글의 Quality 평가**

experiment quality, report quality, usefulness 측면에서 사람 평가 진행

- **Experimental Quality**: What is your perception of the quality of the experimental results presented in this report?
