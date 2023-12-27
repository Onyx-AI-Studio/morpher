# # Re-planner Agent

# **Basic idea**: Based on Plan-and-execute type agents, but capable of more complex tasks as it is able to think and update the plan as and when needed. This helps it to tackle tasks with longer sequences.
#
# **Flow**: Prepare a plan based on the task. Loop over the below step to proceed,
# 1. `Think`: Keeping the current step in mind, choose the right tool from the arsenel with right input.
# 2. `Act`: Execute the selected tool with the input from the previous step.
# 3. `Observe`: Based on the output of the action step, extract relevant information and update the current plan.

# ## Steps

# ### Plan


def prepare_plan(objective: str):
    planner_template = Template("""Your task is to analyze complex tasks and break them down into smaller unit sub-tasks.

Instructions:
* Do not say your knowledge is out of date, just return the requested information.
* Do not say you are a AI language model.
* Do not perform the task just yet, analyze and break down the task and return the sub-tasks.
* If a tool is used, sub-task must say something like, 'Use tool_a with X to do Y'.
* Use only the tools mentioned below if and when needed.
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

Return the output in the specified format, do not deviate. Do not add any text before or after the output.
    """)

    prompt = planner_template.substitute(input=objective, tools=get_current_tools())
    # print(prompt)
    return openai_generate(prompt)


# ### Think


def think():
    thought_template = Template("""Your task is to extract the tool name and the input to the tool for the current step in the specified format.

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
""")

    prompt = thought_template.substitute(current_step=get_current_step(), tools=get_current_tools(),
                                         memory=get_memory())
    # print(prompt)
    action_inputs = openai_generate(prompt)
    action = ast.literal_eval(action_inputs)
    return action['tool_name'], action['tool_input']


# ### Act


def execute_action(tool_name: str, tool_input):
    return system_state['tools'][tool_name]['func'](tool_input)


# ### Observe and Re-plan


def refresh_plan(action_output: str):
    observation_template = Template("""Your task is to observe the `Action Output` for the `Current Step` and update the `Current Plan` modifying it as needed. Return the updated plan as output in the specified format.

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
""")

    prompt = observation_template.substitute(current_step=get_current_step(), action_output=action_output,
                                             current_plan=get_current_plan(), memory=get_memory())
    # print(prompt)
    refreshed_plan = openai_generate(prompt)
    return refreshed_plan


# ## Analyze data from memory and return the output


def analyze_memory():
    analyze_result_template = Template("""Based on each step executed and their result in the `Contextual Memory` and the `Task` at hand, analyze and return the answer.

Contextual Memory:
```
$memory
```

Task:
```
$task
```

Return only the output, do not add any text before or after the output.""")
    prompt = analyze_result_template.substitute(memory=get_memory(), task=get_objective())
    # print(prompt)
    result = openai_generate(prompt)
    return result


# ## Controller


objective = "Research about the current state of OpenAI. Get an outline, search for more information if needed and colate everything together into a coherent essay."
# objective = "Calculate the double of the age of Tom Cruise"

# Initialize system state
system_state['task'] = objective
system_state['short_term_memory'] = []
set_current_plan(prepare_plan(objective))

pretty_print_current_plan()

while "END_PLAN" not in str(system_state['current_plan'][0]):
    current_step = get_current_step()
    print(f"##### Execution Started #####")
    print(f"Executing Step: {get_current_step()}")

    # think
    print("\nTHINK: Keeping the current step in mind, choose the right tool from the list with the right input")
    tool_name, tool_input = think()
    print(f'Tool: {tool_name}, Tool inputs: {tool_input}')

    # act
    print("\nACT: Execute the selected tool with the input from the previous step")
    action_output = execute_action(tool_name, tool_input)
    print(f"Output of the current action: {action_output}")
    append_to_memory(current_step, action_output)

    # observe and refresh plan
    print(
        "\nOBSERVE: Based on the output of the action step, extract relevant information and refresh the current plan")
    refreshed_plan = refresh_plan(action_output)
    set_current_plan(refreshed_plan)
    pretty_print_current_plan()

    print(f"##### Execution Done #####\n\n")

print("Analyzing memory to return the final result...")
result = analyze_memory()
print(f"FINAL RESULT: {result}")
