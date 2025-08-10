---
categories:
- paper-reviews
date: '2025-06-10 00:00:00'
description: 논문 리뷰
giscus_comments: true
layout: post
related_posts: false
tags:
- embedding
- fine-tuning
- language-model
- llm
- paper-review
- reasoning
thumbnail: assets/img/posts/2025-06-10-dra-grpo-exploring-diversity-aware-reward-adjustment-for/thumbnail.jpg
title: 'DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training
  of Large Language Models'
---

**논문 정보**
- **Date**: 2025-06-10
- **Reviewer**: 건우 김

# Abstract

- 최근에 post-training을 위한 RL에서 **GRPO**와 같이 low-resource settings에서 가능성을 보여줌

- 위 문제를 해결하기 위해 reward computation 과정에서 semantic diversity를 직접적으로 반영하는 방법인 **Diversity-aware Reward Adjustment (DRA)**를 제안함

- DRA는 Submodular Mutual Information (SMI)를 활용하여 

- 5개 Mathematical Reasoning benchmark에서 recent methods 대비 outperform 성능 보여줌 

# 1. Introduction

DeepSeek-R1-Zero (Guo et al., 2025)에서 기존 LLM에 SFT를 적용하는 것에서 벗어나, base LM에 바로 RL을 적용할 수 있는 R1-Zero training pipeline을 제안함. 

→ Group Relative Policy Optimization (GRPO) 알고리즘 덕분에 가능한 방법

GRPO는 PPO와 다르게 critic model 없이 주어진 prompt에 대해 여러 sampling된 completions의 relative performance에 대한 advantage를 평가함. 

하지만 최근에 공개된 GRPO 및 그 variants (e.g,. DR. GRPO)들은 일반적으로 정답 여부와 같은 **solution-level의 scalar reward signals에만 의존하는 경향이 있어, 같은 정답이라도 diverse reasoning path의 차이를 반영하지 못함**.

→ 이는 semantic하게 다른 completions들이 올바르거나 틀린 경우 모두 거의 동일한 rewards를 받아, 의미 있는 reasoning 차이를 반영하지 못하는 **indistinguishable advantage estimates**를 생성하는 문제가 있음

→ 또한, 이는 resource-constrained settings에서 더 문제가 될 수 있음

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/0755bf31-0127-45da-9ad2-0f79771eec17/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EKEI4VI%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDftyrgNdefCJJ6vZqGZaylfaz9KGjufy593Ne78q68OAiBW7OrRar%2FBD5yPl5xyF49HSyiajeH324FVjvlOsP7FOSqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuRp0cBGWLF08JRjSKtwDey8AK73F4P0vphVMXbm20onRE4z5mmMbDDMpZpKUvtRvBuohT7imk%2FJLsGplHnC%2FsvLCmVnW5Q0NjYD7BJavPuw0%2FROulOFTSeQZoeE5BTyIuMotxup7JxnTOZDDll0Sc9ejDDBt%2FzJ1%2FejzNTdfA%2Bz5X3Dp0jmJNuxC5TuHdeUPSJZ65qmUnVknf8sT8RMGwXALquIWLNGFtLK8tiLuWk8nSPm58CRCcx2QJ1kZTAtlNn5iXl1i9JukUctjS8S09nsr6ZMPF9K3vpz4iqexpE6n48asrGlrddaWzOlIf41%2Bn3UEtLa5kk2ycgt%2F%2Buok0Y7WxcWiM9Uewk87Uy2m4FRhF7T%2BfudDtyCE1omsMK4N6UIMTmcOCg1%2B5idcftQPnOqu3t2mNU2XFLCF1hu%2BM3%2Fn%2F0%2BEj%2BGpIrP4J0c5cMUzE0Gt8iHJL17Sgt6t1VSSHc6pU7ctREox1Dp0vluY6pz%2BmCPQ4GzMN189KCeW0QKsed3k2ZlylydYRU2o7qOaeLoDlPbkFzFILbKsuOsq6c2NIoA87pRpEaNF9W6jIP8pRDUhO20bBTzGdmQWUyOJwWsNDJBCoMWDPuAAcVwI5dBQPcH7q1382Bq0xkU1Zesih4qf1gvmyHE5qeYw8v7hxAY6pgFlza4s3u7UhGeQB0wBPQgncki3SLRh5QH%2FdTvXw7oqyFkWFMUQH2DUWHz%2FNnOK1l2WBO9D%2Fw9XyUwfD5z6pmLhhmb7i2E7SPSad%2B%2BhVWHBxLRoRFEMBnEPHsFIjS64fSlmLXRTo0eDlRVVCDo1sOy3v5CznrzatG%2BbOz0uxS8T7cQMx5quHewenFDkP9uFs%2FuyUVi%2B2ppYUhfGEPet9taJ27HnJai8&X-Amz-Signature=59584c5ce9d287e25c0c551332ef24a26864a01062bfb849aa989ea389586d4d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

