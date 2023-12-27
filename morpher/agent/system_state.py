system_state = {
    "task": "",
    "tools": {
        "web_search": {
            "func": web_search,
            "description": "Useful to get information on an unknown topic by searching it online. Input must be a string.",
            # "return_direct": True
        },
        "meaning_of_life": {
            "func": meaning_of_life,
            "description": "Useful to get the meaning of life. No inputs needed for this tool.",
        },
        "calculator": {
            "func": calculator,
            "description": "Useful to perform basic arithmetic operations. Input must be a string.",
        },
        "default": {
            "func": default_tool,
            "description": "This is a general purpose tool, which is good at most tasks. Input must be a string, it must contain the task to perform.",
        },
    },
    "current_plan": [],
    "short_term_memory": [],
}


def get_objective():
    return system_state['task']


def get_current_tools():
    tool_str = ""
    for idx, tool in system_state['tools'].items():
        # print(idx, tool['description'])
        tool_str += f"Name: {idx}\nDescription: {tool['description']}\n\n"
    return tool_str.strip()


def get_current_step():
    if len(system_state['current_plan']) == 0:
        return []
    return system_state['current_plan'][0]


def get_current_plan():
    plan = "[\n"
    for s in system_state['current_plan']:
        plan += "    " + s + ",\n"
    plan += "]"
    return plan


def set_current_plan(plan: str):
    system_state['current_plan'] = ast.literal_eval(plan)


def pretty_print_current_plan():
    print(f"""Current Plan:
```
{get_current_plan()}
```""")


def append_to_memory(current_step: str, action_output: str):
    system_state['short_term_memory'].append({'step': current_step, 'output': action_output})


def get_memory(limit: int = 3):
    memory = ""
    size = len(system_state['short_term_memory'])
    if size < limit:
        limit = size

    for s in system_state['short_term_memory'][size - limit:]:
        memory += "Step: " + s['step'] + "\n" + "Result: " + s['output'] + "\n\n"
    return memory.strip()
