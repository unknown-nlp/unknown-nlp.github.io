---
categories:
- paper-reviews
date: '2025-04-08 00:00:00'
description: 논문 리뷰
giscus_comments: true
layout: post
related_posts: false
tags:
- language-model
- llm
- paper-review
- reasoning
thumbnail: assets/img/posts/2025-04-08-on-the-biology-of-a-large-language-model/thumbnail.jpg
title: On the Biology of a Large Language Model
---

**논문 정보**
- **Date**: 2025-04-08
- **Reviewer**: hyowon Cho

오늘 소개할 논문은 Anthropic에서 3월 27일 낸 따끈따끈한 신상입니다. 

개인적으로 느끼기에는 LLM의 동작 원리에 대한 내부 분석을 할거면 이렇게 해라라는 바이블같은 논문인 것 같습니다,, 단순하지만 확실한 변인 통제를 한다는 점에서 재미있었어요!
실험이 너무 많아서, 전체를 다 가져오지는 못했지만 최대한 많이 가져왔습니당

한번 보시죠

# Introduction

대형 언어 모델은 놀라운 능력을 보여주고 있다. 하지만 이러한 능력이 **어떻게 작동하는지에 대한 메커니즘은 대부분 밝혀지지 않았다**.

본 연구는 **모델 내부가 어떻게 작동하는지 역설계함으로써**, 이들을 더 깊이 이해하고, 주어진 목적에 적합한지를 평가할 수 있는 기반을 마련하는 것을 목표로 한다.

최근 다양한 연구팀들은 언어 모델 내부를 탐색하기 위한 도구들을 개발해왔으며, 이 과정에서 모델 내부에는 **해석 가능한 개념 표현**, 즉 ‘기능(feature)’이 존재한다는 사실이 밝혀졌다. 우리가 세포를 생물학적 시스템의 기본 단위로 보듯, **이러한 기능들이 모델 내부 계산의 기본 단위**라고 가정할 수 있다.

하지만 저자들은 이 기능들을 단순히 식별하는 것만으로는 충분하지 않다고 이야기하며, 그들이 **어떻게 상호작용하는지**를 이해해야만 모델의 작동 원리를 파악할 수 있다고 말한다. 

본 연구는 동반 논문 *Circuit Tracing*에서 제안한, **기능들 사이의 연결 관계를 추적하는 도구인 어트리뷰션 그래프**를 이용해 분석을 진행한다. 이 그래프는 모델이 특정 입력 프롬프트를 출력으로 변환하는 중간 단계를 부분적으로 추적할 수 있게 해주기에, **모델의 내부 메커니즘을 실험을 통해 검증할 수 있다. **

본 논문에서는 2024년 10월 공개된** Claude 3.5 Haiku**를 분석 대상으로 삼아 어트리뷰션 그래프를 적용하였다. 분석 대상들은 다음과 같다:

1. **Introductory Example: Multi-step Reasoning.** 

1. **Planning in Poems.** 

1. **Multilingual Circuits.**** **

1. **Addition.** 

1. **Medical Diagnoses****. **

1. **Entity Recognition and Hallucinations.** 

1. **Refusal of Harmful Requests.** 

1. **An Analysis of a Jailbreak.** 

1. **Chain-of-thought Faithfulness.** 

1. **A Model with a Hidden Goal.** 

결론적으로 Claude 3.5 Haiku는 다음과 같은 전략들을 실제로 활용하고 있다:

- 다단계 추론을 내부에서 수행

- 사전 계획 및 역방향 계획(backward planning) 사용

- 자신이 무엇을 알고 무엇을 모르는지 인식하는 메타인지적 회로

- 매우 추상화된 내부 계산 구조가 다양한 맥락에서 일반화

또한, 이러한 방법은 **응답에 드러나지 않는 위험한 사고 과정**을 감지하는 데에도 유용하게 쓰일 수 있다.

## 한계

