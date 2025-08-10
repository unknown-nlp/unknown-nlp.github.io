---
categories: paper-reviews
date: '2024-07-02 00:00:00'
description: ' 논문 리뷰 - RL-JACK: Reinforcement Learning-powered Black-box

  Jailbreaking Attack against LLMs'
giscus_comments: true
layout: post
related_posts: false
tags: llm paper-review
title: 'RL-JACK: Reinforcement Learning-powered Black-box

  Jailbreaking Attack against LLMs'
---

**논문 정보**
- **Date**: 2024-07-02
- **Reviewer**: 상엽
- **Property**: RL, Safety

도입 배경

- LLM의 엄청난 성과 → LLM의 데이터에 포함된 unsafe 내용으로 인해 LLM이 비윤리적인 답변을 함. → Safety alignment를 추가, unsafe 쿼리에 대한 답변 거부를 포함하는 내용으로 fine-tuning → Alignment 이후에도 여전히 실패 사례 존재 → Jailbreaking prompts!

<br/>

Jailbreaking prompt

- 공격 방법 : 가상의 상황과 시나리오를 만든 후 비윤리적 질문을 추가.

- 기존 방법들의 한계점

	- 기존 jailbreaking 방법은 사람들이 직접 만들거나 모델 내부 접근이 필요했음. → scaling의 한계

	- LLM을 활용한 jailbreaking prompt 만드는 연구들로 발전 → 지속적으로 prompt를 refine하는 과정이 없기 때문에 제한이 큼.

	- genetic 모델을 활용해 prompt를 진화 시키는 방법도 등장했으나 확률적인 특성 때문에 제한적임.

→ Deep RL을  활용한 RL-JACK 제안

<br/>

**RL-JACK**

- DRL agent는 jailbreaking generation과 refinement를 맡음.

- 기존에 존재하는 jailbreaking 방법을 선택하는 것을 action으로 설정, 현재 state에서 적절한 action을 선정하는 것이 목표

- reward 설계: continuous feedback이 가능한 reward 설계

- state transition 설계: 안정된 학습을 위해 state를 정의할 방법 설계

<br/>

**Contributions**

- jailbreaking을 검색 문제로 정의함으로써 RL을 활용한 novel black-box jailbreaking 방법 제안

- 기존 SOTA 모델들과 비교했을 때 매우 큰 성능 향상을 보임.

- 아래 실험들을 통해 모델의 강점을 확인함.

	- Resiliency against SOTA defenses

	- Transferability across different LLMs

	- insensitivity to key hyperparameters

<br/>

### Threat Model and Problem Formulation

- Assumptions for attackers: black-box setup 가정

- 공격 목표

	1. target llm이 비윤리적인 질문에 대해 답하는 jailbreaking prompt를 생성하는 것

	1. 다른 방법론들과 달리 비윤리적 질문에 대해 정확한 답변을 생성할 수 있는지도 공격 평가의 척도로 사용하겠음.

- Problem formulation

	- Harmful $ Q = \{q_1,...,q_n\} $이 주어질 때 각각의 쿼리에 대해 정확한 답변($ u_i $)를 얻을 수 있는 prompt ($ p_i $)를 생성하는 것

	$$ \mathbf{p}_i^*=\operatorname{argmax}_{\mathrm{p} \in \mathcal{P}} M\left(\mathbf{q}_i, \mathbf{u}_i\right), \forall \mathbf{q}_i \in Q $$

### Solve Jailbreaking with DRL

- 최적의 Prompt $ p_i $를 찾는 작업은 일종의 searching problem이라고 생각

- 엄청나게 넓은 search space에 대해 다음 두 가지의 search 전략이 있음.

		- Stochastic search

		- 초기 값을 랜덤하게 설정, 현재 region에서 random exploration을 통해 근처 region으로 이동

		- genetic algorithm이 여기에 해당: 현재 seed를 mutation한 후 다음 seed로 이동

	- Deterministic search

		- 구체적인 규칙에 의해서 다음 region으로 이동 e.g) gradient-based method

