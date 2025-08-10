---
categories:
- paper-reviews
date: '2025-01-02 00:00:00'
description: 논문 리뷰 - DiffusionLM, Pre-training 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- bert
- diffusion
- diffusionlm
- language-model
- paper-review
- pre-training
thumbnail: assets/img/posts/2025-01-02-diffusion-language-model-mathematical-foundations-inference-optimization/thumbnail.jpg
title: Diffusion Language Model-Mathematical foundations & inference optimization
---

**논문 정보**
- **Date**: 2025-01-02
- **Reviewer**: 김재희
- **Property**: DiffusionLM, Pre-training

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/957d5b53-7f78-4268-aef0-e138690a817f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GJGWF6Q%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChBFfEdmLI5zt6uYOcOA6p5h6vNTD1LX46ChXjhpGNaQIhAKp7LVkP%2FEbQV58iAfeBAa2OF4YaRZpnGwNdFIqces8aKogECNT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgweAPxru%2Fo6iNvssZ0q3AP%2Fxhjl9LPq8kFS7bN4G1YjQED50zK9WhrGsvPbXarK9hHZfGOgI%2B0bAvuaQUhtSY5T0ZX5Isd13hCrabyCNNxV5ByIdusO9J4hVMkeozfBCLBE1%2FWTkiQTPC3oi%2FkYTruAWvye3LeHacl09gqrA5ihVOe4QwOFMmrRMWqD39Swxkfq2U%2BLDgpXMNrpYS6bdUJRbI3mkYvry5C4wDws9pgyKzNE0FRWhKrxQZ7RehWyeYKvQ%2BFYiJLeh1b7x7n4%2BusM3tmIdJqFF4Qvly2q2C1F1FvvI6ggEV7mYsWigqfJIdfPVtG1r7srZyX4DxEMUbgZoGROfRK5oG2EDde8WNjh5YMe6Vmf5oHd%2B2c86QaytPffRPcfAQnxKv0hnDz6vjhmFO2qKx8v60%2FusFL4ha2wKf8pV1fWP3JLCEcr7oqQ%2FLaS7ykLA%2FFwqIUEUhiDxeyDEuc6ZYprqXD8oricx0w%2FlF2kXV5L9sUlwb8RhD9i1qlry54VdWv9Mc18umNRRZ56XFSTK1kK1QZR0lpwu3AON%2BMdFPkSWSxup%2F%2BRddzJ%2FfgOSO4Wu6T501LSCTzHdZvi5mmnhOx4H2cdLIKFo3D%2BfKxqgnCCgq0EaRNOoLLrsXNcuy3sb%2Btipz4%2BSTCt%2F%2BHEBjqkAWduoxBLeGPOdsxk%2FRCaXJDJ%2FAAI52bMUH8a3zkurMU%2Boz20G14FYh9IaEDzifUwq2outZViS39X4QBID15o7vWQUgHdFfik7wIssY5OLnRl7ONfnYXiHDeoGskmRQ8L%2F8JWsLNTBbfiWwvR2EOt0doxIMfP4bGUo5AD%2BVIZg1wORj6R3ob9psFW4zDnr8AWQHAiMJu7gT7P2Eme8s3yHWMCXc0k&X-Amz-Signature=1e19cf2f3199b56d7a45955bbe5c64760a2c9b698c7ea17d6b5cbb8ffa8dd104&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# Preliminary

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/c599ee51-549c-4cff-910c-da532df44548/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GJGWF6Q%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChBFfEdmLI5zt6uYOcOA6p5h6vNTD1LX46ChXjhpGNaQIhAKp7LVkP%2FEbQV58iAfeBAa2OF4YaRZpnGwNdFIqces8aKogECNT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgweAPxru%2Fo6iNvssZ0q3AP%2Fxhjl9LPq8kFS7bN4G1YjQED50zK9WhrGsvPbXarK9hHZfGOgI%2B0bAvuaQUhtSY5T0ZX5Isd13hCrabyCNNxV5ByIdusO9J4hVMkeozfBCLBE1%2FWTkiQTPC3oi%2FkYTruAWvye3LeHacl09gqrA5ihVOe4QwOFMmrRMWqD39Swxkfq2U%2BLDgpXMNrpYS6bdUJRbI3mkYvry5C4wDws9pgyKzNE0FRWhKrxQZ7RehWyeYKvQ%2BFYiJLeh1b7x7n4%2BusM3tmIdJqFF4Qvly2q2C1F1FvvI6ggEV7mYsWigqfJIdfPVtG1r7srZyX4DxEMUbgZoGROfRK5oG2EDde8WNjh5YMe6Vmf5oHd%2B2c86QaytPffRPcfAQnxKv0hnDz6vjhmFO2qKx8v60%2FusFL4ha2wKf8pV1fWP3JLCEcr7oqQ%2FLaS7ykLA%2FFwqIUEUhiDxeyDEuc6ZYprqXD8oricx0w%2FlF2kXV5L9sUlwb8RhD9i1qlry54VdWv9Mc18umNRRZ56XFSTK1kK1QZR0lpwu3AON%2BMdFPkSWSxup%2F%2BRddzJ%2FfgOSO4Wu6T501LSCTzHdZvi5mmnhOx4H2cdLIKFo3D%2BfKxqgnCCgq0EaRNOoLLrsXNcuy3sb%2Btipz4%2BSTCt%2F%2BHEBjqkAWduoxBLeGPOdsxk%2FRCaXJDJ%2FAAI52bMUH8a3zkurMU%2Boz20G14FYh9IaEDzifUwq2outZViS39X4QBID15o7vWQUgHdFfik7wIssY5OLnRl7ONfnYXiHDeoGskmRQ8L%2F8JWsLNTBbfiWwvR2EOt0doxIMfP4bGUo5AD%2BVIZg1wORj6R3ob9psFW4zDnr8AWQHAiMJu7gT7P2Eme8s3yHWMCXc0k&X-Amz-Signature=10f69c359b3317d614d873fbe5d572dc301896afa53e8d94761d1bb7e86fd87c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Forward process: 원본 데이터에 대해 일정 비율의 노이즈를 입력하여 훼손하는 과정

