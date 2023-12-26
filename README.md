# Morpher - Dynamic Replanner Agent

Dynamic agent which modifies the plan of execution on the fly. Inspired by BabyAGI and Plan-and-Execute agents.

## What is it?

Based on Plan-and-execute type agents, but capable of more complex tasks as it can think and update the plan based on new information after performing an action. It is built from scratch to have better control and expandability over the implementation.

The key added capability is iterative thinking and replanning after each action, facilitates longer execution sequences and potentially hierarchical tasks where sequential processing fails as the main task is split into multiple sub-tasks which should be processed before reaching the next step.

## Core Logic

1. Prepare a plan based on the task. 
2. Loop over the below step to iteratively,
    1. `Think`: Keeping the current step in mind, choose the right tool from the arsenal with the right input.
    2. `Act`: Execute the selected tool with the input from the previous step.
    3. `Observe`: Based on the output of the action step, extract relevant information and update the current plan.

## Examples

### Example 1 - Dynamic Planning

This simple example demonstrates the concept of dynamic planning.

```
Task: Calculate the double of the age of Tom Cruise.

Current Plan:
[
    Use web_search with "Tom Cruise age" to find the age of Tom Cruise,
    Use calculator with "age * 2" to calculate the double of the age,
]

##### Execution Started #####
Executing Step: Use web_search with "Tom Cruise age" to find the age of Tom Cruise

THINK: Keeping the current step in mind, choose the right tool from the list with the right input
Tool: web_search, Tool inputs: ['Tom Cruise age']

ACT: Execute the selected tool with the input from the previous step
Output of the current action: 61 years

OBSERVE: Based on the output of the action step, extract relevant information and refresh the current plan
Current Plan:
[
    Use calculator with "61 * 2" to calculate the double of the age,
]
##### Execution Done #####


##### Execution Started #####
Executing Step: Use calculator with "61 * 2" to calculate the double of the age

THINK: Keeping the current step in mind, choose the right tool from the list with the right input
Tool: calculator, Tool inputs: ['61 * 2']

ACT: Execute the selected tool with the input from the previous step
Output of the current action: 122

OBSERVE: Based on the output of the action step, extract relevant information and refresh the current plan
Current Plan:
[
    END_PLAN,
]
##### Execution Done #####


Analyzing memory to return the final result...
FINAL RESULT: 122
```

### Example 2 - Research

This example demonstrates the ability of the model to research on a particular topic. Omitting output for all the intermediate steps as it is too long.

```
Task: Calculate the double of the age of Tom Cruise.

Current Plan:
[
    Use web_search with "OpenAI current state" to gather information,
    Read multiple sources to get a comprehensive understanding of OpenAI,
    Take notes on key points and important details,
    Organize the information into an outline,
    Write an introduction for the essay,
    Write body paragraphs based on the outline, covering different aspects of OpenAI,
    Include information on recent developments, projects, and achievements,
    Include information on partnerships, collaborations, and funding,
    Include information on the impact of OpenAI in various fields,
    Write a conclusion summarizing the current state of OpenAI,
    Proofread and edit the essay for clarity and coherence,
]

--- Skipping Intermediate Steps ---

Analyzing memory to return the final result...
FINAL RESULT: OpenAI is an organization that has made significant advancements in the field of artificial
intelligence (AI). It has formed partnerships and collaborations with various organizations and researchers
to further its mission of developing and directing AI in ways that benefit humanity. One notable partnership
is with Microsoft, which invested $1 billion in OpenAI in 2019. This partnership aims to accelerate the development
of artificial general intelligence and make it more accessible to a wider range of users. OpenAI actively engages
with the broader AI community through conferences, workshops, and publications, promoting collaboration and
innovation in the field.

OpenAI's funding primarily comes from a combination of sources. In addition to the investment from Microsoft,
OpenAI generates revenue through its commercial activities, such as licensing its AI technologies and providing
AI services to businesses. This diversified funding approach allows OpenAI to maintain financial stability and
continue its research and development efforts in the field of AI.

OpenAI has made a significant impact in various fields through its research and development efforts. One of its
notable projects is GPT-3, a language model capable of generating human-like text. This technology has implications
for automated content generation in areas like journalism, marketing, and creative writing. It has the potential to
streamline content production processes and enable businesses to create personalized and engaging content at scale.

OpenAI's AI technologies also have the potential to revolutionize customer service. Chatbots powered by OpenAI's
language models can provide instant and accurate responses to customer queries, improving customer satisfaction
and reducing the workload on human customer service agents. This technology has the potential to enhance customer
experiences and optimize customer support operations.

Language translation is another field where OpenAI's impact can be seen. By leveraging its language models, OpenAI
has made advancements in machine translation, enabling more accurate and natural language translations across different
languages. This technology has the potential to break down language barriers and facilitate communication and
understanding between people from different linguistic backgrounds.

Overall, OpenAI's research and development efforts have had a transformative impact in fields like content creation,
customer service, and language translation. The organization's AI technologies have the potential to revolutionize
industries, improve efficiency, and enhance human experiences in various domains.
```

## Progress Tracker

- [x] Implement a POC with major steps like, Plan, Thought, Action and Observation.
- [x] Implement contextual memory to support the agent's reasoning.
- [x] Implement a default tool to improve fault tolerance.
- [x] Try out simple scenarios to demonstrate, (i) Dynamic planning, (ii) Research.
- [x] Implement memory management to improve cost efficiency.
- [x] Add Poetry for better dependency management and packaging support.
- [ ] Refactor and reorganize the code to package it into a easy-to-use library.
- [ ] Implement a tool for detailed searches, maybe use Browserless or something similar.
- [ ] Add support for creating agents with roles.
- [ ] Implement mechanism for inter-agent communication for more complex tasks.
- [ ] Implement advanced memory mechanisms for short-term and long-term memory.
- [ ] Publish it to PyPi.


## References

- [`yoheinakajima/babyagi`](https://github.com/yoheinakajima/babyagi) - BabyAGI is a pared-down version of the original Task-Driven Autonomous Agent (Mar 28, 2023) shared on Twitter.
