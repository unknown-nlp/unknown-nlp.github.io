---
categories:
- paper-reviews
date: '2025-08-18 00:00:00'
description: 논문 리뷰
giscus_comments: true
layout: post
related_posts: false
slug: 2025-08-18-reasoning-models-can-be-effective-without-thinking
tags:
- language-model
- llm
- paper-review
- reasoning
title: Reasoning Models Can Be Effective Without Thinking
---

**논문 정보**
- **Date**: 2025-07-01

# 1. Introduction

LLM을 이용해 복잡한 문제를 풀 때, 보통 우리는 “긴 chains of thoughts”를 생성하고 그것을 이용해 reflection, backtracking, self-validation 등을 수행하곤 한다  (“Thinking”). 이러한 reasoning path는 일반적으로 reward를 이용한 강화학습, 혹은 distilled reasoning trace를 이용한 finetuning을 통해서 획득되며, 이 **explicit한 reasoning path가 실제로 성능에 많은 도움이 된다고 믿어져왔다**. 이 때문에 inference-time compute scaling이 주된 paradigm이기도.

하지만 저자들은 이에 대한 근본적인 질문을 던진다: 

- 정말로 explicit Thinking process가 상위 reasoning을 위해 필요한가?

그리고 저자들은 사실 정교한 reasoning path은 그닥 중요하지 않다는 사실을 다양한 실험을 통해서 증명한다. 

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/605b0506-a33c-4c16-8b0a-bbd8fae34e86/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-07-01_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_11.35.26.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYHVBZD3%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110000Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYU%2BBrmqTSgYh1fFMxDdmZKeHOIXdwzHqZ6oEbKaTqcgIhAPHbj9gx6GOWmE%2Fm3PfP6bvNCmRAVHQ%2BsHGkmHhpoHivKogECNP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2FcnCbF%2FBa4s6x0nIq3AOTfHMTWl6JF6AI8d%2Bh2fYFYEVm4LbaQ5DJwNpN4nhF8u%2BeheyOTMKYHMurLXZ%2BsztYrScyAVhkcTtxlZVi7l0MkNssMEcC2U2ex2IOfbHnZOKn6S2i5fP0uJhxlRe5NVo2VEoiBO5XMgHkxWgfLjQ5%2BqBOnSVcy%2BWLarCtq7CYSrs0DNv7O%2B0sgFQXMrfjpB6PU%2FZgwPuwgxLi6FTSq8uRQzyiLD%2Fs9uZc%2F7lKX87cKuuyf75EyBZQ3E6bJM%2B4HSECe%2F8mseh1zlFlDLPvnRILSOkXbYbI47T7%2BTkd0gZCTc47ba%2B2qKMbm1PSD1%2BJkrfhPxZeWHpkfsxkuEdPSBOlP%2FukRilx4u%2FlsZ1oCwHlI6nSvbZxOChD4EnEk9aUBdaxCgYj5Hv8gPmdW4b6PGcMoM7bWmwdcbaL8RMH0B7klRZJ4Z9m3ql15bQCfb7YHDxXrCcUISIgorm6r1j%2FUBwActO8n5dzb9xe%2BQvLPlsftqBNLcFcM1o1JpZ1elo5imofwjNRSVRO1cwHyHeTwp%2F1BBSzqx6zH%2BjX%2FrM7XYYl2TC0psQkXMaXkKqzBEZnhnmBsst%2BXd89codDEJ9POYJZeX8ClIaXHyybsylMhHgCOqEDYUS6x0wM2Ih79DC61OHEBjqkAVVBZ%2B97ccpNHn6tl53zK408ME%2BxjsMVli9aRTEDv4C1g2nvWcrdlB00%2Fxv4wq61%2BoEz9zl4Ilo0xqyFGIwjJe2hltqiRpCDAXYdvWpt9Lec%2B3xvpos9O%2FtsqodJwB7iptoa3S%2Fwe2i%2FSP6zsI9ushV5IDK5XMHWma42PEVK2UCqPe%2BEmDZPOVAri9WySCKAZte2ItIGZFjMwxEJVqw3lJrV8v73&X-Amz-Signature=4c49ce2fb8449d3526bc5e47c8a3fd439094131dcc795d03f34e7c2c3fa34045&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