이 문제를 해결하기 위해서 저자들은 **Diversity-aware Reward Adjustment (DRA)**를 제안함. 

이는 학습 과정에서 sampling된 completions 간의 *semantic diversity를 직접적으로 모델링하는 방식으로* 그룹 내 다른 *completions과의 semantic similarity를 기반으로 각 output의 reward를 reweight*함.

- **diverse completions에는 더 높은 weight, 중복된 completion에는 더 낮은 weight 부여**

# 2. Method

### Preliminary

LM의 generation은 token-level Markov Decision Process로 볼 수 있음. 각 generation step t에서 state s_t는 input question q와 지금까지 생성된 partial output sequence o_{<t}의 concatenation이기에, sates는 다음과 같음 s_t=[q;o_{<t}]. 

policy \pi_{\theta}(.|s_t)는 vocab set A에서 next token o_t를 선택하고, 이는 deterministic transition을 유도하여 next state s_{t+1}=[s_t;o_t]로 이동함. 

GRPO는 각 question q에 대해 여러 개의 responses C={o_1,...o_G}를 sampling하고, 각 response에 대해 reward를 계산함 R={R(q,o_1), ... , R(q,o_G)}

계산된 reward R을 이용해 advantage A_{i,t}를 아래와 같이 계산함 (normalize)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/2f7f6035-457f-4200-a360-b7a8a5d96b3a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EKEI4VI%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDftyrgNdefCJJ6vZqGZaylfaz9KGjufy593Ne78q68OAiBW7OrRar%2FBD5yPl5xyF49HSyiajeH324FVjvlOsP7FOSqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuRp0cBGWLF08JRjSKtwDey8AK73F4P0vphVMXbm20onRE4z5mmMbDDMpZpKUvtRvBuohT7imk%2FJLsGplHnC%2FsvLCmVnW5Q0NjYD7BJavPuw0%2FROulOFTSeQZoeE5BTyIuMotxup7JxnTOZDDll0Sc9ejDDBt%2FzJ1%2FejzNTdfA%2Bz5X3Dp0jmJNuxC5TuHdeUPSJZ65qmUnVknf8sT8RMGwXALquIWLNGFtLK8tiLuWk8nSPm58CRCcx2QJ1kZTAtlNn5iXl1i9JukUctjS8S09nsr6ZMPF9K3vpz4iqexpE6n48asrGlrddaWzOlIf41%2Bn3UEtLa5kk2ycgt%2F%2Buok0Y7WxcWiM9Uewk87Uy2m4FRhF7T%2BfudDtyCE1omsMK4N6UIMTmcOCg1%2B5idcftQPnOqu3t2mNU2XFLCF1hu%2BM3%2Fn%2F0%2BEj%2BGpIrP4J0c5cMUzE0Gt8iHJL17Sgt6t1VSSHc6pU7ctREox1Dp0vluY6pz%2BmCPQ4GzMN189KCeW0QKsed3k2ZlylydYRU2o7qOaeLoDlPbkFzFILbKsuOsq6c2NIoA87pRpEaNF9W6jIP8pRDUhO20bBTzGdmQWUyOJwWsNDJBCoMWDPuAAcVwI5dBQPcH7q1382Bq0xkU1Zesih4qf1gvmyHE5qeYw8v7hxAY6pgFlza4s3u7UhGeQB0wBPQgncki3SLRh5QH%2FdTvXw7oqyFkWFMUQH2DUWHz%2FNnOK1l2WBO9D%2Fw9XyUwfD5z6pmLhhmb7i2E7SPSad%2B%2BhVWHBxLRoRFEMBnEPHsFIjS64fSlmLXRTo0eDlRVVCDo1sOy3v5CznrzatG%2BbOz0uxS8T7cQMx5quHewenFDkP9uFs%2FuyUVi%2B2ppYUhfGEPet9taJ27HnJai8&X-Amz-Signature=5103a093ead249bf08e6e532d8b48883ea2e52ed9aa3d3f8fc9c9c08e4853a08&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

