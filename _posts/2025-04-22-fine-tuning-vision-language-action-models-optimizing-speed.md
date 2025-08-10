---
categories:
- paper-reviews
date: '2025-04-22 00:00:00'
description: 논문 리뷰
giscus_comments: true
layout: post
related_posts: false
tags:
- diffusion
- fine-tuning
- multimodal
- paper-review
- vision
thumbnail: assets/img/posts/2025-04-22-fine-tuning-vision-language-action-models-optimizing-speed/thumbnail.jpg
title: 'Fine-tuning Vision-Language-Action Models: Optimizing Speed and Success'
---

**논문 정보**
- **Date**: 2025-04-22
- **Reviewer**: 전민진

## Motivation

- 기존 openVLA는 generalization에는 성공적(language following ability, semantic generalization)이었지만, 명백한 한계가 존재

- 최근에 생성 속도를 향상시키는 연구가 여러가지 소개되었으나, bi-manual에 취약함 ⇒ 속도도 빠르면서 만족할만한 성능을 보여주는 방법은 없음

- 본 논문에서는 OpenVLA를 베이스로 사용하여 최적의 파인튜닝 레시피 Optimized Fine-Tuning(OFT) recipe를 탐구

- 여러 디자인 초이스를 바탕으로 OpenVLA-OFT를 제안, LIBERO simulation benchmark에서 OpenVLA의 성능을 효과적으로 높이면서도 26x generation throughput를 달성

## Introduction

- 최근 VLA 모델은 low-level robotic control을 위해 대량의 robot dataset에 pretrained VLM을 학습해 구축, 다양한 로봇과 태스크에서 높은 성능과 semantic generalization, language following ability를 보임

- fine-tuning은 새로운 로봇과 태스크에 대해 VLA의 높은 성능을 위해 필수적이지만, 아직 adapation을 위해 어떤 디자인이 가장 효과적인지에 대한 탐구는 부족

- 이전 OpenVLA 논문에서 LoRA를 활용한 FT adaptation strategy를 소개하였으나, 몇가지 한계가 존재

- 최근에 더 좋은 action tokenization schemes를 통해서 efficiency를 높이는(속도를 2배에서 13배 정도 높임) 연구들이 제안되었으나, action chunk사이에 상당한 latency가 있어(최근 가장 빠른 방법 기준 750ms) 아직 high-frequency bimanual robot에 적용하기엔 한계가 존재

- 본 논문에선 이러한 인사이트들을 바탕으로 OFT recipe의 초안, OpenVLA-OFT를 제안

- LIBERO simulation benchmark와 real bimanul ALOHA robot으로 실험

## Related Work

- 이전엔 language와 vision foundation모델을 사용해서 robotic capabilities를 높이는 연구들이 진행

- VLA 모델 개발시 FT의 역할이 중요함에도 불구하고, 효과적인 레시피 탐구는 부족했음

- 최근의 연구에서는 VLA 효율성을 위해 새로운 action tokenization 방법이 고안됨

- 다른 연구 라인에서는 high-frequency, bimanual manipulation을 위한 효과적인 VLA FT를 위해서 diffusion 이나 flow matching을 사용

## Preliminaries

### Original OpenVLA formulation

- 7B manipulation policy, Prismatic VLM을 OXE의 1M episode에 FT해서 만든 모델

- autoregressive prediction을 활용, 각 timestep마다 7 discrete robot action token을 생성

### Action chunking

- 이전 연구는 action chunking(중간 replanning없이 future action sequence를 예측, 실행)이 여러 manipulation task에서 policy 성공률을 높인다는 것을 보임

- 그러나, OpenVLA의 autoregressive generation scheme에서는 action chunking이 어려움

- chunk size를 K, action dimensionality를 D라고 하면,  OpenVLA는 KD번 forward를 해야함

## Proposed Method

### Studying key VLA Fine-Tuning Design Decisions

- 기존 OpenVLA의 한계를 다루기 위해서 다음 3가지 디자인에 대해 조사

{% include figure.liquid loading="eager" path="assets/img/posts/2025-04-22-fine-tuning-vision-language-action-models-optimizing-speed/image_000.png" class="img-fluid rounded z-depth-1" %}

### Implementing Alternative Design Components

- Parallel decoding with action chunking

- Continuous action space

- Additional model inputs and outputs

{% include figure.liquid loading="eager" path="assets/img/posts/2025-04-22-fine-tuning-vision-language-action-models-optimizing-speed/image_001.png" class="img-fluid rounded z-depth-1" %}

### Augmenting OpenVLA-OFT with FiLM for Enchanced Language Grounding

- bimanual에서는 input image가 3개(3rd person view, wrist-mounted cameras)

- 그래서 bi-manual에서는 language following ability향상을 위해서 ViT에 FiLM을 추가

## Experiment

### Research Question

RQ1. How does each design decision affect the fine-tuned policy’s success rate on downstream tasks?

RQ2. How does each design decisions affect model inference efficiency (action generation throughput and latency)?

RQ3. How do alternative fine-tuning formulations affect flexibility in model input-output specifications?

### LIBERO

- Experiment setup

- Task performance comparisons

- Inference Efficiency comparisons

- Model input-output flexibility

- Optimized Fine-tuning recipe

- Additional experiments

### Real-World ALOHA Robot

: 이전까지는 simulation에서의 성능을 봤다면, 이번 파트는 실제 로봇에 적용해봤을 때의 성능

: OpenVLA의 경우 pretraining때 bimanual data를 본 적이 없음

: 여기서는 OpenVLA-OFT에 FiLM을 추가한 OpenVLA-OFT+로 성능 평가

- Setup

- Method in Comparison

- ALOHA Task Performance Results

- ALOHA Inference Efficiency Comparison

## Limitations

- Handling multimodal demonstrations

- Pretraining versus fine-tuning

- Inconsistent language grounding
