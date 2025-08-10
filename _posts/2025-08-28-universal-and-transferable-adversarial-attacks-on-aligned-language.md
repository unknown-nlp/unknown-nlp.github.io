---
categories:
  - paper-reviews
date: "2025-08-28 00:00:00"
description: 논문 리뷰
giscus_comments: true
layout: post
related_posts: false
slug: 2025-08-28-universal-and-transferable-adversarial-attacks-on-aligned-language
tags:
  - alignment
  - gpt
  - language-model
  - llm
  - paper-review
  - rlhf
title: Universal and Transferable Adversarial Attacks on Aligned Language Models
---

**논문 정보**

- **Date**: 2025-04-15
- **Reviewer**: 건우 김

**_23년도 12월에 출판된 논문이라 살짝 outdated 되어있는 점도 있지만, 유용한 내용이 많아서 공유드림._**

# Abstract

- 이때 당시 LLM은 부적절하거나 문제가 될 수 있는 콘텐츠를 생성할 가능성이 있어 alignment에 집중함.

- 본 연구에서 제안하는 attack 기법은 suffix (접미사)를 자동으로 생성하며, 이 접미사를 다양한 질의에 붙이면 모델이 거부하지 않고 부적절한 답변을 할 확류을 높임.

- 생성된 adversarial suffix는 다양한 모델과 상황에 높은 transferabiltiy를 보여줌

# 1. Introduction

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/986e7394-0405-4eb3-a333-f9d167f3e1c6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4FG6YIW%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHIYX4TQUdBldB%2FviVUpTA8siwKTFqBpv8Psb7UIBOXUAiAdYzHFCA0NgGMtPNeJUpxmPNrGqTgsRCijWLr6P%2Bq0KiqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMasupI32%2FfQrlZaVvKtwDnJEEm7PgKGKSaBcwFsDUjYZkpoyJNwXp0KWeFNmsd1FjULCoATLl4EPCTEnnGyMyT1IuL90aSgFZSN2DxYK4jXNCa12P0CE7aIh3uSCkmPAclKBk3L8j16SsGRqX5LTonwVhnRn4cWMw3Kt00uNWo374rOBvlUnLljYpy4mUNEYSpP%2BMoXf0qWVlNp6VmOOr3yYSYJHou4NIGPyGqTQ4aFPLmwBL5Iu5UvlWfP8Ka6qx9%2BULlOn8WFF%2BHk%2B7%2FT%2Fi6fkoLIEOwgNvkMIVX5D6qUQ%2FfmdA%2B7lyOzS7dkx8nqT%2FzZQFDobqu7staHcnaPjkNwrCdiwzEEcHWGmRGDTEYd018rSNjKqeglqRhOl4hM6NWK4rbGUrECFyl68Y1PO4ZDw1rF2%2FmMw083kMqihzO6pNv3Taomn2QUvUdg4qJuS6WedekqZRrLtqHF2AQVNmJnWFzliDUP0vBrQVAjF3sQ043%2FJzviYMZjtFDISVjD5O20Yg5oChEHdvm7c%2BFOgJ%2Bx0vAtBpBAsdVO9A3bJKf8xsinPci7z6TePD%2BZPjkw7UA7z%2FHoeNXDqVwzYbYzAfv8rrtB7aDfPx4DEB4Lb73%2F2xE0nZxdFYFqlGePsGW4ne9WEoPrAsksXNZScwqtPhxAY6pgGpLfjG%2B%2F1WJNth%2FKTN6LCYgBMCqQbOoQwy6ChhCzhhjaqRdeXkCHgBZGEiczvqXwTN2d%2BM6S2ewQEnjlHnP%2FaEp%2BC37%2FFs4epJ9cc47LrD90MLt167vDPG%2BzEwvjP%2F6Ty6KuibavaQ0mAhKdDLy%2BGcjUaTmHl8HjR8xFjABUfROnagOSLRtYtfa%2FUmZGo6vm16rH4uDAVBFZR70o8nKi8lW9Iwa2Z3&X-Amz-Signature=0853f7863501645f666baa07d014abc9d59a09527819b82825cd701fb8134e55&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- LLMs들이 large corpus로 학습될 때, 학습 데이터 안에는 유해한 콘텐츠도 포함되어 있음. 이를 방지하기 위해 alignment 기법이 도임되었고 (ex. RLHF), 결과적으로 사용자 질의에 대해 부적절한 답변을 생성하는 것을 제어하는데 어느 정도 성공함.