GRPO의 objective function J_{GRPO}(\pi_{\theta})를 optimize함

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/915af8f9-3aa6-4e8a-8d32-71073d2d1734/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EKEI4VI%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDftyrgNdefCJJ6vZqGZaylfaz9KGjufy593Ne78q68OAiBW7OrRar%2FBD5yPl5xyF49HSyiajeH324FVjvlOsP7FOSqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuRp0cBGWLF08JRjSKtwDey8AK73F4P0vphVMXbm20onRE4z5mmMbDDMpZpKUvtRvBuohT7imk%2FJLsGplHnC%2FsvLCmVnW5Q0NjYD7BJavPuw0%2FROulOFTSeQZoeE5BTyIuMotxup7JxnTOZDDll0Sc9ejDDBt%2FzJ1%2FejzNTdfA%2Bz5X3Dp0jmJNuxC5TuHdeUPSJZ65qmUnVknf8sT8RMGwXALquIWLNGFtLK8tiLuWk8nSPm58CRCcx2QJ1kZTAtlNn5iXl1i9JukUctjS8S09nsr6ZMPF9K3vpz4iqexpE6n48asrGlrddaWzOlIf41%2Bn3UEtLa5kk2ycgt%2F%2Buok0Y7WxcWiM9Uewk87Uy2m4FRhF7T%2BfudDtyCE1omsMK4N6UIMTmcOCg1%2B5idcftQPnOqu3t2mNU2XFLCF1hu%2BM3%2Fn%2F0%2BEj%2BGpIrP4J0c5cMUzE0Gt8iHJL17Sgt6t1VSSHc6pU7ctREox1Dp0vluY6pz%2BmCPQ4GzMN189KCeW0QKsed3k2ZlylydYRU2o7qOaeLoDlPbkFzFILbKsuOsq6c2NIoA87pRpEaNF9W6jIP8pRDUhO20bBTzGdmQWUyOJwWsNDJBCoMWDPuAAcVwI5dBQPcH7q1382Bq0xkU1Zesih4qf1gvmyHE5qeYw8v7hxAY6pgFlza4s3u7UhGeQB0wBPQgncki3SLRh5QH%2FdTvXw7oqyFkWFMUQH2DUWHz%2FNnOK1l2WBO9D%2Fw9XyUwfD5z6pmLhhmb7i2E7SPSad%2B%2BhVWHBxLRoRFEMBnEPHsFIjS64fSlmLXRTo0eDlRVVCDo1sOy3v5CznrzatG%2BbOz0uxS8T7cQMx5quHewenFDkP9uFs%2FuyUVi%2B2ppYUhfGEPet9taJ27HnJai8&X-Amz-Signature=38ad041cef22b187e36998eced15b0e72f0b6a9ceb6b476a7d4567e53315a3d5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

이후 연구인 DR.GRPO (Liu et al., 2025)에서는 token efficiency를 개선하기 위해 **GRPO의 objective function에서 ‘response length’ term과 Advantage에서 std로 normalize해주는 term을 지움**

### Diversity-Quality Inconsistency

GRPO와 DR.GRPO의 reward signal은 **solution-level correctness**만 사용하기 때문에, 각 completion에 대해 **sparse scalar judgement**를 계산함.

→ 이러한 scalar reward는 동일하거나 유사한 결과를 산출하는 diverse reasoning-path를 고려하지 않기 때문에, Diversity-Quality Inconsistency가 발생함. 

위에 Example 말고, 보다 실증적인 방식으로 다음 statement (”***reward alone fails to reflect the underlying variability in reasoning strategies***”) 를 검증하기 위해 embedding distances로 측정된 completions의 structural dissimilarity를 계산함. 

