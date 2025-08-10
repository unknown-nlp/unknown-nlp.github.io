---
categories:
  - paper-reviews
date: "2023-06-29 00:00:00"
description: 논문 리뷰 - LLM, Efficient Training 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
  - bert
  - efficient training
  - gpt
  - llm
  - paper-review
  - transformer
thumbnail: assets/img/posts/2023-06-29-qlora-eficient-finetuning-of-quantized-llms/thumbnail.jpg
title: "QLoRA: Eficient Finetuning of Quantized LLMs"
---

**논문 정보**

- **Date**: 2023-06-29
- **Reviewer**: 건우 김
- **Property**: LLM, Efficient Training

# Introduction

- Finetuning LLMs is effective way to improve performance, and to add desirable or remove undersiable behaviors

- **QLoRA**: quantize PLM to 4-bit, and add learnable params LoRA weights (updated using quantized weigths) → _performance degradation x_

- **Additional analysis **

## Background

- **Block-wise k-bit Quantization**

- **Low-rank Adapters**

- **Memory Requirement of Parameter-Efficeint Finetuning**

## QLoRA Finetuning

{% include figure.liquid loading="eager" path="assets/img/posts/2023-06-29-qlora-eficient-finetuning-of-quantized-llms/image_000.png" class="img-fluid rounded z-depth-1" %}

- QLoRA의 **storage data type은 4-bit** / **computation data type은 BFloat16**

- **4-bit NormalFloat(NF) Quantization**

- **Double Quantization**

- **Paged Optimzier**

- **QLoRA**

## QLoRA vs Standard Finetuning

- **Default LoRA hyperparameters do not match 16-bit performance**

- **4-bit NormalFloat yields better performance than 4-bit Floating Point**

- **k-bit QLoRA matches 16-bit full finetuning and 16-bit LoRA performance**

- Summary

## Pushing the Chatbot State-of-the-art with QLoRA

- Experiment settings

## Qualitative Analysis

- 다른 LLMs과 비슷한 양상의 실수들이 존재하기 때문에 **생략**

## Limitations and Discussion

- QLoRA를 통해 4-bit base model로 16-bit full finetuning 성능을 재현할 수는 있었지만, model의 scale이 33B 혹은 65B까지 가면 그렇지 못했다. → resource 부족으로 원인 발견 x

- Evaluation of instruction finetuning models

- 다른 bit-precision (e.g 3-bit) base models 혹은 다른 adapter 방법론에 대한 실험 부재

### Implementation

```python
from transformers import AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("facebook/opt-350m", load_in_4bit=True, device_map="auto")

##################

from transformers import BitsAndBytesConfig


nf4_config = BitsAndBytesConfig(
   load_in_4bit=True,
   bnb_4bit_quant_type="nf4",
   bnb_4bit_use_double_quant=True,
   bnb_4bit_compute_dtype=torch.bfloat16
)

model_nf4 = AutoModelForCausalLM.from_pretrained(model_id, quantization_config=nf4_config)

##########
accelerate library를 사용하기 때문에, 지원하는 models은 모두 사용 가능
- Llama, OPT, GPT-Neo, GPT-NeoX

[
    'bigbird_pegasus', 'blip_2', 'bloom', 'bridgetower', 'codegen', 'deit', 'esm',
    'gpt2', 'gpt_bigcode', 'gpt_neo', 'gpt_neox', 'gpt_neox_japanese', 'gptj', 'gptsan_japanese',
    'lilt', 'llama', 'longformer', 'longt5', 'luke', 'm2m_100', 'mbart', 'mega', 'mt5', 'nllb_moe',
    'open_llama', 'opt', 'owlvit', 'plbart', 'roberta', 'roberta_prelayernorm', 'rwkv', 'switch_transformers',
    't5', 'vilt', 'vit', 'vit_hybrid', 'whisper', 'xglm', 'xlm_roberta'
]
```
