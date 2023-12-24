# Dynamic Replanner Agent

Dynamic agent which modifies the plan of execution at each step as needed. Inspired by BabyAGI and Plan-and-Execute agents.

## Example 1

Simple example to demonstrate the concept.

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
Output of the current action: Age of Tom Cruise is 42

OBSERVE: Based on the output of the action step, extract relevant information and refresh the current plan
Current Plan:
[
    Use calculator with "42 * 2" to calculate the double of the age,
]
##### Execution Done #####


##### Execution Started #####
Executing Step: Use calculator with "42 * 2" to calculate the double of the age

THINK: Keeping the current step in mind, choose the right tool from the list with the right input
Tool: calculator, Tool inputs: ['42 * 2']

ACT: Execute the selected tool with the input from the previous step
Output of the current action: 84

OBSERVE: Based on the output of the action step, extract relevant information and refresh the current plan
Current Plan:
[
    END_PLAN,
]
##### Execution Done #####


Analyzing memory to return the final result...
FINAL RESULT: 84
```
