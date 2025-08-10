---
categories:
- paper-reviews
date: '2025-07-15 00:00:00'
description: 논문 리뷰 - Reinforcement Learning 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- language-model
- llm
- paper-review
- pre-training
- reasoning
- reinforcement learning
- reinforcement-learning
thumbnail: assets/img/posts/2025-07-15-search-r1-training-llms-to-reason-and-leverage/thumbnail.jpg
title: 'Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement
  Learning'
---

**논문 정보**
- **Date**: 2025-07-15
- **Reviewer**: 건우 김
- **Property**: Reinforcement Learning

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/8e7d1371-5eab-4baa-94cb-178ccbcff37b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623E2HUM3%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDO0pBaxHhChJR7w3YEmB3OXXyov2ENUcUtfdlQbcdAjAIgFJEIc4Bcg7Sasibu5FTrF5z4bxBmpYHS9umHUEFZgesqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE%2BO347uyagytHF5%2FCrcA4kCyvXxq4bdgSSa3FxaV%2FO31rA%2B9sV%2BGxJUarq7Dbf1R0Vm%2FrJljKd0oGoex%2BW3rVLSIYWqFMRUqlW4FGwCx6WOPeBLJYCudBeKAVRVE7V01jVy8QOK4C%2FmNJRNItzKcijdsw2QfzupUXrlutUUXUHQcyNMOBT%2B6z6Zn%2FvBct3AjrsfGBeVUC3kp3Nj%2FECJWHrNDhgnqF8GH0GmnP2qN5kjoiwoMIa9fjmRLUSG6c56sgK5i7utcYTvdgm42%2BavQiItvp84ZcyO5RHbO733YvxRF%2FGvN7TCk3m1ef9%2F7AaAFFL8MHNGgQUciKxCJoMGT7Lhz3IlrXeHHgG8QHV0vHiw6dpwv7tuefsz9XDnowsHyKh8rvNkmm72Lsp3etHnk88OZ%2FqN5Y5z5Dx7VYIwhXTLfZNQqk%2BYjjvVK%2B6%2B0zQUmJ6hTPKjEk%2BtdE%2B8yrk3O2kWhmJKxAdsclCK1EFuMGoKduqdjf3rfXix21nBe5AeyEUJXiOu7GoAHV4l32KSSl6umyYB6lZbw1k1Nth0dWSEiLkzhmHU9gHzCSjNU5UEw7n9WTftFhAJkdCcnixD3QkCXmEp4GWy1aqcNkDxQ88gCW5or9xtKGni%2BvFt3u5rDqJczBA0ulNaavjeMM%2F%2B4cQGOqUBTZzbwK%2BJXSrwDWvdkeeaExF4NDxoUQL0ZGOLw%2Bulhpc%2FhRywVHYYSWl4uYtL1Xumf6MROQTQSrwo6lWww%2B7hOgxbxd5HcZHpfrRwvwf%2BgjXCUg8ymtzZRj0hF2JpLWAD1uGXB%2Bo9Pm7eVCNcqvXbClX6iWkZbzJY6CyJLu7mwbGway4ITgM1hdAUFThq6tjTQclBgjNIUuYqTrg79Kr3BcV4z9Yt&X-Amz-Signature=4ba55593e1be863a1aff37fbe916e15886e1d2dc4e50e87d17df58dd11ae150d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# Abstract

- Reasoning과 text generation이 가능한 LLM에게 external knowledge와 최신 information을 효율적으로 삽입하는 것은 매우 중요함

- 이 문제를 해결하기 위해 RL을 활용한 reasoning framework인 Search-R1을 소개함

# 1. Introduction

LLM은 natural language understanding과 generation에서 높은 성과를 보여줬지만, 여전히 external sources가 필요한 task에서 한계점을 보여줌. 

→ 즉, 최신 information을 잘 활용할 수 있도록 search engine과 **효과적으로 상호작용하는** 능력이 필수적임

최근까지 LLM과 Search Engine을 결합하는 대표적인 방식은 두가지

1. Retrieval-Augmented Generation (RAG)

1. search engine을 하나의 tool로 활용하는 방식 

