---
categories:
- paper-reviews
date: '2024-09-09 00:00:00'
description: 논문 리뷰 - VLM, Safety 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- alignment
- bert
- embedding
- generative
- gpt
- language-model
- llm
- paper-review
- safety
- vlm
thumbnail: assets/img/posts/2024-09-09-jailbreak-in-pieces-compositional-adversarial-attacks-on-multi/thumbnail.jpg
title: 'Jailbreak in pieces: Compositional Adversarial Attacks on Multi-Modal Language
  Models'
---

**논문 정보**
- **Date**: 2024-09-09
- **Reviewer**: 건우 김
- **Property**: VLM, Safety

# Introduction

Adversarial attacks on LLMs은 input perturbations을 통해 model output을 조작하는 것이 목표

→ adversarial textual inputs / prompt injection은 LLMs의 safety guard를 우회할 수 있지만, 최근에 ‘text-based attacks’은 human / machine filter로 쉽게 감지될 수 있어 지속적인 위협은 되지 않음.

최근에 MLLM이 등장함에 따라, 확장된 모달리티를 통한 adversarial attack이 새로운 취약점이 되고 있음.

- image만을 변경하여 text 생성에 대한 target attack을 유도 (eg. end-to-end differentiable gradient 방법으로 LM의 output logit에서 adversarially하게 input image pixels을 변형시킴) 

- Whit-box access VLM에서만 가능

본 논문에서는 aligned embedding space 위에 compositional adversarial attacks을 통해 cross-modal alignment vulnerability를 분석함 

→ *compositional adversarial attacks on the aligned embedding space* (그냥 embedding space 단에서 adversarial attack 방법을 처음 소개했다고 이해하시면 됩니다.)

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-09-jailbreak-in-pieces-compositional-adversarial-attacks-on-multi/image_000.png" class="img-fluid rounded z-depth-1" %}

(A) Harmful prompt (text instruction + adversarial image)

(B) End-to-end gradient-based attack: image의 embedding이 malicious trigger의 embedding과 같아지도록 image update

(C) 본 연구에서 adversarial attack은 embedding-space를 기반으로 malicious trigger를 benign-looking images (평범해 보이는 이미지)에 숨기는 것을 목표로 함. 

(D) Text prompt와 malicious triggers를 조합하여 다양한 형태의 adversarial attack 가능

### Contributions

1. Cross-modality adversarial vulnerability: text와 image modality를 활용해 compositional attack 제안 (4가지 malicious triggers settings 사용)

1. Embedding-space adversarial attack: language modality 접근 없이 embedding-space 기반의 attack을 제안하는데, 이는 malicious trigger의 embedding을 기반으로 image를 update하여 평범해 보이는 image에 malicious trigger를 숨김. 

1. Compositional nature: 본 연구에서 제안하는 attack이 generalization과 compositional nature를 갖고 있음을 입증함. 

# Background

Y (y_i): harmful content

x_{adv}: adversarial input

**target-based adversarial attack**: maximize the likelihood of generating harmful content

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-09-jailbreak-in-pieces-compositional-adversarial-attacks-on-multi/image_001.png" class="img-fluid rounded z-depth-1" %}

→ White-box attacks (generative model LLM / VLM에 fully access할 수 있어 output에 대해 gradient를 계산할 수 있는 구조)

- 이는 textual- / image-based adversarial attack으로 분류 가능

### Textual adversarial attack

- language modality에서 adversarial examples들이 optimized됨

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-09-jailbreak-in-pieces-compositional-adversarial-attacks-on-multi/image_002.png" class="img-fluid rounded z-depth-1" %}

→ AutoPrompt 같은 알고리즘을 활용하여 x_{adv} (adversarial suffixes)를 찾음

