import ast
import json
from string import Template

import requests




# # Archive

# ## Zephyr templates


planner_template = Template("""<|system|>
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
<|assistant|>""")

prompt = planner_template.substitute(input="Calculate the double of the age of Tom Cruise", tools=get_current_tools())
# print(prompt)
set_current_plan(ollama_generate(prompt))

thought_template = Template("""<|system|>
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
<|assistant|>""")

prompt = thought_template.substitute(current_step=get_current_step(), tools=get_current_tools())
# print(prompt)
print(ollama_generate(prompt))

# ## Manual Serper API Call


url = "https://google.serper.dev/search"

payload = json.dumps({
    "q": "apple inc"
})
headers = {
    'X-API-KEY': '',
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

raw_snippets = json.loads(response.text)['organic']
for s in raw_snippets:
    print(s['snippet'])
