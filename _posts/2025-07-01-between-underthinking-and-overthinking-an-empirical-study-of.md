---
categories:
- paper-reviews
date: '2025-07-01 00:00:00'
description: 논문 리뷰 - Reasoning 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- llm
- paper-review
- reasoning
thumbnail: assets/img/posts/2025-07-01-between-underthinking-and-overthinking-an-empirical-study-of/thumbnail.jpg
title: 'Between Underthinking and Overthinking: An Empirical Study of Reasoning Length
  and correctness in LLMs'
---

**논문 정보**
- **Date**: 2025-07-01
- **Reviewer**: 준원 장
- **Property**: Reasoning

## 1. Introduction

- Test-time scaling is trending, but **longer reasoning is not always better.**

- Reasoning와 accuracy가 항상 상관관계를 이루지 않는다는 최신연구 존재 (Xie et al., 2025; Jin et al., 2024; Wu et al., 2025)

- 여튼, 이러한 흐름에 따라 최근에 나온 용어

- 그래서 논문은 DeepSeek-1.5B-Distill과 DeepScaler-1.5B-Preview를 가지고 reasoning length와 accuracy를 가지고 체계적인 분석을 수행하겠다!

## 2. Related Work

⇒ lengthy reasoning 문제를 관측하고, 이를 해결하기 위한 학습방법론들

- **Concise thinking**

- **Adaptive thinking**

- **Optimal Thinking**

## 3. Experimental Setting

- Model

- Dataset

- Params.

- Notations

## 4. Sample-Level Analysis

→ q는 고정하고 길이가 다른 10개 completion을 비교해 length와 accuracy의 직접 상관을 조사

- 난이도에 대한 변인을 고정하고 length ↔ accuracy 관계만 볼 수 있음

### Non-Linear Relationship of Sample Length and Correctness

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/f377d385-77b6-42c1-b173-280da3a0e50e/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-07-01_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_12.33.23.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJ4V3RSH%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF3j4AR8F9ZiOZmSaZi5PYKK%2FWMeUo3iocx5Qi48pKbPAiEA57w4oTDC7Sl0IkZQpT2hKYqyrLafgf51ptSsStsPW1oqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL7LfVkNX3mJw0xNzCrcA2qoqaDno7HyjP%2FzDx4mNTpXAVxAqLBxWVFChVFrPj%2FnG7UQAIrJLm%2FvkVzUmzxLa8FGOWDoDxcJOS0yLms6QTA6%2BEmAHap8OjsHP94KtLZduGGOnz4o%2FsjjuPwDqMmvD1FCDb3YAraW1uvHHnQ9ax%2BXmBsP%2Fu01qiSntihOgu1aEMPRBv0FJS1FSUcHpIbTNOfFblP90kmUQVuDELCOl7vd%2Fl260dpPGZ1lD1A8UIHGaWaRdo%2BiFmnimmwY63bw48IbfKr5ggOqdkJKO5uALxQYA2BP948XMZCE997z2%2BON6O%2FWmZpNK5DhdsKTjmjo11hSh%2BCAORyqa8sCQi4LOjaiIBjsqSX1txuZ2L1HCyCBs2rR9XXFA8KhqOvCndDSVuYohtU4yd6%2B4osctZbtzEiexyP9FLfjY2es%2Fa4VUegjoDS%2FDQF3SykT0fXqIer%2BLkqZR7Mp%2BRvM6yJEkwypoEevciMT0Xy%2BZGRA2aBvex%2Bwy12zah4uktyRokruGa8ZZGdgqDIgA4E78spf1M0AjASlSmynMzT3h%2FFXkg%2Ble15X8LI46SkJNplVXgyV3oAOIVX3SEzdUeVSnKSZei6K8ULit1JPJctjF6ANdjBYtH7ZRCBmrHOIhRFV37f5MMz%2F4cQGOqUBfS0sMByPnEcNw0AGalFn%2BJafcOw3dlTq0lPiHvECQKlDcfmiyPblZnE1KRaoZSnLcuTFEhNlRmPpJfDWi8POew0zzyqxxG42f9c062YkGWRhqesFFd5GjQDfYZXPW8XLSrTVycC8n1vHQGjYjMC8pGAnA%2Bg0gADL7pI7xCHkQxU%2FdX1ypE7xvpPJIFgxzPsJtwebLJMhkw%2BB2lchDn3o1sFc3w%2Fz&X-Amz-Signature=02b1a48225b8e8a9bc0694b1429ddcf7cf549f34ddfc138421d879bbd2f15bb5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- L_r, Acc_r: r번째로 짧은 reasoning path의 평균 length/accuracy