- Backward process: t번 훼손된 데이터에 대하여 s번 훼손된 데이터로 복원하는 과정 (t > s)

- training objective function

# MDLM(Masked Diffusion Language Model)

## 텍스트 도메인의 특징 (뇌피셜)

1. text: 매우 고밀도의 정보가 보존된 도메인. 이미지와 다르게 정보량이 거의 없는 변수가 적음

1. discrete: 단어는 존재하거나, 존재하지 않는 binary한 변수임

## 수식 전개 Discrete Diffusion

\textit{V} =  [사과, 존맛탱, mask]

입력문장: 사과 존맛탱

### forward process: 노이즈를 주입, actual token → mask

q\left(\mathbf{z}_t \mid \mathbf{x}\right)=\operatorname{Cat}\left(\mathbf{z}_t ; \alpha_t \mathbf{x}+\left(1-\alpha_t\right) \boldsymbol{\pi}\right)

- Terms

- 설명

⇒ 매 시점마다 점차 많은 토큰들이 mask 토큰으로 전환됨

### reverse posterior: 노이즈를 복원, mask → actual token

reverse posterior

q\left(\mathbf{z}_s \mid \mathbf{z}_t, \mathbf{x}\right)=\operatorname{Cat}\left(\mathbf{z}_s ;\frac{\left[\alpha_{t \mid s} \mathbf{z}_t+\left(1-\alpha_{t \mid s}\right) \mathbf{1} \boldsymbol{\pi}^{\top} \mathbf{z}_t\right] \odot\left[\alpha_s \mathbf{x}+\left(1-\alpha_s\right) \boldsymbol{\pi}\right]}{\alpha_t \mathbf{z}_t^{\top} \mathbf{x}+\left(1-\alpha_t\right) \mathbf{z}_t^{\top} \boldsymbol{\pi}}\right)

- t step에서 이전 시점 s(<t)까지 노이즈를 복원하기 위한 추정 확률 

## Masked Diffusion

### forward masking process

q\left(\mathbf{z}_t \mid \mathbf{x}\right)=\operatorname{Cat}\left(\mathbf{z}_t ; \alpha_t \mathbf{x}+\left(1-\alpha_t\right) \boldsymbol{m}\right)

- discrete diffusion에서 \pi가 m으로 변한 것 외에 차이 없습니다. 

### reverse posterior: 실제 loss 식을 산출하기 위해 필요한 항

q\left(\mathbf{z}_s \mid \mathbf{z}_t, \mathbf{x}\right)= \begin{cases}\operatorname{Cat}\left(\mathbf{z}_s ; \mathbf{z}_t\right) & \mathbf{z}_t \neq \mathbf{m} \\ \operatorname{Cat}\left(\mathbf{z}_s ; \frac{\left(1-\alpha_s\right) \mathbf{m}+\left(\alpha_s-\alpha_t\right) \mathbf{x}}{1-\alpha_t}\right) & \mathbf{z}_t=\mathbf{m}\end{cases}

- \textbf{z}_t \neq \textbf{m}: step t에서 원본토큰이라면 → 그대로 유지

- \textbf{z} = \textbf{m}: step t에서 masking token이라면 → step s에서 t 사이에서 masking되었을 확률 산출

### MDLM의 상황에 맞춘 2가지 property

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/4a949d85-7216-447e-845e-2f8c8b60316a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GJGWF6Q%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChBFfEdmLI5zt6uYOcOA6p5h6vNTD1LX46ChXjhpGNaQIhAKp7LVkP%2FEbQV58iAfeBAa2OF4YaRZpnGwNdFIqces8aKogECNT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgweAPxru%2Fo6iNvssZ0q3AP%2Fxhjl9LPq8kFS7bN4G1YjQED50zK9WhrGsvPbXarK9hHZfGOgI%2B0bAvuaQUhtSY5T0ZX5Isd13hCrabyCNNxV5ByIdusO9J4hVMkeozfBCLBE1%2FWTkiQTPC3oi%2FkYTruAWvye3LeHacl09gqrA5ihVOe4QwOFMmrRMWqD39Swxkfq2U%2BLDgpXMNrpYS6bdUJRbI3mkYvry5C4wDws9pgyKzNE0FRWhKrxQZ7RehWyeYKvQ%2BFYiJLeh1b7x7n4%2BusM3tmIdJqFF4Qvly2q2C1F1FvvI6ggEV7mYsWigqfJIdfPVtG1r7srZyX4DxEMUbgZoGROfRK5oG2EDde8WNjh5YMe6Vmf5oHd%2B2c86QaytPffRPcfAQnxKv0hnDz6vjhmFO2qKx8v60%2FusFL4ha2wKf8pV1fWP3JLCEcr7oqQ%2FLaS7ykLA%2FFwqIUEUhiDxeyDEuc6ZYprqXD8oricx0w%2FlF2kXV5L9sUlwb8RhD9i1qlry54VdWv9Mc18umNRRZ56XFSTK1kK1QZR0lpwu3AON%2BMdFPkSWSxup%2F%2BRddzJ%2FfgOSO4Wu6T501LSCTzHdZvi5mmnhOx4H2cdLIKFo3D%2BfKxqgnCCgq0EaRNOoLLrsXNcuy3sb%2Btipz4%2BSTCt%2F%2BHEBjqkAWduoxBLeGPOdsxk%2FRCaXJDJ%2FAAI52bMUH8a3zkurMU%2Boz20G14FYh9IaEDzifUwq2outZViS39X4QBID15o7vWQUgHdFfik7wIssY5OLnRl7ONfnYXiHDeoGskmRQ8L%2F8JWsLNTBbfiWwvR2EOt0doxIMfP4bGUo5AD%2BVIZg1wORj6R3ob9psFW4zDnr8AWQHAiMJu7gT7P2Eme8s3yHWMCXc0k&X-Amz-Signature=38624f2e0168e67ad685b364374c943d58c952c255ecd224893aa65636a84eb7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

