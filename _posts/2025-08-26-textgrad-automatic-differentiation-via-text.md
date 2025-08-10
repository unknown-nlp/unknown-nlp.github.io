---
categories:
  - paper-reviews
date: "2025-08-26 00:00:00"
description: 논문 리뷰
giscus_comments: true
layout: post
related_posts: false
slug: 2025-08-26-textgrad-automatic-differentiation-via-text
tags:
  - gpt
  - language-model
  - llm
  - nlp
  - paper-review
title: "Textgrad:  Automatic “Differentiation” via Text"
---

**논문 정보**

- **Date**: 2025-06-03
- **Reviewer**: hyowon Cho

오늘은 평소의 리서치 관심사와는 달리, 회사에서.. 리서치를 요청한 분야에 대한 논문을 한 편 가져왔습니다.

오늘의 도메인은 **Automated Prompt Engineering** (APE) 입니다. 프롬프트 작성하는 기계가 되는 최근 AI application 시장에서 어찌보면 수요가 낭낭한 연구 분야라고도 할 수 있겠습니다-

도메인 자체는 다들 엄청 흥미있어 하지는 않을 것 같지만, 아직 보완할 부분이 많이 보여서 분석+실험 설계만 잘 한다면 후속 논문 쓸 때는 재미있을 것 같은 연구였어요. 저는 개인적으로 연구 방향에 동의해서 재밌었슴다.

더불어서, nature에 NLP 연구가 요새 종종 보이는데, 어떤 유형이 accept되나 궁금증 겸사겸사 해소도 되고, 역시 연구는 프레이밍이 중요하다라는 것을 느낀 연구입니다.

거두절미 하고 들어가보죠

# 1. Introduction

LLM의 발전으로 인해 AI 시스템을 구축하는 방식에 패러다임 변화가 일고 있습니다. 하지만 이 중 많은 breakthroughs는 특정 도메인의 전문가들이 수작업으로 만든 시스템과 heuristic한 튜닝을 통해 이뤄졌습니다. 따라서 LLM 기반 시스템을 제대로 구축하려면 이를 자동으로 최적화할 수 있는 방식이 필요합니다.

과거 15년간의 AI 발전은 대부분 인공신경망과 미분 가능한 최적화에 기반했죠. 두 뉴런 사이를 연결하는 연산은 행렬곱처럼 미분 가능한 함수이고, 역전파(Backpropagation)는 그 구조 내에서 parameter를 조정하는 방식이었습니다. PyTorch 등 자동 미분 프레임워크가 필수였던 이유도 여기에 있죠.

이번 논문에서는 AI 시스템을 최적화하기 위해 **TEXTGRAD**라는 개념을 소개합니다. 여기에서 우리는 미분(differentiation)과 그래디언트(gradients)를, LLM이 제공하는 텍스트 기반 피드백에 대한 은유적 표현으로 사용합니다.

TEXTGRAD는 AI 시스템을 계산 그래프로 표현하고, 각 노드(변수)에 대해 LLM으로부터 자연어 피드백을 받아 이를 "텍스트 그래디언트(textual gradient)"로 간주합니다. 이후 이 피드백을 그래프 구조를 따라 역방향으로 전파(backpropagation)하며, 각 변수(프롬프트, 응답 등)를 업데이트합니다. 이 과정은 LLM API 호출, 시뮬레이터, 외부 수치 해석기 등을 포함하는 복잡한 연산 구조에도 적용 가능합니다.

저자들은 다양한 도메인에서 TEXTGRAD를 적용한 결과를 보입니다:

1. **코딩**: LeetCode 문제에서 GPT-4o 및 기존 기법 대비 20% 성능 향상.

1. **문제 해결**: 과학 문제에 대해 GPT-4o의 zero-shot 정확도 51% → 55%로 개선.

1. **추론**: GPT-3.5 성능을 prompt optimization으로 GPT-4 수준으로 끌어올림.

1. **화학**: 약물 친화도 및 druglikeness가 높은 분자를 새로 디자인.

