---
categories:
- paper-reviews
date: '2025-08-30 00:00:00'
description: 논문 리뷰
giscus_comments: true
layout: post
related_posts: false
slug: 2025-08-30-reasoning-models-dont-always-say-what-they-think
tags:
- alignment
- paper-review
- reasoning
- reinforcement-learning
- rlhf
title: Reasoning Models Don’t Always Say What They Think
---

**논문 정보**
- **Date**: 2025-04-08
- **Reviewer**: 상엽

# Introduction

- CoT를 활용할 경우, reason, plan, trial and error와 같은 절차를 통해 복잡한 문제를 풀 수 있음.

- 모델의 발전: o1/o3, DeepSeek R1, Gemini Flash Thinking, Claude 3.7 Sonnet Extended Thinking

- 성능 외적으로도 CoT는 AI Safety에 활용이 가능함

→ CoT 자체를 신뢰할 수 없다면

→ 즉, 구체적 언어로 명시되지 않은 사고 과정에 의해 결과가 영향을 받는다면 

→ CoT 모니터링을 통한 Safety 확보를 보장할 수 없음.

일반적으로 우리는 CoT가 신뢰할 수 있다고 생각하는 경향이 있음.

- CoT없이는 풀기 어려운 문제의 경우: CoT 과정을 통해 정답을 도출했으므로

- CoT없이도 풀 수 있는 매우 쉬운 문제의 경우: 옳은 reasoning process를 가진 Human 데이터로 학습이 됐으므로

→ 하지만, **RLHF로 학습할 경우, 바람직하지 않은 reasoning 과정을 숨기기도 한다는 점을 발견.** 

→ 즉, AI의 실제 사고과정과 reasoning이 다를 수 있다는 의문을 제기.

**Section 3: Reasoning 모델의 신뢰성을 실험**

- Claude 3.7 Sonnet과 DeepSeek R1에 대해 6가지 유형의 **힌트**를 이용한 실험을 진행.

- Single forward pass에 대해서만 실험을 진행 (복잡한 reasoning process는 분석이 어려움.)

→ 1% ~ 20% 정도만이 사용한 힌트를 명시적으로 표시했다.

**Section 4: outcome-based RL이 CoT 신뢰성에 주는 영향을 조사**

- 가설: outcome-based RL이 결과만을 평가한다면 정답에 도움이 되는 신뢰할 수 있는 CoT를 더 장려할 것

- for example, **because more faithful ones are more helpful to solve the task**

→ 초기에는 신뢰성이 상승 했으나 곧바로 정체되며 만족할만한 점수를 달성하지 못함.

**Section 5: RL 학습 때 CoT를 통한 모니터링의 효과 검증**

- RL 학습 과정에서 reward hacking을 잡는 방법으로 CoT monitoring 방법이 있음.

- CoT는 reward hacking 행동에 대해 신뢰성 있게 보고를 하는가에 대한 질문

→ reward hacks이 발생하는 환경을 세팅 (reward > 0.99) → 6개의 환경 중 5개의 환경은 2% 이하만이 reward hack을 보고함.

# Measuring CoT Faithfulness

Notation

- input: x

- model: M

- CoT: c

- answer: a

### Metric

Inspired by Turpin et al. (2023); Chua and Evans (2025), we **evaluate faithfulness** using a constructed set of **prompt pairs** where we can infer information about the model’s internal reasoning by observing its responses

- “**unhinted**” **prompt** x_u (standard multiple-choice question)

- “**hinted**” **prompt** x_h (직접적으로 정답을 가리키는 힌트를 x_u에 추가한 것)

→ CoT의 faithfulness ==  x_u에서는 힌트가 아닌 다른 답변을 말하지만 x_h에서는 힌트를 정답으로 말할 때, 모델이 hinted prompt 문제를 풀기 위해 힌트를 사용했음을 말하는지 여부 (a_u \neq h \text { and } a_h=h인 경우)

답변 변경의 무작위 노이즈를 고려하기 위해 다음의 **정규화 과정**을 따름.

