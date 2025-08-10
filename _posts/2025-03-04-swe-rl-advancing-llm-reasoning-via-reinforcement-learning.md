---
categories:
- paper-reviews
date: '2025-03-04 00:00:00'
description: 논문 리뷰 - RL 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- gpt
- llm
- paper-review
- reasoning
- reinforcement-learning
- rl
thumbnail: assets/img/posts/2025-03-04-swe-rl-advancing-llm-reasoning-via-reinforcement-learning/thumbnail.jpg
title: 'SWE-RL: Advancing LLM Reasoning via Reinforcement Learning on Open Software
  Evolution'
---

**논문 정보**
- **Date**: 2025-03-04
- **Reviewer**: 전민진
- **Property**: RL

## Abstract

- DeepSeek-R1 출시 이후, RL이 모델의 일반적인 reasoning ability 끌어올릴 수 있다는 잠재력이 증명됨

- 간단한 rule-based reward(정답과 모델이 생성한 답변과의 유사도)을 활용해서 학습, SWE-RL은 in-domain뿐만 아니라 out-of-domain에서도 뛰어난 성능을 보임

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/76118761-72ae-409f-b419-b293b059315c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662THDCOVN%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDCjr209Hf20%2Bi%2FnxoXVjDtZDmDKiVbI9T5yBKaDXX5mAiAPdJWEx3gqNIsjAB5jOjZf2hIy7X3XbqxU%2FU8LbsHcCCqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrHmc4i4zG%2FMyUZR9KtwD8YsXqWwL9Ky2iSNB0uLsMxDb154VXgLhN7JNoB7LAFP3NtlYb5lOvwbWuu8i%2BNoMexqLJI%2FQcw8rwE6JOkoonC%2FD%2Bwu1Qoohs6Wrm1kyeckBO3xUDMbyjfGWz5B4GTKRB0DSsY%2F35RqYaZNXaip8GOWzguCY3C0ER71RbwBxpVIvv9MvpnhB%2B4OXmG5YVEBxpr1aiNbF8Slb52k8LhKBpzN24K45NI5Q4f7Ew2ADy4nSHL%2Fl2IDK%2BWl664N%2FxNCCUb54Bn6ZpSqDgWVXOFBDraPF91r15GTcBdVidOUnG3g7tte3l6LS1sdXGVDVJgdheQzODNXDKCqpsUkypt2En37iy5CVe5SS3AwJ31PZW7BCzM2GRiewRk9MIyGH9wtTiekG3qXRSQWPmvWCWEgahQdzKR%2BrpGBIGaTrbVXS32yAUOpwNsb3yXDxu8G%2BAeBwHupT69VfDO3sGXp1EorSKvmMjcqHaCBT%2BhGVEr%2Bio6coX3U7d6P52qQ3S%2B6EYG3SbOSF48gRDOJmSOhwIctb%2FeZkBBVt6KvNKhqf%2BZM3M4R2vAAgtqG83FfUQq3BPOqjhqo3Ij8yyBDTpxBCQDJIUosXgZJPVraFOdLNAFcVBF2riSmdcrIxs39%2BviMw8v7hxAY6pgFHWjkHwXO4wcox%2F3TQBE2iZdS0goHUvgt%2Fw693lJJXrSjbsUv2yA0iLGP359ZTqdJtT59%2B4pxNe0j6OB3q%2BF%2BJSoAWHSyBW%2B8fxuWpQmJ2XsRiv0l5oZ3fbst7MNO%2FmHkfrBxYQkhc%2F8PMRHH16HiML%2BkQ6BbJPv73Qao427dlW%2FN7fXDaMEWETgzk85BlWR14da5XgMhtK0rcEgKyID8xt5zrQBvu&X-Amz-Signature=bc2558761ebc89f94ec76ccf067ee7bf31adb284cb33ca29e725c19ac83416fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Introduction

- DeepSeek-R1은 rule-based RL이 용이한 도메인에 대해서만 학습, 실험 진행

