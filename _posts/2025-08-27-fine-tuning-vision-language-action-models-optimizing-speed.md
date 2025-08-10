---
categories:
  - paper-reviews
date: "2025-08-27 00:00:00"
description: 논문 리뷰
giscus_comments: true
layout: post
related_posts: false
slug: 2025-08-27-fine-tuning-vision-language-action-models-optimizing-speed
tags:
  - diffusion
  - fine-tuning
  - multimodal
  - paper-review
title: "Fine-tuning Vision-Language-Action Models: Optimizing Speed and Success"
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

- chunk size를 K, action dimensionality를 D라고 하면, OpenVLA는 KD번 forward를 해야함

## Proposed Method

### Studying key VLA Fine-Tuning Design Decisions

- 기존 OpenVLA의 한계를 다루기 위해서 다음 3가지 디자인에 대해 조사

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/61896b44-f1c8-4189-938b-67fb84d272d0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663B3WBHHR%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCLz9Op%2FwYyZLP7w%2B8kpx6rOwPrw2VNFBmt%2FQTkOXKzHAIhAPDOGOxK6hgI%2BpTf%2FX6V4FSp140hzqtr%2BtOAVOTW13dtKogECNP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxFA9vfEYHYmPXx4T8q3AOci68FAaiFz8F1z5re%2FH9J7Gh321BE43OqgcdaUR2wvxkZa%2B6Q%2FiKRjY%2BPHD4hLltpaqXpvZB6uaNrW7ZROmGB47fBdaWYHQpH0M1d8nDGsIycjQGFJDNmbOfrB64G1pLDXnNdqavM5BkM53dPwrm2ZFNzfb2meRpg%2Bg4g4fagT7XkpEwrzDmtwrczZbBoT%2FTG6Tow5cvjKKP9cq%2FV9olpxXD%2B1tLXurweze9JG2%2FagRSkzOO3Ih6YQfY9mgBOGXRwYsYhfO%2Fs9wcCXU0M4Y8h1blvwB7RgtEjubW9ouHZDyrXgWdWmy4BnRmvrCs5GVYKBUw5vk%2Fw0UYp%2FuI%2FoyTWC5duvsO0q92PAdUMLMaeX%2FeDbTUUEKGE5pnIqWEcyKFQVB%2BGD8PmKz2EinIVJh4FhnilhmJcl095wiFFcJS6Qq9kEppTCo50Nsz3HymIgKWVx5VZCdZBLD51cbq27DOeuAkbSwlsxVVzlWoI5MjxHhf92veZby5g5TrxE624gcq92lx1Bat%2FvuR5oIF5f177dnuozAluxpdQMlsO2gU1OR6Jwjbn8w3ToheRxPKQhu9WO5X5zSbt%2BPXWlRiqLKi%2BtQYkNilvdlxQz9xotThF5lGxuf%2FgEi0l3IAC2zC91OHEBjqkAUvhlJmv0EL9z7tu3bwDupbMBpTSkD6AsR2pATPIe%2BWvkrmMT7M%2BEobo7iEfatK60k4I6IpJgNXU4%2B1WfqzjfukkvhHW3YOhSdXPSQLQQdfU1Jfq5GVZFpUZbds8JOs58wufy6SSWMKUwv5LW0%2BCr43qo0F5GKrEGu0QbVhUQEp4ML6PjjKb25gY5GD9utwDy1E%2FLdjiNtQoEQdnM6J%2BeTj4eCi0&X-Amz-Signature=abc535418f5b6c54f1f528bb905f79d5555d51750bcac4f0977d7ef6755abb51&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Implementing Alternative Design Components

- Parallel decoding with action chunking

- Continuous action space

- Additional model inputs and outputs

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/ab955d06-2287-4f1d-bda1-5f7c3c230606/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663B3WBHHR%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCLz9Op%2FwYyZLP7w%2B8kpx6rOwPrw2VNFBmt%2FQTkOXKzHAIhAPDOGOxK6hgI%2BpTf%2FX6V4FSp140hzqtr%2BtOAVOTW13dtKogECNP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxFA9vfEYHYmPXx4T8q3AOci68FAaiFz8F1z5re%2FH9J7Gh321BE43OqgcdaUR2wvxkZa%2B6Q%2FiKRjY%2BPHD4hLltpaqXpvZB6uaNrW7ZROmGB47fBdaWYHQpH0M1d8nDGsIycjQGFJDNmbOfrB64G1pLDXnNdqavM5BkM53dPwrm2ZFNzfb2meRpg%2Bg4g4fagT7XkpEwrzDmtwrczZbBoT%2FTG6Tow5cvjKKP9cq%2FV9olpxXD%2B1tLXurweze9JG2%2FagRSkzOO3Ih6YQfY9mgBOGXRwYsYhfO%2Fs9wcCXU0M4Y8h1blvwB7RgtEjubW9ouHZDyrXgWdWmy4BnRmvrCs5GVYKBUw5vk%2Fw0UYp%2FuI%2FoyTWC5duvsO0q92PAdUMLMaeX%2FeDbTUUEKGE5pnIqWEcyKFQVB%2BGD8PmKz2EinIVJh4FhnilhmJcl095wiFFcJS6Qq9kEppTCo50Nsz3HymIgKWVx5VZCdZBLD51cbq27DOeuAkbSwlsxVVzlWoI5MjxHhf92veZby5g5TrxE624gcq92lx1Bat%2FvuR5oIF5f177dnuozAluxpdQMlsO2gU1OR6Jwjbn8w3ToheRxPKQhu9WO5X5zSbt%2BPXWlRiqLKi%2BtQYkNilvdlxQz9xotThF5lGxuf%2FgEi0l3IAC2zC91OHEBjqkAUvhlJmv0EL9z7tu3bwDupbMBpTSkD6AsR2pATPIe%2BWvkrmMT7M%2BEobo7iEfatK60k4I6IpJgNXU4%2B1WfqzjfukkvhHW3YOhSdXPSQLQQdfU1Jfq5GVZFpUZbds8JOs58wufy6SSWMKUwv5LW0%2BCr43qo0F5GKrEGu0QbVhUQEp4ML6PjjKb25gY5GD9utwDy1E%2FLdjiNtQoEQdnM6J%2BeTj4eCi0&X-Amz-Signature=76a6c3f7770d59d343acee9e12357f978402552c9e6f8d19f5e9fc6e1e4201c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
