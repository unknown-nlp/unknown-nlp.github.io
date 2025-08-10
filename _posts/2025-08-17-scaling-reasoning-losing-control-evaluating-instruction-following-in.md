---
categories:
  - paper-reviews
date: "2025-08-17 00:00:00"
description: 논문 리뷰
giscus_comments: true
layout: post
related_posts: false
slug: 2025-08-17-scaling-reasoning-losing-control-evaluating-instruction-following-in
tags:
  - attention
  - llm
  - paper-review
  - reasoning
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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/034fc1f8-3069-42bd-9c65-b951653705dc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OBPDM7K%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtCLUb1XplJDxZN1xV2IlajPdhJrtAFKY4G%2FzrOvIxNAIgMzqyh%2FmMb4AwU%2FSb%2FNS%2F2WC%2B5HUF9RH%2FWy1urhXPs38qiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCDVPfC3oYwdt0jKXCrcA0F0RZs0QxziEBxsN30e68F0AuunQC%2FKvxemRY%2ByVvYF%2Fpr%2BG7ewimWET3y6I5PErBNcM2iFWXtnqfwwfvs19Gxda30l%2FlGT1QNZmu9zfWAvu3GkvEWss1ND6aIfSQnEfZoWwhX%2B0IuqhwP9D%2BD72PEQ3UZq6Im87DLmrD2bdKQxJ5P0VX8bnMIqlOLfqBW2zO3%2FXfSr37m3%2F042qvqtZ3j3VfpztmAHeQAb8HVJDBro1v0OlSIL5m9EdKK%2FfP%2FspPRCefvFCi6wMf4msGfHNkDwOZRr11FqZNpqcR3%2BqH2hRPgmqJ0L8jkwM8P%2BM2t9uEF8K0BWoc2o5A5CIL3AlJegEotOmADXj8KeKa8Cd3s1Gp97dlJHY8kOkyPqCQLECCa6D3YiNRSxcCK0yBxs46SxEz4%2FMm4yTRyYwjobeVtA%2BeOjPpndtLl697QSIn21nwhAYHxBegjpBl9qwI7zbPg8nqSdPNnGP0WDUJsZy%2B4yRs0eEz39Ko%2Fbw2wKkgg6eqvAi820mqsXfNfLPqloh1QUUhhYVnzktpDCQXYnXNTpkW72%2FlrhhRK2R92sa4DuPLZzzm%2FkgkzZ26nROVjNn3qIdowHHoRDGpMBBIfSz2HFfTBVGEph1aSqJeRwMJfU4cQGOqUBp9bu42ljWc8lCnP5QftBDG6oYZmMY0xEDuxGpLy2ejWyClRi822WiGMBF1tZ4JY%2FCbHQzXIoCmJRzQbVaPwkm0VO0TdUmz78eDaBxisWaINBK5ljKACm9QY716gZ6CUD66gik1qrKcrJcpPW%2FomobtCJF7rrzytoYRipLG8RgmeJIv0NcFTwHevwq%2B1BBdbJMRqccSnxD4xV6CLpDninrNcer5lY&X-Amz-Signature=37437ec058ae23f8342d321b8823989560ecb050507ec6b59d6c108ca669338b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 모든 LRM은 IF성능이 하락함

- Qwen3 시리즈가 그나마 높은 IF 성능을 보임

- 모델 크기가 IF 성능을 결정하진 않음

- 명시적인 reasoning seperation (<think>,</think>)가 있는 모델이 전반적으로 IF 성능이 높음

