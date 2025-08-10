---
categories:
- paper-reviews
date: '2025-06-24 00:00:00'
description: 논문 리뷰 - Multimodal 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- attention
- language-model
- llm
- multimodal
- paper-review
- reasoning
- vision
thumbnail: assets/img/posts/2025-06-24-see-what-you-are-told-visual-attention-sink/thumbnail.jpg
title: 'See What You Are Told: Visual Attention Sink in Large Multimodal Models'
---

**논문 정보**
- **Date**: 2025-06-24
- **Reviewer**: 조영재
- **Property**: Multimodal

## Introduction

- LLM의 발전과 함께 Multimodal 모델들도 많이 등장하고 있음 (VQA, image captioning, visual reasoning, …)

- LMM에서도 LLM 처럼 똑같이 attention 매커니즘을 따름.  예를 들어 ‘bird’를 말하고자 할때 model은 해당 이미지에 관련있는 visual token에 대해 집중함. (직관적으로) text와 visual token이 매칭됨.

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/f116d18e-8a97-4353-ab93-9caf9c0af669/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643OIJKSW%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCbneZjdMjBmANuGlk9pBqG2QlBPOD8%2FSd22DXSbHJ7tgIhANG%2BLix6siOENG8SYanuqtOw8gRSiENNQjA6MbJ6T1y6KogECNT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzBYg3nSkvQ22qQa6sq3AMhHyPsCsEjXCd4RPSkokt4VrGcDE3sPg2D%2BPrfFrB%2BmrCAt%2BrF8a%2BGKpPINze9JbpTj02HjYdsmIW6kPlhslRBl0LPWPJ%2BA%2Bz1iir6Ci6H%2FgfiguDRZc84tzgM4STYUuqeF1Im8mrQAtQRJdxh38onjpYZpzHO14AnZVBKRv1ufqgOEXeXZiAfevASD8dggVm9B9eHiWIMCZ8Vklyhb36FfcFAqo6rAqj35kqsxEGr1YWc9hbV71k%2F7KqMB3FK0fQjyR47kx1vfNz%2B0W03zQpeh%2B3Kom%2FHDh5eZZvkLyN0DyKcVJKT4oiy5%2BRy45lCgbfBlqFWVyvLeMETZJVahaLpy2X9IdmfbA8VzUahXusUkiM0C%2Bs6FS6z6AdqADg4hgxx3H%2Bm7Uus7F6%2BolLsxjrj2jlCfgsLucZKH0TVPN1fAeGhnyio4cJBWbVNYGvTJgmC6%2Fh%2FjpLfInusSdMCOEnGEVKJnIHfBAyiftor0YeL3y8Quea%2FRMpOmPn2JA5%2BtCX1bhm41TOsPCYqOIvEbxeK8ybiFrfxl%2Bi6Imi6tYX%2BcLsHcVwzzaBpTDWWH9vf1IMavPQrxtBcLYOrcuJEh%2B3gwXdHNpC1yPoF%2FTIa%2BB%2B0O50NFoyvVEA0f3tPbTDN%2FuHEBjqkAbi%2F5jRMviZVUC%2FTJIpOKeqJfYMiYZ7Uj5CqXSkqb7c4OGcT9fP%2F%2B4Kw%2Bzo1fi3tDa%2FkqzSv3Dk6ZFA6r9KzHdLLMkykq6uCjXQ27ZdFTtG42yeCWfWjfgMTj8KHRRVBaNWkEeBc05hvNXmofYQ3VN6n7Gkm42Pb5TKahWcrceqH93AIgr%2ByWmZptm2yVveJcbnedVDlUY3MREFfySkEq3fjqRmU&X-Amz-Signature=1b08aaacbdf6ea1deecd9d34cdde41b662b9ed7024d8fae6d6e68a3c9172cf0a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 근데 실제로는 text와 visual 간의 관계가 unrelated 되는 경우도 관측됨. attention map을 통해 attention을 더 면밀히 살펴보았을때, Example 1을 보면, 위에 bird를 말하는데 ‘빨간 네모’ 처럼 bird와 무관한 곳에 높은 attention이 관측. 다른 예제들도 마찬가지로 텍스트와 무관한 곳에 높은 어텐션이 관측됨. 이게 왜 발생하는지 궁금해서 해당 연구가 시작됨

-  해당 연구의 발견

- 최근에 vlm에서 attention이 text에 비해 이미지에 부족하게 할당된다는 사전 연구도 있었음. 그래서 우리는 attention budget의 개념으로 visual sink token들에 가는 attention을 아껴서 다른 visual token들에 redistribute를 하고자 함(Visual Attention Redistribuion (VAR))

## Related Work

- Visual attention in large multimodal models.


-  Attention sink in language models

## Preliminaries

