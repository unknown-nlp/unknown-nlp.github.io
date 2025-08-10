---
categories:
- paper-reviews
date: '2025-08-13 00:00:00'
description: 논문 리뷰 - LM 관련 연구
giscus_comments: true
layout: post
related_posts: false
slug: 2025-08-13-inferring-from-logits-exploring-best-practices-for-decoding
tags:
- embedding
- gpt
- llm
- lm
- paper-review
- reasoning
title: 'Inferring from Logits: Exploring Best Practices for Decoding-Free Generative
  Candidate Selection'
---

**논문 정보**
- **Date**: 2025-01-02
- **Reviewer**: 조영재
- **Property**: LM

Evaluation을 할때 많은 벤치 데이터셋들은 multiple choice 형태를 갖추고 있음. 근데 아직까지 작은 모델들은 instruction following이 잘 안돼서 파싱도 맞춰줘야 하고 프롬프트도 모델에 맞게 수정해야함. 혹은 모델의 답변을 gpt 사용해서 다시 mapping 시켜줘야함. → 모델에 따라 다른 프롬프트를 사용하는게 불공평 한 것 아닌가? 모두를 통합할 수 있는 방법은 없을까? logit을 이용해 무조건 mapping 시킬 수는 없을까? 

uncertainty가 조금 문제가 될수도…? 또, A라는 대답이 아니라 As, An apple 등등 A 로 시작하는 단어를 말하려던 것일수도 있겠다..   실제 model의 답변이 첫 token step의 logit과 상관관계가 있을까? logit을 이용해 측정을 하는게 편하긴 할텐데 의미가 있을까? 어쨌든 유저가 보게 되는 것은 text인데 어떻게든 text output 형태를 고수해야 하는가? 이 eval 방식은 cot를 간과하는 것이려나?

## 1. Introduction

- **Motivation**: While LLMs typically rely on autoregressive decoding (token-by-token generation), many real-world tasks involve selecting an answer from a **candidate pool**—such as multiple-choice QA or clinical decision-making.

- **Problem**: Full decoding is slow and breaks gradient flow; thus, **decoding-free** methods are increasingly used (i.e., using initial logits only).

- **Contribution**:

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/57d2595d-2c34-4dd5-8b2a-03b81e5a4775/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6BIRTW2%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDvDyEvct6lch2Jf2s71YpuuHEWXatf9RwWs4TmTNiSVAiAlnOBgVw2MIJrxdBhX4vTZ2PiAbGtLj61n6%2FQv5HNvtSqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZaCFi9OrYnbTfY3IKtwD3uTlilIPFaR%2FWfehhZjwSgyXZvtManXbkbYATIkwQMEQz%2BmCC%2FnhY4pwcAqyypZXw4YNjgZuCqKUCMMrf%2Fj6yWsljaNvxIP2J7wKVW%2Byx5jCQpJSJnwQcHYxrxajnWAbewVW6LtNVNCPmkScFepl1oZotKSrQMDSCCE3ue1rAS3YZTW1vtPQIs7kWOuY1%2Fk%2F024%2BkO1N%2BPbGqCYUFDGqGsJjf41GksAjrG68s1y5iO4%2FCvTbLIri%2BjkCsTBSmD9usRkVK5IW1yY0OF336Jw91%2B4%2FFs12EtKAbELxdgRXJMXUyh8nIcFJWNEMOQxe4TkjZk%2BTT10CTeP9dshZtKzQ3I3SGZ4M2coM0elaCucTQ5VPkQVVX8gcPOu0iJQ%2FfLPwMPWqvZfkjfr4jOMjPjPGXbwXWwTlJU%2FwP7PZXPRV%2FNaU%2Fs2yEuTlEG44N9Ona%2BObpmdRohSno0p2wRUZas7aIkX366SeDglTWkc0zmkTIMc5mydtg1Z5qIqKyvun1kRn4iMhe11EoPrOmFBpTtNHrgJecR%2BtBh4Q%2FQAeQ3y0HdnT23vekbnGbYsTQp0afwxx4AArznypfG6PvkGYJiUx2jm41h%2FCdLGhZ%2FXvr8zbFl7oHxhnHSbgt2TAYbMwvdThxAY6pgH0%2FuNgMcMuz9oj50MwciKF4Z7sRQkTgRVHMH6TCKZ3OtYAl%2BLuoN2%2BjKIu%2Bvc%2Bh%2Bo1g%2Fcd9zaxINko%2BY9xsIzTq7WbxDc33Buraq7zgd13bq7pJVw70MEc6inn4SMyhIMhVEafib47l37%2B%2FCMwERjIKE5OUcaiWw6Nm5lvsWKYJJdUs79PCZqYRDA3a0yLY%2BGj5fEovpsoeAZkJChheT4VfqOzXykq&X-Amz-Signature=83353323869bac8b02e968586f533cbae96d6b100f05dffeae4eb6ef4e07d58c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 2. Problem Formulation