- 하지만 LLM 내부에 접근이 불가능하기 때문에 Deterministic 방법을 적용할 수가 없음. → Black-box setup에서 효과적인 deterministic search 방법으로 RL을 활용

	- Agent는 deep neural network를 활용

	- 최적 policy를 찾기 위해 학습을 하고 나면 deterministic한 의사 결정 가능

<br/>

DRL이 아무리 효과적이라 해도 시스템 디자인에 너무 의존적임.

초기 시도: 답변 거절 여부를 활용한 suffixes 토큰 추가

- 관련 여구: suffixes로 특정 토큰을 추가하는 것이 jailbreaking을 가능하게 하더라.

- RL agent의 역할 : jailbreaking suffixes를 추가

- harmful query $ q_i $, 초기 prompt $ p_i^{(0)} $ → suffix로 추가할 토큰 선택 → $ p_i^{(1)} $ → Target LLM에 입력 → $ u_i^{(1)} $→ reward 계산

- Reward는 Keyword match로 계산, llm의 결과가 거절을 의미하는 키워드나 phrases를 포함하는지 여부로 판단 (I’m sorry, I cannot, etc.) → 효과적이지 않았음.

- token 단위 RL 디자인의 문제 원인

	1. token 선택은 vocab만큼의 action space를 가짐. token이 여러개라면 space가 기하급수적으로 커짐.

	1. 답변 거부에 대한 키워드가 없을 때에만 1점을 줌. 성공적인 suffixes가 매우 적기 때문에 거의 zero reward를 받음. (sparse reward problem)

→ 결론적으로 action space는 제한적이어야 하며 reward는 dense 해야 한다.

<br/>

### Our Attack Overview

**Rationale for action design: large search space를 피하기**

- Helper LLM을 이용한 prompt generation 방법 제안

	- agent의 역할은 helper 모델이 jailbreaking prompt를 생성하기 위한 strategy를 선택하는 것

	- Helper LLM은 선택된 strategy를 기반으로 prompt를 생성하는 것

- 10개의 strategies를 선정 (Section 4.4)

	- 추가 context를 생성하고 harmful 질문을 여기에 추가하는 유형 (7개, $ a_1,...,a_7 $)

	- context 추가없이 현재 질문을 변형하는 것 (3개, $ a_8, a_9, a_{10} $)

<br/>

**Rationale for reward design: meaningful dense rewards 방법**

- 실제 LLM의 답변이 harmful query에 대한 답변이 맞는지 여부로 판단

- 0, 1이 아닌 continous한 reward를 주기 위한 방법으로 pre-specified “reference”를 도입

- reward를 계산하기 위해 unaligned model을 이용. harmful question에 대한 답변($ \hat{u_i} $)를 활용

- LLM을 이용한 reward 평가는 계산 비효율적, 고비용이라 제거 했다고 하는데 공감은 안됨. (오히려 aligned 되어 있어서 제대로 평가가 안될 수 있다는 게 더 좋은 이유일듯함.)

<br/>

**System overview**

- $ s^{(0)} $ : 초기 harmful query

- $ a^{(0)} $: prompt 수정 전략 선택

- $ p^{(0)} $: Helper LLM을 통한 prompt 수정 (+ query)

- $ R(u^{(0)}, \hat{u}) $ : reward 계산

<br/>

### Attack Design Details

**RL formulation**

Markov Decision Process (MDP): $ \mathcal{M}=(\mathcal{S}, \mathcal{A}, \mathcal{T}, \mathcal{R}, \gamma) $

- $ \mathcal{T}: \mathcal{S} \times \mathcal{A} \rightarrow \mathcal{S} $ : state transition function

- $ \mathcal{R}: \mathcal{S} \times \mathcal{A} \rightarrow R $: reward function

- $ \mathbb{E}\left[\sum_{t=0}^T \gamma^t r^{(t)}\right] $ 를 최대로 하는 optimal policy 찾기

<br/>

**State and action**

state

- 현 시점에 refined된 prompt $ p^{(t)} $ 다음 state $ s^{(t+1)} $로 사용

- LLM의 답변을 state에 포함할 경우 state의 space가 너무 커지며 cost가 커지기 때문에 제외함. (실험이 있는지는 추후 확인해보자.)

