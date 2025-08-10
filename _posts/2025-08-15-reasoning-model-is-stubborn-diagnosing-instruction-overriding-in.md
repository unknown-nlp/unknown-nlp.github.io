---
categories:
  - paper-reviews
date: "2025-08-15 00:00:00"
description: 논문 리뷰
giscus_comments: true
layout: post
related_posts: false
slug: 2025-08-15-reasoning-model-is-stubborn-diagnosing-instruction-overriding-in
tags:
  - attention
  - embedding
  - llm
  - paper-review
  - reasoning
title: "Reasoning Model is Stubborn: Diagnosing Instruction Overriding in Reasoning
  Models"
---

**논문 정보**

- **Date**: 2025-07-15
- **Reviewer**: 전민진

## Abstract

- 최근 LLM이 복잡한 reasoning task에서 괄목할만한 성능을 보이고 있으나, (모델에게) 편한 reasoning pattern에 의존하는 경향이 있음

- 사용자의 명시적인 instruction이 있음에도 불구하고, 습관적인 reasoning trajectory를 생성, 오답으로 귀결

- 이를 분석하기 위해 reasoning trap이라는 진단 데이터셋을 도입

- reasoning trap을 통해서 모덷이 습관적으로 사용하는 reasoning pattern을 발견, 분류

## Introduction

- LLM은 수학, 복잡한 코딩 문제, 퍼즐 풀이를 포함한 여러 어려운 태스크에서 주목할만한 성능을 보임

- 하지만, 이러한 모델들에게 문제 행동, reasoning rigidity가 발견됨

- reasoning rigidity는 cognitive bias를 반영, 주어진 조건을 이해해도 자기 방식대로 override, 무시하고 문제를 푸는 현상을 뜻함

- reasoning rigidity는 사용자가 서술한 제약이 중요한 도메인에서 큰 문제가 됨

- reasoning rigidity를 식별할 수 있도록, 기존의 수학, 퍼즐 데이터셋을 활용해 reasoningtrap이라는 벤치마크를 제안

- ReasoningTrap으로 여러 모델을 평가한 결과, 여러 중요한 현상들을 발견

- 또한, 이러한 contamination의 패턴을 3가지로 분류

## Related Works

- Large Reasoning Models

- Instruction following of reasoning models

- Rigidity in reasoning models

- Underlying reason for rigidity

## ReasoningTrap: Reasoning Rigidity Diagnostic Set

### Data structure

- 크게 2가지로 도메인으로 구성 : 수학(ConditionedMath), 퍼즐(PuzzleTrivial)

- 각 데이터는 원래 Q-R-A tuple (q_orig, r_orig, a_orig)과 수정된 tuple (q_mod, r_mod, a_mod)로 구성

- 총 164개의 데이터셋, 84개는 수학, 80개는 퍼즐

- ConditionedMath에 있는 모든 질문은 개념적으로 다르고, 겹치지 않고, human annotator에 의해 엄격하게 검증됨

