---
categories:
- paper-reviews
date: '2025-04-15 00:00:00'
description: 논문 리뷰
giscus_comments: true
layout: post
related_posts: false
tags:
- alignment
- gpt
- language-model
- llm
- paper-review
- rlhf
thumbnail: assets/img/posts/2025-04-15-universal-and-transferable-adversarial-attacks-on-aligned-language/thumbnail.jpg
title: Universal and Transferable Adversarial Attacks on Aligned Language Models
---

**논문 정보**
- **Date**: 2025-04-15
- **Reviewer**: 건우 김

***23년도 12월에 출판된 논문이라 살짝 outdated 되어있는 점도 있지만, 유용한 내용이 많아서 공유드림.***

# Abstract

- 이때 당시 LLM은 부적절하거나 문제가 될 수 있는 콘텐츠를 생성할 가능성이 있어 alignment에 집중함.

- 본 연구에서 제안하는 attack 기법은 suffix (접미사)를 자동으로 생성하며, 이 접미사를 다양한 질의에 붙이면 모델이 거부하지 않고 부적절한 답변을 할 확류을 높임.

- 생성된 adversarial suffix는 다양한 모델과 상황에 높은 transferabiltiy를 보여줌

# 1. Introduction

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/986e7394-0405-4eb3-a333-f9d167f3e1c6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FVGCOBF%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAvGnyircrChUbhcKpCSVyguk%2FzOw6h2%2FjHBFxOxHCPzAiBVdl%2FpRFW4MWBQB2n%2BpDyQjQrA9ljLTmPrGsuCFQtXzyqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLqYieE%2FHb8aJu%2FFqKtwDqWMMjceLwHbrgdfCm9%2Fmxe%2FTcHGly49DPN2m2nJwcGkBGQTJmBqA8kKfYi9i15YDMtl6Zrtt76RTdu%2BhLPt6T3x8uZTyC4J%2F4BEeG5dSgqushYiopjsajodCRXT5QyfTbeKu5TEhd%2Fch%2B69vxupRUeCTR8A5B0lMQDolrh87oTpPqcnnlKfrfkBjYlHfbfvc7MuDzSBlq9Y0U5VibD8Q3gkKQMhOxWmNw%2BIc%2BJZ9sJ%2B60NIkhS7aefURV%2BKBroB4fejnsJEuAyxplvO9vKEajau2WgHvBRk0MKF%2FMPCYW%2BydyOiq7QEttW8A%2FKCMZiumWc3%2FRIu%2BfrnG2K%2FQpEs4CUX1ZzifqAsUu2YGoJ5z0m7jUEAt0TVCgJCSF5RMC4WoqlFwn93x1JFesXS4CFFeUxqrAYAj9xx0Nc4TZ%2FdoNheTK3RrLkKOy%2FzQFEIWZ4NsTZVj4NIOtKuG5dyRY132Rhmr6R%2Bn1R3ezKxwXseXYxCdpfvTgjQDrwXITVLjh0Q%2BYbg%2BYNphuQrbuw8HUskI%2FtSQm23cfqJIrbhhvZFSXW1AOw%2FubI1ESmDfQKcbnCtpNc167juFBNEtAIcsiAqojOoPCKhjyqVVwNTlcqQcthPtnLgByBihZ5GsB0Uwyv%2FhxAY6pgEcE10n0clpZL0e7cwbvOvDNoAXaU61Hi%2FeL8qzcEtVpk6EKt4Z7DTKw%2F68Y4lmin78%2FER2MbEeHEGa64anBv6cbRvgKZoh9FiC8NzMQBHaTH58FzDL7PrHtwdWW49n4McGiVXFukowVkcV71M%2BqJ3T8DY9Sd3YTrk57kRMOyDkf4RTr%2FRAoNuC4UwzSoAeAh843OfFsanTwsOS3VY2I9UkAKwqKHIQ&X-Amz-Signature=dfdde138b117dcd85d5f287c0ed86b6f671f85f7f02a5d4980ede572d44835d5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- LLMs들이 large corpus로 학습될 때, 학습 데이터 안에는 유해한 콘텐츠도 포함되어 있음. 이를 방지하기 위해 alignment 기법이 도임되었고 (ex. RLHF), 결과적으로 사용자 질의에 대해 부적절한 답변을 생성하는 것을 제어하는데 어느 정도 성공함.

