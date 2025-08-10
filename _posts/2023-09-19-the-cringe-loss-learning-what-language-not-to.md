---
categories:
- paper-reviews
date: '2023-09-19 00:00:00'
description: 논문 리뷰 - LM 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- language-model
- lm
- neural
- paper-review
- transformer
thumbnail: assets/img/posts/2023-09-19-the-cringe-loss-learning-what-language-not-to/thumbnail.jpg
title: 'The CRINGE Loss: Learning what language not to model'
---

**논문 정보**
- **Date**: 2023-09-19
- **Reviewer**: 건우 김
- **Property**: LM

# Introdution

LM은 아직도 toxicicty, bias, lack of coherence, fail to user’s coherence와 같은 문제들이 있음. 이런 문제들을 해결하기 위해 objective function에 failure cases에 대한 정보를 주입하는 식으로 training objective를 설계하는 여러 시도들이 있음. 

본 연구에서는 일반적으로 자주 사용되는 *positive example sequences*와 *negative example sequences (model should not generate) *를 모두 포함하는 training data를 통해 해당 문제를 탐구함. 

다음 training data에 학습을 시키는 새로운 learning method, **CRINGE loss,**를 소개함.

Positive와 negative training data를 갖는 3가지 task에 실험을 한 결과 existing methods보다 효과적인 성능을 보여줌

# Related works

### Collecting negative examples

최근에는 positive examples(e.g. human written text, websites etc.)을 수집하는 것 뿐만 아니라, 모델이 특정 ‘response’(e.g. contradictory, toxic, unhelpful responses)를 생성하지 않는 식으로 학습을 시키기 위해 negative examples을 수집하는 것에 대한 연구도 많이 진행됨. 

PPO에서 사용되는 human preference에 대한 ranked examples들도 있지만, 본 연구에서는 positive / negative examples만 고려해서 연구를 진행함.

### Training with negative examples

1. Negative examples을 활용해서 LM을 학습하는 연구들도 다수 존재함.

**(Neural Text ****De****Geneartion with Unlikelihood Training, ICLR 2020)**

→ unlikelihood training을 소개하며, negative token들에 대한 probability를 낮추는 식으로 objective function을 새로 제안함. negative candidates들에 대해 모델의 probability를 감소시키는 아이디어. 

**Token-level unlikelihood objective**

{% include figure.liquid loading="eager" path="assets/img/posts/2023-09-19-the-cringe-loss-learning-what-language-not-to/image_000.png" class="img-fluid rounded z-depth-1" %}

하지만, Token-level unlikelihood objective는 token 단위로 penalty를 줄 수 있는 장점이 있지만, training sequence & generated sequence 간의 **distribution mismatch**가 생기는 이슈 존재

**Sequence-level unlikelihood objective**

**(A Simple Contrastive Learning Objective for Alleviating Neural Text Degeneration, arxiv 2022)**

→ Text degeneration을 방지하기 위해 contrastive learning을 사용함. 앞선 M context tokens (negative candidates)들에 대해 positive label에 contrast를 가하는 것은 undesired token들이 생성되는 것을 방지 시켜줌.

(Unlikelihood training은 undesired token을 생성하는 것이 문제): *아마도 ULS에서는 positive token에 대한 정보가 없기 때문*

{% include figure.liquid loading="eager" path="assets/img/posts/2023-09-19-the-cringe-loss-learning-what-language-not-to/image_001.png" class="img-fluid rounded z-depth-1" %}

해당 방법은 positive sequences에 대해서 repetition을 줄이는데 효과적이긴 하지만, 임의의 negative token에 대한 correct positive token의 knowledge가 필요하기 때문에 negative examples들에 대해 일반화 시키기는 어려움.

본 연구에서 제시하는 방법론은 위의 두 방법에 영감을 받고, **negative example training setting**에 대해서 **generalize**할 수 있는 장점이 있음.

1. Negative examples을 objective function에 추가해서 training하는 것 말고, negative examples을 활용하는 방법으로 별도의 classifier 혹은 reranker model을 학습 시키는 것도 존재함.

1. 독립적인 model이 final generation을 선택해주는 것 말고도 model-guiding에 관한 연구들도 다수 존재.

- **(FUDGE: Controlled Text Generation With Future Discriminators, NAACL 2021)**

- **(Am I Me or You? State-of-the-art Dialouge Models Cannot Maintain an Identity, NAACL 2022)**

- **(DIRECTOR: Generator-Classifiers For Supervised Language Modeling, ACL 2022)**

# Method

### CRINGE Loss (ContRastive Iterative Negative GEnearation)

Positive와 negative sequence를 모두 포함하는 training data에 대해 학습을 진행함.

# Experiment

### **Baselines**

