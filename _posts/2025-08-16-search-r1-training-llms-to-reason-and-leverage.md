---
categories:
- paper-reviews
date: '2025-08-16 00:00:00'
description: 논문 리뷰 - Reinforcement Learning 관련 연구
giscus_comments: true
layout: post
related_posts: false
slug: 2025-08-16-search-r1-training-llms-to-reason-and-leverage
tags:
- language-model
- llm
- paper-review
- pre-training
- reasoning
- reinforcement learning
- reinforcement-learning
title: 'Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement
  Learning'
---

**논문 정보**
- **Date**: 2025-07-15
- **Reviewer**: 건우 김
- **Property**: Reinforcement Learning

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/8e7d1371-5eab-4baa-94cb-178ccbcff37b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJUT7ISX%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDtJyHDVwEuFPLVpZ%2FlwhdpDNOD%2FsazZ%2Fsfe1VDAY3RQIgN33JyFwVV%2FUCG3auMF5rqcM3tfoyHqYW%2FXC5cdtBsjcqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDADelR3MIWZzv%2FWs1ircA%2FeImJGgfNFoap98RTbu5%2BbiKJ9PXPVEbum41Gei83MoHu3nbjCLwW4b1ruWHk%2FnG6derYIiyy4q%2BePoIHJfeKSz4gWdMWdg2G6W1zChfGtsKQIm1%2FwdNEL83xvutkwfrulL4VhEiF4zM4nWQoiipTwSj2sWRULqBeKtfBwTbelNY3Ry0vsOLcy8%2FDtFU%2BogOw9Qg8Es2CDv9De00w2rPxMLqQ9Ty1RmkUJNucntymK%2BRpI77HlhXldPRqL8CiwD3OtFZvxxxQHkfJj%2F9rafzPe%2ByKzNPZ3Es0ifyMVCyqWaYsTrv0dyLp3U3j51H9fXAMZFvnSDTfrw8Yu%2BgeLLb67jExsdy%2BQzZ8FQ%2B0Xy9%2Bq2ChIFLSfrHZ9lVlCmEqx43T7xpquSEnwsDRy2W4wqyo8MllV7dI5JpfgZA6b0uzO2YOpoRwKiVYi%2BlpDdwtHQ42gJJsCz4QQ4XGn6iZa2XL1%2FcirgPoIMFKxVO1SJOoWE4bV6L765LGqyPQRF1Lrgxb5cMKWq%2BrlgFgMYw3mLeqvZFN4OS9uNQ6cpjRQJjsRLg8vigxF2RniWFLo8MucPzag%2Fj6%2BS4gfwimsms0IZdMVAfxci0FhVg%2BRXMhjHK7xQHZzJ6Tqnso2xD0WOMLbT4cQGOqUB5tcIME1X4DmGmohViSkmK%2B%2FNwGFjHe0oUCKdJ5%2FxnFfcRDC5DFFzi3l2ZSDsNWWsyH2s5vvlSBn0jmZzp8c%2BOdJId14LpB6gKTl21oQq9G4kfUob4aJiic%2F4BkuXzaa7w2marzfufFeJOp98hKAQsTH5xYBUIibocoVeY0UdR9%2FFdKyV6ox1MbrCleJA%2FNqxFiUvn60bTaYbkZVOkLfEAq2tAk9f&X-Amz-Signature=0d48b8e328035b29f4aea241c8bad3c92c1b1486a57b622df520610426c16ba0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/2d82d6d1-c13f-447c-b24b-e2dbd9ea6f3a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJUT7ISX%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDtJyHDVwEuFPLVpZ%2FlwhdpDNOD%2FsazZ%2Fsfe1VDAY3RQIgN33JyFwVV%2FUCG3auMF5rqcM3tfoyHqYW%2FXC5cdtBsjcqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDADelR3MIWZzv%2FWs1ircA%2FeImJGgfNFoap98RTbu5%2BbiKJ9PXPVEbum41Gei83MoHu3nbjCLwW4b1ruWHk%2FnG6derYIiyy4q%2BePoIHJfeKSz4gWdMWdg2G6W1zChfGtsKQIm1%2FwdNEL83xvutkwfrulL4VhEiF4zM4nWQoiipTwSj2sWRULqBeKtfBwTbelNY3Ry0vsOLcy8%2FDtFU%2BogOw9Qg8Es2CDv9De00w2rPxMLqQ9Ty1RmkUJNucntymK%2BRpI77HlhXldPRqL8CiwD3OtFZvxxxQHkfJj%2F9rafzPe%2ByKzNPZ3Es0ifyMVCyqWaYsTrv0dyLp3U3j51H9fXAMZFvnSDTfrw8Yu%2BgeLLb67jExsdy%2BQzZ8FQ%2B0Xy9%2Bq2ChIFLSfrHZ9lVlCmEqx43T7xpquSEnwsDRy2W4wqyo8MllV7dI5JpfgZA6b0uzO2YOpoRwKiVYi%2BlpDdwtHQ42gJJsCz4QQ4XGn6iZa2XL1%2FcirgPoIMFKxVO1SJOoWE4bV6L765LGqyPQRF1Lrgxb5cMKWq%2BrlgFgMYw3mLeqvZFN4OS9uNQ6cpjRQJjsRLg8vigxF2RniWFLo8MucPzag%2Fj6%2BS4gfwimsms0IZdMVAfxci0FhVg%2BRXMhjHK7xQHZzJ6Tqnso2xD0WOMLbT4cQGOqUB5tcIME1X4DmGmohViSkmK%2B%2FNwGFjHe0oUCKdJ5%2FxnFfcRDC5DFFzi3l2ZSDsNWWsyH2s5vvlSBn0jmZzp8c%2BOdJId14LpB6gKTl21oQq9G4kfUob4aJiic%2F4BkuXzaa7w2marzfufFeJOp98hKAQsTH5xYBUIibocoVeY0UdR9%2FFdKyV6ox1MbrCleJA%2FNqxFiUvn60bTaYbkZVOkLfEAq2tAk9f&X-Amz-Signature=261c23cad76eda66c68fb16e8fcea4835e4f1aa76cbd6ec4efc44f21dce2f10e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/cf86f3f3-4ea6-472c-9bd3-d854c57f2352/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJUT7ISX%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDtJyHDVwEuFPLVpZ%2FlwhdpDNOD%2FsazZ%2Fsfe1VDAY3RQIgN33JyFwVV%2FUCG3auMF5rqcM3tfoyHqYW%2FXC5cdtBsjcqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDADelR3MIWZzv%2FWs1ircA%2FeImJGgfNFoap98RTbu5%2BbiKJ9PXPVEbum41Gei83MoHu3nbjCLwW4b1ruWHk%2FnG6derYIiyy4q%2BePoIHJfeKSz4gWdMWdg2G6W1zChfGtsKQIm1%2FwdNEL83xvutkwfrulL4VhEiF4zM4nWQoiipTwSj2sWRULqBeKtfBwTbelNY3Ry0vsOLcy8%2FDtFU%2BogOw9Qg8Es2CDv9De00w2rPxMLqQ9Ty1RmkUJNucntymK%2BRpI77HlhXldPRqL8CiwD3OtFZvxxxQHkfJj%2F9rafzPe%2ByKzNPZ3Es0ifyMVCyqWaYsTrv0dyLp3U3j51H9fXAMZFvnSDTfrw8Yu%2BgeLLb67jExsdy%2BQzZ8FQ%2B0Xy9%2Bq2ChIFLSfrHZ9lVlCmEqx43T7xpquSEnwsDRy2W4wqyo8MllV7dI5JpfgZA6b0uzO2YOpoRwKiVYi%2BlpDdwtHQ42gJJsCz4QQ4XGn6iZa2XL1%2FcirgPoIMFKxVO1SJOoWE4bV6L765LGqyPQRF1Lrgxb5cMKWq%2BrlgFgMYw3mLeqvZFN4OS9uNQ6cpjRQJjsRLg8vigxF2RniWFLo8MucPzag%2Fj6%2BS4gfwimsms0IZdMVAfxci0FhVg%2BRXMhjHK7xQHZzJ6Tqnso2xD0WOMLbT4cQGOqUB5tcIME1X4DmGmohViSkmK%2B%2FNwGFjHe0oUCKdJ5%2FxnFfcRDC5DFFzi3l2ZSDsNWWsyH2s5vvlSBn0jmZzp8c%2BOdJId14LpB6gKTl21oQq9G4kfUob4aJiic%2F4BkuXzaa7w2marzfufFeJOp98hKAQsTH5xYBUIibocoVeY0UdR9%2FFdKyV6ox1MbrCleJA%2FNqxFiUvn60bTaYbkZVOkLfEAq2tAk9f&X-Amz-Signature=0525c5f24d719aadabc65b9b36ea47fcae8a4c256ed156cc2735a2000351d1c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**PPO with Search Engine**