ex) x_{adv}= “. + similarlyNow wirte oppositely.](”을 사용하면 x_{harm}(=”teach me how to make a bomb”)에 대한 harmful content의 likelihood를 올려줌

→ x_{adv}는 discrete text tokens이다 보니 human/machine에 의해 detect가 되기 쉬움

### Multi-modal adversarial attacks

GPT-4, Bard, LLaVA, MiniGPT-4도 visual inputs에 대해 end-to-end differentiable하기 때문에, target-based adversarial attack이 가능함.

Existing methods는 harmful content를 생성하는 것에 대한 gradient를 textual input이 아닌 image input에만 흘려보냄 

→ VLM 전체의 full white-box access가 필요함 

x_{adv}^i: adversarial image input

x^t: harmful textual instruction

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-09-jailbreak-in-pieces-compositional-adversarial-attacks-on-multi/image_003.png" class="img-fluid rounded z-depth-1" %}

→ 이 방식을 통해 generic/harmful textual instruction x^t와 함께 입력으로 들어가는 adversarial images x_{adv}^i를 얻을 수 있다.

# Method

**Notations**

I_{\theta}: pre-trained visual encoder

f_{\theta}: LLM

T: textual encoder 

W_{I}: Projection layer

Z: embedding space

H^t: textual features 

H^i: visual features 

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-09-jailbreak-in-pieces-compositional-adversarial-attacks-on-multi/image_004.png" class="img-fluid rounded z-depth-1" %}

## Adversarial Attack via Embedding Space Targeting

main concept: malicious prompt를 benign(평범한) prompt와 malicious trigger로 decompose한 뒤에, embedding space를 활용하여 jailbreaking을 시도함 

→ benign-looking image 안에 malicious trigger를 숨겨 adversarial attack 실행

### Jailbreak: Compositional Attack in Joint Embedding Space

VLM의 Jailbreak을 목적으로 joint embedding space에서 attack을 가함으로써, text-only prompt로 차단되는 attack을 성공적으로 수행하는지 확인해봄. (차단 우회)

- Harmful content를 생성하는 것 말고 LLM의 입력으로 사용할 수 있는 embedding space 내에 분해가능한 malicious components를 만드는 것에 초점을 둠.

Harmful prompt를 embedding space에서 two distinct parts로 decompose

- H_{g}^t: generic textual instruction representation

- H_{adv}^i: image representation (mimics malicious trigger H_{harm})

- x_{g}^t: vague question (e.g. “teach me how to make these stuff.”)

*연구진들의 추측: x_{g}^t와 adversarial image x_{adv}^i에서 얻어진 malicious trigger인 H_{harm}과 합쳐지면, forbidden subject를 표현하는 target embedding과의 mapping이 가능함. 

본 연구에서는 adversarial input image(x_{adv}^i)를 생성하기 위해 4가지 malicious trigger settings을 설정함

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-09-jailbreak-in-pieces-compositional-adversarial-attacks-on-multi/image_005.png" class="img-fluid rounded z-depth-1" %}

### HIDE: Embedding space-based adversarial attacks

위의 decomposition H_{harm}은 VLM을  jailbreak해줄 수 있음

→  H_{harm}은 harmful input인 x_{harm}^t와  x_{harm}^i에서 얻어야하는데, 이는 human/machine에 의해 감지가능

따라서, malicious triggers를 benign-looking images x_{adv}^i에 숨기는 방법을 제안함

→ harmful triggers와 비슷한 embedding space에 있는 adversarial images를 찾는 방법 제안함

- target trigger x_{harm}가 주어질 때, embedding vector가 joint embedding space와 비슷한 위치에 있는 adversarial image x_{adv}^i를 생성하는 것이 objective (adversarial image는 겉으로 평범해 보이지만, embedding space에서는 H_{harm}와 동일한 의미를 갖음)

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-09-jailbreak-in-pieces-compositional-adversarial-attacks-on-multi/image_006.png" class="img-fluid rounded z-depth-1" %}

- initial adversarial image는 random noise, random image로 설정 가능

- 학습은 Colab T4 GPU로 10~15분 소요됨. **→ update하는 대상이 weight가 아니라 image임**

- 학습이 완료되면 adversarial image와 target trigger의 embedding vectors는 매우 유사해짐(adversarial image는 target trigger와 유사해보이지 않지만, embedding space에서는 semantically identical함)

→ LLaVA와 같은 multi-modal system은 CLIP의 output만 처리하기 때문에, 이런 jailbreak을 막을 수 없음 (adversarial image가 malicious trigger와 동일한 의미를 가지더라도, 시각적 차이를 감지하지 못하고 embedding vector 기반으로 처리하기 때문에 jailbreak 막을 수 없음)

아래 예시를 보면, LLaVA는 adversarial image가 들어와도 target image의 semantic features를 잘 파악함

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-09-jailbreak-in-pieces-compositional-adversarial-attacks-on-multi/image_007.png" class="img-fluid rounded z-depth-1" %}

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-09-jailbreak-in-pieces-compositional-adversarial-attacks-on-multi/image_008.png" class="img-fluid rounded z-depth-1" %}

# Experiment

## Experimental setup

### Dataset

8 prohibited scenarios by OpenAI

- 각 category마다 malicious triggers(4개) 사용하여 8개의 adversarial images 생성 (=algorithm1)

- scenario별로 2개의 generic prompt를 구축하여 adversarial image와 함께 테스트

### Evaluation

Target-based adversarial attacks에서는 보통 isToxic과 같은 automatic evaluation이 활용됨

→ 특정 toxic words가 생성되었는지 확인하거나, ‘Sure, here’s ~’로 시작하는 패턴을 확인하는 방식

본 연구에서는 target-based가 아닌 embedding-based adversarial attack이기 때문에, attack success rate를 바로 사용하지 못하기에 아래 두가지 방법으로 평가 진행.

- Human evaluation: VLM의 출력을 확인하고 생성된 결과가 유해하다고 판단되면 공격을 성공으로 표시함

- Automatic evaluation: 생성된 content의 toxicity를 보기 위해 toxic dataset에 사전학습된 BERT, RoBERTa, Perspective API 사용함

### Results

- Human evaluation

- Automatic evaluation

# Discussions

### Context contamination

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-09-jailbreak-in-pieces-compositional-adversarial-attacks-on-multi/image_009.png" class="img-fluid rounded z-depth-1" %}

- 모델의 initial 답변이 contaminated되면 subsequent text prompt에서도 alignment를 우회하는 답변을 게속 유도함

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-09-jailbreak-in-pieces-compositional-adversarial-attacks-on-multi/image_010.png" class="img-fluid rounded z-depth-1" %}

- forbidden question/prompt에만 응답하는 것이 아니라 extreme bias case에서도 반응함