1. Zero Masking Probabilities: <\textbf{x}, \textbf{m}>=0임. 즉, 원본 토큰 중에는 masking token이 사용되지 않음

1. Carry-Over Unmasking: step t에서 복원(unmasking)된 토큰은 이후 모델의 복원 과정에서 수정되지 않음

### Rao-Balckwellized Likelihood Bounds

diffusion loss를 산출하듯이 본래 학습할 discrete-time diffusion의 loss의 lower bound를 산출하면 아래와 같음

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/e3eaf5eb-6db5-477d-b805-db48e101bff0/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GJGWF6Q%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChBFfEdmLI5zt6uYOcOA6p5h6vNTD1LX46ChXjhpGNaQIhAKp7LVkP%2FEbQV58iAfeBAa2OF4YaRZpnGwNdFIqces8aKogECNT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgweAPxru%2Fo6iNvssZ0q3AP%2Fxhjl9LPq8kFS7bN4G1YjQED50zK9WhrGsvPbXarK9hHZfGOgI%2B0bAvuaQUhtSY5T0ZX5Isd13hCrabyCNNxV5ByIdusO9J4hVMkeozfBCLBE1%2FWTkiQTPC3oi%2FkYTruAWvye3LeHacl09gqrA5ihVOe4QwOFMmrRMWqD39Swxkfq2U%2BLDgpXMNrpYS6bdUJRbI3mkYvry5C4wDws9pgyKzNE0FRWhKrxQZ7RehWyeYKvQ%2BFYiJLeh1b7x7n4%2BusM3tmIdJqFF4Qvly2q2C1F1FvvI6ggEV7mYsWigqfJIdfPVtG1r7srZyX4DxEMUbgZoGROfRK5oG2EDde8WNjh5YMe6Vmf5oHd%2B2c86QaytPffRPcfAQnxKv0hnDz6vjhmFO2qKx8v60%2FusFL4ha2wKf8pV1fWP3JLCEcr7oqQ%2FLaS7ykLA%2FFwqIUEUhiDxeyDEuc6ZYprqXD8oricx0w%2FlF2kXV5L9sUlwb8RhD9i1qlry54VdWv9Mc18umNRRZ56XFSTK1kK1QZR0lpwu3AON%2BMdFPkSWSxup%2F%2BRddzJ%2FfgOSO4Wu6T501LSCTzHdZvi5mmnhOx4H2cdLIKFo3D%2BfKxqgnCCgq0EaRNOoLLrsXNcuy3sb%2Btipz4%2BSTCt%2F%2BHEBjqkAWduoxBLeGPOdsxk%2FRCaXJDJ%2FAAI52bMUH8a3zkurMU%2Boz20G14FYh9IaEDzifUwq2outZViS39X4QBID15o7vWQUgHdFfik7wIssY5OLnRl7ONfnYXiHDeoGskmRQ8L%2F8JWsLNTBbfiWwvR2EOt0doxIMfP4bGUo5AD%2BVIZg1wORj6R3ob9psFW4zDnr8AWQHAiMJu7gT7P2Eme8s3yHWMCXc0k&X-Amz-Signature=03b3efc4db5cb8414d0f6fe72f7934d6f9874a096e65f4bb7af6c36e8a44359d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Continuous-Time Likelihood Bounds

기존 연구에서 정리하기로 T \to \infin로 정의할 경우 더욱 tight한 lower bound를 산출할 수 있음

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/047cc652-b041-4100-b946-d255f67fcf9f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GJGWF6Q%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChBFfEdmLI5zt6uYOcOA6p5h6vNTD1LX46ChXjhpGNaQIhAKp7LVkP%2FEbQV58iAfeBAa2OF4YaRZpnGwNdFIqces8aKogECNT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgweAPxru%2Fo6iNvssZ0q3AP%2Fxhjl9LPq8kFS7bN4G1YjQED50zK9WhrGsvPbXarK9hHZfGOgI%2B0bAvuaQUhtSY5T0ZX5Isd13hCrabyCNNxV5ByIdusO9J4hVMkeozfBCLBE1%2FWTkiQTPC3oi%2FkYTruAWvye3LeHacl09gqrA5ihVOe4QwOFMmrRMWqD39Swxkfq2U%2BLDgpXMNrpYS6bdUJRbI3mkYvry5C4wDws9pgyKzNE0FRWhKrxQZ7RehWyeYKvQ%2BFYiJLeh1b7x7n4%2BusM3tmIdJqFF4Qvly2q2C1F1FvvI6ggEV7mYsWigqfJIdfPVtG1r7srZyX4DxEMUbgZoGROfRK5oG2EDde8WNjh5YMe6Vmf5oHd%2B2c86QaytPffRPcfAQnxKv0hnDz6vjhmFO2qKx8v60%2FusFL4ha2wKf8pV1fWP3JLCEcr7oqQ%2FLaS7ykLA%2FFwqIUEUhiDxeyDEuc6ZYprqXD8oricx0w%2FlF2kXV5L9sUlwb8RhD9i1qlry54VdWv9Mc18umNRRZ56XFSTK1kK1QZR0lpwu3AON%2BMdFPkSWSxup%2F%2BRddzJ%2FfgOSO4Wu6T501LSCTzHdZvi5mmnhOx4H2cdLIKFo3D%2BfKxqgnCCgq0EaRNOoLLrsXNcuy3sb%2Btipz4%2BSTCt%2F%2BHEBjqkAWduoxBLeGPOdsxk%2FRCaXJDJ%2FAAI52bMUH8a3zkurMU%2Boz20G14FYh9IaEDzifUwq2outZViS39X4QBID15o7vWQUgHdFfik7wIssY5OLnRl7ONfnYXiHDeoGskmRQ8L%2F8JWsLNTBbfiWwvR2EOt0doxIMfP4bGUo5AD%2BVIZg1wORj6R3ob9psFW4zDnr8AWQHAiMJu7gT7P2Eme8s3yHWMCXc0k&X-Amz-Signature=44cce2368c74beb91fb5deb3fd03d23c1cc4d4f9096782ca2d9f8a994d117571&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Masked Diffusion Language Models