- SE task에 대해서 LLM을 향상시키는 첫번째 RL method, SWE-RL을 제안

## SWE-RL

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/77c8e0bf-e4d3-4930-8f6e-ff4d2e730dc6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662THDCOVN%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDCjr209Hf20%2Bi%2FnxoXVjDtZDmDKiVbI9T5yBKaDXX5mAiAPdJWEx3gqNIsjAB5jOjZf2hIy7X3XbqxU%2FU8LbsHcCCqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrHmc4i4zG%2FMyUZR9KtwD8YsXqWwL9Ky2iSNB0uLsMxDb154VXgLhN7JNoB7LAFP3NtlYb5lOvwbWuu8i%2BNoMexqLJI%2FQcw8rwE6JOkoonC%2FD%2Bwu1Qoohs6Wrm1kyeckBO3xUDMbyjfGWz5B4GTKRB0DSsY%2F35RqYaZNXaip8GOWzguCY3C0ER71RbwBxpVIvv9MvpnhB%2B4OXmG5YVEBxpr1aiNbF8Slb52k8LhKBpzN24K45NI5Q4f7Ew2ADy4nSHL%2Fl2IDK%2BWl664N%2FxNCCUb54Bn6ZpSqDgWVXOFBDraPF91r15GTcBdVidOUnG3g7tte3l6LS1sdXGVDVJgdheQzODNXDKCqpsUkypt2En37iy5CVe5SS3AwJ31PZW7BCzM2GRiewRk9MIyGH9wtTiekG3qXRSQWPmvWCWEgahQdzKR%2BrpGBIGaTrbVXS32yAUOpwNsb3yXDxu8G%2BAeBwHupT69VfDO3sGXp1EorSKvmMjcqHaCBT%2BhGVEr%2Bio6coX3U7d6P52qQ3S%2B6EYG3SbOSF48gRDOJmSOhwIctb%2FeZkBBVt6KvNKhqf%2BZM3M4R2vAAgtqG83FfUQq3BPOqjhqo3Ij8yyBDTpxBCQDJIUosXgZJPVraFOdLNAFcVBF2riSmdcrIxs39%2BviMw8v7hxAY6pgFHWjkHwXO4wcox%2F3TQBE2iZdS0goHUvgt%2Fw693lJJXrSjbsUv2yA0iLGP359ZTqdJtT59%2B4pxNe0j6OB3q%2BF%2BJSoAWHSyBW%2B8fxuWpQmJ2XsRiv0l5oZ3fbst7MNO%2FmHkfrBxYQkhc%2F8PMRHH16HiML%2BkQ6BbJPv73Qao427dlW%2FN7fXDaMEWETgzk85BlWR14da5XgMhtK0rcEgKyID8xt5zrQBvu&X-Amz-Signature=4a7be3829707a2859ebfd6190d9676be77f14afa3c6752997d85ceb913cd3f3f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Raw pull request data curation

- Github events and clones

- PR data aggregation ⇒ 자세한 내용은 원문 참고.. 이해 못했음..

- Relevant files prediction 

- Data filtering

