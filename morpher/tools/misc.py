def meaning_of_life():
    return "42 is the answer to life, the universe, and everything."


# TODO: Use dedent for all the prompts.py
def calculator(input: str):
    prompt_template = Template("""You are a calculator, perform the below Task,

Task: ```$task```

Return only the output. Do not add any text before or after the output.""")
    prompt = prompt_template.substitute(task=input)
    result = openai_generate(prompt)
    return result


def default_tool(input: str):
    prompt_template = Template("""You are a helpful, harmless and honest assistant. Perform the below Task, use the information in `Memory` for reference.

Memory:
```
$memory
```

Task: ```$task```

Return only the output. Do not add any text before or after the output.""")
    prompt = prompt_template.substitute(task=input, memory=get_memory())
    result = openai_generate(prompt)
    return result
