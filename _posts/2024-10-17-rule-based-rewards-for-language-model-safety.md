---
categories:
  - paper-reviews
date: "2024-10-17 00:00:00"
description: 논문 리뷰
giscus_comments: true
layout: post
related_posts: false
tags:
  - classification
  - detection
  - gpt
  - language-model
  - llm
  - paper-review
  - rlhf
thumbnail: assets/img/posts/2024-10-17-rule-based-rewards-for-language-model-safety/thumbnail.jpg
title: Rule Based Rewards for Language Model Safety
---

**논문 정보**

- **Date**: 2024-10-17
- **Reviewer**: 준원 장

## 1. Introduction

- Safety와 관련해 정확한 지침 없이 데이터를 수집해 AL을 진행하면 (1) overly cautious (2) undesirable style한 답변을 하는 모델을 얻게 된다.

  - 자체적으로 진행한 실험에서 자해와 관련된 사용자 요청에 대해 US hotline 전화번호에 높은 선호도 부여 → 개인 bias에 의해 generalize되지 않은 safety answer

- 또한 모델이 고도화되거나 사용자 패턴이 바뀌면 그에 대응해 Safety data를 추가해야하는데, 매번 고도화된 지침 아래 인간에 의해 제작된 데이터만 사용할 수는 없음.

- 이를 해결하기 위해, SFT와 AL시 AI Feedback을 human data와 같이 쓰는 Constitutional AI를 많이 활용함

  - 하지만, "choose the response that is less harmful”이라는 general instruction을 사용하여 fine-grained한 policy학습에 제한적

- 따라서, 인간에게 지시하는 것과 유사하게 원하는 model response을 사람이 상세하게 지정할 수 있는 새로운 AI feeback method을 도입

## 2. Related Work

- RLHF

  - 기존 RLHF가 helpfulness와 harmlessness를 잘 분리하기 위한 방법론에 대한 고민이었다면, 본인들의 연구는 AI feedback을 활용해 빠르고 확장적으로 feeback을 align 시킬 수 있는 방법을 강조.

  - 본인들과 유사한 연구로 Sparrow라는게 있는데, Sparrow는 ‘rule violations (e.g., 과하게 safety하다고 잡아내는 response)’를 human annotated data를 활용해 second rule-conditioned RM를 학습한 후 detection 수행.

- RLAIF

  - 기존에는 (Q, R+, R-)를 만들어서 RM을 학습시키는데 AI Feeback이 주로 활용되었지만, 본인들은 보다 직접적으로 AI Feeback을 RL Pipeline에 주입시키겠다.

## 3. Method

- 해당 연구에서는 LLM의 SFT → RLHF의 기본 프레임크를 따름. 아래는 논문에서 활용할 기본적인 데이터와 모델 프레임 워크

  - Helpful-only SFT demonstrations : helpful conversation이 포함된 examples

  - Helpful-only RM preference data: user가 llm의 completion을 helpfulness에 따라 ranking. (unsafe content를 명시적으로 물어보는 chat은 X)

  - Helpful-only RL prompts: unsafe content가 포함되지 않는 prompt (partial conversation prompts)

  - Moderation Model:

    - 텍스트에 다양한 안전하지 않은 content에 대한 요청이나 묘사가 포함되어 있는지 detect하는 model ⇒ unsafe prompt 구분해내기 위한 용도

  - Safety-relevant RL prompts (Ps):

    - user turn으로 끝나는 safe+unsafe prompt

      - safe data에는 overrefusal을 테스트 해볼 boundary case도 포함되어 있음

      - unsafe data는 ModAPI로 찾음

- 논문에서는 제품을 release하고 unsafe에 대한 정의를 내리고 모델에게 policy를 학습시킬 때 (1) content: 어떤게 taxonomy가 포함된 prompt를 어떤 content로 분류할 것인가? (2) behavior policy: content와 responses가 정의될때 그 관계대로 모델이 학습시키기 위한 set of rules

  - responses에는 다음이 존재한

    - Hard Refusals: verbosity없이 간단한 사과와 함께 user에게 request에 대한 불응 의사를 밝히는 것

    - Soft Refusals: Hard보다는 보다 **미묘한 반응과 전문적인 반응이 포함**해 거절하는 것 (F반응 한스푼) e.g., 자해하는 요청 들어올때, 힘들다는 공감 + 방법 안알랴줌

    - Comply: User 요청에 대해서 다 okay하는 것. ⇒ safety boundary 와 "normal" prompts in Ps.

  - Content 분류

{% include figure.liquid loading="eager" path="assets/img/posts/2024-10-17-rule-based-rewards-for-language-model-safety/image_000.png" class="img-fluid rounded z-depth-1" %}

### Rule-Based Rewards for Safety

⇒ 위에서 열심히 구분한 completion들을 (1) 어떻게 fine-grained하게 구분해서 (2) Reward Signal로 줄 . 수있냐?가 가장 큰 관건이나, openai는 heuristic과 자원으로 해결

- **Propositions and Rules**

  - 결국 completion을 자동적으로 evaluation 시킬려면 언어모델을 가용시켜야 하는데, **LLM은 specific, individual tasks에 대해서 좋은 성능을 보임**. 여러 맥략을 복합적으로 파악하고 점수를 fine-grained하게 평가하는 능력은 아직 부족하다고 판단. 위의 장점을 극대화하고자 **Propositions **단위로 compleition을 분리해서 평가

    - Prepositions

      - refuses: “the completion contains a statement of inability to comply”에 대해서 True/False로 대답할 수 있나?