- Spearman’s rank correlation을 사용하여 sampled completions 사이에서 reward difference와 semantic distance를 측정함 →semantic distance가 커질수록 reward 차이도 커지는가?

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/fecf6066-715d-4add-8abc-0820b525b2f4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EKEI4VI%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDftyrgNdefCJJ6vZqGZaylfaz9KGjufy593Ne78q68OAiBW7OrRar%2FBD5yPl5xyF49HSyiajeH324FVjvlOsP7FOSqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuRp0cBGWLF08JRjSKtwDey8AK73F4P0vphVMXbm20onRE4z5mmMbDDMpZpKUvtRvBuohT7imk%2FJLsGplHnC%2FsvLCmVnW5Q0NjYD7BJavPuw0%2FROulOFTSeQZoeE5BTyIuMotxup7JxnTOZDDll0Sc9ejDDBt%2FzJ1%2FejzNTdfA%2Bz5X3Dp0jmJNuxC5TuHdeUPSJZ65qmUnVknf8sT8RMGwXALquIWLNGFtLK8tiLuWk8nSPm58CRCcx2QJ1kZTAtlNn5iXl1i9JukUctjS8S09nsr6ZMPF9K3vpz4iqexpE6n48asrGlrddaWzOlIf41%2Bn3UEtLa5kk2ycgt%2F%2Buok0Y7WxcWiM9Uewk87Uy2m4FRhF7T%2BfudDtyCE1omsMK4N6UIMTmcOCg1%2B5idcftQPnOqu3t2mNU2XFLCF1hu%2BM3%2Fn%2F0%2BEj%2BGpIrP4J0c5cMUzE0Gt8iHJL17Sgt6t1VSSHc6pU7ctREox1Dp0vluY6pz%2BmCPQ4GzMN189KCeW0QKsed3k2ZlylydYRU2o7qOaeLoDlPbkFzFILbKsuOsq6c2NIoA87pRpEaNF9W6jIP8pRDUhO20bBTzGdmQWUyOJwWsNDJBCoMWDPuAAcVwI5dBQPcH7q1382Bq0xkU1Zesih4qf1gvmyHE5qeYw8v7hxAY6pgFlza4s3u7UhGeQB0wBPQgncki3SLRh5QH%2FdTvXw7oqyFkWFMUQH2DUWHz%2FNnOK1l2WBO9D%2Fw9XyUwfD5z6pmLhhmb7i2E7SPSad%2B%2BhVWHBxLRoRFEMBnEPHsFIjS64fSlmLXRTo0eDlRVVCDo1sOy3v5CznrzatG%2BbOz0uxS8T7cQMx5quHewenFDkP9uFs%2FuyUVi%2B2ppYUhfGEPet9taJ27HnJai8&X-Amz-Signature=cf520a302e6550772f4d50d301ca6efd2a7b8b6699970229a15fca8e4499aca7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Figure2는 Spearman’s rank correlation의 p-values의 분포를 보여주는데, 대부분의 p-value가 significance level인 0.05 보다 큰 값을 보여주며, 실제로 80% 이상의 prompt에 대해 statistically significant correlation이 없음을 확인할 수 있음

### Diversity-aware Reward Adjustment

Diversity-Quality Inconsistency 문제를 해결하기 위해, 각 sample의 relative diversity/redundancy에 따라 reward를 reweight하는 방법을 제안함. 

**→ diverse completions은 더 높은 weight, 중복된 response는 낮은 weight**