앞에서 정의된 tight한 lower bound를 language modeling 상황으로 가져오기 위해 아래 가정들을 적용할 수 있음

1. \textbf{x}^{1:L}: L개의 token sequence

1. \textbf{x}^\textit{l}: \textit{l}번째 토큰

1. forward와 backward 모두 각 토큰들이 독립적으로 진행

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/86b0ed88-f0e4-47b2-94af-5fcf1d863627/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GJGWF6Q%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChBFfEdmLI5zt6uYOcOA6p5h6vNTD1LX46ChXjhpGNaQIhAKp7LVkP%2FEbQV58iAfeBAa2OF4YaRZpnGwNdFIqces8aKogECNT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgweAPxru%2Fo6iNvssZ0q3AP%2Fxhjl9LPq8kFS7bN4G1YjQED50zK9WhrGsvPbXarK9hHZfGOgI%2B0bAvuaQUhtSY5T0ZX5Isd13hCrabyCNNxV5ByIdusO9J4hVMkeozfBCLBE1%2FWTkiQTPC3oi%2FkYTruAWvye3LeHacl09gqrA5ihVOe4QwOFMmrRMWqD39Swxkfq2U%2BLDgpXMNrpYS6bdUJRbI3mkYvry5C4wDws9pgyKzNE0FRWhKrxQZ7RehWyeYKvQ%2BFYiJLeh1b7x7n4%2BusM3tmIdJqFF4Qvly2q2C1F1FvvI6ggEV7mYsWigqfJIdfPVtG1r7srZyX4DxEMUbgZoGROfRK5oG2EDde8WNjh5YMe6Vmf5oHd%2B2c86QaytPffRPcfAQnxKv0hnDz6vjhmFO2qKx8v60%2FusFL4ha2wKf8pV1fWP3JLCEcr7oqQ%2FLaS7ykLA%2FFwqIUEUhiDxeyDEuc6ZYprqXD8oricx0w%2FlF2kXV5L9sUlwb8RhD9i1qlry54VdWv9Mc18umNRRZ56XFSTK1kK1QZR0lpwu3AON%2BMdFPkSWSxup%2F%2BRddzJ%2FfgOSO4Wu6T501LSCTzHdZvi5mmnhOx4H2cdLIKFo3D%2BfKxqgnCCgq0EaRNOoLLrsXNcuy3sb%2Btipz4%2BSTCt%2F%2BHEBjqkAWduoxBLeGPOdsxk%2FRCaXJDJ%2FAAI52bMUH8a3zkurMU%2Boz20G14FYh9IaEDzifUwq2outZViS39X4QBID15o7vWQUgHdFfik7wIssY5OLnRl7ONfnYXiHDeoGskmRQ8L%2F8JWsLNTBbfiWwvR2EOt0doxIMfP4bGUo5AD%2BVIZg1wORj6R3ob9psFW4zDnr8AWQHAiMJu7gT7P2Eme8s3yHWMCXc0k&X-Amz-Signature=97de97d03074e0526ad3c94a1081000bf43c87c0157e4f17571b73d2e3dc20e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/21f1eebf-a486-4a9b-a8c6-5ef25daa6960/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GJGWF6Q%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChBFfEdmLI5zt6uYOcOA6p5h6vNTD1LX46ChXjhpGNaQIhAKp7LVkP%2FEbQV58iAfeBAa2OF4YaRZpnGwNdFIqces8aKogECNT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgweAPxru%2Fo6iNvssZ0q3AP%2Fxhjl9LPq8kFS7bN4G1YjQED50zK9WhrGsvPbXarK9hHZfGOgI%2B0bAvuaQUhtSY5T0ZX5Isd13hCrabyCNNxV5ByIdusO9J4hVMkeozfBCLBE1%2FWTkiQTPC3oi%2FkYTruAWvye3LeHacl09gqrA5ihVOe4QwOFMmrRMWqD39Swxkfq2U%2BLDgpXMNrpYS6bdUJRbI3mkYvry5C4wDws9pgyKzNE0FRWhKrxQZ7RehWyeYKvQ%2BFYiJLeh1b7x7n4%2BusM3tmIdJqFF4Qvly2q2C1F1FvvI6ggEV7mYsWigqfJIdfPVtG1r7srZyX4DxEMUbgZoGROfRK5oG2EDde8WNjh5YMe6Vmf5oHd%2B2c86QaytPffRPcfAQnxKv0hnDz6vjhmFO2qKx8v60%2FusFL4ha2wKf8pV1fWP3JLCEcr7oqQ%2FLaS7ykLA%2FFwqIUEUhiDxeyDEuc6ZYprqXD8oricx0w%2FlF2kXV5L9sUlwb8RhD9i1qlry54VdWv9Mc18umNRRZ56XFSTK1kK1QZR0lpwu3AON%2BMdFPkSWSxup%2F%2BRddzJ%2FfgOSO4Wu6T501LSCTzHdZvi5mmnhOx4H2cdLIKFo3D%2BfKxqgnCCgq0EaRNOoLLrsXNcuy3sb%2Btipz4%2BSTCt%2F%2BHEBjqkAWduoxBLeGPOdsxk%2FRCaXJDJ%2FAAI52bMUH8a3zkurMU%2Boz20G14FYh9IaEDzifUwq2outZViS39X4QBID15o7vWQUgHdFfik7wIssY5OLnRl7ONfnYXiHDeoGskmRQ8L%2F8JWsLNTBbfiWwvR2EOt0doxIMfP4bGUo5AD%2BVIZg1wORj6R3ob9psFW4zDnr8AWQHAiMJu7gT7P2Eme8s3yHWMCXc0k&X-Amz-Signature=a0e1b23fe86c1720a5feb62871146f9fce2c056c334507397cd9e29c39f79ec1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- \textbf{x}^\textit{l}_\theta(\textbf{z}_t^{1:L}, t): t번째 step에서의 시퀀스에 대한 모델의 예측 문장, masking된 토큰을 예측하여 복원한 문장문

