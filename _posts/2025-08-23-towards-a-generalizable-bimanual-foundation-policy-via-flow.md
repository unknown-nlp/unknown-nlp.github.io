---
categories:
  - paper-reviews
date: "2025-08-23 00:00:00"
description: 논문 리뷰 - Robotics 관련 연구
giscus_comments: true
layout: post
related_posts: false
slug: 2025-08-23-towards-a-generalizable-bimanual-foundation-policy-via-flow
tags:
  - alignment
  - attention
  - diffusion
  - paper-review
  - robotics
title: Towards a Generalizable Bimanual Foundation Policy via Flow-based Video Prediction
---

**논문 정보**

- **Date**: 2025-06-10
- **Reviewer**: 전민진
- **Property**: Robotics

## Abstract

- Generalizable bimaual policy를 만드는 것은 여러 challenge가 존재

- 최근에 pretrained VLA를 기반으로 general bimanual policy를 만드는 연구들이 제안되어 왔으나 효과적이진 않음

- text-to-video model과 light diffusion policy로 구성된 프레임워크를 구축, 각각의 모델을 FT해서 사용하는 방법론을 제안

## Introduction

- bimanual manipulation은 embodied agent가 양손이 모두 필요한 복잡한 task를 수행하기 위해서 중요한 분야

- single-arm manupulation과 달리, bimanual task의 경우 human-like coordination이 필요

- 이전 bimanual policy는 다음과 같은 방법으로 학습

- 하지만 이전 방법론은 다음과 같은 한계가 존재

- VLA을 기반으로 한 방법론은 일반화가 가능하지만..

- 본 논문의 저자들은 heterogenous action을 직접적으로 다루지 않고, foundation model을 써서 bimanual policy를 구축해보고자 함

- 본 논문에서는 CogRobot를 소개, 기존 SOTA T2V model CogVideoX를 활용해서 bimanual policy를 구축

- 본 논문의 contribution은 다음과 같음

## Preliminaries

- 본 논문에서는 7 DoF realman robotic arm과 external camera를 사용해 dual-arm system을 구축

- bimanual manipulation task T를 goal-conditined Partially Observable Markoc Decision Process(POMDP)로 formulate

- VR device를 통해서 expert data를 수집 (Open-Television을 활용)

- 수집된 데이터셋은 episodic data를 포함

## Proposed Methods

- CogRobot에서, instruction-conditioned bimanual policy의 학습을 두 가지 스텝으로 분해

- 최근 T2V model은 고품질의 realistic video를 생성하는 능력이 아주 굿 ⇒ 하지만 바로 bimanual에 FT하기엔 한계가 존재

- 양팔 학습 데이터로는 RDT, ROBOMIND사용

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/a6e39d64-1e83-4ed8-935d-7dcf345050d4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUISFKIY%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2Q4Kl1a73Clwa%2FOUxyyJ8%2FH6OqW0hMYB0eg5w0TQHgQIhAIfImakH4f4YgAii3TXAJSGCCyTzp6DFoIDfegKiUaj%2FKogECNP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxl8rBn4j7wb%2BUoTPQq3ANEluJ6qZ%2B6wz15ZxWD8qSsH%2B4FWOv78iNDvjp5UliKsONCPmOzwsQ45JpXmJonL%2BTXEecjy2zjW%2BkxgUEo1FM8nqI45IQf4u%2FCKwfnr0xc7cFSV6HOAFfLePAMQoGyqXTEWkCyhk7CLbvp%2B5hkhBxZu77%2BsMx8kUtmlhdrUFEw5ozcgZItSPToSklgLcf104vJow0eAMv9iKTm0ZiCCjT5fqKrYTsqOLPP5mf54j61B4TBtXUEM%2Fpyaq7V5vyuXsVy%2BfYIAOdwp241cLRNhNKmZQgJal4jcRP5gw%2FZ5tmFnImRBwXFfbFddJIQ%2FPpLtca%2BSD6jOQ9jUBhq0XdLJH4efQbG7YxWtBrWcBqx097VdVt53ERu52Jwq6HZh0lblTjSbsy4RxQ42DAyjlx46iS3ggpea6WLSQTfXj%2BdZZC2kxv8hK8RC5P3GGgRzh2mhG%2FH9qKhGy2kbkVIYOYDhld%2FVAb3E1ZfrobpmXKIV%2F3epkDoKsaaeDQpwEgQXtjO59wKkUjI%2F1wHnmdozSbQvI1HlT2OL8zNFn259L3adDVxSoeNsjsUTFAOBvJv7dZubfYOCreDgr2qIDs0OeKnOORzoP9oOQjQbwELu7uEM2bAbS7i1LkTAP7%2BIqew0DCo0%2BHEBjqkAb02oNrAZFLBAsyCVwToyv%2B0WpBpwpc6dmjOgBTfJ27Of3ujF1wYmVATQB1R14rNT3wSFCbO2Qgi5vh9KgNmWDgnlNaYenPeoLQwvACJ%2F%2F31yFi%2FlDQ2lVgCjeH9HnTR4YKCzPP6RlBcj4U%2FKBrOwRv9twF%2Bc49kPqnCRJ6ldDamvb1hgEbMvDVVs0oMdYfDZXQlsTt0T5UT0wLHiChNv5%2FMdohq&X-Amz-Signature=b31955e87ee43eb2f459ad94715c0eabd45f1663873a7ae5b82caf016c6ea8a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Text-to-Flow Generation

