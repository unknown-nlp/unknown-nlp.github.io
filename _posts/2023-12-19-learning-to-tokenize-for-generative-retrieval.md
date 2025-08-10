---
categories:
- paper-reviews
date: '2023-12-19 00:00:00'
description: 논문 리뷰 - Retrieval 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- embedding
- generative
- paper-review
- retrieval
- transformer
thumbnail: assets/img/posts/2023-12-19-learning-to-tokenize-for-generative-retrieval/thumbnail.jpg
title: Learning to Tokenize for Generative Retrieval
---

**논문 정보**
- **Date**: 2023-12-19
- **Reviewer**: 건우 김
- **Property**: Retrieval

{% include figure.liquid loading="eager" path="assets/img/posts/2023-12-19-learning-to-tokenize-for-generative-retrieval/image_000.jpg" class="img-fluid rounded z-depth-1" %}

# Abstract

- 본 연구에서는 generative retrieval 계열의 방법으로 document semantics을 docids로 encoding하는 과정을 학습하는 GENRET을 소개함. 

- 당연하게도 GENRET는 IR에서 SOTA를 보이고, 특히 unseen doc에 있어 높은 성능 향상을 보임.

# Introduction

최근 Information Retrieval에서 generative retrieval을 활용하는 연구들이 많이 진행되고 있다. 우리가 흔히 알고 있는 dense retrieval 방법들과 다르게, generative retrieval은 end-to-end 방법으로 주어진 query에 대해 ranked list of docids를 LM이 생성하게 함.

docid를 할당하는 것은 document가 semantic space에 어떻게 분포되어 있는지 정의하는 과정이기 때문에 중요함. 이전에는 주로 title 혹은 URL과 같은 meta data를 사용하거나 off-the-shelf document embedding에서 clustering 결과를 활용하는 rule-based 방법을 사용해서 training에서 본 것들에 대한 document들은 잘 retrieving 했지만, 이것들은 ad-hoc하고 generalize 못하다는 단점이 있다.

위 문제를 해결하기 위해 연구를 진행함

{% include figure.liquid loading="eager" path="assets/img/posts/2023-12-19-learning-to-tokenize-for-generative-retrieval/image_001.png" class="img-fluid rounded z-depth-1" %}

- **GENRET**: a document tokenization learning framework that learns to tokenize a document into semantic docids in a discrete auto-encoding scheme

- auto-encoding을 이용하여 generative retrieval model을 optimize하는데 아래와 같은 issue 존재

- **Contributions**

# Preliminaries

**document tokenization**: generative retrieval은 original document를 직접 생성하는 것은 길기 때문에 inefficient. document tokenization은 document를 sequence of discrete tokens (docid)로 표현함.

- D: collection of documents

- d: each document

- |d|: total number of tokens in document

- M: length of docid

- z: sequence of discrete tokens (docid)

- z_t: K-way categorical variable

- 위 그림에서는 M=3, K=64인 case

docid인 z는 아래 두가지 조건을 만족해야함.

1. different documents have short but different docids

1. docids capture the semantics of their associated documents as much as possible

**Tokenization model**: Q:d\to z, document d를 docid z로 mapping

**Generative retrieval model: ****P:q \to z****, **query q와 관련된 문서 docid z를 autoregressive하게 생성하며 학습함

# Method

document tokenization은 주로 fixed pre-processing step으로 사용됨

→ 이런 ad-hoc한 방법은 document의 semantic을 잘 잡아내지 못한다는 단점이 존재함.

**GENRET**: Semantic docid를 학습하는 discrete auto-encoding 기반의 tokenization leraning method

{% include figure.liquid loading="eager" path="assets/img/posts/2023-12-19-learning-to-tokenize-for-generative-retrieval/image_002.png" class="img-fluid rounded z-depth-1" %}

크게 세가지 components로 구성이 됨

1. **seq2seq based retrieval model: ****P(z|q)**

1. **document tokenization model: ****Q(z|d)**

1. **reconstruction model: ****R(d|z)**

### **Overview process**

→ document tokenization model Q가 document d를 unique discrete variables z로 변환시키고, retrieval model P가 given query q에 대해 z를 생성하도록 학습이됨. 추가로 Reconstruction model R은 docid z에서 original document를 생성하도록 학습이됨 (original document의 semantic을 파악하기 위해)

## Architecture

### Document Tokenization Model

- enc-dec Transformer: input text d가 있을 때, T5-based tokenization model이 d와 a prefix of docid z_{<t}를 인코딩하여 hidden latent vector d_t 생성.