트랜스포머 공식

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/b655d950-c981-4a30-9376-56a986850191/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643OIJKSW%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCbneZjdMjBmANuGlk9pBqG2QlBPOD8%2FSd22DXSbHJ7tgIhANG%2BLix6siOENG8SYanuqtOw8gRSiENNQjA6MbJ6T1y6KogECNT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzBYg3nSkvQ22qQa6sq3AMhHyPsCsEjXCd4RPSkokt4VrGcDE3sPg2D%2BPrfFrB%2BmrCAt%2BrF8a%2BGKpPINze9JbpTj02HjYdsmIW6kPlhslRBl0LPWPJ%2BA%2Bz1iir6Ci6H%2FgfiguDRZc84tzgM4STYUuqeF1Im8mrQAtQRJdxh38onjpYZpzHO14AnZVBKRv1ufqgOEXeXZiAfevASD8dggVm9B9eHiWIMCZ8Vklyhb36FfcFAqo6rAqj35kqsxEGr1YWc9hbV71k%2F7KqMB3FK0fQjyR47kx1vfNz%2B0W03zQpeh%2B3Kom%2FHDh5eZZvkLyN0DyKcVJKT4oiy5%2BRy45lCgbfBlqFWVyvLeMETZJVahaLpy2X9IdmfbA8VzUahXusUkiM0C%2Bs6FS6z6AdqADg4hgxx3H%2Bm7Uus7F6%2BolLsxjrj2jlCfgsLucZKH0TVPN1fAeGhnyio4cJBWbVNYGvTJgmC6%2Fh%2FjpLfInusSdMCOEnGEVKJnIHfBAyiftor0YeL3y8Quea%2FRMpOmPn2JA5%2BtCX1bhm41TOsPCYqOIvEbxeK8ybiFrfxl%2Bi6Imi6tYX%2BcLsHcVwzzaBpTDWWH9vf1IMavPQrxtBcLYOrcuJEh%2B3gwXdHNpC1yPoF%2FTIa%2BB%2B0O50NFoyvVEA0f3tPbTDN%2FuHEBjqkAbi%2F5jRMviZVUC%2FTJIpOKeqJfYMiYZ7Uj5CqXSkqb7c4OGcT9fP%2F%2B4Kw%2Bzo1fi3tDa%2FkqzSv3Dk6ZFA6r9KzHdLLMkykq6uCjXQ27ZdFTtG42yeCWfWjfgMTj8KHRRVBaNWkEeBc05hvNXmofYQ3VN6n7Gkm42Pb5TKahWcrceqH93AIgr%2ByWmZptm2yVveJcbnedVDlUY3MREFfySkEq3fjqRmU&X-Amz-Signature=ae550b8161cd2603f1dfcb43b16118674dabb7170fb1a034d230e458c1df4090&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/fee16885-a643-48ff-a1c9-49d6eeb9a6d2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643OIJKSW%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCbneZjdMjBmANuGlk9pBqG2QlBPOD8%2FSd22DXSbHJ7tgIhANG%2BLix6siOENG8SYanuqtOw8gRSiENNQjA6MbJ6T1y6KogECNT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzBYg3nSkvQ22qQa6sq3AMhHyPsCsEjXCd4RPSkokt4VrGcDE3sPg2D%2BPrfFrB%2BmrCAt%2BrF8a%2BGKpPINze9JbpTj02HjYdsmIW6kPlhslRBl0LPWPJ%2BA%2Bz1iir6Ci6H%2FgfiguDRZc84tzgM4STYUuqeF1Im8mrQAtQRJdxh38onjpYZpzHO14AnZVBKRv1ufqgOEXeXZiAfevASD8dggVm9B9eHiWIMCZ8Vklyhb36FfcFAqo6rAqj35kqsxEGr1YWc9hbV71k%2F7KqMB3FK0fQjyR47kx1vfNz%2B0W03zQpeh%2B3Kom%2FHDh5eZZvkLyN0DyKcVJKT4oiy5%2BRy45lCgbfBlqFWVyvLeMETZJVahaLpy2X9IdmfbA8VzUahXusUkiM0C%2Bs6FS6z6AdqADg4hgxx3H%2Bm7Uus7F6%2BolLsxjrj2jlCfgsLucZKH0TVPN1fAeGhnyio4cJBWbVNYGvTJgmC6%2Fh%2FjpLfInusSdMCOEnGEVKJnIHfBAyiftor0YeL3y8Quea%2FRMpOmPn2JA5%2BtCX1bhm41TOsPCYqOIvEbxeK8ybiFrfxl%2Bi6Imi6tYX%2BcLsHcVwzzaBpTDWWH9vf1IMavPQrxtBcLYOrcuJEh%2B3gwXdHNpC1yPoF%2FTIa%2BB%2B0O50NFoyvVEA0f3tPbTDN%2FuHEBjqkAbi%2F5jRMviZVUC%2FTJIpOKeqJfYMiYZ7Uj5CqXSkqb7c4OGcT9fP%2F%2B4Kw%2Bzo1fi3tDa%2FkqzSv3Dk6ZFA6r9KzHdLLMkykq6uCjXQ27ZdFTtG42yeCWfWjfgMTj8KHRRVBaNWkEeBc05hvNXmofYQ3VN6n7Gkm42Pb5TKahWcrceqH93AIgr%2ByWmZptm2yVveJcbnedVDlUY3MREFfySkEq3fjqRmU&X-Amz-Signature=cd9c98ff317101feb982a1cd78dce6898228a2ecaa4dc0d5a82a23ad9414e21c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/123e2827-bfa1-4e05-84d4-1bf1c2554142/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643OIJKSW%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCbneZjdMjBmANuGlk9pBqG2QlBPOD8%2FSd22DXSbHJ7tgIhANG%2BLix6siOENG8SYanuqtOw8gRSiENNQjA6MbJ6T1y6KogECNT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzBYg3nSkvQ22qQa6sq3AMhHyPsCsEjXCd4RPSkokt4VrGcDE3sPg2D%2BPrfFrB%2BmrCAt%2BrF8a%2BGKpPINze9JbpTj02HjYdsmIW6kPlhslRBl0LPWPJ%2BA%2Bz1iir6Ci6H%2FgfiguDRZc84tzgM4STYUuqeF1Im8mrQAtQRJdxh38onjpYZpzHO14AnZVBKRv1ufqgOEXeXZiAfevASD8dggVm9B9eHiWIMCZ8Vklyhb36FfcFAqo6rAqj35kqsxEGr1YWc9hbV71k%2F7KqMB3FK0fQjyR47kx1vfNz%2B0W03zQpeh%2B3Kom%2FHDh5eZZvkLyN0DyKcVJKT4oiy5%2BRy45lCgbfBlqFWVyvLeMETZJVahaLpy2X9IdmfbA8VzUahXusUkiM0C%2Bs6FS6z6AdqADg4hgxx3H%2Bm7Uus7F6%2BolLsxjrj2jlCfgsLucZKH0TVPN1fAeGhnyio4cJBWbVNYGvTJgmC6%2Fh%2FjpLfInusSdMCOEnGEVKJnIHfBAyiftor0YeL3y8Quea%2FRMpOmPn2JA5%2BtCX1bhm41TOsPCYqOIvEbxeK8ybiFrfxl%2Bi6Imi6tYX%2BcLsHcVwzzaBpTDWWH9vf1IMavPQrxtBcLYOrcuJEh%2B3gwXdHNpC1yPoF%2FTIa%2BB%2B0O50NFoyvVEA0f3tPbTDN%2FuHEBjqkAbi%2F5jRMviZVUC%2FTJIpOKeqJfYMiYZ7Uj5CqXSkqb7c4OGcT9fP%2F%2B4Kw%2Bzo1fi3tDa%2FkqzSv3Dk6ZFA6r9KzHdLLMkykq6uCjXQ27ZdFTtG42yeCWfWjfgMTj8KHRRVBaNWkEeBc05hvNXmofYQ3VN6n7Gkm42Pb5TKahWcrceqH93AIgr%2ByWmZptm2yVveJcbnedVDlUY3MREFfySkEq3fjqRmU&X-Amz-Signature=5137ce5dcbd824a8862f06dfc7db6ba949b57a53463241460467fc1a1e8c4333&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Visual Attention Sink