저자들은  DeepSeek-R1-Distill-Qwen을 이용해서 Thinking과 이들이 사용하는 NoThinking — 응답에 가짜 Thinking 블록을 미리 채워 넣고, 모델이 그 이후부터 이어서 답변하도록 하는 방법 — 을 비교해보았을 때, 오히려 NoThinking이 훨씬 더 성능이 좋다는 것을 보인다 (pass@k metrics).

NoThinking은 2.0~5.1배 적은 토큰을 사용하면서도, k=1을 제외하고는 Thinking과 비슷하거나 더 좋은 성능을 보인다. 

또한, 두 접근법의 토큰 사용량을 동일하게 통제했을 때, NoThinking은 특히 low-budget 구간에서 pass@1가 Thinking보다 높았으며, k가 커질수록 성능 차이는 더 커졌다 (Figure 2). 

효율성을 체계적으로 평가하기 위해 pass@k와 평균 토큰 사용량 간의 Pareto frontier를 분석한 결과, NoThinking은 항상 Thinking보다 우수한 결과를 보였다. 이는 명시적인 추론 과정을 거치지 않더라도 NoThinking이  더 좋은 accuracy-cost tradeoffs를 가진다는 것을 의미한다. 

pass@k에서 NoThinking이 좋은 성능을 보였다는 것은, Thinking을 사용한 순차적 추론이 아닌, parallel scaling이 가능하다는 것이다. 저자들은 여러 응답을 병렬로 샘플링하고, best-of-N으로 최종 응답을 고르는 방법론을 제안한다.

이들이 고려한 task는 두 가지이다:

1. tasks with perfect verifiers (e.g., formal theorem proving): 자동으로 정답 여부를 확인할 수 있는 경우 

1. tasks without verifiers (e.g., general problem solving): simple confidence-based selection strategies를 사용해야하는 경우


verifiers가 있는 경우, NoThinking이 Thinking을 가뿐히 능가했다 ( both with and without parallel scaling). 특히, 지연 시간을 7배 단축하고 총 토큰 사용량을 4배나 줄였다는 점이 이점. 
verifiers가 없는 경우에도 NoThinking 준수한 성능을 보인다. 예를 들어,  Thinking을 9× lower latency + improved accuracy on OlympiadBench (Math)로 능가함. (Figure 3)

요약하자면, 이 연구는 현재의 추론 모델들이 학습 과정에서 구조화된 추론 형식을 따르도록 훈련되었음에도 불구하고, 높은 성능을 내기 위해 반드시 명시적인 thinking 과정이 필요하지 않다는 사실을 처음으로 보여주고 있다. 

또한, NoThinking 방식을 병렬로 처리하면, 순차적 추론보다 더 좋은 latency-accuracy tradeoffs가 가능함을 보인다. 

전반적으로, 이 연구는 긴 thinking 과정이 과연 정말로 필요한 것인가에 대한 의문에 대한 답을 일부분 보여주고 있다고 할 수 있다!

# 2. Related Work and Background

### Test-Time Scaling for Language Models 

- **Sequential approaches**

- **Parallel approaches**

- **NoThinking의 차별점**

### Efficient Reasoning

recent work has explored various strategies to make reasoning in LLMs more efficient. 

- **추론 시퀀스 길이 최적화**

- **강화 학습 기반 CoT 최적화**

- **Best-of-N 샘플링을 활용한 파인튜닝**

- **출력 방식 수정으로 reasoning 간결화**

- **학습 없는 전략적 기준 설정**

- **추론 단계 수 제한**

