---
categories:
- paper-reviews
date: '2024-04-02 00:00:00'
description: 논문 리뷰 - Reinforcement Learning, Alignment 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- alignment
- classification
- gpt
- language-model
- llm
- paper-review
- reinforcement learning
- rlhf
thumbnail: assets/img/posts/2024-04-02-preference-free-alignment-learning-with-regularized-relevance-reward/thumbnail.jpg
title: Preference-free Alignment Learning with Regularized Relevance Reward
---

**논문 정보**
- **Date**: 2024-04-02
- **Reviewer**: 준원 장
- **Property**: Reinforcement Learning, Alignment

## 0. Preliminary

- Preference

### PPO (Chat-GPT Training)

1. SFT

→ Instruction Tuning Data로 Pre-trained Model 학습

1. Reward Model Training

→ 어떤 text prompt에 대한 응답(response)를 LLM(large language model)이 예측했을 때, 그 응답에 대한 reward score(보상 점수)를 예측하도록 Reward Model을 학습.

→ Using the Bradley-Terry Model to estimate the pairwise loss. (가장 기본)

```python
class PairWiseLoss(nn.Module):
    """
    Pairwise Loss for Reward Model
    """

    def forward(self, chosen_reward: torch.Tensor, reject_reward: torch.Tensor) -> torch.Tensor:
        probs = torch.sigmoid(chosen_reward - reject_reward)
        log_probs = torch.log(probs)
        loss = -log_probs.mean()
        return loss
```

1. PPO

→ PPO를 학습하기 위해서는 3개의 Model이 필요함 (Trainable SFT(RLHF할 SFT), Frozen SFT, Reward Model)

3.1. 학습하고자하는 text prompt에 대해서 (1) Trainable SFT와 Frozen SFT logit outputs 사이의 KL-Divergence 계산 (2) Trainable SFT(RLHF할 SFT)의 text output을 Reward Model에 넣어서 reward score을 계산 (3) (1)+(2)를 더해서 PPO의 Reward를 계산

{% include figure.liquid loading="eager" path="assets/img/posts/2024-04-02-preference-free-alignment-learning-with-regularized-relevance-reward/image_000.png" class="img-fluid rounded z-depth-1" %}

3.2. Ratio (New probs [학습하고자하는 text prompt에 대한 Trainable SFT(RLHF할 SFT)의 확률 값] / 학습하고자하는 text prompt에 대한 [Frozen SFT]의 확률)가 특정 범위 (0.8~1.2)에 일때만 학습이 되도록.

{% include figure.liquid loading="eager" path="assets/img/posts/2024-04-02-preference-free-alignment-learning-with-regularized-relevance-reward/image_001.png" class="img-fluid rounded z-depth-1" %}

```python
class PolicyLoss(nn.Module):
    """
    Policy Loss for PPO
    """

    def __init__(self, clip_eps: float = 0.2) -> None:
        super().__init__()
        self.clip_eps = clip_eps

    def forward(self,
                log_probs: torch.Tensor,
                old_log_probs: torch.Tensor,
                advantages: torch.Tensor,
                action_mask: Optional[torch.Tensor] = None) -> torch.Tensor:
        ratio = (log_probs - old_log_probs).exp()
        surr1 = ratio * advantages
        surr2 = ratio.clamp(1 - self.clip_eps, 1 + self.clip_eps) * advantages
        loss = -torch.min(surr1, surr2)
        if action_mask is not None:
            loss = masked_mean(loss, action_mask)
        loss = loss.mean()
        return loss
```

### DPO (Omit Reward Modeling)

: Clipping을 차용한 RLHF objective를 다음과 같은 수식으로 쓸 수 있음

→ DPO의 목적은 Reward Modeling training 없이 Pairwise triplet으로 Trainable SFT를 직접 Alignment Training할 수 있다를 수식적으로 증명+실험적으로 보인 논문.

→ Policy의 Ratio에 따라 Bradley-Terry Model에 부합하는 목적함수를 설계할 수 있게되며, Triplet을 직접 활용해 SFT Model을 직접적으로 학습할 수 있다.

## 1. Introduction

- 서두에 언급했듯이, RLHF나 대안인 DPO가 LM에 직접적인 pairwise human feedback을 주입하기 위해 활용된다.

- 논문에서는 human feedback이 가지고 있는 선천적인 한계점/bias을 지적한다.

- ***Relevance를 Reward Signal로 주어서 LLM의 Alignment를 human preference 없이 증가시켜볼 수 있지 않을까?***