action

- 아래의 pre-defined된 action과 instruction을 이용.

<br/>

**State transition**

- 이전 prompt를 state로 활용할 때 다양한 action들이 switch하는 것은 jailbreaking 생성 전략에 혼란을 줄 수 있음.

	- state continuity를 위해 context를 추가하는 action ($ a_1,...a_7 $)에 대해서 교차 연산 추가

- Crossover: helper 모델을 활용할 때 두 결과물을 합치는 방식

<br/>

**Reward**

- $ \Phi $ : text encoder

$$ r^{(t)}=\operatorname{Cosine}\left(\Phi\left(\mathbf{u}_i^{(t)}\right), \Phi\left(\hat{\mathbf{u}}_i\right)\right)=\frac{\Phi\left(\mathbf{u}_i^{(t)}\right) \cdot \Phi\left(\hat{\mathbf{u}}_i\right)}{\left\|\Phi\left(\mathbf{u}_i^{(t)}\right)\right\|\left\|\Phi\left(\hat{\mathbf{u}}_i\right)\right\|} $$

**Agent**

- text encoder + classifer 구조

<br/>

**Termination and training algorithm**

- maximum time step $ T $ : 5

- reward threshold $ \tau $ : 0.75

- PPO 알고리즘 활용

$$ \begin{aligned}
& \left.\operatorname{maximize}_\theta \mathbb{E}_{(\mathrm{a}(t), \mathrm{s}}(t)\right) \sim \pi_{\theta_{\text {old }}}\left[\min \left(\operatorname{clip}\left(\rho^{(t)}, 1-\epsilon, 1+\epsilon\right) A^{(t)}, \rho^{(t)} A^{(t)}\right)\right], \\
& \text { where } \rho^{(t)}=\frac{\pi_\theta\left(\mathrm{a}^{(t)} \mid \mathrm{s}^{(t)}\right)}{\pi_{\theta_{\text {old }}}\left(\mathrm{a}^{(t)} \mid \mathrm{s}^{(t)}\right)}, \quad A^{(t)}=A_{\pi_{\theta_{\text {old }}}}\left(\mathrm{s}^{(t)}, \mathrm{a}^{(t)}\right)
\end{aligned} $$

- 일반적으로 advantage function $ A^{(t)} = R^{(t)} - V^{(t)} $ 으로 계산하는 것이 더 효과적이라고 하나 현재 연구에서는 Reward를 직접적으로 사용

	- Value function을 학습할 필요가 없다는 장점.

	- Value 추정 과정에서 생기는 bias가 학습을 방해할 수 있기 때문

	- 개인적 궁금함 (이런식으로 주장할 때는 실험을 해야하는가?)

<br/>

**Launching attack with a trained agent**

- harmful query 제공 → action 선택 → Helper LLM에서 5개의 jailbreaking prompt 생성 → 성공 여부 판단 → 실패 시 재실행 (최대 5번까지)

<br/>

<br/>

### Attack Effectiveness and Efficiency

- Dataset

	- AdvBench에서 520 harmful query (4:6 train test split)

	- Max50 : 특히 더 어려운 query 50개 선정

- Target LLM, helper model, unaligned model

	- target: Llama2-7b, 70b, Vicuna-7b, 13b, Falcon-40b, GPT-3.5-turbo

	- helper: Vicuna-13b

	- Unaligned version Vicuna-7b

- Baselines

	- black-box, gray-box, white-box attack 방법 모두 비교

- Metric

	- effectiveness

		- ASR (키워드 기반)

		- answer와 reference answer와의 cosine 유사도

		- GPT-3.5를 이용한 response relevancy 평가

	- efficiency

		- total run time (Total) : 모든 질문에 대해 jailbreaking prompt를 생성하는 총 run time

		- per question prompt generation time (Per-Q)

Results

**Effectiveness**

- In-context learning을 활용해 prompt를 수정하는  PAIR & Cipher는 성능 안좋음.

- Gradient를 이용하더라도 토큰 단위 추가만 하는 GCG (white-box model) 성능 낮음.

