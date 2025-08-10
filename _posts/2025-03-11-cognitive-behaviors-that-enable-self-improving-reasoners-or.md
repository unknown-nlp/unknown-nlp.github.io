---
categories:
- paper-reviews
date: '2025-03-11 00:00:00'
description: 논문 리뷰 - RL, Reasoning 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- llm
- paper-review
- pre-training
- reasoning
- rl
- vision
thumbnail: assets/img/posts/2025-03-11-cognitive-behaviors-that-enable-self-improving-reasoners-or/thumbnail.jpg
title: Cognitive Behaviors that Enable Self-Improving Reasoners, or, Four Habits of
  Highly Effective STaRs
---

**논문 정보**
- **Date**: 2025-03-11
- **Reviewer**: 준원 장
- **Property**: RL, Reasoning

## 1. Introduction

- Motivation

- **Findings of work**

## 2. Related Works

- Improving Reasoning Capabilities

## 3. Identifying and Engineering Self-Improving Behavior

### Initial Investigation: A tale of two models

- Pilot Test: Countdown

- Why Countdown? (아래를 반영할 수 있는 task)

- BaseLLM

- RL-Training

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/8a9f9d5e-5a48-4779-9ad4-d29fc231d3f6/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-03-07_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_6.56.10.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677PVEWM6%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113456Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBp%2F8jOC7twJSao2M%2BwTVkVcoE%2BmDkvw2%2FABezfFwH4QIhAJ3a6c7dcP%2FMMVmsyVccTxQYSZ%2FiIupCPV7pLVG8omZ%2FKogECNT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxfDCzpqLNv3BhelIYq3AM1lMnVgSiU3ZN9U%2Bh7p10fVU1oV7zKwO6ua%2BXzB5%2FYJ2Z8K71L5QeOgp41JNHeINcqZTqjABoqzbT2xzUHdBgBFSlYzW8nZPBTzs0M0lUPZ8CYSmGV5n65uIPAxHj57pyTFdYa7n14geLTZUprGJUiGieVcRXlbGE4f5IqyauEo3LNW%2Banu4EBO%2BzmqDMD0Ow%2F8cd6hLB1%2B0A%2BS7R4xuaTHvWonAdFp1Q5gUkWc1ppvHmIAgCSZ4RzV31%2BS0dlrT%2BFX%2F3DkRmReaqT19r95jaNXRZSiTvq4SI4JCz5sKINr9tamnLuG1mk0mFmuPWPw5CyWdDYW7DUKBAII8fhVa%2FRSVelnaD8zEk%2FBg91%2Fck3dPIZvdUQCHaGm2l0MIgT%2BwsJTgdpxZVo8XgmWswn0mGZHlsemR3GkVNkONJE8n1ifXoD86hPWO85aNlexUhXzK5i0kOSfq%2FpyR7Wpbc6oYVpzdcPC0PPxfKkGVw6RZB60k7%2B7Xsj1Oaa7rKMdWYAO%2FYztj7ezRm4%2FXvnMdhDCgLKaHaJHrZvf8UaehJiYuCj%2Bqy%2FAGyc7I1VLu4Z%2FAIwXPBu1GmvkCFsD%2F4DktaPETFv0VetfB7IGcGNJTPafpLAZEVumhmwmlUbXyZOCzDw%2F%2BHEBjqkARVmVGgoKMGR42R7kTM6%2FhzvYr9gkdaER8EL3AdBBEXoyZ02O9XSW82kIPWdz2bwqyZ0kRdA3hBY1M3FWcRT1FL%2Bud%2BgdWUOQ7y1Il4XNf2D7QZRq6ZofJyvSN5X43pYdTIfi%2B4AC422p4BGSkvyRL9h2YVBxrg6rgloshEUVgaaMLYzMqWKKXjAnU6vAkNEB474yTWBIE0kVzDosFT1uDKArFk8&X-Amz-Signature=7a54436cc62ed726aeea6ac83821b3268fe74197222d8ba5f3aba7c2028d2f6b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

