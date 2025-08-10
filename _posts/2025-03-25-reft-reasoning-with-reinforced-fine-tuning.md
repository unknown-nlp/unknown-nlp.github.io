---
categories:
- paper-reviews
date: '2025-03-25 00:00:00'
description: 논문 리뷰 - Reinforcement Learning, SFT 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- fine-tuning
- language-model
- llm
- paper-review
- reasoning
- reinforcement learning
- reinforcement-learning
- rlhf
- sft
thumbnail: assets/img/posts/2025-03-25-reft-reasoning-with-reinforced-fine-tuning/thumbnail.jpg
title: 'ReFT: Reasoning with Reinforced Fine-Tuning'
---

**논문 정보**
- **Date**: 2025-03-25
- **Reviewer**: 김재희
- **Property**: Reinforcement Learning, SFT

## 1. Intro

## preliminaries

### PPO

- Original RLHF Objectives

- PPO Objectives

### RLHF

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/060e8dee-a18a-4202-8058-ddb1e975a4f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664AO4UGH%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113454Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAa6Hmk5lW6u1nuFRVT6jEYJciEdDBMVQe6bkv1ZnRt8AiATH95Y03jEoKe40d6pG8Ef%2FmG1DvX%2FsSHthYXTtJFtfiqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM83j72pTknKAq019LKtwDBVVixkTb2wicXpFqEVly8wifNd3kZeL%2F%2BuwojZi0DC8RcCbtvaqdVMbGiaRbUo3wzNf1f7uhfWwvnqSpSvduKGNf0VLRbSRmjsDzXSdZsPkF2SOM%2FW8QFSmyaWTfGEgfuNc5lGYsabV8pHroE2mbVCWtRu5TITHKi6ljgXNHb2%2BjA%2FQcASRZvBFpS12gIbACUbXkCNhM4%2B3a8yfgTp29J6x4g%2BVfW2T%2Fv%2Bp%2FkHrTNL85Z7Ss7XzGHLN5XQSDW3ewE%2Bix9ZrnTlH8CzKOnxLk9lJDd%2FTzBaj15DgkZ%2FyRbRpWS804ekok877qcE77cl%2Fh9sRgTDS6J1dQSJeJ0STl4lX4g1ikGtBq1FaFkRrR5RKwtZMy11jZ%2Bpt2SHFOzUeeWwcl3opShx%2FTGG9Eg9zyw4XhajdxxGbSbJVNGCUksWmWfE5u32U%2FR%2BVaPVC5EouMJ5uS%2Fac1VYaV2vK8qtDXUGeUDhU%2BFJ26iVuLvuJBR30nyBlJNm0SzWgUT0syJWm4xyHgrtk%2FHT%2FkNaHyzA5wXIqdssMTwdBrDaSs8Mf01oBUJAxYTmpf0ikqmmoGECRQ5krTGuf1ckHzOmAXRrMrfIshSdcG%2FXcZLTmkLF%2BdPk5HfB8lDahqlRuQqZgwhf%2FhxAY6pgGIj1nPDbdoqSlG8phjDQkk2xbZkVlSHxGDyj58h%2FEuPlSqUIZ6WeJ%2FhfAtyP0GlR%2FCSiWM0eTxJJbYrkIeo4U4X3hG9pM4PqmYf4fcOd58wQ5ElXwP8yKGBo%2BJ1n4Mo%2F0%2FHBhdktPQYNIZxIISYyC6HxKz4SEiTMkyjFMPMUhSOm3O4GnsCKpQ4zxIWm1tP9msiFTQBbCrL7LiUAHBU3BA70ruhYpI&X-Amz-Signature=f0fcb4eb790f0af337e785e753690f395ec21c270f76d98941d2d30ba10140a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**Training language models to follow instructions with human feedback**

- 방법론 목표: instruction을 따르는 “안전”하고 “사실적”이며 “믿을만”한 출력을 내도록 학습