### Reward modeling

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/6bac7507-27eb-4680-9495-ffb36b69684c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662THDCOVN%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDCjr209Hf20%2Bi%2FnxoXVjDtZDmDKiVbI9T5yBKaDXX5mAiAPdJWEx3gqNIsjAB5jOjZf2hIy7X3XbqxU%2FU8LbsHcCCqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrHmc4i4zG%2FMyUZR9KtwD8YsXqWwL9Ky2iSNB0uLsMxDb154VXgLhN7JNoB7LAFP3NtlYb5lOvwbWuu8i%2BNoMexqLJI%2FQcw8rwE6JOkoonC%2FD%2Bwu1Qoohs6Wrm1kyeckBO3xUDMbyjfGWz5B4GTKRB0DSsY%2F35RqYaZNXaip8GOWzguCY3C0ER71RbwBxpVIvv9MvpnhB%2B4OXmG5YVEBxpr1aiNbF8Slb52k8LhKBpzN24K45NI5Q4f7Ew2ADy4nSHL%2Fl2IDK%2BWl664N%2FxNCCUb54Bn6ZpSqDgWVXOFBDraPF91r15GTcBdVidOUnG3g7tte3l6LS1sdXGVDVJgdheQzODNXDKCqpsUkypt2En37iy5CVe5SS3AwJ31PZW7BCzM2GRiewRk9MIyGH9wtTiekG3qXRSQWPmvWCWEgahQdzKR%2BrpGBIGaTrbVXS32yAUOpwNsb3yXDxu8G%2BAeBwHupT69VfDO3sGXp1EorSKvmMjcqHaCBT%2BhGVEr%2Bio6coX3U7d6P52qQ3S%2B6EYG3SbOSF48gRDOJmSOhwIctb%2FeZkBBVt6KvNKhqf%2BZM3M4R2vAAgtqG83FfUQq3BPOqjhqo3Ij8yyBDTpxBCQDJIUosXgZJPVraFOdLNAFcVBF2riSmdcrIxs39%2BviMw8v7hxAY6pgFHWjkHwXO4wcox%2F3TQBE2iZdS0goHUvgt%2Fw693lJJXrSjbsUv2yA0iLGP359ZTqdJtT59%2B4pxNe0j6OB3q%2BF%2BJSoAWHSyBW%2B8fxuWpQmJ2XsRiv0l5oZ3fbst7MNO%2FmHkfrBxYQkhc%2F8PMRHH16HiML%2BkQ6BbJPv73Qao427dlW%2FN7fXDaMEWETgzk85BlWR14da5XgMhtK0rcEgKyID8xt5zrQBvu&X-Amz-Signature=fb302a62eec30024a09e5d82dc156a2b29d588b89f571ebe50d9c988180100a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- logic-RL과 유사하게 system prompt넣어줌, format이 틀릴 경우 -1을, 맞을 경우 정답과의 유사도를 계산해 reward를 줌

- loss식은 GRPO와 동일

- SWE-RL에서의 학습을 살펴보면, 학습데이터에는 내재적으로 bug 진단, 수정사항 생성 task 2가지 정도만 커버

### Aha Moments and generalized reasoning capabilities

- SWE-RL에서도 아하모먼트(심화된 reasoning ability)가 나타남, 특히 SE task에서 필요한 reasoning ability가 아니라 범용적인 reasoning ability(self reflection, exploring multiple approaches, divide-and-conquer)등이 발현됨

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/b0036177-d0e2-4f14-99e4-cb43b972b27b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662THDCOVN%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDCjr209Hf20%2Bi%2FnxoXVjDtZDmDKiVbI9T5yBKaDXX5mAiAPdJWEx3gqNIsjAB5jOjZf2hIy7X3XbqxU%2FU8LbsHcCCqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrHmc4i4zG%2FMyUZR9KtwD8YsXqWwL9Ky2iSNB0uLsMxDb154VXgLhN7JNoB7LAFP3NtlYb5lOvwbWuu8i%2BNoMexqLJI%2FQcw8rwE6JOkoonC%2FD%2Bwu1Qoohs6Wrm1kyeckBO3xUDMbyjfGWz5B4GTKRB0DSsY%2F35RqYaZNXaip8GOWzguCY3C0ER71RbwBxpVIvv9MvpnhB%2B4OXmG5YVEBxpr1aiNbF8Slb52k8LhKBpzN24K45NI5Q4f7Ew2ADy4nSHL%2Fl2IDK%2BWl664N%2FxNCCUb54Bn6ZpSqDgWVXOFBDraPF91r15GTcBdVidOUnG3g7tte3l6LS1sdXGVDVJgdheQzODNXDKCqpsUkypt2En37iy5CVe5SS3AwJ31PZW7BCzM2GRiewRk9MIyGH9wtTiekG3qXRSQWPmvWCWEgahQdzKR%2BrpGBIGaTrbVXS32yAUOpwNsb3yXDxu8G%2BAeBwHupT69VfDO3sGXp1EorSKvmMjcqHaCBT%2BhGVEr%2Bio6coX3U7d6P52qQ3S%2B6EYG3SbOSF48gRDOJmSOhwIctb%2FeZkBBVt6KvNKhqf%2BZM3M4R2vAAgtqG83FfUQq3BPOqjhqo3Ij8yyBDTpxBCQDJIUosXgZJPVraFOdLNAFcVBF2riSmdcrIxs39%2BviMw8v7hxAY6pgFHWjkHwXO4wcox%2F3TQBE2iZdS0goHUvgt%2Fw693lJJXrSjbsUv2yA0iLGP359ZTqdJtT59%2B4pxNe0j6OB3q%2BF%2BJSoAWHSyBW%2B8fxuWpQmJ2XsRiv0l5oZ3fbst7MNO%2FmHkfrBxYQkhc%2F8PMRHH16HiML%2BkQ6BbJPv73Qao427dlW%2FN7fXDaMEWETgzk85BlWR14da5XgMhtK0rcEgKyID8xt5zrQBvu&X-Amz-Signature=1ebdcb6d1991e5dda121544dd48db053e70f1c12549c0b9999e92b55b1ddf0b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Evaluation