- vanilla CogVideoX로 로봇팔 초기 이미지 넣고 생성해달라고 하면 사람 손을 생성함

- 본 논문에서 CogVideoX 2B, 5B를 단순하게 SFT하는 버전 혹은 2 stage(T2f, f2V)로 나눠서 학습하는 버전 두 가지 모두 실험

- vanilla 모델을 그대로 쓰거나 단순 SFT만 할 경우엔 다음과 같은 문제 발생

- 이러한 문제를 해결하기 위해서 optical flow를 활용하는 방법론을 제안

### Flow-to-Video Generation

- text-to-flow model을 기반으로, flow-to-video model을 구축

- 해당 방식의 우수성을 보이기 위해서, instruction의 특정 단어를 선택, 해당 단어에 대한 cross-attention map을 추출해서 영상과 잘 mapping이 되는지를 봄

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/f9104c29-57ab-40fd-b5f1-9ac6469df9a3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUISFKIY%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2Q4Kl1a73Clwa%2FOUxyyJ8%2FH6OqW0hMYB0eg5w0TQHgQIhAIfImakH4f4YgAii3TXAJSGCCyTzp6DFoIDfegKiUaj%2FKogECNP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxl8rBn4j7wb%2BUoTPQq3ANEluJ6qZ%2B6wz15ZxWD8qSsH%2B4FWOv78iNDvjp5UliKsONCPmOzwsQ45JpXmJonL%2BTXEecjy2zjW%2BkxgUEo1FM8nqI45IQf4u%2FCKwfnr0xc7cFSV6HOAFfLePAMQoGyqXTEWkCyhk7CLbvp%2B5hkhBxZu77%2BsMx8kUtmlhdrUFEw5ozcgZItSPToSklgLcf104vJow0eAMv9iKTm0ZiCCjT5fqKrYTsqOLPP5mf54j61B4TBtXUEM%2Fpyaq7V5vyuXsVy%2BfYIAOdwp241cLRNhNKmZQgJal4jcRP5gw%2FZ5tmFnImRBwXFfbFddJIQ%2FPpLtca%2BSD6jOQ9jUBhq0XdLJH4efQbG7YxWtBrWcBqx097VdVt53ERu52Jwq6HZh0lblTjSbsy4RxQ42DAyjlx46iS3ggpea6WLSQTfXj%2BdZZC2kxv8hK8RC5P3GGgRzh2mhG%2FH9qKhGy2kbkVIYOYDhld%2FVAb3E1ZfrobpmXKIV%2F3epkDoKsaaeDQpwEgQXtjO59wKkUjI%2F1wHnmdozSbQvI1HlT2OL8zNFn259L3adDVxSoeNsjsUTFAOBvJv7dZubfYOCreDgr2qIDs0OeKnOORzoP9oOQjQbwELu7uEM2bAbS7i1LkTAP7%2BIqew0DCo0%2BHEBjqkAb02oNrAZFLBAsyCVwToyv%2B0WpBpwpc6dmjOgBTfJ27Of3ujF1wYmVATQB1R14rNT3wSFCbO2Qgi5vh9KgNmWDgnlNaYenPeoLQwvACJ%2F%2F31yFi%2FlDQ2lVgCjeH9HnTR4YKCzPP6RlBcj4U%2FKBrOwRv9twF%2Bc49kPqnCRJ6ldDamvb1hgEbMvDVVs0oMdYfDZXQlsTt0T5UT0wLHiChNv5%2FMdohq&X-Amz-Signature=423b64d2f276705607ea31eedf14356d185d2e9a261eba0f79c5264b1c9ef9d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 해당 그림을 보면, language-only model의 경우(그냥 SFT) meaningful region을 식별하는데 실패하는 것을 볼 수 있음

- flow video를 중간에 생성, 이를 기반으로 detailed vidoe를 생성함으로써, intruction과 visual input사이의 더 나은 alignment를 달성