### 2.1 Generative LMs

- traditional full decoding

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/f0792e36-49ad-4416-a3b5-3d45a3b5d172/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6BIRTW2%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDvDyEvct6lch2Jf2s71YpuuHEWXatf9RwWs4TmTNiSVAiAlnOBgVw2MIJrxdBhX4vTZ2PiAbGtLj61n6%2FQv5HNvtSqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZaCFi9OrYnbTfY3IKtwD3uTlilIPFaR%2FWfehhZjwSgyXZvtManXbkbYATIkwQMEQz%2BmCC%2FnhY4pwcAqyypZXw4YNjgZuCqKUCMMrf%2Fj6yWsljaNvxIP2J7wKVW%2Byx5jCQpJSJnwQcHYxrxajnWAbewVW6LtNVNCPmkScFepl1oZotKSrQMDSCCE3ue1rAS3YZTW1vtPQIs7kWOuY1%2Fk%2F024%2BkO1N%2BPbGqCYUFDGqGsJjf41GksAjrG68s1y5iO4%2FCvTbLIri%2BjkCsTBSmD9usRkVK5IW1yY0OF336Jw91%2B4%2FFs12EtKAbELxdgRXJMXUyh8nIcFJWNEMOQxe4TkjZk%2BTT10CTeP9dshZtKzQ3I3SGZ4M2coM0elaCucTQ5VPkQVVX8gcPOu0iJQ%2FfLPwMPWqvZfkjfr4jOMjPjPGXbwXWwTlJU%2FwP7PZXPRV%2FNaU%2Fs2yEuTlEG44N9Ona%2BObpmdRohSno0p2wRUZas7aIkX366SeDglTWkc0zmkTIMc5mydtg1Z5qIqKyvun1kRn4iMhe11EoPrOmFBpTtNHrgJecR%2BtBh4Q%2FQAeQ3y0HdnT23vekbnGbYsTQp0afwxx4AArznypfG6PvkGYJiUx2jm41h%2FCdLGhZ%2FXvr8zbFl7oHxhnHSbgt2TAYbMwvdThxAY6pgH0%2FuNgMcMuz9oj50MwciKF4Z7sRQkTgRVHMH6TCKZ3OtYAl%2BLuoN2%2BjKIu%2Bvc%2Bh%2Bo1g%2Fcd9zaxINko%2BY9xsIzTq7WbxDc33Buraq7zgd13bq7pJVw70MEc6inn4SMyhIMhVEafib47l37%2B%2FCMwERjIKE5OUcaiWw6Nm5lvsWKYJJdUs79PCZqYRDA3a0yLY%2BGj5fEovpsoeAZkJChheT4VfqOzXykq&X-Amz-Signature=91f5fb4dea0b158186a79d01e1a3e820e75926c02dd273cf938973697fefdd78&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- full decoding with Cand. Selection

### 2.4 Decoding-Free Generative Candidate Selection

