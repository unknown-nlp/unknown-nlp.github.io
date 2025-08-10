---
categories:
  - paper-reviews
date: "2025-08-12 00:00:00"
description: 논문 리뷰
giscus_comments: true
layout: post
related_posts: false
slug: 2025-08-12-impact-of-fine-tuning-methods-on-memorization-in
tags:
  - attention
  - embedding
  - fine-tuning
  - gpt
  - language-model
  - llm
  - paper-review
title: Impact of Fine-Tuning Methods on Memorization in Large Language Models
---

**논문 정보**

- **Date**: 2025-08-05
- **Reviewer**: hyowon Cho

많은 연구들이 LLM이 사전학습 단계에서 학습 데이터를 외우는 이슈에 대해서 보고하고 있는 한편, finetuning에 대해서 비슷한 연구는 놀라울 정도로 적다.

하지만, finetuning도 당연히 모델 대부의 업데이트와 때때로는 구조적인 변화까지도 이루어지기 때문에, finetuning의 memorization level에 대한 연구도 필요하다.

그렇다면, 존재하는 다양한 finetuning 방법에 따른 memorization of fineuning data의 영향력은 어떻게 되는가?

해당 연구는 이를 시험하기 위해 우선 finetuning 방법을 크게 두 가지로 구분한다:

1. Parameter-based finetuning: 모델 파라 바꿈

1. Prompt-based fine-tuning: 모델 파라 고정, soft token/prefix embedding…

결과적으로 두 카테고리를 고루 포함한 5가지 방법을 시험했고,

평가는 다양한 MIAs(membership inference attacks )로 했고,

데이터는 Wikitext, WebNLG, Xsum 세 가지로 했다 (좀 적긴하네요)

간단하고 빠르게 다음으로 넘어갑시다

# Fine-Tuning Methods

- Parameter-based fine-tuning

- Prompt-based fine-tuning: task-specific prompts only

# Memorization and MIAs

- 사용된 MIA 기법과 점수 계산 방식:

# Experimental Setup

- 데이터

- 평가

- 모델

- Evaluation Metrics

- Implementation Details

# Results and Observations

## Memorization across Tuning Methods

> Does the choice of finetuning strategy affect how much a model memorizes its training data for fine tuning?

> Observation ♯1: (당연)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/ad91ce4c-5fe8-4d71-8c9c-fde31b90ded6/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-08-04_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_8.29.07.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDJV22VM%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDgeIysa%2BMNGORO%2BNMKlpYFISXnSColLf11Oq1hX1%2BxaQIgCilhl9KgulvXAMMjO3%2B0J%2BG4R5G6z%2FDXTYTAbChN3A8qiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDtXeKmq2YUILPYWuyrcA94Zq1YKiVVWiJCQKLGLl9JYQ5vnASp7fwccnWanVgGfNXTWSHvkPLiXoTDTTw7ZcBqLCn4pUkhfSLSL9LTGkJXayOxQhEhUl83pL2eovOJU%2FNq%2FHZ9kTnH6ZIaZqkbS6QSZ4XUz9iICsweAb7r4f%2FbHz9bkwY%2FMR3w3JtTbQ7IUNR5%2BWu8gsdu62OfDcNTmRC2qJ3iUiJszQwTFK%2FnxxZQP7UIxSsPgnQX2VFX7TnQubQMx%2F2nXyvuKFaHZrArm9kOpevspoU7kyIPBy4xUyj7zaO9KPXXBWHrGL93i2KwDzxFtTNZrUG4caXDar4iFJtw0XZQNuMl7bRf8Qgf7Jwd5fAC%2F8nuRhAZHhU%2BX%2BYOIA6co91VTCfuoYG%2BNEB6THKt%2B%2FL%2BV6eJBPWiVuUIgU8QMmZh99jSXxrO4T0QG8ut9kRhezEBFjJV7tcZrsVQWNrEvm%2Fe%2BfU%2BiO8p%2Fa%2F62wVEaue7Qn6kiZYYdZ%2F8r4aOPy%2FNfRsJfmZDTkXDqSnEPLmKjgsWBPK5BHMqc09DDM5JZNJeSNjTQfdw3waKTFICB%2F7WjxHIpWJMcX5H88MtiDJR2XI%2FOIygZJs%2BhVBwATPYAYb3KEaJgxaCFwuDXg6v7SWmxJiWFpw22VsQfMKvU4cQGOqUBSkYYXNq4qXBSp1EBkoCPm9KoK0A%2F1RiY%2BMQlbqf2pqNH9nzz9M14ejJg4h7DAUYLM18KNOloT0MNfBAd8yslrb3TpoChCMdeTLS13oxOe4qSBPxi5BTgmiZyRLh7DVhHwC%2F748EWk5KnSFh7a2jzXpX8mMxEM33Xfn%2BkeSdaeuAxftlGgK5oH3ooqJfM2WHollWs9xkUbv7prZlCUeVz6D42E5py&X-Amz-Signature=a548c5ff7afe7b2c26eb51f8ab45acc7b76cc606cecd477ae832ff7a9b9eca26&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