- PuzzleTrival은 10개의 puzzle concept를 가짐

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/116b04b4-827c-46d3-80a5-76001297c885/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642GNVKOJ%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7zpm6qJj%2B%2FT3MqYJHlbFHQJ%2FX2UrtvldABGabtEwnzwIgGumwWfpkz4iSUNno%2FBa%2BGXJwDEf%2Frp0XbTJGrSi0kyIqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIFwX7mIz9njxNVWvCrcA9H9r7VaUR18CbsfNsvPXhfMwSSQL7w2syE1r%2FeV2AceHv5XJpwjkZMf8Fy295x7%2BAOWEtUmYAy9yQ7IR6NSDflXWuHTEi0h4zZBFYUm%2BN7AzNIsHvkxtHdrF8QSVrQ1mj8t3tcw4yDfAlQ2SzKDn%2F3a2lONAoS0X7%2FjtLjXw3MLvIjBZNl%2Fe3x8olTvb%2FaEYM1I9D4AkopMxtS%2BS5o15gwSkjkQdNsKtKJm%2FMh9qWxRnnQ7bLIBjB50jPUABQTtMze%2FyoCz%2BnLo0gzYvQ7Uk7AH5FiK%2Bj%2BOw8vr2a0jPXRUlr6bKTU1A9QEZ8lUVtD058GvXZkQJxNsPEATZDsQwEvIC3VxlcG4eGPxvxgAopKgiIFKA4mN0X3Mkxma42eihQS5MkPtYOZJZFRsIr7i6d4jafKxILBsDCj27aqqvVKAyK03JR16kIQN91%2Fc2oDMgRs21mDizLuLpPm7sWgurjG4lHBHa7h6wYNHO08HtRW%2FvwmsBizOXSex3fhg3Q33uv0bA7LOh9Fh5XYk%2F1IMrlBur1sl65poO0bI4UnEzQCLKlR5VO1NxQRVupEJmG6Y%2FkzYQviWIDshI%2FANfGR3cLDI0ekX%2F%2FWm3anERRHsiUarYrUZGnmnibcPd4COMI3U4cQGOqUBm2tRTmuTZCJkfUFtDOd%2F70wgO03mY%2BMWptax%2Bq%2Bbiv4LkFbKYqkP4W6S38d9PwhyAhHo%2BU7FOruAzVp1DTkCNlFpElIdyPn8Sdkf4WitgksHw3RYio%2BtvkwDzG5QrGW0bTJolzK7Nr6%2B%2F%2FnrAMoE05fhgzknNarwZtZszc4QjC9YHYy37DydxxiLw1gc7bjSj%2BtuhWNAZ3%2Fa%2FWC9wcEjegbGSqY0&X-Amz-Signature=e1a36ff74957a903916860588ea652a08f65c9654792b37d6cf351218a1cea9c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**ConditionedMath: popular math benchmark with addtional conditions**

- AIME 2022-24 , MATH500 level 5를 활용해서 제작

- 원래 질문을 수정하고, 수정된 질문이 아래 조건에 부합하는지를 확인, 필터링

- 220개의 원본 데이터를 5가지의 variant로 modified, 필터링 후에 최종 84개만 남음

**PuzzleTrivial: Puzzles with subtle Modifications to Trivial Solutions**

- classic puzzle은 조건을 수정하면 급격하게 단순해지거나 답이 여러개일 수 있음

- ambiguity를 줄이기 위해, “valid solution을 위해 가장 간단한 답을 찾아라”라는 문구를 instruction에 추가

- 과정 자체는 위와 동일

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/3381b485-56c2-4439-b9da-81dce83ce7c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642GNVKOJ%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7zpm6qJj%2B%2FT3MqYJHlbFHQJ%2FX2UrtvldABGabtEwnzwIgGumwWfpkz4iSUNno%2FBa%2BGXJwDEf%2Frp0XbTJGrSi0kyIqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIFwX7mIz9njxNVWvCrcA9H9r7VaUR18CbsfNsvPXhfMwSSQL7w2syE1r%2FeV2AceHv5XJpwjkZMf8Fy295x7%2BAOWEtUmYAy9yQ7IR6NSDflXWuHTEi0h4zZBFYUm%2BN7AzNIsHvkxtHdrF8QSVrQ1mj8t3tcw4yDfAlQ2SzKDn%2F3a2lONAoS0X7%2FjtLjXw3MLvIjBZNl%2Fe3x8olTvb%2FaEYM1I9D4AkopMxtS%2BS5o15gwSkjkQdNsKtKJm%2FMh9qWxRnnQ7bLIBjB50jPUABQTtMze%2FyoCz%2BnLo0gzYvQ7Uk7AH5FiK%2Bj%2BOw8vr2a0jPXRUlr6bKTU1A9QEZ8lUVtD058GvXZkQJxNsPEATZDsQwEvIC3VxlcG4eGPxvxgAopKgiIFKA4mN0X3Mkxma42eihQS5MkPtYOZJZFRsIr7i6d4jafKxILBsDCj27aqqvVKAyK03JR16kIQN91%2Fc2oDMgRs21mDizLuLpPm7sWgurjG4lHBHa7h6wYNHO08HtRW%2FvwmsBizOXSex3fhg3Q33uv0bA7LOh9Fh5XYk%2F1IMrlBur1sl65poO0bI4UnEzQCLKlR5VO1NxQRVupEJmG6Y%2FkzYQviWIDshI%2FANfGR3cLDI0ekX%2F%2FWm3anERRHsiUarYrUZGnmnibcPd4COMI3U4cQGOqUBm2tRTmuTZCJkfUFtDOd%2F70wgO03mY%2BMWptax%2Bq%2Bbiv4LkFbKYqkP4W6S38d9PwhyAhHo%2BU7FOruAzVp1DTkCNlFpElIdyPn8Sdkf4WitgksHw3RYio%2BtvkwDzG5QrGW0bTJolzK7Nr6%2B%2F%2FnrAMoE05fhgzknNarwZtZszc4QjC9YHYy37DydxxiLw1gc7bjSj%2BtuhWNAZ3%2Fa%2FWC9wcEjegbGSqY0&X-Amz-Signature=53d7f78cca1a85c2434e0410c9ef32dcb9a93b7fb84ece33a0f0b7d92001ec88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Contamination Ratio and Early Detection Algorithm

