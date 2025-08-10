---
categories:
- paper-reviews
date: '2024-07-02 00:00:00'
description: 논문 리뷰 - Tokenizer 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- embedding
- neural
- paper-review
- tokenizer
thumbnail: assets/img/posts/2024-07-02-llama3-tokenizer/thumbnail.jpg
title: Llama3 Tokenizer
---

**논문 정보**
- **Date**: 2024-07-02
- **Reviewer**: 준원 장
- **Property**: Tokenizer

## Llama3의 개선사항

- Llama3은 전작인 Llama2에 비해서 (1) 학습 데이터 증가 (2) 컨텍스트 길이 증가 (3) tokenizer 교체 (4) GQA등을 적용해서 성능을 향상시켰다고 알려져 있습니다.

- 이 글에서는 (3)에 대해서 보다 깊게 다뤄보고자 합니다.

## Tokenizer의 역할

- [’FileExistsError:’]라는 string이 있을때 더 많은 token이 있는 Tokenizer는 ‘FileExistsError:’를 하나의 token으로 처리할 수 있는 반면, 적은 token이 있는 Tokenizer는 [’File’, ‘Exists’, ‘Error’, ‘:’]로 나누어서 해당 정보를 언어모델에게 처리시킵니다.

## Llama3 Tokenizer의 개선 사항

### Tokenizer의 교체

- Llama3부터는 **BPE(Byte Pair Encoding)**기반의  https://github.com/openai/tiktoken?tab=readme-ov-file 라이브러리로 교체를 했다고 합니다. (효율성과 확장성 때문이지 않을까라고 사료됩니다)

- ti-tokn 라이브러리는 token당 4 bytes의 압축률을 보인다고 합니다.

- 다른 Tokenization 알고리즘은 어떻게 동작할까요?

{% include figure.liquid loading="eager" path="assets/img/posts/2024-07-02-llama3-tokenizer/image_000.png" class="img-fluid rounded z-depth-1" %}

### Token수의 확장 및 이를 통한 효용

- Tokenizer를 변경해 32K개의 토큰에서 128K개의 토큰으로 Vocab Size를 확장했습니다.

- Compression Ratio = Number of Tokens/(Number of characters to encode & Number of bytes)

- 그렇다면 Vocab Size 확장은 왜 중요할까요?

### Token수의 확장은 Not Free Lunch

- 이미 눈치채셨겠지만, Vocab Size를 4배 가량 확장했다는 의미는 Embedding Layer, lm_head(Research Scientist는 Debedding Layer라구하더라구요!ㅋㅋ)도 그만큼 확장해야 한다는 의미입니다. 

- 실제로 이 이유가 Llama3가 7B가 아니라 8B로 끝난 이유라고 합니다..! 

- 특히나 lm_head가 증가하면 inference 속도에 직접적인 영향을 주기 때문에 GQA를 줘서 완화를 했다고 합니다.

- GQA는 MHA와 MQA 사이의 sweet spot이라고 하는데요, 조만간 다른글 혹은 해당 글의 연장선으로 찾아뵙도록 하겠습니다.

## References

https://www.youtube.com/watch?v=qpv6ms_t_1A

https://github.com/openai/tiktoken?tab=readme-ov-file

https://discuss.pytorch.kr/t/llama-3-tokenizer-youtube/4899

https://www.youtube.com/watch?v=Tmdk_H2WDj4&utm_source=pytorchkr&ref=pytorchkr

https://medium.com/codex/sentencepiece-a-simple-and-language-independent-subword-tokenizer-and-detokenizer-for-neural-text-ffda431e704e
