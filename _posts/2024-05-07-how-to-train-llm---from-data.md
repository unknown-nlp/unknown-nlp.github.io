---
categories:
- paper-reviews
date: '2024-05-07 00:00:00'
description: "논문 리뷰 - LLM, \bPre-Training, torch 관련 연구"
giscus_comments: true
layout: post
related_posts: false
tags:
- "\bpre-training"
- llm
- paper-review
- torch
- transformer
thumbnail: assets/img/posts/2024-05-07-how-to-train-llm---from-data/thumbnail.jpg
title: How to Train LLM? - From Data Parallel To Fully Sharded Data Parallel
---

**논문 정보**
- **Date**: 2024-05-07
- **Reviewer**: 준원 장
- **Property**: LLM, Pre-Training, torch

### ! 본 내용에 잘못된 내용이 있을 수도 있으니, 혹시나 잘못된 부분 있다면 언제든 지적해주시면 감사하겠습니다!

## 0. Floating Point

- 컴퓨터에서 실수를 표현하는 방법으로, 수를 Exponent와 Fraction로 분리하여 표현. 

- IEEE 754 표준은 floating 포인트 수를 표현하는 데 널리 사용되는 표준. 해당 표준에서는 다양한 정밀도를 제공.

{% include figure.liquid loading="eager" path="assets/img/posts/2024-05-07-how-to-train-llm---from-data/image_000.png" class="img-fluid rounded z-depth-1" %}

- floating exampling

- FP16

→ fp32 대비 Exponent와 Fraction을 둘다 줄여 DL모델의 inference시 연구자들이 주로 사용하는 precision. (일반적으로 fp32으로 모델학습, fp16으로 inference을 하나 실험적으로 fp32대비 분명한 성능하락 확인)

- BF16

→ BF16은 fp16과 다르게 자릿수를 대표하는 exponent 동일한 8비트로 설정함으로써 더 넓은 범위의 수를 표현할 수 있음. 

→ 대신 fraction의 자릿수를 희생했기 때문에 수의 정밀도가 떨어진다는 한계가 존재

(ex)

십진수 0.1을 이진수로 표현하면 무한 반복 이진수: `**0.0001100110011001100...**` (반복)

- fp16

* fraction는 10비트를 사용하여 이 값을 가능한 한 정확하게 근사: `**0.0001100110**`

* exponent는 이진 표현에서 소수점을 왼쪽으로 몇 칸 이동시켜야 하는지에 따라 결정되며, 이 경우 -4. exponent 필드 값은 −4+15=11 (이진수 `**01011**`).

- bf16

* fraction는 7bit를 사용하여 값을 근사: `**0.0001100**`

* exponent는 FP16과 동일하게 -4이고, 지수 필드 값은 −4+127=123 (이진수 `**01111011**`).

- 결론 

⇒ Layer가 깊어질수록 logit값이 커지는 transformer계열에서는 BF16을 활용해 모델을 training하는 것이 적합해보임. input의 스케일이 크게 다른 경우, BF16은 underflow나 overflow를 방지할 수 있음.

⇒ Normalization, Optimizer state 연산 (e.g., momentum) 등 term을 계속해서 나눠주는 연산의 경우 정밀도를 희생한 BF16은 오차를 유발할 수 있기 때문에 mixed precision 같은 방법론들을 도입해서 한계를 방지해야함.

## 1. Mixed Precision

- Mixed Precision은 DL 학습 시 다양한 Precision을 혼합하여 사용하는 기술. 

- 대표적으로 NVIDIA의 Tensor Cores에서는 fp16과 fp32를 혼합하여 더 빠른 수행 시간과 높은 수치 정밀도를 제공

- fp16으로는 표현할 수 있는 숫자체계가 제한적이기 때문에 gradient update시에 underflow 문제 발생 가능

→ 빨간선 왼쪽이 fp16으로 표현할 수 없는 범위

{% include figure.liquid loading="eager" path="assets/img/posts/2024-05-07-how-to-train-llm---from-data/image_001.png" class="img-fluid rounded z-depth-1" %}

