---
categories:
  - paper-reviews
date: "2025-01-14 00:00:00"
description: 논문 리뷰
giscus_comments: true
layout: post
related_posts: false
tags:
  - fine-tuning
  - language-model
  - paper-review
  - vision
thumbnail: assets/img/posts/2025-01-14-openvla-an-open-source-vision-language-action-model/thumbnail.jpg
title: "OpenVLA: An Open-Source Vision-Language-Action Model"
---

**논문 정보**

- **Date**: 2025-01-14
- **Reviewer**: 전민진

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-14-openvla-an-open-source-vision-language-action-model/image_000.png" class="img-fluid rounded z-depth-1" %}

## Summary

- 기존의 VLA모델들은 1) closed, 2) 새로운 task에 효율적으로 FT하기 어렵다는 단점이 존재

- 현재 공개된 public model중 최고의 성능을 내는 vision-language-action model

- 기존의 closed model인 RT-2-X(55B)보다 훨씬 작은 크기(7B)로 훨씬 높은 성능 달성

- 어떻게 모델을 구상하면 좋은지에 대한 insight가 많이 나와 있음

- 모든 코드가 공개 되어 있어 이를 기반으로 연구를 시작하면 좋음

## Introduction

- robotic dataset은 대량으로 구축하기가 어려움

- 기존 연구

- 970K의 방대한 데이터셋에 대해 pretrained된 fully open source VLA model, OpenVLA를 제안

## Related works

- Visually-Conditioned Language Models

- Generalist Robot Policies

- Vision-Language-Action Models

## Proposed Method

- VLA 모델 개발을 위한 자세한 practice는 아직 연구가 덜 됨

- Preliminaries: Vision-Lnaguage Models

- OpenVLA training procedure

- Training data

- OpenVLA Design decision

- Intrastructure for trainign and inference

## Experiments

- Research question

- Direct Evaluation on Multiple Robot Platforms

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-14-openvla-an-open-source-vision-language-action-model/image_001.png" class="img-fluid rounded z-depth-1" %}

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-14-openvla-an-open-source-vision-language-action-model/image_002.png" class="img-fluid rounded z-depth-1" %}

- Data-Efficient Adaptation to New Robot Setups

- Parameter-Efficient Fine-tuning

- Memory-Efficient Inference via quantization

## Discussion and Limitation

- single-image observations만 지원

- throughtput을 향상시키는게 중요

- 성능 향상의 여지는 있음 - 아직 90%도 달성하지 못함