- **동적 입력 라우팅으로 reasoning 복잡성 제어**

# 3. NoThinking Provides Better Accuracy-budget Tradeoffs than Thinking

Section 3.1: define Thinking and NoThinking 

Section 3.2: describe experimental setup

Section 3.3: present experimental results 

Section 3.4: Discussions and Analyses

## 3.1 Method

대부분의 모델들은 보통 비슷한 구조로 generation을 한다: 

- reasoning process within the thinking box, marked by <|beginning of thinking|> and <|end of thinking|>, followed by the final answer. 

이 구조에 기반해서 Thinking and NoThinking을 다음과 같이 만듦:

- **Thinking: **the reasoning process within the thinking box, the final solution, and the final answer (Figure 1 (blue)).

- **NoThinking: ** explicit reasoning process 무시하고 바로 final solution and answer 만들기. 
thinking box를 decoding 할 때 빈칸으로 하도록 강제 (Figure 1 (orange)).

token usage를 제어하기 위해 budget forcing technique from Muennighoff et al. (2025)을 사용 — 모델이 token budget에 도달하면, 강제로 Final Answer 만들도록 함. 만약 아직 thinking box 안에 있었다면,  <|end of thinking|> 을 final answer tag 이전에 붙여서 만듬. 

## 3.2 Evaluation Setup

- **Models** 

- **Tasks and Benchmarks**

- **Metrics: **pass@k

## 3.3 Results

### Thinking vs. NoThinking vs. Qwen Instruct without token budget controlled

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/684a2c58-a6cb-4757-9fb3-ca345986e094/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-07-01_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_12.31.42.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYHVBZD3%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110000Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYU%2BBrmqTSgYh1fFMxDdmZKeHOIXdwzHqZ6oEbKaTqcgIhAPHbj9gx6GOWmE%2Fm3PfP6bvNCmRAVHQ%2BsHGkmHhpoHivKogECNP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2FcnCbF%2FBa4s6x0nIq3AOTfHMTWl6JF6AI8d%2Bh2fYFYEVm4LbaQ5DJwNpN4nhF8u%2BeheyOTMKYHMurLXZ%2BsztYrScyAVhkcTtxlZVi7l0MkNssMEcC2U2ex2IOfbHnZOKn6S2i5fP0uJhxlRe5NVo2VEoiBO5XMgHkxWgfLjQ5%2BqBOnSVcy%2BWLarCtq7CYSrs0DNv7O%2B0sgFQXMrfjpB6PU%2FZgwPuwgxLi6FTSq8uRQzyiLD%2Fs9uZc%2F7lKX87cKuuyf75EyBZQ3E6bJM%2B4HSECe%2F8mseh1zlFlDLPvnRILSOkXbYbI47T7%2BTkd0gZCTc47ba%2B2qKMbm1PSD1%2BJkrfhPxZeWHpkfsxkuEdPSBOlP%2FukRilx4u%2FlsZ1oCwHlI6nSvbZxOChD4EnEk9aUBdaxCgYj5Hv8gPmdW4b6PGcMoM7bWmwdcbaL8RMH0B7klRZJ4Z9m3ql15bQCfb7YHDxXrCcUISIgorm6r1j%2FUBwActO8n5dzb9xe%2BQvLPlsftqBNLcFcM1o1JpZ1elo5imofwjNRSVRO1cwHyHeTwp%2F1BBSzqx6zH%2BjX%2FrM7XYYl2TC0psQkXMaXkKqzBEZnhnmBsst%2BXd89codDEJ9POYJZeX8ClIaXHyybsylMhHgCOqEDYUS6x0wM2Ih79DC61OHEBjqkAVVBZ%2B97ccpNHn6tl53zK408ME%2BxjsMVli9aRTEDv4C1g2nvWcrdlB00%2Fxv4wq61%2BoEz9zl4Ilo0xqyFGIwjJe2hltqiRpCDAXYdvWpt9Lec%2B3xvpos9O%2FtsqodJwB7iptoa3S%2Fwe2i%2FSP6zsI9ushV5IDK5XMHWma42PEVK2UCqPe%2BEmDZPOVAri9WySCKAZte2ItIGZFjMwxEJVqw3lJrV8v73&X-Amz-Signature=a01b282823866739b693760b53a82435067d60614e6e55883fa8b5c821f4e78b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