위 방법 덕분에 LLM이 external knowledge를 활용할 수 있긴 하지만, 최근 연구 (multi-turn, multi-query retrieval) 역시 본질적으로 **LLM이 search engine과 상호작용하는 방식을 최적화하지 못한 채 prompt에만 의존하는 한계점이 존재함. **

다른 방법으로 LLM이 추론 과정에서 search engine을 포함한 여러 tool을 사용하도록 prompting하거나 training하는 방법들이 있지만

- prompting 방법 역시 LLM의 pre-training 단계에서 경험하지 못한 작업에 generalize가 잘 안되는 문제

- training 기반 방식은 더 나은 adaptability를 보이지만 대규모 high quality annotated trajectories가 필요하고 search 연산이 미분이 불가능하기 때문에 end-to-end gradient descent로 최적화하기 어려움

한편으로 RL은 LLM의 reasoning capability를 높이는 robust 방법으로 최근에 주목 받는데, 이것을 **search-and-reasoning **scenarios에 적용하는 데는 3가지 문제가 있음

1. **RL framework and Stability**: search engine을 어떻게 RL에 효과적으로 통합할지, 특히 검색된 context를 포함할 때 안정적인 최적화를 어떻게 보장할지 명확하지 않음

1. **Multi-Turn Interleaved Reasoning and Search**: 이상적으로는 LLM이 반복적으로 추론하고 search engine을 호출하며 문제의 난이도에 따라 검색 전략을 동적으로 조정할 수 있어야 함

1. **Reward Design**: Search와 Reasoning tasks에 의미 있고 일관된 검색 행동을 학습하게끔 유도할 수 있는 효과적인 reward function 설계가 필요하지만, 단순한 결과 기반 보상이 충분한지는 아직 불확실함.

→ 이러한 문제를 해결하기 위해 ***Search-R1***을 소개함. 이것은 LLM이 자체 추론 과정과 search engine을 interleaved하게 연계하여 사용할 수 있도록 설계가 됨.

주요 특징은 다음과 같음

1. Search engine을 environment의 일부로 modeling하여, **LLM의 token 생성과 검색 결과 호출이 혼합된 trajectory를 샘플링할** 수 있음. 

1. **Multi-turn retrieval과 reasoning을 지원함**. <search>와 </search> token으로 검색 호출을 트리거하고, 검색 결과는 <information>와 </information> 토큰으로, LLM의 추론 단계는 <think>와 </think> 토큰으로, 최종 답변은 <answer>와 </answer> 토큰으로 감싸 구조적이고 반복적인 의사결정이 가능함

1. process-based rewards 대신 단순한 **outcome-based reward function을 적용하여** 복잡성을 줄임

# 2. Related Works

2.1 Large Language Models and Retrieval

(생략)

2.2 Large Language Models and Reinforcement Learning

(생략)

# 3. Search-R1

**(1) extending RL to utilize search engines**

**(2) text generation with an interleaved multi-turn search engine call**

**(3) the training template**

**(4) reward model design**

## 3.1 Reinforcement Learning with a Search Engine