- consistent non-monotonic trend 관찰

(준원 뇌피셜: 일단 R1은 (1) MATH 관련 데이터는 외워서 풀것 같기 때문에 temp=1.0, top_p=1로 줘서 decoding path 길어지면 degen 발생했을것으로 예상 (2) GSM8K 유사 난이도는 거의 외웠을것이고 + 상대적으로 쉽기 때문에 1~1.5K thinking budget내로는 거의 비슷할거 같음..)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/fbac1e04-36c1-40da-86cd-4d47d0bac616/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-07-01_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_1.10.30.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJ4V3RSH%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF3j4AR8F9ZiOZmSaZi5PYKK%2FWMeUo3iocx5Qi48pKbPAiEA57w4oTDC7Sl0IkZQpT2hKYqyrLafgf51ptSsStsPW1oqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL7LfVkNX3mJw0xNzCrcA2qoqaDno7HyjP%2FzDx4mNTpXAVxAqLBxWVFChVFrPj%2FnG7UQAIrJLm%2FvkVzUmzxLa8FGOWDoDxcJOS0yLms6QTA6%2BEmAHap8OjsHP94KtLZduGGOnz4o%2FsjjuPwDqMmvD1FCDb3YAraW1uvHHnQ9ax%2BXmBsP%2Fu01qiSntihOgu1aEMPRBv0FJS1FSUcHpIbTNOfFblP90kmUQVuDELCOl7vd%2Fl260dpPGZ1lD1A8UIHGaWaRdo%2BiFmnimmwY63bw48IbfKr5ggOqdkJKO5uALxQYA2BP948XMZCE997z2%2BON6O%2FWmZpNK5DhdsKTjmjo11hSh%2BCAORyqa8sCQi4LOjaiIBjsqSX1txuZ2L1HCyCBs2rR9XXFA8KhqOvCndDSVuYohtU4yd6%2B4osctZbtzEiexyP9FLfjY2es%2Fa4VUegjoDS%2FDQF3SykT0fXqIer%2BLkqZR7Mp%2BRvM6yJEkwypoEevciMT0Xy%2BZGRA2aBvex%2Bwy12zah4uktyRokruGa8ZZGdgqDIgA4E78spf1M0AjASlSmynMzT3h%2FFXkg%2Ble15X8LI46SkJNplVXgyV3oAOIVX3SEzdUeVSnKSZei6K8ULit1JPJctjF6ANdjBYtH7ZRCBmrHOIhRFV37f5MMz%2F4cQGOqUBfS0sMByPnEcNw0AGalFn%2BJafcOw3dlTq0lPiHvECQKlDcfmiyPblZnE1KRaoZSnLcuTFEhNlRmPpJfDWi8POew0zzyqxxG42f9c062YkGWRhqesFFd5GjQDfYZXPW8XLSrTVycC8n1vHQGjYjMC8pGAnA%2Bg0gADL7pI7xCHkQxU%2FdX1ypE7xvpPJIFgxzPsJtwebLJMhkw%2BB2lchDn3o1sFc3w%2Fz&X-Amz-Signature=dee75d56190d60594f8053dcac0a0566000ec63f8913ef948ecb4a4fe63c5b2b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 초록: q에 대한 정답 completion중 가장 짧은 거

- 파랑: q에 대한 정답 completion중 가장 긴거

- 빨강: q에 대한 오답 completion중 가장 짧은 거

- 노랑: q에 대한 정답 completion중 가장 긴거

- R1-Preview는 MATH, GSM8K 모두 80% 이상의 질문에서 가장 짧은 샘플로 정답을 생성할 수 있음을 보임

- most length한 completion중에 correct response도 있지만 incorrect response도 존재 (논문 해석 이상..)