- 이런 alignment를 bypass하기 위해 jailbreak prompts가 어느정동 효과를 보였지만, 자동화된 adversarial prompt 생성은 효과가 제한적이며, LLM의 discrete input 구조로 인해 탐색 공간이 협소하고 최적화가 어렵다는 한게가 존재함.

- 본 연구에서 simple and roubst한 adversarial suffix attack 기법을 제안하며, alignment된 LLM이 유해한 콘텐츠를 잘 생성하는 것을 유도함.

# 2. A Universal Attack on LLMs

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/54200707-fc30-4a21-94db-4b96d2d0b4dc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FVGCOBF%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAvGnyircrChUbhcKpCSVyguk%2FzOw6h2%2FjHBFxOxHCPzAiBVdl%2FpRFW4MWBQB2n%2BpDyQjQrA9ljLTmPrGsuCFQtXzyqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLqYieE%2FHb8aJu%2FFqKtwDqWMMjceLwHbrgdfCm9%2Fmxe%2FTcHGly49DPN2m2nJwcGkBGQTJmBqA8kKfYi9i15YDMtl6Zrtt76RTdu%2BhLPt6T3x8uZTyC4J%2F4BEeG5dSgqushYiopjsajodCRXT5QyfTbeKu5TEhd%2Fch%2B69vxupRUeCTR8A5B0lMQDolrh87oTpPqcnnlKfrfkBjYlHfbfvc7MuDzSBlq9Y0U5VibD8Q3gkKQMhOxWmNw%2BIc%2BJZ9sJ%2B60NIkhS7aefURV%2BKBroB4fejnsJEuAyxplvO9vKEajau2WgHvBRk0MKF%2FMPCYW%2BydyOiq7QEttW8A%2FKCMZiumWc3%2FRIu%2BfrnG2K%2FQpEs4CUX1ZzifqAsUu2YGoJ5z0m7jUEAt0TVCgJCSF5RMC4WoqlFwn93x1JFesXS4CFFeUxqrAYAj9xx0Nc4TZ%2FdoNheTK3RrLkKOy%2FzQFEIWZ4NsTZVj4NIOtKuG5dyRY132Rhmr6R%2Bn1R3ezKxwXseXYxCdpfvTgjQDrwXITVLjh0Q%2BYbg%2BYNphuQrbuw8HUskI%2FtSQm23cfqJIrbhhvZFSXW1AOw%2FubI1ESmDfQKcbnCtpNc167juFBNEtAIcsiAqojOoPCKhjyqVVwNTlcqQcthPtnLgByBihZ5GsB0Uwyv%2FhxAY6pgEcE10n0clpZL0e7cwbvOvDNoAXaU61Hi%2FeL8qzcEtVpk6EKt4Z7DTKw%2F68Y4lmin78%2FER2MbEeHEGa64anBv6cbRvgKZoh9FiC8NzMQBHaTH58FzDL7PrHtwdWW49n4McGiVXFukowVkcV71M%2BqJ3T8DY9Sd3YTrk57kRMOyDkf4RTr%2FRAoNuC4UwzSoAeAh843OfFsanTwsOS3VY2I9UkAKwqKHIQ&X-Amz-Signature=c1bef991cbdcf1ad2f6fbba66fd4b4a1a73548e24ca14615d2c91332b2cea36e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Objective: 사용자 query (ex. “tell me how to build a bomb”)는 그대로 두고, 추가적인 adversarial suffix (red text)를 붙여 aligned된 LLM이 본래 거부해야 할 유해 요청에 대해 긍정적인 응답을 하도록 유도.

