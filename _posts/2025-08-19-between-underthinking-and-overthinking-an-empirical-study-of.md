---
categories:
  - paper-reviews
date: "2025-08-19 00:00:00"
description: 논문 리뷰 - Reasoning 관련 연구
giscus_comments: true
layout: post
related_posts: false
slug: 2025-08-19-between-underthinking-and-overthinking-an-empirical-study-of
tags:
  - llm
  - paper-review
  - reasoning
title: "Between Underthinking and Overthinking: An Empirical Study of Reasoning Length
  and correctness in LLMs"
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

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/f377d385-77b6-42c1-b173-280da3a0e50e/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-07-01_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_12.33.23.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AJATHMS%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110001Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHli89shSN%2Fc8Aabc%2FlUivfqU3HWuU2VXUBPAqPqlxXQAiAwOrTeg%2FukrfXM81xJy4UCC1dSghAtUECDmhGYcXObCiqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQKAlTuz%2FOHIQpRQYKtwDvrVW654o%2FPaq8hWslFB6vnQ5Wh55jTEWRvGIfj2cvEbQz6T7CJDV96%2F9cnnjm9GHeTxDxnBHOScMaWTXBM1o4RuiSVROrOcplhpHbuegkzmR4L0W2%2FCGM6BLTswKsqW17xoWm6584HYFwDNco3LCU2xzvezcldG06hVF1xQ8oJOTBF1FZsSnwuZNMwcAVzr0bl0IDpa11rLGrMFeU%2Bv9NcEezu5oPfrQu6bCqIRnuNb%2FJrLSOp6xzd3vgpmb3e8BXziwg85%2FjwJ2p6vpSf2L%2Bh1PDKs7p5MrhYCpOhbZG5dWr58feQhFC3kZXWnML50KLhnIOi9CIKkfuYd2pec28Nz1SNXb4LEmiIC9woIJJKjsEZJ9%2FeXIhEBQz5BFQloTLFzxi6Y26cDLlT4HvbQbGo1WhqyOjTLC9Kt2%2BC6q5UkrO8qZj7qdVbfBdsUMZJj3%2Fjix%2FDn6rINV7AJUqvbgrt0vOgTZ6koE0qSCnQrad0R1VwQL5dLsP%2FM%2B67PwGstQbJFd8OaOQpOqJcQUNYA1ycQP457d5aOmLOYCbB%2B7ekU%2F1Co1%2FMh%2FnMDtXlrBsHnuB26sIamTD0cj%2BG1NWBK0AyWlifQ9mGTFRoNh3IZG%2FY7rRPTJCgtq65Uy8skw3dThxAY6pgGdJsdPqK3du6dmRgEQi%2FNtxXqRkhY68cmo0pPBraK1dQyX6hvq4UWtYs5xFjNvt4plmTBfiBoxXOxpIYbeab3XOZx1jAPtzivOQi1XbOVwHKCQ9MkecZrnsNB63zm%2ByTWztn%2Bo7bKwszImOgx%2FnZ%2BRwFFsWXbv1vmh36hLGgwqY%2BC3xm%2Fy99fh7mY5Yvwx%2FdvL9Am4Aks%2FnURLLn9Y1w1r6IKzNgnY&X-Amz-Signature=273cf5407fb69f0744d2e33542498aeba1f47769043a4aef9b51d7370c98f01f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- L_r, Acc_r: r번째로 짧은 reasoning path의 평균 length/accuracy

- consistent non-monotonic trend 관찰