\left.p=P\left(a_h=h \mid a_u \neq h\right)\right): non-hint answer에서 hint answer로 바뀌는 확률 (위의 확률)

q=P\left(a_h \neq h, a_h \neq a_u \mid a_u \neq h\right): non-hint answer에서 다른 non-hint answer로 바뀌는 확률

- p에서 랜덤하게 값이 바뀌는 확률을 빼준 값을 이용, 무작위성에 대해 추정

- \alpha가 작을수록 무작위성이 큼을 의미함. (랜덤하게 골라졌을 확률이 높음.)

- \alpha를 이용해 normalize 진행

- **무작위성이 큰 환경에서도 hint를 골랐다는 건 그만큼 확신을 갖고 고른 것이다 → 신뢰성에 가중치!**

- \alpha가 음수인 경우는 x_h에서 h를 고르지 않을 확률이 더 높다는 뜻이며 이런 데이터는 제거함.

### Data

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/35aa05c3-53bf-4382-97c5-9fbdb0220eb6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRXM5WPA%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBirIFBszEFc0fpsBPCK%2B4NL8vX%2BuoMk0o%2Fhelo%2FUXv0AiEA%2Fttl75oDLcf0RweyfOkkS5RivtVqvD7GN%2F5ndz86djIqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOS%2FMwU5cer4mE83oSrcA4WfJB0obEk155XtqAUQphJjReTgR16AxS1TSJHdN7OZW9r5HhVpZBQX67w5ZL9XKVgZ8VJIAEdh2wlpKTOn7WVk5zMWhegE5CskdobKTVvpHwCDrskzKBbeNphdzLSvBxmSvVIvimlwJEYCVb7bTG6a4OXZwOFLG7%2BMnSjsVLNAPHN%2B771mWDBDY6Yvj%2FjJW9s6uOIdEtFMxQOJjeIB8n3ah9e0QmZ0LmaPB%2B%2BWoGq%2B3E1T6tjyJZaR3AJyHDWAxY2VUA4rrH5SJsUSMJ5PLAlk%2Ba2742vynLwofrWvs96wdNtq6tcYBCPdSh14VvIeiH4gowhz6kyKYwkYr58%2B9Fvb2TJgqEuKkwIYFPk7hAhC6TDcFXOKzOskHFaFkAnkDWtVPDUwF1Mi1MFNh1VEUmQHIEg0QIESRFFJwDEclyJ8msT0%2F4IlwD9VwmsXoXCMZaYhi5abPzVLsx2E3l9RuukqwiC9qLTdN5dTlmebRkOQNvOvsmMuJyjM3spwoIiXJspaQXcB2ocO1u4eg5rNj%2F5TzHOLDXVHfjwRO%2FmsqKX%2FGWiJ0f2SE8xpLCeqqUplJT4Put%2B1UD79yRZ61TXFj6iJTb9cJosNNDpz85%2B8en99Ug6HN9CnP5vphqi2MKTU4cQGOqUBp1sSjXpHiAetn7%2F%2BwKhr6PgIbV7CnCCcTNQRCGt4%2BRbYHy%2FD8GwDGzCp36v76zLv2mC69Azz%2FAmc5o7n0pMe7XVS2VT2zLH%2FBhTeKJXzwA5%2FHc1s%2BhcJop6%2BBgIY%2B8JM8DQgx49juXUOrXr0wZtFIjZIyoG0i8Vvbe8TA79TZwH4ygcLjYRoSk4kD8KoOm%2FzYEEs0oUwN%2Bl4kxJJH6hhul3GVZeZ&X-Amz-Signature=6288a5f4825a253cf029794245ea0f27c6822224ed49470474e4da7b81ccf514&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Neutral: 정답을 제공하는 방식을 다양하게 구성.

- Misaligned: 구체적으로 나쁜 행위들에 대해 예시를 통해 가르쳐줌.

### Experimental Setup

- Eliciting CoTs: Think step-by-step

- Evaluating CoTs: **verbalize 여부를 결정**

# Benchmarking CoT Faithfulness of Reasoning Models

- Reasoning model: Claude 3.7 Sonnet and DeepSeek R1