## 5. Question-Level Analysis

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/71468c9e-5f26-4dd2-89be-54b89681ea8e/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-07-01_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_5.44.47.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJ4V3RSH%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF3j4AR8F9ZiOZmSaZi5PYKK%2FWMeUo3iocx5Qi48pKbPAiEA57w4oTDC7Sl0IkZQpT2hKYqyrLafgf51ptSsStsPW1oqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL7LfVkNX3mJw0xNzCrcA2qoqaDno7HyjP%2FzDx4mNTpXAVxAqLBxWVFChVFrPj%2FnG7UQAIrJLm%2FvkVzUmzxLa8FGOWDoDxcJOS0yLms6QTA6%2BEmAHap8OjsHP94KtLZduGGOnz4o%2FsjjuPwDqMmvD1FCDb3YAraW1uvHHnQ9ax%2BXmBsP%2Fu01qiSntihOgu1aEMPRBv0FJS1FSUcHpIbTNOfFblP90kmUQVuDELCOl7vd%2Fl260dpPGZ1lD1A8UIHGaWaRdo%2BiFmnimmwY63bw48IbfKr5ggOqdkJKO5uALxQYA2BP948XMZCE997z2%2BON6O%2FWmZpNK5DhdsKTjmjo11hSh%2BCAORyqa8sCQi4LOjaiIBjsqSX1txuZ2L1HCyCBs2rR9XXFA8KhqOvCndDSVuYohtU4yd6%2B4osctZbtzEiexyP9FLfjY2es%2Fa4VUegjoDS%2FDQF3SykT0fXqIer%2BLkqZR7Mp%2BRvM6yJEkwypoEevciMT0Xy%2BZGRA2aBvex%2Bwy12zah4uktyRokruGa8ZZGdgqDIgA4E78spf1M0AjASlSmynMzT3h%2FFXkg%2Ble15X8LI46SkJNplVXgyV3oAOIVX3SEzdUeVSnKSZei6K8ULit1JPJctjF6ANdjBYtH7ZRCBmrHOIhRFV37f5MMz%2F4cQGOqUBfS0sMByPnEcNw0AGalFn%2BJafcOw3dlTq0lPiHvECQKlDcfmiyPblZnE1KRaoZSnLcuTFEhNlRmPpJfDWi8POew0zzyqxxG42f9c062YkGWRhqesFFd5GjQDfYZXPW8XLSrTVycC8n1vHQGjYjMC8pGAnA%2Bg0gADL7pI7xCHkQxU%2FdX1ypE7xvpPJIFgxzPsJtwebLJMhkw%2BB2lchDn3o1sFc3w%2Fz&X-Amz-Signature=e519f1edd7b8b2056dad1218e0f1f3f4e30868afabaf1308f4def72df21b0a2c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 단순하게 문제 난이도를 틀림 여부로 볼때, incorrect response가 어떤 조합에서든 response 길이가 더 길었음

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/a0c41355-ea1e-4a11-9f19-cb3b980f4c97/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-07-01_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_5.49.19.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJ4V3RSH%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF3j4AR8F9ZiOZmSaZi5PYKK%2FWMeUo3iocx5Qi48pKbPAiEA57w4oTDC7Sl0IkZQpT2hKYqyrLafgf51ptSsStsPW1oqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL7LfVkNX3mJw0xNzCrcA2qoqaDno7HyjP%2FzDx4mNTpXAVxAqLBxWVFChVFrPj%2FnG7UQAIrJLm%2FvkVzUmzxLa8FGOWDoDxcJOS0yLms6QTA6%2BEmAHap8OjsHP94KtLZduGGOnz4o%2FsjjuPwDqMmvD1FCDb3YAraW1uvHHnQ9ax%2BXmBsP%2Fu01qiSntihOgu1aEMPRBv0FJS1FSUcHpIbTNOfFblP90kmUQVuDELCOl7vd%2Fl260dpPGZ1lD1A8UIHGaWaRdo%2BiFmnimmwY63bw48IbfKr5ggOqdkJKO5uALxQYA2BP948XMZCE997z2%2BON6O%2FWmZpNK5DhdsKTjmjo11hSh%2BCAORyqa8sCQi4LOjaiIBjsqSX1txuZ2L1HCyCBs2rR9XXFA8KhqOvCndDSVuYohtU4yd6%2B4osctZbtzEiexyP9FLfjY2es%2Fa4VUegjoDS%2FDQF3SykT0fXqIer%2BLkqZR7Mp%2BRvM6yJEkwypoEevciMT0Xy%2BZGRA2aBvex%2Bwy12zah4uktyRokruGa8ZZGdgqDIgA4E78spf1M0AjASlSmynMzT3h%2FFXkg%2Ble15X8LI46SkJNplVXgyV3oAOIVX3SEzdUeVSnKSZei6K8ULit1JPJctjF6ANdjBYtH7ZRCBmrHOIhRFV37f5MMz%2F4cQGOqUBfS0sMByPnEcNw0AGalFn%2BJafcOw3dlTq0lPiHvECQKlDcfmiyPblZnE1KRaoZSnLcuTFEhNlRmPpJfDWi8POew0zzyqxxG42f9c062YkGWRhqesFFd5GjQDfYZXPW8XLSrTVycC8n1vHQGjYjMC8pGAnA%2Bg0gADL7pI7xCHkQxU%2FdX1ypE7xvpPJIFgxzPsJtwebLJMhkw%2BB2lchDn3o1sFc3w%2Fz&X-Amz-Signature=16bbda1ed4239231749f90cfb62cec008af8c78989ebec6296724b8990b4bb3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- N-completion별로 difficulty를 분류