- Genetic algorithm을 활용하는 GPTFUZZER, AutoDAN 모델이 상대적으로 우수

- RL-JACK (결과가 좋기는 한데 상식적이지는 않음.)

	- 큰 모델에서도 우수함.

	- MAX50은 더 잘함. (We believe it is because of the capability of our RL agent to refine jailbreaking prompts based on the feedback, making RL-JACK easier to bypass these difficult questions. ???)

	- Genetic 기반 방법과 비교햇을 때 GPT-judge 결과가 큰 차이가 남.

<br/>

**Efficiency**

<br/>

### Resiliency against Defenses

- 방어기법의 종류

	- input mutation-based defenses

		- Perplexity: GPT-2를 이용, perplexity의 값이 20보다 높은 입력 프롬프트를 거부

	- filtering-based defenses

		- RAIN: novel decoding strategy를 활용 (self-evaluation & rewind, output을 스스로 평가하고 유해하면 되돌아가서 다시 생성)

	- Rephrasing

- Target models: Llama2-7b-chat, GPT-3.5-turbo, and Falcon-40b-instruct

Results

- RL-JACK is more resilient against SOTA defenses compared to the baseline attacks

- 특히, Perplexity 결과가 인상적 (근데 이건 정상적인 질문에 대해서도 답변을 못할 것 같은 느낌?)

<br/>

### Attack Transferability

- 하나의 Target LLM을 대상으로 학습 된 모델이 다른 Target LLM에도 작동하는지 평가

Results

- 돈이 없어서 GPT-judge 안했음 (요즘에도 이런게 되나)

- 더 큰 모델로의 transfer는 안된다. 작은 모델로의 Transfer는 잘 된다.

<br/>

### Ablation Study and Sensitivity Test

model: Vicuna-7b (small model) and Llama2-70b-chat (large model)

- Ablation study

	- Agent

		- random agent: action을 random하게 선택하는 agent

		- LLM agent: LLM에게 다음 action 선택을 맡기는 agent

	- Reward

		- KM as reward: Keyword match를 reward로 활용

	- Action

		- Token-lavel action: harmful query에 token 추가를 action으로

		- Hyperparameter sensitivity

	- $ \tau $ : 0.7 ~ 0.8

	- helper llm

		# Discussion

- Action & Reward design

	- 다양한 jailbreaking 전략을 결합한 앙상블과 같다고 볼 수 있음.

	- 인풋 암호화를 통한 jailbreaking 방법과 같이 여러 방법들을 쉽게 결합해 action space를 확장할 수 있음.

	- Reward 함수는 개선이 필요하다.

		- 거부 응답과 실제 정답의 구별력 개선 필요 : 현재 거부 응답의 cosine similarity도 0.6을 보임 (경험상 이건 embedding 모델만 바꿔도 해결 가능한 부분 같음.)

		- 정답 reference를 여러 개로 활용할 방법은 없을까?

		- GPT-judge를 reward로 활용하면 어떨까? 현재는 비용 문제로 제외

- Helper LLM and LLM agent

	- helper llm은 주어진 몇 개의 prompt를 단순 실행하는 것이다보니 성능에 크게 영향을 받지 않는 거 같음.

- RL-JACK for LLM safety alignment

	- 자동 생성된 jailbreaking 프롬프트로 LLM 안전성 개선 가능

	- jailbreaking prompt에 대해 답변 거부하도록 fine-tuning

	- jailbreaking prompt 확보 비용을 줄일 수 있을듯 (우리가 생각하고 있는 부분)

<br/>

- 토큰 단위 변화를 넘어서 jailbreaking 자체에 RL을 시도한 건 처음

- Jailbreaking을 search 문제로 변환하여 action space를 대폭 줄이고 확률에 의존하는 genetic algorithm보다 좋은 성과를 보임.

- 글이 장황한 경향

- 내용은 매우 흥미롭지만 몇몇 실험이 빠지거나 개선해야할 필요성이 보임.

- 방어기법에 대한 resiliency를 보이는 건 재밌는 방법 같음.

- 현재 진행중인 내용과 많이 일치해서 흥미로움.