1. **의료**: 전립선암 방사선 치료 플랜을 최적화하여 효과는 높이고 부작용은 줄임,

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/5567aae6-d340-4328-8c45-a72a7b5bb372/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7_2025-05-19_142325.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFY7G5TL%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGinWivckc59RrOIStwhLvrEs3MulynalaMc7x%2FbhKKeAiEAq3H2OZvkDVJsPq1HqoTR1wsUL8BauQxr%2BP%2FuNokDTXoqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJT21E0Hdx%2BA8Ar7%2FSrcA0YpVR4KWs5cUejYPbL%2F5lyvfoa%2BZz6cjxF31iqaG7THbZbqSldDwytX44e%2BCrvB3ofNyJTgnx3TFdCoYyspkNLbo%2BaAH%2FH%2BmHeLY6wLAbJyuLhJ8j%2FWI7iaSXGbU1fPJcAqI%2BlvXjwgvw7jxEfj7m6ZmN9rpmN6jFMMM707yJjyIeSiNmim3w0btvQMcE1d8QYaB4tnhg3uP0XAwABh5BxByD2urMHfwykHyAqbgWAgN0gg3p9hmyMfkOEBPFlS4l4MErjMZzQqvQBAX1cjpaJlAzlB5TV2GYU%2FYfpsMf6JimpqZaBUKSK9oXi%2FmhRqdPW2ZmN8QRCzAZcMp1b2n7NqkRVRrhWgiERfEuiC6NnyH%2FjrROcRsu9%2BQs4Hbju42LUKsGeae65m6Vvmt37pdXdqW3mCdLud3KOmSfpXAYAXneIPHZn0sdya93EAc7RZ6r5tib6xBaRH6%2BeMN8GTtGGZNwXRQDNBl3JT2XAqQuXVwKKZ3i3d3QyHwQ%2B7TRW2flw8%2B152LkOKjSaQDBUJfyXZVkaCLhUjCCsECXvIfd0ZtdgXlUQOBWT5fR1BbTrLwjCk7ALMK8uenuZqd0iM4rh5kTTrG30aod4BTDftzwZW0RXGQCXmxM9M%2BvB%2BMM%2FU4cQGOqUBzn%2FgDKfmiZab14gOIYYJAJ2%2FFL6JNrGTQWhKBuxqYgKzSWiIU856moSEkTX6fsZAoDoom4jSXsdeXD4qvTBZu%2B6%2Fu4I3qm9Hv60Y5yxo6wNZ0ZZPPdNSWlK%2F8jOxV2kGCWAOwDzmKHWBiUlp5NdUt5jR%2FVP62W8VhcocGBwPX4DGTlFgA1%2Fv082VHJnjQTsXiruCjlW4%2FN3irhe6j8vASQKjdwkf&X-Amz-Signature=3ce2bc5b294d17012ebb526924c6b1ea565dc1f394c038c62abb4c2440aaa346&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# 2. TEXTGRAD: Optimizing AI systems by backpropagating text feedback

먼저 두 개의 LLM 호출로 구성된 간단한 예제를 통해 TEXTGRAD가 어떤 모습인지 보여주고, 그 뒤에는 더 일반적인 시스템에 대한 설명을 이어갑니다:

계산 그래프는 다음과 같이 정의됩니다:

1. Prediction = LLM(**_Prompt _**+ Question)

1. Evaluation = LLM(Evaluation Instruction + Prediction)

여기서 우리가 최적화하려는 자유 변수는 "Prompt"이고, +는 문자열 연결을 의미하며, LLM(x)는 x를 프롬프트로 넣어 응답을 받는 LLM 호출을 의미합니다.

이를 다음과 같이 체인 표기법으로 나타낼 수 있습니다:

**_Prompt _**+ Question LLM→ Evaluation Instruction + Prediction LLM → Evaluation