모든 방법론은 validation PPL기준으로 성능 좋았음.

하지만, prompt-based methods 는 parameter-based 보다 외우는 성능 떨어짐 (당연)

> Observation ♯2:

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/2a8d6656-bf86-4c07-ae08-ce475dbfc5e4/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-08-04_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_8.31.58.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDJV22VM%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDgeIysa%2BMNGORO%2BNMKlpYFISXnSColLf11Oq1hX1%2BxaQIgCilhl9KgulvXAMMjO3%2B0J%2BG4R5G6z%2FDXTYTAbChN3A8qiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDtXeKmq2YUILPYWuyrcA94Zq1YKiVVWiJCQKLGLl9JYQ5vnASp7fwccnWanVgGfNXTWSHvkPLiXoTDTTw7ZcBqLCn4pUkhfSLSL9LTGkJXayOxQhEhUl83pL2eovOJU%2FNq%2FHZ9kTnH6ZIaZqkbS6QSZ4XUz9iICsweAb7r4f%2FbHz9bkwY%2FMR3w3JtTbQ7IUNR5%2BWu8gsdu62OfDcNTmRC2qJ3iUiJszQwTFK%2FnxxZQP7UIxSsPgnQX2VFX7TnQubQMx%2F2nXyvuKFaHZrArm9kOpevspoU7kyIPBy4xUyj7zaO9KPXXBWHrGL93i2KwDzxFtTNZrUG4caXDar4iFJtw0XZQNuMl7bRf8Qgf7Jwd5fAC%2F8nuRhAZHhU%2BX%2BYOIA6co91VTCfuoYG%2BNEB6THKt%2B%2FL%2BV6eJBPWiVuUIgU8QMmZh99jSXxrO4T0QG8ut9kRhezEBFjJV7tcZrsVQWNrEvm%2Fe%2BfU%2BiO8p%2Fa%2F62wVEaue7Qn6kiZYYdZ%2F8r4aOPy%2FNfRsJfmZDTkXDqSnEPLmKjgsWBPK5BHMqc09DDM5JZNJeSNjTQfdw3waKTFICB%2F7WjxHIpWJMcX5H88MtiDJR2XI%2FOIygZJs%2BhVBwATPYAYb3KEaJgxaCFwuDXg6v7SWmxJiWFpw22VsQfMKvU4cQGOqUBSkYYXNq4qXBSp1EBkoCPm9KoK0A%2F1RiY%2BMQlbqf2pqNH9nzz9M14ejJg4h7DAUYLM18KNOloT0MNfBAd8yslrb3TpoChCMdeTLS13oxOe4qSBPxi5BTgmiZyRLh7DVhHwC%2F748EWk5KnSFh7a2jzXpX8mMxEM33Xfn%2BkeSdaeuAxftlGgK5oH3ooqJfM2WHollWs9xkUbv7prZlCUeVz6D42E5py&X-Amz-Signature=1b545110eed2c819019acefa5746052115cdfb2ae1cd3f78070507a018b01af1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Why Prompt-Based Fine-Tuning Exhibits Low Memorization

prompt-based fine-tuning introduces a bias into the model’s attention mechanism indirectly via
the soft prompt or prefix, rather than altering the attention mechanism itself.

- **Prefix Tuning 수식 (Petrov et al., 2024)**

- 결과적으로 **표현 공간의 이동(shift) < 적음** → 학습, 비학습 샘플 분포 차이가 작아 MIA가 어렵다.

이 가설을 확인하기 위해:

distributions of non-membership and membership examples on the LLaMA2-7B를 세 세팅에서 비교함:

1. pre-trained model,

1. fine-tuned with LoRA