Search-R1에서는 검색 호출이 포함된 시나리오에 맞춰 PPO를 적용함

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/3723c33f-e9c9-4bfc-924b-6eb5a0bfcf89/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJUT7ISX%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDtJyHDVwEuFPLVpZ%2FlwhdpDNOD%2FsazZ%2Fsfe1VDAY3RQIgN33JyFwVV%2FUCG3auMF5rqcM3tfoyHqYW%2FXC5cdtBsjcqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDADelR3MIWZzv%2FWs1ircA%2FeImJGgfNFoap98RTbu5%2BbiKJ9PXPVEbum41Gei83MoHu3nbjCLwW4b1ruWHk%2FnG6derYIiyy4q%2BePoIHJfeKSz4gWdMWdg2G6W1zChfGtsKQIm1%2FwdNEL83xvutkwfrulL4VhEiF4zM4nWQoiipTwSj2sWRULqBeKtfBwTbelNY3Ry0vsOLcy8%2FDtFU%2BogOw9Qg8Es2CDv9De00w2rPxMLqQ9Ty1RmkUJNucntymK%2BRpI77HlhXldPRqL8CiwD3OtFZvxxxQHkfJj%2F9rafzPe%2ByKzNPZ3Es0ifyMVCyqWaYsTrv0dyLp3U3j51H9fXAMZFvnSDTfrw8Yu%2BgeLLb67jExsdy%2BQzZ8FQ%2B0Xy9%2Bq2ChIFLSfrHZ9lVlCmEqx43T7xpquSEnwsDRy2W4wqyo8MllV7dI5JpfgZA6b0uzO2YOpoRwKiVYi%2BlpDdwtHQ42gJJsCz4QQ4XGn6iZa2XL1%2FcirgPoIMFKxVO1SJOoWE4bV6L765LGqyPQRF1Lrgxb5cMKWq%2BrlgFgMYw3mLeqvZFN4OS9uNQ6cpjRQJjsRLg8vigxF2RniWFLo8MucPzag%2Fj6%2BS4gfwimsms0IZdMVAfxci0FhVg%2BRXMhjHK7xQHZzJ6Tqnso2xD0WOMLbT4cQGOqUB5tcIME1X4DmGmohViSkmK%2B%2FNwGFjHe0oUCKdJ5%2FxnFfcRDC5DFFzi3l2ZSDsNWWsyH2s5vvlSBn0jmZzp8c%2BOdJId14LpB6gKTl21oQq9G4kfUob4aJiic%2F4BkuXzaa7w2marzfufFeJOp98hKAQsTH5xYBUIibocoVeY0UdR9%2FFdKyV6ox1MbrCleJA%2FNqxFiUvn60bTaYbkZVOkLfEAq2tAk9f&X-Amz-Signature=065d4975f15df4b2f3b976995bff15cf64af6de5a8c2fc530c6a15c0d91560a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- \pi_{\theta}: current policy