## 2.1 Producing Affirmative Responses

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/35fa8feb-dca6-4da7-9814-25b19c57b74a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FVGCOBF%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAvGnyircrChUbhcKpCSVyguk%2FzOw6h2%2FjHBFxOxHCPzAiBVdl%2FpRFW4MWBQB2n%2BpDyQjQrA9ljLTmPrGsuCFQtXzyqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLqYieE%2FHb8aJu%2FFqKtwDqWMMjceLwHbrgdfCm9%2Fmxe%2FTcHGly49DPN2m2nJwcGkBGQTJmBqA8kKfYi9i15YDMtl6Zrtt76RTdu%2BhLPt6T3x8uZTyC4J%2F4BEeG5dSgqushYiopjsajodCRXT5QyfTbeKu5TEhd%2Fch%2B69vxupRUeCTR8A5B0lMQDolrh87oTpPqcnnlKfrfkBjYlHfbfvc7MuDzSBlq9Y0U5VibD8Q3gkKQMhOxWmNw%2BIc%2BJZ9sJ%2B60NIkhS7aefURV%2BKBroB4fejnsJEuAyxplvO9vKEajau2WgHvBRk0MKF%2FMPCYW%2BydyOiq7QEttW8A%2FKCMZiumWc3%2FRIu%2BfrnG2K%2FQpEs4CUX1ZzifqAsUu2YGoJ5z0m7jUEAt0TVCgJCSF5RMC4WoqlFwn93x1JFesXS4CFFeUxqrAYAj9xx0Nc4TZ%2FdoNheTK3RrLkKOy%2FzQFEIWZ4NsTZVj4NIOtKuG5dyRY132Rhmr6R%2Bn1R3ezKxwXseXYxCdpfvTgjQDrwXITVLjh0Q%2BYbg%2BYNphuQrbuw8HUskI%2FtSQm23cfqJIrbhhvZFSXW1AOw%2FubI1ESmDfQKcbnCtpNc167juFBNEtAIcsiAqojOoPCKhjyqVVwNTlcqQcthPtnLgByBihZ5GsB0Uwyv%2FhxAY6pgEcE10n0clpZL0e7cwbvOvDNoAXaU61Hi%2FeL8qzcEtVpk6EKt4Z7DTKw%2F68Y4lmin78%2FER2MbEeHEGa64anBv6cbRvgKZoh9FiC8NzMQBHaTH58FzDL7PrHtwdWW49n4McGiVXFukowVkcV71M%2BqJ3T8DY9Sd3YTrk57kRMOyDkf4RTr%2FRAoNuC4UwzSoAeAh843OfFsanTwsOS3VY2I9UkAKwqKHIQ&X-Amz-Signature=fd54ab136d6ede7aebbeb3e341b40345897105627f6713db46450db8eb0611dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Objective 설정: 모델이 “Sure, here is how to build a bomb:”와 같이 긍정적이고 적극적인 응답의 첫 문구를 생성하도록 유도함.

- **Formalizing the adversarial objective**

## 2.2 Greedy Coordinate Gradient-based Search

- minimize L(x_1:n)은 discrete token space 위에서 동작하기 때문에, 전체 token 위치에서 최적의 변경을 찾기 위해 모든 가능한 대체를 평가하는 것은 계산 비용이 매우 큼.

- 위 문제를 해결하기에 gradient를 활용한 GCG방법을 제안함