- \log<\textbf{x}^\textit{l}_\theta(\textbf{z}_t^{1:L}, t), \textbf{x}^\textit{l}>: loglikelihood, 갑자기요…?!

- 이때 \alpha_s 가 사라진 것을 확인할 수 있음

### Training Algorithm

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/2900feab-6cf6-486d-83b8-26816f816a5e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GJGWF6Q%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChBFfEdmLI5zt6uYOcOA6p5h6vNTD1LX46ChXjhpGNaQIhAKp7LVkP%2FEbQV58iAfeBAa2OF4YaRZpnGwNdFIqces8aKogECNT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgweAPxru%2Fo6iNvssZ0q3AP%2Fxhjl9LPq8kFS7bN4G1YjQED50zK9WhrGsvPbXarK9hHZfGOgI%2B0bAvuaQUhtSY5T0ZX5Isd13hCrabyCNNxV5ByIdusO9J4hVMkeozfBCLBE1%2FWTkiQTPC3oi%2FkYTruAWvye3LeHacl09gqrA5ihVOe4QwOFMmrRMWqD39Swxkfq2U%2BLDgpXMNrpYS6bdUJRbI3mkYvry5C4wDws9pgyKzNE0FRWhKrxQZ7RehWyeYKvQ%2BFYiJLeh1b7x7n4%2BusM3tmIdJqFF4Qvly2q2C1F1FvvI6ggEV7mYsWigqfJIdfPVtG1r7srZyX4DxEMUbgZoGROfRK5oG2EDde8WNjh5YMe6Vmf5oHd%2B2c86QaytPffRPcfAQnxKv0hnDz6vjhmFO2qKx8v60%2FusFL4ha2wKf8pV1fWP3JLCEcr7oqQ%2FLaS7ykLA%2FFwqIUEUhiDxeyDEuc6ZYprqXD8oricx0w%2FlF2kXV5L9sUlwb8RhD9i1qlry54VdWv9Mc18umNRRZ56XFSTK1kK1QZR0lpwu3AON%2BMdFPkSWSxup%2F%2BRddzJ%2FfgOSO4Wu6T501LSCTzHdZvi5mmnhOx4H2cdLIKFo3D%2BfKxqgnCCgq0EaRNOoLLrsXNcuy3sb%2Btipz4%2BSTCt%2F%2BHEBjqkAWduoxBLeGPOdsxk%2FRCaXJDJ%2FAAI52bMUH8a3zkurMU%2Boz20G14FYh9IaEDzifUwq2outZViS39X4QBID15o7vWQUgHdFfik7wIssY5OLnRl7ONfnYXiHDeoGskmRQ8L%2F8JWsLNTBbfiWwvR2EOt0doxIMfP4bGUo5AD%2BVIZg1wORj6R3ob9psFW4zDnr8AWQHAiMJu7gT7P2Eme8s3yHWMCXc0k&X-Amz-Signature=0dc68b165245531eebee5377406e3b9516ae7bc0e5517cf4726752ce1a4e2471&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

1. 데이터 sampling

1. step sampling

1. 이전 step 대비 추가적으로 \alpha_t 비율을 masking한  masked input 산출

1. weighted sum of MLM loss 형식으로 update

## Actual Inference

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/d2e666a0-4261-49de-857b-871b0c42a118/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GJGWF6Q%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChBFfEdmLI5zt6uYOcOA6p5h6vNTD1LX46ChXjhpGNaQIhAKp7LVkP%2FEbQV58iAfeBAa2OF4YaRZpnGwNdFIqces8aKogECNT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgweAPxru%2Fo6iNvssZ0q3AP%2Fxhjl9LPq8kFS7bN4G1YjQED50zK9WhrGsvPbXarK9hHZfGOgI%2B0bAvuaQUhtSY5T0ZX5Isd13hCrabyCNNxV5ByIdusO9J4hVMkeozfBCLBE1%2FWTkiQTPC3oi%2FkYTruAWvye3LeHacl09gqrA5ihVOe4QwOFMmrRMWqD39Swxkfq2U%2BLDgpXMNrpYS6bdUJRbI3mkYvry5C4wDws9pgyKzNE0FRWhKrxQZ7RehWyeYKvQ%2BFYiJLeh1b7x7n4%2BusM3tmIdJqFF4Qvly2q2C1F1FvvI6ggEV7mYsWigqfJIdfPVtG1r7srZyX4DxEMUbgZoGROfRK5oG2EDde8WNjh5YMe6Vmf5oHd%2B2c86QaytPffRPcfAQnxKv0hnDz6vjhmFO2qKx8v60%2FusFL4ha2wKf8pV1fWP3JLCEcr7oqQ%2FLaS7ykLA%2FFwqIUEUhiDxeyDEuc6ZYprqXD8oricx0w%2FlF2kXV5L9sUlwb8RhD9i1qlry54VdWv9Mc18umNRRZ56XFSTK1kK1QZR0lpwu3AON%2BMdFPkSWSxup%2F%2BRddzJ%2FfgOSO4Wu6T501LSCTzHdZvi5mmnhOx4H2cdLIKFo3D%2BfKxqgnCCgq0EaRNOoLLrsXNcuy3sb%2Btipz4%2BSTCt%2F%2BHEBjqkAWduoxBLeGPOdsxk%2FRCaXJDJ%2FAAI52bMUH8a3zkurMU%2Boz20G14FYh9IaEDzifUwq2outZViS39X4QBID15o7vWQUgHdFfik7wIssY5OLnRl7ONfnYXiHDeoGskmRQ8L%2F8JWsLNTBbfiWwvR2EOt0doxIMfP4bGUo5AD%2BVIZg1wORj6R3ob9psFW4zDnr8AWQHAiMJu7gT7P2Eme8s3yHWMCXc0k&X-Amz-Signature=782635cd1151d565157c72aa48606dc839f150e0be16e12e90806632da229197&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