- 시스템적으로 reasoning model의 contamination을 측정하기 위해서, Contamination ratio를 제안

**Contamination Ratio in Synthetic Dataset**

- 모델이 문제를 풀 때, 수정된 조건을 이해하고 풀었는지 이해하지 않고 풀었는지를 구분하기 위해 metric을 도입

- 생성된 reasoning path를 단락별로 쪼개고, 각 단락을 textual representation으로 embedding

- 각 단락과 오리지널 문제의 reasoning path, 각 단락과 modified reasoning path와의 cosine 유사도를 계산, 둘을 비교해 original reasoning path와의 유사도가 더 높을 경우 1로 계산

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/ce44517f-dd76-42b5-bc57-545202ff74b1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642GNVKOJ%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7zpm6qJj%2B%2FT3MqYJHlbFHQJ%2FX2UrtvldABGabtEwnzwIgGumwWfpkz4iSUNno%2FBa%2BGXJwDEf%2Frp0XbTJGrSi0kyIqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIFwX7mIz9njxNVWvCrcA9H9r7VaUR18CbsfNsvPXhfMwSSQL7w2syE1r%2FeV2AceHv5XJpwjkZMf8Fy295x7%2BAOWEtUmYAy9yQ7IR6NSDflXWuHTEi0h4zZBFYUm%2BN7AzNIsHvkxtHdrF8QSVrQ1mj8t3tcw4yDfAlQ2SzKDn%2F3a2lONAoS0X7%2FjtLjXw3MLvIjBZNl%2Fe3x8olTvb%2FaEYM1I9D4AkopMxtS%2BS5o15gwSkjkQdNsKtKJm%2FMh9qWxRnnQ7bLIBjB50jPUABQTtMze%2FyoCz%2BnLo0gzYvQ7Uk7AH5FiK%2Bj%2BOw8vr2a0jPXRUlr6bKTU1A9QEZ8lUVtD058GvXZkQJxNsPEATZDsQwEvIC3VxlcG4eGPxvxgAopKgiIFKA4mN0X3Mkxma42eihQS5MkPtYOZJZFRsIr7i6d4jafKxILBsDCj27aqqvVKAyK03JR16kIQN91%2Fc2oDMgRs21mDizLuLpPm7sWgurjG4lHBHa7h6wYNHO08HtRW%2FvwmsBizOXSex3fhg3Q33uv0bA7LOh9Fh5XYk%2F1IMrlBur1sl65poO0bI4UnEzQCLKlR5VO1NxQRVupEJmG6Y%2FkzYQviWIDshI%2FANfGR3cLDI0ekX%2F%2FWm3anERRHsiUarYrUZGnmnibcPd4COMI3U4cQGOqUBm2tRTmuTZCJkfUFtDOd%2F70wgO03mY%2BMWptax%2Bq%2Bbiv4LkFbKYqkP4W6S38d9PwhyAhHo%2BU7FOruAzVp1DTkCNlFpElIdyPn8Sdkf4WitgksHw3RYio%2BtvkwDzG5QrGW0bTJolzK7Nr6%2B%2F%2FnrAMoE05fhgzknNarwZtZszc4QjC9YHYy37DydxxiLw1gc7bjSj%2BtuhWNAZ3%2Fa%2FWC9wcEjegbGSqY0&X-Amz-Signature=8684317dcc4ee44b91c3131166fea8c2acc137e6a0ed2a26805f884e13ffa086&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**Evaluation of Reasoning Rigidity**