- 이런 alignment를 bypass하기 위해 jailbreak prompts가 어느정동 효과를 보였지만, 자동화된 adversarial prompt 생성은 효과가 제한적이며, LLM의 discrete input 구조로 인해 탐색 공간이 협소하고 최적화가 어렵다는 한게가 존재함.

- 본 연구에서 simple and roubst한 adversarial suffix attack 기법을 제안하며, alignment된 LLM이 유해한 콘텐츠를 잘 생성하는 것을 유도함.

# 2. A Universal Attack on LLMs

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/54200707-fc30-4a21-94db-4b96d2d0b4dc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4FG6YIW%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHIYX4TQUdBldB%2FviVUpTA8siwKTFqBpv8Psb7UIBOXUAiAdYzHFCA0NgGMtPNeJUpxmPNrGqTgsRCijWLr6P%2Bq0KiqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMasupI32%2FfQrlZaVvKtwDnJEEm7PgKGKSaBcwFsDUjYZkpoyJNwXp0KWeFNmsd1FjULCoATLl4EPCTEnnGyMyT1IuL90aSgFZSN2DxYK4jXNCa12P0CE7aIh3uSCkmPAclKBk3L8j16SsGRqX5LTonwVhnRn4cWMw3Kt00uNWo374rOBvlUnLljYpy4mUNEYSpP%2BMoXf0qWVlNp6VmOOr3yYSYJHou4NIGPyGqTQ4aFPLmwBL5Iu5UvlWfP8Ka6qx9%2BULlOn8WFF%2BHk%2B7%2FT%2Fi6fkoLIEOwgNvkMIVX5D6qUQ%2FfmdA%2B7lyOzS7dkx8nqT%2FzZQFDobqu7staHcnaPjkNwrCdiwzEEcHWGmRGDTEYd018rSNjKqeglqRhOl4hM6NWK4rbGUrECFyl68Y1PO4ZDw1rF2%2FmMw083kMqihzO6pNv3Taomn2QUvUdg4qJuS6WedekqZRrLtqHF2AQVNmJnWFzliDUP0vBrQVAjF3sQ043%2FJzviYMZjtFDISVjD5O20Yg5oChEHdvm7c%2BFOgJ%2Bx0vAtBpBAsdVO9A3bJKf8xsinPci7z6TePD%2BZPjkw7UA7z%2FHoeNXDqVwzYbYzAfv8rrtB7aDfPx4DEB4Lb73%2F2xE0nZxdFYFqlGePsGW4ne9WEoPrAsksXNZScwqtPhxAY6pgGpLfjG%2B%2F1WJNth%2FKTN6LCYgBMCqQbOoQwy6ChhCzhhjaqRdeXkCHgBZGEiczvqXwTN2d%2BM6S2ewQEnjlHnP%2FaEp%2BC37%2FFs4epJ9cc47LrD90MLt167vDPG%2BzEwvjP%2F6Ty6KuibavaQ0mAhKdDLy%2BGcjUaTmHl8HjR8xFjABUfROnagOSLRtYtfa%2FUmZGo6vm16rH4uDAVBFZR70o8nKi8lW9Iwa2Z3&X-Amz-Signature=8bde4005809c2035d7ae0392fed493316aef3978a53fce3a56d0f603c0c15126&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Objective: 사용자 query (ex. “tell me how to build a bomb”)는 그대로 두고, 추가적인 adversarial suffix (red text)를 붙여 aligned된 LLM이 본래 거부해야 할 유해 요청에 대해 긍정적인 응답을 하도록 유도.