→ Qwen 30 step부터 성능 증가, 60% accuracy 달성. Llama 최종 30% accuracy 달성.

→ Qwen 초기에 explicit verification statements → implicit solution checking 

(‘verbose하게 verification하다가 올바른 답을 찾을 때까지 순차적으로 다른 해결책을 시도를 하는 방식으로 바뀜)

**RQ: what underlying capabilities enable successful reasoning-based improvement?**

### A Framework for Analyzing Cognitive Behaviors

1. **Backtracking or the explicit revision of approaches when errors are detected**: 백트래킹 또는 오류가 감지되었을 때 접근 방식의 명시적 수정(예: '이 접근 방식은 다음과 같은 이유로 작동하지 않습니다...')”

1. **Verification or the systematic checking of intermediate results**: 검증 또는 중간 결과의 체계적인 확인 (예: '이 결과를 다음과 같은 방식으로 검증해 봅시다...')”

1. **Subgoal Setting**: 하위 목표 설정, 복잡한 문제를 관리 가능한 단계로 분해하는 것(예: '이를 해결하기 위해, 우리는 먼저 다음이 필요합니다...')”

1. **Backward Chaining**: 역방향 연쇄, 목표 지향적 추론 문제에서 원하는 결과에서부터 역으로 해결책을 찾아가는 것(예: '75라는 목표에 도달하기 위해, 우리는 다음으로 나눌 수 있는 숫자가 필요합니다...')”

⇒ gpo-4o-mini를 활용해 각 training step에서 model output이 위의 behaviors를 포함하는지 분류

### The Role of Initial Behaviors in Self-Improvement

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/295716a5-8bf3-48c9-94c9-c4ffad6c7e25/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-03-07_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_6.56.25.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677PVEWM6%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113456Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBp%2F8jOC7twJSao2M%2BwTVkVcoE%2BmDkvw2%2FABezfFwH4QIhAJ3a6c7dcP%2FMMVmsyVccTxQYSZ%2FiIupCPV7pLVG8omZ%2FKogECNT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxfDCzpqLNv3BhelIYq3AM1lMnVgSiU3ZN9U%2Bh7p10fVU1oV7zKwO6ua%2BXzB5%2FYJ2Z8K71L5QeOgp41JNHeINcqZTqjABoqzbT2xzUHdBgBFSlYzW8nZPBTzs0M0lUPZ8CYSmGV5n65uIPAxHj57pyTFdYa7n14geLTZUprGJUiGieVcRXlbGE4f5IqyauEo3LNW%2Banu4EBO%2BzmqDMD0Ow%2F8cd6hLB1%2B0A%2BS7R4xuaTHvWonAdFp1Q5gUkWc1ppvHmIAgCSZ4RzV31%2BS0dlrT%2BFX%2F3DkRmReaqT19r95jaNXRZSiTvq4SI4JCz5sKINr9tamnLuG1mk0mFmuPWPw5CyWdDYW7DUKBAII8fhVa%2FRSVelnaD8zEk%2FBg91%2Fck3dPIZvdUQCHaGm2l0MIgT%2BwsJTgdpxZVo8XgmWswn0mGZHlsemR3GkVNkONJE8n1ifXoD86hPWO85aNlexUhXzK5i0kOSfq%2FpyR7Wpbc6oYVpzdcPC0PPxfKkGVw6RZB60k7%2B7Xsj1Oaa7rKMdWYAO%2FYztj7ezRm4%2FXvnMdhDCgLKaHaJHrZvf8UaehJiYuCj%2Bqy%2FAGyc7I1VLu4Z%2FAIwXPBu1GmvkCFsD%2F4DktaPETFv0VetfB7IGcGNJTPafpLAZEVumhmwmlUbXyZOCzDw%2F%2BHEBjqkARVmVGgoKMGR42R7kTM6%2FhzvYr9gkdaER8EL3AdBBEXoyZ02O9XSW82kIPWdz2bwqyZ0kRdA3hBY1M3FWcRT1FL%2Bud%2BgdWUOQ7y1Il4XNf2D7QZRq6ZofJyvSN5X43pYdTIfi%2B4AC422p4BGSkvyRL9h2YVBxrg6rgloshEUVgaaMLYzMqWKKXjAnU6vAkNEB474yTWBIE0kVzDosFT1uDKArFk8&X-Amz-Signature=d0881605e96a1d8d50e062488f726c0b8a7b7d4beaf7713c9ffd03888d9fd4b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