### What makes reinforcement learning effective in LLM paradigm?

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/956aacac-5991-430e-9089-aba1c0760f9e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664AO4UGH%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113454Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAa6Hmk5lW6u1nuFRVT6jEYJciEdDBMVQe6bkv1ZnRt8AiATH95Y03jEoKe40d6pG8Ef%2FmG1DvX%2FsSHthYXTtJFtfiqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM83j72pTknKAq019LKtwDBVVixkTb2wicXpFqEVly8wifNd3kZeL%2F%2BuwojZi0DC8RcCbtvaqdVMbGiaRbUo3wzNf1f7uhfWwvnqSpSvduKGNf0VLRbSRmjsDzXSdZsPkF2SOM%2FW8QFSmyaWTfGEgfuNc5lGYsabV8pHroE2mbVCWtRu5TITHKi6ljgXNHb2%2BjA%2FQcASRZvBFpS12gIbACUbXkCNhM4%2B3a8yfgTp29J6x4g%2BVfW2T%2Fv%2Bp%2FkHrTNL85Z7Ss7XzGHLN5XQSDW3ewE%2Bix9ZrnTlH8CzKOnxLk9lJDd%2FTzBaj15DgkZ%2FyRbRpWS804ekok877qcE77cl%2Fh9sRgTDS6J1dQSJeJ0STl4lX4g1ikGtBq1FaFkRrR5RKwtZMy11jZ%2Bpt2SHFOzUeeWwcl3opShx%2FTGG9Eg9zyw4XhajdxxGbSbJVNGCUksWmWfE5u32U%2FR%2BVaPVC5EouMJ5uS%2Fac1VYaV2vK8qtDXUGeUDhU%2BFJ26iVuLvuJBR30nyBlJNm0SzWgUT0syJWm4xyHgrtk%2FHT%2FkNaHyzA5wXIqdssMTwdBrDaSs8Mf01oBUJAxYTmpf0ikqmmoGECRQ5krTGuf1ckHzOmAXRrMrfIshSdcG%2FXcZLTmkLF%2BdPk5HfB8lDahqlRuQqZgwhf%2FhxAY6pgGIj1nPDbdoqSlG8phjDQkk2xbZkVlSHxGDyj58h%2FEuPlSqUIZ6WeJ%2FhfAtyP0GlR%2FCSiWM0eTxJJbYrkIeo4U4X3hG9pM4PqmYf4fcOd58wQ5ElXwP8yKGBo%2BJ1n4Mo%2F0%2FHBhdktPQYNIZxIISYyC6HxKz4SEiTMkyjFMPMUhSOm3O4GnsCKpQ4zxIWm1tP9msiFTQBbCrL7LiUAHBU3BA70ruhYpI&X-Amz-Signature=21366e460a0d581c14ea75ffc75390b554a1a1ba87cb1f4e811d2c6b1e7416ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- diversity of trajactory: 질문과 정답은 하나지만, 과정은 다양하니까.

## 2. Method