- instruction-following과 mathematical reasoning사이에 trade-off가 존재

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/5eac7dbd-7f1e-4164-811f-c770cdb9e064/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OBPDM7K%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtCLUb1XplJDxZN1xV2IlajPdhJrtAFKY4G%2FzrOvIxNAIgMzqyh%2FmMb4AwU%2FSb%2FNS%2F2WC%2B5HUF9RH%2FWy1urhXPs38qiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCDVPfC3oYwdt0jKXCrcA0F0RZs0QxziEBxsN30e68F0AuunQC%2FKvxemRY%2ByVvYF%2Fpr%2BG7ewimWET3y6I5PErBNcM2iFWXtnqfwwfvs19Gxda30l%2FlGT1QNZmu9zfWAvu3GkvEWss1ND6aIfSQnEfZoWwhX%2B0IuqhwP9D%2BD72PEQ3UZq6Im87DLmrD2bdKQxJ5P0VX8bnMIqlOLfqBW2zO3%2FXfSr37m3%2F042qvqtZ3j3VfpztmAHeQAb8HVJDBro1v0OlSIL5m9EdKK%2FfP%2FspPRCefvFCi6wMf4msGfHNkDwOZRr11FqZNpqcR3%2BqH2hRPgmqJ0L8jkwM8P%2BM2t9uEF8K0BWoc2o5A5CIL3AlJegEotOmADXj8KeKa8Cd3s1Gp97dlJHY8kOkyPqCQLECCa6D3YiNRSxcCK0yBxs46SxEz4%2FMm4yTRyYwjobeVtA%2BeOjPpndtLl697QSIn21nwhAYHxBegjpBl9qwI7zbPg8nqSdPNnGP0WDUJsZy%2B4yRs0eEz39Ko%2Fbw2wKkgg6eqvAi820mqsXfNfLPqloh1QUUhhYVnzktpDCQXYnXNTpkW72%2FlrhhRK2R92sa4DuPLZzzm%2FkgkzZ26nROVjNn3qIdowHHoRDGpMBBIfSz2HFfTBVGEph1aSqJeRwMJfU4cQGOqUBp9bu42ljWc8lCnP5QftBDG6oYZmMY0xEDuxGpLy2ejWyClRi822WiGMBF1tZ4JY%2FCbHQzXIoCmJRzQbVaPwkm0VO0TdUmz78eDaBxisWaINBK5ljKACm9QY716gZ6CUD66gik1qrKcrJcpPW%2FomobtCJF7rrzytoYRipLG8RgmeJIv0NcFTwHevwq%2B1BBdbJMRqccSnxD4xV6CLpDninrNcer5lY&X-Amz-Signature=9b70b96db5d5e77e15b11c8b2b794681df0c4485bbb3f2ed3be87a37b3f38681&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 제약조건을 만족하면서 문제를 맞추는 경우는 크지 않음

- 보통 제약조건 혹은 문제 하나만을 만족함 + 즉, 제약조건을 걸면 문제 풀이 성능이 하락

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/f1bd8edc-c4b9-4ad3-9ffd-1f24a730e21a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OBPDM7K%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtCLUb1XplJDxZN1xV2IlajPdhJrtAFKY4G%2FzrOvIxNAIgMzqyh%2FmMb4AwU%2FSb%2FNS%2F2WC%2B5HUF9RH%2FWy1urhXPs38qiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCDVPfC3oYwdt0jKXCrcA0F0RZs0QxziEBxsN30e68F0AuunQC%2FKvxemRY%2ByVvYF%2Fpr%2BG7ewimWET3y6I5PErBNcM2iFWXtnqfwwfvs19Gxda30l%2FlGT1QNZmu9zfWAvu3GkvEWss1ND6aIfSQnEfZoWwhX%2B0IuqhwP9D%2BD72PEQ3UZq6Im87DLmrD2bdKQxJ5P0VX8bnMIqlOLfqBW2zO3%2FXfSr37m3%2F042qvqtZ3j3VfpztmAHeQAb8HVJDBro1v0OlSIL5m9EdKK%2FfP%2FspPRCefvFCi6wMf4msGfHNkDwOZRr11FqZNpqcR3%2BqH2hRPgmqJ0L8jkwM8P%2BM2t9uEF8K0BWoc2o5A5CIL3AlJegEotOmADXj8KeKa8Cd3s1Gp97dlJHY8kOkyPqCQLECCa6D3YiNRSxcCK0yBxs46SxEz4%2FMm4yTRyYwjobeVtA%2BeOjPpndtLl697QSIn21nwhAYHxBegjpBl9qwI7zbPg8nqSdPNnGP0WDUJsZy%2B4yRs0eEz39Ko%2Fbw2wKkgg6eqvAi820mqsXfNfLPqloh1QUUhhYVnzktpDCQXYnXNTpkW72%2FlrhhRK2R92sa4DuPLZzzm%2FkgkzZ26nROVjNn3qIdowHHoRDGpMBBIfSz2HFfTBVGEph1aSqJeRwMJfU4cQGOqUBp9bu42ljWc8lCnP5QftBDG6oYZmMY0xEDuxGpLy2ejWyClRi822WiGMBF1tZ4JY%2FCbHQzXIoCmJRzQbVaPwkm0VO0TdUmz78eDaBxisWaINBK5ljKACm9QY716gZ6CUD66gik1qrKcrJcpPW%2FomobtCJF7rrzytoYRipLG8RgmeJIv0NcFTwHevwq%2B1BBdbJMRqccSnxD4xV6CLpDninrNcer5lY&X-Amz-Signature=a2354bcd2de03dda6778089a143e24aef98cd0408db1791c52ed52651047b869&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- IF가 낮았던 Qwen2.5를 대상으로 실험, 데이터는 deepscalar를 사용, QwQ로 CoT생성, 정답을 맞추면서 너무 길지 않은 애들만 필터링해서 학습에 사용

