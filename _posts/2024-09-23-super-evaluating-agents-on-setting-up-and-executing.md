---
categories:
- paper-reviews
date: '2024-09-23 00:00:00'
description: 논문 리뷰 - Autonomous-Agents, Code Generation 관련 연구
giscus_comments: true
layout: post
related_posts: false
tags:
- autonomous-agents
- bert
- code generation
- fine-tuning
- gpt
- llm
- paper-review
- reasoning
- transformer
thumbnail: assets/img/posts/2024-09-23-super-evaluating-agents-on-setting-up-and-executing/thumbnail.jpg
title: 'SUPER: Evaluating Agents on Setting Up and Executing Tasks

  from Research Repositories'
---

**논문 정보**
- **Date**: 2024-09-23
- **Reviewer**: yukyung lee
- **Property**: Autonomous-Agents, Code Generation

## 1. Introduction

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-23-super-evaluating-agents-on-setting-up-and-executing/image_000.png" class="img-fluid rounded z-depth-1" %}

- Can LLMs automate theset up and execution of tasks in research repositories?

  - Experimentation frequently requires substantial effort to setup and execute them

    - installing the environment:

      - conﬁguration changes

      - resolv-ing outdated package dependencies

      - ﬁxing bugs

      - determining the correct execution commands

- both setting up and executing experiments using research repositories in-the-wild

## 2. Related work

### 1) Coding benchmarks

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-23-super-evaluating-agents-on-setting-up-and-executing/image_001.png" class="img-fluid rounded z-depth-1" %}

- Contributions

  - In contrast to these works,SUPER focuses onthe end-to-end task of setting up and executingresearch tasks in lower-proﬁle repositories, pre-senting a unique set of challenges, with tasks thatrequire repository comprehension and reasoning,editing multiple ﬁles, setting up the repository en-vironment for execution while interactively run-ning commands in the environment

### 2) LLM Agent

- Our benchmark introduces an importantnew domain that encourages the development ofLLM-based agents to assist researchers in their end to end research tasks with arbitrary repositories

## 3. Benchmark Construction

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-23-super-evaluating-agents-on-setting-up-and-executing/image_002.png" class="img-fluid rounded z-depth-1" %}

- SUPER benchmark (3 setting)

  - Expert set - contains manuallywritten problems, solved by experts. 

  - Masked set - contains sub-problems extracted from the Expert set using the gold solution, which pro-vide easier and more focused sub-problems.

  - Auto set -  contains automatically generated problemswhich can be used for development and improve-ment of agents

- Environment setup : Jupyter notebook as engine

  - Execute cells: system shell command & stateful python command

  - Each execution returns an observation string

  - https://modal.com

    - 2-3 cents per problem in Modal (**not including** API costs)


---

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-23-super-evaluating-agents-on-setting-up-and-executing/image_003.png" class="img-fluid rounded z-depth-1" %}

**Expert**: 45 end-to-end

- Manually written by “expert” programmers

- Ask for git commit hash, and any exceptional implementation decisions they had to make (which are specified to agent)

- Check that solutions are reproducible (up to error of 10-2)

**Masked**: 152 sub-problems from Expert

- Removes parts of expert-written code (“masks” them)

- Pre-execute existing cells and pass as history - code to be written by model not required to fit “in between” existing cells, can follow sequentially

  - In prompt history as [pre-executed by the user]

**Auto**:** **604 auto-generated examples

- state-of-the-art approaches struggle to solve these problems with the best model (GPT-4o) solving only **16.3% of the end-to-end** set, and **46.1% ofthe scenarios**.

## **4. Evaluation**

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-23-super-evaluating-agents-on-setting-up-and-executing/image_004.png" class="img-fluid rounded z-depth-1" %}

- replication of metrics

- Partial credit through “**landmarks**” (points in code signalling sub-completion, e.g. training stage done)

  - E.g., the explicit output string “***training completed ***” or the string “Loading data... 100%”

- Auto-generated: check no exceptions when running script (for a minimum duration)

  - use 10 seconds based on gold expert solutions

> “Open-source models substantially lag behind on both the sub-problems and end-to-end tasks.”

“agents are better at resolving well-specified sub-problems, such as solving exceptions, bugs, and other issues, than tasks requiring repository and file exploration to understand code structure”

**LLMs**

GPT-4o (gpt-4o-2024-08-06)

GPT-4o mini (gpt-4o-mini-2024-07-18)

Mixtral-8x22B-Instruct

Llama 3.1 70B

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-23-super-evaluating-agents-on-setting-up-and-executing/image_005.png" class="img-fluid rounded z-depth-1" %}

**Agents**

- Execute and submit commands

1. ReAct

<thought, action, observation>

**Truncation** strategies to keep context in limit (e.g. reduce size of training file output)

