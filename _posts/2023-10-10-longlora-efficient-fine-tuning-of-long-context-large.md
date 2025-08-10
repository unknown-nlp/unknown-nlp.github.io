---
categories:
  - paper-reviews
date: "2023-10-10 00:00:00"
description: 논문 리뷰 - LLM, Efficient Training 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
  - attention
  - efficient training
  - embedding
  - fine-tuning
  - language-model
  - llm
  - paper-review
  - transformer
thumbnail: assets/img/posts/2023-10-10-longlora-efficient-fine-tuning-of-long-context-large/thumbnail.jpg
title: "LongLoRA: Efficient Fine-Tuning of Long-Context Large Language Models"
---

**논문 정보**

- **Date**: 2023-10-10
- **Reviewer**: 건우 김
- **Property**: LLM, Efficient Training

## Abstract

LLM의 context extension을 두 가지 aspects를 고려함

1. inference는 dense global attention이 필요하지만, finetuning은 sparse local attention으로 사용 가능 → shift short attention (S^2-Attn) 제안

1. PEFT 방법 적용 → 단순히 LoRA를 적용한 LongLoRA 제안

8장 A100으로 LongLoRA를 적용한 LLaMA2 7B는 최대 100k, 70B는 32k token까지 처리 가능

## Introduction

길이가 긴 text를 처리하고자 하는 LLM에 대한 수요가 많음. 하지만 단순히 long text를 finetuning하는 것은 compuationally 매우 비싸기 때문에 이에 대한 연구들이 많이 이어져 왔음.

최근에 연구된 Positional Interpolation (Chen et al., 2023)은 RoPE을 기반으로 LLM의 context window size를 32k까지 늘리는 방법을 제안했지만, 실제로 8k 이상의 길이를 처리하게끔 학습을 시킬 때 128대의 A100이 필요하다는 resource가 여전히 많이 필요하다는 문제점이 있음.

{% include figure.liquid loading="eager" path="assets/img/posts/2023-10-10-longlora-efficient-fine-tuning-of-long-context-large/image_000.png" class="img-fluid rounded z-depth-1" %}

또한, Focused Transformer (Tworkowski et al., 2023)은 contrastive learning에 영감을 받은 학습 방식을 사용해서 256k 길이의 prompt까지 처리할 수 있긴 하지만, 이 역시도 128대의 TPU가 필요하다는 문제점이 있다.

{% include figure.liquid loading="eager" path="assets/img/posts/2023-10-10-longlora-efficient-fine-tuning-of-long-context-large/image_001.png" class="img-fluid rounded z-depth-1" %}

이 외에도 다양한 연구들이 최근에 진행이 되었지만, efficient하게 접근해서 long text를 처리하는 연구는 없음. 본 연구에서 efficient하게 적은 resource로 LLM을 long text에 training시키는 방법을 처음으로 제안함.

연구진들은 직관적으로 pre-trained LLM에 LoRA를 단순히 적용하는 것을 시도해봤는데, 실험적으로 이렇게 하면 long context에서 매우 높은 perplexity를 보인다고 발견함 (=no effectiveness). 또한, LoRA를 사용하는 것과 무관하게 self-attention 연산에서 computational cost가 높은 것을 지적함 (=no efficiency). 아래 그림에서 확인 가능 (LoRA)

{% include figure.liquid loading="eager" path="assets/img/posts/2023-10-10-longlora-efficient-fine-tuning-of-long-context-large/image_002.png" class="img-fluid rounded z-depth-1" %}

본 연구에서 위에 문제점들을 개선한 LongLoRA를 소개함.

Contributions은 다음과 같음

- **shift short attention (S^2-Attn)**: standard self-attention 대체

- **fine-tuning layers**: Embedding layers + normalization layers + LoRA training

- **LongQA dataset**: SFT에 사용되는 long text dataset을 직접 구축하고 제안

## Related work

### Long-context Transformers

- retrieval-based approach: inference 시에 attention mechnaism을 변경하지 않아도 됨

- modify multi-head attention: quadratic complexity를 갖는 self-attention 연산을 완화

### Long-context LLMs

- fine-tuning을 통해 context length를 확장

- Postion embedding에 변화를 주는 연구

### Efficient Fine-tuning

(생략)

## Method

