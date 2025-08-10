---
categories:
- paper-reviews
date: '2024-01-23 00:00:00'
description: 논문 리뷰
giscus_comments: true
layout: post
related_posts: false
tags:
- attention
- classification
- gpt
- language-model
- paper-review
thumbnail: assets/img/posts/2024-01-23-overthinking-the-truth-understanding-how-language-models-process/thumbnail.jpg
title: 'OVERTHINKING THE TRUTH: UNDERSTANDING HOW LANGUAGE MODELS PROCESS FALSE DEMONSTRATIONS'
---

**논문 정보**
- **Date**: 2024-01-23
- **Reviewer**: hyowon Cho

# Introduction

최근의 언어모델들의 핵심은 context-following이 가능하다는 것이다. 때때로 그들은 finetuning 없이도 그에 준하는 성능을 보인다. 이 때문에, 최신 연구들은 context가 성능에 미치는 영향을 연구하고 더 발달된 프롬프트를 만들기 위한 연구 혹은 그것에 대한 Internal mechanism에 집중하고 있다.

하지만, context-following이 가능하는 말은 즉,  incorrect, toxic, unsafe한 모델 출력을 만들어낸다는 말과도 동일하다. 즉, user error의 패턴을 받아들여 그것을 재생산하는 문제가 있다는 것이다. 다른 말로, context-following learns too much. 의도한 속성 외에도 다른 것까지 모조리 학습해버리는 문제가 있다.

오늘 소개할 논문에서는 모델이 이미 zero-shot에서 정답을 알고 있지만 context에 의해 잘못된 답을 뱉는 경우를 좀 더 파고 든다.

1. how incorrect imitations emerge over the course of the model’s processing

1. look for the model components that cause them.

전체 결과를 요약하면 다음과 같다:

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-23-overthinking-the-truth-understanding-how-language-models-process/image_000.png" class="img-fluid rounded z-depth-1" %}

1. 언어모델은 분명 context를 imitate하고

1. demonstration을 처리하는 critical layer가 존재하며, 이는 일반적으로 후반부 layer에 위치

1. 이것에 기여하는 특정 attention head들이 존재한다. 이 head들은 일반적으로 critical layer의 뒤에 몰려있다.

# PRELIMINARIES: FEW-SHOT LEARNING WITH FALSE DEMONSTRATIONS

- Task: few-shot learning for classification tasks

- Datasets

  - SST-2

  - Poem Sentiment

  - Financial Phrasebank

  - Ethos

  - TweetEval-Hate, -Atheism, and -Feminist

  - Medical Question Pairs

  - MRPC

  - SICK

  - RTE

  - AGNews

  - TREC

  - DBpedia

  - Unnatural: demonstrations are of the form“[object]: [label]” and the labels are “plant/vegetable”, “sport”, and “animal”.

- Models

  - GPT-J-6B

  - GPT2-XL-1.5B

  - GPT-NeoX-20B

  - GPT-J-6B (intruction tuned)

  - GPT2-XL-1.5B (intructoin tuned)

  - GPT-NeoX-20B (intructoin tuned)

  - Pythia - 410M, 2.8B, 6.9B, and 12B

  - Llama2-7B

- Evaluation metrics.

  - calibrated classification accuracy

    - we measure how often the correct label has a higher probability than its median probability over the dataset

## FALSE DEMONSTRATION LABELS DECREASE ACCURACY

첫 번째로 보장한 것은, demonstratoin label이 모두 맞을 경우와, 모두 틀린 경우의 성능 차이이다. 잘못된 레이블을 매핑할 때, 같은 클래스의 데이터는 모두 같은 레이블을 가지도록 한다. 즉, 레이블만 permute됨으로, 저자들은 이 세팅을  permuted labels setting이라고 부른다.

결과는 다음과 같다:

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-23-overthinking-the-truth-understanding-how-language-models-process/image_001.png" class="img-fluid rounded z-depth-1" %}

