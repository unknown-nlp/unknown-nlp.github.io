---
categories: paper-reviews
date: '2024-08-13 00:00:00'
description: ' 논문 리뷰 - Physics of Language Models: Part 2.1, Grade-School Math and
  the Hidden Reasoning Process'
giscus_comments: true
layout: post
related_posts: false
tags: llm paper-review
title: 'Physics of Language Models: Part 2.1, Grade-School Math and the Hidden Reasoning
  Process'
---

**논문 정보**
- **Date**: 2024-08-13
- **Reviewer**: 준원 장
- **Property**: Reasoning, Explainability

[//]: # (table_of_contents is not supported)

## 1. Introduction

### Motivation

- small language models (GPT2 in this paper)의 GSM8K, its augmentation의 성능을 향상시키는 기존의 연구는 많았음.

- 논문에서는 단순한 성능 향상이 아닌 보다 근본적인 질문을 해결하고자 함.

	- small language model이 진정으로 grade-school (초등학교 수준)의 수학문제를 풀 수 있는 능력을 학습할 수 있는가?

- 이를 위해 6개의 RQ를 수립하고, 이를 검증하기 위한 굉장히 통제적인 실험을 진행함

<br/>

### Research Question

1. LM은 진정으로 추론 능력을 개발할 수 있을까?, 아니면 단순히 템플릿을 기억하는 것일까?

	(Can language models truly develop reasoning skills, or do they simply memorize templates?)

1. LM의 hidden (mental) reasoning process는 무엇일까? (hidden state에서는 어떤 semantic이 형성되었는가? ⇒ Explainability를 위한 질문)

	(What is the model’s hidden (mental) reasoning process?)

1. LM은 모델은 인간과 유사 혹은 다른 방식으로 수학 문제를 해결할까?

	(Do models solve math questions using skills similar to or different from humans?)

1.  GSM8K와 같은 데이터셋에 훈련된 LM은 GSM8K 문제를 해결하는 데 필요한 것을 넘어서는 추론 능력을 학습할 수 있을까? (⇒ Generalization에 대한 질문)

	(Do models trained on GSM8K-like datasets develop reasoning skills beyond those necessary for solving GSM8K problems?)

1. 어떤  hidden (mental) reasoning process이 추론 오류를 범하게 만들까?

	(What mental process causes models to make reasoning mistakes?)

1. GSM8K 수준의 수학 문제를 효과적으로 해결할 수 있는 LM은 얼마나 크거나 깊어야 할까?

	(How large or deep must a model be to effectively solve GSM8K-level math questions?)

⇒ 각 RQ에 1:1로 대응되는 해답을 내놓지는 않지만, 논문 전반에 걸쳐 위에 대한 대답을 하고 있음

<br/>

### Pre-Training From the Scratch

- 논문에서는 통제적인 실험을 위해 아래를 근거 삼아 from the scratch LM을 실험에 활용함

	- Data Contamination

		- 상용되는 LLM은 massive pre-training corpus를 활용하기에, (해답이 동일하진 않더라도) GSM8K와 동일한 문제 또는 다른 수학문제를 이미 사전에 학습했을 가능성이 높음

		- 따라서, 일부 RQ(4,6)에 완벽한 답을 할 수 없다고 옹호함

	- Solution Diversity

		- GSM8K는 7.5K training data밖에 없으며, GPT4o로 다양한 solution을 prompting해도 (ICL의 한계 때문에) training dataset에 표현된 template에서 벗어나는 diverse solution을 생성하기에는 한계가 있다고 주장.

	- To this end,

		1. 직접 데이터를 만들고 GPT2에 training한다.

		1. ‘Alice’s apple is three times the sum of Bob’s orange and Charles’s banana.’와 같이 parameter(미지수)간의 dependency가 명시된 문장들로 이루어진 합성 데이터를 구축

		1. ‘a candle burned for 12 hours at 1 inch per hour’ (초는 시간이 지날수록 길이가 짧아진다.) 처럼 parameter(미지수)간의 dependency가 explicit/implicit하게 추론되는게 아니라 Common Sense를 기반으로 문장 자체 해석을 통해 수학적 개념을 도출해야하는 문장을 제외시켰다.

		1. 정수만 사용하고, 큰 수 방지를 위해 arithmetic mod23를 사용

			1. 12 + 20 = 9. (32%23=9)

		1. 이렇게 함으로써 특정 template에 구애받지 않는 diverse한 합성 데이터를 구축하는 프레임워크 제시 (GPT2-small (100M)보다 많은 데이터 생성해서 training)

<br/>

## 2. Result 1: Data Generation

> Betty is saving money for a new wallet which costs 100. Betty has only half of the money she needs. Her parents decided to give her 15 for that purpose, and her grandparents twice as much as her parents. How much more money does Betty need to buy the wallet?

- “Betty’s current money = 0.5 × cost of the wallet” , “money given by grandparents = 2 × money given by parents.”처럼 GSM8K가 다변수로 엮여있는 방정식을 설계하는게 Data Generation의 목표

- GSM8K를 흉내내는 데이터셋이기에, LM이 학습되면서 (저자들이 정의한) 아래의 dependency를 학습하도록 dataset generation framework를 설계하였음

	1. Direct dependency(♡): A = 5 × (X + Y) 경우, A는 X와 Y가 주어진 후에 계산이 되는 dependency.

	- Instance dependency(♠): "모든 교실에는 X개의 의자가 있고, Y개의 교실이 있습니다." LM이 (독립적인) X와 Y를 곱하여 총 의자 수를 추론하는 depedency.

	- Implicit dependency(♣): "Bob은 Alice보다 3배 많은 과일을 가지고 있습니다. Alice는 사과 3개, 계란 4개, 바나나 2개를 가지고 있습니다." LM이 2문장에서 사과와 바나나가 과일이고 계란은 과일이 아님을 알아내야 하며, "Alice의 과일"이라는 것은 문제 진술에서 파생된 추상적 parameter(미지수).

<br/>

- Data Generation은 parameter(미지수)간의 hierarchy를 기준으로 그래프 설립 → 문제 생성의 순을 따름

	1. 문제에서 parameter(미지수)를 담당할 category기반 layered structure 구조를 아래와 같이 구축.

		1. Structure Graph

				1. Dance Studio - School Daypack를 연결하면 “the number of school daypacks in each dance studio” Instance parameter로 설정 가능

		1. “the total number of classrooms in Central High” (솔직히 100% 이해는 안됨;;;)는 (다른 문장이 더 필요) Abstract parameters로 지정, Structure Graph에 명시적 표기가 불가.

		⇒ 1문제에 제한적인 vertex만 포함됨으로 여러 문제 학습해서 영어 개념을 암시적으로 학습시킨다고 함

		⇒ “the total number of classrooms in Central High”같은 Abstract parameters를 이해하려면 LM이 여러 문장을 이해해야함

	1. Dependency Graph

		1. 각 instance parameter에 대해 random number generator  RNG를 포함하여 depedency를 생성 수 있는 (최대 4개까지) parameter set을 구성

			1. [param A ] is X more than the difference of [param B ] and [param C ]라는 문장이 있다면

			1. B & C & RNG → A로 edge를 그림

		1. Abstract parameters는 instance parameter에 의해 암시되도록 설계

	1. Problem Generation

				- Problem은 각 인스턴스 instance parameter에 대해 한 문장씩 영어로 의존성 그래프를 기술

		- 난이도를 향상을 위해 이전에 생성한 문장 순서를 무작위로 permute

		- 특정 parameter(미지수)가 선택되고 [Problem;Question] or [Question;Problem] 형식으로 data generate

	1. Solution Construction

		- CoT 형식을 차용해서 topological 문장을 나열하는 식으로 solution 구성

		- parameter(미지수)를 아래와 같은 식으로 서술함으로써 solution을 구성

			- Define [param] as X; [intermediate steps]; so X =

					1. question answering에 필요한 parameter(미지수)만 solution에 포함

		1. sentence내 logical order 준수

		1. 모든 operation을 binary operation으로 제한 (e.g., g = 12+13+7 is broken into g = 12+R and R = 13+7)

	1. Data Generation

		1. 매 문제마다 hierarchical categorization (i.e., the English part); a structure graph (i.e., the instance parameters); a dependency graph; arithmetic computations on the dependency graph; integer numbers (i.e., the RNG); problem sentence permutation; and the query parameter을 랜덤하게 선택해 문제의 중복 방지.

		1. $ GSM^{op≤op,ip≤ip} $

			1. op: solution에 있는 operation 수

			1. ip: question에 있는 instance parameter 수

		1. Training & Eval Setup (Training Data → Eval Data)

			1. iGSM-med

				1. $ GSM-med^{op≤15,ip≤20} $ → $ GSM-med^{op≤15,ip≤20} $, $ GSM-med^{op=\{15, 20, 21, 22, 23\},ip≤20} $,  $ GSM-med^{op=op,reask} $ (query parameter만 바꾼 문제)

			1. iGSM-hard

				1. $ GSM-hard^{op≤21, ip≤28} $ → $ GSM-hard^{op≤21,ip≤28} $, $ GSM-hard^{op=\{21, 28, 29, 30, 31, 32\},ip≤28} $,  $ GSM-hard^{op=op,reask} $ (query parameter만 바꾼 문제)

			1. problem & question order

				1. GSM_pq (problem → query parameter)

				1. GSM_qp (query parameter → problem)

			1. Define Owl Forest’s Elephant as y; so y = 11. Define Parrot Paradise’s Raccoon as t; so t = y = 11."은 "Define Inst as a; so a = 0. Define Inst as b; so b = a = 0."라는 하나의 solution template으로 정의하면 7billion~90 trillion개의 solution template이 나온다고 주장.

			<u>⇒ op ≤ 21 samples로 학습 op ≥ 28 samples로 eval: 통제된 실험 가능</u>

		<br/>

				→ mod5 arithmetics로 설계된 iGSM-med는 GPT-4(ICL setting)도 operation이 많아질수록 성능이 낮아진다고 함 (pre-training preference 때문에 당연할듯… 아니면 진짜 복잡한건 못풀던가…)

		<br/>

<br/>

## 3. Result 2-3: Summarize Model’s Behavior Process

- LM 학습은 GPT2 small을 일정 training step을 만족시킬만큼 데이터셋을 합성해 진행

<br/>

> **Result 2**

	- iGSM-med 또는 iGSM-hard로 pre-training시, 더 어려운 (즉, 더 많은 연산이 필요한) 수학 문제에서도 좋은 성능을 보임

	- 따라서, LM은 solution template을 단순히 기억하는 대신 실제로 일부 reasoning process를 학습할 수 있다고 주장 (문장 1개의 format을 정해져 있어서 pattern 따기 쉬움. 논문에서는 문장 N개를 논리적으로 이어서 대답을 하는 능력을 말하는 듯)

	- OOD test에서도 높은 ACC로 Generation을 보임

<br/>

- 논문에서는 2가지 Reasoning Skill을 정의

	- “level-0” reasoning skill: 문제에 주어진 모든 parameter(미지수)를 solution path에서 계산

	- “level-1” reasoning skill: question 해결을 위한 parameter(미지수)만을 solution path에서 계산

	(X =3+2, E =3+X, Y =X+2 → E가 query일때 Y =X+2 =7를 계산하지 않으면 “level-1” reasoning)

[correct solution마다 생성된 unnecessary params / operations의 수]

> **Result 3**

	- GPT2가 주로 “level-1” reasoning을 사용하여 iGSM 문제를 해결하고, OOD eval시에도 불필요한 계산을 피한다는 것을 증명.

	- 인간은 수학문제를 풀때, “backward reasoning”(question parameter로부터 반대로 어떤 parameter가 필요한지 탐색), a scratch pad to write down necessary parameters (그 paramater를 적어서 구조를 설계)하는데 LM은 단순 forwarding으로 parameter간의 dependency를 파악해 shortest solution을 구축

<br/>

## 4. Result 4-5: Discover Model’s Mental Process

- LM이 hidden state에서 인간처럼 인지적인 논리작용이 이루어지는지를 확인하기 위해 Probing Setup을 설계해서 실험

- 인간의 인지작용해서 자연스럽게 계산될 다음의 함수를 사전 지정

	- nece(A): parameter A가 답을 계산하는 데 필요한지 여부.

	- dep(A, B): 주어진 문제에서 parameter A가 parameter B에 (재귀적으로) 의존하는지 여부. (A←B)

	- known(A): parameter A가 이미 계산되었는지 여부.

	- value(A): parameter A의 값(0-22 사이의 숫자, 또는 known(A) = false인 경우 23).

	- can next(A): A가 다음 해결 문장에서 계산될 수 있는지 여부(이때 가정은 A의 parent는 미리 계산되었다고 가정).

	- nece next(A): parameter A가 can next(A)와 nece(A) 모두를 만족하는지 여부.

	⇒ shortest solution을 위해서는 solution 생성 전에 nece(A)에 대한 판단이 끝나야하며, solution 생성중에는 known(A), value(A),can next(A) .. 에 대한 판단이 완료되어야 정확히 답을 생성할 수 있음

- Probing Process & Example

		- problem 끝나면 dep(), question 끝나면 necc(), 그외에는 solution sentence 끝날때마다 진행

	- [START] parameter [END]로 parameter를 감싸고 [END] last hidden에서 linear probing

	- embedding에 rank-8 (linear) update해서 [START], [END]이 추가로 들어오는거 처리

	- LM freeze & linear classifier train으로 probing 진행

- pretrained weights에서 성능이 기인했음을 보기 위해 random initialized model에도 linear classifier학습을 진행

<br/>

<br/>

> **Result 4**

	- LM은 어떤 parameter가 계산되었고 어떤 parameter가 계산되지 않았는지(value, known) 기억할 뿐이 아니라, 어떤 parameter를 다음에 계산할 수 있는지(can next, nece next)도 거의 완벽에 가깝게 알고 문제를 풂.

	- 특히 LM이 solution path 생성전에 인간과 다르게 forwarding하면서 어떤 parameter(necc)가 필요한지 거의 완벽하게 파악하고 solution planning (NTP)에 들어가는 것을 알 수 있음

	- 대량의 학습 데이터가 존재한다면, LM에게 logically하게 작동하는 complex reasoning process도 충분히 주입할 수 있음을 시사

<br/>

<br/>

> **Result 5**

	- solution path에 없는 A에 대해서도 dep(A, B)와 can next(A)에 대해서 높은 확률로 예측함 (baseline이 없어서 아쉽긴하지만)

	- 인간의 “backward reasoning”과 달리 LM은 question이 시작되기 전에 문제 안에 존재하는 모든 의존성 그래프 dep(A, B)를 정신적으로 미리 계산 → 문제파악을 문제 읽으면서 함

		- pre-training data에서  “all-pair dependency” 를 학습하지 않는데도 (fitting the data only requires computing necessary parameters) 위의 성능을 통해 LM의 generalization을 실험적으로 증명

	- ~~어떤 문제를 풀때, “because I want to compute X, but X depends on Y and Y depends on Z, so let me compute Z first”를 명시적으로 사고하도록 LM을 만드는 것은 AGI의 목표와 동일. 본인들 실험을 통해 적어도 “because I want to compute X, but X depends on Y and Y depends on Z, so let me compute Z first”라는 명시적인 데이터로 학습하지 않아도 언어모델이 초등학교 수학수준에서는 이가 가능하다는 것을 실험적으로 보임~~

<br/>

## 5. Result 6: Explain Model’s Mistakes

- Reasoning process의 mistake를 2가지 질문을 통해 해석하고자 함.

<br/>

1. When does the model answer correctly but include unnecessary parameter?

		- unnecessary parameter를 포함하면, output acc가 현저하게 떨어짐

<br/>

1. What causes incorrect answers?

		- wrong solutions의 first wrong parameters을 probing해본 결과, nece next(A)나 can next(A)을 잘못 true라고 예측하고 solution을 생성할 경우, acc가 낮아지는 것을 확인할 수 있음

<br/>

> **Result 6**

	- LM이 범하는 reasoning error는 생성 과정에서 비롯된 무작위적인 것이 아니라, 그 hidden state computation에서 발생하는 오류에서 비롯된 체계적인 error임

	- 따라서, explainability 관점에 solution generation hidden state 확인을 통해 오류의 사전 검사가 가능함

<br/>

## 6. Result 7-8: Depth vs. Reasoning Length

- LM의 layer와 size(head hidden dim)을 늘려가면서 성능변화 추이를 확인

	- Size2이 대략 Size1의 2배

	- GPT2-ℓ-h represents an ℓ-layer, h-head, 64h-dimensional GPT2 model. Size-1 models are GPT2-4-21, GPT2-815, GPT2-12-12, GPT2-16-10, GPT2-20-9, with similar parameter counts; size-2 models are GPT2-4-30, GPT2-8-21, GPT2-12-17, GPT2-16-15, GPT2-20-13,

> **Result 7**

	- 크기만 큰 4-layer transformer, even with 1920(Size2)은 성능이 낮고, 20-layer 576-dim(Size1)보다 성능이 좋음 (hidden이 forwarding되면서 representation fine-grained?)

	- (모델 자체가 작아서 좀 당연한거 같긴한데) LM의 depth는 수학적 reasoning에 있어 결정적.

<br/>

- x축: A가 문제로 부터 떨어진 거리, y축: Layer별로 necc()결과

> **Result 8**

	-  parameter A에 대해 정신적으로 nece(A)를 계산하는 t-단계 hidden reasoning process, 다른 모든 하이퍼파라미터가 일정하다고 가정할 때, t가 클수록 더 depth한 LM이 필요함

		(Attention/Transformer을 생각할때 사실상 당연함)

	- “backward thinking process”이 명시된 solution을 학습시키면 위같은 그래프가 안나오지 않을까?라고 저자들은 이야기함

<br/>

<br/>

## 7. Conclusion

- 통제된 실험을 통해 LM이 reasoning process를 진정으로 학습할 수 있는지 (generalization), hidden reasoning processes probing을 통해 인간과 얼마나 유사한 인지작용을 하는지 검증

- 다소 pattern따기 쉬운 데이터셋임으로, 엄청나게 학습을 시키면 probing성능을 사실상 어느정도 높게 나오는게 당연하다고 보임.

- 그럼에도, LM의 generalization (OOD performance)의 실험적 증명 + LM이 token에서 어떤 정보를 학습할 수 있는지를 보여 solution을 생성한건 굉장히 고무적

- 오히려 (LLM시대에 들어오면서 더 어쩔 수 없는 Data Contamination을 인정하고) reasoning task에 한정된 LM이 아닌 General LLM에서 이 논문에서 밝힌 경향을 동일하게 보이는지도 궁금함.

<br/>

<br/>

<br/>

<br/>