Figure1보면 attention이 우리의 직관대로 잘 따라가긴 하지만 **고정된 어떤 background spot**에 굳이 필요없는 limited semanic meaning에 높은 attention이 배정되어 있음

### How to distinguish irrelevant visual tokens?

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/11c46bbd-0156-461d-8ca9-ff4b3741c2e4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643OIJKSW%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCbneZjdMjBmANuGlk9pBqG2QlBPOD8%2FSd22DXSbHJ7tgIhANG%2BLix6siOENG8SYanuqtOw8gRSiENNQjA6MbJ6T1y6KogECNT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzBYg3nSkvQ22qQa6sq3AMhHyPsCsEjXCd4RPSkokt4VrGcDE3sPg2D%2BPrfFrB%2BmrCAt%2BrF8a%2BGKpPINze9JbpTj02HjYdsmIW6kPlhslRBl0LPWPJ%2BA%2Bz1iir6Ci6H%2FgfiguDRZc84tzgM4STYUuqeF1Im8mrQAtQRJdxh38onjpYZpzHO14AnZVBKRv1ufqgOEXeXZiAfevASD8dggVm9B9eHiWIMCZ8Vklyhb36FfcFAqo6rAqj35kqsxEGr1YWc9hbV71k%2F7KqMB3FK0fQjyR47kx1vfNz%2B0W03zQpeh%2B3Kom%2FHDh5eZZvkLyN0DyKcVJKT4oiy5%2BRy45lCgbfBlqFWVyvLeMETZJVahaLpy2X9IdmfbA8VzUahXusUkiM0C%2Bs6FS6z6AdqADg4hgxx3H%2Bm7Uus7F6%2BolLsxjrj2jlCfgsLucZKH0TVPN1fAeGhnyio4cJBWbVNYGvTJgmC6%2Fh%2FjpLfInusSdMCOEnGEVKJnIHfBAyiftor0YeL3y8Quea%2FRMpOmPn2JA5%2BtCX1bhm41TOsPCYqOIvEbxeK8ybiFrfxl%2Bi6Imi6tYX%2BcLsHcVwzzaBpTDWWH9vf1IMavPQrxtBcLYOrcuJEh%2B3gwXdHNpC1yPoF%2FTIa%2BB%2B0O50NFoyvVEA0f3tPbTDN%2FuHEBjqkAbi%2F5jRMviZVUC%2FTJIpOKeqJfYMiYZ7Uj5CqXSkqb7c4OGcT9fP%2F%2B4Kw%2Bzo1fi3tDa%2FkqzSv3Dk6ZFA6r9KzHdLLMkykq6uCjXQ27ZdFTtG42yeCWfWjfgMTj8KHRRVBaNWkEeBc05hvNXmofYQ3VN6n7Gkm42Pb5TKahWcrceqH93AIgr%2ByWmZptm2yVveJcbnedVDlUY3MREFfySkEq3fjqRmU&X-Amz-Signature=42e547a4efc989c3e2bbc650648be8f6a8a67ca4d4ad554f3f4acf72c0a3401f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