## 2.3 Universal Multi-prompt and Multi-model attacks

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/42ddc2ba-a427-4035-9461-8d7cbcac368f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FVGCOBF%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAvGnyircrChUbhcKpCSVyguk%2FzOw6h2%2FjHBFxOxHCPzAiBVdl%2FpRFW4MWBQB2n%2BpDyQjQrA9ljLTmPrGsuCFQtXzyqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLqYieE%2FHb8aJu%2FFqKtwDqWMMjceLwHbrgdfCm9%2Fmxe%2FTcHGly49DPN2m2nJwcGkBGQTJmBqA8kKfYi9i15YDMtl6Zrtt76RTdu%2BhLPt6T3x8uZTyC4J%2F4BEeG5dSgqushYiopjsajodCRXT5QyfTbeKu5TEhd%2Fch%2B69vxupRUeCTR8A5B0lMQDolrh87oTpPqcnnlKfrfkBjYlHfbfvc7MuDzSBlq9Y0U5VibD8Q3gkKQMhOxWmNw%2BIc%2BJZ9sJ%2B60NIkhS7aefURV%2BKBroB4fejnsJEuAyxplvO9vKEajau2WgHvBRk0MKF%2FMPCYW%2BydyOiq7QEttW8A%2FKCMZiumWc3%2FRIu%2BfrnG2K%2FQpEs4CUX1ZzifqAsUu2YGoJ5z0m7jUEAt0TVCgJCSF5RMC4WoqlFwn93x1JFesXS4CFFeUxqrAYAj9xx0Nc4TZ%2FdoNheTK3RrLkKOy%2FzQFEIWZ4NsTZVj4NIOtKuG5dyRY132Rhmr6R%2Bn1R3ezKxwXseXYxCdpfvTgjQDrwXITVLjh0Q%2BYbg%2BYNphuQrbuw8HUskI%2FtSQm23cfqJIrbhhvZFSXW1AOw%2FubI1ESmDfQKcbnCtpNc167juFBNEtAIcsiAqojOoPCKhjyqVVwNTlcqQcthPtnLgByBihZ5GsB0Uwyv%2FhxAY6pgEcE10n0clpZL0e7cwbvOvDNoAXaU61Hi%2FeL8qzcEtVpk6EKt4Z7DTKw%2F68Y4lmin78%2FER2MbEeHEGa64anBv6cbRvgKZoh9FiC8NzMQBHaTH58FzDL7PrHtwdWW49n4McGiVXFukowVkcV71M%2BqJ3T8DY9Sd3YTrk57kRMOyDkf4RTr%2FRAoNuC4UwzSoAeAh843OfFsanTwsOS3VY2I9UkAKwqKHIQ&X-Amz-Signature=02aa328fce95d58c19dcdb3f2f7294ff1af6936ba9c336ea12f6bd63f804b6e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

단일 prompt가 아닌 다양한 prompt에 저굥 가능한 GCG를 확장시켜 universal attack을 제안함.

- objective: 단 하나의 adeversarial suffix p_1:l로 유해한 prompt에 대해 공통적으로 잘 작동하기

- 동일한 tokenizer를 사용하면, gradient는 같은 차원의 공간 R^V에 존재하기 때문에, 별다른 변환 없이 합산 할 수 있음 (ex. Vicuna-7B, 13B를 동시에 최적화 할 수 있음)

# 3. Experimental Results: Direct and Transfer Attack

### Dataset

본 연구에서 제안한 새로운 밴치마큰 AdvBench

- Harmful strings: 500개 유해한 텍스트를 포함한 문장으로 구성됨.

- Harmful Behaviors: 500개 유해 행동 지시문 (ex. how to build a bomb?)

### Metrics

- ASR (Attack Success Rate): 성공률 측정

- Harmful Strings: 정확히 해당 string을 출력했는지 확인

- Harmful Behaviors: 모델이 지시를 거부하지 않고 따르려는 시도를 했는지 확인 (사람이 평가)