즉, 첫 번째 LLM 호출로 Question에 대해 Prompt를 기반으로 Prediction을 생성하고, 두 번째 LLM 호출로 그 Prediction에 대해 평가합니다.

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/dab02a04-64d0-497b-a005-e4b6e6ed41b9/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7_2025-05-19_142904.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFY7G5TL%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGinWivckc59RrOIStwhLvrEs3MulynalaMc7x%2FbhKKeAiEAq3H2OZvkDVJsPq1HqoTR1wsUL8BauQxr%2BP%2FuNokDTXoqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJT21E0Hdx%2BA8Ar7%2FSrcA0YpVR4KWs5cUejYPbL%2F5lyvfoa%2BZz6cjxF31iqaG7THbZbqSldDwytX44e%2BCrvB3ofNyJTgnx3TFdCoYyspkNLbo%2BaAH%2FH%2BmHeLY6wLAbJyuLhJ8j%2FWI7iaSXGbU1fPJcAqI%2BlvXjwgvw7jxEfj7m6ZmN9rpmN6jFMMM707yJjyIeSiNmim3w0btvQMcE1d8QYaB4tnhg3uP0XAwABh5BxByD2urMHfwykHyAqbgWAgN0gg3p9hmyMfkOEBPFlS4l4MErjMZzQqvQBAX1cjpaJlAzlB5TV2GYU%2FYfpsMf6JimpqZaBUKSK9oXi%2FmhRqdPW2ZmN8QRCzAZcMp1b2n7NqkRVRrhWgiERfEuiC6NnyH%2FjrROcRsu9%2BQs4Hbju42LUKsGeae65m6Vvmt37pdXdqW3mCdLud3KOmSfpXAYAXneIPHZn0sdya93EAc7RZ6r5tib6xBaRH6%2BeMN8GTtGGZNwXRQDNBl3JT2XAqQuXVwKKZ3i3d3QyHwQ%2B7TRW2flw8%2B152LkOKjSaQDBUJfyXZVkaCLhUjCCsECXvIfd0ZtdgXlUQOBWT5fR1BbTrLwjCk7ALMK8uenuZqd0iM4rh5kTTrG30aod4BTDftzwZW0RXGQCXmxM9M%2BvB%2BMM%2FU4cQGOqUBzn%2FgDKfmiZab14gOIYYJAJ2%2FFL6JNrGTQWhKBuxqYgKzSWiIU856moSEkTX6fsZAoDoom4jSXsdeXD4qvTBZu%2B6%2Fu4I3qm9Hv60Y5yxo6wNZ0ZZPPdNSWlK%2F8jOxV2kGCWAOwDzmKHWBiUlp5NdUt5jR%2FVP62W8VhcocGBwPX4DGTlFgA1%2Fv082VHJnjQTsXiruCjlW4%2FN3irhe6j8vASQKjdwkf&X-Amz-Signature=497917740481ea1a8e643b7c30d43f4104e3823a710e18b06307a0f406052ae7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/741d756e-477c-46ff-b74f-988e2381275d/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7_2025-05-19_142926.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFY7G5TL%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGinWivckc59RrOIStwhLvrEs3MulynalaMc7x%2FbhKKeAiEAq3H2OZvkDVJsPq1HqoTR1wsUL8BauQxr%2BP%2FuNokDTXoqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJT21E0Hdx%2BA8Ar7%2FSrcA0YpVR4KWs5cUejYPbL%2F5lyvfoa%2BZz6cjxF31iqaG7THbZbqSldDwytX44e%2BCrvB3ofNyJTgnx3TFdCoYyspkNLbo%2BaAH%2FH%2BmHeLY6wLAbJyuLhJ8j%2FWI7iaSXGbU1fPJcAqI%2BlvXjwgvw7jxEfj7m6ZmN9rpmN6jFMMM707yJjyIeSiNmim3w0btvQMcE1d8QYaB4tnhg3uP0XAwABh5BxByD2urMHfwykHyAqbgWAgN0gg3p9hmyMfkOEBPFlS4l4MErjMZzQqvQBAX1cjpaJlAzlB5TV2GYU%2FYfpsMf6JimpqZaBUKSK9oXi%2FmhRqdPW2ZmN8QRCzAZcMp1b2n7NqkRVRrhWgiERfEuiC6NnyH%2FjrROcRsu9%2BQs4Hbju42LUKsGeae65m6Vvmt37pdXdqW3mCdLud3KOmSfpXAYAXneIPHZn0sdya93EAc7RZ6r5tib6xBaRH6%2BeMN8GTtGGZNwXRQDNBl3JT2XAqQuXVwKKZ3i3d3QyHwQ%2B7TRW2flw8%2B152LkOKjSaQDBUJfyXZVkaCLhUjCCsECXvIfd0ZtdgXlUQOBWT5fR1BbTrLwjCk7ALMK8uenuZqd0iM4rh5kTTrG30aod4BTDftzwZW0RXGQCXmxM9M%2BvB%2BMM%2FU4cQGOqUBzn%2FgDKfmiZab14gOIYYJAJ2%2FFL6JNrGTQWhKBuxqYgKzSWiIU856moSEkTX6fsZAoDoom4jSXsdeXD4qvTBZu%2B6%2Fu4I3qm9Hv60Y5yxo6wNZ0ZZPPdNSWlK%2F8jOxV2kGCWAOwDzmKHWBiUlp5NdUt5jR%2FVP62W8VhcocGBwPX4DGTlFgA1%2Fv082VHJnjQTsXiruCjlW4%2FN3irhe6j8vASQKjdwkf&X-Amz-Signature=2ead02a8c3017b247cc5ed75da204fb13b98e7586ef34935d5b8bc299353c281&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## The general case

이 추상화는 복잡한 시스템으로 쉽게 확장할 수 있습니다. 계산 그래프의 각 변수 v에 대해 다음과 같이 정의합니다. PredecessorsOf는 해당 변수의 입력값들을, SuccessorsOf는 출력값들을 나타냅니다.:

```javascript
v = f_v(PredecessorsOf(v))   for all v ∈ V
```

대체로 v의 값은 자연어 텍스트나 이미지 같은 비구조적 데이터일 수 있습니다. 이 논문에서는 대부분 자연어 텍스트로 구성되어 있습니다.