(준원 뇌피셜: 일단 R1은 (1) MATH 관련 데이터는 외워서 풀것 같기 때문에 temp=1.0, top_p=1로 줘서 decoding path 길어지면 degen 발생했을것으로 예상 (2) GSM8K 유사 난이도는 거의 외웠을것이고 + 상대적으로 쉽기 때문에 1~1.5K thinking budget내로는 거의 비슷할거 같음..)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/fbac1e04-36c1-40da-86cd-4d47d0bac616/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-07-01_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_1.10.30.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AJATHMS%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110001Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHli89shSN%2Fc8Aabc%2FlUivfqU3HWuU2VXUBPAqPqlxXQAiAwOrTeg%2FukrfXM81xJy4UCC1dSghAtUECDmhGYcXObCiqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQKAlTuz%2FOHIQpRQYKtwDvrVW654o%2FPaq8hWslFB6vnQ5Wh55jTEWRvGIfj2cvEbQz6T7CJDV96%2F9cnnjm9GHeTxDxnBHOScMaWTXBM1o4RuiSVROrOcplhpHbuegkzmR4L0W2%2FCGM6BLTswKsqW17xoWm6584HYFwDNco3LCU2xzvezcldG06hVF1xQ8oJOTBF1FZsSnwuZNMwcAVzr0bl0IDpa11rLGrMFeU%2Bv9NcEezu5oPfrQu6bCqIRnuNb%2FJrLSOp6xzd3vgpmb3e8BXziwg85%2FjwJ2p6vpSf2L%2Bh1PDKs7p5MrhYCpOhbZG5dWr58feQhFC3kZXWnML50KLhnIOi9CIKkfuYd2pec28Nz1SNXb4LEmiIC9woIJJKjsEZJ9%2FeXIhEBQz5BFQloTLFzxi6Y26cDLlT4HvbQbGo1WhqyOjTLC9Kt2%2BC6q5UkrO8qZj7qdVbfBdsUMZJj3%2Fjix%2FDn6rINV7AJUqvbgrt0vOgTZ6koE0qSCnQrad0R1VwQL5dLsP%2FM%2B67PwGstQbJFd8OaOQpOqJcQUNYA1ycQP457d5aOmLOYCbB%2B7ekU%2F1Co1%2FMh%2FnMDtXlrBsHnuB26sIamTD0cj%2BG1NWBK0AyWlifQ9mGTFRoNh3IZG%2FY7rRPTJCgtq65Uy8skw3dThxAY6pgGdJsdPqK3du6dmRgEQi%2FNtxXqRkhY68cmo0pPBraK1dQyX6hvq4UWtYs5xFjNvt4plmTBfiBoxXOxpIYbeab3XOZx1jAPtzivOQi1XbOVwHKCQ9MkecZrnsNB63zm%2ByTWztn%2Bo7bKwszImOgx%2FnZ%2BRwFFsWXbv1vmh36hLGgwqY%2BC3xm%2Fy99fh7mY5Yvwx%2FdvL9Am4Aks%2FnURLLn9Y1w1r6IKzNgnY&X-Amz-Signature=2153ce332f99b80f28196ee1c93a4279be58e31b0ec30eb78101ad25310c78ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 초록: q에 대한 정답 completion중 가장 짧은 거

- 파랑: q에 대한 정답 completion중 가장 긴거

- 빨강: q에 대한 오답 completion중 가장 짧은 거

- 노랑: q에 대한 정답 completion중 가장 긴거

- R1-Preview는 MATH, GSM8K 모두 80% 이상의 질문에서 가장 짧은 샘플로 정답을 생성할 수 있음을 보임

- most length한 completion중에 correct response도 있지만 incorrect response도 존재 (논문 해석 이상..)