1. fine-tuned with prefix tuning

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/921ea729-8962-4660-9050-b2942099dcca/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-08-04_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_8.37.31.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDJV22VM%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDgeIysa%2BMNGORO%2BNMKlpYFISXnSColLf11Oq1hX1%2BxaQIgCilhl9KgulvXAMMjO3%2B0J%2BG4R5G6z%2FDXTYTAbChN3A8qiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDtXeKmq2YUILPYWuyrcA94Zq1YKiVVWiJCQKLGLl9JYQ5vnASp7fwccnWanVgGfNXTWSHvkPLiXoTDTTw7ZcBqLCn4pUkhfSLSL9LTGkJXayOxQhEhUl83pL2eovOJU%2FNq%2FHZ9kTnH6ZIaZqkbS6QSZ4XUz9iICsweAb7r4f%2FbHz9bkwY%2FMR3w3JtTbQ7IUNR5%2BWu8gsdu62OfDcNTmRC2qJ3iUiJszQwTFK%2FnxxZQP7UIxSsPgnQX2VFX7TnQubQMx%2F2nXyvuKFaHZrArm9kOpevspoU7kyIPBy4xUyj7zaO9KPXXBWHrGL93i2KwDzxFtTNZrUG4caXDar4iFJtw0XZQNuMl7bRf8Qgf7Jwd5fAC%2F8nuRhAZHhU%2BX%2BYOIA6co91VTCfuoYG%2BNEB6THKt%2B%2FL%2BV6eJBPWiVuUIgU8QMmZh99jSXxrO4T0QG8ut9kRhezEBFjJV7tcZrsVQWNrEvm%2Fe%2BfU%2BiO8p%2Fa%2F62wVEaue7Qn6kiZYYdZ%2F8r4aOPy%2FNfRsJfmZDTkXDqSnEPLmKjgsWBPK5BHMqc09DDM5JZNJeSNjTQfdw3waKTFICB%2F7WjxHIpWJMcX5H88MtiDJR2XI%2FOIygZJs%2BhVBwATPYAYb3KEaJgxaCFwuDXg6v7SWmxJiWFpw22VsQfMKvU4cQGOqUBSkYYXNq4qXBSp1EBkoCPm9KoK0A%2F1RiY%2BMQlbqf2pqNH9nzz9M14ejJg4h7DAUYLM18KNOloT0MNfBAd8yslrb3TpoChCMdeTLS13oxOe4qSBPxi5BTgmiZyRLh7DVhHwC%2F748EWk5KnSFh7a2jzXpX8mMxEM33Xfn%2BkeSdaeuAxftlGgK5oH3ooqJfM2WHollWs9xkUbv7prZlCUeVz6D42E5py&X-Amz-Signature=bdfd3714b32d98b4e2515690a38b9d965e666cb8f56bf54b81ba83ce6752ec6a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

LoRA는 membership and non-membership samples 사이 분포 차이가 큰데, prefix tuning은 미미하다는 것을 알 수 있음

## Performance in Different Tuning Paradigms

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/d33692c5-dcd0-4f86-9106-c80cc1c2ba4a/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-08-04_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_8.40.18.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDJV22VM%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDgeIysa%2BMNGORO%2BNMKlpYFISXnSColLf11Oq1hX1%2BxaQIgCilhl9KgulvXAMMjO3%2B0J%2BG4R5G6z%2FDXTYTAbChN3A8qiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDtXeKmq2YUILPYWuyrcA94Zq1YKiVVWiJCQKLGLl9JYQ5vnASp7fwccnWanVgGfNXTWSHvkPLiXoTDTTw7ZcBqLCn4pUkhfSLSL9LTGkJXayOxQhEhUl83pL2eovOJU%2FNq%2FHZ9kTnH6ZIaZqkbS6QSZ4XUz9iICsweAb7r4f%2FbHz9bkwY%2FMR3w3JtTbQ7IUNR5%2BWu8gsdu62OfDcNTmRC2qJ3iUiJszQwTFK%2FnxxZQP7UIxSsPgnQX2VFX7TnQubQMx%2F2nXyvuKFaHZrArm9kOpevspoU7kyIPBy4xUyj7zaO9KPXXBWHrGL93i2KwDzxFtTNZrUG4caXDar4iFJtw0XZQNuMl7bRf8Qgf7Jwd5fAC%2F8nuRhAZHhU%2BX%2BYOIA6co91VTCfuoYG%2BNEB6THKt%2B%2FL%2BV6eJBPWiVuUIgU8QMmZh99jSXxrO4T0QG8ut9kRhezEBFjJV7tcZrsVQWNrEvm%2Fe%2BfU%2BiO8p%2Fa%2F62wVEaue7Qn6kiZYYdZ%2F8r4aOPy%2FNfRsJfmZDTkXDqSnEPLmKjgsWBPK5BHMqc09DDM5JZNJeSNjTQfdw3waKTFICB%2F7WjxHIpWJMcX5H88MtiDJR2XI%2FOIygZJs%2BhVBwATPYAYb3KEaJgxaCFwuDXg6v7SWmxJiWFpw22VsQfMKvU4cQGOqUBSkYYXNq4qXBSp1EBkoCPm9KoK0A%2F1RiY%2BMQlbqf2pqNH9nzz9M14ejJg4h7DAUYLM18KNOloT0MNfBAd8yslrb3TpoChCMdeTLS13oxOe4qSBPxi5BTgmiZyRLh7DVhHwC%2F748EWk5KnSFh7a2jzXpX8mMxEM33Xfn%2BkeSdaeuAxftlGgK5oH3ooqJfM2WHollWs9xkUbv7prZlCUeVz6D42E5py&X-Amz-Signature=f73c097a6c8a5c7279eea0c3fdbad0d68374d15ea1cb792b62da3eed09779b36&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