Search-R1은 search engine R을 활용하는 RL의 objective function을 아래와 같이 정의함

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/2d82d6d1-c13f-447c-b24b-e2dbd9ea6f3a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623E2HUM3%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDO0pBaxHhChJR7w3YEmB3OXXyov2ENUcUtfdlQbcdAjAIgFJEIc4Bcg7Sasibu5FTrF5z4bxBmpYHS9umHUEFZgesqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE%2BO347uyagytHF5%2FCrcA4kCyvXxq4bdgSSa3FxaV%2FO31rA%2B9sV%2BGxJUarq7Dbf1R0Vm%2FrJljKd0oGoex%2BW3rVLSIYWqFMRUqlW4FGwCx6WOPeBLJYCudBeKAVRVE7V01jVy8QOK4C%2FmNJRNItzKcijdsw2QfzupUXrlutUUXUHQcyNMOBT%2B6z6Zn%2FvBct3AjrsfGBeVUC3kp3Nj%2FECJWHrNDhgnqF8GH0GmnP2qN5kjoiwoMIa9fjmRLUSG6c56sgK5i7utcYTvdgm42%2BavQiItvp84ZcyO5RHbO733YvxRF%2FGvN7TCk3m1ef9%2F7AaAFFL8MHNGgQUciKxCJoMGT7Lhz3IlrXeHHgG8QHV0vHiw6dpwv7tuefsz9XDnowsHyKh8rvNkmm72Lsp3etHnk88OZ%2FqN5Y5z5Dx7VYIwhXTLfZNQqk%2BYjjvVK%2B6%2B0zQUmJ6hTPKjEk%2BtdE%2B8yrk3O2kWhmJKxAdsclCK1EFuMGoKduqdjf3rfXix21nBe5AeyEUJXiOu7GoAHV4l32KSSl6umyYB6lZbw1k1Nth0dWSEiLkzhmHU9gHzCSjNU5UEw7n9WTftFhAJkdCcnixD3QkCXmEp4GWy1aqcNkDxQ88gCW5or9xtKGni%2BvFt3u5rDqJczBA0ulNaavjeMM%2F%2B4cQGOqUBTZzbwK%2BJXSrwDWvdkeeaExF4NDxoUQL0ZGOLw%2Bulhpc%2FhRywVHYYSWl4uYtL1Xumf6MROQTQSrwo6lWww%2B7hOgxbxd5HcZHpfrRwvwf%2BgjXCUg8ymtzZRj0hF2JpLWAD1uGXB%2Bo9Pm7eVCNcqvXbClX6iWkZbzJY6CyJLu7mwbGway4ITgM1hdAUFThq6tjTQclBgjNIUuYqTrg79Kr3BcV4z9Yt&X-Amz-Signature=accdf9db77c7523c3a4408324a4cae32a09ca46e0fa113d22aa2e6eedf26bd99&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- r_{\phi}: output quality를 평가하는 reward function

- \pi_\theta: policy LLM

- \pi_{ref}: reference LLM

- x: dataset D에서 추출된 input sample

- y: search engine calling 결과와 interleaved된 generated outputs

- D_{KL}: KL-divergence

기존 RL은 원래 \pi_\theta가 생성한 sequence만 학습하지만, Search-R1은 검색 호출과 추론이 교차된 (interleaved) 형태를 학습에 explicit하게 포함함.

즉, 추론 중 검색 결과를 반영하는 흐름을 통해 external information가 필요한 reasoning-intensive tasks에서도 더 효과적인 결정을 내릴 수 있게 해줌

**Loss Masking for Retrieved Tokens**

PPO와 GRPO에서는 token-level loss를 전체 rollout sequence에 대해 계산함. 하지만 Search-R1의 rollout sequence는 LLM이 직접 생성한 token과 external knowledge에서 가져온 token이 함께 포함됨.

LLM이 직접 생성한 token에 대해 손실을 최적화하는 것은 model이 search engine과 효과적으로 상호작용하고 추론하는 능력을 높이는데 도움됨. 그러나, 동일한 최적화를 검색된 token에까지 적용하면 원치 않는 학습 효과가 발생할 수 있음.

따라서, Search-R1은 **검색된 token에 대한 loss masking을 적용하여**, policy gradient objective은 LLM이 생성한 token에 대해서만 계산하고, **검색된 content는 최적화 과정에서 제외됨**. 

