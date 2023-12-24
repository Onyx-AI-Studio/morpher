# Dynamic Replanner Agent

Dynamic agent which modifies the plan of execution as needed on the fly. Inspired by BabyAGI and Plan-and-Execute agents.

## What is it?

Based on Plan-and-execute type agents, but capable of more complex tasks as it can think and update the plan based on new information after performing an action. 

This helps it to tackle tasks with longer sequences and potentially hierarchical tasks where sequential processing fails as the main task is split into multiple sub-tasks which should be processed before reaching the next step.

## Core Logic

1. Prepare a plan based on the task. 
2. Loop over the below step to iteratively,
    1. `Think`: Keeping the current step in mind, choose the right tool from the arsenal with the right input.
    2. `Act`: Execute the selected tool with the input from the previous step.
    3. `Observe`: Based on the output of the action step, extract relevant information and update the current plan.

## Example 1

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