- 첫번째 단계에서 생성한 flow video를 잘 활용하여 detailed video를 생성할 수 있도록, flow video와 RGB vidoe를 channel dimension에 따라서 concat하는 방법론을 제안

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/93f3655f-127a-4030-a8a9-85711bbe49c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUISFKIY%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2Q4Kl1a73Clwa%2FOUxyyJ8%2FH6OqW0hMYB0eg5w0TQHgQIhAIfImakH4f4YgAii3TXAJSGCCyTzp6DFoIDfegKiUaj%2FKogECNP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxl8rBn4j7wb%2BUoTPQq3ANEluJ6qZ%2B6wz15ZxWD8qSsH%2B4FWOv78iNDvjp5UliKsONCPmOzwsQ45JpXmJonL%2BTXEecjy2zjW%2BkxgUEo1FM8nqI45IQf4u%2FCKwfnr0xc7cFSV6HOAFfLePAMQoGyqXTEWkCyhk7CLbvp%2B5hkhBxZu77%2BsMx8kUtmlhdrUFEw5ozcgZItSPToSklgLcf104vJow0eAMv9iKTm0ZiCCjT5fqKrYTsqOLPP5mf54j61B4TBtXUEM%2Fpyaq7V5vyuXsVy%2BfYIAOdwp241cLRNhNKmZQgJal4jcRP5gw%2FZ5tmFnImRBwXFfbFddJIQ%2FPpLtca%2BSD6jOQ9jUBhq0XdLJH4efQbG7YxWtBrWcBqx097VdVt53ERu52Jwq6HZh0lblTjSbsy4RxQ42DAyjlx46iS3ggpea6WLSQTfXj%2BdZZC2kxv8hK8RC5P3GGgRzh2mhG%2FH9qKhGy2kbkVIYOYDhld%2FVAb3E1ZfrobpmXKIV%2F3epkDoKsaaeDQpwEgQXtjO59wKkUjI%2F1wHnmdozSbQvI1HlT2OL8zNFn259L3adDVxSoeNsjsUTFAOBvJv7dZubfYOCreDgr2qIDs0OeKnOORzoP9oOQjQbwELu7uEM2bAbS7i1LkTAP7%2BIqew0DCo0%2BHEBjqkAb02oNrAZFLBAsyCVwToyv%2B0WpBpwpc6dmjOgBTfJ27Of3ujF1wYmVATQB1R14rNT3wSFCbO2Qgi5vh9KgNmWDgnlNaYenPeoLQwvACJ%2F%2F31yFi%2FlDQ2lVgCjeH9HnTR4YKCzPP6RlBcj4U%2FKBrOwRv9twF%2Bc49kPqnCRJ6ldDamvb1hgEbMvDVVs0oMdYfDZXQlsTt0T5UT0wLHiChNv5%2FMdohq&X-Amz-Signature=f05dda68265a1c07b817ec74e27eaf844c9e0d0957565e7c004bdbdb917a3868&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Diffusion policy from Videos

- predicted video의 각 프레임을 target observation으로 사용해서 excutable low-level action을 생성

- 학습 동안, goal step을 랜덤하게 추출, 노이즈를 활용해서 progressively perturb

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/357c99ef-ce49-44e2-9ddd-a3e0fae79812/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUISFKIY%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2Q4Kl1a73Clwa%2FOUxyyJ8%2FH6OqW0hMYB0eg5w0TQHgQIhAIfImakH4f4YgAii3TXAJSGCCyTzp6DFoIDfegKiUaj%2FKogECNP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxl8rBn4j7wb%2BUoTPQq3ANEluJ6qZ%2B6wz15ZxWD8qSsH%2B4FWOv78iNDvjp5UliKsONCPmOzwsQ45JpXmJonL%2BTXEecjy2zjW%2BkxgUEo1FM8nqI45IQf4u%2FCKwfnr0xc7cFSV6HOAFfLePAMQoGyqXTEWkCyhk7CLbvp%2B5hkhBxZu77%2BsMx8kUtmlhdrUFEw5ozcgZItSPToSklgLcf104vJow0eAMv9iKTm0ZiCCjT5fqKrYTsqOLPP5mf54j61B4TBtXUEM%2Fpyaq7V5vyuXsVy%2BfYIAOdwp241cLRNhNKmZQgJal4jcRP5gw%2FZ5tmFnImRBwXFfbFddJIQ%2FPpLtca%2BSD6jOQ9jUBhq0XdLJH4efQbG7YxWtBrWcBqx097VdVt53ERu52Jwq6HZh0lblTjSbsy4RxQ42DAyjlx46iS3ggpea6WLSQTfXj%2BdZZC2kxv8hK8RC5P3GGgRzh2mhG%2FH9qKhGy2kbkVIYOYDhld%2FVAb3E1ZfrobpmXKIV%2F3epkDoKsaaeDQpwEgQXtjO59wKkUjI%2F1wHnmdozSbQvI1HlT2OL8zNFn259L3adDVxSoeNsjsUTFAOBvJv7dZubfYOCreDgr2qIDs0OeKnOORzoP9oOQjQbwELu7uEM2bAbS7i1LkTAP7%2BIqew0DCo0%2BHEBjqkAb02oNrAZFLBAsyCVwToyv%2B0WpBpwpc6dmjOgBTfJ27Of3ujF1wYmVATQB1R14rNT3wSFCbO2Qgi5vh9KgNmWDgnlNaYenPeoLQwvACJ%2F%2F31yFi%2FlDQ2lVgCjeH9HnTR4YKCzPP6RlBcj4U%2FKBrOwRv9twF%2Bc49kPqnCRJ6ldDamvb1hgEbMvDVVs0oMdYfDZXQlsTt0T5UT0wLHiChNv5%2FMdohq&X-Amz-Signature=1817c6cdf3281852258c5f246b2ac0cde545d997a722c9a90bc997ecab9c5798&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Related works