irrelevant visual token에서 두 가지 특성이 나타남. (1) figure 1에서 보듯 이미지에 same irrelevant visual token에 고정적으로 등장. (2) BOS 토큰이랑 유사하게 같은 dimension에서 등장 (Fig 2)

### Irrelevant visual tokens have high activation in specific dimensions

- Fig2의 BOS랑 빨간<img> 를 보면 같은 dimension에서 attention 값이 튀는 것을 볼 수 있음. 이는 LLM 각자가 같은 고유한 특성이라고 함. 예를들어 LLaVA-1.5-7B가 사용한 LLaMA2 백본은 모두 고정적으로 {1415, 2533} 의 dimension에서 위와같은 형태를 보임.   (pretrain 과정에서 쏠리는 거라 finetuning을 해도 sink dimension은 계속 고정되어있다고 함)

- 특정 토큰이 갖는 sink dimension value **Φ(x)**를 아래와 같이 정의

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/ae082751-8c4b-48c7-932d-deb1e4cdb933/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643OIJKSW%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCbneZjdMjBmANuGlk9pBqG2QlBPOD8%2FSd22DXSbHJ7tgIhANG%2BLix6siOENG8SYanuqtOw8gRSiENNQjA6MbJ6T1y6KogECNT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzBYg3nSkvQ22qQa6sq3AMhHyPsCsEjXCd4RPSkokt4VrGcDE3sPg2D%2BPrfFrB%2BmrCAt%2BrF8a%2BGKpPINze9JbpTj02HjYdsmIW6kPlhslRBl0LPWPJ%2BA%2Bz1iir6Ci6H%2FgfiguDRZc84tzgM4STYUuqeF1Im8mrQAtQRJdxh38onjpYZpzHO14AnZVBKRv1ufqgOEXeXZiAfevASD8dggVm9B9eHiWIMCZ8Vklyhb36FfcFAqo6rAqj35kqsxEGr1YWc9hbV71k%2F7KqMB3FK0fQjyR47kx1vfNz%2B0W03zQpeh%2B3Kom%2FHDh5eZZvkLyN0DyKcVJKT4oiy5%2BRy45lCgbfBlqFWVyvLeMETZJVahaLpy2X9IdmfbA8VzUahXusUkiM0C%2Bs6FS6z6AdqADg4hgxx3H%2Bm7Uus7F6%2BolLsxjrj2jlCfgsLucZKH0TVPN1fAeGhnyio4cJBWbVNYGvTJgmC6%2Fh%2FjpLfInusSdMCOEnGEVKJnIHfBAyiftor0YeL3y8Quea%2FRMpOmPn2JA5%2BtCX1bhm41TOsPCYqOIvEbxeK8ybiFrfxl%2Bi6Imi6tYX%2BcLsHcVwzzaBpTDWWH9vf1IMavPQrxtBcLYOrcuJEh%2B3gwXdHNpC1yPoF%2FTIa%2BB%2B0O50NFoyvVEA0f3tPbTDN%2FuHEBjqkAbi%2F5jRMviZVUC%2FTJIpOKeqJfYMiYZ7Uj5CqXSkqb7c4OGcT9fP%2F%2B4Kw%2Bzo1fi3tDa%2FkqzSv3Dk6ZFA6r9KzHdLLMkykq6uCjXQ27ZdFTtG42yeCWfWjfgMTj8KHRRVBaNWkEeBc05hvNXmofYQ3VN6n7Gkm42Pb5TKahWcrceqH93AIgr%2ByWmZptm2yVveJcbnedVDlUY3MREFfySkEq3fjqRmU&X-Amz-Signature=1f71f5c28d80143be80de359f1349b844b442be2241881a73c8e2ef7d5d4d546&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