{% include figure.liquid loading="eager" path="assets/img/posts/2023-12-19-learning-to-tokenize-for-generative-retrieval/image_003.png" class="img-fluid rounded z-depth-1" %}

- tokenization model은 d_t를 기반으로 각 document에 대한 token을 생성

- 각 timestep t 마다, codebook을 정의해줌

- codebook embedding matrix E_t와 latent vector d_t를 dot-prodcut softmax 취하여 j \isin [K]에 대한 t 시점에서의 확률값 계산, 

{% include figure.liquid loading="eager" path="assets/img/posts/2023-12-19-learning-to-tokenize-for-generative-retrieval/image_004.png" class="img-fluid rounded z-depth-1" %}

### Reconstruction Model

- tokenization model Q가 생성한 docid는 semantic 정보를 담아야하기에, auto-encoding training scheme 사용

- Input: docid z

- output: document d

### Retrieval-based reconstruction model

- docid z와 target document d 간의 relevance score는 다음과 같이 정의함

## Optimization

Document tokenization model, generative retrieval model, reconstruction model을 한 번에 auto-encoding을 활용하여 학습시키기에는 다음과 같은 이유로 어렵다.

1. **Learning docids in an autoregressive fashion**

1. **Generating docids with diversity**

### Progressive training scheme

- M번의 learning steps을 갖는 전체 learning scheme에서 docid z_T은 T \isin [M] 시점에 학습이 됨. 이후 시점에서는 이전 시점의 docid z_T와 parameters들은 fixed됨. 

{% include figure.liquid loading="eager" path="assets/img/posts/2023-12-19-learning-to-tokenize-for-generative-retrieval/image_005.png" class="img-fluid rounded z-depth-1" %}

- 아래 3가지 loss function을 통해 학습이 이루어짐

### Diverse clustering techniques

docids의 diversity를 보장하기 위해 아래 두가지 clustering techniques을 각 progressive training step에 적용함. 

1. **Codebook Initialization**

1. **Docid re-assignment**

# Experimental Setup

- enc-dec: T5-base

- retrieval model과 tokenization model에 사용되는 enc-dec, codebook 각각은 shared

- K number of clusters: 512

- M length of docid: 문서의 개수에 따라 달라짐

# Experimental Results

### NQ320K results

{% include figure.liquid loading="eager" path="assets/img/posts/2023-12-19-learning-to-tokenize-for-generative-retrieval/image_006.png" class="img-fluid rounded z-depth-1" %}

- strong pretrained retrieval GTR + previous SOTA in generative retrieval보다 우수한 성능 보임

- Seen + Unseen dataset에서 우수한 성능 보임 

### MS MARCO + BEIR results

{% include figure.liquid loading="eager" path="assets/img/posts/2023-12-19-learning-to-tokenize-for-generative-retrieval/image_007.png" class="img-fluid rounded z-depth-1" %}

- **MS MARCO**

- **BEIR**

### Qualitative analysis

NQ320K dataset에서 GENRET이 생성한 docid에 대한 시각화

- left: similar docids는 비슷한 content로 구성

- right: same group에 들어가는 docid는 semantically하게 비슷함

{% include figure.liquid loading="eager" path="assets/img/posts/2023-12-19-learning-to-tokenize-for-generative-retrieval/image_008.png" class="img-fluid rounded z-depth-1" %}

# Conclusion

본 연구에서 처음으로 generative retrieval 계열의 document tokenization learning method인 GENRET 소개함. 요약하면, generated docids가 semantics을 담게 설계된 auto-encoding 방식을 통해 documents를 discrete representations으로 tokenize하는 것을 학습함. 

Dense retrieval method 보다 안정적으로 높은 성능을 보이며, 특히 unseen dataset에서도 좋은 성능을 보인 것으로 미루어 보아 generative retrieval이 앞으로 IR에서 핵심 연구 주제가 되지 않을까 싶음

더 짧은 docids로 학습 및 infer해서 효율적이지만, training process가 복잡해서 computation cost가 높을 것 같은데, 이 점에 대한 dense retreival method와 비교 실험이 없어서 아쉬움.

이 아니고 appendix에 꼭 숨겨놨었네요

{% include figure.liquid loading="eager" path="assets/img/posts/2023-12-19-learning-to-tokenize-for-generative-retrieval/image_009.png" class="img-fluid rounded z-depth-1" %}

학습 속도는 느리긴 하지만, infer 속도는 가장 빠르다는 결론!

{% include figure.liquid loading="eager" path="assets/img/posts/2023-12-19-learning-to-tokenize-for-generative-retrieval/image_010.jpg" class="img-fluid rounded z-depth-1" %}