### Experimental Setup

- Training configs

- Scaffolding

- Evaluation setup

- SFT baseline

### Main results

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/f0c1ed9f-e5b7-4769-bbd5-c2eaf4743012/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662THDCOVN%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDCjr209Hf20%2Bi%2FnxoXVjDtZDmDKiVbI9T5yBKaDXX5mAiAPdJWEx3gqNIsjAB5jOjZf2hIy7X3XbqxU%2FU8LbsHcCCqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrHmc4i4zG%2FMyUZR9KtwD8YsXqWwL9Ky2iSNB0uLsMxDb154VXgLhN7JNoB7LAFP3NtlYb5lOvwbWuu8i%2BNoMexqLJI%2FQcw8rwE6JOkoonC%2FD%2Bwu1Qoohs6Wrm1kyeckBO3xUDMbyjfGWz5B4GTKRB0DSsY%2F35RqYaZNXaip8GOWzguCY3C0ER71RbwBxpVIvv9MvpnhB%2B4OXmG5YVEBxpr1aiNbF8Slb52k8LhKBpzN24K45NI5Q4f7Ew2ADy4nSHL%2Fl2IDK%2BWl664N%2FxNCCUb54Bn6ZpSqDgWVXOFBDraPF91r15GTcBdVidOUnG3g7tte3l6LS1sdXGVDVJgdheQzODNXDKCqpsUkypt2En37iy5CVe5SS3AwJ31PZW7BCzM2GRiewRk9MIyGH9wtTiekG3qXRSQWPmvWCWEgahQdzKR%2BrpGBIGaTrbVXS32yAUOpwNsb3yXDxu8G%2BAeBwHupT69VfDO3sGXp1EorSKvmMjcqHaCBT%2BhGVEr%2Bio6coX3U7d6P52qQ3S%2B6EYG3SbOSF48gRDOJmSOhwIctb%2FeZkBBVt6KvNKhqf%2BZM3M4R2vAAgtqG83FfUQq3BPOqjhqo3Ij8yyBDTpxBCQDJIUosXgZJPVraFOdLNAFcVBF2riSmdcrIxs39%2BviMw8v7hxAY6pgFHWjkHwXO4wcox%2F3TQBE2iZdS0goHUvgt%2Fw693lJJXrSjbsUv2yA0iLGP359ZTqdJtT59%2B4pxNe0j6OB3q%2BF%2BJSoAWHSyBW%2B8fxuWpQmJ2XsRiv0l5oZ3fbst7MNO%2FmHkfrBxYQkhc%2F8PMRHH16HiML%2BkQ6BbJPv73Qao427dlW%2FN7fXDaMEWETgzk85BlWR14da5XgMhtK0rcEgKyID8xt5zrQBvu&X-Amz-Signature=9af52964dc214c155a0726d56ae3970f8c45bd6aecd8fdfc3396c6cafc110ae9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- GPT-4o 혹은 Claude-3.5-Sonnet의 결과를 Distillation한 Lingma-SWE-GPT, SWE-Gym, SWE-Fixer 등을 비교군으로 사용