쉽게 말해서 1415, 2333 등과 같은 sink dimension에서 토큰이 갖게 되는 튀는 값을 나타냄. (Fig 2 참고)

- visual sink token을 구분하기 위해 20보다 **Φ(x)**가 큰 토큰들은 다 visual sink token으로 분류. 이를 통해 irrelevant visual token(sink dimension에서 attention 값이 튀는 애들)과 relevant visual token(튀지 않는 애들)을 구분함.**  **

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/915eba9d-c7fa-4379-adfb-327a1963cdd2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643OIJKSW%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCbneZjdMjBmANuGlk9pBqG2QlBPOD8%2FSd22DXSbHJ7tgIhANG%2BLix6siOENG8SYanuqtOw8gRSiENNQjA6MbJ6T1y6KogECNT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzBYg3nSkvQ22qQa6sq3AMhHyPsCsEjXCd4RPSkokt4VrGcDE3sPg2D%2BPrfFrB%2BmrCAt%2BrF8a%2BGKpPINze9JbpTj02HjYdsmIW6kPlhslRBl0LPWPJ%2BA%2Bz1iir6Ci6H%2FgfiguDRZc84tzgM4STYUuqeF1Im8mrQAtQRJdxh38onjpYZpzHO14AnZVBKRv1ufqgOEXeXZiAfevASD8dggVm9B9eHiWIMCZ8Vklyhb36FfcFAqo6rAqj35kqsxEGr1YWc9hbV71k%2F7KqMB3FK0fQjyR47kx1vfNz%2B0W03zQpeh%2B3Kom%2FHDh5eZZvkLyN0DyKcVJKT4oiy5%2BRy45lCgbfBlqFWVyvLeMETZJVahaLpy2X9IdmfbA8VzUahXusUkiM0C%2Bs6FS6z6AdqADg4hgxx3H%2Bm7Uus7F6%2BolLsxjrj2jlCfgsLucZKH0TVPN1fAeGhnyio4cJBWbVNYGvTJgmC6%2Fh%2FjpLfInusSdMCOEnGEVKJnIHfBAyiftor0YeL3y8Quea%2FRMpOmPn2JA5%2BtCX1bhm41TOsPCYqOIvEbxeK8ybiFrfxl%2Bi6Imi6tYX%2BcLsHcVwzzaBpTDWWH9vf1IMavPQrxtBcLYOrcuJEh%2B3gwXdHNpC1yPoF%2FTIa%2BB%2B0O50NFoyvVEA0f3tPbTDN%2FuHEBjqkAbi%2F5jRMviZVUC%2FTJIpOKeqJfYMiYZ7Uj5CqXSkqb7c4OGcT9fP%2F%2B4Kw%2Bzo1fi3tDa%2FkqzSv3Dk6ZFA6r9KzHdLLMkykq6uCjXQ27ZdFTtG42yeCWfWjfgMTj8KHRRVBaNWkEeBc05hvNXmofYQ3VN6n7Gkm42Pb5TKahWcrceqH93AIgr%2ByWmZptm2yVveJcbnedVDlUY3MREFfySkEq3fjqRmU&X-Amz-Signature=65fdf76148bb3ee8b050e50cb9f64d8c9cea12aefac6d2050e48c93c080b7530&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Fig3 (a)를 통해 본인들이 정의한 high sink dimension value 들이 높은 attention 값을 가지는 애들이였으며, (b) 실제로 visual sink 들을 mask하고 하니 안할때보다 성능이 높았음. (c) attention contribution도 측정했을 때 (실제로 text 답변 만드는 logit에 기여하는 정도) 는 작았음. (d) 를 봐도 w/o sinks 가 noise를 잡아내며 대부분의 sink 들은 background에 존재

## Surplus attentions in visual attention sink : can we recycle them?

(1) image centric-head 를 먼저 뽑고 (2) 해당 head에서 sink token들에 가던 attention을 보아서 non sink token 에게 분배할 예정