어트리뷰션 그래프는 모든 프롬프트에 적용 가능한 것은 아니다. 시도한 프롬프트 중 약 25%에서 유의미한 통찰을 얻을 수 있었고, 이 논문에 소개된 예시는 그중 성공적인 사례들이다.

게다가, 분석은 모델 자체가 아닌 보다 해석 가능한 'replacement model,'을 활용해 간접적으로 수행되었기에, 불완전성과 왜곡 가능성이 존재한다.

# **Method: Circuit Tracing**

### Building an Interpretable Replacement Model

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/1ac90084-0057-484a-a4f7-cd47b1f0dc7b/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-04-07_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_8.24.35.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRAABYAO%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIET6GAb%2FwgPsK%2BHBHQbfSm2VIITT192qEa5KOBIT3ZHgAiA5ov9pllg2Om8qbbuJ%2FAahoXNIaBjHHz0dHLNTqDQHjSqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxc0I89fxq7Xz6sz%2FKtwDLJ%2FR%2Bu3VH51K0yyJt4Ph2ZBcGMdjHstVSzeAfcawdpBJT5Q8YnWuDijB8tZINF%2FJV5%2BW5jl20UIGyz1XNSFe627L4hnpHaXR20rRHK8Y2dJnRII42OuwPY23oXbRwduMRBEtOYpilI6DtiUXHIZxJawHqu89ih%2BQEvijtXgU0NvMZF8YB1if5ilzntBVFj1YTNjCAhkdhYnxi0mr2Zqc9mVMLHQn%2BgzBgn0Tz3YYb9Q81tRSUnN3OKqqUZJPwhwkePgBoFKz%2BCWrO%2F3NAg4xsypnsQhJOtzCJnyUQ%2FCd%2BFeOE7%2FBk0g7kQ5Oy3SEV8yQa%2BKt%2F1fttvau3n5jCNKEypoaNH9cP4%2B%2FxIf9bNEJQCQkO%2FMYkliTHO8OQN5bn8AAUiOzPME6kOpq5nIrE6jC9p2Oete%2F6jkKl%2FKL0S0xldvV6QuGpXV8fOvisZyHUx3o1KSt2qTu8Os7QT892B5VbGN7jMnINg%2FcMjg8ZzhQirsK1ZznSPBOmS1ZBtT4DN%2BVWTDkeGzHGvzpPqIkjnFKgIOB2NwDit%2BH3EA8LL3YVXeHKe7x8M%2BmXG9tFobTHb579EB5LkEk7KPLSuNvLC%2FDujr8xP%2BwszFjhUgIMDCH9cCOBHU4mYq43e4ZwHQwzv7hxAY6pgENxvjXxa5F7jl7a6s8RuslkXaxDVBKRPTJKvvznGT%2F6xFGseR%2FTL6vYcAeKlsnoeftBp5TljHBJuS6WpS%2FSn7swqkzASjsmBniAgcsgXH%2FNwwjjB%2BfDd4CNZw1Mrxx3RFs%2B3TsTQ3LorpUrm6ndtw4kgYgf5Zlr0r9AzaGDSy31ChXUG6JPugFRp3FmTO8vEytKTjtinXjKDaotjkpCFNPDBi4ECvr&X-Amz-Signature=28c3435d951ce64f836e6e9dfd589b857491f7da06177fc66d93f6851c9d3869&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- **원래 트랜스포머 모델**:

- **대체 모델**:

모델을 해석하기 어려운 이유 중 하나는 뉴런들이 다의적(polysemantic)이라는 점이다. 즉, 개별 뉴런이 서로 관련 없어 보이는 여러 기능을 동시에 수행한다는 뜻.

이를 해결하기 위해, 저자들은 원래 모델의 활성값을 근사 재현하면서도 해석 가능한 구성요소로 이루어진 ‘대체 모델(replacement model)’을 만든다. 

이 대체 모델은 **CLT(Cross-Layer Transcoder)** 아키텍처에 기반하며, 원래의 MLP 뉴런을 희소하게 활성화되는 해석 가능한 기능(feature)들로 대체한다. 본 논문에서 사용한 CLT는 모든 레이어에 걸쳐 총 3천만 개의 기능을 갖고 있다.

