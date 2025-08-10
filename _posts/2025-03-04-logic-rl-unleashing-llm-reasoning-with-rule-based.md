---
categories:
- paper-reviews
date: '2025-03-04 00:00:00'
description: 논문 리뷰 - RL 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- llm
- paper-review
- reasoning
- reinforcement-learning
- rl
thumbnail: assets/img/posts/2025-03-04-logic-rl-unleashing-llm-reasoning-with-rule-based/thumbnail.jpg
title: 'Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning'
---

**논문 정보**
- **Date**: 2025-03-04
- **Reviewer**: 전민진
- **Property**: RL

## Abstract

- DeepSeek-R1의 성공에서 영감을 받아서 rule-based reinforcement learning이 large reasoning model(7B)에 미치는 영향을 분석

- synthetic logic puzzle을 training data로 활용해 분석 실험

- 실험 결과, 효과적이고 안정적인 RL학습을 위한 기술적 꿀팁을 소개

- 7B모델을 rule-based RL을 통해서 reflection, verification, summarization과 같은 reasoning skill을 학습할 수 있었음

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/c8a6b837-f776-4be9-b8ff-1807e72de0e9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKLAIBX4%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDSoQ7qAxACm6nsD4TfPGvCh83QGEyEDGAeiUNinXkLhAiEA5aV8JoU4T3W%2FSLAwLO8jwmnhFgJGfwNCAl54LuW0kEsqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMhmT5XYtSN9nND3bCrcA8Fg8lleydbKPYAdUpqT7ZKOqJKB8%2FC5X4EpMHpNdxWaJ4rOysY3rDOauvzUotziN3LjPZD%2BlUN1TC6xz2zMT6BcMtitJrne751wiuFTQRtHQrXlDOKDpxmpFvSselSzcfLlxxmyBh8UIYvOCTLjRjDF%2B3VMunADMFPGOFnBffSNncXn1uJFuxMTSHdZZx9w9P0bJwDNJcDS8EwlKYoqGBBMyvtBcx7BJX9hwAIzh908uz8KL5QEPSYClsMWYBdwW07awCIPubVd01JusUHY29HHFUG7yYKMKW1gt5Zc6VeZbA97kEXV43MdYhGDL6nav2N9sXUaeO0q5fAyFrcPJmPdYNWQ3Q8Q4JGvbcHlgDm6owA8rV5xvYhNM20yaYxCm4RnKjJoM4flRFojOqhLK%2B%2BL7iyfjYBGwzxhMrCR6%2BcrfJEEype6BoOE4NrXM%2Bg63bHnBexVmDCLuZWHZdlau68%2BbTaZ2XkFJifTzz4huq9epxPpoBeK4wLf8d%2FRvvfIshPsjWf%2BnH263QntIkO09Jr%2BlAacXgBr5G%2FHUviLYaIz4lMC4NgCvnpdvJUnX%2FyusImY3xHqEb20bxk4jKP6RCaSmjKyze6uTvFiddHxr9eE4z%2FIf4MGJH58Mu0LMOb%2B4cQGOqUBeOYFgcMHMWFsL4tzIpB6%2FbeBrx%2BYXTSoP2Ra6pXvvAgeIqdEu15%2BFVT2XPE5Xt0AdiJk%2FCo0bHkturuwjSCWR%2BI9k6e25aJREXyXR9cv0YPNaVRQAzA9YVpqfYOzrpqzg%2BrD%2BJ%2BOuvE31uFwh3UHYPCmx3x8gnHPrIr%2BU51olSuFfsjWzVIP0qjPm4fP0trFGWe%2FJFRyg9%2F11U9VSVfxSzQoLcsm&X-Amz-Signature=a59186d9f064db89be6c7573dd6744ca5027d516cd6a59384d4dcde7693307d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Introduction

- LLM의 post-training은 DeepSeek-R1, Kimi-K 1.5, OpenAI-o1과 함께 급속도로 발전

- 특히 DeepSeek-R1의 경우 기존의 핵심 기법인 Monte Carlo Tree Search(MCTS), Process Reward Models(PRM)을 사용하지 않고, 간단하면서 효과적인 rule-based reinforcement learning을 소개

- 이러한 질문에 대해 답을 하기 위해 실험에 사용하는 데이터가 controllable해야함 ⇒ Knights and Knaves (K&K) logic puzzle dataset를 학습 데이터로 사용

- 본 논문에서는 Logic-RL, R1과 같은 reasoning pattern을 logic puzzle 학습으로 얻는 rule-based reinforcement learning framework를 소개

- 5000개의 로직 퍼즐로 학습했을 때, 로직퍼즐에 대한 성능 뿐만 아니라 cross-domain generalization 성능도 높아짐

- 실험을 하면서 얻은 여러 인사이트

## Method

**Data Synthesis**

- Knights and Knaves (K&K) puzzle은 추리? 느낌의 퀴즈

1. Procedural Generation :  퍼즐은 logic template를 사용해서 생성됨 ⇒ consistency와 무한한 variability를 보장