→ 검색 기반 생성의 유연성은 유지하면서 학습 안정성을 높임

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/cf86f3f3-4ea6-472c-9bd3-d854c57f2352/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623E2HUM3%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDO0pBaxHhChJR7w3YEmB3OXXyov2ENUcUtfdlQbcdAjAIgFJEIc4Bcg7Sasibu5FTrF5z4bxBmpYHS9umHUEFZgesqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE%2BO347uyagytHF5%2FCrcA4kCyvXxq4bdgSSa3FxaV%2FO31rA%2B9sV%2BGxJUarq7Dbf1R0Vm%2FrJljKd0oGoex%2BW3rVLSIYWqFMRUqlW4FGwCx6WOPeBLJYCudBeKAVRVE7V01jVy8QOK4C%2FmNJRNItzKcijdsw2QfzupUXrlutUUXUHQcyNMOBT%2B6z6Zn%2FvBct3AjrsfGBeVUC3kp3Nj%2FECJWHrNDhgnqF8GH0GmnP2qN5kjoiwoMIa9fjmRLUSG6c56sgK5i7utcYTvdgm42%2BavQiItvp84ZcyO5RHbO733YvxRF%2FGvN7TCk3m1ef9%2F7AaAFFL8MHNGgQUciKxCJoMGT7Lhz3IlrXeHHgG8QHV0vHiw6dpwv7tuefsz9XDnowsHyKh8rvNkmm72Lsp3etHnk88OZ%2FqN5Y5z5Dx7VYIwhXTLfZNQqk%2BYjjvVK%2B6%2B0zQUmJ6hTPKjEk%2BtdE%2B8yrk3O2kWhmJKxAdsclCK1EFuMGoKduqdjf3rfXix21nBe5AeyEUJXiOu7GoAHV4l32KSSl6umyYB6lZbw1k1Nth0dWSEiLkzhmHU9gHzCSjNU5UEw7n9WTftFhAJkdCcnixD3QkCXmEp4GWy1aqcNkDxQ88gCW5or9xtKGni%2BvFt3u5rDqJczBA0ulNaavjeMM%2F%2B4cQGOqUBTZzbwK%2BJXSrwDWvdkeeaExF4NDxoUQL0ZGOLw%2Bulhpc%2FhRywVHYYSWl4uYtL1Xumf6MROQTQSrwo6lWww%2B7hOgxbxd5HcZHpfrRwvwf%2BgjXCUg8ymtzZRj0hF2JpLWAD1uGXB%2Bo9Pm7eVCNcqvXbClX6iWkZbzJY6CyJLu7mwbGway4ITgM1hdAUFThq6tjTQclBgjNIUuYqTrg79Kr3BcV4z9Yt&X-Amz-Signature=503dd915687562b4cf93b2ba7471ee98bbf518c6b5c32c1cfb7a1f58eb295aad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**PPO with Search Engine**

Search-R1에서는 검색 호출이 포함된 시나리오에 맞춰 PPO를 적용함

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/3723c33f-e9c9-4bfc-924b-6eb5a0bfcf89/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623E2HUM3%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDO0pBaxHhChJR7w3YEmB3OXXyov2ENUcUtfdlQbcdAjAIgFJEIc4Bcg7Sasibu5FTrF5z4bxBmpYHS9umHUEFZgesqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE%2BO347uyagytHF5%2FCrcA4kCyvXxq4bdgSSa3FxaV%2FO31rA%2B9sV%2BGxJUarq7Dbf1R0Vm%2FrJljKd0oGoex%2BW3rVLSIYWqFMRUqlW4FGwCx6WOPeBLJYCudBeKAVRVE7V01jVy8QOK4C%2FmNJRNItzKcijdsw2QfzupUXrlutUUXUHQcyNMOBT%2B6z6Zn%2FvBct3AjrsfGBeVUC3kp3Nj%2FECJWHrNDhgnqF8GH0GmnP2qN5kjoiwoMIa9fjmRLUSG6c56sgK5i7utcYTvdgm42%2BavQiItvp84ZcyO5RHbO733YvxRF%2FGvN7TCk3m1ef9%2F7AaAFFL8MHNGgQUciKxCJoMGT7Lhz3IlrXeHHgG8QHV0vHiw6dpwv7tuefsz9XDnowsHyKh8rvNkmm72Lsp3etHnk88OZ%2FqN5Y5z5Dx7VYIwhXTLfZNQqk%2BYjjvVK%2B6%2B0zQUmJ6hTPKjEk%2BtdE%2B8yrk3O2kWhmJKxAdsclCK1EFuMGoKduqdjf3rfXix21nBe5AeyEUJXiOu7GoAHV4l32KSSl6umyYB6lZbw1k1Nth0dWSEiLkzhmHU9gHzCSjNU5UEw7n9WTftFhAJkdCcnixD3QkCXmEp4GWy1aqcNkDxQ88gCW5or9xtKGni%2BvFt3u5rDqJczBA0ulNaavjeMM%2F%2B4cQGOqUBTZzbwK%2BJXSrwDWvdkeeaExF4NDxoUQL0ZGOLw%2Bulhpc%2FhRywVHYYSWl4uYtL1Xumf6MROQTQSrwo6lWww%2B7hOgxbxd5HcZHpfrRwvwf%2BgjXCUg8ymtzZRj0hF2JpLWAD1uGXB%2Bo9Pm7eVCNcqvXbClX6iWkZbzJY6CyJLu7mwbGway4ITgM1hdAUFThq6tjTQclBgjNIUuYqTrg79Kr3BcV4z9Yt&X-Amz-Signature=94c094ae2cc315d0eca0a442eb6458033bc79beb66f38ddea9322ad8d01de377&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- \pi_{\theta}: current policy