두 방법론이 최종적으로는 비슷한 PPL을 가졌음에도 불구하고, Learning trajactories는 꽤나 달랐음

parameterbased fine-tuning:

- decreases over the first few epochs

- later increases due to overfitting, before eventually converging

prompt-based fine-tuning:

- slightly decreasing validation PPL throughout training,

- converging without the overfitting-induced rise

이는 아까도 이야기 했듯이, 후자가 internal sample distribution of the model을 바꾸는 것이 아니라 단순히 다운스트림 태스크에 쪼끔 더 나은 bias를 추가하는 정도임을 다시한번 보인다

# Discussion

## Regarding Model Scale

모델 사이즈가 memorization에 중요한 영향력을 줄 것임.

→ To what extent does model size influence memorization under different fine-tuning strategies?

> Observation ♯3

four variants of the GPT-2 architecture:

- GPT-2 (124M),

- GPT-2 Medium (345M),

- GPT2 Large (762M),

- GPT-2 XL (1.5B).

LLaMA2-7B vs LLaMA3-1B

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/b560e507-553c-4427-994f-307595515593/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-08-04_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_8.46.56.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDJV22VM%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDgeIysa%2BMNGORO%2BNMKlpYFISXnSColLf11Oq1hX1%2BxaQIgCilhl9KgulvXAMMjO3%2B0J%2BG4R5G6z%2FDXTYTAbChN3A8qiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDtXeKmq2YUILPYWuyrcA94Zq1YKiVVWiJCQKLGLl9JYQ5vnASp7fwccnWanVgGfNXTWSHvkPLiXoTDTTw7ZcBqLCn4pUkhfSLSL9LTGkJXayOxQhEhUl83pL2eovOJU%2FNq%2FHZ9kTnH6ZIaZqkbS6QSZ4XUz9iICsweAb7r4f%2FbHz9bkwY%2FMR3w3JtTbQ7IUNR5%2BWu8gsdu62OfDcNTmRC2qJ3iUiJszQwTFK%2FnxxZQP7UIxSsPgnQX2VFX7TnQubQMx%2F2nXyvuKFaHZrArm9kOpevspoU7kyIPBy4xUyj7zaO9KPXXBWHrGL93i2KwDzxFtTNZrUG4caXDar4iFJtw0XZQNuMl7bRf8Qgf7Jwd5fAC%2F8nuRhAZHhU%2BX%2BYOIA6co91VTCfuoYG%2BNEB6THKt%2B%2FL%2BV6eJBPWiVuUIgU8QMmZh99jSXxrO4T0QG8ut9kRhezEBFjJV7tcZrsVQWNrEvm%2Fe%2BfU%2BiO8p%2Fa%2F62wVEaue7Qn6kiZYYdZ%2F8r4aOPy%2FNfRsJfmZDTkXDqSnEPLmKjgsWBPK5BHMqc09DDM5JZNJeSNjTQfdw3waKTFICB%2F7WjxHIpWJMcX5H88MtiDJR2XI%2FOIygZJs%2BhVBwATPYAYb3KEaJgxaCFwuDXg6v7SWmxJiWFpw22VsQfMKvU4cQGOqUBSkYYXNq4qXBSp1EBkoCPm9KoK0A%2F1RiY%2BMQlbqf2pqNH9nzz9M14ejJg4h7DAUYLM18KNOloT0MNfBAd8yslrb3TpoChCMdeTLS13oxOe4qSBPxi5BTgmiZyRLh7DVhHwC%2F748EWk5KnSFh7a2jzXpX8mMxEM33Xfn%2BkeSdaeuAxftlGgK5oH3ooqJfM2WHollWs9xkUbv7prZlCUeVz6D42E5py&X-Amz-Signature=b1c1e2cd2e391191cb78d6b7dacff5c57c913c50f73a8e2c4ca74d4e8b622c79&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