각 함수 f_v는 입력 변수 집합을 받아서 새로운 변수를 생성합니다. 예를 들어, LLM이나 수치 시뮬레이터가 이 역할을 수행할 수 있습니다.

그래디언트는 다음과 같이 계산됩니다:

```javascript
∂L/∂v = sum[ ∇f_v(w, ∂L/∂w)  for w ∈ SuccessorsOf(v) ]
```

즉, 변수 v가 사용된 모든 맥락(context)으로부터 피드백을 수집하고 이를 집계합니다.

최종적으로 변수 v를 업데이트할 때는 다음의 Optimizer를 사용합니다:

```javascript
v_new = TGD.step(v, ∂L/∂v)
```

계산 그래프에 n개의 엣지가 있다고 할 때, 각 최적화 반복(iteration)마다 최대 n번의 LLM 호출이 추가로 이뤄지며, 각각의 엣지에 대해 한 번씩 그래디언트를 계산합니다. TEXTGRAD의 연산 구현은 부록 A를 참고하면 됩니다.

### Appendix A.1: Variables

아래는 변수의 가장 핵심적인 속성들입니다:

1. **값 (Value):** 변수에 담긴 비구조적 데이터입니다. 본 논문에서는 대부분 텍스트 데이터입니다.

1. **역할 설명 (Role description):** 해당 변수가 계산 그래프 내에서 어떤 역할을 수행하는지를 설명하는 정보입니다. 이는 사용자가 그래프에 지식을 삽입하고 최적화 방향을 안내하는 데 활용됩니다. 예를 들어, "system prompt"나 "language model의 최종 출력"과 같은 설명이 될 수 있습니다.

1. **그래디언트 (Gradients):** 역전파 과정에서 LLM이 제공하는 자연어 기반 피드백입니다. 변수의 값을 어떻게 바꾸면 downstream loss를 줄일 수 있을지를 설명합니다.

1. **선행 변수 (Predecessors):** 해당 변수를 생성하는 데 사용된 변수들의 집합입니다. 예: LLM 호출에서 instruction과 question을 입력으로 넣고 response를 얻었다면, instruction과 question은 response의 선행 변수입니다.

1. **requires_grad:** PyTorch와 유사하게, 해당 변수에 대해 그래디언트를 계산할지 여부를 나타냅니다. 예를 들어, question 변수에 대해 그래디언트를 계산하고 싶지 않다면 `Variable(value=question, requires_grad=False, ...)`로 설정하면 됩니다.

### Appendix A.2: Backpropagation

TEXTGRAD의 역전파는 각 노드가 사용된 모든 맥락으로부터 피드백을 수집하고, 이 피드백을 선행 노드로 전파하는 구조를 따릅니다. 즉, 어떤 변수에 대한 그래디언트는 그것이 어떤 결과를 만들었고 그 결과가 얼마나 좋았는지에 대한 LLM의 피드백으로 표현됩니다. 이 피드백은 후속 노드로부터 역방향으로 전파되어 최종적으로 최적화하고자 하는 변수에 도달합니다.

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/52c75b77-3281-4df4-93e5-4fac073988f9/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7_2025-05-19_143422.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFY7G5TL%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGinWivckc59RrOIStwhLvrEs3MulynalaMc7x%2FbhKKeAiEAq3H2OZvkDVJsPq1HqoTR1wsUL8BauQxr%2BP%2FuNokDTXoqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJT21E0Hdx%2BA8Ar7%2FSrcA0YpVR4KWs5cUejYPbL%2F5lyvfoa%2BZz6cjxF31iqaG7THbZbqSldDwytX44e%2BCrvB3ofNyJTgnx3TFdCoYyspkNLbo%2BaAH%2FH%2BmHeLY6wLAbJyuLhJ8j%2FWI7iaSXGbU1fPJcAqI%2BlvXjwgvw7jxEfj7m6ZmN9rpmN6jFMMM707yJjyIeSiNmim3w0btvQMcE1d8QYaB4tnhg3uP0XAwABh5BxByD2urMHfwykHyAqbgWAgN0gg3p9hmyMfkOEBPFlS4l4MErjMZzQqvQBAX1cjpaJlAzlB5TV2GYU%2FYfpsMf6JimpqZaBUKSK9oXi%2FmhRqdPW2ZmN8QRCzAZcMp1b2n7NqkRVRrhWgiERfEuiC6NnyH%2FjrROcRsu9%2BQs4Hbju42LUKsGeae65m6Vvmt37pdXdqW3mCdLud3KOmSfpXAYAXneIPHZn0sdya93EAc7RZ6r5tib6xBaRH6%2BeMN8GTtGGZNwXRQDNBl3JT2XAqQuXVwKKZ3i3d3QyHwQ%2B7TRW2flw8%2B152LkOKjSaQDBUJfyXZVkaCLhUjCCsECXvIfd0ZtdgXlUQOBWT5fR1BbTrLwjCk7ALMK8uenuZqd0iM4rh5kTTrG30aod4BTDftzwZW0RXGQCXmxM9M%2BvB%2BMM%2FU4cQGOqUBzn%2FgDKfmiZab14gOIYYJAJ2%2FFL6JNrGTQWhKBuxqYgKzSWiIU856moSEkTX6fsZAoDoom4jSXsdeXD4qvTBZu%2B6%2Fu4I3qm9Hv60Y5yxo6wNZ0ZZPPdNSWlK%2F8jOxV2kGCWAOwDzmKHWBiUlp5NdUt5jR%2FVP62W8VhcocGBwPX4DGTlFgA1%2Fv082VHJnjQTsXiruCjlW4%2FN3irhe6j8vASQKjdwkf&X-Amz-Signature=84b0b96885ae23540e415ba2cc7e4545ecd4ee110036041412077147ec3cf8a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Appendix A.3: Functions

