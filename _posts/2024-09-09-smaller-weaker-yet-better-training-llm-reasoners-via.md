---
categories:
  - paper-reviews
date: "2024-09-09 00:00:00"
description: 논문 리뷰 - Knowledge Distillation, LLM, Limited Budget 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
  - knowledge distillation
  - language-model
  - limited budget
  - llm
  - paper-review
  - reasoning
thumbnail: assets/img/posts/2024-09-09-smaller-weaker-yet-better-training-llm-reasoners-via/thumbnail.jpg
title: "Smaller, Weaker, Yet Better: Training LLM Reasoners via Compute-Optimal Sampling"
---

**논문 정보**

- **Date**: 2024-09-09
- **Reviewer**: hyowon Cho
- **Property**: Knowledge Distillation, LLM, Limited Budget

> Google DeepMind (2024-08-30)

# Introduction

많은 연구들이 이미 언어모델을 학습시키는 데 synthetic 데이터를 사용하고 있다. 이들 중, reasoning task에서 가장 일반적인 방법은 하나의 질문에 대해서 여러 가지 후보 답변들을 생성하게 하고, 이를 gold answer와 비교해, 맞는 정답을 가진 것들만 남기고 나머지는 버리는 것이다.

하지만, 이렇게 여러 개의 데이터를 strong LMs로 부터 생성해 사용하는 것은 비싸고, resource-intensive하다. 또한 현실적으로 우리가 사용할 수 있는 예산은 정해져있기 때문에 만들 수 있는 solution도 그리 많지는 못하다.

이 논문에서는 fixed compute budget 상황에서, weaker but cheaper (WC) model이 우리가 일반적으로 생각하는 것과 다르게 stronger but more expensive (SE) model을 사용하는 것보다 낫다고 주장한다.

이를 증명하기 위해 저자들은 크게 3가지 축에서 데이터들에 대한 비교를 진행한다.

1. coverage, the number of unique problems that are solved,

1. diversity, the average number of unique solutions we obtain per problem,

1. false positive rate (FPR), the percentage of problems that arrive at the correct final answer but with a wrong reasoning.

당연히 고정된 예산 하에서, WC model이 SE model보다 더 많은 데이터를 만들어낼 수 있다. 하지만 SE가 당연히 퀄리티는 높을 것. 그렇기 때문에, WC가 더 높은 coverage and diversity 그리고 동시에 higher FPR를 가질 것이라고 이야기한다.

이후, 저자들은 이 추측을 검증하기 위해서 SE and WC로 만든 데이터를 이용해서 모델들을 finetuning한다. 단순 하나의 방법이 아니라 여러 가지로.

1. knowledge distillation, where a student LM learns from a teacher LM (Hinton et al., 2015);

1. self-improvement, where an LM learns from self-generated data (Huang et al., 2022); and

1. a new paradigm we introduce called Weak-to-Strong Improvement, where a strong student LM improves using synthetic data from a weaker teacher LM.

저자들은 여러 개의 벤치마크에서 아주 일관적 SE-generated data 보다 WC-generated data로 학습한 결과가 훨씬 좋음을 보인다 (일반적인 믿음과 달리) 즉, WC-generated data에서 샘플링하는 것이 훨씬 compute optimal하다는 것.

어느 정도 큰 스케일에서 더 작은 모델과 큰 모델의 성능 갭이 점차 줄어들고 있는 요즘, LM reasoners를 어떤 방식으로 학습할지 생각을 하게 한다.

# Preliminaries

- D = {𝑞𝑖, 𝑎𝑖} = training

- reasoning questions = 𝑞𝑖

- final answers = 𝑎𝑖

다 아시겠지만, 이들을 가지고 synthetic data를 만드는 방법은 다음과 같다:

1. sample multiple solutions for each 𝑞𝑖 at a non-zero temperature

1. create the synthetic data with reasoning chain & generated answer

1. filter the incorrect solutions by comparing 𝑎ˆ𝑖 𝑗 to 𝑎𝑖 and removing the solutions whose final answer do not match that of the gold answer

### Metric

- 𝑐𝑜𝑣𝑒𝑟𝑎𝑔𝑒@𝑘 (aka 𝑝𝑎𝑠𝑠@𝑘)

- 𝑑𝑖𝑣𝑒𝑟𝑠𝑖𝑡𝑦@𝑘

- false positive rate

# Compute-Matched Sampling and Training

당연히 고정된 예산, 고정된 sampling budget (FLOPs) 상에서, 사람들은 더 weaker but cheaper (WC) model을 통해서 더 많은 샘플들을 만들어낼 수도 있고 혹은 stronger but more expensive (SE) model을 통해 더 적지만 양질의 데이터를 만들 수 있다.