### Main Research Question

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/502e6748-e807-4f75-b4e6-b0108a3dc2e9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664AO4UGH%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113454Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAa6Hmk5lW6u1nuFRVT6jEYJciEdDBMVQe6bkv1ZnRt8AiATH95Y03jEoKe40d6pG8Ef%2FmG1DvX%2FsSHthYXTtJFtfiqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM83j72pTknKAq019LKtwDBVVixkTb2wicXpFqEVly8wifNd3kZeL%2F%2BuwojZi0DC8RcCbtvaqdVMbGiaRbUo3wzNf1f7uhfWwvnqSpSvduKGNf0VLRbSRmjsDzXSdZsPkF2SOM%2FW8QFSmyaWTfGEgfuNc5lGYsabV8pHroE2mbVCWtRu5TITHKi6ljgXNHb2%2BjA%2FQcASRZvBFpS12gIbACUbXkCNhM4%2B3a8yfgTp29J6x4g%2BVfW2T%2Fv%2Bp%2FkHrTNL85Z7Ss7XzGHLN5XQSDW3ewE%2Bix9ZrnTlH8CzKOnxLk9lJDd%2FTzBaj15DgkZ%2FyRbRpWS804ekok877qcE77cl%2Fh9sRgTDS6J1dQSJeJ0STl4lX4g1ikGtBq1FaFkRrR5RKwtZMy11jZ%2Bpt2SHFOzUeeWwcl3opShx%2FTGG9Eg9zyw4XhajdxxGbSbJVNGCUksWmWfE5u32U%2FR%2BVaPVC5EouMJ5uS%2Fac1VYaV2vK8qtDXUGeUDhU%2BFJ26iVuLvuJBR30nyBlJNm0SzWgUT0syJWm4xyHgrtk%2FHT%2FkNaHyzA5wXIqdssMTwdBrDaSs8Mf01oBUJAxYTmpf0ikqmmoGECRQ5krTGuf1ckHzOmAXRrMrfIshSdcG%2FXcZLTmkLF%2BdPk5HfB8lDahqlRuQqZgwhf%2FhxAY6pgGIj1nPDbdoqSlG8phjDQkk2xbZkVlSHxGDyj58h%2FEuPlSqUIZ6WeJ%2FhfAtyP0GlR%2FCSiWM0eTxJJbYrkIeo4U4X3hG9pM4PqmYf4fcOd58wQ5ElXwP8yKGBo%2BJ1n4Mo%2F0%2FHBhdktPQYNIZxIISYyC6HxKz4SEiTMkyjFMPMUhSOm3O4GnsCKpQ4zxIWm1tP9msiFTQBbCrL7LiUAHBU3BA70ruhYpI&X-Amz-Signature=495959e4ee66792fe4b39e662f66793ceb2b47360ef19ef3d78623b89a8222c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 논문 요약

### Notations

- CoT ( \textbf{e}): CoT trajactory including final answer

- state: all tokens including question and generated so far

- policy model( \pi_\theta): 학습 대상 모델 

### Objectives

- SFT

- RL: RLHF 수식과 동일합니다. 

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/e15dab3c-ae61-406a-a721-60b641ef8b78/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664AO4UGH%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113454Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAa6Hmk5lW6u1nuFRVT6jEYJciEdDBMVQe6bkv1ZnRt8AiATH95Y03jEoKe40d6pG8Ef%2FmG1DvX%2FsSHthYXTtJFtfiqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM83j72pTknKAq019LKtwDBVVixkTb2wicXpFqEVly8wifNd3kZeL%2F%2BuwojZi0DC8RcCbtvaqdVMbGiaRbUo3wzNf1f7uhfWwvnqSpSvduKGNf0VLRbSRmjsDzXSdZsPkF2SOM%2FW8QFSmyaWTfGEgfuNc5lGYsabV8pHroE2mbVCWtRu5TITHKi6ljgXNHb2%2BjA%2FQcASRZvBFpS12gIbACUbXkCNhM4%2B3a8yfgTp29J6x4g%2BVfW2T%2Fv%2Bp%2FkHrTNL85Z7Ss7XzGHLN5XQSDW3ewE%2Bix9ZrnTlH8CzKOnxLk9lJDd%2FTzBaj15DgkZ%2FyRbRpWS804ekok877qcE77cl%2Fh9sRgTDS6J1dQSJeJ0STl4lX4g1ikGtBq1FaFkRrR5RKwtZMy11jZ%2Bpt2SHFOzUeeWwcl3opShx%2FTGG9Eg9zyw4XhajdxxGbSbJVNGCUksWmWfE5u32U%2FR%2BVaPVC5EouMJ5uS%2Fac1VYaV2vK8qtDXUGeUDhU%2BFJ26iVuLvuJBR30nyBlJNm0SzWgUT0syJWm4xyHgrtk%2FHT%2FkNaHyzA5wXIqdssMTwdBrDaSs8Mf01oBUJAxYTmpf0ikqmmoGECRQ5krTGuf1ckHzOmAXRrMrfIshSdcG%2FXcZLTmkLF%2BdPk5HfB8lDahqlRuQqZgwhf%2FhxAY6pgGIj1nPDbdoqSlG8phjDQkk2xbZkVlSHxGDyj58h%2FEuPlSqUIZ6WeJ%2FhfAtyP0GlR%2FCSiWM0eTxJJbYrkIeo4U4X3hG9pM4PqmYf4fcOd58wQ5ElXwP8yKGBo%2BJ1n4Mo%2F0%2FHBhdktPQYNIZxIISYyC6HxKz4SEiTMkyjFMPMUhSOm3O4GnsCKpQ4zxIWm1tP9msiFTQBbCrL7LiUAHBU3BA70ruhYpI&X-Amz-Signature=361ffcdc854ddf133d9f815512a5a3c17b1269b760b16bec486f96486794ee63&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- value loss: Value model의 linear 학습을 위해 쓰이는듯