- \pi_{old}: previous policy

- I(y_t): token loss masking 연산으로, y_t가 LLM이 생성한 token이면 1, 검색된 token이면 0으로 설정

**GRPO with Search Engine**

GRPO 역시 PPO와 마찬가지로 Search Engine을 적용할때, 검색된 token은 masking 적용함

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/975e2f45-4960-4c9a-a908-6b8189e2a1fa/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623E2HUM3%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDO0pBaxHhChJR7w3YEmB3OXXyov2ENUcUtfdlQbcdAjAIgFJEIc4Bcg7Sasibu5FTrF5z4bxBmpYHS9umHUEFZgesqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE%2BO347uyagytHF5%2FCrcA4kCyvXxq4bdgSSa3FxaV%2FO31rA%2B9sV%2BGxJUarq7Dbf1R0Vm%2FrJljKd0oGoex%2BW3rVLSIYWqFMRUqlW4FGwCx6WOPeBLJYCudBeKAVRVE7V01jVy8QOK4C%2FmNJRNItzKcijdsw2QfzupUXrlutUUXUHQcyNMOBT%2B6z6Zn%2FvBct3AjrsfGBeVUC3kp3Nj%2FECJWHrNDhgnqF8GH0GmnP2qN5kjoiwoMIa9fjmRLUSG6c56sgK5i7utcYTvdgm42%2BavQiItvp84ZcyO5RHbO733YvxRF%2FGvN7TCk3m1ef9%2F7AaAFFL8MHNGgQUciKxCJoMGT7Lhz3IlrXeHHgG8QHV0vHiw6dpwv7tuefsz9XDnowsHyKh8rvNkmm72Lsp3etHnk88OZ%2FqN5Y5z5Dx7VYIwhXTLfZNQqk%2BYjjvVK%2B6%2B0zQUmJ6hTPKjEk%2BtdE%2B8yrk3O2kWhmJKxAdsclCK1EFuMGoKduqdjf3rfXix21nBe5AeyEUJXiOu7GoAHV4l32KSSl6umyYB6lZbw1k1Nth0dWSEiLkzhmHU9gHzCSjNU5UEw7n9WTftFhAJkdCcnixD3QkCXmEp4GWy1aqcNkDxQ88gCW5or9xtKGni%2BvFt3u5rDqJczBA0ulNaavjeMM%2F%2B4cQGOqUBTZzbwK%2BJXSrwDWvdkeeaExF4NDxoUQL0ZGOLw%2Bulhpc%2FhRywVHYYSWl4uYtL1Xumf6MROQTQSrwo6lWww%2B7hOgxbxd5HcZHpfrRwvwf%2BgjXCUg8ymtzZRj0hF2JpLWAD1uGXB%2Bo9Pm7eVCNcqvXbClX6iWkZbzJY6CyJLu7mwbGway4ITgM1hdAUFThq6tjTQclBgjNIUuYqTrg79Kr3BcV4z9Yt&X-Amz-Signature=c8a6fedff259ed776cc5d22a801489021cd6d4244c07e8ca2a71aaf8ad6caa59&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 3.2 Generation with Multi-turn Search Engine Calling

Search-R1이 어떻게 multi-turn search와 text 생성을 interleaved하게 수행하는지 rollout process를 수식적으로 나타내면 다음과 같음

Search-R1의 생성 과정은 iterative한 구조로 진행됨

* **LLM은 text를 생성하다가 필요할 때마다 external search engine queries를 보낸 뒤 검색 결과를 다시 반영하여 다음 generation step을 수행하며 이어가는 방식**