→** Qwen의 performance improvements지점과 emergence of cognitive behaviors의 지점이 거의 일치함 (30~130steps)**

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/aac67e6b-3265-4a42-9c95-98ad14069cc3/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-03-07_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_7.12.08.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677PVEWM6%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113456Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBp%2F8jOC7twJSao2M%2BwTVkVcoE%2BmDkvw2%2FABezfFwH4QIhAJ3a6c7dcP%2FMMVmsyVccTxQYSZ%2FiIupCPV7pLVG8omZ%2FKogECNT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxfDCzpqLNv3BhelIYq3AM1lMnVgSiU3ZN9U%2Bh7p10fVU1oV7zKwO6ua%2BXzB5%2FYJ2Z8K71L5QeOgp41JNHeINcqZTqjABoqzbT2xzUHdBgBFSlYzW8nZPBTzs0M0lUPZ8CYSmGV5n65uIPAxHj57pyTFdYa7n14geLTZUprGJUiGieVcRXlbGE4f5IqyauEo3LNW%2Banu4EBO%2BzmqDMD0Ow%2F8cd6hLB1%2B0A%2BS7R4xuaTHvWonAdFp1Q5gUkWc1ppvHmIAgCSZ4RzV31%2BS0dlrT%2BFX%2F3DkRmReaqT19r95jaNXRZSiTvq4SI4JCz5sKINr9tamnLuG1mk0mFmuPWPw5CyWdDYW7DUKBAII8fhVa%2FRSVelnaD8zEk%2FBg91%2Fck3dPIZvdUQCHaGm2l0MIgT%2BwsJTgdpxZVo8XgmWswn0mGZHlsemR3GkVNkONJE8n1ifXoD86hPWO85aNlexUhXzK5i0kOSfq%2FpyR7Wpbc6oYVpzdcPC0PPxfKkGVw6RZB60k7%2B7Xsj1Oaa7rKMdWYAO%2FYztj7ezRm4%2FXvnMdhDCgLKaHaJHrZvf8UaehJiYuCj%2Bqy%2FAGyc7I1VLu4Z%2FAIwXPBu1GmvkCFsD%2F4DktaPETFv0VetfB7IGcGNJTPafpLAZEVumhmwmlUbXyZOCzDw%2F%2BHEBjqkARVmVGgoKMGR42R7kTM6%2FhzvYr9gkdaER8EL3AdBBEXoyZ02O9XSW82kIPWdz2bwqyZ0kRdA3hBY1M3FWcRT1FL%2Bud%2BgdWUOQ7y1Il4XNf2D7QZRq6ZofJyvSN5X43pYdTIfi%2B4AC422p4BGSkvyRL9h2YVBxrg6rgloshEUVgaaMLYzMqWKKXjAnU6vAkNEB474yTWBIE0kVzDosFT1uDKArFk8&X-Amz-Signature=a8e6185b7a3e83b150af968a6d26237e0b2464cf0bc13b0abe040ed5d3c6c7db&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

→ General한 분석을 위해  Qwen-2.5-3B, Llama-3.2-3B, Llama-3.1-70B에 대한 분석 진행 (PPO model output)

→  Qwen-2.5-3B가 Llama들에 비해 4가지 행동 모두에서 상당히 높은 비율 기록