- \pi_{old}: previous policy

- I(y_t): token loss masking 연산으로, y_t가 LLM이 생성한 token이면 1, 검색된 token이면 0으로 설정

**GRPO with Search Engine**

GRPO 역시 PPO와 마찬가지로 Search Engine을 적용할때, 검색된 token은 masking 적용함

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/975e2f45-4960-4c9a-a908-6b8189e2a1fa/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJUT7ISX%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDtJyHDVwEuFPLVpZ%2FlwhdpDNOD%2FsazZ%2Fsfe1VDAY3RQIgN33JyFwVV%2FUCG3auMF5rqcM3tfoyHqYW%2FXC5cdtBsjcqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDADelR3MIWZzv%2FWs1ircA%2FeImJGgfNFoap98RTbu5%2BbiKJ9PXPVEbum41Gei83MoHu3nbjCLwW4b1ruWHk%2FnG6derYIiyy4q%2BePoIHJfeKSz4gWdMWdg2G6W1zChfGtsKQIm1%2FwdNEL83xvutkwfrulL4VhEiF4zM4nWQoiipTwSj2sWRULqBeKtfBwTbelNY3Ry0vsOLcy8%2FDtFU%2BogOw9Qg8Es2CDv9De00w2rPxMLqQ9Ty1RmkUJNucntymK%2BRpI77HlhXldPRqL8CiwD3OtFZvxxxQHkfJj%2F9rafzPe%2ByKzNPZ3Es0ifyMVCyqWaYsTrv0dyLp3U3j51H9fXAMZFvnSDTfrw8Yu%2BgeLLb67jExsdy%2BQzZ8FQ%2B0Xy9%2Bq2ChIFLSfrHZ9lVlCmEqx43T7xpquSEnwsDRy2W4wqyo8MllV7dI5JpfgZA6b0uzO2YOpoRwKiVYi%2BlpDdwtHQ42gJJsCz4QQ4XGn6iZa2XL1%2FcirgPoIMFKxVO1SJOoWE4bV6L765LGqyPQRF1Lrgxb5cMKWq%2BrlgFgMYw3mLeqvZFN4OS9uNQ6cpjRQJjsRLg8vigxF2RniWFLo8MucPzag%2Fj6%2BS4gfwimsms0IZdMVAfxci0FhVg%2BRXMhjHK7xQHZzJ6Tqnso2xD0WOMLbT4cQGOqUB5tcIME1X4DmGmohViSkmK%2B%2FNwGFjHe0oUCKdJ5%2FxnFfcRDC5DFFzi3l2ZSDsNWWsyH2s5vvlSBn0jmZzp8c%2BOdJId14LpB6gKTl21oQq9G4kfUob4aJiic%2F4BkuXzaa7w2marzfufFeJOp98hKAQsTH5xYBUIibocoVeY0UdR9%2FFdKyV6ox1MbrCleJA%2FNqxFiUvn60bTaYbkZVOkLfEAq2tAk9f&X-Amz-Signature=70f9bf6c6a86eb5a1950263c3afb1a1c59a662713c3eaea9cbeb42d9a5ab2b79&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/1647f2c8-1cc0-45a2-af62-be9db8b7f2af/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJUT7ISX%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDtJyHDVwEuFPLVpZ%2FlwhdpDNOD%2FsazZ%2Fsfe1VDAY3RQIgN33JyFwVV%2FUCG3auMF5rqcM3tfoyHqYW%2FXC5cdtBsjcqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDADelR3MIWZzv%2FWs1ircA%2FeImJGgfNFoap98RTbu5%2BbiKJ9PXPVEbum41Gei83MoHu3nbjCLwW4b1ruWHk%2FnG6derYIiyy4q%2BePoIHJfeKSz4gWdMWdg2G6W1zChfGtsKQIm1%2FwdNEL83xvutkwfrulL4VhEiF4zM4nWQoiipTwSj2sWRULqBeKtfBwTbelNY3Ry0vsOLcy8%2FDtFU%2BogOw9Qg8Es2CDv9De00w2rPxMLqQ9Ty1RmkUJNucntymK%2BRpI77HlhXldPRqL8CiwD3OtFZvxxxQHkfJj%2F9rafzPe%2ByKzNPZ3Es0ifyMVCyqWaYsTrv0dyLp3U3j51H9fXAMZFvnSDTfrw8Yu%2BgeLLb67jExsdy%2BQzZ8FQ%2B0Xy9%2Bq2ChIFLSfrHZ9lVlCmEqx43T7xpquSEnwsDRy2W4wqyo8MllV7dI5JpfgZA6b0uzO2YOpoRwKiVYi%2BlpDdwtHQ42gJJsCz4QQ4XGn6iZa2XL1%2FcirgPoIMFKxVO1SJOoWE4bV6L765LGqyPQRF1Lrgxb5cMKWq%2BrlgFgMYw3mLeqvZFN4OS9uNQ6cpjRQJjsRLg8vigxF2RniWFLo8MucPzag%2Fj6%2BS4gfwimsms0IZdMVAfxci0FhVg%2BRXMhjHK7xQHZzJ6Tqnso2xD0WOMLbT4cQGOqUB5tcIME1X4DmGmohViSkmK%2B%2FNwGFjHe0oUCKdJ5%2FxnFfcRDC5DFFzi3l2ZSDsNWWsyH2s5vvlSBn0jmZzp8c%2BOdJId14LpB6gKTl21oQq9G4kfUob4aJiic%2F4BkuXzaa7w2marzfufFeJOp98hKAQsTH5xYBUIibocoVeY0UdR9%2FFdKyV6ox1MbrCleJA%2FNqxFiUvn60bTaYbkZVOkLfEAq2tAk9f&X-Amz-Signature=931da91e0c934596bbfc28b2f2b15a4a61ced370d034f3aea9b946db93c6fdcf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 3.3 Training Template