## 5. Question-Level Analysis

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/71468c9e-5f26-4dd2-89be-54b89681ea8e/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-07-01_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_5.44.47.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AJATHMS%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110001Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHli89shSN%2Fc8Aabc%2FlUivfqU3HWuU2VXUBPAqPqlxXQAiAwOrTeg%2FukrfXM81xJy4UCC1dSghAtUECDmhGYcXObCiqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQKAlTuz%2FOHIQpRQYKtwDvrVW654o%2FPaq8hWslFB6vnQ5Wh55jTEWRvGIfj2cvEbQz6T7CJDV96%2F9cnnjm9GHeTxDxnBHOScMaWTXBM1o4RuiSVROrOcplhpHbuegkzmR4L0W2%2FCGM6BLTswKsqW17xoWm6584HYFwDNco3LCU2xzvezcldG06hVF1xQ8oJOTBF1FZsSnwuZNMwcAVzr0bl0IDpa11rLGrMFeU%2Bv9NcEezu5oPfrQu6bCqIRnuNb%2FJrLSOp6xzd3vgpmb3e8BXziwg85%2FjwJ2p6vpSf2L%2Bh1PDKs7p5MrhYCpOhbZG5dWr58feQhFC3kZXWnML50KLhnIOi9CIKkfuYd2pec28Nz1SNXb4LEmiIC9woIJJKjsEZJ9%2FeXIhEBQz5BFQloTLFzxi6Y26cDLlT4HvbQbGo1WhqyOjTLC9Kt2%2BC6q5UkrO8qZj7qdVbfBdsUMZJj3%2Fjix%2FDn6rINV7AJUqvbgrt0vOgTZ6koE0qSCnQrad0R1VwQL5dLsP%2FM%2B67PwGstQbJFd8OaOQpOqJcQUNYA1ycQP457d5aOmLOYCbB%2B7ekU%2F1Co1%2FMh%2FnMDtXlrBsHnuB26sIamTD0cj%2BG1NWBK0AyWlifQ9mGTFRoNh3IZG%2FY7rRPTJCgtq65Uy8skw3dThxAY6pgGdJsdPqK3du6dmRgEQi%2FNtxXqRkhY68cmo0pPBraK1dQyX6hvq4UWtYs5xFjNvt4plmTBfiBoxXOxpIYbeab3XOZx1jAPtzivOQi1XbOVwHKCQ9MkecZrnsNB63zm%2ByTWztn%2Bo7bKwszImOgx%2FnZ%2BRwFFsWXbv1vmh36hLGgwqY%2BC3xm%2Fy99fh7mY5Yvwx%2FdvL9Am4Aks%2FnURLLn9Y1w1r6IKzNgnY&X-Amz-Signature=da4f08d43df5cf403c351602e4b778d70ee380443488ed95a854b88b232b7cf9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 단순하게 문제 난이도를 틀림 여부로 볼때, incorrect response가 어떤 조합에서든 response 길이가 더 길었음

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/a0c41355-ea1e-4a11-9f19-cb3b980f4c97/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-07-01_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_5.49.19.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AJATHMS%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110001Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHli89shSN%2Fc8Aabc%2FlUivfqU3HWuU2VXUBPAqPqlxXQAiAwOrTeg%2FukrfXM81xJy4UCC1dSghAtUECDmhGYcXObCiqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQKAlTuz%2FOHIQpRQYKtwDvrVW654o%2FPaq8hWslFB6vnQ5Wh55jTEWRvGIfj2cvEbQz6T7CJDV96%2F9cnnjm9GHeTxDxnBHOScMaWTXBM1o4RuiSVROrOcplhpHbuegkzmR4L0W2%2FCGM6BLTswKsqW17xoWm6584HYFwDNco3LCU2xzvezcldG06hVF1xQ8oJOTBF1FZsSnwuZNMwcAVzr0bl0IDpa11rLGrMFeU%2Bv9NcEezu5oPfrQu6bCqIRnuNb%2FJrLSOp6xzd3vgpmb3e8BXziwg85%2FjwJ2p6vpSf2L%2Bh1PDKs7p5MrhYCpOhbZG5dWr58feQhFC3kZXWnML50KLhnIOi9CIKkfuYd2pec28Nz1SNXb4LEmiIC9woIJJKjsEZJ9%2FeXIhEBQz5BFQloTLFzxi6Y26cDLlT4HvbQbGo1WhqyOjTLC9Kt2%2BC6q5UkrO8qZj7qdVbfBdsUMZJj3%2Fjix%2FDn6rINV7AJUqvbgrt0vOgTZ6koE0qSCnQrad0R1VwQL5dLsP%2FM%2B67PwGstQbJFd8OaOQpOqJcQUNYA1ycQP457d5aOmLOYCbB%2B7ekU%2F1Co1%2FMh%2FnMDtXlrBsHnuB26sIamTD0cj%2BG1NWBK0AyWlifQ9mGTFRoNh3IZG%2FY7rRPTJCgtq65Uy8skw3dThxAY6pgGdJsdPqK3du6dmRgEQi%2FNtxXqRkhY68cmo0pPBraK1dQyX6hvq4UWtYs5xFjNvt4plmTBfiBoxXOxpIYbeab3XOZx1jAPtzivOQi1XbOVwHKCQ9MkecZrnsNB63zm%2ByTWztn%2Bo7bKwszImOgx%2FnZ%2BRwFFsWXbv1vmh36hLGgwqY%2BC3xm%2Fy99fh7mY5Yvwx%2FdvL9Am4Aks%2FnURLLn9Y1w1r6IKzNgnY&X-Amz-Signature=d7c42b276304e450f46bdd1816b6dc13f52f3f2d5b91ded2caaab0938e046936&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- N-completion별로 difficulty를 분류