TEXTGRAD는 forward와 backward 양방향 연산이 정의된 여러 종류의 연산을 지원합니다. 이들은 PyTorch 스타일의 추상 클래스 `textgrad.autograd.Function`을 상속하며, `forward`와 `backward` 메서드를 정의합니다.

가장 핵심적인 함수는 **LLMCall Function**입니다:

- **Forward 모드:** LLM에 API 호출을 하며, 호출에 사용된 모든 입력 변수들은 출력(response)의 선행 변수로 등록됩니다. 예를 들어 instruction + question → response의 경우, response의 선행 변수는 [instruction, question]입니다.

- **Backward 모드:** 응답(response)에 대한 그래디언트를 instruction 및 question으로 전파합니다. 이때 system prompt에 다음과 같은 glossary 태그를 추가하여 LLM이 어떤 역할의 변수에 피드백을 줘야 하는지 명확히 합니다:

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/3a2dd53d-8f55-4aa6-8c7f-758ab7dd915e/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7_2025-05-19_144539.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFY7G5TL%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGinWivckc59RrOIStwhLvrEs3MulynalaMc7x%2FbhKKeAiEAq3H2OZvkDVJsPq1HqoTR1wsUL8BauQxr%2BP%2FuNokDTXoqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJT21E0Hdx%2BA8Ar7%2FSrcA0YpVR4KWs5cUejYPbL%2F5lyvfoa%2BZz6cjxF31iqaG7THbZbqSldDwytX44e%2BCrvB3ofNyJTgnx3TFdCoYyspkNLbo%2BaAH%2FH%2BmHeLY6wLAbJyuLhJ8j%2FWI7iaSXGbU1fPJcAqI%2BlvXjwgvw7jxEfj7m6ZmN9rpmN6jFMMM707yJjyIeSiNmim3w0btvQMcE1d8QYaB4tnhg3uP0XAwABh5BxByD2urMHfwykHyAqbgWAgN0gg3p9hmyMfkOEBPFlS4l4MErjMZzQqvQBAX1cjpaJlAzlB5TV2GYU%2FYfpsMf6JimpqZaBUKSK9oXi%2FmhRqdPW2ZmN8QRCzAZcMp1b2n7NqkRVRrhWgiERfEuiC6NnyH%2FjrROcRsu9%2BQs4Hbju42LUKsGeae65m6Vvmt37pdXdqW3mCdLud3KOmSfpXAYAXneIPHZn0sdya93EAc7RZ6r5tib6xBaRH6%2BeMN8GTtGGZNwXRQDNBl3JT2XAqQuXVwKKZ3i3d3QyHwQ%2B7TRW2flw8%2B152LkOKjSaQDBUJfyXZVkaCLhUjCCsECXvIfd0ZtdgXlUQOBWT5fR1BbTrLwjCk7ALMK8uenuZqd0iM4rh5kTTrG30aod4BTDftzwZW0RXGQCXmxM9M%2BvB%2BMM%2FU4cQGOqUBzn%2FgDKfmiZab14gOIYYJAJ2%2FFL6JNrGTQWhKBuxqYgKzSWiIU856moSEkTX6fsZAoDoom4jSXsdeXD4qvTBZu%2B6%2Fu4I3qm9Hv60Y5yxo6wNZ0ZZPPdNSWlK%2F8jOxV2kGCWAOwDzmKHWBiUlp5NdUt5jR%2FVP62W8VhcocGBwPX4DGTlFgA1%2Fv082VHJnjQTsXiruCjlW4%2FN3irhe6j8vASQKjdwkf&X-Amz-Signature=748850623f25d6a69b05ff57abd09923596cc12a2d56ad48f006bf406ad81c8e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Appendix A.4: Textual Gradient Descent Implementation