WC model가 𝑃*𝑊𝐶 parameters를 가지고, SE가 𝑃*𝑆𝐸 parameters를 가진다고 하고, 두 모델을 이용해서 무조건 같은 예산만을 사용할 수 있다고 하면, 만들 수 있는 데이터의 개수는 다음과 같이 차이가 난다.

- Following (Kaplan et al., 2020), FLOPs per inference token = 2𝑃

- FLOPs for 𝑇 inference tokens = 2𝑃𝑇

- assume that generating each solution requires an average of 𝑊 inference tokens

- 𝑆*𝑊𝐶 and 𝑆*𝑆𝐸 = number of samples we generate per question

- total cost

즉, 고정 예산에서 𝑃_𝑆𝐸/𝑃_WC 만큼 WC에서 더 데이터를 만들어낼 수 있다는 말. 이렇게 둘 중 하나로 데이터를 만든 이후, 고정된 스텝으로 모델들을 학습시켜보고 비교하여 데이터들의 유용성을 판단할 수 있다.

언급했듯 학습 방법은 3가지:

1. knowledge distillation(Student-LM finetuning)

1. self-improvement

1. 그리고 이들이 제안하는 novel weak-to-strong improvement paradigm

# Experimental Setup

- Datasets

- Data Generation

- Synthetic Data Evaluation

- Evaluating Finetuned Models:

# Experiments and Results

- (§5.1) we analyze the data along various quality metrics .

- (§5.2) Subsequently, we present the supervised finetuning results for the different setups .

- (§5.3) Finally, we perform ablation studies to study the impact of dataset size, sampling
  strategy, and the role of quality dimensions in the model performance.

## 1. Synthetic Data Analysis

### 1) Coverage

결론: Gemma2-9B (WC)이 Gemma2-27B (SE)보다 훨씬 좋았다.

- MATH:

- 11% and 6% at the low and high sampling budgets,

- 8% and 1% for GSM-8K.

즉, 더 많이 만드는 것이 퀄리티가 더 낮더라도 더 많이 문제를 푸는데 도움이 되었다. converge trend는 다양.

추가적으로, 더 많이 데이터를 만드는 것은 비단 낮은 난이도의 문제 뿐만 아니라 높은 난이도에서도 공통적이었다.

오히려 반대로, 더 큰 모델로 10개 만들 때는 풀지 못했던 어려운 문제도 더 약한 모델로 30번 만드는 경우에 자주 풀렸다고.

### 2) Diversity

Gemma2-9B에서 생성된 데이터의 다양성은 Gemma2-27B보다 MATH 데이터셋의 저예산에서 86%, 고예산에서 125% 더 높았으며, GSM-8K 데이터셋에서는 각각 134%와 158% 더 높음.

### 3) FPR

human 평가에 따르면 WC 모델이 생성한 해결책의 FPR이 MATH에서는 SE 모델보다 7% 높았고, GSM-8K에서는 2% 높았음.
-> 생각보다 차이는 안나지만, 그럼에도 불구하고 좋지는 않음.

## 2. Compute-Optimality Results for Training

그렇다면 이들은 다양하게 학습해봤을 때는 어떨까.

1. Student-LM Finetuning
   Gemma-7B를 WC와 SC로 학습한 결과.
   WC consistently outperforms the one finetuned on data from SC. 일반적인 믿음과 다르다.

1. WC-LM Finetuning
   Gemma2-9B를 Gemma2-9B가 만든 WC와 27B가 만든 SC로 학습한 결과. 대부분 WC가 더 나았지만, 그렇지 않은 경우도 존재. 저자들은 이것이 데이터가 너무 쉬워서라고 주장.

1. SE-LM finetuning
   Gemma2-27B를 양 데이터로 학습. 더 작은 모델로 만든 데이터가 놀랍게도 더 도움이 되었다.

> Takeaway: Overall, our findings challenge the conventional wisdom that advocates training on samples from the SE model, by showing that training on samples from the WC model may be more compute-optimal across various tasks and setups.

## 3. Ablation Studies

### Impact of Dataset Size

### Default vs Compute-Optimal Sampling from Cheap LMs

그렇다면, 기존에 SE를 사용하던 일반적인 방법처럼 데이터 개수를 통일하면?

볼 수 있는 것처럼, 더 퀄리티 좋은 것을 사용하는게 더 좋은 것은 확실하다.

### Coverage and Diversity:

# Scaling to state-of-the-art language models

> Takeaway: We demonstrate that price-matched sampling from weaker SoTA LMs produces
> superior reasoners compared to finetuning with data from stronger SoTA models.

# Conclusion