- distillation data 구축 없이도 성능 압도

### Baseline comparison

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/995cea78-9200-45cc-80bc-621b970214bf/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662THDCOVN%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDCjr209Hf20%2Bi%2FnxoXVjDtZDmDKiVbI9T5yBKaDXX5mAiAPdJWEx3gqNIsjAB5jOjZf2hIy7X3XbqxU%2FU8LbsHcCCqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrHmc4i4zG%2FMyUZR9KtwD8YsXqWwL9Ky2iSNB0uLsMxDb154VXgLhN7JNoB7LAFP3NtlYb5lOvwbWuu8i%2BNoMexqLJI%2FQcw8rwE6JOkoonC%2FD%2Bwu1Qoohs6Wrm1kyeckBO3xUDMbyjfGWz5B4GTKRB0DSsY%2F35RqYaZNXaip8GOWzguCY3C0ER71RbwBxpVIvv9MvpnhB%2B4OXmG5YVEBxpr1aiNbF8Slb52k8LhKBpzN24K45NI5Q4f7Ew2ADy4nSHL%2Fl2IDK%2BWl664N%2FxNCCUb54Bn6ZpSqDgWVXOFBDraPF91r15GTcBdVidOUnG3g7tte3l6LS1sdXGVDVJgdheQzODNXDKCqpsUkypt2En37iy5CVe5SS3AwJ31PZW7BCzM2GRiewRk9MIyGH9wtTiekG3qXRSQWPmvWCWEgahQdzKR%2BrpGBIGaTrbVXS32yAUOpwNsb3yXDxu8G%2BAeBwHupT69VfDO3sGXp1EorSKvmMjcqHaCBT%2BhGVEr%2Bio6coX3U7d6P52qQ3S%2B6EYG3SbOSF48gRDOJmSOhwIctb%2FeZkBBVt6KvNKhqf%2BZM3M4R2vAAgtqG83FfUQq3BPOqjhqo3Ij8yyBDTpxBCQDJIUosXgZJPVraFOdLNAFcVBF2riSmdcrIxs39%2BviMw8v7hxAY6pgFHWjkHwXO4wcox%2F3TQBE2iZdS0goHUvgt%2Fw693lJJXrSjbsUv2yA0iLGP359ZTqdJtT59%2B4pxNe0j6OB3q%2BF%2BJSoAWHSyBW%2B8fxuWpQmJ2XsRiv0l5oZ3fbst7MNO%2FmHkfrBxYQkhc%2F8PMRHH16HiML%2BkQ6BbJPv73Qao427dlW%2FN7fXDaMEWETgzk85BlWR14da5XgMhtK0rcEgKyID8xt5zrQBvu&X-Amz-Signature=f54595d05883146649f6aa5a032f88faba3402489d3363244515fed7a00bb27c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Repair performance에 집중해 성능 분석

- Llama-3.3모델은 20개 샘플링해서 다수결해도 formatting에 어려움을 겪음

- RL은 formatting도 잘하면서 repair performance도 우수