- reasoning rigidity를 잘 관찰하기 위해, 모델이 수정된 조건을 이해했는데도 습관처럼 풀었는지 아니면 인지조차 하지 못했는지를 구분

- 이를 반영한 metric을 p-passs@k라고 정의, reasosning path에서 constraint를 인지하고 있는 경우에만 accuracy를 측정

- constraint를 인지했는지는 모델이 생성한 reasoning path중 첫 15개의 단락과 정답, 질문을 LLM에 넣고 판단하도록 함(p_i)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/f399899f-e285-4d1e-b0e8-73125d3f93ad/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642GNVKOJ%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7zpm6qJj%2B%2FT3MqYJHlbFHQJ%2FX2UrtvldABGabtEwnzwIgGumwWfpkz4iSUNno%2FBa%2BGXJwDEf%2Frp0XbTJGrSi0kyIqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIFwX7mIz9njxNVWvCrcA9H9r7VaUR18CbsfNsvPXhfMwSSQL7w2syE1r%2FeV2AceHv5XJpwjkZMf8Fy295x7%2BAOWEtUmYAy9yQ7IR6NSDflXWuHTEi0h4zZBFYUm%2BN7AzNIsHvkxtHdrF8QSVrQ1mj8t3tcw4yDfAlQ2SzKDn%2F3a2lONAoS0X7%2FjtLjXw3MLvIjBZNl%2Fe3x8olTvb%2FaEYM1I9D4AkopMxtS%2BS5o15gwSkjkQdNsKtKJm%2FMh9qWxRnnQ7bLIBjB50jPUABQTtMze%2FyoCz%2BnLo0gzYvQ7Uk7AH5FiK%2Bj%2BOw8vr2a0jPXRUlr6bKTU1A9QEZ8lUVtD058GvXZkQJxNsPEATZDsQwEvIC3VxlcG4eGPxvxgAopKgiIFKA4mN0X3Mkxma42eihQS5MkPtYOZJZFRsIr7i6d4jafKxILBsDCj27aqqvVKAyK03JR16kIQN91%2Fc2oDMgRs21mDizLuLpPm7sWgurjG4lHBHa7h6wYNHO08HtRW%2FvwmsBizOXSex3fhg3Q33uv0bA7LOh9Fh5XYk%2F1IMrlBur1sl65poO0bI4UnEzQCLKlR5VO1NxQRVupEJmG6Y%2FkzYQviWIDshI%2FANfGR3cLDI0ekX%2F%2FWm3anERRHsiUarYrUZGnmnibcPd4COMI3U4cQGOqUBm2tRTmuTZCJkfUFtDOd%2F70wgO03mY%2BMWptax%2Bq%2Bbiv4LkFbKYqkP4W6S38d9PwhyAhHo%2BU7FOruAzVp1DTkCNlFpElIdyPn8Sdkf4WitgksHw3RYio%2BtvkwDzG5QrGW0bTJolzK7Nr6%2B%2F%2FnrAMoE05fhgzknNarwZtZszc4QjC9YHYy37DydxxiLw1gc7bjSj%2BtuhWNAZ3%2Fa%2FWC9wcEjegbGSqY0&X-Amz-Signature=8534c865dce64f843fd27f4202910cbd2b437567a7a27c55f208ebdd26787f67&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/00631d4b-bfc6-4499-b9dd-ba640642bc0f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642GNVKOJ%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7zpm6qJj%2B%2FT3MqYJHlbFHQJ%2FX2UrtvldABGabtEwnzwIgGumwWfpkz4iSUNno%2FBa%2BGXJwDEf%2Frp0XbTJGrSi0kyIqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIFwX7mIz9njxNVWvCrcA9H9r7VaUR18CbsfNsvPXhfMwSSQL7w2syE1r%2FeV2AceHv5XJpwjkZMf8Fy295x7%2BAOWEtUmYAy9yQ7IR6NSDflXWuHTEi0h4zZBFYUm%2BN7AzNIsHvkxtHdrF8QSVrQ1mj8t3tcw4yDfAlQ2SzKDn%2F3a2lONAoS0X7%2FjtLjXw3MLvIjBZNl%2Fe3x8olTvb%2FaEYM1I9D4AkopMxtS%2BS5o15gwSkjkQdNsKtKJm%2FMh9qWxRnnQ7bLIBjB50jPUABQTtMze%2FyoCz%2BnLo0gzYvQ7Uk7AH5FiK%2Bj%2BOw8vr2a0jPXRUlr6bKTU1A9QEZ8lUVtD058GvXZkQJxNsPEATZDsQwEvIC3VxlcG4eGPxvxgAopKgiIFKA4mN0X3Mkxma42eihQS5MkPtYOZJZFRsIr7i6d4jafKxILBsDCj27aqqvVKAyK03JR16kIQN91%2Fc2oDMgRs21mDizLuLpPm7sWgurjG4lHBHa7h6wYNHO08HtRW%2FvwmsBizOXSex3fhg3Q33uv0bA7LOh9Fh5XYk%2F1IMrlBur1sl65poO0bI4UnEzQCLKlR5VO1NxQRVupEJmG6Y%2FkzYQviWIDshI%2FANfGR3cLDI0ekX%2F%2FWm3anERRHsiUarYrUZGnmnibcPd4COMI3U4cQGOqUBm2tRTmuTZCJkfUFtDOd%2F70wgO03mY%2BMWptax%2Bq%2Bbiv4LkFbKYqkP4W6S38d9PwhyAhHo%2BU7FOruAzVp1DTkCNlFpElIdyPn8Sdkf4WitgksHw3RYio%2BtvkwDzG5QrGW0bTJolzK7Nr6%2B%2F%2FnrAMoE05fhgzknNarwZtZszc4QjC9YHYy37DydxxiLw1gc7bjSj%2BtuhWNAZ3%2Fa%2FWC9wcEjegbGSqY0&X-Amz-Signature=6af989eec9f6ea8caceaacdcaaedda77586c82a4d4ecde97bfd6189b59c67e9d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Signals for Contamination in Realistic Situation