- 이를 위해 Relevance에 대한 정의부터 하고 넘어감

{% include figure.liquid loading="eager" path="assets/img/posts/2024-04-02-preference-free-alignment-learning-with-regularized-relevance-reward/image_002.png" class="img-fluid rounded z-depth-1" %}

- 제안하는 방법론은

## 2. Motivation and Preliminary Study

- Relevance는 정의상 User의 Specific한 Need나 Request에 얼마나 적절한 답변을 할 수 있는가를 측정하는 척도이다.

- Reward Model 관점에서 논문에서는 2가지 Research Question을 던진다.

### 1. 현존하는 Open-Source RMs들이 Relevance를 capture하는가?

- PopQA에서 popularity가 1K이하인 530 entities에 대해서 (query, relevant response, irrelevant response triplet 구축)

- irrelevant는 GPT API로 관련 없는 entity에 대해서 생성하도록 지시

(“Please tell me about {entity}”)

{% include figure.liquid loading="eager" path="assets/img/posts/2024-04-02-preference-free-alignment-learning-with-regularized-relevance-reward/image_003.png" class="img-fluid rounded z-depth-1" %}

[회색: Anthropic-HH, SHP training set으로 학습한 RM, * 자체적으로 학습한 RM]

⇒ Anthropic-HH & SHP이 Human preference를 반영하는데에는 적합하더라도, trivial한 relevance는 capture하지 못한다.

### 2. Relevance가 Alignment를 위해서 좋은 지표인가?

- Contriever를 직접적인 RM으로 사용해서 Reward Signal을 줘보자

-  x : query

-  \hat{y} : rollout response in the exploration stage of PPO 

-  M(x) \cdot M(\hat{y})\rightarrow r_{x}\in \R^{1}  : M is contriever

- Anthropic-HH dataset 사용, Vicuna Bench

- Preference가 Reward Training 이후 증가했는지 평가

{% include figure.liquid loading="eager" path="assets/img/posts/2024-04-02-preference-free-alignment-learning-with-regularized-relevance-reward/image_004.png" class="img-fluid rounded z-depth-1" %}

[For a fair comparison with the open-source RMs, we train SFT model based on LLaMA-2-7B (Touvron et al., 2023) with the 161k chosen responses in Anthropic-HH]

⇒ Contriever reward가 preference를 약화시킨다.

⇒ 또 해당 reward는 relevance는 높지만, response 길이가 짧다.

**[Reward Hacking (agent가 편법과 같은 의도하지 않은 방법론을 통해 목표를 달성하는 것) 발생 → 40%가 question을 그대로 copy and paste하도록 LMs을 training하는 signal을 주었다고 함]**

## 3. R^3: Regularized Relevance Reward

- 이전에 언급한 문제들을 해결하기 위해 다양한 Regularizing 기법들을 Reward Function에 주입하기 시작.

### Length Incentive (LI)

-  r_{x} 가 response를 짧게하는 것을 방지하기 위함

### Repetition Penalty (RP)

- Length Incentive를 걸어두면 query랑 똑같은 문장을 계속 반복생성하는 Reward hacking이 일어남.

- unique trigram을 보장하는 아래의 reward를 추가함

-  RP(\hat{y})= \frac{\# unique \ trigram \ of  \ \hat{y}}{\# \ trigrams \ of  \ \hat{y}}

⇒  r_{x} \cdot LI(\hat{y})\cdot RP(\hat{y})

- 높은 relevance

- 긴 generation

- less repetition

### Reference Answer Relevance (r_{y})

- Contrained/Factual한 Response를 요구하는 Query에서 여전히 Diverse한 답변을 생성하는 위의 Reward는 치명적일 수 있음 

- 저자들은 Open-ended/Closed Ended Query에 대해서 다른 Reward를 적용함.

- F(r_{y}) \ ,where \ M (y) · M (\hat{y}) → r_{y}: 범위 맞춰주는 interpolation function

⇒ Mixture of Reward Function, Only needs SFT dataset!

### Query Type Classification

- 저자분들도 Open-ended vs Closed Ended Query 구분 주관적이라고 인정

- 100개정도 GPT-4로 구분했을 때 83% 정확도 나왔고 사내 LLAMA2로 구분했을때 만족할만한 성능이라 사용했다고 보고.

### PPO Training

## 4. Results

### 4.1 R^3가 human preference를 증가시키는가?