역전파와 마찬가지로, TEXTGRAD의 최적화 단계도 일반성을 유지하도록 구현되어 있습니다. optimizer에 glossary를 포함하여, 각 변수의 역할, 목표, 현재 값 등을 포함한 정보를 시스템 프롬프트에 넣고, 피드백을 바탕으로 값을 업데이트합니다.

## Objective functions

수치 최적화나 자동 미분에서는, 목적 함수(objective function)는 일반적으로 mean squared error나 cross entropy처럼 미분 가능한 함수입니다. 하지만 TEXTGRAD에서는 목적 함수가 더 복잡하거나 미분 불가능한 함수일 수 있으며, 함수의 정의역(domain)과 공역(codomain)이 비구조적인 데이터일 수도 있습니다.

a simple loss function for a code snippet can be the following:
`Loss(code, target goal) =LLM(Here is a code snippet:{code}.`

## Instance vs Prompt Optimization

이 논문에서 다루는 최적화 문제는 크게 두 가지 범주로 나뉩니다:

- **인스턴스 최적화:** 특정 문제의 해답—예: 코드 조각, 문제 풀이, 분자 구조 등을 직접 최적화 변수로 간주합니다. 예컨대 앞서 언급한 코드 예시에서는, 테스트 시점에서 특정 코드 인스턴스를 개선하는 것이 목표입니다. 프레임워크는 이에 대해 그래디언트를 생성하고, 해당 코드를 직접 최적화합니다.

- **프롬프트 최적화:** 특정 작업에 대해 다수의 쿼리에 대해 성능을 높이는 프롬프트를 찾는 것이 목표입니다. 예를 들어, 수학적 추론 문제에 대해 LLM의 성능을 향상시키는 시스템 프롬프트를 찾는 것이 될 수 있습니다 (§3.3 참조). 여기서는 단일 쿼리에 대한 성능 향상보다는, 다양한 쿼리에 일반화될 수 있는 프롬프트를 만드는 것이 목적입니다.

두 가지 문제 유형 모두 TEXTGRAD 프레임워크를 별도로 손대지 않고 동일하게 해결할 수 있습니다.

## Optimization Techniques

TEXTGRAD는 자동 미분의 개념을 기반으로 하고 있으며, 이 개념은 프레임워크에 포함된 여러 최적화 기법들을 이론적으로 뒷받침합니다. 아래는 구현된 예시들입니다:

- **Batch Optimization:** 프롬프트 최적화를 위해 stochastic minibatch gradient descent를 구현했습니다. 각 반복마다 여러 인스턴스를 배치로 forward pass한 후 개별 loss 항목을 계산하고, `tg.sum` 함수를 통해 총 loss를 합산합니다 (torch.sum과 유사). backward pass에서는 개별 loss 항목을 통해 얻은 그래디언트를 각 변수에 대해 합칩니다.

- **Constrained Optimization:** 제약 조건이 있는 최적화(constrained optimization) 개념을 차용하여, 자연어 기반 제약 조건을 사용합니다. 예: "응답의 마지막 줄은 반드시 'Answer: $LETTER' 형식이어야 하며, LETTER는 ABCD 중 하나여야 한다." LLM은 instruction-tuning 덕분에 이러한 간단한 제약 조건을 잘 따르며, 단 제약 조건이 너무 많아질 경우 신뢰도가 낮아질 수 있습니다.

- **모멘텀 (Momentum):** 변수 업데이트 시, TGD 옵티마이저는 해당 변수의 이전 iteration들 또한 참고할 수 있습니다.

TEXTGRAD에 구현된 최적화 기법들의 더 자세한 내용은 부록 B에서 확인할 수 있습니다:

## Appendix B

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/95d70420-21a4-41de-9a2b-f1d8c1327c36/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7_2025-05-19_144943.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFY7G5TL%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGinWivckc59RrOIStwhLvrEs3MulynalaMc7x%2FbhKKeAiEAq3H2OZvkDVJsPq1HqoTR1wsUL8BauQxr%2BP%2FuNokDTXoqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJT21E0Hdx%2BA8Ar7%2FSrcA0YpVR4KWs5cUejYPbL%2F5lyvfoa%2BZz6cjxF31iqaG7THbZbqSldDwytX44e%2BCrvB3ofNyJTgnx3TFdCoYyspkNLbo%2BaAH%2FH%2BmHeLY6wLAbJyuLhJ8j%2FWI7iaSXGbU1fPJcAqI%2BlvXjwgvw7jxEfj7m6ZmN9rpmN6jFMMM707yJjyIeSiNmim3w0btvQMcE1d8QYaB4tnhg3uP0XAwABh5BxByD2urMHfwykHyAqbgWAgN0gg3p9hmyMfkOEBPFlS4l4MErjMZzQqvQBAX1cjpaJlAzlB5TV2GYU%2FYfpsMf6JimpqZaBUKSK9oXi%2FmhRqdPW2ZmN8QRCzAZcMp1b2n7NqkRVRrhWgiERfEuiC6NnyH%2FjrROcRsu9%2BQs4Hbju42LUKsGeae65m6Vvmt37pdXdqW3mCdLud3KOmSfpXAYAXneIPHZn0sdya93EAc7RZ6r5tib6xBaRH6%2BeMN8GTtGGZNwXRQDNBl3JT2XAqQuXVwKKZ3i3d3QyHwQ%2B7TRW2flw8%2B152LkOKjSaQDBUJfyXZVkaCLhUjCCsECXvIfd0ZtdgXlUQOBWT5fR1BbTrLwjCk7ALMK8uenuZqd0iM4rh5kTTrG30aod4BTDftzwZW0RXGQCXmxM9M%2BvB%2BMM%2FU4cQGOqUBzn%2FgDKfmiZab14gOIYYJAJ2%2FFL6JNrGTQWhKBuxqYgKzSWiIU856moSEkTX6fsZAoDoom4jSXsdeXD4qvTBZu%2B6%2Fu4I3qm9Hv60Y5yxo6wNZ0ZZPPdNSWlK%2F8jOxV2kGCWAOwDzmKHWBiUlp5NdUt5jR%2FVP62W8VhcocGBwPX4DGTlFgA1%2Fv082VHJnjQTsXiruCjlW4%2FN3irhe6j8vASQKjdwkf&X-Amz-Signature=923fdc1919547bc30d8b12a7e57fa97ab4985f8462e9edf9c6c4524c401920eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/3b70a581-9392-4d7e-bc0f-97e06cb38094/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7_2025-05-19_145001.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFY7G5TL%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGinWivckc59RrOIStwhLvrEs3MulynalaMc7x%2FbhKKeAiEAq3H2OZvkDVJsPq1HqoTR1wsUL8BauQxr%2BP%2FuNokDTXoqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJT21E0Hdx%2BA8Ar7%2FSrcA0YpVR4KWs5cUejYPbL%2F5lyvfoa%2BZz6cjxF31iqaG7THbZbqSldDwytX44e%2BCrvB3ofNyJTgnx3TFdCoYyspkNLbo%2BaAH%2FH%2BmHeLY6wLAbJyuLhJ8j%2FWI7iaSXGbU1fPJcAqI%2BlvXjwgvw7jxEfj7m6ZmN9rpmN6jFMMM707yJjyIeSiNmim3w0btvQMcE1d8QYaB4tnhg3uP0XAwABh5BxByD2urMHfwykHyAqbgWAgN0gg3p9hmyMfkOEBPFlS4l4MErjMZzQqvQBAX1cjpaJlAzlB5TV2GYU%2FYfpsMf6JimpqZaBUKSK9oXi%2FmhRqdPW2ZmN8QRCzAZcMp1b2n7NqkRVRrhWgiERfEuiC6NnyH%2FjrROcRsu9%2BQs4Hbju42LUKsGeae65m6Vvmt37pdXdqW3mCdLud3KOmSfpXAYAXneIPHZn0sdya93EAc7RZ6r5tib6xBaRH6%2BeMN8GTtGGZNwXRQDNBl3JT2XAqQuXVwKKZ3i3d3QyHwQ%2B7TRW2flw8%2B152LkOKjSaQDBUJfyXZVkaCLhUjCCsECXvIfd0ZtdgXlUQOBWT5fR1BbTrLwjCk7ALMK8uenuZqd0iM4rh5kTTrG30aod4BTDftzwZW0RXGQCXmxM9M%2BvB%2BMM%2FU4cQGOqUBzn%2FgDKfmiZab14gOIYYJAJ2%2FFL6JNrGTQWhKBuxqYgKzSWiIU856moSEkTX6fsZAoDoom4jSXsdeXD4qvTBZu%2B6%2Fu4I3qm9Hv60Y5yxo6wNZ0ZZPPdNSWlK%2F8jOxV2kGCWAOwDzmKHWBiUlp5NdUt5jR%2FVP62W8VhcocGBwPX4DGTlFgA1%2Fv082VHJnjQTsXiruCjlW4%2FN3irhe6j8vASQKjdwkf&X-Amz-Signature=b64c98ed3af174f95c9bcf68856e211d303179272ee5ab9c895539c6e599673b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# 3. Results