1. **Architecture (구조)**

1. **From Cross-Layer Transcoder to Replacement Model (CLT에서 대체 모델로)**

### Local Replacement Model and Attribution Graphs

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/e6689982-4950-4b6d-a226-e7e714a9e74c/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-04-07_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_8.24.48.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRAABYAO%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIET6GAb%2FwgPsK%2BHBHQbfSm2VIITT192qEa5KOBIT3ZHgAiA5ov9pllg2Om8qbbuJ%2FAahoXNIaBjHHz0dHLNTqDQHjSqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxc0I89fxq7Xz6sz%2FKtwDLJ%2FR%2Bu3VH51K0yyJt4Ph2ZBcGMdjHstVSzeAfcawdpBJT5Q8YnWuDijB8tZINF%2FJV5%2BW5jl20UIGyz1XNSFe627L4hnpHaXR20rRHK8Y2dJnRII42OuwPY23oXbRwduMRBEtOYpilI6DtiUXHIZxJawHqu89ih%2BQEvijtXgU0NvMZF8YB1if5ilzntBVFj1YTNjCAhkdhYnxi0mr2Zqc9mVMLHQn%2BgzBgn0Tz3YYb9Q81tRSUnN3OKqqUZJPwhwkePgBoFKz%2BCWrO%2F3NAg4xsypnsQhJOtzCJnyUQ%2FCd%2BFeOE7%2FBk0g7kQ5Oy3SEV8yQa%2BKt%2F1fttvau3n5jCNKEypoaNH9cP4%2B%2FxIf9bNEJQCQkO%2FMYkliTHO8OQN5bn8AAUiOzPME6kOpq5nIrE6jC9p2Oete%2F6jkKl%2FKL0S0xldvV6QuGpXV8fOvisZyHUx3o1KSt2qTu8Os7QT892B5VbGN7jMnINg%2FcMjg8ZzhQirsK1ZznSPBOmS1ZBtT4DN%2BVWTDkeGzHGvzpPqIkjnFKgIOB2NwDit%2BH3EA8LL3YVXeHKe7x8M%2BmXG9tFobTHb579EB5LkEk7KPLSuNvLC%2FDujr8xP%2BwszFjhUgIMDCH9cCOBHU4mYq43e4ZwHQwzv7hxAY6pgENxvjXxa5F7jl7a6s8RuslkXaxDVBKRPTJKvvznGT%2F6xFGseR%2FTL6vYcAeKlsnoeftBp5TljHBJuS6WpS%2FSn7swqkzASjsmBniAgcsgXH%2FNwwjjB%2BfDd4CNZw1Mrxx3RFs%2B3TsTQ3LorpUrm6ndtw4kgYgf5Zlr0r9AzaGDSy31ChXUG6JPugFRp3FmTO8vEytKTjtinXjKDaotjkpCFNPDBi4ECvr&X-Amz-Signature=82d8e856afaccb4395c170e60d650a805a0ac9b9ed7887c4d5ce682a1d047ce7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**The Local Replacement Model **

- **Local:** 특정 입력(prompt)에 대해 작동하는 작은 서브모델을 구성. 즉, 기존 모델의 모든 계산을 완전히 재현하는 건 불가능하기 때문에, **특정 문장 하나에 대해서만 작동하는 작은 모델 만들기**

- **목적**: 

- **보완기법**

**Constructing an Attribution Graph for a Prompt**

> 특정 입력 프롬프트에 대해, 모델이 어떻게 예측을 구성했는지 ‘그래프 구조’로 표현

- 구성 요소:

- 활용