- 실험 결과, reasoning-orienteed 방법론이 reasoning성능은 향상시키지만 IF는 하락하는 것을 볼 수 있음

Figure 7

- 모델이 reasonign path를 종료하려고 할 때마다 wait를 걸어서 강제로 CoT길이를 늘림

- CoT길이가 길어질수록 constraint instruction과 멀어져서 constraint에 대한 acc가 떨어지는 것으로 추론

Table 5

- cold-RL에서 roll-out 길이를 조정하며 학습, 길어질수록 reasoning은 향상되나 IF는 떨어짐

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/c8bc4577-c051-4e0e-9dcb-117865f76d3c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OBPDM7K%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtCLUb1XplJDxZN1xV2IlajPdhJrtAFKY4G%2FzrOvIxNAIgMzqyh%2FmMb4AwU%2FSb%2FNS%2F2WC%2B5HUF9RH%2FWy1urhXPs38qiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCDVPfC3oYwdt0jKXCrcA0F0RZs0QxziEBxsN30e68F0AuunQC%2FKvxemRY%2ByVvYF%2Fpr%2BG7ewimWET3y6I5PErBNcM2iFWXtnqfwwfvs19Gxda30l%2FlGT1QNZmu9zfWAvu3GkvEWss1ND6aIfSQnEfZoWwhX%2B0IuqhwP9D%2BD72PEQ3UZq6Im87DLmrD2bdKQxJ5P0VX8bnMIqlOLfqBW2zO3%2FXfSr37m3%2F042qvqtZ3j3VfpztmAHeQAb8HVJDBro1v0OlSIL5m9EdKK%2FfP%2FspPRCefvFCi6wMf4msGfHNkDwOZRr11FqZNpqcR3%2BqH2hRPgmqJ0L8jkwM8P%2BM2t9uEF8K0BWoc2o5A5CIL3AlJegEotOmADXj8KeKa8Cd3s1Gp97dlJHY8kOkyPqCQLECCa6D3YiNRSxcCK0yBxs46SxEz4%2FMm4yTRyYwjobeVtA%2BeOjPpndtLl697QSIn21nwhAYHxBegjpBl9qwI7zbPg8nqSdPNnGP0WDUJsZy%2B4yRs0eEz39Ko%2Fbw2wKkgg6eqvAi820mqsXfNfLPqloh1QUUhhYVnzktpDCQXYnXNTpkW72%2FlrhhRK2R92sa4DuPLZzzm%2FkgkzZ26nROVjNn3qIdowHHoRDGpMBBIfSz2HFfTBVGEph1aSqJeRwMJfU4cQGOqUBp9bu42ljWc8lCnP5QftBDG6oYZmMY0xEDuxGpLy2ejWyClRi822WiGMBF1tZ4JY%2FCbHQzXIoCmJRzQbVaPwkm0VO0TdUmz78eDaBxisWaINBK5ljKACm9QY716gZ6CUD66gik1qrKcrJcpPW%2FomobtCJF7rrzytoYRipLG8RgmeJIv0NcFTwHevwq%2B1BBdbJMRqccSnxD4xV6CLpDninrNcer5lY&X-Amz-Signature=da4113991cfd1c535288dcfdae9e71a1d5c212a22146deaea9848bc6d66e2c1c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 간단하게 reasoning이 끝나갈 때 쯤에 wait을 넣고 constraint instruction을 반복해서 넣어준 경우의 성능을 측정

- IF성능은 향상되나 Correctness는 하락하는 것을 볼 수 있음

## Conclusion

- Reasoning-oriented model들이 생각보다 instruction following 성능이 악화됨

- 대부분 간단한 형식에 대한 제약인데도, 제약이 있을 때와 없을 때의 성능 차이가 큰게 충격적

- LLM이 정말 reasoning을 하는걸까? 그냥 답변 길이가 길어져서 발생하는 attention sink일까?