### Algorithm

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/be5ca694-aab6-43d5-9772-95b44b2d5520/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664AO4UGH%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113454Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAa6Hmk5lW6u1nuFRVT6jEYJciEdDBMVQe6bkv1ZnRt8AiATH95Y03jEoKe40d6pG8Ef%2FmG1DvX%2FsSHthYXTtJFtfiqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM83j72pTknKAq019LKtwDBVVixkTb2wicXpFqEVly8wifNd3kZeL%2F%2BuwojZi0DC8RcCbtvaqdVMbGiaRbUo3wzNf1f7uhfWwvnqSpSvduKGNf0VLRbSRmjsDzXSdZsPkF2SOM%2FW8QFSmyaWTfGEgfuNc5lGYsabV8pHroE2mbVCWtRu5TITHKi6ljgXNHb2%2BjA%2FQcASRZvBFpS12gIbACUbXkCNhM4%2B3a8yfgTp29J6x4g%2BVfW2T%2Fv%2Bp%2FkHrTNL85Z7Ss7XzGHLN5XQSDW3ewE%2Bix9ZrnTlH8CzKOnxLk9lJDd%2FTzBaj15DgkZ%2FyRbRpWS804ekok877qcE77cl%2Fh9sRgTDS6J1dQSJeJ0STl4lX4g1ikGtBq1FaFkRrR5RKwtZMy11jZ%2Bpt2SHFOzUeeWwcl3opShx%2FTGG9Eg9zyw4XhajdxxGbSbJVNGCUksWmWfE5u32U%2FR%2BVaPVC5EouMJ5uS%2Fac1VYaV2vK8qtDXUGeUDhU%2BFJ26iVuLvuJBR30nyBlJNm0SzWgUT0syJWm4xyHgrtk%2FHT%2FkNaHyzA5wXIqdssMTwdBrDaSs8Mf01oBUJAxYTmpf0ikqmmoGECRQ5krTGuf1ckHzOmAXRrMrfIshSdcG%2FXcZLTmkLF%2BdPk5HfB8lDahqlRuQqZgwhf%2FhxAY6pgGIj1nPDbdoqSlG8phjDQkk2xbZkVlSHxGDyj58h%2FEuPlSqUIZ6WeJ%2FhfAtyP0GlR%2FCSiWM0eTxJJbYrkIeo4U4X3hG9pM4PqmYf4fcOd58wQ5ElXwP8yKGBo%2BJ1n4Mo%2F0%2FHBhdktPQYNIZxIISYyC6HxKz4SEiTMkyjFMPMUhSOm3O4GnsCKpQ4zxIWm1tP9msiFTQBbCrL7LiUAHBU3BA70ruhYpI&X-Amz-Signature=afb055038793289118ef46a18b3089f61579d3b0991199bee6b2ad85ea0beb2b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Dataset

- SFT 때 활용된 데이터를 그대로 활용 가능

### Reward function

- fine-tuning을 위해 가장 중요한 설계 요소

- 논문에서는 단순하게 접근

### Training Reward Model 

### Reranking & Majority Voting

학습된 모델에 대한 추가적인 성능 개선 방법론

- Reranking: test query 당 100개의 generation 진행

- majority voting: test query 당 100개의 generation 진행

