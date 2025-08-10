---
categories:
- paper-reviews
date: '2025-01-02 00:00:00'
description: 논문 리뷰 - Robotics, Evaluation Metric 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- evaluation metric
- multimodal
- paper-review
- robotics
- transformer
- vision
thumbnail: assets/img/posts/2025-01-02-tracevla-visual-trace-prompting-enhances-spatial-temporal-awareness/thumbnail.jpg
title: 'TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist
  Robotic Policies'
---

**논문 정보**
- **Date**: 2025-01-02
- **Reviewer**: 전민진
- **Property**: Robotics, Evaluation Metric

## Abstract

- 기존 VLA 모델들은 로봇 분야의 policy generalization에 큰 영향을 끼쳤으나, 여러 가지 보완해야할 부분들이 있음

- 본 논문에서는 보완해야할 점 중에 하나로 Spatial-temporal dynamics을 지적

- state-action trajectories를 인코딩해서 action prediction을 위한 spatial-temporal awareness를 향상시키는 visual trace prompting을 제안

- OpenVLA를 finetuning해서 TraceVLA를 제작, visual trace prompting학습을 위한 150K robot manipulation trajectories를 수집

- 실험 결과, SimpleEnv의 137 config에서 우수한 성능을 보임, WidowX robot을 활용한 real experiment에서도 높은 성능을 보임

## Preliminaries

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-02-tracevla-visual-trace-prompting-enhances-spatial-temporal-awareness/image_000.png" class="img-fluid rounded z-depth-1" %}

- OpenVLA

## Introduction

- Robotic manipulation policies는 보통 specific task demonstration에 학습되기 때문에 학습 데이터를 넘는 generalization 능력은 매우 부족

- VLM 모델은 높은 일반화 성능을 보임

- 하지만 VLA모델의 경우 과거의 움직임을 고려하지 않고, 과거 spatial-history 정보보다 현재 상태에 더 반응해서 결정을 내리는 경향이 있음

- 본 논문에서는 위와 같은 문제를 해소하기 위해서, 로봇의 과거 움직임 trajectory를 트래킹하는 multi-point visual input을 추가적으로 사용

- visual trace prompting을 사용하는 TraceVLA를 제안

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-02-tracevla-visual-trace-prompting-enhances-spatial-temporal-awareness/image_001.png" class="img-fluid rounded z-depth-1" %}

## TraceVLA

### Visual Trace Prompting

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-02-tracevla-visual-trace-prompting-enhances-spatial-temporal-awareness/image_002.png" class="img-fluid rounded z-depth-1" %}

- visual trace prompting을 위해서, 과거 프레임을 단순하게 concat하는 것이 아니라, key point의 trace를 생성하기 위해서 off-the-shelf point tracking algorithm을 사용

**[Visual trace를 생성하는 방법]**

- timestep t, time window budget N이 주어질 때, 우선 historical image observations h_t = (o_{t-N},...,o_t)에서 dense point trajectories 집합을 추출

- K x K개의 tracking point가 만들어진 후, 그 중에서 active point만 식별하기 위해서 pixel location에서의 change를 계산

- sampled active point trajectories를 robot의 original observation frame에 그림, 이를 visual prompt으로 최종적으로 사용

### Model Architecture Design

- 위에서 만든 visual prompt와 original observation을 모델의 input으로 사용

-  test시 visual trace를 사용하지 못하는 상황이 발생할 수 있으므로, 학습 동안에 dropout mechanism을 구현

### Implementation Details

- 학습시 visual trace generation pipeline에 대해서, grid size K=40, sample M=5, time window N=6을 사용

- computational overhead를 줄이기 위해서, dense point tracking은 N step마다 2N step에 대해서 실행

- 토탈 150K tracjectories를 annotate, TraceVLA를 finetuning 하기 위한 학습 데이터를 구축

- inference시 real-time visual trace를 위해, 매 타임스텝마다 densely querying이 아닌 M active point를 tracking를 함

- OpenVLA 7B모델을 기반으로 학습, 추가적으로 Phi3-Vision를 백본으로 사용

## Experiment

- 3 task를 137개의 configuration으로 simulation에서 실험, real robot으로 4 task에 대해 실험

### Baselines

- OpenVLA : Open-X-Embodiment로 학습한 7B VLA

- OpenVLA-Phi3 : Phi-3-Vision을 backbone으로 Open-X-Embodiment로 학습한 4.5B VLA

- Octo-Base : Open-X-Embodiement에서 800k trajectories로 학습한 transformer기반의 Policy(93M)