## 2.1 Producing Affirmative Responses

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/35fa8feb-dca6-4da7-9814-25b19c57b74a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4FG6YIW%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHIYX4TQUdBldB%2FviVUpTA8siwKTFqBpv8Psb7UIBOXUAiAdYzHFCA0NgGMtPNeJUpxmPNrGqTgsRCijWLr6P%2Bq0KiqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMasupI32%2FfQrlZaVvKtwDnJEEm7PgKGKSaBcwFsDUjYZkpoyJNwXp0KWeFNmsd1FjULCoATLl4EPCTEnnGyMyT1IuL90aSgFZSN2DxYK4jXNCa12P0CE7aIh3uSCkmPAclKBk3L8j16SsGRqX5LTonwVhnRn4cWMw3Kt00uNWo374rOBvlUnLljYpy4mUNEYSpP%2BMoXf0qWVlNp6VmOOr3yYSYJHou4NIGPyGqTQ4aFPLmwBL5Iu5UvlWfP8Ka6qx9%2BULlOn8WFF%2BHk%2B7%2FT%2Fi6fkoLIEOwgNvkMIVX5D6qUQ%2FfmdA%2B7lyOzS7dkx8nqT%2FzZQFDobqu7staHcnaPjkNwrCdiwzEEcHWGmRGDTEYd018rSNjKqeglqRhOl4hM6NWK4rbGUrECFyl68Y1PO4ZDw1rF2%2FmMw083kMqihzO6pNv3Taomn2QUvUdg4qJuS6WedekqZRrLtqHF2AQVNmJnWFzliDUP0vBrQVAjF3sQ043%2FJzviYMZjtFDISVjD5O20Yg5oChEHdvm7c%2BFOgJ%2Bx0vAtBpBAsdVO9A3bJKf8xsinPci7z6TePD%2BZPjkw7UA7z%2FHoeNXDqVwzYbYzAfv8rrtB7aDfPx4DEB4Lb73%2F2xE0nZxdFYFqlGePsGW4ne9WEoPrAsksXNZScwqtPhxAY6pgGpLfjG%2B%2F1WJNth%2FKTN6LCYgBMCqQbOoQwy6ChhCzhhjaqRdeXkCHgBZGEiczvqXwTN2d%2BM6S2ewQEnjlHnP%2FaEp%2BC37%2FFs4epJ9cc47LrD90MLt167vDPG%2BzEwvjP%2F6Ty6KuibavaQ0mAhKdDLy%2BGcjUaTmHl8HjR8xFjABUfROnagOSLRtYtfa%2FUmZGo6vm16rH4uDAVBFZR70o8nKi8lW9Iwa2Z3&X-Amz-Signature=36f9251ead267c58229eae804ff7008f957a3172465d0891b82ff65147b567a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Objective 설정: 모델이 “Sure, here is how to build a bomb:”와 같이 긍정적이고 적극적인 응답의 첫 문구를 생성하도록 유도함.

- **Formalizing the adversarial objective**

## 2.2 Greedy Coordinate Gradient-based Search

- minimize L(x_1:n)은 discrete token space 위에서 동작하기 때문에, 전체 token 위치에서 최적의 변경을 찾기 위해 모든 가능한 대체를 평가하는 것은 계산 비용이 매우 큼.

- 위 문제를 해결하기에 gradient를 활용한 GCG방법을 제안함