## 3. Baselines

- SFT: 기존에 마련된 학습 데이터를 활용하여 SFT 학습

- Offline Self-training: SFT (warm up) 학습이 된 모델 이용

- Online Self-training: 학습 과정 중인 모델에 대해 offline과 동일하게 생성 → filtering → SFT 진행

### Hyperparameters

**ReFT**

- 8 x A100 80GB

- SFT epoch: 2

- RLHF epoch: 300 → 지속적으로 성능이 개선되어서 학습을 오래 시켰다고 표현

**SFT**

- epoch: 40 → 성능 개선이 없어 여기서 중단했다고 표현

**Offline Self-training**

- SFT epoch: 40

- self-training epoch: 20 → 성능 개선이 없어 여기서 중단했다고 표현

## 4. Experiments

### Reasoning type

- N-CoT: reasoning을 자연어로 진행

- P-CoT: reasoning을 코드로 진행

### Answer Type

- GSM8K, SVAMP: numeric, 실제 정답 숫자 예측 태스크

- MathQA: multiple choice, 4지선다

### Main Result

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/c06f72c1-729b-4ba0-87ba-a62a0cd3ac6a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664AO4UGH%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113454Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAa6Hmk5lW6u1nuFRVT6jEYJciEdDBMVQe6bkv1ZnRt8AiATH95Y03jEoKe40d6pG8Ef%2FmG1DvX%2FsSHthYXTtJFtfiqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM83j72pTknKAq019LKtwDBVVixkTb2wicXpFqEVly8wifNd3kZeL%2F%2BuwojZi0DC8RcCbtvaqdVMbGiaRbUo3wzNf1f7uhfWwvnqSpSvduKGNf0VLRbSRmjsDzXSdZsPkF2SOM%2FW8QFSmyaWTfGEgfuNc5lGYsabV8pHroE2mbVCWtRu5TITHKi6ljgXNHb2%2BjA%2FQcASRZvBFpS12gIbACUbXkCNhM4%2B3a8yfgTp29J6x4g%2BVfW2T%2Fv%2Bp%2FkHrTNL85Z7Ss7XzGHLN5XQSDW3ewE%2Bix9ZrnTlH8CzKOnxLk9lJDd%2FTzBaj15DgkZ%2FyRbRpWS804ekok877qcE77cl%2Fh9sRgTDS6J1dQSJeJ0STl4lX4g1ikGtBq1FaFkRrR5RKwtZMy11jZ%2Bpt2SHFOzUeeWwcl3opShx%2FTGG9Eg9zyw4XhajdxxGbSbJVNGCUksWmWfE5u32U%2FR%2BVaPVC5EouMJ5uS%2Fac1VYaV2vK8qtDXUGeUDhU%2BFJ26iVuLvuJBR30nyBlJNm0SzWgUT0syJWm4xyHgrtk%2FHT%2FkNaHyzA5wXIqdssMTwdBrDaSs8Mf01oBUJAxYTmpf0ikqmmoGECRQ5krTGuf1ckHzOmAXRrMrfIshSdcG%2FXcZLTmkLF%2BdPk5HfB8lDahqlRuQqZgwhf%2FhxAY6pgGIj1nPDbdoqSlG8phjDQkk2xbZkVlSHxGDyj58h%2FEuPlSqUIZ6WeJ%2FhfAtyP0GlR%2FCSiWM0eTxJJbYrkIeo4U4X3hG9pM4PqmYf4fcOd58wQ5ElXwP8yKGBo%2BJ1n4Mo%2F0%2FHBhdktPQYNIZxIISYyC6HxKz4SEiTMkyjFMPMUhSOm3O4GnsCKpQ4zxIWm1tP9msiFTQBbCrL7LiUAHBU3BA70ruhYpI&X-Amz-Signature=af6e6e0ccc35e231c1de041c310a91bbd42001f551b6556b24ef02bfac91cfa1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- ReFT

- Self-training

### Reward Hacking for MathQA

- MathQA: 4지선다 예측 문제