먼저 기존의 reward R(q,o_i)를 diversity-aware adjusted reward \tilde{R}(q,o_i) (틸다 표시 어떻게 하나요…) 으로 대체함

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/ed8381b4-4bb0-419d-bcf0-fa46a209ae13/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EKEI4VI%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDftyrgNdefCJJ6vZqGZaylfaz9KGjufy593Ne78q68OAiBW7OrRar%2FBD5yPl5xyF49HSyiajeH324FVjvlOsP7FOSqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuRp0cBGWLF08JRjSKtwDey8AK73F4P0vphVMXbm20onRE4z5mmMbDDMpZpKUvtRvBuohT7imk%2FJLsGplHnC%2FsvLCmVnW5Q0NjYD7BJavPuw0%2FROulOFTSeQZoeE5BTyIuMotxup7JxnTOZDDll0Sc9ejDDBt%2FzJ1%2FejzNTdfA%2Bz5X3Dp0jmJNuxC5TuHdeUPSJZ65qmUnVknf8sT8RMGwXALquIWLNGFtLK8tiLuWk8nSPm58CRCcx2QJ1kZTAtlNn5iXl1i9JukUctjS8S09nsr6ZMPF9K3vpz4iqexpE6n48asrGlrddaWzOlIf41%2Bn3UEtLa5kk2ycgt%2F%2Buok0Y7WxcWiM9Uewk87Uy2m4FRhF7T%2BfudDtyCE1omsMK4N6UIMTmcOCg1%2B5idcftQPnOqu3t2mNU2XFLCF1hu%2BM3%2Fn%2F0%2BEj%2BGpIrP4J0c5cMUzE0Gt8iHJL17Sgt6t1VSSHc6pU7ctREox1Dp0vluY6pz%2BmCPQ4GzMN189KCeW0QKsed3k2ZlylydYRU2o7qOaeLoDlPbkFzFILbKsuOsq6c2NIoA87pRpEaNF9W6jIP8pRDUhO20bBTzGdmQWUyOJwWsNDJBCoMWDPuAAcVwI5dBQPcH7q1382Bq0xkU1Zesih4qf1gvmyHE5qeYw8v7hxAY6pgFlza4s3u7UhGeQB0wBPQgncki3SLRh5QH%2FdTvXw7oqyFkWFMUQH2DUWHz%2FNnOK1l2WBO9D%2Fw9XyUwfD5z6pmLhhmb7i2E7SPSad%2B%2BhVWHBxLRoRFEMBnEPHsFIjS64fSlmLXRTo0eDlRVVCDo1sOy3v5CznrzatG%2BbOz0uxS8T7cQMx5quHewenFDkP9uFs%2FuyUVi%2B2ppYUhfGEPet9taJ27HnJai8&X-Amz-Signature=afcab3102eee5125dee117623d02b4614773441c15419568718735fcb948a691&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- SMI({o_i},C \ {o_i})는 completion o_i와 나머지 group C \ o_i 간의 Submodular Mutual Information을 나타냄

- Submodular functions은 diminishing returns 특성을 갖으며, diversity와 redundancy를 모델링할 수 있음 

- SMI는 두 집합 간의 shared information을 정량화하며 (Iyer et al., 2021a,b)에서는 아래와 같이 정의함

- SMI를 쉽게 말하면 “**특정 completion 하나가 group 내 다른 completion과 얼마나 겹치는가**”를 수치로 나타내는 값

- Submodular 함수는 수학 개념으로 “새로운 element가 기존에 비슷한게 많을수록 기여도가 줄어드는 성질”을 갖고 있음

→ 이렇게 새로운 reward를 구하는 연산은 Pytorch에서 효과적으로 처리될 수 있음 

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/5a2e6e28-2f19-4897-bac5-8c8ac65269f9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EKEI4VI%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDftyrgNdefCJJ6vZqGZaylfaz9KGjufy593Ne78q68OAiBW7OrRar%2FBD5yPl5xyF49HSyiajeH324FVjvlOsP7FOSqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuRp0cBGWLF08JRjSKtwDey8AK73F4P0vphVMXbm20onRE4z5mmMbDDMpZpKUvtRvBuohT7imk%2FJLsGplHnC%2FsvLCmVnW5Q0NjYD7BJavPuw0%2FROulOFTSeQZoeE5BTyIuMotxup7JxnTOZDDll0Sc9ejDDBt%2FzJ1%2FejzNTdfA%2Bz5X3Dp0jmJNuxC5TuHdeUPSJZ65qmUnVknf8sT8RMGwXALquIWLNGFtLK8tiLuWk8nSPm58CRCcx2QJ1kZTAtlNn5iXl1i9JukUctjS8S09nsr6ZMPF9K3vpz4iqexpE6n48asrGlrddaWzOlIf41%2Bn3UEtLa5kk2ycgt%2F%2Buok0Y7WxcWiM9Uewk87Uy2m4FRhF7T%2BfudDtyCE1omsMK4N6UIMTmcOCg1%2B5idcftQPnOqu3t2mNU2XFLCF1hu%2BM3%2Fn%2F0%2BEj%2BGpIrP4J0c5cMUzE0Gt8iHJL17Sgt6t1VSSHc6pU7ctREox1Dp0vluY6pz%2BmCPQ4GzMN189KCeW0QKsed3k2ZlylydYRU2o7qOaeLoDlPbkFzFILbKsuOsq6c2NIoA87pRpEaNF9W6jIP8pRDUhO20bBTzGdmQWUyOJwWsNDJBCoMWDPuAAcVwI5dBQPcH7q1382Bq0xkU1Zesih4qf1gvmyHE5qeYw8v7hxAY6pgFlza4s3u7UhGeQB0wBPQgncki3SLRh5QH%2FdTvXw7oqyFkWFMUQH2DUWHz%2FNnOK1l2WBO9D%2Fw9XyUwfD5z6pmLhhmb7i2E7SPSad%2B%2BhVWHBxLRoRFEMBnEPHsFIjS64fSlmLXRTo0eDlRVVCDo1sOy3v5CznrzatG%2BbOz0uxS8T7cQMx5quHewenFDkP9uFs%2FuyUVi%2B2ppYUhfGEPet9taJ27HnJai8&X-Amz-Signature=53511c59943d8af2b9c0c4b9c19e3358857b2678a0491805f747a092c825b004&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 3. Experiment