- Image centric-head

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/533d4c6e-5941-44c3-bdbd-9e2a9b97aa3f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643OIJKSW%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCbneZjdMjBmANuGlk9pBqG2QlBPOD8%2FSd22DXSbHJ7tgIhANG%2BLix6siOENG8SYanuqtOw8gRSiENNQjA6MbJ6T1y6KogECNT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzBYg3nSkvQ22qQa6sq3AMhHyPsCsEjXCd4RPSkokt4VrGcDE3sPg2D%2BPrfFrB%2BmrCAt%2BrF8a%2BGKpPINze9JbpTj02HjYdsmIW6kPlhslRBl0LPWPJ%2BA%2Bz1iir6Ci6H%2FgfiguDRZc84tzgM4STYUuqeF1Im8mrQAtQRJdxh38onjpYZpzHO14AnZVBKRv1ufqgOEXeXZiAfevASD8dggVm9B9eHiWIMCZ8Vklyhb36FfcFAqo6rAqj35kqsxEGr1YWc9hbV71k%2F7KqMB3FK0fQjyR47kx1vfNz%2B0W03zQpeh%2B3Kom%2FHDh5eZZvkLyN0DyKcVJKT4oiy5%2BRy45lCgbfBlqFWVyvLeMETZJVahaLpy2X9IdmfbA8VzUahXusUkiM0C%2Bs6FS6z6AdqADg4hgxx3H%2Bm7Uus7F6%2BolLsxjrj2jlCfgsLucZKH0TVPN1fAeGhnyio4cJBWbVNYGvTJgmC6%2Fh%2FjpLfInusSdMCOEnGEVKJnIHfBAyiftor0YeL3y8Quea%2FRMpOmPn2JA5%2BtCX1bhm41TOsPCYqOIvEbxeK8ybiFrfxl%2Bi6Imi6tYX%2BcLsHcVwzzaBpTDWWH9vf1IMavPQrxtBcLYOrcuJEh%2B3gwXdHNpC1yPoF%2FTIa%2BB%2B0O50NFoyvVEA0f3tPbTDN%2FuHEBjqkAbi%2F5jRMviZVUC%2FTJIpOKeqJfYMiYZ7Uj5CqXSkqb7c4OGcT9fP%2F%2B4Kw%2Bzo1fi3tDa%2FkqzSv3Dk6ZFA6r9KzHdLLMkykq6uCjXQ27ZdFTtG42yeCWfWjfgMTj8KHRRVBaNWkEeBc05hvNXmofYQ3VN6n7Gkm42Pb5TKahWcrceqH93AIgr%2ByWmZptm2yVveJcbnedVDlUY3MREFfySkEq3fjqRmU&X-Amz-Signature=931b14afd207d4d5dee88852b482e278017b3e448ba1ffdfff99fb3ffc35ca53&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Redistributing attention weights

### Experiments

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/e41b47c8-045d-4dda-a06a-66a45ccfd0ca/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643OIJKSW%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCbneZjdMjBmANuGlk9pBqG2QlBPOD8%2FSd22DXSbHJ7tgIhANG%2BLix6siOENG8SYanuqtOw8gRSiENNQjA6MbJ6T1y6KogECNT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzBYg3nSkvQ22qQa6sq3AMhHyPsCsEjXCd4RPSkokt4VrGcDE3sPg2D%2BPrfFrB%2BmrCAt%2BrF8a%2BGKpPINze9JbpTj02HjYdsmIW6kPlhslRBl0LPWPJ%2BA%2Bz1iir6Ci6H%2FgfiguDRZc84tzgM4STYUuqeF1Im8mrQAtQRJdxh38onjpYZpzHO14AnZVBKRv1ufqgOEXeXZiAfevASD8dggVm9B9eHiWIMCZ8Vklyhb36FfcFAqo6rAqj35kqsxEGr1YWc9hbV71k%2F7KqMB3FK0fQjyR47kx1vfNz%2B0W03zQpeh%2B3Kom%2FHDh5eZZvkLyN0DyKcVJKT4oiy5%2BRy45lCgbfBlqFWVyvLeMETZJVahaLpy2X9IdmfbA8VzUahXusUkiM0C%2Bs6FS6z6AdqADg4hgxx3H%2Bm7Uus7F6%2BolLsxjrj2jlCfgsLucZKH0TVPN1fAeGhnyio4cJBWbVNYGvTJgmC6%2Fh%2FjpLfInusSdMCOEnGEVKJnIHfBAyiftor0YeL3y8Quea%2FRMpOmPn2JA5%2BtCX1bhm41TOsPCYqOIvEbxeK8ybiFrfxl%2Bi6Imi6tYX%2BcLsHcVwzzaBpTDWWH9vf1IMavPQrxtBcLYOrcuJEh%2B3gwXdHNpC1yPoF%2FTIa%2BB%2B0O50NFoyvVEA0f3tPbTDN%2FuHEBjqkAbi%2F5jRMviZVUC%2FTJIpOKeqJfYMiYZ7Uj5CqXSkqb7c4OGcT9fP%2F%2B4Kw%2Bzo1fi3tDa%2FkqzSv3Dk6ZFA6r9KzHdLLMkykq6uCjXQ27ZdFTtG42yeCWfWjfgMTj8KHRRVBaNWkEeBc05hvNXmofYQ3VN6n7Gkm42Pb5TKahWcrceqH93AIgr%2ByWmZptm2yVveJcbnedVDlUY3MREFfySkEq3fjqRmU&X-Amz-Signature=79af27f144937ca3cae4db2286af8d1342f6837f713aa1deedfb746a0f701660&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

