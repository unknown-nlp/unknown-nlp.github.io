---
categories:
- paper-reviews
date: '2024-02-13 00:00:00'
description: 논문 리뷰 - Editing, Evaluation Metric 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- editing
- evaluation metric
- gpt
- language-model
- llm
- paper-review
thumbnail: assets/img/posts/2024-02-13-can-sensitive-information-be-deleted-from-llms-objectives/thumbnail.jpg
title: CAN SENSITIVE INFORMATION BE DELETED FROM LLMS? OBJECTIVES FOR DEFENDING AGAINST
  EXTRACTION ATTACKS
---

**논문 정보**
- **Date**: 2024-02-13
- **Reviewer**: hyowon Cho
- **Property**: Editing, Evaluation Metric

# INTRODUCTION

언어 모델이 사실 정보를 가지고 있다는 것은 이미 자명하며, 그에 따라서 personal information을 기억하거나 혹은 out-dated 지식들을 여전히 사실이라고 여길 위험에 대한 경각심이 늘어나고 있다. 모델들은 또한 사람들에게 직접적으로 psychological harm을 가할 가능성이 있는 것으로 드러났는데, 이러한 유형의 사실 혹은 믿음을 sensitive information이라고 부른다.

저자들은 이러한 분야에 가장 근본적인 질문 두 가지를 던진다.

1. How can we “delete” specific sensitive information from language models when we do not want models to know or express this information?

1. How do we test whether that specific information was successfully deleted?

- > 특히나, 2번째의 질문이 knowledge editing이나 unlearning 분야의 고질적인 한계점으로 계속 지적되고 있는 만큼 어떠한 연구를 할지 흥미를 유발!

### Scrubbing Sensitive Info From LLM Outputs.

최근, sensitive information을 LLM output에서 지우기 위한 가장 지배적인 방법론은 강화학습을 사용하는 것이다. 가장 간단한 방법론으로는, training data에서 민감한 정보들을 필터링하는 것이라고 할 수 있겠다. 하지만, 여전히 이러한 필터링 이외에도 잘못된 정보를 뱉는 것으로 보아, 많은 한계가 있는 것이 사실이다.

### Model Editing for Information Deletion

이러한 이유로, 저자들은 이상적인 방법론은 model weight로부터 직접적으로 정보를 지울 수 있어야한다고 주장하며, 추가적으로 이러한 방식만이 whitebox extraction attack을 방지할 수 있다고 말한다.

### Whitebox Attacks.

저자들은 Whitebox Attacks으로 모델의 interpretability에 관한 연구들을 참조한다. *즉, 지난번에 다뤘던 logit lens를 이용한다! *intermediate hidden states를 이용하여 보다 정밀하게 모델이 특정 지식을 모든 weight에서 잊었는지 확인할 수 있다.

또한 기존의 방법론은 보통 final layer의 단에서 수정을 하는데, logit lens를 활용하기 때문에 해당 model editing 방법론을 모든 layer 단에서 구현한다. 이를 통해 attack success rate를 38%에서 2.4%까지 내렸다.

하지만 저자들은 여전히 이러한 공격 방식이 충분하지 않다고 이야기하며 정말 모델이 특정 지식을 잊었는지 판단하기 위한 다른 attack을 제안한다.

### Blackbox Attacks.

해당 공격은 automated input rephrasing attack이다.

비록 model editing 방법론이 대부분의 prompt에 대한 paraphrases에 대해서 잘 반응하지만, 여전히 paramrphasing model로부터 만들어진 더 많은 것들에 대해서는 반응하지 못한다는 것을 확인했다.

# RELATED WORK

- Evidence That LLMs Memorize Sensitive Information.

- Attacking LLMs for Sensitive Information

- Machine Unlearning and Model Editing.

# PROBLEM STATEMENT

이 연구에서의 목표는 "single undesired fact를 모델에서부터 제거하는 것"이다. 이를 위해서는 이것이 제대로 제거되었는지 아닌지 평가할 수 있는 metric이 필요하다.