- 라벨링

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/4bdad117-70b9-40b4-9d99-4eb0deed0025/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-04-07_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_8.24.55.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRAABYAO%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIET6GAb%2FwgPsK%2BHBHQbfSm2VIITT192qEa5KOBIT3ZHgAiA5ov9pllg2Om8qbbuJ%2FAahoXNIaBjHHz0dHLNTqDQHjSqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxc0I89fxq7Xz6sz%2FKtwDLJ%2FR%2Bu3VH51K0yyJt4Ph2ZBcGMdjHstVSzeAfcawdpBJT5Q8YnWuDijB8tZINF%2FJV5%2BW5jl20UIGyz1XNSFe627L4hnpHaXR20rRHK8Y2dJnRII42OuwPY23oXbRwduMRBEtOYpilI6DtiUXHIZxJawHqu89ih%2BQEvijtXgU0NvMZF8YB1if5ilzntBVFj1YTNjCAhkdhYnxi0mr2Zqc9mVMLHQn%2BgzBgn0Tz3YYb9Q81tRSUnN3OKqqUZJPwhwkePgBoFKz%2BCWrO%2F3NAg4xsypnsQhJOtzCJnyUQ%2FCd%2BFeOE7%2FBk0g7kQ5Oy3SEV8yQa%2BKt%2F1fttvau3n5jCNKEypoaNH9cP4%2B%2FxIf9bNEJQCQkO%2FMYkliTHO8OQN5bn8AAUiOzPME6kOpq5nIrE6jC9p2Oete%2F6jkKl%2FKL0S0xldvV6QuGpXV8fOvisZyHUx3o1KSt2qTu8Os7QT892B5VbGN7jMnINg%2FcMjg8ZzhQirsK1ZznSPBOmS1ZBtT4DN%2BVWTDkeGzHGvzpPqIkjnFKgIOB2NwDit%2BH3EA8LL3YVXeHKe7x8M%2BmXG9tFobTHb579EB5LkEk7KPLSuNvLC%2FDujr8xP%2BwszFjhUgIMDCH9cCOBHU4mYq43e4ZwHQwzv7hxAY6pgENxvjXxa5F7jl7a6s8RuslkXaxDVBKRPTJKvvznGT%2F6xFGseR%2FTL6vYcAeKlsnoeftBp5TljHBJuS6WpS%2FSn7swqkzASjsmBniAgcsgXH%2FNwwjjB%2BfDd4CNZw1Mrxx3RFs%2B3TsTQ3LorpUrm6ndtw4kgYgf5Zlr0r9AzaGDSy31ChXUG6JPugFRp3FmTO8vEytKTjtinXjKDaotjkpCFNPDBi4ECvr&X-Amz-Signature=85247d71539a5b5c21375cc671718d87bc24b6906bc80f76982ab6806bba518b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

모든 feature를 개별 노드로 두면 **그래프가 너무 복잡**해지고 해석이 어려움. 따라서, 비슷한 역할을 하는 feature들은 **슈퍼노드(supernode)**로 묶습니다. 예를 들어:

- ‘Texas’라는 개념을 포착하는 여러 기능들

- ‘수도를 말하기’ 관련 기능들

- ‘Austin’이라는 단어 생성을 유도하는 기능들