→fp16으로 tensor 연산 시의 문제점

- 위를 해결하기 위해 Precision을 혼합해서 활용하는 Mixed Precision 기법이 나옴

- 가정: 우리의 Model은 fp32이다. 해당 모델이 가지고 있는  weights을 Master weights라고 명명.

1. fp32로 표현된 Master weights을 복사하여 fp16 weights로 가져옴

1. fp16 weights로 forward & loss 계산

1. loss값이 scaling factor를 곱한다. 

1. fp16으로 표현된 loss에서 backward (loss.backward()) → backpropagate 한다.

1. upscaling한 gradient(XS)를 optimizer.step()을 위해서 다시 unscale (X1/S)해준다.

1. optimizer.step()은 fp32에서 이루어지며 master weight을 업데이트 함.

{% include figure.liquid loading="eager" path="assets/img/posts/2024-05-07-how-to-train-llm---from-data/image_002.png" class="img-fluid rounded z-depth-1" %}

- Torch AMP(**Automatic Mixed Precision**)에 위의 설명 및 코드가 그대로 반영되어 있음

```python
# Creates model and optimizer in default precision
model = Net().cuda()
optimizer = optim.SGD(model.parameters(), ...)

# Creates a GradScaler once at the beginning of training.
scaler = GradScaler()

for epoch in epochs:
    for input, target in data:
        optimizer.zero_grad()

        # Runs the forward pass with autocasting.
        with autocast(device_type='cuda', dtype=torch.float16):
            output = model(input)
            loss = loss_fn(output, target)

        # Scales loss. Calls backward() on scaled loss to create scaled gradients.
        # Backward passes under autocast are not recommended.
        # Backward ops run in the same dtype autocast chose for corresponding forward ops.
        scaler.scale(loss).backward()

        # scaler.step() first unscales the gradients of the optimizer's assigned params.
        # If these gradients do not contain infs or NaNs, optimizer.step() is then called,
        # otherwise, optimizer.step() is skipped.
        scaler.step(optimizer)

        # Updates the scale for next iteration.
        scaler.update()
```

## 2. List of NCCL Operation

- 2개의 프로세스간의 통신 패턴을 point-to-point communication(점대점 통신)라고 명명한다면, 여러 개의 프로세스간의 통신을 collective communication(집합 통신)이라고 명명한다.

→  point-to-point communication는 sender는 데이터를 보내고, receiver는 데이터를 받도록 설계하면 되기 때문에 구현 난이도가 상대적으로 쉬움

{% include figure.liquid loading="eager" path="assets/img/posts/2024-05-07-how-to-train-llm---from-data/image_003.png" class="img-fluid rounded z-depth-1" %}

→ multiple senders와 multiple receivers가 있는  collective communication의 경우, topology들이 구성이 매우 다양하기 때문에 (위 그림처럼) 데이터 통신을 최적화하기 매우 어렵다는 한계점이 존재한다.

- 조금 더 자세히 말하면, 몇 개의 GPU가 있고, 어떤 GPU가 어떤 GPU와 어떻게 연결(PCIe, NVLink, IB, ethernet 등등) 되어 있는 지와 같은 topology 정보는 통신 최적화에 필수로 고려해야 하는 요소인데, 그 조합이 너무나도 많기에 이것을 다 만족하는 최적화된 솔루션을 찾아 구현하기가 매우 어렵다.

- 이러한 문제점을 해결하기 위해 'Pitch Patarasuk and Xin Yuan. Bandwidth optimal all-reduce algorithms for clusters of workstations. J. Parallel Distrib. Comput., 69:117–124, 2009.’에서 모든 어떤 topology라도 **Ring(s) topology**로 생각하고 구현할 경우 최적 성능을 달성할 수 있음을 보여줌.

→ 위는 Broadcast 연산인데 GPU0이 GPU[1:3]에 data를 뿌릴때 순차적으로 (GPU0→ GPU1 이 끝나면 GPU0 → GPU2 …)으로 하는게 아니라 데이터를 작은 조각으로 나누어서 GPU0 → GPU1 & GPU1 → GPU2 & GPU2 → GPU3 이렇게 인접한 모든 프로세스가 데이터를 전송하도록 구현하였음.

