---
categories:
  - paper-reviews
date: "2025-07-15 00:00:00"
description: 논문 리뷰
giscus_comments: true
layout: post
related_posts: false
tags:
  - attention
  - llm
  - paper-review
  - reasoning
thumbnail: assets/img/posts/2025-07-15-scaling-reasoning-losing-control-evaluating-instruction-following-in/thumbnail.jpg
title: "Scaling Reasoning, Losing Control: Evaluating Instruction Following in Large
  Reasoning Models"
---

**논문 정보**

- **Date**: 2025-07-15
- **Reviewer**: 전민진

## Abstract

- 최근의 reasoning oriented model(LRM)은 여러 수학 데이터셋에서 높은 성능 달성을 보이나, natural instruction following에 대한 성능은 분석되지 않음

- 본 논문에서는 이러한 LRM들의 instruction following 능력을 분석하기 위해 MathIF라는 데이터셋을 제안, math 도메인에서의 instruction following 성능을 평가

- 실험 결과, reasoning을 효과적으로 하는 모델이 user direction에 따르는 것을 어려워 하는 현상 발견

## Introduction

- CoT reasoning을 scaling하는 것은 reasoning ability를 향상시킴

- LRM의 경우 간단한 instruction도 following하는 것을 어려워 한다는 것을 발견

⇒ reasoning-oriented learning을 하면 모델 자체의 reasoning ability는 향상돼도 controllability는 떨어지는게 아닐까?

- 하지만 현재는 범용 목적의 instruction following(IF) 벤치마크만 존재

⇒ 수학 도메인에서의 IF 벤치마크를 만들고 평가해보자!

- 실험 결과, instruction following과 reasoning capability사이의 일종의 trade-off가 존재

- contribution

## Related Work

- LRM

- Instruction-followiwng benchmark

## MathIF

- Overview

- Constraint type

- Compositional Constraint

- Math problem collection

- Evaluation metric

## Experiment

- 모든 LRM은 nucleus sampling(T=1.0, p=0.95)로 디코딩, 최대 답변 길이 16,384 토큰, vLLM 사용

{% include figure.liquid loading="eager" path="assets/img/posts/2025-07-15-scaling-reasoning-losing-control-evaluating-instruction-following-in/image_000.png" class="img-fluid rounded z-depth-1" %}

- 모든 LRM은 IF성능이 하락함

- Qwen3 시리즈가 그나마 높은 IF 성능을 보임

- 모델 크기가 IF 성능을 결정하진 않음

- 명시적인 reasoning seperation (<think>,</think>)가 있는 모델이 전반적으로 IF 성능이 높음

- instruction-following과 mathematical reasoning사이에 trade-off가 존재

{% include figure.liquid loading="eager" path="assets/img/posts/2025-07-15-scaling-reasoning-losing-control-evaluating-instruction-following-in/image_001.png" class="img-fluid rounded z-depth-1" %}

- 제약조건을 만족하면서 문제를 맞추는 경우는 크지 않음

- 보통 제약조건 혹은 문제 하나만을 만족함 + 즉, 제약조건을 걸면 문제 풀이 성능이 하락

{% include figure.liquid loading="eager" path="assets/img/posts/2025-07-15-scaling-reasoning-losing-control-evaluating-instruction-following-in/image_002.png" class="img-fluid rounded z-depth-1" %}

- IF가 낮았던 Qwen2.5를 대상으로 실험, 데이터는 deepscalar를 사용, QwQ로 CoT생성, 정답을 맞추면서 너무 길지 않은 애들만 필터링해서 학습에 사용

- 실험 결과, reasoning-orienteed 방법론이 reasoning성능은 향상시키지만 IF는 하락하는 것을 볼 수 있음

Figure 7

- 모델이 reasonign path를 종료하려고 할 때마다 wait를 걸어서 강제로 CoT길이를 늘림

- CoT길이가 길어질수록 constraint instruction과 멀어져서 constraint에 대한 acc가 떨어지는 것으로 추론

Table 5

- cold-RL에서 roll-out 길이를 조정하며 학습, 길어질수록 reasoning은 향상되나 IF는 떨어짐

{% include figure.liquid loading="eager" path="assets/img/posts/2025-07-15-scaling-reasoning-losing-control-evaluating-instruction-following-in/image_003.png" class="img-fluid rounded z-depth-1" %}

- 간단하게 reasoning이 끝나갈 때 쯤에 wait을 넣고 constraint instruction을 반복해서 넣어준 경우의 성능을 측정

- IF성능은 향상되나 Correctness는 하락하는 것을 볼 수 있음

## Conclusion

- Reasoning-oriented model들이 생각보다 instruction following 성능이 악화됨

- 대부분 간단한 형식에 대한 제약인데도, 제약이 있을 때와 없을 때의 성능 차이가 큰게 충격적

- LLM이 정말 reasoning을 하는걸까? 그냥 답변 길이가 길어져서 발생하는 attention sink일까?