왼쪽의 figure를 통해 알 수 있듯, 성능 차이가 커진다. 하지만 이는 모델이 random label을 선택함으로써 이루어졌을 가능성도 존재함으로, 어떤 레이블을 선택했는가를 확인한다 (오른쪽). 보다시피, demonstration을 점차 잘 따라가고 있음을 확인할 수 있다.

## RANDOM AND PARTIALLY CORRECT LABELS LEAD TO LOWER ACCURACY THAN CORRECT LABELS

다른 세팅들에 대한 실험도 추가적으로 진행한다.

1. half correct labels half permuted labels --> acc gap: 0.12

1. random labels --> acc gap: 0.15

1. permuted labels --> acc gap: 0.28

- -> 생각: 랜덤일때는 오히려 학습을 거부하고 본래에 stick? 랜덤하게 하다가 맞춰버린건지, 오류 결과를 봤으면 좋았을텐데 없다ㅠㅠ

# ZEROING LATER LAYERS IMPROVES ACCURACY

false context-following에 대해 더 잘 알아보기 위해, 저자들은 model prediction을 intermediate layer에서 직접적으로 decode해본다.

이 섹션에서는 크게 두 가지 finding이 있다.

1. the model’s accuracies given correct and incorrect demonstrations sharply diverge at
the same “critical layers” across tasks

1. on incorrect demonstrations the model “overthinks” – it performs better midway through processing

## Intermediate layer predictions: the logit lens.

먼저, 각 layer에서 decoding은 logit lens 방법을 이용해 수행한다.

당연히, 중간 레이어를 거쳐 나온 distribution은 앞선 L개의 레이어를 거친 뒤의 모델 prediction일 것이다.

즉, 본래 . For a sequence of tokens t1, ..., tn \in V , the logits of the full
model’s predictive distribution p(tn+1 | t1, ..., tn) are given by:
[logit_1, ..., logit_{|V|}] = W_U . LayerNorm(h^{(n)}_L).

여기서 h_L을 intermediate hidden state인 h_l^{(n)}으로 바꿨다고 생각하면 된다.

## Overall Result

average accuracy of 3 of our 11 models over the fourteen non-toy datasets

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-23-overthinking-the-truth-understanding-how-language-models-process/image_002.png" class="img-fluid rounded z-depth-1" %}

## Accurate and incorrect demonstrations sharply diverge at “critical layers”

올바른 demonstration을 주었을 때, 정확도는 layer가 깊어질수록 높아졌다.

놀랍게도 permuted이나 random에서도 early에서는 비슷한 양상을 보였지만, 후반부에 갈수록 양상이 변화하며 정확도가 떨어졌다. 이 트렌드는 다양한 데이터셋에서 공통적으로 나타났다.

즉, 모든 실험에서 올바른 그리고 올바르지 않은 프롬프트에 대한 정확도는 모두 동일한 레이어 구간에서 나타났다. 저자들은 이를 critical layer라고 부른다.

예를 들어, GPT-J에서는 13-14, pythia는 7-8, llama는 15-17가 해당 레이어이다.

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-23-overthinking-the-truth-understanding-how-language-models-process/image_003.png" class="img-fluid rounded z-depth-1" %}

## Early-exiting improves classification performance given incorrect demonstrations.

올바르지 않은 demonstration을 주었을 때, 저자들은 overthinking을 발견한다: decoding from earlier layers performs better than decoding from the final layer.

위의 figure에서 확인할 수 있듯, 16을 넘어가는 순간부터는 full model을 계속해서 이긴다.

- -> 개인적으로는 되려 잘못된 정보를 지속적으로 넣었는데 early stage에서 acc이 오르는게 더 신기한데! 다들 저자가 이야기한게 더 놀라운 사실인지,, 오히려 overthinking이 아니라, counterfactual한걸 잘 받아들일 가능성을 보여줬다고도 할 수 있지 않나 싶은데! 어떻게 생각하시나요?