budget forcing없이 세 경우를 비교한 결과:

- MiniF2F and ProofNet에서 NoThinking은 모든 K에 대해서 Thinking과 비슷했으며, 둘은 Qwen-Instruct보다 성능 훨씬 좋았음

- 다른 데이터셋에서는 k = 1일 때는 NoThinking의 성능이 훨씬 떨어지지만, k가 커질수록 갭이 작아짐

- 결과적으로, NoThinking은 가장 큰 k일때, 2.0–5.1x fewer tokens을 사용하는데도, Thinking의 성능을 넘거나 거의 근사함.

- Qwen-Instruct의 관점에서:

### Thinking vs. NoThinking with token budget controlled 

위에서 확인했듯,Thinking이 NoThinking보다 대부분의 데이터셋에서 성능이 더 좋음. 하지만, 결과적으로 Thinking이 더 많은 토큰을 사용하기 때문에 같은 토큰 수를 사용할 때 어떤 것이 더 성능이 좋은가를 비교함

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/1a27f577-a97d-48b1-ae01-c80422e0dd10/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-07-01_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_12.32.33.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYHVBZD3%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110000Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYU%2BBrmqTSgYh1fFMxDdmZKeHOIXdwzHqZ6oEbKaTqcgIhAPHbj9gx6GOWmE%2Fm3PfP6bvNCmRAVHQ%2BsHGkmHhpoHivKogECNP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2FcnCbF%2FBa4s6x0nIq3AOTfHMTWl6JF6AI8d%2Bh2fYFYEVm4LbaQ5DJwNpN4nhF8u%2BeheyOTMKYHMurLXZ%2BsztYrScyAVhkcTtxlZVi7l0MkNssMEcC2U2ex2IOfbHnZOKn6S2i5fP0uJhxlRe5NVo2VEoiBO5XMgHkxWgfLjQ5%2BqBOnSVcy%2BWLarCtq7CYSrs0DNv7O%2B0sgFQXMrfjpB6PU%2FZgwPuwgxLi6FTSq8uRQzyiLD%2Fs9uZc%2F7lKX87cKuuyf75EyBZQ3E6bJM%2B4HSECe%2F8mseh1zlFlDLPvnRILSOkXbYbI47T7%2BTkd0gZCTc47ba%2B2qKMbm1PSD1%2BJkrfhPxZeWHpkfsxkuEdPSBOlP%2FukRilx4u%2FlsZ1oCwHlI6nSvbZxOChD4EnEk9aUBdaxCgYj5Hv8gPmdW4b6PGcMoM7bWmwdcbaL8RMH0B7klRZJ4Z9m3ql15bQCfb7YHDxXrCcUISIgorm6r1j%2FUBwActO8n5dzb9xe%2BQvLPlsftqBNLcFcM1o1JpZ1elo5imofwjNRSVRO1cwHyHeTwp%2F1BBSzqx6zH%2BjX%2FrM7XYYl2TC0psQkXMaXkKqzBEZnhnmBsst%2BXd89codDEJ9POYJZeX8ClIaXHyybsylMhHgCOqEDYUS6x0wM2Ih79DC61OHEBjqkAVVBZ%2B97ccpNHn6tl53zK408ME%2BxjsMVli9aRTEDv4C1g2nvWcrdlB00%2Fxv4wq61%2BoEz9zl4Ilo0xqyFGIwjJe2hltqiRpCDAXYdvWpt9Lec%2B3xvpos9O%2FtsqodJwB7iptoa3S%2Fwe2i%2FSP6zsI9ushV5IDK5XMHWma42PEVK2UCqPe%2BEmDZPOVAri9WySCKAZte2ItIGZFjMwxEJVqw3lJrV8v73&X-Amz-Signature=427c26f876e95ab9ceb8ee704846a6b1e0d294ec615cde7797efb29d1007f221&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