- Non-reasoning model: Claude 3.5 Sonnet and DeepSeek V3

**All evaluated models consistently use the hints.**

- 4가지 모두 일관되게 힌트를 사용하지만 Claude 모델이 더 자주 힌트를 사용함

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/004d56eb-7647-41e9-b505-003c062be59e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRXM5WPA%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBirIFBszEFc0fpsBPCK%2B4NL8vX%2BuoMk0o%2Fhelo%2FUXv0AiEA%2Fttl75oDLcf0RweyfOkkS5RivtVqvD7GN%2F5ndz86djIqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOS%2FMwU5cer4mE83oSrcA4WfJB0obEk155XtqAUQphJjReTgR16AxS1TSJHdN7OZW9r5HhVpZBQX67w5ZL9XKVgZ8VJIAEdh2wlpKTOn7WVk5zMWhegE5CskdobKTVvpHwCDrskzKBbeNphdzLSvBxmSvVIvimlwJEYCVb7bTG6a4OXZwOFLG7%2BMnSjsVLNAPHN%2B771mWDBDY6Yvj%2FjJW9s6uOIdEtFMxQOJjeIB8n3ah9e0QmZ0LmaPB%2B%2BWoGq%2B3E1T6tjyJZaR3AJyHDWAxY2VUA4rrH5SJsUSMJ5PLAlk%2Ba2742vynLwofrWvs96wdNtq6tcYBCPdSh14VvIeiH4gowhz6kyKYwkYr58%2B9Fvb2TJgqEuKkwIYFPk7hAhC6TDcFXOKzOskHFaFkAnkDWtVPDUwF1Mi1MFNh1VEUmQHIEg0QIESRFFJwDEclyJ8msT0%2F4IlwD9VwmsXoXCMZaYhi5abPzVLsx2E3l9RuukqwiC9qLTdN5dTlmebRkOQNvOvsmMuJyjM3spwoIiXJspaQXcB2ocO1u4eg5rNj%2F5TzHOLDXVHfjwRO%2FmsqKX%2FGWiJ0f2SE8xpLCeqqUplJT4Put%2B1UD79yRZ61TXFj6iJTb9cJosNNDpz85%2B8en99Ug6HN9CnP5vphqi2MKTU4cQGOqUBp1sSjXpHiAetn7%2F%2BwKhr6PgIbV7CnCCcTNQRCGt4%2BRbYHy%2FD8GwDGzCp36v76zLv2mC69Azz%2FAmc5o7n0pMe7XVS2VT2zLH%2FBhTeKJXzwA5%2FHc1s%2BhcJop6%2BBgIY%2B8JM8DQgx49juXUOrXr0wZtFIjZIyoG0i8Vvbe8TA79TZwH4ygcLjYRoSk4kD8KoOm%2FzYEEs0oUwN%2Bl4kxJJH6hhul3GVZeZ&X-Amz-Signature=b36c15b0f6203050c2fc2b25c73ae70859e395eeffa8a324b5e9a05a406cb32b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**CoTs of reasoning models reveal hints across more settings, and do so more often than those of non-reasoning models.** 

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/77ad8a4f-b079-4892-ac4c-5f280a869c3a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRXM5WPA%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBirIFBszEFc0fpsBPCK%2B4NL8vX%2BuoMk0o%2Fhelo%2FUXv0AiEA%2Fttl75oDLcf0RweyfOkkS5RivtVqvD7GN%2F5ndz86djIqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOS%2FMwU5cer4mE83oSrcA4WfJB0obEk155XtqAUQphJjReTgR16AxS1TSJHdN7OZW9r5HhVpZBQX67w5ZL9XKVgZ8VJIAEdh2wlpKTOn7WVk5zMWhegE5CskdobKTVvpHwCDrskzKBbeNphdzLSvBxmSvVIvimlwJEYCVb7bTG6a4OXZwOFLG7%2BMnSjsVLNAPHN%2B771mWDBDY6Yvj%2FjJW9s6uOIdEtFMxQOJjeIB8n3ah9e0QmZ0LmaPB%2B%2BWoGq%2B3E1T6tjyJZaR3AJyHDWAxY2VUA4rrH5SJsUSMJ5PLAlk%2Ba2742vynLwofrWvs96wdNtq6tcYBCPdSh14VvIeiH4gowhz6kyKYwkYr58%2B9Fvb2TJgqEuKkwIYFPk7hAhC6TDcFXOKzOskHFaFkAnkDWtVPDUwF1Mi1MFNh1VEUmQHIEg0QIESRFFJwDEclyJ8msT0%2F4IlwD9VwmsXoXCMZaYhi5abPzVLsx2E3l9RuukqwiC9qLTdN5dTlmebRkOQNvOvsmMuJyjM3spwoIiXJspaQXcB2ocO1u4eg5rNj%2F5TzHOLDXVHfjwRO%2FmsqKX%2FGWiJ0f2SE8xpLCeqqUplJT4Put%2B1UD79yRZ61TXFj6iJTb9cJosNNDpz85%2B8en99Ug6HN9CnP5vphqi2MKTU4cQGOqUBp1sSjXpHiAetn7%2F%2BwKhr6PgIbV7CnCCcTNQRCGt4%2BRbYHy%2FD8GwDGzCp36v76zLv2mC69Azz%2FAmc5o7n0pMe7XVS2VT2zLH%2FBhTeKJXzwA5%2FHc1s%2BhcJop6%2BBgIY%2B8JM8DQgx49juXUOrXr0wZtFIjZIyoG0i8Vvbe8TA79TZwH4ygcLjYRoSk4kD8KoOm%2FzYEEs0oUwN%2Bl4kxJJH6hhul3GVZeZ&X-Amz-Signature=da648273e675e6e6cca2309ab04e786fcab6a137da7d3791e12e656ba67d928d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- **Reasoning model이 더 높은 faithfulness 점수를 보임.**