⇒ 그러나 (1) 문제가 어려워서 lengthy한지 (2) length해져서 틀린건지 판단이 어려움

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/6c8cd3cd-6aa3-4c46-b883-68b4246ceefc/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-07-01_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_6.07.59.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJ4V3RSH%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF3j4AR8F9ZiOZmSaZi5PYKK%2FWMeUo3iocx5Qi48pKbPAiEA57w4oTDC7Sl0IkZQpT2hKYqyrLafgf51ptSsStsPW1oqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL7LfVkNX3mJw0xNzCrcA2qoqaDno7HyjP%2FzDx4mNTpXAVxAqLBxWVFChVFrPj%2FnG7UQAIrJLm%2FvkVzUmzxLa8FGOWDoDxcJOS0yLms6QTA6%2BEmAHap8OjsHP94KtLZduGGOnz4o%2FsjjuPwDqMmvD1FCDb3YAraW1uvHHnQ9ax%2BXmBsP%2Fu01qiSntihOgu1aEMPRBv0FJS1FSUcHpIbTNOfFblP90kmUQVuDELCOl7vd%2Fl260dpPGZ1lD1A8UIHGaWaRdo%2BiFmnimmwY63bw48IbfKr5ggOqdkJKO5uALxQYA2BP948XMZCE997z2%2BON6O%2FWmZpNK5DhdsKTjmjo11hSh%2BCAORyqa8sCQi4LOjaiIBjsqSX1txuZ2L1HCyCBs2rR9XXFA8KhqOvCndDSVuYohtU4yd6%2B4osctZbtzEiexyP9FLfjY2es%2Fa4VUegjoDS%2FDQF3SykT0fXqIer%2BLkqZR7Mp%2BRvM6yJEkwypoEevciMT0Xy%2BZGRA2aBvex%2Bwy12zah4uktyRokruGa8ZZGdgqDIgA4E78spf1M0AjASlSmynMzT3h%2FFXkg%2Ble15X8LI46SkJNplVXgyV3oAOIVX3SEzdUeVSnKSZei6K8ULit1JPJctjF6ANdjBYtH7ZRCBmrHOIhRFV37f5MMz%2F4cQGOqUBfS0sMByPnEcNw0AGalFn%2BJafcOw3dlTq0lPiHvECQKlDcfmiyPblZnE1KRaoZSnLcuTFEhNlRmPpJfDWi8POew0zzyqxxG42f9c062YkGWRhqesFFd5GjQDfYZXPW8XLSrTVycC8n1vHQGjYjMC8pGAnA%2Bg0gADL7pI7xCHkQxU%2FdX1ypE7xvpPJIFgxzPsJtwebLJMhkw%2BB2lchDn3o1sFc3w%2Fz&X-Amz-Signature=0f668a6a254bd030a63e77e184e2ed5fc1319d3bca653ab1156ed1c6bf6e2866&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Q^{easy}_{\cap} = Q^{easy}_{i} \cap Q^{easy}_{j}