- **NCCL(NVIDIA Collective Communications Library)**은 ***멀티 GPU*** 및 ***멀티 노드 환경***에서 고성능을 제공하는 통신 라이브러리로 다양한 네트워크 topology에서도 최적 성능을 달성하는 것을 목표로 개발되었으며 이전에 언급한 Ring-based 집합통신 알고리즘을 기반으로 최적화된 집합 통신을 구현

- NCCL은 DL training, inference에서의 다양한 집합 연산(예: All-reduce, All-gather, Broadcast 등)을 최적화하여 각 GPU 사이에 일관되고 효율적인 통신을 제공하여 병렬 처리 성능을 극대화하는것에 목표를 두고 있음. 

- 동기 및 비동기 통신을 지원하며, CUDA 스트림을 통해 다른 연산과 겹쳐서 수행이 가능하다고 함.

{% include figure.liquid loading="eager" path="assets/img/posts/2024-05-07-how-to-train-llm---from-data/image_004.png" class="img-fluid rounded z-depth-1" %}

→ (1) GPU를 이용한 연산 GPGPU(CUDA)으로 가속화 (2) NCCL을 활용해 하나의 GPU가 아닌 multiple GPUs, 나아가 multi-node 상의 multiple GPUs의 통신을 통한 연산 가속화

* General-Purpse computing on Graphic Processing Unit: 일반적으로 컴퓨터 그래픽스를 위한 계산만 맡았던 그래픽 처리 장치를, 전통적으로 중앙 처리 장치가 맡았던 응용 프로그램들의 계산에 사용하는 기술

- 간단한 용어 정리

- **NCCL Operations (DP나 DDP 쓰면서 다들 호출해보셨을 operations들)**

1. **AllReduce**

1. **Broadcast**

1. **Reduce**

1. **AllGather**

1. **ReduceScatter**

- **inXY**: 노드 X에서 노드 Y로 보내진 데이터.

- **out[Y]**: 노드 Y에서 모든 입력 데이터를 합산한 결과를 저장하는 배열.

- **count**: 각 노드에서 전송된 데이터 요소 수.

- **i**: 각 노드의 데이터 배열에서의 인덱스.

- **노드 0**에서는 `**[in00, in01, in02, in03]**`의 데이터 존재

- **노드 1**에서는 `**[in10, in11, in12, in13]**`의 데이터 존재

- **노드 2**에서는 `**[in20, in21, in22, in23]**`의 데이터 존재

- **노드 3**에서는 `**[in30, in31, in32, in33]**`의 데이터 존재

노드 0의 출력 `**out0**`을 구하는 방법:

- 노드 0으로 보내진 모든 데이터 요소를 합산.

- `**out0 = sum(in00*4+0, in10*4+0, in20*4+0, in30*4+0)**`

## 3. DP (DataParallel) & DDP (DistributedDataParallel)

- 두 방법론 모두 효율적으로 모델을 학습하기 위해 등장한 방법론.

- `DataParallel`은 단일 작업, 멀티쓰레드 방법론으로  GPU에 입력 데이터를 부분적으로 할당(mini-batch를 분할)하고 동일한 신경망 모델을 복제하여 이용하는 방식

- 반면, `DistributedDataParallel`은 다중 작업이며 단일 및 다중 기기 학습을 전부 지원하는 방식

- `DataParallel`가 가진 스레드간 GIL 경합, 복제 모델의 반복 당 생성, 입력 및 수집 출력으로 인한 추가적인 오버헤드를 `DistributedDataParallel`가 보완해 현재는 DDP를 주로 활용,

- ***DP와 DDP 모두 (당연히 ) Multi-GPUs training setting을 가정함***

- **DP (DataParallel)**

{% include figure.liquid loading="eager" path="assets/img/posts/2024-05-07-how-to-train-llm---from-data/image_005.png" class="img-fluid rounded z-depth-1" %}

1. **Scatter**

1. **Replicate**

1. **Forward** 