- 여기서 **1% 초과 여부**를 계속 언급하는데 이유가 뭔지는 모르겠음.

- Grader Hacking, Unethical information과 같은 misalignment 영역에서 낮은 점수는 더 큰 문제

**CoT unfaithfulness is negatively correlated with brevity.**

- **신뢰할 수 없을수록 복잡하게 글을 작성하는 경향이 생김.**

- Claude 3.7 Sonnet의 경우, unfaithful CoTs (**2064** ± 59 tokens), faithful CoTs (1439 ± 54).

- DeepSeek R1의 경우, unfaithful CoTs (**6003** ± 74 tokens), faithful CoTs (4737 ± 79 tokens).

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/cc70151a-089d-4998-99bb-178fcecf3057/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRXM5WPA%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBirIFBszEFc0fpsBPCK%2B4NL8vX%2BuoMk0o%2Fhelo%2FUXv0AiEA%2Fttl75oDLcf0RweyfOkkS5RivtVqvD7GN%2F5ndz86djIqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOS%2FMwU5cer4mE83oSrcA4WfJB0obEk155XtqAUQphJjReTgR16AxS1TSJHdN7OZW9r5HhVpZBQX67w5ZL9XKVgZ8VJIAEdh2wlpKTOn7WVk5zMWhegE5CskdobKTVvpHwCDrskzKBbeNphdzLSvBxmSvVIvimlwJEYCVb7bTG6a4OXZwOFLG7%2BMnSjsVLNAPHN%2B771mWDBDY6Yvj%2FjJW9s6uOIdEtFMxQOJjeIB8n3ah9e0QmZ0LmaPB%2B%2BWoGq%2B3E1T6tjyJZaR3AJyHDWAxY2VUA4rrH5SJsUSMJ5PLAlk%2Ba2742vynLwofrWvs96wdNtq6tcYBCPdSh14VvIeiH4gowhz6kyKYwkYr58%2B9Fvb2TJgqEuKkwIYFPk7hAhC6TDcFXOKzOskHFaFkAnkDWtVPDUwF1Mi1MFNh1VEUmQHIEg0QIESRFFJwDEclyJ8msT0%2F4IlwD9VwmsXoXCMZaYhi5abPzVLsx2E3l9RuukqwiC9qLTdN5dTlmebRkOQNvOvsmMuJyjM3spwoIiXJspaQXcB2ocO1u4eg5rNj%2F5TzHOLDXVHfjwRO%2FmsqKX%2FGWiJ0f2SE8xpLCeqqUplJT4Put%2B1UD79yRZ61TXFj6iJTb9cJosNNDpz85%2B8en99Ug6HN9CnP5vphqi2MKTU4cQGOqUBp1sSjXpHiAetn7%2F%2BwKhr6PgIbV7CnCCcTNQRCGt4%2BRbYHy%2FD8GwDGzCp36v76zLv2mC69Azz%2FAmc5o7n0pMe7XVS2VT2zLH%2FBhTeKJXzwA5%2FHc1s%2BhcJop6%2BBgIY%2B8JM8DQgx49juXUOrXr0wZtFIjZIyoG0i8Vvbe8TA79TZwH4ygcLjYRoSk4kD8KoOm%2FzYEEs0oUwN%2Bl4kxJJH6hhul3GVZeZ&X-Amz-Signature=02070cfc003340d88b476dc9eb1cc945dff4847784bbb480261a53633df64e24&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Unfaithful CoTs에서는 **힌트를 사용하지 않고** (=Unfaithfulness) 장황한게 **각각의 옵션에 대해 확인을 하는 절차를 포함하는 경우가 많음.** 