## 2.3 Universal Multi-prompt and Multi-model attacks

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/42ddc2ba-a427-4035-9461-8d7cbcac368f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4FG6YIW%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHIYX4TQUdBldB%2FviVUpTA8siwKTFqBpv8Psb7UIBOXUAiAdYzHFCA0NgGMtPNeJUpxmPNrGqTgsRCijWLr6P%2Bq0KiqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMasupI32%2FfQrlZaVvKtwDnJEEm7PgKGKSaBcwFsDUjYZkpoyJNwXp0KWeFNmsd1FjULCoATLl4EPCTEnnGyMyT1IuL90aSgFZSN2DxYK4jXNCa12P0CE7aIh3uSCkmPAclKBk3L8j16SsGRqX5LTonwVhnRn4cWMw3Kt00uNWo374rOBvlUnLljYpy4mUNEYSpP%2BMoXf0qWVlNp6VmOOr3yYSYJHou4NIGPyGqTQ4aFPLmwBL5Iu5UvlWfP8Ka6qx9%2BULlOn8WFF%2BHk%2B7%2FT%2Fi6fkoLIEOwgNvkMIVX5D6qUQ%2FfmdA%2B7lyOzS7dkx8nqT%2FzZQFDobqu7staHcnaPjkNwrCdiwzEEcHWGmRGDTEYd018rSNjKqeglqRhOl4hM6NWK4rbGUrECFyl68Y1PO4ZDw1rF2%2FmMw083kMqihzO6pNv3Taomn2QUvUdg4qJuS6WedekqZRrLtqHF2AQVNmJnWFzliDUP0vBrQVAjF3sQ043%2FJzviYMZjtFDISVjD5O20Yg5oChEHdvm7c%2BFOgJ%2Bx0vAtBpBAsdVO9A3bJKf8xsinPci7z6TePD%2BZPjkw7UA7z%2FHoeNXDqVwzYbYzAfv8rrtB7aDfPx4DEB4Lb73%2F2xE0nZxdFYFqlGePsGW4ne9WEoPrAsksXNZScwqtPhxAY6pgGpLfjG%2B%2F1WJNth%2FKTN6LCYgBMCqQbOoQwy6ChhCzhhjaqRdeXkCHgBZGEiczvqXwTN2d%2BM6S2ewQEnjlHnP%2FaEp%2BC37%2FFs4epJ9cc47LrD90MLt167vDPG%2BzEwvjP%2F6Ty6KuibavaQ0mAhKdDLy%2BGcjUaTmHl8HjR8xFjABUfROnagOSLRtYtfa%2FUmZGo6vm16rH4uDAVBFZR70o8nKi8lW9Iwa2Z3&X-Amz-Signature=7dafa6a53563d82efd7d19a4bac9ea901a5fc6fe24c4110d65e76cf555944600&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

단일 prompt가 아닌 다양한 prompt에 저굥 가능한 GCG를 확장시켜 universal attack을 제안함.

- objective: 단 하나의 adeversarial suffix p_1:l로 유해한 prompt에 대해 공통적으로 잘 작동하기

- 동일한 tokenizer를 사용하면, gradient는 같은 차원의 공간 R^V에 존재하기 때문에, 별다른 변환 없이 합산 할 수 있음 (ex. Vicuna-7B, 13B를 동시에 최적화 할 수 있음)

# 3. Experimental Results: Direct and Transfer Attack

### Dataset

본 연구에서 제안한 새로운 밴치마큰 AdvBench

- Harmful strings: 500개 유해한 텍스트를 포함한 문장으로 구성됨.

- Harmful Behaviors: 500개 유해 행동 지시문 (ex. how to build a bomb?)

### Metrics

- ASR (Attack Success Rate): 성공률 측정

- Harmful Strings: 정확히 해당 string을 출력했는지 확인

- Harmful Behaviors: 모델이 지시를 거부하지 않고 따르려는 시도를 했는지 확인 (사람이 평가)