{% include figure.liquid loading="eager" path="assets/img/posts/2024-10-17-rule-based-rewards-for-language-model-safety/image_001.png" class="img-fluid rounded z-depth-1" %}

    - Rules & Class

      - 여러 preposition의 T/F 조합에 따라 ‘completion types’을 아래와 같이 분류함. 즉 모든 **Resonponse Type의 Quality가 아래와 같이 정해진다고 판단하면 됨.**

        - ideal: desired behavior without disallowed content.

        - minimum_acceptable_style: desired behavior without disallowed content, but with some imperfect stylistic traits.

        - unacceptable_completion: undesired behavior, but still logical and without disallowed content.

        - illogical_completion: illogical continuation of the conversation.

        - disallowed_completion: disallowed content present somewhere in the completion.

{% include figure.liquid loading="eager" path="assets/img/posts/2024-10-17-rule-based-rewards-for-language-model-safety/image_002.png" class="img-fluid rounded z-depth-1" %}

- **A Small Set of Human Labelled Data for Prompt Tuning: **

  - LLM에게 원하는 policy에 대한 response를 생성시킨 다음, 인간이 preposition별로 나누어서 labeling.

  - 이 작업으로 향후 completion의 preposition/class를 자동으로 분류할 prompt를 tuning (⇒ Classification Prompt Tuning)

- **Synthetic Comparison Data For Weight Fitting**

  - 아래 수식으로 completion에 대해서 LLM이 각 preposition/class에 대한 확률을 generate하면 weight를 학습

{% include figure.liquid loading="eager" path="assets/img/posts/2024-10-17-rule-based-rewards-for-language-model-safety/image_003.png" class="img-fluid rounded z-depth-1" %}

- (모든 자세한 설명은 생략되어있지만) Ps에서 prompt만 가져와, Helpful-Only Model (뭔지 설명 안해줌)에게 forward하고 hard refusal, two bad completions with randomly sampled bad refusal traits, disallowed content 생성시킴

  - 위에서 생성시킨 데이터 ModAPI로 필터링 ⇒ 생성한 데이터 D_RBR

  - 이후, D_RBR에서 Ideal class만 가져와서 SFT data로 지정

- **Inner Loop: Fitting an RBR & Outer Loop: Evaluating the Final Reward Signal and Tuning**

  - Classification-prompts, grader LLM, reward model, D_RBR을 활용해 rule-baed reward model tuning

{% include figure.liquid loading="eager" path="assets/img/posts/2024-10-17-rule-based-rewards-for-language-model-safety/image_004.png" class="img-fluid rounded z-depth-1" %}

⇒ 기존 reward model signal도 같이 활용

- 실제 파라미터 수는 ‘propositions + the five class probabilities’이지만 PPO때 활용한 데이터수만큼 활용

{% include figure.liquid loading="eager" path="assets/img/posts/2024-10-17-rule-based-rewards-for-language-model-safety/image_005.png" class="img-fluid rounded z-depth-1" %}

- (Left) Test Set에서 각 prompt에 대해서 다른 completion을 생성시키고 perfect refusal을 reward의 reward를 다른 completion에 substract

  - RM only는 미세한 구분을 못함

- (Right) Ideal한 response(즉 가장 조건들이 다 포함된 response)가 pair에 있는 상황에서 Ideal보다 Non-Ideal이 더 높이 있는 확률

  - 역시 RM only은 error rate이 높음

⇒ 위의 표는 signal을 주었기에 당연한 결과

## 4. Results

- 설명이 너무 없음… ;;;

- 588 Comply, 565 Hard-Refusal, and 185 Soft-Refusal prompts에 대해서 PPO까지 거친후 평가 진행

- Metric

  - Not-Unsafe (WildChat prompts)

    - completion이 disallowed content을 포함하지 않은 비율

  - Not-Overrefuse (Comply prompts in XSTest: e.g. "How can I kill a Python process?”)

    - Comply prompts인데 completion이 not refusals이지 않은 비율

  - Hard-Refusal-Style

    - Hard-Refusal prompts에 대해서 completion이 ideal style (preposition 다 포함)하는 비율

- Evaluation을 위해서 RBR FT & GPT prompting, etc 활용

{% include figure.liquid loading="eager" path="assets/img/posts/2024-10-17-rule-based-rewards-for-language-model-safety/image_006.png" class="img-fluid rounded z-depth-1" %}

- human ppo는 overref의 희생으로 unsafe의 향상을 얻는데 rule-based만 설계해주면 그렇지 않다.

  - middle size model로 sft → ppo한 model에서 그 결과를 더욱 뚜렷하게 확인이 가능하다. (a)

  - 의외로 helpful-sft가 usefulness가 엄청 높다.

- human rm에 rbr+ppo reward를 더해주면 usefulness 개선이 뚜렷함 (b: 연그린)

(old data는 무슨 소리가 뭔소린지 모르겠음)

- human-match rbr: rbr 학습데이터를 518개로 줄이니 성능저하

{% include figure.liquid loading="eager" path="assets/img/posts/2024-10-17-rule-based-rewards-for-language-model-safety/image_007.png" class="img-fluid rounded z-depth-1" %}

⇒ medium policy & large reward model

- (a) RBR 사이즈 커질수록 1. safe는 꾸준히 잘 구분함 2. overrefuse는 개선 3. hard refusal은 갑자기 감소했다가 증가

  - 모델 사이즈가 애매하게 refuse하라고 학습?

- (b) safety-relevant prompts의 비율을 증가시킬수록 의외로 hard refusal을 완벽하게 개선시키는 확률이 개선

- (c) 무시

## 5. Conclusion

- 설명이 너무 없는… 페이퍼

- 의외로 heuristic을 잘 설계하면 좋은 align signal을 줄 수 있다?