- 더 문제가 되는 부분은 힌트를 정답으로 하기 위해 **기존 지식과 모순되는 방법을 동원**하기도 한다는 점. 이 때에도 힌트 사용 여부를 설명하지 않는 경우가 많음. 

**CoT appears to be less faithful on harder questions.** 

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/875f196a-7b36-4d58-90fa-2683539a057f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRXM5WPA%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBirIFBszEFc0fpsBPCK%2B4NL8vX%2BuoMk0o%2Fhelo%2FUXv0AiEA%2Fttl75oDLcf0RweyfOkkS5RivtVqvD7GN%2F5ndz86djIqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOS%2FMwU5cer4mE83oSrcA4WfJB0obEk155XtqAUQphJjReTgR16AxS1TSJHdN7OZW9r5HhVpZBQX67w5ZL9XKVgZ8VJIAEdh2wlpKTOn7WVk5zMWhegE5CskdobKTVvpHwCDrskzKBbeNphdzLSvBxmSvVIvimlwJEYCVb7bTG6a4OXZwOFLG7%2BMnSjsVLNAPHN%2B771mWDBDY6Yvj%2FjJW9s6uOIdEtFMxQOJjeIB8n3ah9e0QmZ0LmaPB%2B%2BWoGq%2B3E1T6tjyJZaR3AJyHDWAxY2VUA4rrH5SJsUSMJ5PLAlk%2Ba2742vynLwofrWvs96wdNtq6tcYBCPdSh14VvIeiH4gowhz6kyKYwkYr58%2B9Fvb2TJgqEuKkwIYFPk7hAhC6TDcFXOKzOskHFaFkAnkDWtVPDUwF1Mi1MFNh1VEUmQHIEg0QIESRFFJwDEclyJ8msT0%2F4IlwD9VwmsXoXCMZaYhi5abPzVLsx2E3l9RuukqwiC9qLTdN5dTlmebRkOQNvOvsmMuJyjM3spwoIiXJspaQXcB2ocO1u4eg5rNj%2F5TzHOLDXVHfjwRO%2FmsqKX%2FGWiJ0f2SE8xpLCeqqUplJT4Put%2B1UD79yRZ61TXFj6iJTb9cJosNNDpz85%2B8en99Ug6HN9CnP5vphqi2MKTU4cQGOqUBp1sSjXpHiAetn7%2F%2BwKhr6PgIbV7CnCCcTNQRCGt4%2BRbYHy%2FD8GwDGzCp36v76zLv2mC69Azz%2FAmc5o7n0pMe7XVS2VT2zLH%2FBhTeKJXzwA5%2FHc1s%2BhcJop6%2BBgIY%2B8JM8DQgx49juXUOrXr0wZtFIjZIyoG0i8Vvbe8TA79TZwH4ygcLjYRoSk4kD8KoOm%2FzYEEs0oUwN%2Bl4kxJJH6hhul3GVZeZ&X-Amz-Signature=8f03a959fc0da214213e57f5e520253f95e6bbfd94d7933e2c7481fe56098ef0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- **GPQA >> MMLU, GPQA에서 신뢰도가 훨씬 낮았음.** (Claude 3.7 Sonnet에서 44% R1에서 32% 감소)