요약: 파라미터 바꾸는 애들은 모델 크기 커질수록 더 잘 외웠는데 반대는 미미하더라 (low sensitivity of prompt tuning to model scale)

특히, gpt2의 경우나 1B 스케일에서 LoRA는 사실상 거의 못외움

## Impact of Downstream Tasks

> Observation ♯4
> Prompt-based tuning leads to stronger memorization in structured tasks than in other downstream tasks.

다운스트림 태스크의 종류에 따라서도 다를 수 있음. 이를 위 LLaMA2-7B를 다양한 방법을 통해 학습시키고 LOSS attack against에 대해서 각각을 평가해봄

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/ad91ce4c-5fe8-4d71-8c9c-fde31b90ded6/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-08-04_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_8.29.07.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDJV22VM%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105951Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDgeIysa%2BMNGORO%2BNMKlpYFISXnSColLf11Oq1hX1%2BxaQIgCilhl9KgulvXAMMjO3%2B0J%2BG4R5G6z%2FDXTYTAbChN3A8qiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDtXeKmq2YUILPYWuyrcA94Zq1YKiVVWiJCQKLGLl9JYQ5vnASp7fwccnWanVgGfNXTWSHvkPLiXoTDTTw7ZcBqLCn4pUkhfSLSL9LTGkJXayOxQhEhUl83pL2eovOJU%2FNq%2FHZ9kTnH6ZIaZqkbS6QSZ4XUz9iICsweAb7r4f%2FbHz9bkwY%2FMR3w3JtTbQ7IUNR5%2BWu8gsdu62OfDcNTmRC2qJ3iUiJszQwTFK%2FnxxZQP7UIxSsPgnQX2VFX7TnQubQMx%2F2nXyvuKFaHZrArm9kOpevspoU7kyIPBy4xUyj7zaO9KPXXBWHrGL93i2KwDzxFtTNZrUG4caXDar4iFJtw0XZQNuMl7bRf8Qgf7Jwd5fAC%2F8nuRhAZHhU%2BX%2BYOIA6co91VTCfuoYG%2BNEB6THKt%2B%2FL%2BV6eJBPWiVuUIgU8QMmZh99jSXxrO4T0QG8ut9kRhezEBFjJV7tcZrsVQWNrEvm%2Fe%2BfU%2BiO8p%2Fa%2F62wVEaue7Qn6kiZYYdZ%2F8r4aOPy%2FNfRsJfmZDTkXDqSnEPLmKjgsWBPK5BHMqc09DDM5JZNJeSNjTQfdw3waKTFICB%2F7WjxHIpWJMcX5H88MtiDJR2XI%2FOIygZJs%2BhVBwATPYAYb3KEaJgxaCFwuDXg6v7SWmxJiWFpw22VsQfMKvU4cQGOqUBSkYYXNq4qXBSp1EBkoCPm9KoK0A%2F1RiY%2BMQlbqf2pqNH9nzz9M14ejJg4h7DAUYLM18KNOloT0MNfBAd8yslrb3TpoChCMdeTLS13oxOe4qSBPxi5BTgmiZyRLh7DVhHwC%2F748EWk5KnSFh7a2jzXpX8mMxEM33Xfn%2BkeSdaeuAxftlGgK5oH3ooqJfM2WHollWs9xkUbv7prZlCUeVz6D42E5py&X-Amz-Signature=a548c5ff7afe7b2c26eb51f8ab45acc7b76cc606cecd477ae832ff7a9b9eca26&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Prompt-based 만 봤을 때, WebNLG가 다른 것들에 비해서 성능이 높다

아마도 구조화된 pattern학습에는 유리한 것 같다