해당 섹션에서는 TEXTGRAD을 다양한 응용 분야에서 사용해봅니다. §3.1에서는 어려운 코딩 문제에 대한 코드 스니펫을 최적화하고, §3.2에서는 과학 문제 해결을 위한 솔루션을 개선하며, §3.3에서는 프롬프트를 최적화하여 LLM의 추론 능력을 향상시킵니다. §3.4에서는 분자 구조를 최적화하여 약물 특성을 향상시키고, §3.5에서는 전립선암 환자를 위한 방사선 치료 계획을 최적화합니다.

## 3.1 Code optimization

코드 최적화는 인스턴스 최적화의 대표적인 사례. 여기서 목표는 코드의 정확성과 실행 복잡도를 개선하는 것입니다. 일반적인 계산 그래프는 다음과 같습니다:

```plain text
Code-Refinement Objective = LLM(Problem + ***Code ***+ Test-time Instruction + Local Test Results)
```

Test-time Instruction = critique or investigate the current iteration

예시: "정수 배열 nums와 정수 k가 주어졌을 때, 중앙값이 k인 비어있지 않은 subarrays 수를 반환하시오."

GPT-4o가 생성한 첫 번째 해답은 테스트를 통과하지 못했고, TEXTGRAD는 edge case를 식별하고 개선 방안을 제안. 최종 최적화된 구현은 모든 테스트를 통과함.

- **Task:** LeetCode Hard 데이터셋을 사용. 이 데이터셋은 매우 어려운 문제로 구성되어 있으며 GPT-4조차도 7% 성공률을 보이는 것으로 알려져 있음. 테스트 데이터가 public하지 않기 때문에, 만들고 하나하나 LeetCode platform에 제출되었음. (unseen task)

- **Baseline:**

- **결과:**

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/ae04007e-9564-4dd2-9976-8a24cf9ca089/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7_2025-05-19_145441.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFY7G5TL%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGinWivckc59RrOIStwhLvrEs3MulynalaMc7x%2FbhKKeAiEAq3H2OZvkDVJsPq1HqoTR1wsUL8BauQxr%2BP%2FuNokDTXoqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJT21E0Hdx%2BA8Ar7%2FSrcA0YpVR4KWs5cUejYPbL%2F5lyvfoa%2BZz6cjxF31iqaG7THbZbqSldDwytX44e%2BCrvB3ofNyJTgnx3TFdCoYyspkNLbo%2BaAH%2FH%2BmHeLY6wLAbJyuLhJ8j%2FWI7iaSXGbU1fPJcAqI%2BlvXjwgvw7jxEfj7m6ZmN9rpmN6jFMMM707yJjyIeSiNmim3w0btvQMcE1d8QYaB4tnhg3uP0XAwABh5BxByD2urMHfwykHyAqbgWAgN0gg3p9hmyMfkOEBPFlS4l4MErjMZzQqvQBAX1cjpaJlAzlB5TV2GYU%2FYfpsMf6JimpqZaBUKSK9oXi%2FmhRqdPW2ZmN8QRCzAZcMp1b2n7NqkRVRrhWgiERfEuiC6NnyH%2FjrROcRsu9%2BQs4Hbju42LUKsGeae65m6Vvmt37pdXdqW3mCdLud3KOmSfpXAYAXneIPHZn0sdya93EAc7RZ6r5tib6xBaRH6%2BeMN8GTtGGZNwXRQDNBl3JT2XAqQuXVwKKZ3i3d3QyHwQ%2B7TRW2flw8%2B152LkOKjSaQDBUJfyXZVkaCLhUjCCsECXvIfd0ZtdgXlUQOBWT5fR1BbTrLwjCk7ALMK8uenuZqd0iM4rh5kTTrG30aod4BTDftzwZW0RXGQCXmxM9M%2BvB%2BMM%2FU4cQGOqUBzn%2FgDKfmiZab14gOIYYJAJ2%2FFL6JNrGTQWhKBuxqYgKzSWiIU856moSEkTX6fsZAoDoom4jSXsdeXD4qvTBZu%2B6%2Fu4I3qm9Hv60Y5yxo6wNZ0ZZPPdNSWlK%2F8jOxV2kGCWAOwDzmKHWBiUlp5NdUt5jR%2FVP62W8VhcocGBwPX4DGTlFgA1%2Fv082VHJnjQTsXiruCjlW4%2FN3irhe6j8vASQKjdwkf&X-Amz-Signature=c8bf99a0782363d600d7fcb9869c6eaf882df8a10743a5bffbbf94c5fa267525&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