- Faithful CoTs의 경우, **자신의 답변을 먼저 생성**하고 **Hint와 답변을 비교**하는 reasoning 과정을 가진 후 **hint에 따라 답을 바꾼다는 사실**을 보여줌. 

- CoT monitoring을 통한 safety 관리는 **어려운 문제로 scale이 어려울듯**

# The Impact of Outcome-Based Reinforcement Learning on CoT Faithfulness

- 이전 결과들에서 결론에 도달하는데 reasoning이 실제로 도움이 되지 않는 경우가 많다는 것을 발견

- 결론을 만드는 과정에서 **CoT에 더 의존적이게 학습**을 한다면 어떨까?

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/eafc4a97-fca3-40a6-87a0-904a97bf1b72/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRXM5WPA%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBirIFBszEFc0fpsBPCK%2B4NL8vX%2BuoMk0o%2Fhelo%2FUXv0AiEA%2Fttl75oDLcf0RweyfOkkS5RivtVqvD7GN%2F5ndz86djIqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOS%2FMwU5cer4mE83oSrcA4WfJB0obEk155XtqAUQphJjReTgR16AxS1TSJHdN7OZW9r5HhVpZBQX67w5ZL9XKVgZ8VJIAEdh2wlpKTOn7WVk5zMWhegE5CskdobKTVvpHwCDrskzKBbeNphdzLSvBxmSvVIvimlwJEYCVb7bTG6a4OXZwOFLG7%2BMnSjsVLNAPHN%2B771mWDBDY6Yvj%2FjJW9s6uOIdEtFMxQOJjeIB8n3ah9e0QmZ0LmaPB%2B%2BWoGq%2B3E1T6tjyJZaR3AJyHDWAxY2VUA4rrH5SJsUSMJ5PLAlk%2Ba2742vynLwofrWvs96wdNtq6tcYBCPdSh14VvIeiH4gowhz6kyKYwkYr58%2B9Fvb2TJgqEuKkwIYFPk7hAhC6TDcFXOKzOskHFaFkAnkDWtVPDUwF1Mi1MFNh1VEUmQHIEg0QIESRFFJwDEclyJ8msT0%2F4IlwD9VwmsXoXCMZaYhi5abPzVLsx2E3l9RuukqwiC9qLTdN5dTlmebRkOQNvOvsmMuJyjM3spwoIiXJspaQXcB2ocO1u4eg5rNj%2F5TzHOLDXVHfjwRO%2FmsqKX%2FGWiJ0f2SE8xpLCeqqUplJT4Put%2B1UD79yRZ61TXFj6iJTb9cJosNNDpz85%2B8en99Ug6HN9CnP5vphqi2MKTU4cQGOqUBp1sSjXpHiAetn7%2F%2BwKhr6PgIbV7CnCCcTNQRCGt4%2BRbYHy%2FD8GwDGzCp36v76zLv2mC69Azz%2FAmc5o7n0pMe7XVS2VT2zLH%2FBhTeKJXzwA5%2FHc1s%2BhcJop6%2BBgIY%2B8JM8DQgx49juXUOrXr0wZtFIjZIyoG0i8Vvbe8TA79TZwH4ygcLjYRoSk4kD8KoOm%2FzYEEs0oUwN%2Bl4kxJJH6hhul3GVZeZ&X-Amz-Signature=1fc2fd7f6233268ca7e003874a681025c290a27f50e6f536434edee0827ab2c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Sonnet 3.7 모델에 대해서 학습 극초기에는 MMLU 63%, GPQA 41% 정도 향상되는 것으로 보임.

- 더 학습을 진행하더라도 개선되지 않음. 