- MathQA를 직접 정답 숫자 예측 문제로 전환하여 실험 진행

### Majority Voting & Reward Reranking

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/ed09568f-0f0d-4972-90c4-1067be52b865/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664AO4UGH%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113455Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAa6Hmk5lW6u1nuFRVT6jEYJciEdDBMVQe6bkv1ZnRt8AiATH95Y03jEoKe40d6pG8Ef%2FmG1DvX%2FsSHthYXTtJFtfiqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM83j72pTknKAq019LKtwDBVVixkTb2wicXpFqEVly8wifNd3kZeL%2F%2BuwojZi0DC8RcCbtvaqdVMbGiaRbUo3wzNf1f7uhfWwvnqSpSvduKGNf0VLRbSRmjsDzXSdZsPkF2SOM%2FW8QFSmyaWTfGEgfuNc5lGYsabV8pHroE2mbVCWtRu5TITHKi6ljgXNHb2%2BjA%2FQcASRZvBFpS12gIbACUbXkCNhM4%2B3a8yfgTp29J6x4g%2BVfW2T%2Fv%2Bp%2FkHrTNL85Z7Ss7XzGHLN5XQSDW3ewE%2Bix9ZrnTlH8CzKOnxLk9lJDd%2FTzBaj15DgkZ%2FyRbRpWS804ekok877qcE77cl%2Fh9sRgTDS6J1dQSJeJ0STl4lX4g1ikGtBq1FaFkRrR5RKwtZMy11jZ%2Bpt2SHFOzUeeWwcl3opShx%2FTGG9Eg9zyw4XhajdxxGbSbJVNGCUksWmWfE5u32U%2FR%2BVaPVC5EouMJ5uS%2Fac1VYaV2vK8qtDXUGeUDhU%2BFJ26iVuLvuJBR30nyBlJNm0SzWgUT0syJWm4xyHgrtk%2FHT%2FkNaHyzA5wXIqdssMTwdBrDaSs8Mf01oBUJAxYTmpf0ikqmmoGECRQ5krTGuf1ckHzOmAXRrMrfIshSdcG%2FXcZLTmkLF%2BdPk5HfB8lDahqlRuQqZgwhf%2FhxAY6pgGIj1nPDbdoqSlG8phjDQkk2xbZkVlSHxGDyj58h%2FEuPlSqUIZ6WeJ%2FhfAtyP0GlR%2FCSiWM0eTxJJbYrkIeo4U4X3hG9pM4PqmYf4fcOd58wQ5ElXwP8yKGBo%2BJ1n4Mo%2F0%2FHBhdktPQYNIZxIISYyC6HxKz4SEiTMkyjFMPMUhSOm3O4GnsCKpQ4zxIWm1tP9msiFTQBbCrL7LiUAHBU3BA70ruhYpI&X-Amz-Signature=ba55ef508b75b2e7b1a5704315fc16ab8cdb9d66a54bfe92ee8a6b0d958654ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 추가 데이터 annotation을 이용하지 않고도 annotated data를 활용하는 방법론들과 유사한 성능 도출

### ReFT w/ small models

- RLHF 프레임워크의 핵심

### Ablation Study

- KL coefficient 를 지우면 LLM의 본래 파라미터에서 멀어져서 학습이 실패