해당 수식을 통해 실제 생성이 이루어지게 됨

1. \textbf{z}_t = \textbf{m}: t step에서 mask 토큰으로 입력된 위치에 대해서만 예측 수행

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/444ac4d9-3787-4636-ad4b-914abf9b6cbf/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GJGWF6Q%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChBFfEdmLI5zt6uYOcOA6p5h6vNTD1LX46ChXjhpGNaQIhAKp7LVkP%2FEbQV58iAfeBAa2OF4YaRZpnGwNdFIqces8aKogECNT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgweAPxru%2Fo6iNvssZ0q3AP%2Fxhjl9LPq8kFS7bN4G1YjQED50zK9WhrGsvPbXarK9hHZfGOgI%2B0bAvuaQUhtSY5T0ZX5Isd13hCrabyCNNxV5ByIdusO9J4hVMkeozfBCLBE1%2FWTkiQTPC3oi%2FkYTruAWvye3LeHacl09gqrA5ihVOe4QwOFMmrRMWqD39Swxkfq2U%2BLDgpXMNrpYS6bdUJRbI3mkYvry5C4wDws9pgyKzNE0FRWhKrxQZ7RehWyeYKvQ%2BFYiJLeh1b7x7n4%2BusM3tmIdJqFF4Qvly2q2C1F1FvvI6ggEV7mYsWigqfJIdfPVtG1r7srZyX4DxEMUbgZoGROfRK5oG2EDde8WNjh5YMe6Vmf5oHd%2B2c86QaytPffRPcfAQnxKv0hnDz6vjhmFO2qKx8v60%2FusFL4ha2wKf8pV1fWP3JLCEcr7oqQ%2FLaS7ykLA%2FFwqIUEUhiDxeyDEuc6ZYprqXD8oricx0w%2FlF2kXV5L9sUlwb8RhD9i1qlry54VdWv9Mc18umNRRZ56XFSTK1kK1QZR0lpwu3AON%2BMdFPkSWSxup%2F%2BRddzJ%2FfgOSO4Wu6T501LSCTzHdZvi5mmnhOx4H2cdLIKFo3D%2BfKxqgnCCgq0EaRNOoLLrsXNcuy3sb%2Btipz4%2BSTCt%2F%2BHEBjqkAWduoxBLeGPOdsxk%2FRCaXJDJ%2FAAI52bMUH8a3zkurMU%2Boz20G14FYh9IaEDzifUwq2outZViS39X4QBID15o7vWQUgHdFfik7wIssY5OLnRl7ONfnYXiHDeoGskmRQ8L%2F8JWsLNTBbfiWwvR2EOt0doxIMfP4bGUo5AD%2BVIZg1wORj6R3ob9psFW4zDnr8AWQHAiMJu7gT7P2Eme8s3yHWMCXc0k&X-Amz-Signature=1d14290f3e033c9f4759662e1f62167064bb908ac2131c272c2f14cafc0808e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

1. \frac{(1-\alpha_s)\textbf{m} + (\alpha_s - \alpha_t)\textbf{x}_\theta(\textbf{z}_t, t)}{1-\alpha_t} = \frac{1-\alpha_s}{1-\alpha_t}\textbf{m} + \frac{\alpha_s-\alpha_t}{1-\alpha_t}\textbf{x}_\theta(\textbf{z}_t, t): 모든 mask 토큰 위치에서 예측된 확률분포 중에서 \frac{1-\alpha_s}{1-\alpha_t} 비율은 다시 masking으로 돌림

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/f46d1e04-1de1-49d7-b53a-e7f95a2aba5e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GJGWF6Q%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChBFfEdmLI5zt6uYOcOA6p5h6vNTD1LX46ChXjhpGNaQIhAKp7LVkP%2FEbQV58iAfeBAa2OF4YaRZpnGwNdFIqces8aKogECNT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgweAPxru%2Fo6iNvssZ0q3AP%2Fxhjl9LPq8kFS7bN4G1YjQED50zK9WhrGsvPbXarK9hHZfGOgI%2B0bAvuaQUhtSY5T0ZX5Isd13hCrabyCNNxV5ByIdusO9J4hVMkeozfBCLBE1%2FWTkiQTPC3oi%2FkYTruAWvye3LeHacl09gqrA5ihVOe4QwOFMmrRMWqD39Swxkfq2U%2BLDgpXMNrpYS6bdUJRbI3mkYvry5C4wDws9pgyKzNE0FRWhKrxQZ7RehWyeYKvQ%2BFYiJLeh1b7x7n4%2BusM3tmIdJqFF4Qvly2q2C1F1FvvI6ggEV7mYsWigqfJIdfPVtG1r7srZyX4DxEMUbgZoGROfRK5oG2EDde8WNjh5YMe6Vmf5oHd%2B2c86QaytPffRPcfAQnxKv0hnDz6vjhmFO2qKx8v60%2FusFL4ha2wKf8pV1fWP3JLCEcr7oqQ%2FLaS7ykLA%2FFwqIUEUhiDxeyDEuc6ZYprqXD8oricx0w%2FlF2kXV5L9sUlwb8RhD9i1qlry54VdWv9Mc18umNRRZ56XFSTK1kK1QZR0lpwu3AON%2BMdFPkSWSxup%2F%2BRddzJ%2FfgOSO4Wu6T501LSCTzHdZvi5mmnhOx4H2cdLIKFo3D%2BfKxqgnCCgq0EaRNOoLLrsXNcuy3sb%2Btipz4%2BSTCt%2F%2BHEBjqkAWduoxBLeGPOdsxk%2FRCaXJDJ%2FAAI52bMUH8a3zkurMU%2Boz20G14FYh9IaEDzifUwq2outZViS39X4QBID15o7vWQUgHdFfik7wIssY5OLnRl7ONfnYXiHDeoGskmRQ8L%2F8JWsLNTBbfiWwvR2EOt0doxIMfP4bGUo5AD%2BVIZg1wORj6R3ob9psFW4zDnr8AWQHAiMJu7gT7P2Eme8s3yHWMCXc0k&X-Amz-Signature=fc9b4996ad5422cb6bb9a29601fc93ea9f1b1ca985fc54c6f14a1dfcd365bec7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