(1) VL-task

(2) visual hallucination

(3) vision centric (spatial relationship between objects)

### Ablation studies

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/7789042f-29ef-4193-9f0e-3eabac6e3df0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643OIJKSW%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCbneZjdMjBmANuGlk9pBqG2QlBPOD8%2FSd22DXSbHJ7tgIhANG%2BLix6siOENG8SYanuqtOw8gRSiENNQjA6MbJ6T1y6KogECNT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzBYg3nSkvQ22qQa6sq3AMhHyPsCsEjXCd4RPSkokt4VrGcDE3sPg2D%2BPrfFrB%2BmrCAt%2BrF8a%2BGKpPINze9JbpTj02HjYdsmIW6kPlhslRBl0LPWPJ%2BA%2Bz1iir6Ci6H%2FgfiguDRZc84tzgM4STYUuqeF1Im8mrQAtQRJdxh38onjpYZpzHO14AnZVBKRv1ufqgOEXeXZiAfevASD8dggVm9B9eHiWIMCZ8Vklyhb36FfcFAqo6rAqj35kqsxEGr1YWc9hbV71k%2F7KqMB3FK0fQjyR47kx1vfNz%2B0W03zQpeh%2B3Kom%2FHDh5eZZvkLyN0DyKcVJKT4oiy5%2BRy45lCgbfBlqFWVyvLeMETZJVahaLpy2X9IdmfbA8VzUahXusUkiM0C%2Bs6FS6z6AdqADg4hgxx3H%2Bm7Uus7F6%2BolLsxjrj2jlCfgsLucZKH0TVPN1fAeGhnyio4cJBWbVNYGvTJgmC6%2Fh%2FjpLfInusSdMCOEnGEVKJnIHfBAyiftor0YeL3y8Quea%2FRMpOmPn2JA5%2BtCX1bhm41TOsPCYqOIvEbxeK8ybiFrfxl%2Bi6Imi6tYX%2BcLsHcVwzzaBpTDWWH9vf1IMavPQrxtBcLYOrcuJEh%2B3gwXdHNpC1yPoF%2FTIa%2BB%2B0O50NFoyvVEA0f3tPbTDN%2FuHEBjqkAbi%2F5jRMviZVUC%2FTJIpOKeqJfYMiYZ7Uj5CqXSkqb7c4OGcT9fP%2F%2B4Kw%2Bzo1fi3tDa%2FkqzSv3Dk6ZFA6r9KzHdLLMkykq6uCjXQ27ZdFTtG42yeCWfWjfgMTj8KHRRVBaNWkEeBc05hvNXmofYQ3VN6n7Gkm42Pb5TKahWcrceqH93AIgr%2ByWmZptm2yVveJcbnedVDlUY3MREFfySkEq3fjqRmU&X-Amz-Signature=2b6cf65e5e94c04d53ee86784548956ac5051e75c87b0ac675b31033d537fdfd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- (Table 4) visual non sink ratio 를 정의해서 로 보다 큰 애들의 head 만 살렸었는데 이 과정이 필수적이였음. 

- (Table 5) visual token 내에서만 attention redistribution이 성능이 제일 높음. 