⇒ 그러나 (1) 문제가 어려워서 lengthy한지 (2) length해져서 틀린건지 판단이 어려움

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/6c8cd3cd-6aa3-4c46-b883-68b4246ceefc/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-07-01_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_6.07.59.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AJATHMS%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110001Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHli89shSN%2Fc8Aabc%2FlUivfqU3HWuU2VXUBPAqPqlxXQAiAwOrTeg%2FukrfXM81xJy4UCC1dSghAtUECDmhGYcXObCiqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQKAlTuz%2FOHIQpRQYKtwDvrVW654o%2FPaq8hWslFB6vnQ5Wh55jTEWRvGIfj2cvEbQz6T7CJDV96%2F9cnnjm9GHeTxDxnBHOScMaWTXBM1o4RuiSVROrOcplhpHbuegkzmR4L0W2%2FCGM6BLTswKsqW17xoWm6584HYFwDNco3LCU2xzvezcldG06hVF1xQ8oJOTBF1FZsSnwuZNMwcAVzr0bl0IDpa11rLGrMFeU%2Bv9NcEezu5oPfrQu6bCqIRnuNb%2FJrLSOp6xzd3vgpmb3e8BXziwg85%2FjwJ2p6vpSf2L%2Bh1PDKs7p5MrhYCpOhbZG5dWr58feQhFC3kZXWnML50KLhnIOi9CIKkfuYd2pec28Nz1SNXb4LEmiIC9woIJJKjsEZJ9%2FeXIhEBQz5BFQloTLFzxi6Y26cDLlT4HvbQbGo1WhqyOjTLC9Kt2%2BC6q5UkrO8qZj7qdVbfBdsUMZJj3%2Fjix%2FDn6rINV7AJUqvbgrt0vOgTZ6koE0qSCnQrad0R1VwQL5dLsP%2FM%2B67PwGstQbJFd8OaOQpOqJcQUNYA1ycQP457d5aOmLOYCbB%2B7ekU%2F1Co1%2FMh%2FnMDtXlrBsHnuB26sIamTD0cj%2BG1NWBK0AyWlifQ9mGTFRoNh3IZG%2FY7rRPTJCgtq65Uy8skw3dThxAY6pgGdJsdPqK3du6dmRgEQi%2FNtxXqRkhY68cmo0pPBraK1dQyX6hvq4UWtYs5xFjNvt4plmTBfiBoxXOxpIYbeab3XOZx1jAPtzivOQi1XbOVwHKCQ9MkecZrnsNB63zm%2ByTWztn%2Bo7bKwszImOgx%2FnZ%2BRwFFsWXbv1vmh36hLGgwqY%2BC3xm%2Fy99fh7mY5Yvwx%2FdvL9Am4Aks%2FnURLLn9Y1w1r6IKzNgnY&X-Amz-Signature=fc9cffd60f868d6a5667952278475a639f5b448cfcf3d9daa3a125c5bf6123d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Q^{easy}_{\cap} = Q^{easy}_{i} \cap Q^{easy}\_{j}

- Q^{easy}_{i/j} = Q^{easy}_{i} / Q^{easy}\_{j} > M_i 에서만 쉬운 문제

- Q^{easy}_{j/i} = Q^{easy}_{j} / Q^{easy}\_{i} > M_j에서만 쉬운 문제

- 보편적으로 쉬운 문제가 아니라 another model’s advantage set (다른모델에서 쉬운 문제)에서 오히려 lengthy generation을 보임