결과적으로 NoThinking generally outperforms Thinking. 

특히, low-budget setting (e.g., fewer than ≈ 3, 000 tokens)에서 NoThinking은 모든 k에서 더 좋은 성능을 보였고, k가 커질수록 차이는 커졌음. 
좀 더 토큰 제한을 늘렸을 때 (e.g., around 3, 500 tokens), Thinking이 pass@1에서는 더 좋았으나, k = 2부터는 다시 NoThinking이 더 좋은 성능을 보임

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/ad227eca-5b01-41d5-8ca1-f4f5fdf9db83/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-07-01_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_12.33.12.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYHVBZD3%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110000Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYU%2BBrmqTSgYh1fFMxDdmZKeHOIXdwzHqZ6oEbKaTqcgIhAPHbj9gx6GOWmE%2Fm3PfP6bvNCmRAVHQ%2BsHGkmHhpoHivKogECNP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2FcnCbF%2FBa4s6x0nIq3AOTfHMTWl6JF6AI8d%2Bh2fYFYEVm4LbaQ5DJwNpN4nhF8u%2BeheyOTMKYHMurLXZ%2BsztYrScyAVhkcTtxlZVi7l0MkNssMEcC2U2ex2IOfbHnZOKn6S2i5fP0uJhxlRe5NVo2VEoiBO5XMgHkxWgfLjQ5%2BqBOnSVcy%2BWLarCtq7CYSrs0DNv7O%2B0sgFQXMrfjpB6PU%2FZgwPuwgxLi6FTSq8uRQzyiLD%2Fs9uZc%2F7lKX87cKuuyf75EyBZQ3E6bJM%2B4HSECe%2F8mseh1zlFlDLPvnRILSOkXbYbI47T7%2BTkd0gZCTc47ba%2B2qKMbm1PSD1%2BJkrfhPxZeWHpkfsxkuEdPSBOlP%2FukRilx4u%2FlsZ1oCwHlI6nSvbZxOChD4EnEk9aUBdaxCgYj5Hv8gPmdW4b6PGcMoM7bWmwdcbaL8RMH0B7klRZJ4Z9m3ql15bQCfb7YHDxXrCcUISIgorm6r1j%2FUBwActO8n5dzb9xe%2BQvLPlsftqBNLcFcM1o1JpZ1elo5imofwjNRSVRO1cwHyHeTwp%2F1BBSzqx6zH%2BjX%2FrM7XYYl2TC0psQkXMaXkKqzBEZnhnmBsst%2BXd89codDEJ9POYJZeX8ClIaXHyybsylMhHgCOqEDYUS6x0wM2Ih79DC61OHEBjqkAVVBZ%2B97ccpNHn6tl53zK408ME%2BxjsMVli9aRTEDv4C1g2nvWcrdlB00%2Fxv4wq61%2BoEz9zl4Ilo0xqyFGIwjJe2hltqiRpCDAXYdvWpt9Lec%2B3xvpos9O%2FtsqodJwB7iptoa3S%2Fwe2i%2FSP6zsI9ushV5IDK5XMHWma42PEVK2UCqPe%2BEmDZPOVAri9WySCKAZte2ItIGZFjMwxEJVqw3lJrV8v73&X-Amz-Signature=bc453697eb5725768067d22a6e8fd6ed343f96162ae7e6f3723bf4fc516a549b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Figure 6는 해당 데이터셋에서 사용한 가장 큰 k와 1, 그리고 token usage를 plot하면서 위의 결과를 더 잘 보여줌. 