1. Controlled Difficulty Levels : 퍼즐의 난이도는 등장인물의 수와, logical operation(1-4 combination of Boolean operators)으로 조절 가능

1. Ease of Verification : 각 퍼즐은 하나의 명확한 답이 있음

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/76de166b-a5b4-41ac-bd3e-63694c7db546/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKLAIBX4%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDSoQ7qAxACm6nsD4TfPGvCh83QGEyEDGAeiUNinXkLhAiEA5aV8JoU4T3W%2FSLAwLO8jwmnhFgJGfwNCAl54LuW0kEsqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMhmT5XYtSN9nND3bCrcA8Fg8lleydbKPYAdUpqT7ZKOqJKB8%2FC5X4EpMHpNdxWaJ4rOysY3rDOauvzUotziN3LjPZD%2BlUN1TC6xz2zMT6BcMtitJrne751wiuFTQRtHQrXlDOKDpxmpFvSselSzcfLlxxmyBh8UIYvOCTLjRjDF%2B3VMunADMFPGOFnBffSNncXn1uJFuxMTSHdZZx9w9P0bJwDNJcDS8EwlKYoqGBBMyvtBcx7BJX9hwAIzh908uz8KL5QEPSYClsMWYBdwW07awCIPubVd01JusUHY29HHFUG7yYKMKW1gt5Zc6VeZbA97kEXV43MdYhGDL6nav2N9sXUaeO0q5fAyFrcPJmPdYNWQ3Q8Q4JGvbcHlgDm6owA8rV5xvYhNM20yaYxCm4RnKjJoM4flRFojOqhLK%2B%2BL7iyfjYBGwzxhMrCR6%2BcrfJEEype6BoOE4NrXM%2Bg63bHnBexVmDCLuZWHZdlau68%2BbTaZ2XkFJifTzz4huq9epxPpoBeK4wLf8d%2FRvvfIshPsjWf%2BnH263QntIkO09Jr%2BlAacXgBr5G%2FHUviLYaIz4lMC4NgCvnpdvJUnX%2FyusImY3xHqEb20bxk4jKP6RCaSmjKyze6uTvFiddHxr9eE4z%2FIf4MGJH58Mu0LMOb%2B4cQGOqUBeOYFgcMHMWFsL4tzIpB6%2FbeBrx%2BYXTSoP2Ra6pXvvAgeIqdEu15%2BFVT2XPE5Xt0AdiJk%2FCo0bHkturuwjSCWR%2BI9k6e25aJREXyXR9cv0YPNaVRQAzA9YVpqfYOzrpqzg%2BrD%2BJ%2BOuvE31uFwh3UHYPCmx3x8gnHPrIr%2BU51olSuFfsjWzVIP0qjPm4fP0trFGWe%2FJFRyg9%2F11U9VSVfxSzQoLcsm&X-Amz-Signature=4963a3cd7cb0d80eb8386d1a375ee0450165ee0b0b8edd9878ac5e05c20812cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**Rule Based Reward Modeling**

- reward은 학습에 필요한 핵심 시그널

- 하지만 저자들은 모델의 output에서 hacking behavior를 관찰했고, reward design을 계속 바꿈 
⇒ 아래가 이제 거의 unhackable한 rule-based reward system. 

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/197dee41-968f-4b73-bba5-b125b564fe9a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKLAIBX4%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDSoQ7qAxACm6nsD4TfPGvCh83QGEyEDGAeiUNinXkLhAiEA5aV8JoU4T3W%2FSLAwLO8jwmnhFgJGfwNCAl54LuW0kEsqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMhmT5XYtSN9nND3bCrcA8Fg8lleydbKPYAdUpqT7ZKOqJKB8%2FC5X4EpMHpNdxWaJ4rOysY3rDOauvzUotziN3LjPZD%2BlUN1TC6xz2zMT6BcMtitJrne751wiuFTQRtHQrXlDOKDpxmpFvSselSzcfLlxxmyBh8UIYvOCTLjRjDF%2B3VMunADMFPGOFnBffSNncXn1uJFuxMTSHdZZx9w9P0bJwDNJcDS8EwlKYoqGBBMyvtBcx7BJX9hwAIzh908uz8KL5QEPSYClsMWYBdwW07awCIPubVd01JusUHY29HHFUG7yYKMKW1gt5Zc6VeZbA97kEXV43MdYhGDL6nav2N9sXUaeO0q5fAyFrcPJmPdYNWQ3Q8Q4JGvbcHlgDm6owA8rV5xvYhNM20yaYxCm4RnKjJoM4flRFojOqhLK%2B%2BL7iyfjYBGwzxhMrCR6%2BcrfJEEype6BoOE4NrXM%2Bg63bHnBexVmDCLuZWHZdlau68%2BbTaZ2XkFJifTzz4huq9epxPpoBeK4wLf8d%2FRvvfIshPsjWf%2BnH263QntIkO09Jr%2BlAacXgBr5G%2FHUviLYaIz4lMC4NgCvnpdvJUnX%2FyusImY3xHqEb20bxk4jKP6RCaSmjKyze6uTvFiddHxr9eE4z%2FIf4MGJH58Mu0LMOb%2B4cQGOqUBeOYFgcMHMWFsL4tzIpB6%2FbeBrx%2BYXTSoP2Ra6pXvvAgeIqdEu15%2BFVT2XPE5Xt0AdiJk%2FCo0bHkturuwjSCWR%2BI9k6e25aJREXyXR9cv0YPNaVRQAzA9YVpqfYOzrpqzg%2BrD%2BJ%2BOuvE31uFwh3UHYPCmx3x8gnHPrIr%2BU51olSuFfsjWzVIP0qjPm4fP0trFGWe%2FJFRyg9%2F11U9VSVfxSzQoLcsm&X-Amz-Signature=a2dff2a54fb1e756ba7f672b4227960f6995303a3f8381c2939a19e58bf83601&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Format Reward