- signficant로 보면 M_i → M_j-Adv Set을 풀때 보다 lengthy해짐

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/b272f5c0-6437-4a3b-8b62-31be1fb32ee4/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-07-01_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_6.32.17.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AJATHMS%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHli89shSN%2Fc8Aabc%2FlUivfqU3HWuU2VXUBPAqPqlxXQAiAwOrTeg%2FukrfXM81xJy4UCC1dSghAtUECDmhGYcXObCiqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQKAlTuz%2FOHIQpRQYKtwDvrVW654o%2FPaq8hWslFB6vnQ5Wh55jTEWRvGIfj2cvEbQz6T7CJDV96%2F9cnnjm9GHeTxDxnBHOScMaWTXBM1o4RuiSVROrOcplhpHbuegkzmR4L0W2%2FCGM6BLTswKsqW17xoWm6584HYFwDNco3LCU2xzvezcldG06hVF1xQ8oJOTBF1FZsSnwuZNMwcAVzr0bl0IDpa11rLGrMFeU%2Bv9NcEezu5oPfrQu6bCqIRnuNb%2FJrLSOp6xzd3vgpmb3e8BXziwg85%2FjwJ2p6vpSf2L%2Bh1PDKs7p5MrhYCpOhbZG5dWr58feQhFC3kZXWnML50KLhnIOi9CIKkfuYd2pec28Nz1SNXb4LEmiIC9woIJJKjsEZJ9%2FeXIhEBQz5BFQloTLFzxi6Y26cDLlT4HvbQbGo1WhqyOjTLC9Kt2%2BC6q5UkrO8qZj7qdVbfBdsUMZJj3%2Fjix%2FDn6rINV7AJUqvbgrt0vOgTZ6koE0qSCnQrad0R1VwQL5dLsP%2FM%2B67PwGstQbJFd8OaOQpOqJcQUNYA1ycQP457d5aOmLOYCbB%2B7ekU%2F1Co1%2FMh%2FnMDtXlrBsHnuB26sIamTD0cj%2BG1NWBK0AyWlifQ9mGTFRoNh3IZG%2FY7rRPTJCgtq65Uy8skw3dThxAY6pgGdJsdPqK3du6dmRgEQi%2FNtxXqRkhY68cmo0pPBraK1dQyX6hvq4UWtYs5xFjNvt4plmTBfiBoxXOxpIYbeab3XOZx1jAPtzivOQi1XbOVwHKCQ9MkecZrnsNB63zm%2ByTWztn%2Bo7bKwszImOgx%2FnZ%2BRwFFsWXbv1vmh36hLGgwqY%2BC3xm%2Fy99fh7mY5Yvwx%2FdvL9Am4Aks%2FnURLLn9Y1w1r6IKzNgnY&X-Amz-Signature=1f04e310eea5b25681d7220dcbeb5b9a18f1354472210b84eb8ff588da87cccb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- hard question에서는 Q^{hard}\_{\cap}에서 보다 another model’s advantage set에서 lengthy해질 것을 기대했으나 그렇진 않음

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/9e383a99-5093-4f6d-b4b5-b45916cafabd/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-07-01_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_6.36.41.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AJATHMS%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHli89shSN%2Fc8Aabc%2FlUivfqU3HWuU2VXUBPAqPqlxXQAiAwOrTeg%2FukrfXM81xJy4UCC1dSghAtUECDmhGYcXObCiqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQKAlTuz%2FOHIQpRQYKtwDvrVW654o%2FPaq8hWslFB6vnQ5Wh55jTEWRvGIfj2cvEbQz6T7CJDV96%2F9cnnjm9GHeTxDxnBHOScMaWTXBM1o4RuiSVROrOcplhpHbuegkzmR4L0W2%2FCGM6BLTswKsqW17xoWm6584HYFwDNco3LCU2xzvezcldG06hVF1xQ8oJOTBF1FZsSnwuZNMwcAVzr0bl0IDpa11rLGrMFeU%2Bv9NcEezu5oPfrQu6bCqIRnuNb%2FJrLSOp6xzd3vgpmb3e8BXziwg85%2FjwJ2p6vpSf2L%2Bh1PDKs7p5MrhYCpOhbZG5dWr58feQhFC3kZXWnML50KLhnIOi9CIKkfuYd2pec28Nz1SNXb4LEmiIC9woIJJKjsEZJ9%2FeXIhEBQz5BFQloTLFzxi6Y26cDLlT4HvbQbGo1WhqyOjTLC9Kt2%2BC6q5UkrO8qZj7qdVbfBdsUMZJj3%2Fjix%2FDn6rINV7AJUqvbgrt0vOgTZ6koE0qSCnQrad0R1VwQL5dLsP%2FM%2B67PwGstQbJFd8OaOQpOqJcQUNYA1ycQP457d5aOmLOYCbB%2B7ekU%2F1Co1%2FMh%2FnMDtXlrBsHnuB26sIamTD0cj%2BG1NWBK0AyWlifQ9mGTFRoNh3IZG%2FY7rRPTJCgtq65Uy8skw3dThxAY6pgGdJsdPqK3du6dmRgEQi%2FNtxXqRkhY68cmo0pPBraK1dQyX6hvq4UWtYs5xFjNvt4plmTBfiBoxXOxpIYbeab3XOZx1jAPtzivOQi1XbOVwHKCQ9MkecZrnsNB63zm%2ByTWztn%2Bo7bKwszImOgx%2FnZ%2BRwFFsWXbv1vmh36hLGgwqY%2BC3xm%2Fy99fh7mY5Yvwx%2FdvL9Am4Aks%2FnURLLn9Y1w1r6IKzNgnY&X-Amz-Signature=17b896b6facbaf99f39560c7ae8d19345ca683f9d409429cb7ee60589d4d543a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- (어떻게 실험했는지는 모르겠는데..) token length가 짧아질수록 accuracy가 올라간다.