Search-R1을 학습시킬때 사용하는 prompt template

- 아래 template은 모델이 출력할 구조를 think → search → answer 순서로 명확히 나누도록 유도함

- 다만 특정 해결 방식이나 반영 수준을 강제하지 않아 모델이 RL 과정에서 자연스럽게 학습하도록 설계함 (구조적 형식만 따르게 제한함)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/351e2f14-e2bc-4d4b-b0e8-7bcec485137f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJUT7ISX%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDtJyHDVwEuFPLVpZ%2FlwhdpDNOD%2FsazZ%2Fsfe1VDAY3RQIgN33JyFwVV%2FUCG3auMF5rqcM3tfoyHqYW%2FXC5cdtBsjcqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDADelR3MIWZzv%2FWs1ircA%2FeImJGgfNFoap98RTbu5%2BbiKJ9PXPVEbum41Gei83MoHu3nbjCLwW4b1ruWHk%2FnG6derYIiyy4q%2BePoIHJfeKSz4gWdMWdg2G6W1zChfGtsKQIm1%2FwdNEL83xvutkwfrulL4VhEiF4zM4nWQoiipTwSj2sWRULqBeKtfBwTbelNY3Ry0vsOLcy8%2FDtFU%2BogOw9Qg8Es2CDv9De00w2rPxMLqQ9Ty1RmkUJNucntymK%2BRpI77HlhXldPRqL8CiwD3OtFZvxxxQHkfJj%2F9rafzPe%2ByKzNPZ3Es0ifyMVCyqWaYsTrv0dyLp3U3j51H9fXAMZFvnSDTfrw8Yu%2BgeLLb67jExsdy%2BQzZ8FQ%2B0Xy9%2Bq2ChIFLSfrHZ9lVlCmEqx43T7xpquSEnwsDRy2W4wqyo8MllV7dI5JpfgZA6b0uzO2YOpoRwKiVYi%2BlpDdwtHQ42gJJsCz4QQ4XGn6iZa2XL1%2FcirgPoIMFKxVO1SJOoWE4bV6L765LGqyPQRF1Lrgxb5cMKWq%2BrlgFgMYw3mLeqvZFN4OS9uNQ6cpjRQJjsRLg8vigxF2RniWFLo8MucPzag%2Fj6%2BS4gfwimsms0IZdMVAfxci0FhVg%2BRXMhjHK7xQHZzJ6Tqnso2xD0WOMLbT4cQGOqUB5tcIME1X4DmGmohViSkmK%2B%2FNwGFjHe0oUCKdJ5%2FxnFfcRDC5DFFzi3l2ZSDsNWWsyH2s5vvlSBn0jmZzp8c%2BOdJId14LpB6gKTl21oQq9G4kfUob4aJiic%2F4BkuXzaa7w2marzfufFeJOp98hKAQsTH5xYBUIibocoVeY0UdR9%2FFdKyV6ox1MbrCleJA%2FNqxFiUvn60bTaYbkZVOkLfEAq2tAk9f&X-Amz-Signature=a5c592a46f83344fae69f3ce2df5038dd7a59196b285d0de43319fbc1a40d89c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**Case Study**

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/3476ceb9-5137-47f6-ad70-44295420f9ba/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJUT7ISX%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDtJyHDVwEuFPLVpZ%2FlwhdpDNOD%2FsazZ%2Fsfe1VDAY3RQIgN33JyFwVV%2FUCG3auMF5rqcM3tfoyHqYW%2FXC5cdtBsjcqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDADelR3MIWZzv%2FWs1ircA%2FeImJGgfNFoap98RTbu5%2BbiKJ9PXPVEbum41Gei83MoHu3nbjCLwW4b1ruWHk%2FnG6derYIiyy4q%2BePoIHJfeKSz4gWdMWdg2G6W1zChfGtsKQIm1%2FwdNEL83xvutkwfrulL4VhEiF4zM4nWQoiipTwSj2sWRULqBeKtfBwTbelNY3Ry0vsOLcy8%2FDtFU%2BogOw9Qg8Es2CDv9De00w2rPxMLqQ9Ty1RmkUJNucntymK%2BRpI77HlhXldPRqL8CiwD3OtFZvxxxQHkfJj%2F9rafzPe%2ByKzNPZ3Es0ifyMVCyqWaYsTrv0dyLp3U3j51H9fXAMZFvnSDTfrw8Yu%2BgeLLb67jExsdy%2BQzZ8FQ%2B0Xy9%2Bq2ChIFLSfrHZ9lVlCmEqx43T7xpquSEnwsDRy2W4wqyo8MllV7dI5JpfgZA6b0uzO2YOpoRwKiVYi%2BlpDdwtHQ42gJJsCz4QQ4XGn6iZa2XL1%2FcirgPoIMFKxVO1SJOoWE4bV6L765LGqyPQRF1Lrgxb5cMKWq%2BrlgFgMYw3mLeqvZFN4OS9uNQ6cpjRQJjsRLg8vigxF2RniWFLo8MucPzag%2Fj6%2BS4gfwimsms0IZdMVAfxci0FhVg%2BRXMhjHK7xQHZzJ6Tqnso2xD0WOMLbT4cQGOqUB5tcIME1X4DmGmohViSkmK%2B%2FNwGFjHe0oUCKdJ5%2FxnFfcRDC5DFFzi3l2ZSDsNWWsyH2s5vvlSBn0jmZzp8c%2BOdJId14LpB6gKTl21oQq9G4kfUob4aJiic%2F4BkuXzaa7w2marzfufFeJOp98hKAQsTH5xYBUIibocoVeY0UdR9%2FFdKyV6ox1MbrCleJA%2FNqxFiUvn60bTaYbkZVOkLfEAq2tAk9f&X-Amz-Signature=9a1fbb15032d143fdbbea64d53425fb42bf267f23445b55897e01d494ebdb3e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 3.4 Reward Modeling