- Q^{easy}_{i/j} = Q^{easy}_{i} /  Q^{easy}_{j} > M_i  에서만 쉬운 문제

- Q^{easy}_{j/i} = Q^{easy}_{j} /  Q^{easy}_{i} > M_j에서만 쉬운 문제 

- 보편적으로 쉬운 문제가 아니라 another model’s advantage set (다른모델에서 쉬운 문제)에서 오히려 lengthy generation을 보임

- signficant로 보면 M_i  → M_j-Adv Set을 풀때 보다 lengthy해짐

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/b272f5c0-6437-4a3b-8b62-31be1fb32ee4/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-07-01_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_6.32.17.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJ4V3RSH%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF3j4AR8F9ZiOZmSaZi5PYKK%2FWMeUo3iocx5Qi48pKbPAiEA57w4oTDC7Sl0IkZQpT2hKYqyrLafgf51ptSsStsPW1oqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL7LfVkNX3mJw0xNzCrcA2qoqaDno7HyjP%2FzDx4mNTpXAVxAqLBxWVFChVFrPj%2FnG7UQAIrJLm%2FvkVzUmzxLa8FGOWDoDxcJOS0yLms6QTA6%2BEmAHap8OjsHP94KtLZduGGOnz4o%2FsjjuPwDqMmvD1FCDb3YAraW1uvHHnQ9ax%2BXmBsP%2Fu01qiSntihOgu1aEMPRBv0FJS1FSUcHpIbTNOfFblP90kmUQVuDELCOl7vd%2Fl260dpPGZ1lD1A8UIHGaWaRdo%2BiFmnimmwY63bw48IbfKr5ggOqdkJKO5uALxQYA2BP948XMZCE997z2%2BON6O%2FWmZpNK5DhdsKTjmjo11hSh%2BCAORyqa8sCQi4LOjaiIBjsqSX1txuZ2L1HCyCBs2rR9XXFA8KhqOvCndDSVuYohtU4yd6%2B4osctZbtzEiexyP9FLfjY2es%2Fa4VUegjoDS%2FDQF3SykT0fXqIer%2BLkqZR7Mp%2BRvM6yJEkwypoEevciMT0Xy%2BZGRA2aBvex%2Bwy12zah4uktyRokruGa8ZZGdgqDIgA4E78spf1M0AjASlSmynMzT3h%2FFXkg%2Ble15X8LI46SkJNplVXgyV3oAOIVX3SEzdUeVSnKSZei6K8ULit1JPJctjF6ANdjBYtH7ZRCBmrHOIhRFV37f5MMz%2F4cQGOqUBfS0sMByPnEcNw0AGalFn%2BJafcOw3dlTq0lPiHvECQKlDcfmiyPblZnE1KRaoZSnLcuTFEhNlRmPpJfDWi8POew0zzyqxxG42f9c062YkGWRhqesFFd5GjQDfYZXPW8XLSrTVycC8n1vHQGjYjMC8pGAnA%2Bg0gADL7pI7xCHkQxU%2FdX1ypE7xvpPJIFgxzPsJtwebLJMhkw%2BB2lchDn3o1sFc3w%2Fz&X-Amz-Signature=0ad296a782d2b44c59ead865655e0be992e30ed0aa645f701188596228055cb9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- hard question에서는 Q^{hard}_{\cap}에서 보다 another model’s advantage set에서 lengthy해질 것을 기대했으나 그렇진 않음

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/9e383a99-5093-4f6d-b4b5-b45916cafabd/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-07-01_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_6.36.41.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJ4V3RSH%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF3j4AR8F9ZiOZmSaZi5PYKK%2FWMeUo3iocx5Qi48pKbPAiEA57w4oTDC7Sl0IkZQpT2hKYqyrLafgf51ptSsStsPW1oqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL7LfVkNX3mJw0xNzCrcA2qoqaDno7HyjP%2FzDx4mNTpXAVxAqLBxWVFChVFrPj%2FnG7UQAIrJLm%2FvkVzUmzxLa8FGOWDoDxcJOS0yLms6QTA6%2BEmAHap8OjsHP94KtLZduGGOnz4o%2FsjjuPwDqMmvD1FCDb3YAraW1uvHHnQ9ax%2BXmBsP%2Fu01qiSntihOgu1aEMPRBv0FJS1FSUcHpIbTNOfFblP90kmUQVuDELCOl7vd%2Fl260dpPGZ1lD1A8UIHGaWaRdo%2BiFmnimmwY63bw48IbfKr5ggOqdkJKO5uALxQYA2BP948XMZCE997z2%2BON6O%2FWmZpNK5DhdsKTjmjo11hSh%2BCAORyqa8sCQi4LOjaiIBjsqSX1txuZ2L1HCyCBs2rR9XXFA8KhqOvCndDSVuYohtU4yd6%2B4osctZbtzEiexyP9FLfjY2es%2Fa4VUegjoDS%2FDQF3SykT0fXqIer%2BLkqZR7Mp%2BRvM6yJEkwypoEevciMT0Xy%2BZGRA2aBvex%2Bwy12zah4uktyRokruGa8ZZGdgqDIgA4E78spf1M0AjASlSmynMzT3h%2FFXkg%2Ble15X8LI46SkJNplVXgyV3oAOIVX3SEzdUeVSnKSZei6K8ULit1JPJctjF6ANdjBYtH7ZRCBmrHOIhRFV37f5MMz%2F4cQGOqUBfS0sMByPnEcNw0AGalFn%2BJafcOw3dlTq0lPiHvECQKlDcfmiyPblZnE1KRaoZSnLcuTFEhNlRmPpJfDWi8POew0zzyqxxG42f9c062YkGWRhqesFFd5GjQDfYZXPW8XLSrTVycC8n1vHQGjYjMC8pGAnA%2Bg0gADL7pI7xCHkQxU%2FdX1ypE7xvpPJIFgxzPsJtwebLJMhkw%2BB2lchDn3o1sFc3w%2Fz&X-Amz-Signature=0eea511f01f7ecd02abfa22d411239bf7fc8579debf967479de5e8efafe1b08f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- (어떻게 실험했는지는 모르겠는데..) token length가 짧아질수록 accuracy가 올라간다. 

