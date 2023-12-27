import ast
from typing import List, Optional, Any

from pydantic import BaseModel

from morpher.tools import Tool, MiscTools, WebSearch


class Memory(BaseModel):
    step: str
    output: str


class SystemState(BaseModel):
    task: str = ""
    current_plan: Optional[List[str]] = []
    short_term_memory: Optional[List[Memory]] = []
    tools: List[Tool] = []

    def __init__(self, task: str, **data: Any):
        super().__init__(**data)

        self.task = task

        webSearch = WebSearch()
        self.tools.extend(webSearch.tool_info)

        miscTools = MiscTools()
        self.tools.extend(miscTools.tool_info)

    def get_objective(self):
        return self.task

    def get_current_tools(self):
        tool_str = ""
        for tool in self.tools:
            # print(idx, tool['description'])
            tool_str += f"Name: {tool.name}\nDescription: {tool.description}\n\n"
        return tool_str.strip()

    def get_current_step(self):
        if len(self.current_plan) == 0:
            return []
        return self.current_plan[0]

    def get_current_plan(self):
        plan = "[\n"
        for s in self.current_plan:
            plan += "    " + s + ",\n"
        plan += "]"
        return plan

    def set_current_plan(self, plan: str):
        self.current_plan = ast.literal_eval(plan)

    def pretty_print_current_plan(self):
        print("Current Plan:")
        print(f"```\n{self.get_current_plan()}\n```")

    def append_to_memory(self, current_step: str, action_output: str):
        # self.short_term_memory.append({'step': current_step, 'output': action_output})
        self.short_term_memory.append(Memory(**{'step': current_step, 'output': action_output}))

    def get_memory(self, limit: int = 3):
        memory = ""
        size = len(self.short_term_memory)
        if size < limit:
            limit = size

        for s in self.short_term_memory[size - limit:]:
            memory += "Step: " + s.step + "\n" + "Result: " + s.output + "\n\n"
        return memory.strip()