## 3.1 Attacks on White-box Models

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/fe2e81de-18d5-45e6-be8f-421accea0211/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FVGCOBF%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAvGnyircrChUbhcKpCSVyguk%2FzOw6h2%2FjHBFxOxHCPzAiBVdl%2FpRFW4MWBQB2n%2BpDyQjQrA9ljLTmPrGsuCFQtXzyqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLqYieE%2FHb8aJu%2FFqKtwDqWMMjceLwHbrgdfCm9%2Fmxe%2FTcHGly49DPN2m2nJwcGkBGQTJmBqA8kKfYi9i15YDMtl6Zrtt76RTdu%2BhLPt6T3x8uZTyC4J%2F4BEeG5dSgqushYiopjsajodCRXT5QyfTbeKu5TEhd%2Fch%2B69vxupRUeCTR8A5B0lMQDolrh87oTpPqcnnlKfrfkBjYlHfbfvc7MuDzSBlq9Y0U5VibD8Q3gkKQMhOxWmNw%2BIc%2BJZ9sJ%2B60NIkhS7aefURV%2BKBroB4fejnsJEuAyxplvO9vKEajau2WgHvBRk0MKF%2FMPCYW%2BydyOiq7QEttW8A%2FKCMZiumWc3%2FRIu%2BfrnG2K%2FQpEs4CUX1ZzifqAsUu2YGoJ5z0m7jUEAt0TVCgJCSF5RMC4WoqlFwn93x1JFesXS4CFFeUxqrAYAj9xx0Nc4TZ%2FdoNheTK3RrLkKOy%2FzQFEIWZ4NsTZVj4NIOtKuG5dyRY132Rhmr6R%2Bn1R3ezKxwXseXYxCdpfvTgjQDrwXITVLjh0Q%2BYbg%2BYNphuQrbuw8HUskI%2FtSQm23cfqJIrbhhvZFSXW1AOw%2FubI1ESmDfQKcbnCtpNc167juFBNEtAIcsiAqojOoPCKhjyqVVwNTlcqQcthPtnLgByBihZ5GsB0Uwyv%2FhxAY6pgEcE10n0clpZL0e7cwbvOvDNoAXaU61Hi%2FeL8qzcEtVpk6EKt4Z7DTKw%2F68Y4lmin78%2FER2MbEeHEGa64anBv6cbRvgKZoh9FiC8NzMQBHaTH58FzDL7PrHtwdWW49n4McGiVXFukowVkcV71M%2BqJ3T8DY9Sd3YTrk57kRMOyDkf4RTr%2FRAoNuC4UwzSoAeAh843OfFsanTwsOS3VY2I9UkAKwqKHIQ&X-Amz-Signature=7a39386523fbeb9546c8bc7d6ef0965b9df8d10ef7de4b3fa1fcff0c091bddbe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- **1 behavior / string, 1 model**: 공격 기법들이 하나의 유해 질의에 대해 얼마나 잘 응답을 유도하는지 평가

- 25 behaviors, 1 model: 하나의 suffix로 다수 유해 behaviors에 대한 ASR 평가

## 3.2 Transfer Attacks

본 실험에서는 하나의 attack prompt가 여러 model에도 효과적인지 평가함

25개 harmful behaviors를 2~4개 models에 대해서 동시에 GCG로 최적화 진행함

**Baselines**

1. Prompt only

1. “Sure, here’s”: (수동 jailbreak 기법)