- 별도의 value model을 사용하는 경우 더 빠르게 모델이 수렴하는 것을 확인

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/61ee2fe7-0318-40a2-963e-f54cfdce1310/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664AO4UGH%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113455Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAa6Hmk5lW6u1nuFRVT6jEYJciEdDBMVQe6bkv1ZnRt8AiATH95Y03jEoKe40d6pG8Ef%2FmG1DvX%2FsSHthYXTtJFtfiqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM83j72pTknKAq019LKtwDBVVixkTb2wicXpFqEVly8wifNd3kZeL%2F%2BuwojZi0DC8RcCbtvaqdVMbGiaRbUo3wzNf1f7uhfWwvnqSpSvduKGNf0VLRbSRmjsDzXSdZsPkF2SOM%2FW8QFSmyaWTfGEgfuNc5lGYsabV8pHroE2mbVCWtRu5TITHKi6ljgXNHb2%2BjA%2FQcASRZvBFpS12gIbACUbXkCNhM4%2B3a8yfgTp29J6x4g%2BVfW2T%2Fv%2Bp%2FkHrTNL85Z7Ss7XzGHLN5XQSDW3ewE%2Bix9ZrnTlH8CzKOnxLk9lJDd%2FTzBaj15DgkZ%2FyRbRpWS804ekok877qcE77cl%2Fh9sRgTDS6J1dQSJeJ0STl4lX4g1ikGtBq1FaFkRrR5RKwtZMy11jZ%2Bpt2SHFOzUeeWwcl3opShx%2FTGG9Eg9zyw4XhajdxxGbSbJVNGCUksWmWfE5u32U%2FR%2BVaPVC5EouMJ5uS%2Fac1VYaV2vK8qtDXUGeUDhU%2BFJ26iVuLvuJBR30nyBlJNm0SzWgUT0syJWm4xyHgrtk%2FHT%2FkNaHyzA5wXIqdssMTwdBrDaSs8Mf01oBUJAxYTmpf0ikqmmoGECRQ5krTGuf1ckHzOmAXRrMrfIshSdcG%2FXcZLTmkLF%2BdPk5HfB8lDahqlRuQqZgwhf%2FhxAY6pgGIj1nPDbdoqSlG8phjDQkk2xbZkVlSHxGDyj58h%2FEuPlSqUIZ6WeJ%2FhfAtyP0GlR%2FCSiWM0eTxJJbYrkIeo4U4X3hG9pM4PqmYf4fcOd58wQ5ElXwP8yKGBo%2BJ1n4Mo%2F0%2FHBhdktPQYNIZxIISYyC6HxKz4SEiTMkyjFMPMUhSOm3O4GnsCKpQ4zxIWm1tP9msiFTQBbCrL7LiUAHBU3BA70ruhYpI&X-Amz-Signature=c6357240a439f0754afdded20d4a809a0c6b90fe93bdab33f65606891ee73a9e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Human Evaluation

- reasoning의 품질이 얼마나 좋은지 3가지 척도(Logic, Naming, Compactness)로 평가 진행