⇒ 매 iteration 마다 \frac{\alpha_s - \alpha_t}{1-\alpha_t}만큼의 토큰이 복원되면서 생성

# Experiments

### 1. Perplexity evaluation

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/51d026ce-8e3f-4fd1-99d4-1e9edb825916/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GJGWF6Q%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChBFfEdmLI5zt6uYOcOA6p5h6vNTD1LX46ChXjhpGNaQIhAKp7LVkP%2FEbQV58iAfeBAa2OF4YaRZpnGwNdFIqces8aKogECNT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgweAPxru%2Fo6iNvssZ0q3AP%2Fxhjl9LPq8kFS7bN4G1YjQED50zK9WhrGsvPbXarK9hHZfGOgI%2B0bAvuaQUhtSY5T0ZX5Isd13hCrabyCNNxV5ByIdusO9J4hVMkeozfBCLBE1%2FWTkiQTPC3oi%2FkYTruAWvye3LeHacl09gqrA5ihVOe4QwOFMmrRMWqD39Swxkfq2U%2BLDgpXMNrpYS6bdUJRbI3mkYvry5C4wDws9pgyKzNE0FRWhKrxQZ7RehWyeYKvQ%2BFYiJLeh1b7x7n4%2BusM3tmIdJqFF4Qvly2q2C1F1FvvI6ggEV7mYsWigqfJIdfPVtG1r7srZyX4DxEMUbgZoGROfRK5oG2EDde8WNjh5YMe6Vmf5oHd%2B2c86QaytPffRPcfAQnxKv0hnDz6vjhmFO2qKx8v60%2FusFL4ha2wKf8pV1fWP3JLCEcr7oqQ%2FLaS7ykLA%2FFwqIUEUhiDxeyDEuc6ZYprqXD8oricx0w%2FlF2kXV5L9sUlwb8RhD9i1qlry54VdWv9Mc18umNRRZ56XFSTK1kK1QZR0lpwu3AON%2BMdFPkSWSxup%2F%2BRddzJ%2FfgOSO4Wu6T501LSCTzHdZvi5mmnhOx4H2cdLIKFo3D%2BfKxqgnCCgq0EaRNOoLLrsXNcuy3sb%2Btipz4%2BSTCt%2F%2BHEBjqkAWduoxBLeGPOdsxk%2FRCaXJDJ%2FAAI52bMUH8a3zkurMU%2Boz20G14FYh9IaEDzifUwq2outZViS39X4QBID15o7vWQUgHdFfik7wIssY5OLnRl7ONfnYXiHDeoGskmRQ8L%2F8JWsLNTBbfiWwvR2EOt0doxIMfP4bGUo5AD%2BVIZg1wORj6R3ob9psFW4zDnr8AWQHAiMJu7gT7P2Eme8s3yHWMCXc0k&X-Amz-Signature=0a4ca84df3fa4278ee2dafc8fb1b24958858da60ba1abaa681f6a16d69f40876&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 동일한 corpus를 이용하여 autoregressive model과 MDLM을 학습시켜 비교

### 2. Training NLL

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/2c10fdcc-8f02-458e-9b35-8ae60ad63344/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GJGWF6Q%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChBFfEdmLI5zt6uYOcOA6p5h6vNTD1LX46ChXjhpGNaQIhAKp7LVkP%2FEbQV58iAfeBAa2OF4YaRZpnGwNdFIqces8aKogECNT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgweAPxru%2Fo6iNvssZ0q3AP%2Fxhjl9LPq8kFS7bN4G1YjQED50zK9WhrGsvPbXarK9hHZfGOgI%2B0bAvuaQUhtSY5T0ZX5Isd13hCrabyCNNxV5ByIdusO9J4hVMkeozfBCLBE1%2FWTkiQTPC3oi%2FkYTruAWvye3LeHacl09gqrA5ihVOe4QwOFMmrRMWqD39Swxkfq2U%2BLDgpXMNrpYS6bdUJRbI3mkYvry5C4wDws9pgyKzNE0FRWhKrxQZ7RehWyeYKvQ%2BFYiJLeh1b7x7n4%2BusM3tmIdJqFF4Qvly2q2C1F1FvvI6ggEV7mYsWigqfJIdfPVtG1r7srZyX4DxEMUbgZoGROfRK5oG2EDde8WNjh5YMe6Vmf5oHd%2B2c86QaytPffRPcfAQnxKv0hnDz6vjhmFO2qKx8v60%2FusFL4ha2wKf8pV1fWP3JLCEcr7oqQ%2FLaS7ykLA%2FFwqIUEUhiDxeyDEuc6ZYprqXD8oricx0w%2FlF2kXV5L9sUlwb8RhD9i1qlry54VdWv9Mc18umNRRZ56XFSTK1kK1QZR0lpwu3AON%2BMdFPkSWSxup%2F%2BRddzJ%2FfgOSO4Wu6T501LSCTzHdZvi5mmnhOx4H2cdLIKFo3D%2BfKxqgnCCgq0EaRNOoLLrsXNcuy3sb%2Btipz4%2BSTCt%2F%2BHEBjqkAWduoxBLeGPOdsxk%2FRCaXJDJ%2FAAI52bMUH8a3zkurMU%2Boz20G14FYh9IaEDzifUwq2outZViS39X4QBID15o7vWQUgHdFfik7wIssY5OLnRl7ONfnYXiHDeoGskmRQ8L%2F8JWsLNTBbfiWwvR2EOt0doxIMfP4bGUo5AD%2BVIZg1wORj6R3ob9psFW4zDnr8AWQHAiMJu7gT7P2Eme8s3yHWMCXc0k&X-Amz-Signature=45844c07dedacffce40f3602488a753f852370d0a091a43aadd548aeaa320686&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 기존 DDLM(SEDD)보다 훨씬 안정적인 NLL을 보이며 학습