- 위에 실험을 기반으로 token legnth가 짧으니 확률적으로 당연히 accuracy가 높은 답변일수록 PPL도 낮을 것

## 6. Effect of Length Preference Optimization

- 지금까지 지적된 문제들을 해결하기 위해 correct/length-balanced reward-based RL등이 소개되었음

- 이를 위해 이전에 drive-out한 직관들을 가지고 간단한 실험을 진행.

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/4a1d6e98-90ef-46ac-9f19-1bf7410ba26a/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-07-01_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_6.53.47.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJ4V3RSH%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF3j4AR8F9ZiOZmSaZi5PYKK%2FWMeUo3iocx5Qi48pKbPAiEA57w4oTDC7Sl0IkZQpT2hKYqyrLafgf51ptSsStsPW1oqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL7LfVkNX3mJw0xNzCrcA2qoqaDno7HyjP%2FzDx4mNTpXAVxAqLBxWVFChVFrPj%2FnG7UQAIrJLm%2FvkVzUmzxLa8FGOWDoDxcJOS0yLms6QTA6%2BEmAHap8OjsHP94KtLZduGGOnz4o%2FsjjuPwDqMmvD1FCDb3YAraW1uvHHnQ9ax%2BXmBsP%2Fu01qiSntihOgu1aEMPRBv0FJS1FSUcHpIbTNOfFblP90kmUQVuDELCOl7vd%2Fl260dpPGZ1lD1A8UIHGaWaRdo%2BiFmnimmwY63bw48IbfKr5ggOqdkJKO5uALxQYA2BP948XMZCE997z2%2BON6O%2FWmZpNK5DhdsKTjmjo11hSh%2BCAORyqa8sCQi4LOjaiIBjsqSX1txuZ2L1HCyCBs2rR9XXFA8KhqOvCndDSVuYohtU4yd6%2B4osctZbtzEiexyP9FLfjY2es%2Fa4VUegjoDS%2FDQF3SykT0fXqIer%2BLkqZR7Mp%2BRvM6yJEkwypoEevciMT0Xy%2BZGRA2aBvex%2Bwy12zah4uktyRokruGa8ZZGdgqDIgA4E78spf1M0AjASlSmynMzT3h%2FFXkg%2Ble15X8LI46SkJNplVXgyV3oAOIVX3SEzdUeVSnKSZei6K8ULit1JPJctjF6ANdjBYtH7ZRCBmrHOIhRFV37f5MMz%2F4cQGOqUBfS0sMByPnEcNw0AGalFn%2BJafcOw3dlTq0lPiHvECQKlDcfmiyPblZnE1KRaoZSnLcuTFEhNlRmPpJfDWi8POew0zzyqxxG42f9c062YkGWRhqesFFd5GjQDfYZXPW8XLSrTVycC8n1vHQGjYjMC8pGAnA%2Bg0gADL7pI7xCHkQxU%2FdX1ypE7xvpPJIFgxzPsJtwebLJMhkw%2BB2lchDn3o1sFc3w%2Fz&X-Amz-Signature=4f0e58b394a60dd6522e95b665f568d15d04d12273777ad188a9e9379cf2a70f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- training step을 반복할수록 accuracy 변동폭은 적으나 average token length 30%에서 60% 감소

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/f7a55473-abc1-4d8c-811b-3922246b68a3/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-07-01_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_6.56.30.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJ4V3RSH%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF3j4AR8F9ZiOZmSaZi5PYKK%2FWMeUo3iocx5Qi48pKbPAiEA57w4oTDC7Sl0IkZQpT2hKYqyrLafgf51ptSsStsPW1oqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL7LfVkNX3mJw0xNzCrcA2qoqaDno7HyjP%2FzDx4mNTpXAVxAqLBxWVFChVFrPj%2FnG7UQAIrJLm%2FvkVzUmzxLa8FGOWDoDxcJOS0yLms6QTA6%2BEmAHap8OjsHP94KtLZduGGOnz4o%2FsjjuPwDqMmvD1FCDb3YAraW1uvHHnQ9ax%2BXmBsP%2Fu01qiSntihOgu1aEMPRBv0FJS1FSUcHpIbTNOfFblP90kmUQVuDELCOl7vd%2Fl260dpPGZ1lD1A8UIHGaWaRdo%2BiFmnimmwY63bw48IbfKr5ggOqdkJKO5uALxQYA2BP948XMZCE997z2%2BON6O%2FWmZpNK5DhdsKTjmjo11hSh%2BCAORyqa8sCQi4LOjaiIBjsqSX1txuZ2L1HCyCBs2rR9XXFA8KhqOvCndDSVuYohtU4yd6%2B4osctZbtzEiexyP9FLfjY2es%2Fa4VUegjoDS%2FDQF3SykT0fXqIer%2BLkqZR7Mp%2BRvM6yJEkwypoEevciMT0Xy%2BZGRA2aBvex%2Bwy12zah4uktyRokruGa8ZZGdgqDIgA4E78spf1M0AjASlSmynMzT3h%2FFXkg%2Ble15X8LI46SkJNplVXgyV3oAOIVX3SEzdUeVSnKSZei6K8ULit1JPJctjF6ANdjBYtH7ZRCBmrHOIhRFV37f5MMz%2F4cQGOqUBfS0sMByPnEcNw0AGalFn%2BJafcOw3dlTq0lPiHvECQKlDcfmiyPblZnE1KRaoZSnLcuTFEhNlRmPpJfDWi8POew0zzyqxxG42f9c062YkGWRhqesFFd5GjQDfYZXPW8XLSrTVycC8n1vHQGjYjMC8pGAnA%2Bg0gADL7pI7xCHkQxU%2FdX1ypE7xvpPJIFgxzPsJtwebLJMhkw%2BB2lchDn3o1sFc3w%2Fz&X-Amz-Signature=17ae5b8fb3c47e13f24872be5e9640d98be2575209f535a67a1153683b9e7a7d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- SimPO가 진행됨에 따라 incorrect response의 생성이 줄어들었다.

## 7. Conclusion &  Limitation

- generation length와 final answer correctness에 대해서 심도 있는 분석

- LM의 크기가 너무 작고, benchmark가 너무 쉬움…