- ReFT가 더 나은 모습을 보임

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/ef6ee6e0-7b09-4e85-84d4-d31bb7922830/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664AO4UGH%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113455Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAa6Hmk5lW6u1nuFRVT6jEYJciEdDBMVQe6bkv1ZnRt8AiATH95Y03jEoKe40d6pG8Ef%2FmG1DvX%2FsSHthYXTtJFtfiqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM83j72pTknKAq019LKtwDBVVixkTb2wicXpFqEVly8wifNd3kZeL%2F%2BuwojZi0DC8RcCbtvaqdVMbGiaRbUo3wzNf1f7uhfWwvnqSpSvduKGNf0VLRbSRmjsDzXSdZsPkF2SOM%2FW8QFSmyaWTfGEgfuNc5lGYsabV8pHroE2mbVCWtRu5TITHKi6ljgXNHb2%2BjA%2FQcASRZvBFpS12gIbACUbXkCNhM4%2B3a8yfgTp29J6x4g%2BVfW2T%2Fv%2Bp%2FkHrTNL85Z7Ss7XzGHLN5XQSDW3ewE%2Bix9ZrnTlH8CzKOnxLk9lJDd%2FTzBaj15DgkZ%2FyRbRpWS804ekok877qcE77cl%2Fh9sRgTDS6J1dQSJeJ0STl4lX4g1ikGtBq1FaFkRrR5RKwtZMy11jZ%2Bpt2SHFOzUeeWwcl3opShx%2FTGG9Eg9zyw4XhajdxxGbSbJVNGCUksWmWfE5u32U%2FR%2BVaPVC5EouMJ5uS%2Fac1VYaV2vK8qtDXUGeUDhU%2BFJ26iVuLvuJBR30nyBlJNm0SzWgUT0syJWm4xyHgrtk%2FHT%2FkNaHyzA5wXIqdssMTwdBrDaSs8Mf01oBUJAxYTmpf0ikqmmoGECRQ5krTGuf1ckHzOmAXRrMrfIshSdcG%2FXcZLTmkLF%2BdPk5HfB8lDahqlRuQqZgwhf%2FhxAY6pgGIj1nPDbdoqSlG8phjDQkk2xbZkVlSHxGDyj58h%2FEuPlSqUIZ6WeJ%2FhfAtyP0GlR%2FCSiWM0eTxJJbYrkIeo4U4X3hG9pM4PqmYf4fcOd58wQ5ElXwP8yKGBo%2BJ1n4Mo%2F0%2FHBhdktPQYNIZxIISYyC6HxKz4SEiTMkyjFMPMUhSOm3O4GnsCKpQ4zxIWm1tP9msiFTQBbCrL7LiUAHBU3BA70ruhYpI&X-Amz-Signature=06a3f5bafbce6005da01aaf247a6cba92e95ca49beb797042eb682f37e9011ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### When ReFT surpasses SFT?

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/15f43899-d30a-419c-bcd7-ebb198eb6a72/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664AO4UGH%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113455Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAa6Hmk5lW6u1nuFRVT6jEYJciEdDBMVQe6bkv1ZnRt8AiATH95Y03jEoKe40d6pG8Ef%2FmG1DvX%2FsSHthYXTtJFtfiqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM83j72pTknKAq019LKtwDBVVixkTb2wicXpFqEVly8wifNd3kZeL%2F%2BuwojZi0DC8RcCbtvaqdVMbGiaRbUo3wzNf1f7uhfWwvnqSpSvduKGNf0VLRbSRmjsDzXSdZsPkF2SOM%2FW8QFSmyaWTfGEgfuNc5lGYsabV8pHroE2mbVCWtRu5TITHKi6ljgXNHb2%2BjA%2FQcASRZvBFpS12gIbACUbXkCNhM4%2B3a8yfgTp29J6x4g%2BVfW2T%2Fv%2Bp%2FkHrTNL85Z7Ss7XzGHLN5XQSDW3ewE%2Bix9ZrnTlH8CzKOnxLk9lJDd%2FTzBaj15DgkZ%2FyRbRpWS804ekok877qcE77cl%2Fh9sRgTDS6J1dQSJeJ0STl4lX4g1ikGtBq1FaFkRrR5RKwtZMy11jZ%2Bpt2SHFOzUeeWwcl3opShx%2FTGG9Eg9zyw4XhajdxxGbSbJVNGCUksWmWfE5u32U%2FR%2BVaPVC5EouMJ5uS%2Fac1VYaV2vK8qtDXUGeUDhU%2BFJ26iVuLvuJBR30nyBlJNm0SzWgUT0syJWm4xyHgrtk%2FHT%2FkNaHyzA5wXIqdssMTwdBrDaSs8Mf01oBUJAxYTmpf0ikqmmoGECRQ5krTGuf1ckHzOmAXRrMrfIshSdcG%2FXcZLTmkLF%2BdPk5HfB8lDahqlRuQqZgwhf%2FhxAY6pgGIj1nPDbdoqSlG8phjDQkk2xbZkVlSHxGDyj58h%2FEuPlSqUIZ6WeJ%2FhfAtyP0GlR%2FCSiWM0eTxJJbYrkIeo4U4X3hG9pM4PqmYf4fcOd58wQ5ElXwP8yKGBo%2BJ1n4Mo%2F0%2FHBhdktPQYNIZxIISYyC6HxKz4SEiTMkyjFMPMUhSOm3O4GnsCKpQ4zxIWm1tP9msiFTQBbCrL7LiUAHBU3BA70ruhYpI&X-Amz-Signature=a4e3c924de2d4a8bce0aedabd07491651e09763806b1f25de02ce9320b78c8ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- SFT warmup step을 달리하며 실험 진행 