- **Transformer Baseline**: 모든 baselines들이 아래 두개의 transformers를 backbone model로 사용

- **Reranking and Model Guiding**

- **Unlikelihood Loss**

- **Director**

- **SCONES (Sigmoid-only)**

## Safe Generation Task

모든 실험 setting은 DIRECTOR에서 진행한 실험과 동일하게 구성.

Backbone으로 BB1 사용

다음 두 가지 기준으로 평가 진행

1. 동일 prompt가 주어질 때, ConvAI2 dataset의 gold respones에 대한 F1 score로 ***generation performance*** 측정

1. WTC dataset의 toxic prompt에 대한* ****safe generation***의 비중 (DIRECTOR에서 사용한 classifier를 기준으로 평가 진행 → CRINGE training loop에서 사용되는 c도 동일하게 사용)

{% include figure.liquid loading="eager" path="assets/img/posts/2023-09-19-the-cringe-loss-learning-what-language-not-to/image_002.png" class="img-fluid rounded z-depth-1" %}

- CRINGE loss (single iteration)은 DIRECTOR와 비슷한 수준을 보이고, unlikelihood training, Reranker, FUDGE, PACER보다 높은 성능 보임

- 추가 iteration 진행한 CRINGE는 Geneartion perfromance (F1)을 거의 유지하며, Safety score가 거의 100% 수준을 보임 

- 아래는 WikiToxic prompt에 대한 정성 평가인데, CRINGE는 safe response를 잘 생성하는 반면에 DIRECTOR는 그렇지 못함 

## Contradiction Avoidance Task

사람이 contradictory / nonconctradictory로 label한 examples인 DECODE dataset을 사용 

Backbone으로 BB1 사용

다음 두 가지 기준으로 평가 진행

1. ConvAI2 dataset의 gold respones에 대한 F1 score로 ***generation performance*** 측정

1. DECODE에서 ***coherent*** 비중 (여기서도 Safe Generation Task와 유사하게 별도의 labeled dataset에 학습된 classifier 사용)

{% include figure.liquid loading="eager" path="assets/img/posts/2023-09-19-the-cringe-loss-learning-what-language-not-to/image_003.png" class="img-fluid rounded z-depth-1" %}

- CRINGE (single-iteration)과 DIRECTOR가 다른 baseline 보다 classifier accuracy 측면에서 큰 차이로 우수한 성능을 보임 

## Open-domain Dialogue (FITS) Task

specific tasks가 아닌 practical한 상황에서 평가하기 위해 Feedback for Interactive Talk & Search (FITS) benchmark사용해서 실험 진행 

Backbone으로 BB2 사용 (search engine 사용 → FiD를 통해 top search results 사용)

{% include figure.liquid loading="eager" path="assets/img/posts/2023-09-19-the-cringe-loss-learning-what-language-not-to/image_004.png" class="img-fluid rounded z-depth-1" %}

- valid(684), test(1453), test unseen(1366) 종류의 F1 score에 대한 weighted average 

- CRINGE (single-iteration)이 baseline 뛰어 넘고, 추가 iteration한 case가 가장 우수함

{% include figure.liquid loading="eager" path="assets/img/posts/2023-09-19-the-cringe-loss-learning-what-language-not-to/image_005.png" class="img-fluid rounded z-depth-1" %}

- 각 data별로 성능을 나누어 확인해보면, CRINGE는 iteration이 거듭될 수록 test unseen에서 성능이 하락하는 것을 볼 수 있음. 다소 큰 폭으로 성능이 하락하는데, 저자는 이를 overfitting이 원인일 수 있다고 방어함.

# Conclusion

본 연구에서는 LM을 iterative하게 학습시킬 수 있는 CRINGE Loss를 새롭게 제안함.

그런데, 개인적인 생각으로 CRINGE Loss는 **(A Simple Contrastive Learning Objective for Alleviating Neural Text Degeneration, arxiv 2022) **에서 주장한 Contrastive Loss와 구조적으로 거의 동일하고, negative token에 대한 alternative positive token을 top-k prediction으로 사용해 개선한 점이 유일한 novelty라고 생각함. 

iterative하게 training data를 scale up 시키는 것에 대한 effectiveness를 실험적으로 잘 보여줬고, Safety task 와 Contradiction task에서 압도적으로 높은 성능을 보임

다만, Open-domain Dialogue Task에서는 Unlikelihood training과 비슷하거나 못한 성능을 보임 

최근 Language Modeling objective function에 variant를 가한 아이디어 자체는 아래 범주에서 크게 벗어나지 않고 있는 것 같다고 느낌

{% include figure.liquid loading="eager" path="assets/img/posts/2023-09-19-the-cringe-loss-learning-what-language-not-to/image_006.png" class="img-fluid rounded z-depth-1" %}
