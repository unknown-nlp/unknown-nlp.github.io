---
categories:
- paper-reviews
date: '2024-02-20 00:00:00'
description: 논문 리뷰 - Retrieval, ICL, QA, Knowledge 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- bert
- gpt
- icl
- knowledge
- language-model
- llm
- paper-review
- qa
- retrieval
thumbnail: assets/img/posts/2024-02-20-wikichat-stopping-the-hallucination-of-large-language-model/thumbnail.jpg
title: 'WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot
  Grounding on Wikipedia'
---

**논문 정보**
- **Date**: 2024-02-20
- **Reviewer**: 김재희
- **Property**: Retrieval, ICL, QA, Knowledge

## 1. Intro

> Wikipedia 기반 Knowledge Grounded Conversation 특화 언어모델

- LLM : Hallucination 현상이 매우 심함

- RALM : Query 관련 정보를 Retrieval하여 추가 정보로 입력하자. 

- ROME : 모델의 내부 파라미터를 수정하여 지식을 업데이트하자. 

- Knowledge Grounded Task 평가 방식

> **Contribution
**1. 광범위한 지식, 그 중에서도 모델 학습 이후 발생하는 지식을 이용한 효과적인 대화 모델 프레임워크 및 평가 방법론 제안
2. Knowledge Base 변경을 통해 개인정보 및 기업 내부 정보에 대해서도 활용 가능

## 2. Method

{% include figure.liquid loading="eager" path="assets/img/posts/2024-02-20-wikichat-stopping-the-hallucination-of-large-language-model/image_000.png" class="img-fluid rounded z-depth-1" %}

- LLM : GPT-3.5/GPT-4/LLaMA-1

- Retriever : ColBERT + PLAID(reranker)

### 1단계 Search Query 작성

- Retrieval을 위한 Query 작성

- Input : User Query + history → 특히 입력 정보의 시점을 함께 Prompting

- Retriever가 N_{IR}개의 Passage 반환

### 2단계 Passage 내 필요 정보 추출

- Passage에는 현재 User Query와 관련된 정보와 관련없는 정보가 혼재

- Bullet Point를 통해 Passage의 정보를 요약/필터링하도록 Promping

### 3단계 LLM 단독 Response 생성

- Retrieve된 정보를 이용하지 않고 User Query에 대한 Response 생성

- 해당 과정에서 생성된 Response는 신뢰도가 낮음

{% include figure.liquid loading="eager" path="assets/img/posts/2024-02-20-wikichat-stopping-the-hallucination-of-large-language-model/image_001.png" class="img-fluid rounded z-depth-1" %}

### 4단계 Response 분해 

- 3단계에서 생성된 Response 초안을 Claim 단위로 분해

- 분해 과정에서 발생할 수 있는 Coreference 문제를 해결하도록 Prompting

- 대화 기준 날짜를 직접 명시하여 날짜에 다른 지식 변화 고려

- K-Shot Prompting

{% include figure.liquid loading="eager" path="assets/img/posts/2024-02-20-wikichat-stopping-the-hallucination-of-large-language-model/image_002.png" class="img-fluid rounded z-depth-1" %}

{% include figure.liquid loading="eager" path="assets/img/posts/2024-02-20-wikichat-stopping-the-hallucination-of-large-language-model/image_003.png" class="img-fluid rounded z-depth-1" %}

- 각각의 Claim에 대해 Retriever을 이용하여 N_{evidence}개의 Passage 탐색

### 5단계 Claim 검증

- 4단계에서 마련된 (claim-passage) tuple을 이용하여 prompting

- 모델은 각 claim이 (사실, 거짓, 판별불가)인지 분류

### 6단계 실제 Response 초안 작성

- 5단계에서 사실로 판별된 claim이 있을 경우에만 수행

- 2단계에서 생성한 passage 요약을 prompting하여 response 생성

### 7단계 Response 정제

- 6단계에서 생성한 Response를 다시 Prompting하여 Feedback 작성 → 반영

- Feedback 기준 

- Feedback: 각 기준에 대해 0-100점

- Refinement : feedback 생성 시점 이후에 바로 정제하도록 prompting

- K-Shot Prompting

### Distillation to LLaMA

- 각 단계별 input, output을 pair로 하여 LLaMA2 Finetune 진행

- 대화 데이터 : User Simulator Framework를 이용하여 다양한 지식에 대해 이야기하는 데이터셋 구축 → GPT-4 이용

- Knowledge : Head, Tail, Recent로 구분하여 구축

### Summary

- Retrieval, Summarization, Refinement의 반복을 통해 답변의 품질 개선 프레임워크

## 3. Evaluation

### Factuality 

- 답변이 정말 사실 정보를 바탕으로 생성되었는지 평가

- GPT-4 + human을 통해 Response의 Factuality 평가

### Conversationality

- 답변의 챗봇 응답으로서 품질

## 4. Experiments

### Main Results

{% include figure.liquid loading="eager" path="assets/img/posts/2024-02-20-wikichat-stopping-the-hallucination-of-large-language-model/image_004.png" class="img-fluid rounded z-depth-1" %}

- All 

- Head vs Tail

- Recent 

### Latency

{% include figure.liquid loading="eager" path="assets/img/posts/2024-02-20-wikichat-stopping-the-hallucination-of-large-language-model/image_005.png" class="img-fluid rounded z-depth-1" %}

- Retrieval와 Generation을 매우 여러번 반복하면서 비용과 시간 손해가 매우 큼

- 프레임워크 특성 상 Prompt가 매우 길어져서 불가피한 속도/비용 손해

### Human Evaluation

{% include figure.liquid loading="eager" path="assets/img/posts/2024-02-20-wikichat-stopping-the-hallucination-of-large-language-model/image_006.png" class="img-fluid rounded z-depth-1" %}

- Human Evaluation 결과 기존 LLM 대비 좋은 성능 기록

{% include figure.liquid loading="eager" path="assets/img/posts/2024-02-20-wikichat-stopping-the-hallucination-of-large-language-model/image_007.png" class="img-fluid rounded z-depth-1" %}

- “I Don’t Know”라고 응답한 비중

{% include figure.liquid loading="eager" path="assets/img/posts/2024-02-20-wikichat-stopping-the-hallucination-of-large-language-model/image_008.png" class="img-fluid rounded z-depth-1" %}

- refinement 전/후 응답의 BLEU Score 평균

## 7. Conclusion

- 숫자로 보면 매우 좋은 방법론처럼 보임. 

- Prompting과 Retrieval을 극단으로 결합한 프레임워크

- 사실성이 정말 중요한 경우라면 해당 프레임워크 도입 or 개선이 가능할듯

- 당장 해당 방법론이 정말 좋다고 이야기 X