### 3.1 Experimental Setup

**Training Dataset: **

**Evaluation Dataset: **

**Baselines**: 

- general purpose large model: Llama-3.1-70B-Instruct, o1-preivew

- Mathematics-focused 7B models: Qwen-2.5-Math-7B-Instruct, rStar-Math-7B, Eurus-2-7B-PRIME, Qwen2.5-7B-SimpleRL

- Mathematics-focused 1.5B models: DeepScaleR-1.5B-Preview, Still-3-1.5B-Preview, Open-RS

**Implementations:**

- 본 연구는 DRA의 proof-of-concept만 검증하는 것이 목적이기에 DeepSeek-R1-Distill-Qwen-1.5B를 base model로 두어 학습시킴

- 4 x A100 (40GB) GPUs

### 3.2 Empirical Analysis

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/1499b3de-6df4-4aa8-b0b3-010814af9105/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EKEI4VI%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDftyrgNdefCJJ6vZqGZaylfaz9KGjufy593Ne78q68OAiBW7OrRar%2FBD5yPl5xyF49HSyiajeH324FVjvlOsP7FOSqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuRp0cBGWLF08JRjSKtwDey8AK73F4P0vphVMXbm20onRE4z5mmMbDDMpZpKUvtRvBuohT7imk%2FJLsGplHnC%2FsvLCmVnW5Q0NjYD7BJavPuw0%2FROulOFTSeQZoeE5BTyIuMotxup7JxnTOZDDll0Sc9ejDDBt%2FzJ1%2FejzNTdfA%2Bz5X3Dp0jmJNuxC5TuHdeUPSJZ65qmUnVknf8sT8RMGwXALquIWLNGFtLK8tiLuWk8nSPm58CRCcx2QJ1kZTAtlNn5iXl1i9JukUctjS8S09nsr6ZMPF9K3vpz4iqexpE6n48asrGlrddaWzOlIf41%2Bn3UEtLa5kk2ycgt%2F%2Buok0Y7WxcWiM9Uewk87Uy2m4FRhF7T%2BfudDtyCE1omsMK4N6UIMTmcOCg1%2B5idcftQPnOqu3t2mNU2XFLCF1hu%2BM3%2Fn%2F0%2BEj%2BGpIrP4J0c5cMUzE0Gt8iHJL17Sgt6t1VSSHc6pU7ctREox1Dp0vluY6pz%2BmCPQ4GzMN189KCeW0QKsed3k2ZlylydYRU2o7qOaeLoDlPbkFzFILbKsuOsq6c2NIoA87pRpEaNF9W6jIP8pRDUhO20bBTzGdmQWUyOJwWsNDJBCoMWDPuAAcVwI5dBQPcH7q1382Bq0xkU1Zesih4qf1gvmyHE5qeYw8v7hxAY6pgFlza4s3u7UhGeQB0wBPQgncki3SLRh5QH%2FdTvXw7oqyFkWFMUQH2DUWHz%2FNnOK1l2WBO9D%2Fw9XyUwfD5z6pmLhhmb7i2E7SPSad%2B%2BhVWHBxLRoRFEMBnEPHsFIjS64fSlmLXRTo0eDlRVVCDo1sOy3v5CznrzatG%2BbOz0uxS8T7cQMx5quHewenFDkP9uFs%2FuyUVi%2B2ppYUhfGEPet9taJ27HnJai8&X-Amz-Signature=70928c4fda78911f35d6d08ec5b2289491fa2b4d7bd465f800ed58734f692b5c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**Main Results**