- Goal: Estimate the **candidate probabilities** directly from the **first-step logits** without generating tokens.

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/84ee718f-6c65-4462-bf5a-fe8d85614b0b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6BIRTW2%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDvDyEvct6lch2Jf2s71YpuuHEWXatf9RwWs4TmTNiSVAiAlnOBgVw2MIJrxdBhX4vTZ2PiAbGtLj61n6%2FQv5HNvtSqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZaCFi9OrYnbTfY3IKtwD3uTlilIPFaR%2FWfehhZjwSgyXZvtManXbkbYATIkwQMEQz%2BmCC%2FnhY4pwcAqyypZXw4YNjgZuCqKUCMMrf%2Fj6yWsljaNvxIP2J7wKVW%2Byx5jCQpJSJnwQcHYxrxajnWAbewVW6LtNVNCPmkScFepl1oZotKSrQMDSCCE3ue1rAS3YZTW1vtPQIs7kWOuY1%2Fk%2F024%2BkO1N%2BPbGqCYUFDGqGsJjf41GksAjrG68s1y5iO4%2FCvTbLIri%2BjkCsTBSmD9usRkVK5IW1yY0OF336Jw91%2B4%2FFs12EtKAbELxdgRXJMXUyh8nIcFJWNEMOQxe4TkjZk%2BTT10CTeP9dshZtKzQ3I3SGZ4M2coM0elaCucTQ5VPkQVVX8gcPOu0iJQ%2FfLPwMPWqvZfkjfr4jOMjPjPGXbwXWwTlJU%2FwP7PZXPRV%2FNaU%2Fs2yEuTlEG44N9Ona%2BObpmdRohSno0p2wRUZas7aIkX366SeDglTWkc0zmkTIMc5mydtg1Z5qIqKyvun1kRn4iMhe11EoPrOmFBpTtNHrgJecR%2BtBh4Q%2FQAeQ3y0HdnT23vekbnGbYsTQp0afwxx4AArznypfG6PvkGYJiUx2jm41h%2FCdLGhZ%2FXvr8zbFl7oHxhnHSbgt2TAYbMwvdThxAY6pgH0%2FuNgMcMuz9oj50MwciKF4Z7sRQkTgRVHMH6TCKZ3OtYAl%2BLuoN2%2BjKIu%2Bvc%2Bh%2Bo1g%2Fcd9zaxINko%2BY9xsIzTq7WbxDc33Buraq7zgd13bq7pJVw70MEc6inn4SMyhIMhVEafib47l37%2B%2FCMwERjIKE5OUcaiWw6Nm5lvsWKYJJdUs79PCZqYRDA3a0yLY%2BGj5fEovpsoeAZkJChheT4VfqOzXykq&X-Amz-Signature=d89fbe7a3d909326836baf44934843ed44e4adfc675607851fcfc2cb7cde819b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Uses only the raw logits and candidate token representations.
             

## 3. Candidate Selection Methods

### 3.1 Estimation via Logits

- **First-token logit**: Use logits of first token in candidate

- **Last-token logit**

- **Average logits**: Mean over all candidate token logits

- **Sum logits**: Sum over all candidate token logits

- **Sample Avg.**: Average logits of sampled tokens (used for long candidates)

logits of k-th token(4)                  Averaged token logits (5)          Sum of token logits (6) 

### 3.2 Baselines

- **Full decoding**: Followed by mapping output to candidate

- **Dense retrieval**: Facebook DPR embeddings with cosine similarity

##  4. Evaluation Settings

### 4.1 Tasks

- **Limited-candidate tasks (3–5 options)**:

- **Massive-candidate tasks (1K–94K options)**:

### 4.2 Base LMs

- Decoder-only: LLaMA3 (8B), Mistral (7.3B)

- Encoder-decoder: Flan-T5 XL (11B)

- Variants with and without **instruction tuning** used