{% include figure.liquid loading="eager" path="assets/img/posts/2023-10-10-longlora-efficient-fine-tuning-of-long-context-large/image_003.png" class="img-fluid rounded z-depth-1" %}

### Shift Short Attention

**Pilot test**

- Model: LLaMA2 7B (finetuned on RedPajama (2023) dataset)

- Short: target context 길이의 1/4

- Long: target context 길이

- Metric: perplexity

{% include figure.liquid loading="eager" path="assets/img/posts/2023-10-10-longlora-efficient-fine-tuning-of-long-context-large/image_004.png" class="img-fluid rounded z-depth-1" %}

당연하게 finetuning을 하지 않으면, context 길이가 늘어남에 따라 perplexity가 매우 높아짐.

앞으로 standard baseline을 full attention으로 full finetuning시킨 model로 설정

1. **Pattern 1 (Short attention)**

1. **Pattern 2 (Shifted pattern)**

**Consistency to Full Attention**

본 논문에서 제안하는 S^2-Attn을 다른 efficient attention과 비교 진행

{% include figure.liquid loading="eager" path="assets/img/posts/2023-10-10-longlora-efficient-fine-tuning-of-long-context-large/image_005.png" class="img-fluid rounded z-depth-1" %}

### Improved LoRA for Long Context

LoRA를 바로 LLM에 적용해서 lon-context를 다루는 것은 어렵다. 실제로, 아래 Table에서 LoRA와 Full-finetuning간의 perplexity는 많이 차이 나고, LoRA Rank를 키워봐도 별로 효과가 없음.

따라서, 단순히 LoRA만 학습시키는 것이 아니라 Normalization/embedding layers를 LoRA와 함께 학습 시키는 것이 Full Finetuning과 성능 면에서 비슷한 것을 실험적으로 확인함

- Model: LLaMA2 7B (with S^2-Attn)

- Target length: 32k

- +Norm/Embed: Normalization layers 혹은 embedding layers를 학습 시키는지

## Experiment

### Settings

- Models and maximum extended context window sizes

- Resources

- Datasets

### Main Results

**Long-sequence Language Modeling**

아래는 proof-file data에 대한 perplexity. Redpajama perplexity는 appendix에 있던데, perplexity 값이 7~8 정도 되서 본문에 넣지 않은듯.

{% include figure.liquid loading="eager" path="assets/img/posts/2023-10-10-longlora-efficient-fine-tuning-of-long-context-large/image_006.png" class="img-fluid rounded z-depth-1" %}

가장 흥미롭게 본 실험 결과인데, 극단적으로 context length를 늘리고 난 결과 LongLoRA는 준수한 실험 결과를 보여줌. (근데 이것도 역시 proof-pile dataset)

{% include figure.liquid loading="eager" path="assets/img/posts/2023-10-10-longlora-efficient-fine-tuning-of-long-context-large/image_007.png" class="img-fluid rounded z-depth-1" %}

RedPajama도 그렇게 나쁘진 않음

{% include figure.liquid loading="eager" path="assets/img/posts/2023-10-10-longlora-efficient-fine-tuning-of-long-context-large/image_008.png" class="img-fluid rounded z-depth-1" %}

### Ablation study

- **Efficiency Profile**

- Fine-tuning steps

## Conclusion

LLM이 Long-context를 다루는데 효과적인 매우 간단한 방법론인 LongLoRA를 제안함. LLaMA가 2048 tokens, LLaMA2가 4096 tokens까지 처리하는 것을 생각하면, 본 실험에서 진행한 **32k**~**100k**는 매우 크다는 것을 알 수 있음.

또한, A100 8장으로 모든 실험을 진행했기에 정말 효율적으로 학습을 진행시킬 수 있고, Full-FT와 비교해도 비슷한 수준을 선 보임.
Downstream task로는 topic retrieval을 진행하고, 해당 분야에서 SOTA인 LongChat-13B와 비교했을 때, 실제로 비슷하거나 더 나은 성능을 보여줌. 다만, downstream task가 하나 밖에 없어서 아쉬움 (물론 극단적인 길이의 long-context를 처리하는 task의 부재도 있음)

{% include figure.liquid loading="eager" path="assets/img/posts/2023-10-10-longlora-efficient-fine-tuning-of-long-context-large/image_009.png" class="img-fluid rounded z-depth-1" %}