### Scaling analysis with more samples

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/b85c12c8-c4de-4261-942c-62d11528e44b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662THDCOVN%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDCjr209Hf20%2Bi%2FnxoXVjDtZDmDKiVbI9T5yBKaDXX5mAiAPdJWEx3gqNIsjAB5jOjZf2hIy7X3XbqxU%2FU8LbsHcCCqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrHmc4i4zG%2FMyUZR9KtwD8YsXqWwL9Ky2iSNB0uLsMxDb154VXgLhN7JNoB7LAFP3NtlYb5lOvwbWuu8i%2BNoMexqLJI%2FQcw8rwE6JOkoonC%2FD%2Bwu1Qoohs6Wrm1kyeckBO3xUDMbyjfGWz5B4GTKRB0DSsY%2F35RqYaZNXaip8GOWzguCY3C0ER71RbwBxpVIvv9MvpnhB%2B4OXmG5YVEBxpr1aiNbF8Slb52k8LhKBpzN24K45NI5Q4f7Ew2ADy4nSHL%2Fl2IDK%2BWl664N%2FxNCCUb54Bn6ZpSqDgWVXOFBDraPF91r15GTcBdVidOUnG3g7tte3l6LS1sdXGVDVJgdheQzODNXDKCqpsUkypt2En37iy5CVe5SS3AwJ31PZW7BCzM2GRiewRk9MIyGH9wtTiekG3qXRSQWPmvWCWEgahQdzKR%2BrpGBIGaTrbVXS32yAUOpwNsb3yXDxu8G%2BAeBwHupT69VfDO3sGXp1EorSKvmMjcqHaCBT%2BhGVEr%2Bio6coX3U7d6P52qQ3S%2B6EYG3SbOSF48gRDOJmSOhwIctb%2FeZkBBVt6KvNKhqf%2BZM3M4R2vAAgtqG83FfUQq3BPOqjhqo3Ij8yyBDTpxBCQDJIUosXgZJPVraFOdLNAFcVBF2riSmdcrIxs39%2BviMw8v7hxAY6pgFHWjkHwXO4wcox%2F3TQBE2iZdS0goHUvgt%2Fw693lJJXrSjbsUv2yA0iLGP359ZTqdJtT59%2B4pxNe0j6OB3q%2BF%2BJSoAWHSyBW%2B8fxuWpQmJ2XsRiv0l5oZ3fbst7MNO%2FmHkfrBxYQkhc%2F8PMRHH16HiML%2BkQ6BbJPv73Qao427dlW%2FN7fXDaMEWETgzk85BlWR14da5XgMhtK0rcEgKyID8xt5zrQBvu&X-Amz-Signature=868b9a1e4bad8d0d502c12c43640c0921aee8909ec3544dd5129de4416d5c037&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- repair sample, test sample의 수를 조절하면서 성능 비교

- 어느정도 큰 수가 되면 성능이 수렴

### Generalizability of RL

- SWE-bench 외에도 function coding, library use, code reasoning등의 code 도메인의 다른 task에서도 성능이 향상됨

- 대단한건 MATH 성능이 크게 향상, MMLU 성능을 잃지 않음..!!!

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/7ab10067-00d5-4859-acbf-84c47f5d5bc2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662THDCOVN%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDCjr209Hf20%2Bi%2FnxoXVjDtZDmDKiVbI9T5yBKaDXX5mAiAPdJWEx3gqNIsjAB5jOjZf2hIy7X3XbqxU%2FU8LbsHcCCqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrHmc4i4zG%2FMyUZR9KtwD8YsXqWwL9Ky2iSNB0uLsMxDb154VXgLhN7JNoB7LAFP3NtlYb5lOvwbWuu8i%2BNoMexqLJI%2FQcw8rwE6JOkoonC%2FD%2Bwu1Qoohs6Wrm1kyeckBO3xUDMbyjfGWz5B4GTKRB0DSsY%2F35RqYaZNXaip8GOWzguCY3C0ER71RbwBxpVIvv9MvpnhB%2B4OXmG5YVEBxpr1aiNbF8Slb52k8LhKBpzN24K45NI5Q4f7Ew2ADy4nSHL%2Fl2IDK%2BWl664N%2FxNCCUb54Bn6ZpSqDgWVXOFBDraPF91r15GTcBdVidOUnG3g7tte3l6LS1sdXGVDVJgdheQzODNXDKCqpsUkypt2En37iy5CVe5SS3AwJ31PZW7BCzM2GRiewRk9MIyGH9wtTiekG3qXRSQWPmvWCWEgahQdzKR%2BrpGBIGaTrbVXS32yAUOpwNsb3yXDxu8G%2BAeBwHupT69VfDO3sGXp1EorSKvmMjcqHaCBT%2BhGVEr%2Bio6coX3U7d6P52qQ3S%2B6EYG3SbOSF48gRDOJmSOhwIctb%2FeZkBBVt6KvNKhqf%2BZM3M4R2vAAgtqG83FfUQq3BPOqjhqo3Ij8yyBDTpxBCQDJIUosXgZJPVraFOdLNAFcVBF2riSmdcrIxs39%2BviMw8v7hxAY6pgFHWjkHwXO4wcox%2F3TQBE2iZdS0goHUvgt%2Fw693lJJXrSjbsUv2yA0iLGP359ZTqdJtT59%2B4pxNe0j6OB3q%2BF%2BJSoAWHSyBW%2B8fxuWpQmJ2XsRiv0l5oZ3fbst7MNO%2FmHkfrBxYQkhc%2F8PMRHH16HiML%2BkQ6BbJPv73Qao427dlW%2FN7fXDaMEWETgzk85BlWR14da5XgMhtK0rcEgKyID8xt5zrQBvu&X-Amz-Signature=b8f6911c44732b9a0295b34ea3cb4b084b4388aaf50138ad1df815d68afd39b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Reward ablation

