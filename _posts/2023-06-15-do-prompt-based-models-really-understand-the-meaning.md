---
categories:
  - paper-reviews
date: "2023-06-15 00:00:00"
description: 논문 리뷰 - Instruction Tuning, ICL, Prompt Tuning 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
  - bert
  - fine-tuning
  - gpt
  - icl
  - instruction tuning
  - language-model
  - nlp
  - paper-review
  - prompt tuning
thumbnail: assets/img/posts/2023-06-15-do-prompt-based-models-really-understand-the-meaning/thumbnail.jpg
title: Do Prompt-Based Models Really Understand the Meaning of Their Prompts?
---

**논문 정보**

- **Date**: 2023-06-15
- **Reviewer**: 준원 장
- **Property**: Instruction Tuning, ICL, Prompt Tuning

### Introduction

1. 이라크에서는 아직 대량의 살상 무기가 발견되지 않았다.

1. 이라크에서 대량의 살상 무기가 발견되었다.

모델에게 1과 2가 동치인지 아닌지 판별하는 능력을 갖게 하기 위해서는 다양한 데이터셋이 필요하다.

(PLM → Transfer Learning 관점)

하지만**_ ‘이라크에서는 아직 대량의 살상 무기가 발견되지 않았다.’라는 문장이 주어졌을때, ‘이라크에서 대량의 살상 무기가 발견되었다.’라는 문장은 옳은 문장인가?’ _**라는 식으로 질문을 바꾸어 버리면 인간은 한번에 빠르게 학습이 가능하다. (Motivation of Instruct Fine-Tuning)

→ 이렇게 추가적인 Prompt가 Input에 결합되면 모델이 Input으로부터 유의미한 task instruction을 해석할 수 있기 때문에 빠르고 안정적인 학습이 가능하다고 알려져있다.

→ 인간이 직접 쓴 Prompt가 자동으로 찾거나 만든 Prompt에 비해서 성능 향상에 도움이 된다고 알려져 있고 (report that Schick and Schütze (2021b)’s manually written prompts still on average outperform the automatically searched prompts across a range of SuperGLUE tasks (Wang et al., 2019)) 전문가에 의해서 작성된 Prompt에 의해서 유의미한 instruction을 작동시킬 수 있다고 알려져 있다.

하지만, 본 연구는 위의 성능향상이 few-shot 및 zero-shot 상황에서 230M-175B까지의 다양한 모델들과 instruction tuning된 모델들이 과연 (사람처럼) prompt 내의 instruction 제대로 해석했기 때문일지에 대한 의문을 제기한다.

### Prompt Tuning & Prompting

앞으로 언급할 prompt tuning 및 prompting은 아래 3개 중 하나를 의미함

- **Discrete Prompts: \***{sent} In summary, the restaurant is [prediction]\*

- **Priming: ICL**

- **Continuous Prompts(prompt tuning, p-tuning)**: In addition to discrete prompts, some models use continuous prompts that are generated using a separate language model. These continuous prompts are designed to be more flexible and can be tailored to specific tasks or domains. However, it is unclear whether these continuous prompts are better at conveying task-specific information than discrete prompts.

### Experiment Setup

**Problem Situation**

- Few shot 상황에서 Model이 Prompt내 Instruction의 의미를 얼마나 잘 이해하는지 실험

- k-shot = {0, 4, 8, 16, 32, 64, 128, 256}

- Prompt내에 있는 instruction의 범위를 ‘description of task’로 좁힘

**Baseline Setup**

- **Weak Baseline**

- **Instruction-Tuned Model**

- **ICL**

**Data**

- NLI (T0가 instruct tuning때 안봐서)

- Label Space는 Yes/No로 통일하고 실험 진행

**4개 Random Seed**

### Templates

논문의 목적이 모델이 Prompt내 Instruction의 Semantic을 제대로 이해했냐를 파악하기 위함이기에 아래 5개 종류의 Template를 제작함

- Instructive: how we would describe the NLI task to a human who has never seen this task before. (처음 NLI 문제를 보는 인간에게 설명하듯이 기술하기)

**→ Prompt(Instruction) Tuning를 통해 모델이 인간이 Instruction을 보고 unseen task를 풀때와 같은 동작을 하기를 기대한다면 Instructive Prompt를 보았을때랑 아래 Prompt를 보았을 때 성능 차이가 뚜렸해야함**