- pass@k

- pass@1

[요약] 

- reasoning models의 핵심인 thinking box를 없애도, 여전히 효과 좋음

- 3.3–3.7x 적은 토큰을 사용하는데도 비슷한 성능 나옴

- 비슷한 수의 토큰이라면 thinking보다 성능 좋음


## 3.4 Discussions and Analyses

### Task-Specific Differences in NoThinking Performance 

Section 3.3에서 나름 일관적인 트렌드가 보이긴 하지만, 각 벤치마크 결과를 자세히 살펴보면 조금 동작이 다름

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/684a2c58-a6cb-4757-9fb3-ca345986e094/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-07-01_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_12.31.42.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYHVBZD3%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110001Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYU%2BBrmqTSgYh1fFMxDdmZKeHOIXdwzHqZ6oEbKaTqcgIhAPHbj9gx6GOWmE%2Fm3PfP6bvNCmRAVHQ%2BsHGkmHhpoHivKogECNP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2FcnCbF%2FBa4s6x0nIq3AOTfHMTWl6JF6AI8d%2Bh2fYFYEVm4LbaQ5DJwNpN4nhF8u%2BeheyOTMKYHMurLXZ%2BsztYrScyAVhkcTtxlZVi7l0MkNssMEcC2U2ex2IOfbHnZOKn6S2i5fP0uJhxlRe5NVo2VEoiBO5XMgHkxWgfLjQ5%2BqBOnSVcy%2BWLarCtq7CYSrs0DNv7O%2B0sgFQXMrfjpB6PU%2FZgwPuwgxLi6FTSq8uRQzyiLD%2Fs9uZc%2F7lKX87cKuuyf75EyBZQ3E6bJM%2B4HSECe%2F8mseh1zlFlDLPvnRILSOkXbYbI47T7%2BTkd0gZCTc47ba%2B2qKMbm1PSD1%2BJkrfhPxZeWHpkfsxkuEdPSBOlP%2FukRilx4u%2FlsZ1oCwHlI6nSvbZxOChD4EnEk9aUBdaxCgYj5Hv8gPmdW4b6PGcMoM7bWmwdcbaL8RMH0B7klRZJ4Z9m3ql15bQCfb7YHDxXrCcUISIgorm6r1j%2FUBwActO8n5dzb9xe%2BQvLPlsftqBNLcFcM1o1JpZ1elo5imofwjNRSVRO1cwHyHeTwp%2F1BBSzqx6zH%2BjX%2FrM7XYYl2TC0psQkXMaXkKqzBEZnhnmBsst%2BXd89codDEJ9POYJZeX8ClIaXHyybsylMhHgCOqEDYUS6x0wM2Ih79DC61OHEBjqkAVVBZ%2B97ccpNHn6tl53zK408ME%2BxjsMVli9aRTEDv4C1g2nvWcrdlB00%2Fxv4wq61%2BoEz9zl4Ilo0xqyFGIwjJe2hltqiRpCDAXYdvWpt9Lec%2B3xvpos9O%2FtsqodJwB7iptoa3S%2Fwe2i%2FSP6zsI9ushV5IDK5XMHWma42PEVK2UCqPe%2BEmDZPOVAri9WySCKAZte2ItIGZFjMwxEJVqw3lJrV8v73&X-Amz-Signature=a1135255af29924b89d57829c193262f8e9eeb42e3e9dfa354ec74d42e3f48a1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

In Figure 4, 

- AMC 2023는 모든 세팅에서 거의 performance gap없이 convergence를 보임. 아마도 saturation이 예상됨 

- MiniF2F and ProofNet pass@1에서 NoThinking은 Thinking에 비해 훨씬 더 적은 토큰을 사용하면서 비슷한 성능을 냄. 하지만, 이는 단순히 task simplicity 이슈로 해석되면 안됨! 검증 결과, OpenAI’s o1과 같은 엄청 강한 모델은 MiniF2F에서  30% accuracy 밖에 안됐고,  ProofNet은 모든 방법론에서 성능 낮았음. 즉, 왜 어떤 벤치마크에서는 NoThinking이 잘되었는가는 open question for future work이라는 것 