- reward를 0-1사이의 continuous값이 아니라 discrete한 값으로 주었을 때의 결과

- continuous가 낫다!

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/8ef19bd2-e0d9-46d5-89cb-eb0b02d288ba/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662THDCOVN%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDCjr209Hf20%2Bi%2FnxoXVjDtZDmDKiVbI9T5yBKaDXX5mAiAPdJWEx3gqNIsjAB5jOjZf2hIy7X3XbqxU%2FU8LbsHcCCqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrHmc4i4zG%2FMyUZR9KtwD8YsXqWwL9Ky2iSNB0uLsMxDb154VXgLhN7JNoB7LAFP3NtlYb5lOvwbWuu8i%2BNoMexqLJI%2FQcw8rwE6JOkoonC%2FD%2Bwu1Qoohs6Wrm1kyeckBO3xUDMbyjfGWz5B4GTKRB0DSsY%2F35RqYaZNXaip8GOWzguCY3C0ER71RbwBxpVIvv9MvpnhB%2B4OXmG5YVEBxpr1aiNbF8Slb52k8LhKBpzN24K45NI5Q4f7Ew2ADy4nSHL%2Fl2IDK%2BWl664N%2FxNCCUb54Bn6ZpSqDgWVXOFBDraPF91r15GTcBdVidOUnG3g7tte3l6LS1sdXGVDVJgdheQzODNXDKCqpsUkypt2En37iy5CVe5SS3AwJ31PZW7BCzM2GRiewRk9MIyGH9wtTiekG3qXRSQWPmvWCWEgahQdzKR%2BrpGBIGaTrbVXS32yAUOpwNsb3yXDxu8G%2BAeBwHupT69VfDO3sGXp1EorSKvmMjcqHaCBT%2BhGVEr%2Bio6coX3U7d6P52qQ3S%2B6EYG3SbOSF48gRDOJmSOhwIctb%2FeZkBBVt6KvNKhqf%2BZM3M4R2vAAgtqG83FfUQq3BPOqjhqo3Ij8yyBDTpxBCQDJIUosXgZJPVraFOdLNAFcVBF2riSmdcrIxs39%2BviMw8v7hxAY6pgFHWjkHwXO4wcox%2F3TQBE2iZdS0goHUvgt%2Fw693lJJXrSjbsUv2yA0iLGP359ZTqdJtT59%2B4pxNe0j6OB3q%2BF%2BJSoAWHSyBW%2B8fxuWpQmJ2XsRiv0l5oZ3fbst7MNO%2FmHkfrBxYQkhc%2F8PMRHH16HiML%2BkQ6BbJPv73Qao427dlW%2FN7fXDaMEWETgzk85BlWR14da5XgMhtK0rcEgKyID8xt5zrQBvu&X-Amz-Signature=438517228405c6b257b39666b2ebf1d46d480441de591e4de831e825cb64b720&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