- **Takeway**

### Intervening on initial behaviors

**RQ: targeted intervention을 통해 인위적으로 ‘cognitive behavior’를 발현시킬 수 있을까?**

- Claude 3.5 Sonnet으로 ‘cognitive behavior’를 반드시 포함하는 reasoning path를 생성하도록 함

- 이때, 각 reasoning path는 특정 ‘cognitive behavior’를 가지도록 controlled setting (system message)

- Controlled reasoning path [Correct Answer]

- Experimental Setting

- Result

### Behavioral Augmentation of the Pretraining Data.

- 이전까지 진행했던 priming 실험은 Countdown-specific실험

**RQ: LM의 pre-training distribution을 RL때 self-improvement하도록 수정하는 방법은 없을까?**

**(Generalization)**

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/6abf7444-22be-4935-bfe5-636d78867dfd/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-03-09_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_11.58.41.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677PVEWM6%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113456Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBp%2F8jOC7twJSao2M%2BwTVkVcoE%2BmDkvw2%2FABezfFwH4QIhAJ3a6c7dcP%2FMMVmsyVccTxQYSZ%2FiIupCPV7pLVG8omZ%2FKogECNT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxfDCzpqLNv3BhelIYq3AM1lMnVgSiU3ZN9U%2Bh7p10fVU1oV7zKwO6ua%2BXzB5%2FYJ2Z8K71L5QeOgp41JNHeINcqZTqjABoqzbT2xzUHdBgBFSlYzW8nZPBTzs0M0lUPZ8CYSmGV5n65uIPAxHj57pyTFdYa7n14geLTZUprGJUiGieVcRXlbGE4f5IqyauEo3LNW%2Banu4EBO%2BzmqDMD0Ow%2F8cd6hLB1%2B0A%2BS7R4xuaTHvWonAdFp1Q5gUkWc1ppvHmIAgCSZ4RzV31%2BS0dlrT%2BFX%2F3DkRmReaqT19r95jaNXRZSiTvq4SI4JCz5sKINr9tamnLuG1mk0mFmuPWPw5CyWdDYW7DUKBAII8fhVa%2FRSVelnaD8zEk%2FBg91%2Fck3dPIZvdUQCHaGm2l0MIgT%2BwsJTgdpxZVo8XgmWswn0mGZHlsemR3GkVNkONJE8n1ifXoD86hPWO85aNlexUhXzK5i0kOSfq%2FpyR7Wpbc6oYVpzdcPC0PPxfKkGVw6RZB60k7%2B7Xsj1Oaa7rKMdWYAO%2FYztj7ezRm4%2FXvnMdhDCgLKaHaJHrZvf8UaehJiYuCj%2Bqy%2FAGyc7I1VLu4Z%2FAIwXPBu1GmvkCFsD%2F4DktaPETFv0VetfB7IGcGNJTPafpLAZEVumhmwmlUbXyZOCzDw%2F%2BHEBjqkARVmVGgoKMGR42R7kTM6%2FhzvYr9gkdaER8EL3AdBBEXoyZ02O9XSW82kIPWdz2bwqyZ0kRdA3hBY1M3FWcRT1FL%2Bud%2BgdWUOQ7y1Il4XNf2D7QZRq6ZofJyvSN5X43pYdTIfi%2B4AC422p4BGSkvyRL9h2YVBxrg6rgloshEUVgaaMLYzMqWKKXjAnU6vAkNEB474yTWBIE0kVzDosFT1uDKArFk8&X-Amz-Signature=afdd5a59a61c40c9ec76fa0fbece39255c8c58fe949cead3b705d0d49ea6ad18&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 바로 OpenWebMath나 FineMath에 Qwen-2.5-32B를 classifier로 두고 ‘cognitive behavior’가 있는지 검수해봤는데 비율이 많지는 않더라 (200K)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/b0131db2-b0b7-40d0-b8a9-cb26a51950a4/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-03-09_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_7.30.42.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677PVEWM6%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113456Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBp%2F8jOC7twJSao2M%2BwTVkVcoE%2BmDkvw2%2FABezfFwH4QIhAJ3a6c7dcP%2FMMVmsyVccTxQYSZ%2FiIupCPV7pLVG8omZ%2FKogECNT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxfDCzpqLNv3BhelIYq3AM1lMnVgSiU3ZN9U%2Bh7p10fVU1oV7zKwO6ua%2BXzB5%2FYJ2Z8K71L5QeOgp41JNHeINcqZTqjABoqzbT2xzUHdBgBFSlYzW8nZPBTzs0M0lUPZ8CYSmGV5n65uIPAxHj57pyTFdYa7n14geLTZUprGJUiGieVcRXlbGE4f5IqyauEo3LNW%2Banu4EBO%2BzmqDMD0Ow%2F8cd6hLB1%2B0A%2BS7R4xuaTHvWonAdFp1Q5gUkWc1ppvHmIAgCSZ4RzV31%2BS0dlrT%2BFX%2F3DkRmReaqT19r95jaNXRZSiTvq4SI4JCz5sKINr9tamnLuG1mk0mFmuPWPw5CyWdDYW7DUKBAII8fhVa%2FRSVelnaD8zEk%2FBg91%2Fck3dPIZvdUQCHaGm2l0MIgT%2BwsJTgdpxZVo8XgmWswn0mGZHlsemR3GkVNkONJE8n1ifXoD86hPWO85aNlexUhXzK5i0kOSfq%2FpyR7Wpbc6oYVpzdcPC0PPxfKkGVw6RZB60k7%2B7Xsj1Oaa7rKMdWYAO%2FYztj7ezRm4%2FXvnMdhDCgLKaHaJHrZvf8UaehJiYuCj%2Bqy%2FAGyc7I1VLu4Z%2FAIwXPBu1GmvkCFsD%2F4DktaPETFv0VetfB7IGcGNJTPafpLAZEVumhmwmlUbXyZOCzDw%2F%2BHEBjqkARVmVGgoKMGR42R7kTM6%2FhzvYr9gkdaER8EL3AdBBEXoyZ02O9XSW82kIPWdz2bwqyZ0kRdA3hBY1M3FWcRT1FL%2Bud%2BgdWUOQ7y1Il4XNf2D7QZRq6ZofJyvSN5X43pYdTIfi%2B4AC422p4BGSkvyRL9h2YVBxrg6rgloshEUVgaaMLYzMqWKKXjAnU6vAkNEB474yTWBIE0kVzDosFT1uDKArFk8&X-Amz-Signature=57555a185bc4df2c6d678d50a309470368592a0837a6fbcc2e3e148faf8e8d1a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

1. OpenWebMath에서 'cognitive behaviors'가 있는 부분을 추출해서

1. question-thought-answer format변환 

1. 'cognitive behaviors'가 있는 부분 없는 부분 (curated vs minimized curated)

1. CL → PPO

- 'cognitive behaviors'가 발현되도록 RL training이 가능하며 output에서 verification과 backtracking을 하는 것으로 드러남

## 4. Discussion

1. RL후에 발현되는 test-time scaling은 base-model이 가지고 있는 (엄밀히 말하면 실현시킬 수 있는) 'cognitive behaviors'에 따라 다르다.

1. 논문에서는 QWEN은 cognitive behaviors가 있고 Llama3은 'cognitive behaviors'이 없다고 실험적으로 보여줌

1. 'cognitive behaviors'의 포함여부가 correct answer유무보다 RL시 self-improvement에 있어서 더 중요한 인과관계를 가짐

1. 'cognitive behaviors'가 rich한 pre-training data를 curation해 CL하면 RL후 test-time scaling을 달성할 수 있음

1. 논문에서 검증한 'cognitive behaviors'가 task-dependent하다. 