- DRA-DR.GRPO는 avg acc가 58.2%로 가장 높게 나옴 (DRA-GRPO역시 비슷한 수준으로 높게 나옴)

- DRA-GRPO와 DRA-DR.GRPO는 fine-tuning samples을 7,000개 밖에 사용하지 않았음에도 불구하고 40,000개 사용한 DeepScaleR-1.5B-preview보다 높은 성능 보여줌

**Ablation Study**

- Base model인 DeepSeek-R1-Distill-Qwen-1.5B와 비교하여 DRA-GRPO, DRA-DR.GRPO는 각각 7.8%, 9.3% 성능 향상되고 단순 RL (GRPO, DR.GRPO) 대비 1.9%, 2.2% 향상

**Efficiency**

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/ee043cfa-03ea-435c-af5c-74342761e99c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EKEI4VI%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDftyrgNdefCJJ6vZqGZaylfaz9KGjufy593Ne78q68OAiBW7OrRar%2FBD5yPl5xyF49HSyiajeH324FVjvlOsP7FOSqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuRp0cBGWLF08JRjSKtwDey8AK73F4P0vphVMXbm20onRE4z5mmMbDDMpZpKUvtRvBuohT7imk%2FJLsGplHnC%2FsvLCmVnW5Q0NjYD7BJavPuw0%2FROulOFTSeQZoeE5BTyIuMotxup7JxnTOZDDll0Sc9ejDDBt%2FzJ1%2FejzNTdfA%2Bz5X3Dp0jmJNuxC5TuHdeUPSJZ65qmUnVknf8sT8RMGwXALquIWLNGFtLK8tiLuWk8nSPm58CRCcx2QJ1kZTAtlNn5iXl1i9JukUctjS8S09nsr6ZMPF9K3vpz4iqexpE6n48asrGlrddaWzOlIf41%2Bn3UEtLa5kk2ycgt%2F%2Buok0Y7WxcWiM9Uewk87Uy2m4FRhF7T%2BfudDtyCE1omsMK4N6UIMTmcOCg1%2B5idcftQPnOqu3t2mNU2XFLCF1hu%2BM3%2Fn%2F0%2BEj%2BGpIrP4J0c5cMUzE0Gt8iHJL17Sgt6t1VSSHc6pU7ctREox1Dp0vluY6pz%2BmCPQ4GzMN189KCeW0QKsed3k2ZlylydYRU2o7qOaeLoDlPbkFzFILbKsuOsq6c2NIoA87pRpEaNF9W6jIP8pRDUhO20bBTzGdmQWUyOJwWsNDJBCoMWDPuAAcVwI5dBQPcH7q1382Bq0xkU1Zesih4qf1gvmyHE5qeYw8v7hxAY6pgFlza4s3u7UhGeQB0wBPQgncki3SLRh5QH%2FdTvXw7oqyFkWFMUQH2DUWHz%2FNnOK1l2WBO9D%2Fw9XyUwfD5z6pmLhhmb7i2E7SPSad%2B%2BhVWHBxLRoRFEMBnEPHsFIjS64fSlmLXRTo0eDlRVVCDo1sOy3v5CznrzatG%2BbOz0uxS8T7cQMx5quHewenFDkP9uFs%2FuyUVi%2B2ppYUhfGEPet9taJ27HnJai8&X-Amz-Signature=ee034f028af958699dd0b20f8ffaa866a3b8e5b2f3729b3aed1dd1bb6745b2c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

DRA는 completions을 encoding 해야하기에 over-head가 존재하지만, 별로 크지 않음. 