### 3. Zero-shot Perplexity

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/99480a95-157d-453b-9ddf-ba5927cb7298/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GJGWF6Q%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChBFfEdmLI5zt6uYOcOA6p5h6vNTD1LX46ChXjhpGNaQIhAKp7LVkP%2FEbQV58iAfeBAa2OF4YaRZpnGwNdFIqces8aKogECNT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgweAPxru%2Fo6iNvssZ0q3AP%2Fxhjl9LPq8kFS7bN4G1YjQED50zK9WhrGsvPbXarK9hHZfGOgI%2B0bAvuaQUhtSY5T0ZX5Isd13hCrabyCNNxV5ByIdusO9J4hVMkeozfBCLBE1%2FWTkiQTPC3oi%2FkYTruAWvye3LeHacl09gqrA5ihVOe4QwOFMmrRMWqD39Swxkfq2U%2BLDgpXMNrpYS6bdUJRbI3mkYvry5C4wDws9pgyKzNE0FRWhKrxQZ7RehWyeYKvQ%2BFYiJLeh1b7x7n4%2BusM3tmIdJqFF4Qvly2q2C1F1FvvI6ggEV7mYsWigqfJIdfPVtG1r7srZyX4DxEMUbgZoGROfRK5oG2EDde8WNjh5YMe6Vmf5oHd%2B2c86QaytPffRPcfAQnxKv0hnDz6vjhmFO2qKx8v60%2FusFL4ha2wKf8pV1fWP3JLCEcr7oqQ%2FLaS7ykLA%2FFwqIUEUhiDxeyDEuc6ZYprqXD8oricx0w%2FlF2kXV5L9sUlwb8RhD9i1qlry54VdWv9Mc18umNRRZ56XFSTK1kK1QZR0lpwu3AON%2BMdFPkSWSxup%2F%2BRddzJ%2FfgOSO4Wu6T501LSCTzHdZvi5mmnhOx4H2cdLIKFo3D%2BfKxqgnCCgq0EaRNOoLLrsXNcuy3sb%2Btipz4%2BSTCt%2F%2BHEBjqkAWduoxBLeGPOdsxk%2FRCaXJDJ%2FAAI52bMUH8a3zkurMU%2Boz20G14FYh9IaEDzifUwq2outZViS39X4QBID15o7vWQUgHdFfik7wIssY5OLnRl7ONfnYXiHDeoGskmRQ8L%2F8JWsLNTBbfiWwvR2EOt0doxIMfP4bGUo5AD%2BVIZg1wORj6R3ob9psFW4zDnr8AWQHAiMJu7gT7P2Eme8s3yHWMCXc0k&X-Amz-Signature=9252b374181b67afe4b75c0aa8f951fbb9564ded1e6968444ade03fe2722e7d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 다양한 분야에 대하여 AR과 근접한 수준의 성능 달성

### 4. Downstream Task

![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/3acbc979-3f43-48f4-8683-229c6104ec76/a06d904c-b3ef-4c4a-a841-868f41b432c9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GJGWF6Q%2F20250810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250810T113431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChBFfEdmLI5zt6uYOcOA6p5h6vNTD1LX46ChXjhpGNaQIhAKp7LVkP%2FEbQV58iAfeBAa2OF4YaRZpnGwNdFIqces8aKogECNT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgweAPxru%2Fo6iNvssZ0q3AP%2Fxhjl9LPq8kFS7bN4G1YjQED50zK9WhrGsvPbXarK9hHZfGOgI%2B0bAvuaQUhtSY5T0ZX5Isd13hCrabyCNNxV5ByIdusO9J4hVMkeozfBCLBE1%2FWTkiQTPC3oi%2FkYTruAWvye3LeHacl09gqrA5ihVOe4QwOFMmrRMWqD39Swxkfq2U%2BLDgpXMNrpYS6bdUJRbI3mkYvry5C4wDws9pgyKzNE0FRWhKrxQZ7RehWyeYKvQ%2BFYiJLeh1b7x7n4%2BusM3tmIdJqFF4Qvly2q2C1F1FvvI6ggEV7mYsWigqfJIdfPVtG1r7srZyX4DxEMUbgZoGROfRK5oG2EDde8WNjh5YMe6Vmf5oHd%2B2c86QaytPffRPcfAQnxKv0hnDz6vjhmFO2qKx8v60%2FusFL4ha2wKf8pV1fWP3JLCEcr7oqQ%2FLaS7ykLA%2FFwqIUEUhiDxeyDEuc6ZYprqXD8oricx0w%2FlF2kXV5L9sUlwb8RhD9i1qlry54VdWv9Mc18umNRRZ56XFSTK1kK1QZR0lpwu3AON%2BMdFPkSWSxup%2F%2BRddzJ%2FfgOSO4Wu6T501LSCTzHdZvi5mmnhOx4H2cdLIKFo3D%2BfKxqgnCCgq0EaRNOoLLrsXNcuy3sb%2Btipz4%2BSTCt%2F%2BHEBjqkAWduoxBLeGPOdsxk%2FRCaXJDJ%2FAAI52bMUH8a3zkurMU%2Boz20G14FYh9IaEDzifUwq2outZViS39X4QBID15o7vWQUgHdFfik7wIssY5OLnRl7ONfnYXiHDeoGskmRQ8L%2F8JWsLNTBbfiWwvR2EOt0doxIMfP4bGUo5AD%2BVIZg1wORj6R3ob9psFW4zDnr8AWQHAiMJu7gT7P2Eme8s3yHWMCXc0k&X-Amz-Signature=66442bf548699b2200c7774dab1884860f873df3e2904fdf0af066b9ae2a1f0c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- BERT를 MDLM으로 일부 finetune한 결과로 비교

# conclusion