- system instruction은 LLM에게 external retrieval이 필요할 때 search query를 <search>와 <\search>  token으로 감싸도록 함

- generated sequence에 이러한 token이 감지되면, system은 query를 추출해 search engine에 전달하고 적절한 relevant results를 가져옴

- retrieved information은 <information>과 <\information>  token으로 감싸져 현재 rollout 시퀀스에 추가됨. 이렇게 추가된 정보는 next generation step에 추가 context로 활용

위 과정이 반복적으로 이어가다가 아래 두 가지 조건 중 하나를 만족하면 종료함

1. 사전에 정의된 최대 행동 횟수에 도달할 때

1. 모델이 최종 응답을 생성하여 이를 <answer>와 <\answer> token으로 감쌀때

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/1647f2c8-1cc0-45a2-af62-be9db8b7f2af/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623E2HUM3%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDO0pBaxHhChJR7w3YEmB3OXXyov2ENUcUtfdlQbcdAjAIgFJEIc4Bcg7Sasibu5FTrF5z4bxBmpYHS9umHUEFZgesqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE%2BO347uyagytHF5%2FCrcA4kCyvXxq4bdgSSa3FxaV%2FO31rA%2B9sV%2BGxJUarq7Dbf1R0Vm%2FrJljKd0oGoex%2BW3rVLSIYWqFMRUqlW4FGwCx6WOPeBLJYCudBeKAVRVE7V01jVy8QOK4C%2FmNJRNItzKcijdsw2QfzupUXrlutUUXUHQcyNMOBT%2B6z6Zn%2FvBct3AjrsfGBeVUC3kp3Nj%2FECJWHrNDhgnqF8GH0GmnP2qN5kjoiwoMIa9fjmRLUSG6c56sgK5i7utcYTvdgm42%2BavQiItvp84ZcyO5RHbO733YvxRF%2FGvN7TCk3m1ef9%2F7AaAFFL8MHNGgQUciKxCJoMGT7Lhz3IlrXeHHgG8QHV0vHiw6dpwv7tuefsz9XDnowsHyKh8rvNkmm72Lsp3etHnk88OZ%2FqN5Y5z5Dx7VYIwhXTLfZNQqk%2BYjjvVK%2B6%2B0zQUmJ6hTPKjEk%2BtdE%2B8yrk3O2kWhmJKxAdsclCK1EFuMGoKduqdjf3rfXix21nBe5AeyEUJXiOu7GoAHV4l32KSSl6umyYB6lZbw1k1Nth0dWSEiLkzhmHU9gHzCSjNU5UEw7n9WTftFhAJkdCcnixD3QkCXmEp4GWy1aqcNkDxQ88gCW5or9xtKGni%2BvFt3u5rDqJczBA0ulNaavjeMM%2F%2B4cQGOqUBTZzbwK%2BJXSrwDWvdkeeaExF4NDxoUQL0ZGOLw%2Bulhpc%2FhRywVHYYSWl4uYtL1Xumf6MROQTQSrwo6lWww%2B7hOgxbxd5HcZHpfrRwvwf%2BgjXCUg8ymtzZRj0hF2JpLWAD1uGXB%2Bo9Pm7eVCNcqvXbClX6iWkZbzJY6CyJLu7mwbGway4ITgM1hdAUFThq6tjTQclBgjNIUuYqTrg79Kr3BcV4z9Yt&X-Amz-Signature=edb8e553f833256af533ecd02faca65b20932602df9346df118a70756fabd143&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 3.3 Training Template

Search-R1을 학습시킬때 사용하는 prompt template

- 아래 template은 모델이 출력할 구조를 think → search → answer 순서로 명확히 나누도록 유도함