- question만 주어지는 현실적인 상황에서, generated reasosning이 원치 않지만 친숙한 pattern으로 contaminated됐는지 자동적으로 식별하는 것을 불가능

- 그래서 간단하게, contamination의 종류를 분류해서, 각 type별 의심스러운 pattern을 식별

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/b6b17efd-320c-4e2d-bae2-407969e2e701/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642GNVKOJ%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7zpm6qJj%2B%2FT3MqYJHlbFHQJ%2FX2UrtvldABGabtEwnzwIgGumwWfpkz4iSUNno%2FBa%2BGXJwDEf%2Frp0XbTJGrSi0kyIqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIFwX7mIz9njxNVWvCrcA9H9r7VaUR18CbsfNsvPXhfMwSSQL7w2syE1r%2FeV2AceHv5XJpwjkZMf8Fy295x7%2BAOWEtUmYAy9yQ7IR6NSDflXWuHTEi0h4zZBFYUm%2BN7AzNIsHvkxtHdrF8QSVrQ1mj8t3tcw4yDfAlQ2SzKDn%2F3a2lONAoS0X7%2FjtLjXw3MLvIjBZNl%2Fe3x8olTvb%2FaEYM1I9D4AkopMxtS%2BS5o15gwSkjkQdNsKtKJm%2FMh9qWxRnnQ7bLIBjB50jPUABQTtMze%2FyoCz%2BnLo0gzYvQ7Uk7AH5FiK%2Bj%2BOw8vr2a0jPXRUlr6bKTU1A9QEZ8lUVtD058GvXZkQJxNsPEATZDsQwEvIC3VxlcG4eGPxvxgAopKgiIFKA4mN0X3Mkxma42eihQS5MkPtYOZJZFRsIr7i6d4jafKxILBsDCj27aqqvVKAyK03JR16kIQN91%2Fc2oDMgRs21mDizLuLpPm7sWgurjG4lHBHa7h6wYNHO08HtRW%2FvwmsBizOXSex3fhg3Q33uv0bA7LOh9Fh5XYk%2F1IMrlBur1sl65poO0bI4UnEzQCLKlR5VO1NxQRVupEJmG6Y%2FkzYQviWIDshI%2FANfGR3cLDI0ekX%2F%2FWm3anERRHsiUarYrUZGnmnibcPd4COMI3U4cQGOqUBm2tRTmuTZCJkfUFtDOd%2F70wgO03mY%2BMWptax%2Bq%2Bbiv4LkFbKYqkP4W6S38d9PwhyAhHo%2BU7FOruAzVp1DTkCNlFpElIdyPn8Sdkf4WitgksHw3RYio%2BtvkwDzG5QrGW0bTJolzK7Nr6%2B%2F%2FnrAMoE05fhgzknNarwZtZszc4QjC9YHYy37DydxxiLw1gc7bjSj%2BtuhWNAZ3%2Fa%2FWC9wcEjegbGSqY0&X-Amz-Signature=295f9f25dbc2d81f81c56a303187d12bc3fb277f72b3ac75641bf72128af1f3f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Interpretation overload : 모델이 주어진 문제 조건을 거절하는 것으로 시작, 문제를 바로 해석하는 것보다 여러 방식으로 재해석. 보통 reasoning 중간 단계에서 발생, inconsistent 혹은 contraditory한 결론을 야기