## 3.1 Attacks on White-box Models

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/fe2e81de-18d5-45e6-be8f-421accea0211/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4FG6YIW%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHIYX4TQUdBldB%2FviVUpTA8siwKTFqBpv8Psb7UIBOXUAiAdYzHFCA0NgGMtPNeJUpxmPNrGqTgsRCijWLr6P%2Bq0KiqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMasupI32%2FfQrlZaVvKtwDnJEEm7PgKGKSaBcwFsDUjYZkpoyJNwXp0KWeFNmsd1FjULCoATLl4EPCTEnnGyMyT1IuL90aSgFZSN2DxYK4jXNCa12P0CE7aIh3uSCkmPAclKBk3L8j16SsGRqX5LTonwVhnRn4cWMw3Kt00uNWo374rOBvlUnLljYpy4mUNEYSpP%2BMoXf0qWVlNp6VmOOr3yYSYJHou4NIGPyGqTQ4aFPLmwBL5Iu5UvlWfP8Ka6qx9%2BULlOn8WFF%2BHk%2B7%2FT%2Fi6fkoLIEOwgNvkMIVX5D6qUQ%2FfmdA%2B7lyOzS7dkx8nqT%2FzZQFDobqu7staHcnaPjkNwrCdiwzEEcHWGmRGDTEYd018rSNjKqeglqRhOl4hM6NWK4rbGUrECFyl68Y1PO4ZDw1rF2%2FmMw083kMqihzO6pNv3Taomn2QUvUdg4qJuS6WedekqZRrLtqHF2AQVNmJnWFzliDUP0vBrQVAjF3sQ043%2FJzviYMZjtFDISVjD5O20Yg5oChEHdvm7c%2BFOgJ%2Bx0vAtBpBAsdVO9A3bJKf8xsinPci7z6TePD%2BZPjkw7UA7z%2FHoeNXDqVwzYbYzAfv8rrtB7aDfPx4DEB4Lb73%2F2xE0nZxdFYFqlGePsGW4ne9WEoPrAsksXNZScwqtPhxAY6pgGpLfjG%2B%2F1WJNth%2FKTN6LCYgBMCqQbOoQwy6ChhCzhhjaqRdeXkCHgBZGEiczvqXwTN2d%2BM6S2ewQEnjlHnP%2FaEp%2BC37%2FFs4epJ9cc47LrD90MLt167vDPG%2BzEwvjP%2F6Ty6KuibavaQ0mAhKdDLy%2BGcjUaTmHl8HjR8xFjABUfROnagOSLRtYtfa%2FUmZGo6vm16rH4uDAVBFZR70o8nKi8lW9Iwa2Z3&X-Amz-Signature=a8c18232a785ecd97e4b91f747523ebca71c791ca71a4256b89dd0b93e0478d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- **1 behavior / string, 1 model**: 공격 기법들이 하나의 유해 질의에 대해 얼마나 잘 응답을 유도하는지 평가

- 25 behaviors, 1 model: 하나의 suffix로 다수 유해 behaviors에 대한 ASR 평가

## 3.2 Transfer Attacks

본 실험에서는 하나의 attack prompt가 여러 model에도 효과적인지 평가함

25개 harmful behaviors를 2~4개 models에 대해서 동시에 GCG로 최적화 진행함

**Baselines**

1. Prompt only

1. “Sure, here’s”: (수동 jailbreak 기법)