### Appendix

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/4e4b9015-1e0f-49ea-9414-eba1db211bc0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643OIJKSW%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCbneZjdMjBmANuGlk9pBqG2QlBPOD8%2FSd22DXSbHJ7tgIhANG%2BLix6siOENG8SYanuqtOw8gRSiENNQjA6MbJ6T1y6KogECNT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzBYg3nSkvQ22qQa6sq3AMhHyPsCsEjXCd4RPSkokt4VrGcDE3sPg2D%2BPrfFrB%2BmrCAt%2BrF8a%2BGKpPINze9JbpTj02HjYdsmIW6kPlhslRBl0LPWPJ%2BA%2Bz1iir6Ci6H%2FgfiguDRZc84tzgM4STYUuqeF1Im8mrQAtQRJdxh38onjpYZpzHO14AnZVBKRv1ufqgOEXeXZiAfevASD8dggVm9B9eHiWIMCZ8Vklyhb36FfcFAqo6rAqj35kqsxEGr1YWc9hbV71k%2F7KqMB3FK0fQjyR47kx1vfNz%2B0W03zQpeh%2B3Kom%2FHDh5eZZvkLyN0DyKcVJKT4oiy5%2BRy45lCgbfBlqFWVyvLeMETZJVahaLpy2X9IdmfbA8VzUahXusUkiM0C%2Bs6FS6z6AdqADg4hgxx3H%2Bm7Uus7F6%2BolLsxjrj2jlCfgsLucZKH0TVPN1fAeGhnyio4cJBWbVNYGvTJgmC6%2Fh%2FjpLfInusSdMCOEnGEVKJnIHfBAyiftor0YeL3y8Quea%2FRMpOmPn2JA5%2BtCX1bhm41TOsPCYqOIvEbxeK8ybiFrfxl%2Bi6Imi6tYX%2BcLsHcVwzzaBpTDWWH9vf1IMavPQrxtBcLYOrcuJEh%2B3gwXdHNpC1yPoF%2FTIa%2BB%2B0O50NFoyvVEA0f3tPbTDN%2FuHEBjqkAbi%2F5jRMviZVUC%2FTJIpOKeqJfYMiYZ7Uj5CqXSkqb7c4OGcT9fP%2F%2B4Kw%2Bzo1fi3tDa%2FkqzSv3Dk6ZFA6r9KzHdLLMkykq6uCjXQ27ZdFTtG42yeCWfWjfgMTj8KHRRVBaNWkEeBc05hvNXmofYQ3VN6n7Gkm42Pb5TKahWcrceqH93AIgr%2ByWmZptm2yVveJcbnedVDlUY3MREFfySkEq3fjqRmU&X-Amz-Signature=f42067cfd4e793751dc95be30d89c6a02184ec5a02303df43cab286952435814&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/fe2f5c5f-d7d6-45a9-90da-d92dbf86f674/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643OIJKSW%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCbneZjdMjBmANuGlk9pBqG2QlBPOD8%2FSd22DXSbHJ7tgIhANG%2BLix6siOENG8SYanuqtOw8gRSiENNQjA6MbJ6T1y6KogECNT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzBYg3nSkvQ22qQa6sq3AMhHyPsCsEjXCd4RPSkokt4VrGcDE3sPg2D%2BPrfFrB%2BmrCAt%2BrF8a%2BGKpPINze9JbpTj02HjYdsmIW6kPlhslRBl0LPWPJ%2BA%2Bz1iir6Ci6H%2FgfiguDRZc84tzgM4STYUuqeF1Im8mrQAtQRJdxh38onjpYZpzHO14AnZVBKRv1ufqgOEXeXZiAfevASD8dggVm9B9eHiWIMCZ8Vklyhb36FfcFAqo6rAqj35kqsxEGr1YWc9hbV71k%2F7KqMB3FK0fQjyR47kx1vfNz%2B0W03zQpeh%2B3Kom%2FHDh5eZZvkLyN0DyKcVJKT4oiy5%2BRy45lCgbfBlqFWVyvLeMETZJVahaLpy2X9IdmfbA8VzUahXusUkiM0C%2Bs6FS6z6AdqADg4hgxx3H%2Bm7Uus7F6%2BolLsxjrj2jlCfgsLucZKH0TVPN1fAeGhnyio4cJBWbVNYGvTJgmC6%2Fh%2FjpLfInusSdMCOEnGEVKJnIHfBAyiftor0YeL3y8Quea%2FRMpOmPn2JA5%2BtCX1bhm41TOsPCYqOIvEbxeK8ybiFrfxl%2Bi6Imi6tYX%2BcLsHcVwzzaBpTDWWH9vf1IMavPQrxtBcLYOrcuJEh%2B3gwXdHNpC1yPoF%2FTIa%2BB%2B0O50NFoyvVEA0f3tPbTDN%2FuHEBjqkAbi%2F5jRMviZVUC%2FTJIpOKeqJfYMiYZ7Uj5CqXSkqb7c4OGcT9fP%2F%2B4Kw%2Bzo1fi3tDa%2FkqzSv3Dk6ZFA6r9KzHdLLMkykq6uCjXQ27ZdFTtG42yeCWfWjfgMTj8KHRRVBaNWkEeBc05hvNXmofYQ3VN6n7Gkm42Pb5TKahWcrceqH93AIgr%2ByWmZptm2yVveJcbnedVDlUY3MREFfySkEq3fjqRmU&X-Amz-Signature=e88be30adbc503deff0b2acf3262f13fff19e413e2fbfbc1c1be675dc40fd3d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Discussion

- latency가 별로 없으면서 정말 많은 VL task에서 성능이 다 오른건 신기! 다만 해당 방법론 역시 projector을 이용한 vision language model에서만 적용 가능할 것으로 보임. (one-to-one 매칭, instructVL, instructBLIP같은 resampler는 적용 안됨)

- 마지막 table5에서 budet을 아껴서 text에 줬을 때 성능이 안오른건 의외. 직관적으로 필요 없는 잉여물을 준다고 해서 오르는건 아닌것같음