- Input Distrust : 모델이 번역 오류, input error, typo존재 등을 가정함. 직관적으로 바로 문제를 풀 수 있음에도 부정하고 매우 복잡하게 풀게 됨.

- Partial Instruction Attention : 모델이 제공된 instruction의 일부분만을 선택적으로 집중

## Experiments

- ReasoningTrap을 여러 LLM에 inference

- 실험은 CoT prompting을 사용, ‘Please reason step by step, and put your final answer within \boxed{}.\n\n{Question}’ 포맷으로 질문을 전달

- table 2,3은 16번 sampling, 다른 실험은 4번 sampling

- 수학 문제의 경우, exat matching으로 correctness 판단, puzzle의 경우 free-from sentence로 답이 구성되다 보니, LLM을 사용해서 정답과 모델 답변을 함께 제공해 correctness를 판단

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/723a978c-8909-4555-be80-5f175dd3071c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642GNVKOJ%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7zpm6qJj%2B%2FT3MqYJHlbFHQJ%2FX2UrtvldABGabtEwnzwIgGumwWfpkz4iSUNno%2FBa%2BGXJwDEf%2Frp0XbTJGrSi0kyIqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIFwX7mIz9njxNVWvCrcA9H9r7VaUR18CbsfNsvPXhfMwSSQL7w2syE1r%2FeV2AceHv5XJpwjkZMf8Fy295x7%2BAOWEtUmYAy9yQ7IR6NSDflXWuHTEi0h4zZBFYUm%2BN7AzNIsHvkxtHdrF8QSVrQ1mj8t3tcw4yDfAlQ2SzKDn%2F3a2lONAoS0X7%2FjtLjXw3MLvIjBZNl%2Fe3x8olTvb%2FaEYM1I9D4AkopMxtS%2BS5o15gwSkjkQdNsKtKJm%2FMh9qWxRnnQ7bLIBjB50jPUABQTtMze%2FyoCz%2BnLo0gzYvQ7Uk7AH5FiK%2Bj%2BOw8vr2a0jPXRUlr6bKTU1A9QEZ8lUVtD058GvXZkQJxNsPEATZDsQwEvIC3VxlcG4eGPxvxgAopKgiIFKA4mN0X3Mkxma42eihQS5MkPtYOZJZFRsIr7i6d4jafKxILBsDCj27aqqvVKAyK03JR16kIQN91%2Fc2oDMgRs21mDizLuLpPm7sWgurjG4lHBHa7h6wYNHO08HtRW%2FvwmsBizOXSex3fhg3Q33uv0bA7LOh9Fh5XYk%2F1IMrlBur1sl65poO0bI4UnEzQCLKlR5VO1NxQRVupEJmG6Y%2FkzYQviWIDshI%2FANfGR3cLDI0ekX%2F%2FWm3anERRHsiUarYrUZGnmnibcPd4COMI3U4cQGOqUBm2tRTmuTZCJkfUFtDOd%2F70wgO03mY%2BMWptax%2Bq%2Bbiv4LkFbKYqkP4W6S38d9PwhyAhHo%2BU7FOruAzVp1DTkCNlFpElIdyPn8Sdkf4WitgksHw3RYio%2BtvkwDzG5QrGW0bTJolzK7Nr6%2B%2F%2FnrAMoE05fhgzknNarwZtZszc4QjC9YHYy37DydxxiLw1gc7bjSj%2BtuhWNAZ3%2Fa%2FWC9wcEjegbGSqY0&X-Amz-Signature=958be257ce819a8019616fbbc4726b5a978fd9b0e94e312a0f71a7b1f4e78fda&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 실험 결과, 대부분 reason모드일 때보다 base모드에서 더 높은 성능을 보임