1. GCG Prompt

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/cf26dd77-7f3f-4dea-b8f9-c391acf2009c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FVGCOBF%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAvGnyircrChUbhcKpCSVyguk%2FzOw6h2%2FjHBFxOxHCPzAiBVdl%2FpRFW4MWBQB2n%2BpDyQjQrA9ljLTmPrGsuCFQtXzyqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLqYieE%2FHb8aJu%2FFqKtwDqWMMjceLwHbrgdfCm9%2Fmxe%2FTcHGly49DPN2m2nJwcGkBGQTJmBqA8kKfYi9i15YDMtl6Zrtt76RTdu%2BhLPt6T3x8uZTyC4J%2F4BEeG5dSgqushYiopjsajodCRXT5QyfTbeKu5TEhd%2Fch%2B69vxupRUeCTR8A5B0lMQDolrh87oTpPqcnnlKfrfkBjYlHfbfvc7MuDzSBlq9Y0U5VibD8Q3gkKQMhOxWmNw%2BIc%2BJZ9sJ%2B60NIkhS7aefURV%2BKBroB4fejnsJEuAyxplvO9vKEajau2WgHvBRk0MKF%2FMPCYW%2BydyOiq7QEttW8A%2FKCMZiumWc3%2FRIu%2BfrnG2K%2FQpEs4CUX1ZzifqAsUu2YGoJ5z0m7jUEAt0TVCgJCSF5RMC4WoqlFwn93x1JFesXS4CFFeUxqrAYAj9xx0Nc4TZ%2FdoNheTK3RrLkKOy%2FzQFEIWZ4NsTZVj4NIOtKuG5dyRY132Rhmr6R%2Bn1R3ezKxwXseXYxCdpfvTgjQDrwXITVLjh0Q%2BYbg%2BYNphuQrbuw8HUskI%2FtSQm23cfqJIrbhhvZFSXW1AOw%2FubI1ESmDfQKcbnCtpNc167juFBNEtAIcsiAqojOoPCKhjyqVVwNTlcqQcthPtnLgByBihZ5GsB0Uwyv%2FhxAY6pgEcE10n0clpZL0e7cwbvOvDNoAXaU61Hi%2FeL8qzcEtVpk6EKt4Z7DTKw%2F68Y4lmin78%2FER2MbEeHEGa64anBv6cbRvgKZoh9FiC8NzMQBHaTH58FzDL7PrHtwdWW49n4McGiVXFukowVkcV71M%2BqJ3T8DY9Sd3YTrk57kRMOyDkf4RTr%2FRAoNuC4UwzSoAeAh843OfFsanTwsOS3VY2I9UkAKwqKHIQ&X-Amz-Signature=979b3e28eb926452478922b1b303a087f481393e6a0090c8c9b2f4bff9524697&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- GCG는 대부분 모델에서 ASR 80~100% 수준을 보여줌

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/e78ff324-4b41-4921-b225-30506e96e10a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FVGCOBF%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAvGnyircrChUbhcKpCSVyguk%2FzOw6h2%2FjHBFxOxHCPzAiBVdl%2FpRFW4MWBQB2n%2BpDyQjQrA9ljLTmPrGsuCFQtXzyqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLqYieE%2FHb8aJu%2FFqKtwDqWMMjceLwHbrgdfCm9%2Fmxe%2FTcHGly49DPN2m2nJwcGkBGQTJmBqA8kKfYi9i15YDMtl6Zrtt76RTdu%2BhLPt6T3x8uZTyC4J%2F4BEeG5dSgqushYiopjsajodCRXT5QyfTbeKu5TEhd%2Fch%2B69vxupRUeCTR8A5B0lMQDolrh87oTpPqcnnlKfrfkBjYlHfbfvc7MuDzSBlq9Y0U5VibD8Q3gkKQMhOxWmNw%2BIc%2BJZ9sJ%2B60NIkhS7aefURV%2BKBroB4fejnsJEuAyxplvO9vKEajau2WgHvBRk0MKF%2FMPCYW%2BydyOiq7QEttW8A%2FKCMZiumWc3%2FRIu%2BfrnG2K%2FQpEs4CUX1ZzifqAsUu2YGoJ5z0m7jUEAt0TVCgJCSF5RMC4WoqlFwn93x1JFesXS4CFFeUxqrAYAj9xx0Nc4TZ%2FdoNheTK3RrLkKOy%2FzQFEIWZ4NsTZVj4NIOtKuG5dyRY132Rhmr6R%2Bn1R3ezKxwXseXYxCdpfvTgjQDrwXITVLjh0Q%2BYbg%2BYNphuQrbuw8HUskI%2FtSQm23cfqJIrbhhvZFSXW1AOw%2FubI1ESmDfQKcbnCtpNc167juFBNEtAIcsiAqojOoPCKhjyqVVwNTlcqQcthPtnLgByBihZ5GsB0Uwyv%2FhxAY6pgEcE10n0clpZL0e7cwbvOvDNoAXaU61Hi%2FeL8qzcEtVpk6EKt4Z7DTKw%2F68Y4lmin78%2FER2MbEeHEGa64anBv6cbRvgKZoh9FiC8NzMQBHaTH58FzDL7PrHtwdWW49n4McGiVXFukowVkcV71M%2BqJ3T8DY9Sd3YTrk57kRMOyDkf4RTr%2FRAoNuC4UwzSoAeAh843OfFsanTwsOS3VY2I9UkAKwqKHIQ&X-Amz-Signature=e0223938f2bbf2b626a2f52c3ec7eecb17b954cf7a0fa47669e4ca1b202d8589&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Proprietary models에 대해서는 Claude-2를 제외하고 어느정도 유의미한 ASR을 보여줌

- Concatenate: 서로 다른 GCG Prompt 3개를 하나로 연결해서 suffix로 사용

- Ensemble: 여러 GCG prompt만 시도하면서 성공한 것만 사용

## 3.3 Discussion

저자들은 GCG attack은 기존 alignment로 방어하기에 어렵고, 기존 alignment방식이 계속 유지될 수 있을지 근본적인 의문을 제기함.