1. GCG Prompt

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/cf26dd77-7f3f-4dea-b8f9-c391acf2009c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4FG6YIW%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHIYX4TQUdBldB%2FviVUpTA8siwKTFqBpv8Psb7UIBOXUAiAdYzHFCA0NgGMtPNeJUpxmPNrGqTgsRCijWLr6P%2Bq0KiqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMasupI32%2FfQrlZaVvKtwDnJEEm7PgKGKSaBcwFsDUjYZkpoyJNwXp0KWeFNmsd1FjULCoATLl4EPCTEnnGyMyT1IuL90aSgFZSN2DxYK4jXNCa12P0CE7aIh3uSCkmPAclKBk3L8j16SsGRqX5LTonwVhnRn4cWMw3Kt00uNWo374rOBvlUnLljYpy4mUNEYSpP%2BMoXf0qWVlNp6VmOOr3yYSYJHou4NIGPyGqTQ4aFPLmwBL5Iu5UvlWfP8Ka6qx9%2BULlOn8WFF%2BHk%2B7%2FT%2Fi6fkoLIEOwgNvkMIVX5D6qUQ%2FfmdA%2B7lyOzS7dkx8nqT%2FzZQFDobqu7staHcnaPjkNwrCdiwzEEcHWGmRGDTEYd018rSNjKqeglqRhOl4hM6NWK4rbGUrECFyl68Y1PO4ZDw1rF2%2FmMw083kMqihzO6pNv3Taomn2QUvUdg4qJuS6WedekqZRrLtqHF2AQVNmJnWFzliDUP0vBrQVAjF3sQ043%2FJzviYMZjtFDISVjD5O20Yg5oChEHdvm7c%2BFOgJ%2Bx0vAtBpBAsdVO9A3bJKf8xsinPci7z6TePD%2BZPjkw7UA7z%2FHoeNXDqVwzYbYzAfv8rrtB7aDfPx4DEB4Lb73%2F2xE0nZxdFYFqlGePsGW4ne9WEoPrAsksXNZScwqtPhxAY6pgGpLfjG%2B%2F1WJNth%2FKTN6LCYgBMCqQbOoQwy6ChhCzhhjaqRdeXkCHgBZGEiczvqXwTN2d%2BM6S2ewQEnjlHnP%2FaEp%2BC37%2FFs4epJ9cc47LrD90MLt167vDPG%2BzEwvjP%2F6Ty6KuibavaQ0mAhKdDLy%2BGcjUaTmHl8HjR8xFjABUfROnagOSLRtYtfa%2FUmZGo6vm16rH4uDAVBFZR70o8nKi8lW9Iwa2Z3&X-Amz-Signature=95ee2fced6ea6ffc7806f33c11876d2c3757735f1f99aa2f339686992a046c0e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- GCG는 대부분 모델에서 ASR 80~100% 수준을 보여줌

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/e78ff324-4b41-4921-b225-30506e96e10a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4FG6YIW%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHIYX4TQUdBldB%2FviVUpTA8siwKTFqBpv8Psb7UIBOXUAiAdYzHFCA0NgGMtPNeJUpxmPNrGqTgsRCijWLr6P%2Bq0KiqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMasupI32%2FfQrlZaVvKtwDnJEEm7PgKGKSaBcwFsDUjYZkpoyJNwXp0KWeFNmsd1FjULCoATLl4EPCTEnnGyMyT1IuL90aSgFZSN2DxYK4jXNCa12P0CE7aIh3uSCkmPAclKBk3L8j16SsGRqX5LTonwVhnRn4cWMw3Kt00uNWo374rOBvlUnLljYpy4mUNEYSpP%2BMoXf0qWVlNp6VmOOr3yYSYJHou4NIGPyGqTQ4aFPLmwBL5Iu5UvlWfP8Ka6qx9%2BULlOn8WFF%2BHk%2B7%2FT%2Fi6fkoLIEOwgNvkMIVX5D6qUQ%2FfmdA%2B7lyOzS7dkx8nqT%2FzZQFDobqu7staHcnaPjkNwrCdiwzEEcHWGmRGDTEYd018rSNjKqeglqRhOl4hM6NWK4rbGUrECFyl68Y1PO4ZDw1rF2%2FmMw083kMqihzO6pNv3Taomn2QUvUdg4qJuS6WedekqZRrLtqHF2AQVNmJnWFzliDUP0vBrQVAjF3sQ043%2FJzviYMZjtFDISVjD5O20Yg5oChEHdvm7c%2BFOgJ%2Bx0vAtBpBAsdVO9A3bJKf8xsinPci7z6TePD%2BZPjkw7UA7z%2FHoeNXDqVwzYbYzAfv8rrtB7aDfPx4DEB4Lb73%2F2xE0nZxdFYFqlGePsGW4ne9WEoPrAsksXNZScwqtPhxAY6pgGpLfjG%2B%2F1WJNth%2FKTN6LCYgBMCqQbOoQwy6ChhCzhhjaqRdeXkCHgBZGEiczvqXwTN2d%2BM6S2ewQEnjlHnP%2FaEp%2BC37%2FFs4epJ9cc47LrD90MLt167vDPG%2BzEwvjP%2F6Ty6KuibavaQ0mAhKdDLy%2BGcjUaTmHl8HjR8xFjABUfROnagOSLRtYtfa%2FUmZGo6vm16rH4uDAVBFZR70o8nKi8lW9Iwa2Z3&X-Amz-Signature=b2f4099bf9ab2b0fd596351ecd46bd100ce39ee9049b4eb53237b78dba214b65&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Proprietary models에 대해서는 Claude-2를 제외하고 어느정도 유의미한 ASR을 보여줌

- Concatenate: 서로 다른 GCG Prompt 3개를 하나로 연결해서 suffix로 사용

- Ensemble: 여러 GCG prompt만 시도하면서 성공한 것만 사용

## 3.3 Discussion

저자들은 GCG attack은 기존 alignment로 방어하기에 어렵고, 기존 alignment방식이 계속 유지될 수 있을지 근본적인 의문을 제기함.