## THREAT MODEL

### Adversary’s Objective:

민감한 정보에 대한 질문과 답을 담은  pair (Q, A)에서 답을 inference 중 낸 경우. 이때, A가 Candidate set C에 속하느냐로 unlearning 성능을 측정하며, |C| = B를 attack budget이라 칭한다.

1. Password Attempts:

1. Parallel Pursuit

1. Verification by Data Owner

### Attack Success Metric.

$AttackSuccess@B(M)$ = prediction이 C안에 속하는 경우.

- Adversary’s Capabilities

## METRICS FOR INFORMATION DELETION

두 가지를 고려한다.

1. remove specific information

1. avoiding damaging the model’s knowledge in general

arg\ min _{M^∗}AttackSuccess@B(M^∗) + λDamage(M^∗,M)

M^∗은 edited model. M은 수정 전 모델.

Model Damage를 판단하기 위한 metric으로는 두 가지를 측정한다.

1. Random ∆-Acc

1. Neighborhood ∆-Acc

추가적으로 Rewrite Score 점수도 제공한다.

\frac{p(y|x;M^∗) − p(y|x;M)}{1 − p(y|x;M)}

즉, target에 대해서 얼마나 바뀌었는지! 1이 된다면 new target 확률이 극대화, 0이 되면 반대. 이 점수를 극대화가 아닌 minimizing이 목적이 되게 되면 다음과 같이 수식이 변화한다.

1 − p(y|x;M∗)/p(y|x;M)

즉, target prob가 0에 가까워질수록 잘 잊었다!

# ATTACK METHODS

## WHITEBOX LOGIT LENS ATTACKS

- Head Projection Attack:

- Probability Delta Attack

## BLACKBOX ATTACK: INPUT REPHRASING

단순하게, rephrasing model을 만들어서 Model editing을 할 때 사용했던 데이터에 대한 변형을 만들고, 이 전부를 이용해서 공격을 하는 경우!

- > 단순하지만 아직 아무도 안했다는 점이 포인트!

5개의 paraphrases 생성.


dipper-paraphraser-xxl (Krishna et al., 2023) model 사용.

# DEFENSE METHODS

기존에 존재하는 방법론들과 추가된 denfense 방법들을 소개한다.

1. The Empty Response Defense(Ouyang et al.,2022)

1. Fact Erasure (Hase et al., 2023).

1. Error Injection (De Cao et al., 2021).

1. Head Projection Defense (new!)

1. Max-Entropy Defense. (new!)

1. Input Rephrasing Defense.(new!)

# EXPERIMENT

## SETUP

- Models

- Datasets

- Model Editing Methods.

## RESULT

### CAN WE EXTRACT A “DELETED” ANSWER FROM A LANGUAGE MODEL?

세팅: gpt-j, counterfact dataset, ROME editing with empty respose objectvie, Rewrite Score is high for all methods (90%+), with low Random ∆-Acc scores (<1%)

결과를 통해서 확인할 수 있듯, B=20을 이용했을 때, attack success ratesms 38%를 넘어간다. 즉, 제대로 지워지지 않았음을 의미!

whitebox뿐만 아니라, blackbox에서도 29%의 성공을 보였다.

B=1일때도 사실, delat atttack에서 18%의 공격 성공률을 보였다.

흥미롭게도 B=20을 넘어가면, 모든 방법론들은 saturate.

### HOW TO DEFEND AGAINST INFORMATION EXTRACTION ATTACKS

결과를 해석해보면 다음과 같다:

1. whitebox and blackbox attacks are all frequently successful at extracting “deleted” facts. -> 다른 말로는 여전히 정보들이 지워지지 않았다.

1. MEMIT with the Empty Response defense is successfully attacked by our Head Projection attack 89% of the time on zsRE

1. Head Projection and Max-Entropy defenses are the strongest defenses against whitebox attacks.

1. Input Rephrasing defense does not reduce the blackbox attack success.

1. MEMIT is generally higher than against ROME,