- 위에 실험을 기반으로 token legnth가 짧으니 확률적으로 당연히 accuracy가 높은 답변일수록 PPL도 낮을 것

## 6. Effect of Length Preference Optimization

- 지금까지 지적된 문제들을 해결하기 위해 correct/length-balanced reward-based RL등이 소개되었음

- 이를 위해 이전에 drive-out한 직관들을 가지고 간단한 실험을 진행.

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/4a1d6e98-90ef-46ac-9f19-1bf7410ba26a/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-07-01_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_6.53.47.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AJATHMS%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHli89shSN%2Fc8Aabc%2FlUivfqU3HWuU2VXUBPAqPqlxXQAiAwOrTeg%2FukrfXM81xJy4UCC1dSghAtUECDmhGYcXObCiqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQKAlTuz%2FOHIQpRQYKtwDvrVW654o%2FPaq8hWslFB6vnQ5Wh55jTEWRvGIfj2cvEbQz6T7CJDV96%2F9cnnjm9GHeTxDxnBHOScMaWTXBM1o4RuiSVROrOcplhpHbuegkzmR4L0W2%2FCGM6BLTswKsqW17xoWm6584HYFwDNco3LCU2xzvezcldG06hVF1xQ8oJOTBF1FZsSnwuZNMwcAVzr0bl0IDpa11rLGrMFeU%2Bv9NcEezu5oPfrQu6bCqIRnuNb%2FJrLSOp6xzd3vgpmb3e8BXziwg85%2FjwJ2p6vpSf2L%2Bh1PDKs7p5MrhYCpOhbZG5dWr58feQhFC3kZXWnML50KLhnIOi9CIKkfuYd2pec28Nz1SNXb4LEmiIC9woIJJKjsEZJ9%2FeXIhEBQz5BFQloTLFzxi6Y26cDLlT4HvbQbGo1WhqyOjTLC9Kt2%2BC6q5UkrO8qZj7qdVbfBdsUMZJj3%2Fjix%2FDn6rINV7AJUqvbgrt0vOgTZ6koE0qSCnQrad0R1VwQL5dLsP%2FM%2B67PwGstQbJFd8OaOQpOqJcQUNYA1ycQP457d5aOmLOYCbB%2B7ekU%2F1Co1%2FMh%2FnMDtXlrBsHnuB26sIamTD0cj%2BG1NWBK0AyWlifQ9mGTFRoNh3IZG%2FY7rRPTJCgtq65Uy8skw3dThxAY6pgGdJsdPqK3du6dmRgEQi%2FNtxXqRkhY68cmo0pPBraK1dQyX6hvq4UWtYs5xFjNvt4plmTBfiBoxXOxpIYbeab3XOZx1jAPtzivOQi1XbOVwHKCQ9MkecZrnsNB63zm%2ByTWztn%2Bo7bKwszImOgx%2FnZ%2BRwFFsWXbv1vmh36hLGgwqY%2BC3xm%2Fy99fh7mY5Yvwx%2FdvL9Am4Aks%2FnURLLn9Y1w1r6IKzNgnY&X-Amz-Signature=8c518a39d61123ef40156e26401cea473e1ccdcae07fd4f0851e9a9e76ddde4a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- training step을 반복할수록 accuracy 변동폭은 적으나 average token length 30%에서 60% 감소

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/f7a55473-abc1-4d8c-811b-3922246b68a3/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2025-07-01_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_6.56.30.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666AJATHMS%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T110002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHli89shSN%2Fc8Aabc%2FlUivfqU3HWuU2VXUBPAqPqlxXQAiAwOrTeg%2FukrfXM81xJy4UCC1dSghAtUECDmhGYcXObCiqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQKAlTuz%2FOHIQpRQYKtwDvrVW654o%2FPaq8hWslFB6vnQ5Wh55jTEWRvGIfj2cvEbQz6T7CJDV96%2F9cnnjm9GHeTxDxnBHOScMaWTXBM1o4RuiSVROrOcplhpHbuegkzmR4L0W2%2FCGM6BLTswKsqW17xoWm6584HYFwDNco3LCU2xzvezcldG06hVF1xQ8oJOTBF1FZsSnwuZNMwcAVzr0bl0IDpa11rLGrMFeU%2Bv9NcEezu5oPfrQu6bCqIRnuNb%2FJrLSOp6xzd3vgpmb3e8BXziwg85%2FjwJ2p6vpSf2L%2Bh1PDKs7p5MrhYCpOhbZG5dWr58feQhFC3kZXWnML50KLhnIOi9CIKkfuYd2pec28Nz1SNXb4LEmiIC9woIJJKjsEZJ9%2FeXIhEBQz5BFQloTLFzxi6Y26cDLlT4HvbQbGo1WhqyOjTLC9Kt2%2BC6q5UkrO8qZj7qdVbfBdsUMZJj3%2Fjix%2FDn6rINV7AJUqvbgrt0vOgTZ6koE0qSCnQrad0R1VwQL5dLsP%2FM%2B67PwGstQbJFd8OaOQpOqJcQUNYA1ycQP457d5aOmLOYCbB%2B7ekU%2F1Co1%2FMh%2FnMDtXlrBsHnuB26sIamTD0cj%2BG1NWBK0AyWlifQ9mGTFRoNh3IZG%2FY7rRPTJCgtq65Uy8skw3dThxAY6pgGdJsdPqK3du6dmRgEQi%2FNtxXqRkhY68cmo0pPBraK1dQyX6hvq4UWtYs5xFjNvt4plmTBfiBoxXOxpIYbeab3XOZx1jAPtzivOQi1XbOVwHKCQ9MkecZrnsNB63zm%2ByTWztn%2Bo7bKwszImOgx%2FnZ%2BRwFFsWXbv1vmh36hLGgwqY%2BC3xm%2Fy99fh7mY5Yvwx%2FdvL9Am4Aks%2FnURLLn9Y1w1r6IKzNgnY&X-Amz-Signature=b786d96f612432c2396076db8219710c8e424e0f6dd613764b9ea60a85c12e7f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- SimPO가 진행됨에 따라 incorrect response의 생성이 줄어들었다.

## 7. Conclusion & Limitation

- generation length와 final answer correctness에 대해서 심도 있는 분석

- LM의 크기가 너무 작고, benchmark가 너무 쉬움…