- Answer Reward

**RL Algorithm**

- Reinforce Return Calculation

⇒ 아래는 DeepSeek-Math의 추천에 따라, REINFORCE++를 구현할 때 몇가지 수정사항을 반영

- First modification : Use KL Loss

- Second ModificationL KL Estimation

**Training Schedule**

- 3600 step 학습, 4*10^-7의 learning rate, temperature 0.7로 사용

- 학습 동안에, logic puzzle의 등장 인물은 3-7명

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/1d5c63f7-1f20-44dc-b2f3-07cd17e055f9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKLAIBX4%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDSoQ7qAxACm6nsD4TfPGvCh83QGEyEDGAeiUNinXkLhAiEA5aV8JoU4T3W%2FSLAwLO8jwmnhFgJGfwNCAl54LuW0kEsqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMhmT5XYtSN9nND3bCrcA8Fg8lleydbKPYAdUpqT7ZKOqJKB8%2FC5X4EpMHpNdxWaJ4rOysY3rDOauvzUotziN3LjPZD%2BlUN1TC6xz2zMT6BcMtitJrne751wiuFTQRtHQrXlDOKDpxmpFvSselSzcfLlxxmyBh8UIYvOCTLjRjDF%2B3VMunADMFPGOFnBffSNncXn1uJFuxMTSHdZZx9w9P0bJwDNJcDS8EwlKYoqGBBMyvtBcx7BJX9hwAIzh908uz8KL5QEPSYClsMWYBdwW07awCIPubVd01JusUHY29HHFUG7yYKMKW1gt5Zc6VeZbA97kEXV43MdYhGDL6nav2N9sXUaeO0q5fAyFrcPJmPdYNWQ3Q8Q4JGvbcHlgDm6owA8rV5xvYhNM20yaYxCm4RnKjJoM4flRFojOqhLK%2B%2BL7iyfjYBGwzxhMrCR6%2BcrfJEEype6BoOE4NrXM%2Bg63bHnBexVmDCLuZWHZdlau68%2BbTaZ2XkFJifTzz4huq9epxPpoBeK4wLf8d%2FRvvfIshPsjWf%2BnH263QntIkO09Jr%2BlAacXgBr5G%2FHUviLYaIz4lMC4NgCvnpdvJUnX%2FyusImY3xHqEb20bxk4jKP6RCaSmjKyze6uTvFiddHxr9eE4z%2FIf4MGJH58Mu0LMOb%2B4cQGOqUBeOYFgcMHMWFsL4tzIpB6%2FbeBrx%2BYXTSoP2Ra6pXvvAgeIqdEu15%2BFVT2XPE5Xt0AdiJk%2FCo0bHkturuwjSCWR%2BI9k6e25aJREXyXR9cv0YPNaVRQAzA9YVpqfYOzrpqzg%2BrD%2BJ%2BOuvE31uFwh3UHYPCmx3x8gnHPrIr%2BU51olSuFfsjWzVIP0qjPm4fP0trFGWe%2FJFRyg9%2F11U9VSVfxSzQoLcsm&X-Amz-Signature=300026d8d9bd187b83533509c6c8f6f08c0f985265ad028ae9cf53bfa9bd44fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Experiment

- Qwen 2.5 친구들을 주로 사용

- 3-7명이 등장하는 K&K logic을 학습 데이터(<5k)로 사용, 8명이 등장하는 퍼즐을 OOD로 사용

## Research Question

- RQ1 : How does GRPO Compare to Other RL Algorithms?

- RQ2 : Do certain thinking tokens and language-mixing phenemona improve reasoning?

- RQ3 : Does an ‘Aha Moment’ Emerge During Training?

- RQ4 : Can the Model Generalize to Out-of-Distribution (OOD) Tasks?

- RQ5 : Which Generalizes Better, SFT or RL?

- RQ6 : Is Curriculum Learning Still Necessary in RL?

- RQ7 : Does Longer Response Length Guarantee Better Reasoning?