- RT1-X : Octo와 같은 데이터셋으로 학습한 35M parameter의 모델

- TraceVLA, TraceVLA-Phi3 : OpenVLA, OpenVLA-Phi3을 visual trace prompting으로 FT한 모델

### Simulation Evaluation

- SimplerEnv를 사용해서 평가, visual matching, visual aggregation이라는 setting을 사용

- Overall performance

- Environmental Variant Aggregation

### Real Robot Experiments

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-02-tracevla-visual-trace-prompting-enhances-spatial-temporal-awareness/image_003.png" class="img-fluid rounded z-depth-1" %}

- TraceVLA를 WidoxX-250에 fixed-mounted third-person view camera capturing 256 X 256 RGB image를 사용하는 세팅에서 평가

- BridgeData-v2와 같은 로봇 세팅이지만, setup, lighting, camera angle등의 차이를 위해 각 Task별로 30개의 trajectories를 수집, finetuning에 사용

- 실험 결과, 다양한 task에서 높은 성능을 보였고, 특히 pick-place corn task는 training data에 없었음에도 높은 성능(8/10)을 보임

- generalization capabilities를 평가하기 위해서, 4개의 unseen task에 대해서 추가 실험 진행

- generalization 실험 결과, OpenVLA보다 압도적인 성능을 냄

⇒ TraceVLA는 language grounding capability가 향상됨, spurious correlation에 강건함

### Ablation Study

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-02-tracevla-visual-trace-prompting-enhances-spatial-temporal-awareness/image_004.png" class="img-fluid rounded z-depth-1" %}

Q. Open X-embodiment dataset의 smaller subset으로 further finetuning을 해서 TraceVLA의 성능이 오른게 아닐까?

- Figure 7의 왼쪽 그림을 보면 VLA further FT의 경우 VLA와 성능이 거의 비슷, 하지만 VLA w visual trace는 성능이 크게 상승

Q. historical image observation을 appending하면 TraceVLA처럼 성능이 향상될까?

- N=6, 과거 frame을 input으로 제공(frame사이에 sep token 넣어줌), 학습

- Figure 7의 올느쪽 그림에서 VLA.ft History성능을 보면 더 낮아지는 것을 확인할 수 있음. 이 이유는 다른 timestep의 visual token사이의 redundant information 때문으로 추정

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-02-tracevla-visual-trace-prompting-enhances-spatial-temporal-awareness/image_005.png" class="img-fluid rounded z-depth-1" %}

Q. visual trace prompting이 text trace prompting보다 더 좋은 성능을 보이나요?

- visual trace를 orignal image에 얹어서 가이드 하는 방식 외에, 포인터의 움직임을 2D 좌표를 텍스트로 표현해서 input으로 넣을 수도 있음

- 실험 결과, text보단 visual prompting이 효과가 더 좋았으며, text prompting의 경우 visual prompting에 비해서 토큰수가 증가(~150 token), GPU cost가 더 많이 듦

- text에 의존하는건 VLM 모델의 multimodal grounding 역량을 풀로 사용하기 어렵다고 함

Q. TraceVLM가 visual-trace의 길이에 따라 어떻게 영향을 받나요?

- N이 커지면 visul context가 지저분하게 되고, key object나 robot end-effector를 방해할 수 있고, N이 작아지면 historical information을 덜 갖게 됨

- 실험 결과, N=6일 때의 성능이 가장 높았음

## Limitation analysis

- TraceVLA는 CoTracker가 필요하다보니, 이에 따른 추가적인 cost를 H100 GPU 1대로 분석해봄

- inference시, TraceVLA에 필요한 추가적인 computation은 대략 300장의 추가 이미지와 text 토큰 + 각 스텝마다 5-point CoTracker와 20 스텝마다 KxK(K=40) dense point tracking이 필요

- 실험 결과, OpenVLA와 0.036초 차이로 큰 차이 없는 Inference time을 보여줌

{% include figure.liquid loading="eager" path="assets/img/posts/2025-01-02-tracevla-visual-trace-prompting-enhances-spatial-temporal-awareness/image_006.png" class="img-fluid rounded z-depth-1" %}

## Related works

- LLARVA

## Conclusion

- VLA 모델이 temporal-spatial information을 잘 활용하지 못한다는 점을 해소하기 위해 visual trace prompting하는 방법론을 제안

- 7B, 4B backbone VLA 모델을 FT해서 다양한 환경에서 높은 성능을 보임