##  5. Experimental Results

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/591b8204-0b09-4ad8-be21-3d5164545c5b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6BIRTW2%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDvDyEvct6lch2Jf2s71YpuuHEWXatf9RwWs4TmTNiSVAiAlnOBgVw2MIJrxdBhX4vTZ2PiAbGtLj61n6%2FQv5HNvtSqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZaCFi9OrYnbTfY3IKtwD3uTlilIPFaR%2FWfehhZjwSgyXZvtManXbkbYATIkwQMEQz%2BmCC%2FnhY4pwcAqyypZXw4YNjgZuCqKUCMMrf%2Fj6yWsljaNvxIP2J7wKVW%2Byx5jCQpJSJnwQcHYxrxajnWAbewVW6LtNVNCPmkScFepl1oZotKSrQMDSCCE3ue1rAS3YZTW1vtPQIs7kWOuY1%2Fk%2F024%2BkO1N%2BPbGqCYUFDGqGsJjf41GksAjrG68s1y5iO4%2FCvTbLIri%2BjkCsTBSmD9usRkVK5IW1yY0OF336Jw91%2B4%2FFs12EtKAbELxdgRXJMXUyh8nIcFJWNEMOQxe4TkjZk%2BTT10CTeP9dshZtKzQ3I3SGZ4M2coM0elaCucTQ5VPkQVVX8gcPOu0iJQ%2FfLPwMPWqvZfkjfr4jOMjPjPGXbwXWwTlJU%2FwP7PZXPRV%2FNaU%2Fs2yEuTlEG44N9Ona%2BObpmdRohSno0p2wRUZas7aIkX366SeDglTWkc0zmkTIMc5mydtg1Z5qIqKyvun1kRn4iMhe11EoPrOmFBpTtNHrgJecR%2BtBh4Q%2FQAeQ3y0HdnT23vekbnGbYsTQp0afwxx4AArznypfG6PvkGYJiUx2jm41h%2FCdLGhZ%2FXvr8zbFl7oHxhnHSbgt2TAYbMwvdThxAY6pgH0%2FuNgMcMuz9oj50MwciKF4Z7sRQkTgRVHMH6TCKZ3OtYAl%2BLuoN2%2BjKIu%2Bvc%2Bh%2Bo1g%2Fcd9zaxINko%2BY9xsIzTq7WbxDc33Buraq7zgd13bq7pJVw70MEc6inn4SMyhIMhVEafib47l37%2B%2FCMwERjIKE5OUcaiWw6Nm5lvsWKYJJdUs79PCZqYRDA3a0yLY%2BGj5fEovpsoeAZkJChheT4VfqOzXykq&X-Amz-Signature=dddc0cefd7f4dfdd22231fa725b796fa820847fdd41b6997bbf1734fe58636da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Key Insights

- **Insight 1**: Estimation methods are strong when full decoding fails (e.g., weak models or hard tasks like GPQA)

- **Insight 2**: When full decoding works well, estimation methods fall short

- **Insight 3**: Instruction tuning helps full decoding but not decoding-free estimation

- **Insight 4**: Method effectiveness varies with model and dataset

- **Insight 5**: Decoding-free estimation is far more efficient (up to 57.6× speedup)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/5c2e05b8-3832-4538-a9e1-deb80d42160d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6BIRTW2%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDvDyEvct6lch2Jf2s71YpuuHEWXatf9RwWs4TmTNiSVAiAlnOBgVw2MIJrxdBhX4vTZ2PiAbGtLj61n6%2FQv5HNvtSqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZaCFi9OrYnbTfY3IKtwD3uTlilIPFaR%2FWfehhZjwSgyXZvtManXbkbYATIkwQMEQz%2BmCC%2FnhY4pwcAqyypZXw4YNjgZuCqKUCMMrf%2Fj6yWsljaNvxIP2J7wKVW%2Byx5jCQpJSJnwQcHYxrxajnWAbewVW6LtNVNCPmkScFepl1oZotKSrQMDSCCE3ue1rAS3YZTW1vtPQIs7kWOuY1%2Fk%2F024%2BkO1N%2BPbGqCYUFDGqGsJjf41GksAjrG68s1y5iO4%2FCvTbLIri%2BjkCsTBSmD9usRkVK5IW1yY0OF336Jw91%2B4%2FFs12EtKAbELxdgRXJMXUyh8nIcFJWNEMOQxe4TkjZk%2BTT10CTeP9dshZtKzQ3I3SGZ4M2coM0elaCucTQ5VPkQVVX8gcPOu0iJQ%2FfLPwMPWqvZfkjfr4jOMjPjPGXbwXWwTlJU%2FwP7PZXPRV%2FNaU%2Fs2yEuTlEG44N9Ona%2BObpmdRohSno0p2wRUZas7aIkX366SeDglTWkc0zmkTIMc5mydtg1Z5qIqKyvun1kRn4iMhe11EoPrOmFBpTtNHrgJecR%2BtBh4Q%2FQAeQ3y0HdnT23vekbnGbYsTQp0afwxx4AArznypfG6PvkGYJiUx2jm41h%2FCdLGhZ%2FXvr8zbFl7oHxhnHSbgt2TAYbMwvdThxAY6pgH0%2FuNgMcMuz9oj50MwciKF4Z7sRQkTgRVHMH6TCKZ3OtYAl%2BLuoN2%2BjKIu%2Bvc%2Bh%2Bo1g%2Fcd9zaxINko%2BY9xsIzTq7WbxDc33Buraq7zgd13bq7pJVw70MEc6inn4SMyhIMhVEafib47l37%2B%2FCMwERjIKE5OUcaiWw6Nm5lvsWKYJJdUs79PCZqYRDA3a0yLY%2BGj5fEovpsoeAZkJChheT4VfqOzXykq&X-Amz-Signature=d2c8f56cc3bd3f5e7e4b6fb7301aa786a2b03e9a1a1f7056c829be83fb696e8e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Detailed Analyses