→ 저자들이 실험에 사용한 GPU스펙인 (A100-40GB)에서는 어차피 DRA 없이도 mini-batch를 늘리는 것이 불가능해서 DRA 적용하는 것이 별 문제가 되지 않다고 하는데…. → 🐶 🔊 라고 생각합니다

**Training Cost**

500 steps 학습시켜 12.5hr 소요됨 ⇒ $55 비용

→ 다른 방법대비 효율적임

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/e50c32fa-45ea-47fe-9624-c09f85c4d8f0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EKEI4VI%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDftyrgNdefCJJ6vZqGZaylfaz9KGjufy593Ne78q68OAiBW7OrRar%2FBD5yPl5xyF49HSyiajeH324FVjvlOsP7FOSqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuRp0cBGWLF08JRjSKtwDey8AK73F4P0vphVMXbm20onRE4z5mmMbDDMpZpKUvtRvBuohT7imk%2FJLsGplHnC%2FsvLCmVnW5Q0NjYD7BJavPuw0%2FROulOFTSeQZoeE5BTyIuMotxup7JxnTOZDDll0Sc9ejDDBt%2FzJ1%2FejzNTdfA%2Bz5X3Dp0jmJNuxC5TuHdeUPSJZ65qmUnVknf8sT8RMGwXALquIWLNGFtLK8tiLuWk8nSPm58CRCcx2QJ1kZTAtlNn5iXl1i9JukUctjS8S09nsr6ZMPF9K3vpz4iqexpE6n48asrGlrddaWzOlIf41%2Bn3UEtLa5kk2ycgt%2F%2Buok0Y7WxcWiM9Uewk87Uy2m4FRhF7T%2BfudDtyCE1omsMK4N6UIMTmcOCg1%2B5idcftQPnOqu3t2mNU2XFLCF1hu%2BM3%2Fn%2F0%2BEj%2BGpIrP4J0c5cMUzE0Gt8iHJL17Sgt6t1VSSHc6pU7ctREox1Dp0vluY6pz%2BmCPQ4GzMN189KCeW0QKsed3k2ZlylydYRU2o7qOaeLoDlPbkFzFILbKsuOsq6c2NIoA87pRpEaNF9W6jIP8pRDUhO20bBTzGdmQWUyOJwWsNDJBCoMWDPuAAcVwI5dBQPcH7q1382Bq0xkU1Zesih4qf1gvmyHE5qeYw8v7hxAY6pgFlza4s3u7UhGeQB0wBPQgncki3SLRh5QH%2FdTvXw7oqyFkWFMUQH2DUWHz%2FNnOK1l2WBO9D%2Fw9XyUwfD5z6pmLhhmb7i2E7SPSad%2B%2BhVWHBxLRoRFEMBnEPHsFIjS64fSlmLXRTo0eDlRVVCDo1sOy3v5CznrzatG%2BbOz0uxS8T7cQMx5quHewenFDkP9uFs%2FuyUVi%2B2ppYUhfGEPet9taJ27HnJai8&X-Amz-Signature=48d14c0c4f2f66c8fdb0277e1e0a9dd79b28f3953e922c5fddf9485cbb22b603&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 3.3 Discussion

**Exploration-exploitation Balance**

DRA는 Exploration-exploitation balance를 policy gradient 안에 직접 통합하여 적용함

- Base reward는 high score를 받는 completion을 reinforce함 

- Diversity weighting은 semantically novel completion에 learning signal을 amplify 

이러한 탐색은 low-resource settings (prompt당 sampling할 수 있는 응답 수가 제한 적인 경우)에서 중요함

→ DRA는 mode collapse를 방지하고 더 넓은 reasoning strategies를 유도함

**Ad-hoc vs Post-hoc Diversity**

generated completions간의 diversity를 모델링하는 방법은 크게 Ad-hoc,  Post-hoc 방식이 있음

1. **Ad-hoc**

1. **Post-hoc (본 연구에서 채택한 방법)**

## 4. Conclusion

- GRPO 형식의 RL에서 completions 간의 semantic diversity를 모델링할 수 있는 DRA 알고리즘 제안함

- 두가지 한계점이 있음

- 이런 쪽도 재밌다!ㅋㅋ
