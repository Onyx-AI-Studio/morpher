CALCULATOR_TEMPLATE = """You are a calculator, perform the below Task,

Task: ```$task```

Return only the output. Do not add any text before or after the output."""

DEFAULT_TEMPLATE = """You are a helpful, harmless and honest assistant. Perform the below Task, use the information in `Memory` for reference.

Memory:
```
$memory
```

Task: ```$task```

Return only the output. Do not add any text before or after the output."""

ZEPHYR_STANDARD_TEMPLATE = """<|system|>
You are an assistant who is always helpful, harmless and honest.</s>
<|user|>
$prompt</s>
<|assistant|>"""

ZEPHYR_PLANNER_TEMPLATE = """<|system|>
You are an assistant who is always helpful, harmless and honest.</s>
<|user|>
Your task is to analyze complex tasks and break them down into smaller sub-tasks.

Instructions:
* Do not say your knowledge is out of date, just return the requested information.
* Do not say you are a AI language model.
* Do not perform the task just yet, analyze and break down the task and return the sub-tasks.
* If a tool is used, sub-task must say something like, 'Use tool_a with X to do Y'.
* Use only the tools mentioned below if and when needed.
* The sub-tasks must not say 'store the data'. All the data is by default stored in memory.
* Return the output in the form of an array, follow the below output format strictly.

Tools:
```
$tools
```

Output format:
```
[
    'sub-task 1',
    'sub-task 2',
    ...
]
```

Task: $input

Return the output in the specified format, do not deviate. Do not add any text before or after the output.</s>
<|assistant|>"""

ZEPHYR_THOUGHT_TEMPLATE = """<|system|>
You are an assistant who is always helpful, harmless and honest.</s>
<|user|>
Your task is to extract the tool name and the input to the tool for the current step in the specified format.

Instructions:
* Do not say your knowledge is out of date, just return the requested information.
* Do not say you are a AI language model.
* Understand the `Current step` and extract the tool name and the complete input to the tool.
* Refer to the list of tools available to get the right tool name.
* Follow the below output format strictly.

Current step: `$current_step`

Tools:
```
$tools
```

Output format:
```
{
    'current_step': "current step that is being analyzed",
    'tool_name': "name of the tool",
    'tool_input': ["input 1", "input 2", ...]
}
```

Return the output in the specified format, do not deviate. Do not add any text before or after the output.</s>
<|assistant|>"""

OPENAI_PLANNER_TEMPLATE = """Your task is to analyze complex tasks and break them down into smaller unit sub-tasks.

Instructions:
* Do not say your knowledge is out of date, just return the requested information.
* Do not say you are a AI language model.
* Do not perform the task just yet, analyze and break down the task and return the sub-tasks.
* If a tool is used, sub-task must say something like, 'Use tool_a with X to do Y'.
* Use only the tools mentioned below if and when needed.
* Return the output in the form of an array, follow the below output format strictly.

Task: $input

Tools:
```
$tools
```

Output format:
```
[
    'sub-task 1', 
    'sub-task 2', 
    ...
]
```

Return the output in the specified format, do not deviate. Do not add any text before or after the output.
"""

OPENAI_THOUGHT_TEMPLATE = """Your task is to extract the tool name and the input to the tool for the current step in the specified format.

Instructions:
* Do not say your knowledge is out of date, just return the requested information.
* Do not say you are a AI language model.
* Understand the `Current step` and extract the tool name and the complete input to the tool.
* Use the information from `Memory` if needed.
* Refer to the list of tools available to get the right tool name.
* Follow the below output format strictly.

Current step: `$current_step`

Tools:
```
$tools
```

Memory:
```
$memory
```

Output format:
```
{
    'current_step': "current step that is being analyzed",
    'tool_name': "name of the tool",
    'tool_input': "input to the tool with all the relevant information extracted",
}
```

Return the output in the specified format, do not deviate. Do not add any text before or after the output.
"""

OPENAI_OBSERVATION_TEMPLATE = """Your task is to observe the `Action Output` for the `Current Step` and update the `Current Plan` modifying it as needed. Return the updated plan as output in the specified format.

Instructions:
* Do not say your knowledge is out of date, just return the requested information.
* Do not say you are a AI language model.
* Update the plan by removing already executed steps or steps which are not necessary now.
* Less number of steps are preferred.
* Update any values in the next sub-tasks if they are available.
* Return `END_PLAN` as the only sub-task if all the steps are executed.
* You cannot have steps like, `note down x` or `write down y` or `save data to a variable`. All the data is already being saved to `Memory`.
* Follow the below output format strictly.

Current Step: `$current_step`

Action Output:
```
$action_output
```

Current Plan:
```
$current_plan
```

Memory:
```
$memory
```

Output format:
```
[
    'sub-task 1', 
    'sub-task 2', 
    ...
]
```

The output must be an array and every element must be in single quotes with a comma at the end, do not deviate. Do not add any text before or after the output.
"""

OPENAI_ANALYZE_MEMORY_TEMPLATE = """Based on each step executed and their result in the `Contextual Memory` and the `Task` at hand, analyze and return the answer.

Contextual Memory:
```
$memory
```

Task:
```
$task
```

Return only the output, do not add any text before or after the output."""