- Misleading-Moderate (적당히 속이기): instruct the models to perform a task related or tangential to NLI such that, if the model were to perform the task as explicitly instructed, it would perform poorly on NLI in general. (NLI랑 비슷한 Task를 수행하도록 기술함. 기술한 그대로 수행하면 NLI 성능은 좋지 않을 수 있음)

- Misleading-Extreme: instruct the models to perform a task unrelated to NLI. (NLI랑 무관)

- Irrelevant: concatenate the premise, a sentence unrelated to any NLP task, and the hypothesis. (무관한 문장을 premise랑 hypo사이에 끼워넣기)

- Null: concatenate the premise and the hypothesis without any additional text. (아무 정보도 넣지 않기)

{% include figure.liquid loading="eager" path="assets/img/posts/2023-06-15-do-prompt-based-models-really-understand-the-meaning/image_000.png" class="img-fluid rounded z-depth-1" %}

### Results

- **T0: Instructive Vs Irrelevant Template **

- **Misleading Template**

- **Null Template**

{% include figure.liquid loading="eager" path="assets/img/posts/2023-06-15-do-prompt-based-models-really-understand-the-meaning/image_001.png" class="img-fluid rounded z-depth-1" %}

→ 일반적으로 제일 성능이 안좋으나 특정 order template의 경우 32 SHOT에서 성능 좋은 경우 있음 (뭐.. 이럴 수도 있지..)

- **Zero shot**

→ Zero-shot에서 random보다 marginal하게 성능을 보인 model은 T0밖에 없어서 T0로 실험을 진행

→ 3B모델은 Prompt 종류가 어떻든 간에 비슷한 수준의 performance를 보임

→ 11B 모델은 통계적으로 유의미한 performance 차이를 보이지 못함. 11B++ 모델부터 유의미한 차이를 보이기 시작함 (instructicve prompt에서 성능이 제일 좋지만) (그럼에도 misleading-extreme prompt에 여전히 너무 잘 반응함)

**→ GPT3도 비슷한 양상 보임 (instruct tuning은 안했지만 사이즈 키운다고 해서 해결되는 문제는 아님)**

### Label Space

→ Label Space도 임의로 바꿔서 모델이 Label에 sensitive하게 반응하는지 실험함

- Yes-no: Model is expected to predict the word “yes” for entailment and “no” for nonentailment. (기존 setting)

- Yes-no-like: Semantically equivalent to yesno but using superficially different words, e.g., “true”/“false”, “positive”/“negative”. (유의어)

- Arbitrary: Model is expected to predict arbitrary words that have no semantic relation to the entailment task, e.g., “cat” for entailment, “dog” for non-entailment. (임의 단어로 mapping)

- Reversed: Model is expected to predict the opposite of the (intuitive) yes-no and yes-nolike labels, e.g., (reverse)

**Results**

{% include figure.liquid loading="eager" path="assets/img/posts/2023-06-15-do-prompt-based-models-really-understand-the-meaning/image_002.png" class="img-fluid rounded z-depth-1" %}

→ ALBERT, T0 둘다 Best Illustrastive template로 실험했을때 Yes-No > Arbitrary.Reversed

- 추가 실험도 진행

1. **An irrelevant or misleading template + yes-no targets**, e.g., {premise} Does the paragraph start with "the"? [yes/no] {hypothesis} :

1. **An instructive template + arbitrary targets**, e.g., {premise} Based on the previous passage, is it true that "{hypothesis}"? [cat/dog]

{% include figure.liquid loading="eager" path="assets/img/posts/2023-06-15-do-prompt-based-models-really-understand-the-meaning/image_003.png" class="img-fluid rounded z-depth-1" %}

→ **An irrelevant or misleading template + yes-no targets의 성능이 더 높음. 인간이라면 몇개 shot만으로 Cat → Entatlilment / Dog → Not-Entailmenet라는 것을 빨리 Mapping할텐데 모델은 그렇지 못하고 있음. 오히려 잘못된 instruction을 전혀 해석하지 못하고 있음을 보여주고 있음.**

### Conclusion

→ Model이 instructive and irrelevant templates, misleading templates에 따라서 performance 차이가 다르게 나야하는데 그렇지 않음 (인간처럼 instruction을 해석하지는 않음)

→ 반면 Target word에 따른 performance 차이는 consensus 존재

**Additional Interpretation**

- **Lack of Competence (너무 어려운 Task)**

- **Lack of Compliance (Instruction 무시)**