## Ablating attention heads only improves accuracy further

올바른 정보와 잘못된 정보를 보여주는 demonstration이 critical layer에서부터 차이가 나기 시작한다는 것은, 해당 레이어 이후에서야 demonstration에 대한 정보가 제대로 인코딩된다고도 해석할 수 있다. 즉,  late attention layers가 overthinking을 유발한다는 것이다.

이를 확인하기 위해, 뒤의 Layer에서 attention head들을 zero-out 해본다 (MLP는 건들지 않는다).

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-23-overthinking-the-truth-understanding-how-language-models-process/image_004.png" class="img-fluid rounded z-depth-1" %}

표에서 확인할 수 있듯,

- ablating just the attention heads has a similar effect to ablating the entire layer

- ablating just MLPs has a much smaller effect

즉, overthinking은 late attention head로부터 발생한다는 것이다!

# ZOOMING INTO ATTENTION HEADS

가설은 다음과 같다:
there are false induction heads that attend to false labels in similar past demonstrations, and make the model more likely to output them.

이를 formal하게 표현하기 위해, 저자들은 attention head가 false induction head가 되게 하는 3가지 properties를 언급한다.

1. label-attending

  - concentrate its attention on labels in the previous demonstrations

1. class-sensitive

  - meaning it attends specifically to labels that follow inputs from the same class

  - (e.g “tomato”, “garlic” and “kale” in Figure 5).

1. label-promoting

  - meaning it increases the probability of the labels it attends to.

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-23-overthinking-the-truth-understanding-how-language-models-process/image_005.png" class="img-fluid rounded z-depth-1" %}

false induction head를 판별하는 공식  prefix-matching score는 다음과 같다:

PM^h = \sum
^n_{i=1}Att^h(x, yi) · 1_{class(x)=class(x_i)} −
\frac{1}{\#labels − 1}
\sum^n_{i=1}Att^h
(x, y_i) · 1_{class(x)\neq class(x_i)}

첫번째 텀에서 head가 class x의 label에 잘 attend하는가를 포착하고, 그렇지 않으면 작아지도록 뒤의 텀에서 값을 줄인다.

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-23-overthinking-the-truth-understanding-how-language-models-process/image_006.png" class="img-fluid rounded z-depth-1" %}

보다시피, early layer에서는 점수가 낮게 유지되다가 critical layer를 지나면 증가하기 시작한다.

## Ablating false induction heads

가장 높은 점수를 가지는 attention head를 zeroing했을 때, 성능을 크게 증가하는 것을 알 수 있었다. 랜덤한 head를 ablate했을 때는 오히려 성능이 낮아지는 양상을 보였다.

{% include figure.liquid loading="eager" path="assets/img/posts/2024-01-23-overthinking-the-truth-understanding-how-language-models-process/image_007.png" class="img-fluid rounded z-depth-1" %}

## Verifying that our heads are label-promoting.

 여기서는 label promoting (i.e. that they increase the probability of the false labels they attend to)한지를 확인한다.

이를 위해 각 head들에게 logit lens를 적용해본다. 이후, 정답 레이블과 permuted 레이블의 차를 false label promoting score로 지정한다. 높은 숫자는 permuted label의 확률이 높아졌다는 뜻이다.

위에 언급한 5 heads: average false label promoting score of 6.5를 기록했다. 즉, 그들은 정답 레이블에 비해  permuted label logit을 6.5나 더 증가시킨 것이다.

반면, 랜덤하게 레드들을 추출했을 때는  average score of −0.04, with a standard deviation of 0.41를 기록했다.

요약하면, later layer에 소수의 false induction heads가 있으며, 그들은 false labels in past demonstrations에 attend, and increasing their probability함으로써 잘못된 컨텍스트를 따르는데 기여한다.