- Buget forcing : 버짓 마지막에 ‘Considering the limited time by the user, I have to give the solution based on the thinking directly now.</think>’를 추가하여 답을 바로 내도록 함

- prompt hinting : 문제에 오타 없고 지시 그대로 하라는 prompt를 추가

- 실험 결과, budget이 커질 수록 성능이 악화됨

- prompt로 hint를 줘도 여전히 reasoning rigidity가 존재

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/dc9954e6-e510-4259-8718-cd0a879019c9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642GNVKOJ%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T105954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7zpm6qJj%2B%2FT3MqYJHlbFHQJ%2FX2UrtvldABGabtEwnzwIgGumwWfpkz4iSUNno%2FBa%2BGXJwDEf%2Frp0XbTJGrSi0kyIqiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIFwX7mIz9njxNVWvCrcA9H9r7VaUR18CbsfNsvPXhfMwSSQL7w2syE1r%2FeV2AceHv5XJpwjkZMf8Fy295x7%2BAOWEtUmYAy9yQ7IR6NSDflXWuHTEi0h4zZBFYUm%2BN7AzNIsHvkxtHdrF8QSVrQ1mj8t3tcw4yDfAlQ2SzKDn%2F3a2lONAoS0X7%2FjtLjXw3MLvIjBZNl%2Fe3x8olTvb%2FaEYM1I9D4AkopMxtS%2BS5o15gwSkjkQdNsKtKJm%2FMh9qWxRnnQ7bLIBjB50jPUABQTtMze%2FyoCz%2BnLo0gzYvQ7Uk7AH5FiK%2Bj%2BOw8vr2a0jPXRUlr6bKTU1A9QEZ8lUVtD058GvXZkQJxNsPEATZDsQwEvIC3VxlcG4eGPxvxgAopKgiIFKA4mN0X3Mkxma42eihQS5MkPtYOZJZFRsIr7i6d4jafKxILBsDCj27aqqvVKAyK03JR16kIQN91%2Fc2oDMgRs21mDizLuLpPm7sWgurjG4lHBHa7h6wYNHO08HtRW%2FvwmsBizOXSex3fhg3Q33uv0bA7LOh9Fh5XYk%2F1IMrlBur1sl65poO0bI4UnEzQCLKlR5VO1NxQRVupEJmG6Y%2FkzYQviWIDshI%2FANfGR3cLDI0ekX%2F%2FWm3anERRHsiUarYrUZGnmnibcPd4COMI3U4cQGOqUBm2tRTmuTZCJkfUFtDOd%2F70wgO03mY%2BMWptax%2Bq%2Bbiv4LkFbKYqkP4W6S38d9PwhyAhHo%2BU7FOruAzVp1DTkCNlFpElIdyPn8Sdkf4WitgksHw3RYio%2BtvkwDzG5QrGW0bTJolzK7Nr6%2B%2F%2FnrAMoE05fhgzknNarwZtZszc4QjC9YHYy37DydxxiLw1gc7bjSj%2BtuhWNAZ3%2Fa%2FWC9wcEjegbGSqY0&X-Amz-Signature=9dfb918af073df137e1abf38375f9dae7cd3b4ca99134a0e73c0ca7c71d6529c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 모델 크기에 따른 실험. base모델이 성능이 전반적으로 높게 나오는 편