**Are models becoming more robust through alignment? **

- GPT-4, Claude2는 GPT-3.5보다 ASR이 낮음 → 최근 alignment의 effectiveness로 보여질 수 있으나 주의할 점은 다음과 같음

**Are the attacks meaningful?**

- Claude는 chat interface에서 content filter (guardrail)을 적용해 유해한 response를 생성하지 않지만, API를 사용하면 bypass가능

- 초기 prompt의 단어를 바꾸는 간단한 조작으로 filter 역시 우회 가능

**Why did these attacks not yet exist?**

# Conclusion

- 본 연구에서 GCG Attack을 통해, alignment된 LLM을 bypass하는 최초의 automatic universal attack을 보여줌.

- Trasnferabiltiy도 강하게 보여주고, 기존 수작업 jailbreak보다 효과적임

- 본 연구의 실험 결과는 현재의 alignment 전략이 자동화된 adversarial attack에 취약하다는 것을 시사하며, 향후 adversarial training을 포함한 새로운 alignment method가 필요하다는 것을 제안

- 궁극적으로는 pretraining부터 유해한 응답을 생성하는 것을 억제하는 근본적인 해결책에 대한 탐색이 필요하다는 것 역시 제안함

아래 repo보면 nanoGCG로 매우 쉽게 구현할 수 있음.

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/348e3ff2-81a0-4799-b98d-05176d26e7e4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4FG6YIW%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHIYX4TQUdBldB%2FviVUpTA8siwKTFqBpv8Psb7UIBOXUAiAdYzHFCA0NgGMtPNeJUpxmPNrGqTgsRCijWLr6P%2Bq0KiqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMasupI32%2FfQrlZaVvKtwDnJEEm7PgKGKSaBcwFsDUjYZkpoyJNwXp0KWeFNmsd1FjULCoATLl4EPCTEnnGyMyT1IuL90aSgFZSN2DxYK4jXNCa12P0CE7aIh3uSCkmPAclKBk3L8j16SsGRqX5LTonwVhnRn4cWMw3Kt00uNWo374rOBvlUnLljYpy4mUNEYSpP%2BMoXf0qWVlNp6VmOOr3yYSYJHou4NIGPyGqTQ4aFPLmwBL5Iu5UvlWfP8Ka6qx9%2BULlOn8WFF%2BHk%2B7%2FT%2Fi6fkoLIEOwgNvkMIVX5D6qUQ%2FfmdA%2B7lyOzS7dkx8nqT%2FzZQFDobqu7staHcnaPjkNwrCdiwzEEcHWGmRGDTEYd018rSNjKqeglqRhOl4hM6NWK4rbGUrECFyl68Y1PO4ZDw1rF2%2FmMw083kMqihzO6pNv3Taomn2QUvUdg4qJuS6WedekqZRrLtqHF2AQVNmJnWFzliDUP0vBrQVAjF3sQ043%2FJzviYMZjtFDISVjD5O20Yg5oChEHdvm7c%2BFOgJ%2Bx0vAtBpBAsdVO9A3bJKf8xsinPci7z6TePD%2BZPjkw7UA7z%2FHoeNXDqVwzYbYzAfv8rrtB7aDfPx4DEB4Lb73%2F2xE0nZxdFYFqlGePsGW4ne9WEoPrAsksXNZScwqtPhxAY6pgGpLfjG%2B%2F1WJNth%2FKTN6LCYgBMCqQbOoQwy6ChhCzhhjaqRdeXkCHgBZGEiczvqXwTN2d%2BM6S2ewQEnjlHnP%2FaEp%2BC37%2FFs4epJ9cc47LrD90MLt167vDPG%2BzEwvjP%2F6Ty6KuibavaQ0mAhKdDLy%2BGcjUaTmHl8HjR8xFjABUfROnagOSLRtYtfa%2FUmZGo6vm16rH4uDAVBFZR70o8nKi8lW9Iwa2Z3&X-Amz-Signature=931160c22d397c29516b503a1d48aee6bef25f13e6032a6728c5613f6bcd2cdb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