- For the **last step, we provide the 50k last characters**, which is usually enough for the entire observation. For **earlier steps, we shorten the observations to show the last 500 characters**.

1. ReAct-SUPER

  - **Result**

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-23-super-evaluating-agents-on-setting-up-and-executing/image_006.png" class="img-fluid rounded z-depth-1" %}

**Edit** action

- “ Specifically, the edit command accepts three parameters: the name of the file, the exact content of the lines to be replaced, and the content to replace it with.”

{filename}

<BEFORE_EDIT>

(lines before edit)

<AFTER_EDIT>

(lines after edit)

- The edit command requires the provided replaced lines to be (1) precisely copied, including correct whitespaces and indentations and (2) unique in the contents file, so that the edit command is not ambiguous. To help the agent with these requirements, we configure the edit command to provide specific feedback to the agent in case one of these conditions does not apply. (e.g. one without trailing whitespaces, or multiple occurrences if so, with 1-3 lines before/after for disambiguation)

- Execute and submit actions as well

1. SWE-Agent

  - Can read and scroll through file content

1. Reflection

  - *k tries to solve problem*

  - Only provides minor improvements

(1) reproducing numbers from research papers by running specific experiments

(2) running **modified** experiments with different datasets, models, or configurations

  - PapersWithCode repos with “Text” modality research papers (with repos from 2021 or after)

  - Tasks that involve running experiment in readme/script in repo

  - “Whenever possible, we make the task more challenging by requiring the experiment to be run on a new dataset or model, other than the one described in the available documentation

    - Either from HF datasets, or Google Drive link

    - “The challenge of running on a specific dataset varies in difficulty: it could involve only a single configuration line change if the dataset is already supported, or creating a new dataset reader, adjusting column names, etc.


---

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-23-super-evaluating-agents-on-setting-up-and-executing/image_007.png" class="img-fluid rounded z-depth-1" %}

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-23-super-evaluating-agents-on-setting-up-and-executing/image_008.png" class="img-fluid rounded z-depth-1" %}

Reduce computational requirements by reducing model size/training time/dataset size

- E.g. load first 10 examples only

- E.g. run one epoch

Other implementation instructions:

- Branch

- Certain HPs

- Seeds

{% include figure.liquid loading="eager" path="assets/img/posts/2024-09-23-super-evaluating-agents-on-setting-up-and-executing/image_009.png" class="img-fluid rounded z-depth-1" %}

# 5. Core Examples

**Hardest**: data (27%), configuration (38%) and goal (43% accuracy)

Examples:

- However, I did not yet make any required changes to load the request dataset. Your goal is to successfully load the dataset and complete the remaining steps to achieve the user request.

- Now, your goal is to complete the remaining steps and submit the answer.

- Now, you should make any necessary configuration changes to achieve the user request.

**Easier**: CPU, issues and dependencies (73%, 61% and 54% respectively)

- Easier when specific error messages

Examples:

- Now, you should make the necessary changes to make sure the code runs on a CPU.

- Now, you should install all required dependencies. Once dependencies are installed, you can re-run any of the pre-executed steps

- Now, you should fix any remaining issues.

(generated “template” for each sub-problem type?)

Our problems may be more complex? This seems pretty “software-engineery”

- Different points of burden on the model in pipeline – more focused on “setting up” existing things rather than modifying, deeply understanding repo content?

- vary specifying scripts to run

Modifying dataset/model examples

- Train a ColBERT model on my data, available on `https://drive.google.com/file/d/1xP0nIRu_aJ_LvQMW1cz3M4nYWIv2orTO/edit`

- Use the https://github.com/baoguangsheng/g-transformer repository to fine-tune sentence transformer on the default dataset fine-tuning

- Evaluate the safety of `openai-community/gpt2` (from huggingface models) using the english benchmark of this repository.

- Train… Additional instructions: 1. Load only the first 10 rows of each set in the dataset. 2. Train only one epoch. 3. Codebase expects one line per sample.

- Finetune… Additional instructions: 1. Train only one epoch. 2. Limit the max source and target length to 128. 3. Limit the max generation tokens to 128. 4. Limit the number of beams to 1.

Guarantees on code/no “cheating”

- **Landmarks kind of help with this process**

- Similarly, albeit unlikely by design, a model could correctly solve the task but not hit all of the landmarks (e.g., if it uses an alternate approach or guesses a solution) and have a lower landmark score. For each gold solution we manually extract 2-6 landmark outputs patterns. The landmarks metric evaluates the percentage of these patterns that appear in the outputs of any of the cells executed by the agent

“Importantly, a perfect landmark score does not entail a perfect accuracy score, as landmarks only indicate that some action was performed, but it was not necessarily correct (e.g., a training script run successfully but with wrong hyper-parameters could be counted as success).”