이러한 슈퍼노드는 **단순화된 그래프를 구성하는 핵심 단위**로 사용된다.

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/db918326-0941-44c0-ba71-e70192434d81/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-04-07_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_8.25.03.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRAABYAO%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIET6GAb%2FwgPsK%2BHBHQbfSm2VIITT192qEa5KOBIT3ZHgAiA5ov9pllg2Om8qbbuJ%2FAahoXNIaBjHHz0dHLNTqDQHjSqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxc0I89fxq7Xz6sz%2FKtwDLJ%2FR%2Bu3VH51K0yyJt4Ph2ZBcGMdjHstVSzeAfcawdpBJT5Q8YnWuDijB8tZINF%2FJV5%2BW5jl20UIGyz1XNSFe627L4hnpHaXR20rRHK8Y2dJnRII42OuwPY23oXbRwduMRBEtOYpilI6DtiUXHIZxJawHqu89ih%2BQEvijtXgU0NvMZF8YB1if5ilzntBVFj1YTNjCAhkdhYnxi0mr2Zqc9mVMLHQn%2BgzBgn0Tz3YYb9Q81tRSUnN3OKqqUZJPwhwkePgBoFKz%2BCWrO%2F3NAg4xsypnsQhJOtzCJnyUQ%2FCd%2BFeOE7%2FBk0g7kQ5Oy3SEV8yQa%2BKt%2F1fttvau3n5jCNKEypoaNH9cP4%2B%2FxIf9bNEJQCQkO%2FMYkliTHO8OQN5bn8AAUiOzPME6kOpq5nIrE6jC9p2Oete%2F6jkKl%2FKL0S0xldvV6QuGpXV8fOvisZyHUx3o1KSt2qTu8Os7QT892B5VbGN7jMnINg%2FcMjg8ZzhQirsK1ZznSPBOmS1ZBtT4DN%2BVWTDkeGzHGvzpPqIkjnFKgIOB2NwDit%2BH3EA8LL3YVXeHKe7x8M%2BmXG9tFobTHb579EB5LkEk7KPLSuNvLC%2FDujr8xP%2BwszFjhUgIMDCH9cCOBHU4mYq43e4ZwHQwzv7hxAY6pgENxvjXxa5F7jl7a6s8RuslkXaxDVBKRPTJKvvznGT%2F6xFGseR%2FTL6vYcAeKlsnoeftBp5TljHBJuS6WpS%2FSn7swqkzASjsmBniAgcsgXH%2FNwwjjB%2BfDd4CNZw1Mrxx3RFs%2B3TsTQ3LorpUrm6ndtw4kgYgf5Zlr0r9AzaGDSy31ChXUG6JPugFRp3FmTO8vEytKTjtinXjKDaotjkpCFNPDBi4ECvr&X-Amz-Signature=59bd90f78b66fbb343e45fef5785c7a4dc96e528e9db2383ef189175f3842ee5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Attribution Graph는 모델 계산의 근사적 표현 → 어디까지나 **설명 가능한 추정 (가설)이다**. 따라서 이를 검증하기 위해 실제 원래 모델에 개입 실험(intervention)을 수행한다:

- 특정 기능 그룹을 억제하거나 비활성화하고

- 그 결과로 **다른 기능들과 출력이 어떻게 변하는지** 관찰.

예를 들어, ‘Texas’ 관련 기능을 껐을 때 ‘Austin’이 출력되지 않는다면, 해당 기능이 **실제로 중요한 역할을 한다는 증거**가 된다.

이 외에도, 해당 논문에서는 다음의 것들을 다루기도 함:

- **중요한 레이어의 위치 파악 (Localizing Important Layers):** 모델의 계산에서 중요한 역할을 하는 레이어를 식별하는 방법을 다룹니다.

- **평가 (Evaluations)**

- **생물학 (Biology)**

현재 우리가 보고있는 논문은 아니기에 pass

## 1. Multi-step Reasoning

첫 번째 사례 연구는 모델이 **다단계 추론을 하는가를 확인하는 것**. 예를 들어, 다음과 같은 질문을 생각해봅시다:

> Q: the capital of the state containing Dallas is __

이 질문을 올바르게 답하려면 두 가지 정보를 순차적으로 추론해야 한다:

1. **댈러스는 텍사스 주에 있다.**

1. **텍사스의 수도는 오스틴이다.**

Claude 3.5 Haiku는 이 질문에 대해 정확하게 **Austin**이라고 답합니다. 중요한 질문은: 모델이 이 답을 도출할 때, 이 두 단계를 **실제로 내부적으로 수행했는가?** 아니면 단순히 전체 질문을 암기하거나 통계적 상관관계에 따라 응답했는가?

### 어트리뷰션 그래프를 통한 분석

어트리뷰션 그래프를 생성하여 이 질문에 대한 모델의 추론 경로를 시각적으로 확인함.

- 관찰 1: “텍사스”는 중간 단계로 사용된다

