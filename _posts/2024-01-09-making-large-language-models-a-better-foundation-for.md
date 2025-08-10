---
categories:
- paper-reviews
date: '2024-01-09 00:00:00'
description: 논문 리뷰 - LLM, Retrieval 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- embedding
- generative
- language-model
- llm
- paper-review
- pre-training
- retrieval
thumbnail: assets/img/posts/2024-01-09-making-large-language-models-a-better-foundation-for/thumbnail.jpg
title: Making Large Language Models A Better Foundation For Dense Retrieval
---

**논문 정보**
- **Date**: 2024-01-09
- **Reviewer**: 상엽
- **Property**: LLM, Retrieval

# Introduction

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-09-making-large-language-models-a-better-foundation-for/image_000.png" class="img-fluid rounded z-depth-1" %}

- **dense retrieval** : query와 document의 semantic 유사도를 반영할 수 있는 동일 latent space embedding을 만드는 것

- 활용처 : web search, open-domain QA, conversational system

- **Dense retrieval의 발전사**

- **LLM을 활용한 기존 retrieval의 한계점**

- **Contribution**

# Preliminary

**Text embedding**

- tokenized sequence T:[\mathrm{CLS}], \mathrm{t} 1, \ldots, \mathrm{tN},[\mathrm{EOS}]

- output embedding → text embedding 방법

**RepLLaMA**

- LLaMA 모델을 backbone decoder로 활용

- RankLLaMA (reranker)와 함께 text-retrieval 모델 제안

- text embedding of RepLLaMA

- InfoNCE loss를 이용해 학습.

# LLaRA 

- **LL**M **a**datpeted for dense **R**etriv**A**l (LLaRA)

- post-hoc adaptation of LLMs to improve their **usability for dense retrieval.**

- extended training stage of the **unsupervised** generative pre-training.

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-09-making-large-language-models-a-better-foundation-for/image_001.png" class="img-fluid rounded z-depth-1" %}

- **Objective **(remind)

- **Two pretext training tasks**

- **Text embedding**

- **Training objective**

→ LLaRA 특장점

- **기존 LLM 모델에 추가적인 module을 필요로 하지 않음.** sentence prediction은 LLM output 임베딩의 linear projection

- **competitive training efficiency** : simple한 목적함수 + 뒷 부분에 등장하는 LoRA를 말하는 것으로 보임.

- **there is no need to collect any labeled data** because LLaRA is performed purely based on the plain corpora.

# Experimental Study

- **Settings**

- **Analysis**

# Conclusion이라기보다는 나의 의견

- Unsupervised embedding + 간단한 목적함수로 학습 및 적용이 편할 거란 생각은 듦.

- 정말로 최초의 시도인지에 대해서는 잘 모르겠음. LLM을 어떻게 활용하는가에 따라 다르게 해석가능할듯.

- 코드가 나오면 한 번쯤 사용해보고 싶긴하다.

- RepLLaMA + RankLLaMA는 retrieval + rerank까지 다 포함한 전체적인 IR 내용을 다뤘다면 여기는 Retrieval만 다루고 있음.

- objective 2를 달성하기 위해 next sentence prediction을 활용하는 것에 대한 가정 “query → document (passage)로 이뤄진 문장 구조”가 얼마나 현실적인지는 모르겠다. 

- document retrieval로써 next sentence prediction의 효용은?

- BAAI 그룹은 text embedding에 진심인 것 같다. (리더보드)