Search-R1은 outcome-based rule-based reward function을 사용함

- 예를 들어, factual reasoning task에서 정답과 모델의 출력이 일치하는지 exact match로 평가함

- 별도의 형식 보상이나 복잡한 과정 기반 보상은 사용하지 않고, 신경망 기반 보상 모델도 학습하지 않아 학습 복잡성을 줄임

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/c989f85c-f315-417c-9abd-8a2d86df00ba/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJUT7ISX%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDtJyHDVwEuFPLVpZ%2FlwhdpDNOD%2FsazZ%2Fsfe1VDAY3RQIgN33JyFwVV%2FUCG3auMF5rqcM3tfoyHqYW%2FXC5cdtBsjcqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDADelR3MIWZzv%2FWs1ircA%2FeImJGgfNFoap98RTbu5%2BbiKJ9PXPVEbum41Gei83MoHu3nbjCLwW4b1ruWHk%2FnG6derYIiyy4q%2BePoIHJfeKSz4gWdMWdg2G6W1zChfGtsKQIm1%2FwdNEL83xvutkwfrulL4VhEiF4zM4nWQoiipTwSj2sWRULqBeKtfBwTbelNY3Ry0vsOLcy8%2FDtFU%2BogOw9Qg8Es2CDv9De00w2rPxMLqQ9Ty1RmkUJNucntymK%2BRpI77HlhXldPRqL8CiwD3OtFZvxxxQHkfJj%2F9rafzPe%2ByKzNPZ3Es0ifyMVCyqWaYsTrv0dyLp3U3j51H9fXAMZFvnSDTfrw8Yu%2BgeLLb67jExsdy%2BQzZ8FQ%2B0Xy9%2Bq2ChIFLSfrHZ9lVlCmEqx43T7xpquSEnwsDRy2W4wqyo8MllV7dI5JpfgZA6b0uzO2YOpoRwKiVYi%2BlpDdwtHQ42gJJsCz4QQ4XGn6iZa2XL1%2FcirgPoIMFKxVO1SJOoWE4bV6L765LGqyPQRF1Lrgxb5cMKWq%2BrlgFgMYw3mLeqvZFN4OS9uNQ6cpjRQJjsRLg8vigxF2RniWFLo8MucPzag%2Fj6%2BS4gfwimsms0IZdMVAfxci0FhVg%2BRXMhjHK7xQHZzJ6Tqnso2xD0WOMLbT4cQGOqUB5tcIME1X4DmGmohViSkmK%2B%2FNwGFjHe0oUCKdJ5%2FxnFfcRDC5DFFzi3l2ZSDsNWWsyH2s5vvlSBn0jmZzp8c%2BOdJId14LpB6gKTl21oQq9G4kfUob4aJiic%2F4BkuXzaa7w2marzfufFeJOp98hKAQsTH5xYBUIibocoVeY0UdR9%2FFdKyV6ox1MbrCleJA%2FNqxFiUvn60bTaYbkZVOkLfEAq2tAk9f&X-Amz-Signature=ea44df374acee3bb17c4da1bdf415e2ac185073f255f21602f689cfb815db04e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# 4. Main Results

## 4.1 Datasets

1. General QA

1. Multi-Hop QA

## 4.2 Baselines