- Bimnaual의 challenge

- 이전에 나온 연구

- 이전 video generation 활용 연구

## Experiments

### Experiment setup

- Simulation setup

- Real-world setup and data collection

- Architecthre Detail

- Baseline

### Main result in simulation setup

- 각 태스크 별로 10개의 random seed를 활용해서 평가, 각 시드마다 10번 돌리고 평균냄

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/b2194d29-4e84-48a8-b639-f909d521b63f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUISFKIY%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2Q4Kl1a73Clwa%2FOUxyyJ8%2FH6OqW0hMYB0eg5w0TQHgQIhAIfImakH4f4YgAii3TXAJSGCCyTzp6DFoIDfegKiUaj%2FKogECNP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igxl8rBn4j7wb%2BUoTPQq3ANEluJ6qZ%2B6wz15ZxWD8qSsH%2B4FWOv78iNDvjp5UliKsONCPmOzwsQ45JpXmJonL%2BTXEecjy2zjW%2BkxgUEo1FM8nqI45IQf4u%2FCKwfnr0xc7cFSV6HOAFfLePAMQoGyqXTEWkCyhk7CLbvp%2B5hkhBxZu77%2BsMx8kUtmlhdrUFEw5ozcgZItSPToSklgLcf104vJow0eAMv9iKTm0ZiCCjT5fqKrYTsqOLPP5mf54j61B4TBtXUEM%2Fpyaq7V5vyuXsVy%2BfYIAOdwp241cLRNhNKmZQgJal4jcRP5gw%2FZ5tmFnImRBwXFfbFddJIQ%2FPpLtca%2BSD6jOQ9jUBhq0XdLJH4efQbG7YxWtBrWcBqx097VdVt53ERu52Jwq6HZh0lblTjSbsy4RxQ42DAyjlx46iS3ggpea6WLSQTfXj%2BdZZC2kxv8hK8RC5P3GGgRzh2mhG%2FH9qKhGy2kbkVIYOYDhld%2FVAb3E1ZfrobpmXKIV%2F3epkDoKsaaeDQpwEgQXtjO59wKkUjI%2F1wHnmdozSbQvI1HlT2OL8zNFn259L3adDVxSoeNsjsUTFAOBvJv7dZubfYOCreDgr2qIDs0OeKnOORzoP9oOQjQbwELu7uEM2bAbS7i1LkTAP7%2BIqew0DCo0%2BHEBjqkAb02oNrAZFLBAsyCVwToyv%2B0WpBpwpc6dmjOgBTfJ27Of3ujF1wYmVATQB1R14rNT3wSFCbO2Qgi5vh9KgNmWDgnlNaYenPeoLQwvACJ%2F%2F31yFi%2FlDQ2lVgCjeH9HnTR4YKCzPP6RlBcj4U%2FKBrOwRv9twF%2Bc49kPqnCRJ6ldDamvb1hgEbMvDVVs0oMdYfDZXQlsTt0T5UT0wLHiChNv5%2FMdohq&X-Amz-Signature=d0c84f1a7ef855cafbb4e7596ad7280d7b225d7655e530ff95e861919407cb80&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- single camera를 사용하기 때문에 vanilla DP는 다른 추가적인 visual input(3d representation이나 multi-view images)을 사용하는 baseline보다 낮게 나옴

- 하지만 future state를 예상하는 능력이 추가된 CogRobot의 경우 제한적인 image input으로도 높은 성능을 보임

### Real-World experiments

- 2가지 task로 평가

- 실험 결과, 확실히 어려운 task(pull box)에서 CogRobot의 성능이 높게 나옴

### Visualization and Ablation

- Visualization

- Ablation

## Conclusion

- bimanual policy를 구축할 때 T2V 모델을 활용

- 적은 데이터에서 효과적으로 T2V를 FT하기 위해 flow-guided framework를 제안

- 방법론은 신박한데 평가가 아쉽다