### How Increasing k Affects NoThinking Performance 

왜 k가 늘어날수록 NoThinking이 더 좋은 성능을 보이는지 대략적인 이유를 찾아보기 위해 생성된 답변의 diversity를 측정함 — by computing the entropy of the answer distribution for each question.

높은 mean entropy는 당연히  더 높은 overall diversity를 의미하고,  lower standard deviation은 더 일관적인 것을 의미. 실험은 token budget이 제한된 환경에서 진행

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/d5f633b1-01d1-4acb-ba42-6df5d5453f3d/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-07-01_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_12.35.20.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYHVBZD3%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110000Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYU%2BBrmqTSgYh1fFMxDdmZKeHOIXdwzHqZ6oEbKaTqcgIhAPHbj9gx6GOWmE%2Fm3PfP6bvNCmRAVHQ%2BsHGkmHhpoHivKogECNP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2FcnCbF%2FBa4s6x0nIq3AOTfHMTWl6JF6AI8d%2Bh2fYFYEVm4LbaQ5DJwNpN4nhF8u%2BeheyOTMKYHMurLXZ%2BsztYrScyAVhkcTtxlZVi7l0MkNssMEcC2U2ex2IOfbHnZOKn6S2i5fP0uJhxlRe5NVo2VEoiBO5XMgHkxWgfLjQ5%2BqBOnSVcy%2BWLarCtq7CYSrs0DNv7O%2B0sgFQXMrfjpB6PU%2FZgwPuwgxLi6FTSq8uRQzyiLD%2Fs9uZc%2F7lKX87cKuuyf75EyBZQ3E6bJM%2B4HSECe%2F8mseh1zlFlDLPvnRILSOkXbYbI47T7%2BTkd0gZCTc47ba%2B2qKMbm1PSD1%2BJkrfhPxZeWHpkfsxkuEdPSBOlP%2FukRilx4u%2FlsZ1oCwHlI6nSvbZxOChD4EnEk9aUBdaxCgYj5Hv8gPmdW4b6PGcMoM7bWmwdcbaL8RMH0B7klRZJ4Z9m3ql15bQCfb7YHDxXrCcUISIgorm6r1j%2FUBwActO8n5dzb9xe%2BQvLPlsftqBNLcFcM1o1JpZ1elo5imofwjNRSVRO1cwHyHeTwp%2F1BBSzqx6zH%2BjX%2FrM7XYYl2TC0psQkXMaXkKqzBEZnhnmBsst%2BXd89codDEJ9POYJZeX8ClIaXHyybsylMhHgCOqEDYUS6x0wM2Ih79DC61OHEBjqkAVVBZ%2B97ccpNHn6tl53zK408ME%2BxjsMVli9aRTEDv4C1g2nvWcrdlB00%2Fxv4wq61%2BoEz9zl4Ilo0xqyFGIwjJe2hltqiRpCDAXYdvWpt9Lec%2B3xvpos9O%2FtsqodJwB7iptoa3S%2Fwe2i%2FSP6zsI9ushV5IDK5XMHWma42PEVK2UCqPe%2BEmDZPOVAri9WySCKAZte2ItIGZFjMwxEJVqw3lJrV8v73&X-Amz-Signature=e5bb8bd6096b5a2021b6fb4321f3e8992d05a43a7d5073dbcf242690a70fbdf6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 엔트로피의 관점에서는 특별한 차이를 찾지 못함. 어떨 땐 NoThinking이 어떨 땐  Thinking이 더 높음

- variance의 관점에서 NoThinking은 항상 더 낮은 값을 보임 — 
더 uniform하게 답을 내고 있다는 것. 