- **5.2 Output step**: (a)

- **5.3 Candidate token selection**: (b)

- **5.4 Sensitivity**:

##  6. Related Work

- Classification-based methods require retraining and don’t generalize to dynamic candidates.

- Retrieval models struggle with reasoning tasks.

- This is the **first systematic evaluation** of decoding-free methods.

##  7. Conclusion & Future Work

- **Main findings**:

- **Future directions**:

### Appendix

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/e81a494c-5b19-493c-b78d-b5c8c22aa801/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6BIRTW2%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105952Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDvDyEvct6lch2Jf2s71YpuuHEWXatf9RwWs4TmTNiSVAiAlnOBgVw2MIJrxdBhX4vTZ2PiAbGtLj61n6%2FQv5HNvtSqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZaCFi9OrYnbTfY3IKtwD3uTlilIPFaR%2FWfehhZjwSgyXZvtManXbkbYATIkwQMEQz%2BmCC%2FnhY4pwcAqyypZXw4YNjgZuCqKUCMMrf%2Fj6yWsljaNvxIP2J7wKVW%2Byx5jCQpJSJnwQcHYxrxajnWAbewVW6LtNVNCPmkScFepl1oZotKSrQMDSCCE3ue1rAS3YZTW1vtPQIs7kWOuY1%2Fk%2F024%2BkO1N%2BPbGqCYUFDGqGsJjf41GksAjrG68s1y5iO4%2FCvTbLIri%2BjkCsTBSmD9usRkVK5IW1yY0OF336Jw91%2B4%2FFs12EtKAbELxdgRXJMXUyh8nIcFJWNEMOQxe4TkjZk%2BTT10CTeP9dshZtKzQ3I3SGZ4M2coM0elaCucTQ5VPkQVVX8gcPOu0iJQ%2FfLPwMPWqvZfkjfr4jOMjPjPGXbwXWwTlJU%2FwP7PZXPRV%2FNaU%2Fs2yEuTlEG44N9Ona%2BObpmdRohSno0p2wRUZas7aIkX366SeDglTWkc0zmkTIMc5mydtg1Z5qIqKyvun1kRn4iMhe11EoPrOmFBpTtNHrgJecR%2BtBh4Q%2FQAeQ3y0HdnT23vekbnGbYsTQp0afwxx4AArznypfG6PvkGYJiUx2jm41h%2FCdLGhZ%2FXvr8zbFl7oHxhnHSbgt2TAYbMwvdThxAY6pgH0%2FuNgMcMuz9oj50MwciKF4Z7sRQkTgRVHMH6TCKZ3OtYAl%2BLuoN2%2BjKIu%2Bvc%2Bh%2Bo1g%2Fcd9zaxINko%2BY9xsIzTq7WbxDc33Buraq7zgd13bq7pJVw70MEc6inn4SMyhIMhVEafib47l37%2B%2FCMwERjIKE5OUcaiWw6Nm5lvsWKYJJdUs79PCZqYRDA3a0yLY%2BGj5fEovpsoeAZkJChheT4VfqOzXykq&X-Amz-Signature=cf6bf43f3242387d7762386736a4fc15cd13c6c0165701069f40f500afa078a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

full decoding 성능 대비 logit estimation (with cot and without cot) MMLU 수학 성능표.