- 다만 특정 해결 방식이나 반영 수준을 강제하지 않아 모델이 RL 과정에서 자연스럽게 학습하도록 설계함 (구조적 형식만 따르게 제한함)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/351e2f14-e2bc-4d4b-b0e8-7bcec485137f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623E2HUM3%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDO0pBaxHhChJR7w3YEmB3OXXyov2ENUcUtfdlQbcdAjAIgFJEIc4Bcg7Sasibu5FTrF5z4bxBmpYHS9umHUEFZgesqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE%2BO347uyagytHF5%2FCrcA4kCyvXxq4bdgSSa3FxaV%2FO31rA%2B9sV%2BGxJUarq7Dbf1R0Vm%2FrJljKd0oGoex%2BW3rVLSIYWqFMRUqlW4FGwCx6WOPeBLJYCudBeKAVRVE7V01jVy8QOK4C%2FmNJRNItzKcijdsw2QfzupUXrlutUUXUHQcyNMOBT%2B6z6Zn%2FvBct3AjrsfGBeVUC3kp3Nj%2FECJWHrNDhgnqF8GH0GmnP2qN5kjoiwoMIa9fjmRLUSG6c56sgK5i7utcYTvdgm42%2BavQiItvp84ZcyO5RHbO733YvxRF%2FGvN7TCk3m1ef9%2F7AaAFFL8MHNGgQUciKxCJoMGT7Lhz3IlrXeHHgG8QHV0vHiw6dpwv7tuefsz9XDnowsHyKh8rvNkmm72Lsp3etHnk88OZ%2FqN5Y5z5Dx7VYIwhXTLfZNQqk%2BYjjvVK%2B6%2B0zQUmJ6hTPKjEk%2BtdE%2B8yrk3O2kWhmJKxAdsclCK1EFuMGoKduqdjf3rfXix21nBe5AeyEUJXiOu7GoAHV4l32KSSl6umyYB6lZbw1k1Nth0dWSEiLkzhmHU9gHzCSjNU5UEw7n9WTftFhAJkdCcnixD3QkCXmEp4GWy1aqcNkDxQ88gCW5or9xtKGni%2BvFt3u5rDqJczBA0ulNaavjeMM%2F%2B4cQGOqUBTZzbwK%2BJXSrwDWvdkeeaExF4NDxoUQL0ZGOLw%2Bulhpc%2FhRywVHYYSWl4uYtL1Xumf6MROQTQSrwo6lWww%2B7hOgxbxd5HcZHpfrRwvwf%2BgjXCUg8ymtzZRj0hF2JpLWAD1uGXB%2Bo9Pm7eVCNcqvXbClX6iWkZbzJY6CyJLu7mwbGway4ITgM1hdAUFThq6tjTQclBgjNIUuYqTrg79Kr3BcV4z9Yt&X-Amz-Signature=73ed8eab8a830979e32070192055e44847adf92ee593efa038572a2bb86cad44&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**Case Study**

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/3476ceb9-5137-47f6-ad70-44295420f9ba/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623E2HUM3%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDO0pBaxHhChJR7w3YEmB3OXXyov2ENUcUtfdlQbcdAjAIgFJEIc4Bcg7Sasibu5FTrF5z4bxBmpYHS9umHUEFZgesqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE%2BO347uyagytHF5%2FCrcA4kCyvXxq4bdgSSa3FxaV%2FO31rA%2B9sV%2BGxJUarq7Dbf1R0Vm%2FrJljKd0oGoex%2BW3rVLSIYWqFMRUqlW4FGwCx6WOPeBLJYCudBeKAVRVE7V01jVy8QOK4C%2FmNJRNItzKcijdsw2QfzupUXrlutUUXUHQcyNMOBT%2B6z6Zn%2FvBct3AjrsfGBeVUC3kp3Nj%2FECJWHrNDhgnqF8GH0GmnP2qN5kjoiwoMIa9fjmRLUSG6c56sgK5i7utcYTvdgm42%2BavQiItvp84ZcyO5RHbO733YvxRF%2FGvN7TCk3m1ef9%2F7AaAFFL8MHNGgQUciKxCJoMGT7Lhz3IlrXeHHgG8QHV0vHiw6dpwv7tuefsz9XDnowsHyKh8rvNkmm72Lsp3etHnk88OZ%2FqN5Y5z5Dx7VYIwhXTLfZNQqk%2BYjjvVK%2B6%2B0zQUmJ6hTPKjEk%2BtdE%2B8yrk3O2kWhmJKxAdsclCK1EFuMGoKduqdjf3rfXix21nBe5AeyEUJXiOu7GoAHV4l32KSSl6umyYB6lZbw1k1Nth0dWSEiLkzhmHU9gHzCSjNU5UEw7n9WTftFhAJkdCcnixD3QkCXmEp4GWy1aqcNkDxQ88gCW5or9xtKGni%2BvFt3u5rDqJczBA0ulNaavjeMM%2F%2B4cQGOqUBTZzbwK%2BJXSrwDWvdkeeaExF4NDxoUQL0ZGOLw%2Bulhpc%2FhRywVHYYSWl4uYtL1Xumf6MROQTQSrwo6lWww%2B7hOgxbxd5HcZHpfrRwvwf%2BgjXCUg8ymtzZRj0hF2JpLWAD1uGXB%2Bo9Pm7eVCNcqvXbClX6iWkZbzJY6CyJLu7mwbGway4ITgM1hdAUFThq6tjTQclBgjNIUuYqTrg79Kr3BcV4z9Yt&X-Amz-Signature=c3679cac18ed61c084fb48350f46ffa4f2437dd8705305994107ef00596827a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 3.4 Reward Modeling