그래프를 분석해본 결과, 모델은 먼저 ‘Dallas’를 입력으로 받고 이를 바탕으로 **Texas**라는 기능을 활성화합니다. 이 기능은 **다음 단계의 추론**, 즉 ‘Texas의 주도 = Austin’으로 이어지는 경로를 활성화하는 데 중요하게 작용합니다. 다시 말해, **텍사스라는 중간 개념은 명시적으로 내부에서 추론됩니다. **

**The graph indicates that the replacement model does in fact perform “multi-hop reasoning” – that is, its decision to say Austin hinges on a chain of several intermediate computational steps (Dallas → Texas, and Texas + capital → Austin). **

- 관찰 2: “텍사스” 기능이 없다면?

이를 검증하기 위해, ‘텍사스’ 개념을 담당하는 기능들을 **비활성화(disable)** 한 후, 모델이 여전히 Austin이라고 답하는지를 테스트했습니다. 그 결과, 모델은 ‘Austin’이라는 출력을 생성하지 못했습니다. 이는 모델이 진짜로 ‘텍사스’를 중간 단계로 활용하고 있다는 강력한 증거입니다.

다음과 같이 다른 feature로 중간 스텝을 대체해 output을 조절하는 실험도 진행

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/cfd56df0-cf89-4ee7-95c5-baf489a03499/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-04-07_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_9.15.27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRAABYAO%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIET6GAb%2FwgPsK%2BHBHQbfSm2VIITT192qEa5KOBIT3ZHgAiA5ov9pllg2Om8qbbuJ%2FAahoXNIaBjHHz0dHLNTqDQHjSqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMxc0I89fxq7Xz6sz%2FKtwDLJ%2FR%2Bu3VH51K0yyJt4Ph2ZBcGMdjHstVSzeAfcawdpBJT5Q8YnWuDijB8tZINF%2FJV5%2BW5jl20UIGyz1XNSFe627L4hnpHaXR20rRHK8Y2dJnRII42OuwPY23oXbRwduMRBEtOYpilI6DtiUXHIZxJawHqu89ih%2BQEvijtXgU0NvMZF8YB1if5ilzntBVFj1YTNjCAhkdhYnxi0mr2Zqc9mVMLHQn%2BgzBgn0Tz3YYb9Q81tRSUnN3OKqqUZJPwhwkePgBoFKz%2BCWrO%2F3NAg4xsypnsQhJOtzCJnyUQ%2FCd%2BFeOE7%2FBk0g7kQ5Oy3SEV8yQa%2BKt%2F1fttvau3n5jCNKEypoaNH9cP4%2B%2FxIf9bNEJQCQkO%2FMYkliTHO8OQN5bn8AAUiOzPME6kOpq5nIrE6jC9p2Oete%2F6jkKl%2FKL0S0xldvV6QuGpXV8fOvisZyHUx3o1KSt2qTu8Os7QT892B5VbGN7jMnINg%2FcMjg8ZzhQirsK1ZznSPBOmS1ZBtT4DN%2BVWTDkeGzHGvzpPqIkjnFKgIOB2NwDit%2BH3EA8LL3YVXeHKe7x8M%2BmXG9tFobTHb579EB5LkEk7KPLSuNvLC%2FDujr8xP%2BwszFjhUgIMDCH9cCOBHU4mYq43e4ZwHQwzv7hxAY6pgENxvjXxa5F7jl7a6s8RuslkXaxDVBKRPTJKvvznGT%2F6xFGseR%2FTL6vYcAeKlsnoeftBp5TljHBJuS6WpS%2FSn7swqkzASjsmBniAgcsgXH%2FNwwjjB%2BfDd4CNZw1Mrxx3RFs%2B3TsTQ3LorpUrm6ndtw4kgYgf5Zlr0r9AzaGDSy31ChXUG6JPugFRp3FmTO8vEytKTjtinXjKDaotjkpCFNPDBi4ECvr&X-Amz-Signature=e77d139163e7712a41e919c8b85122f08d5f33da09c10583561dc8ff2d9abbc6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