**Are models becoming more robust through alignment? **

- GPT-4, Claude2는 GPT-3.5보다 ASR이 낮음 → 최근 alignment의 effectiveness로 보여질 수 있으나 주의할 점은 다음과 같음

**Are the attacks meaningful?**

- Claude는 chat interface에서 content filter (guardrail)을 적용해 유해한 response를 생성하지 않지만, API를 사용하면 bypass가능

- 초기 prompt의 단어를 바꾸는 간단한 조작으로 filter 역시 우회 가능

**Why did these attacks not yet exist?**

# Conclusion

- 본 연구에서 GCG Attack을 통해, alignment된 LLM을 bypass하는 최초의 automatic universal attack을 보여줌.

- Trasnferabiltiy도 강하게 보여주고, 기존 수작업 jailbreak보다 효과적임

- 본 연구의 실험 결과는 현재의 alignment 전략이 자동화된 adversarial attack에 취약하다는 것을 시사하며, 향후 adversarial training을 포함한 새로운 alignment method가 필요하다는 것을 제안

- 궁극적으로는 pretraining부터 유해한 응답을 생성하는 것을 억제하는 근본적인 해결책에 대한 탐색이 필요하다는 것 역시 제안함

아래 repo보면 nanoGCG로 매우 쉽게 구현할 수 있음.

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/348e3ff2-81a0-4799-b98d-05176d26e7e4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FVGCOBF%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAvGnyircrChUbhcKpCSVyguk%2FzOw6h2%2FjHBFxOxHCPzAiBVdl%2FpRFW4MWBQB2n%2BpDyQjQrA9ljLTmPrGsuCFQtXzyqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLqYieE%2FHb8aJu%2FFqKtwDqWMMjceLwHbrgdfCm9%2Fmxe%2FTcHGly49DPN2m2nJwcGkBGQTJmBqA8kKfYi9i15YDMtl6Zrtt76RTdu%2BhLPt6T3x8uZTyC4J%2F4BEeG5dSgqushYiopjsajodCRXT5QyfTbeKu5TEhd%2Fch%2B69vxupRUeCTR8A5B0lMQDolrh87oTpPqcnnlKfrfkBjYlHfbfvc7MuDzSBlq9Y0U5VibD8Q3gkKQMhOxWmNw%2BIc%2BJZ9sJ%2B60NIkhS7aefURV%2BKBroB4fejnsJEuAyxplvO9vKEajau2WgHvBRk0MKF%2FMPCYW%2BydyOiq7QEttW8A%2FKCMZiumWc3%2FRIu%2BfrnG2K%2FQpEs4CUX1ZzifqAsUu2YGoJ5z0m7jUEAt0TVCgJCSF5RMC4WoqlFwn93x1JFesXS4CFFeUxqrAYAj9xx0Nc4TZ%2FdoNheTK3RrLkKOy%2FzQFEIWZ4NsTZVj4NIOtKuG5dyRY132Rhmr6R%2Bn1R3ezKxwXseXYxCdpfvTgjQDrwXITVLjh0Q%2BYbg%2BYNphuQrbuw8HUskI%2FtSQm23cfqJIrbhhvZFSXW1AOw%2FubI1ESmDfQKcbnCtpNc167juFBNEtAIcsiAqojOoPCKhjyqVVwNTlcqQcthPtnLgByBihZ5GsB0Uwyv%2FhxAY6pgEcE10n0clpZL0e7cwbvOvDNoAXaU61Hi%2FeL8qzcEtVpk6EKt4Z7DTKw%2F68Y4lmin78%2FER2MbEeHEGa64anBv6cbRvgKZoh9FiC8NzMQBHaTH58FzDL7PrHtwdWW49n4McGiVXFukowVkcV71M%2BqJ3T8DY9Sd3YTrk57kRMOyDkf4RTr%2FRAoNuC4UwzSoAeAh843OfFsanTwsOS3VY2I9UkAKwqKHIQ&X-Amz-Signature=bd831505f9d684ecdd7f31329bdaaf93ca5b11ca5bd81cff9f2d58f6caf19c87&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