Search-R1은 outcome-based rule-based reward function을 사용함

- 예를 들어, factual reasoning task에서 정답과 모델의 출력이 일치하는지 exact match로 평가함

- 별도의 형식 보상이나 복잡한 과정 기반 보상은 사용하지 않고, 신경망 기반 보상 모델도 학습하지 않아 학습 복잡성을 줄임

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/c989f85c-f315-417c-9abd-8a2d86df00ba/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623E2HUM3%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDO0pBaxHhChJR7w3YEmB3OXXyov2ENUcUtfdlQbcdAjAIgFJEIc4Bcg7Sasibu5FTrF5z4bxBmpYHS9umHUEFZgesqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE%2BO347uyagytHF5%2FCrcA4kCyvXxq4bdgSSa3FxaV%2FO31rA%2B9sV%2BGxJUarq7Dbf1R0Vm%2FrJljKd0oGoex%2BW3rVLSIYWqFMRUqlW4FGwCx6WOPeBLJYCudBeKAVRVE7V01jVy8QOK4C%2FmNJRNItzKcijdsw2QfzupUXrlutUUXUHQcyNMOBT%2B6z6Zn%2FvBct3AjrsfGBeVUC3kp3Nj%2FECJWHrNDhgnqF8GH0GmnP2qN5kjoiwoMIa9fjmRLUSG6c56sgK5i7utcYTvdgm42%2BavQiItvp84ZcyO5RHbO733YvxRF%2FGvN7TCk3m1ef9%2F7AaAFFL8MHNGgQUciKxCJoMGT7Lhz3IlrXeHHgG8QHV0vHiw6dpwv7tuefsz9XDnowsHyKh8rvNkmm72Lsp3etHnk88OZ%2FqN5Y5z5Dx7VYIwhXTLfZNQqk%2BYjjvVK%2B6%2B0zQUmJ6hTPKjEk%2BtdE%2B8yrk3O2kWhmJKxAdsclCK1EFuMGoKduqdjf3rfXix21nBe5AeyEUJXiOu7GoAHV4l32KSSl6umyYB6lZbw1k1Nth0dWSEiLkzhmHU9gHzCSjNU5UEw7n9WTftFhAJkdCcnixD3QkCXmEp4GWy1aqcNkDxQ88gCW5or9xtKGni%2BvFt3u5rDqJczBA0ulNaavjeMM%2F%2B4cQGOqUBTZzbwK%2BJXSrwDWvdkeeaExF4NDxoUQL0ZGOLw%2Bulhpc%2FhRywVHYYSWl4uYtL1Xumf6MROQTQSrwo6lWww%2B7hOgxbxd5HcZHpfrRwvwf%2BgjXCUg8ymtzZRj0hF2JpLWAD1uGXB%2Bo9Pm7eVCNcqvXbClX6iWkZbzJY6CyJLu7mwbGway4ITgM1hdAUFThq6tjTQclBgjNIUuYqTrg79Kr3BcV4z9Yt&X-Amz-Signature=100e909f7f17cab44119e4eae514088be1f06c5cd3839582cae80a7a819e2be7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# 4. Main Results

## 4.1 Datasets

1. General QA

1. Multi-Hop QA

## 4.2 Baselines
