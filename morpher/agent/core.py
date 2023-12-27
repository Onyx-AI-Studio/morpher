import ast
from string import Template
from typing import Any

from pydantic import BaseModel

from morpher.agent import SystemState
from morpher.llm import OpenAIWrapper
from morpher.prompts import OPENAI_PLANNER_TEMPLATE, OPENAI_THOUGHT_TEMPLATE, OPENAI_OBSERVATION_TEMPLATE, \
    OPENAI_ANALYZE_MEMORY_TEMPLATE


# **Basic idea**: Based on Plan-and-execute type agents, but capable of more complex tasks as it is able to think and
# update the plan as and when needed. This helps it to tackle tasks with longer sequences.
#
# **Flow**: Prepare a plan based on the task. Loop over the below step to proceed,
# 1. `Think`: Keeping the current step in mind, choose the right tool from the arsenel with right input.
# 2. `Act`: Execute the selected tool with the input from the previous step.
# 3. `Observe`: Based on the output of the action step, extract relevant information and update the current plan.

class Core(BaseModel):
    systemState: SystemState = SystemState("")

    def __init__(self, task: str, **data: Any):
        super().__init__(**data)
        self.systemState.task = task

    def prepare_plan(self, objective: str):
        planner_template = Template(OPENAI_PLANNER_TEMPLATE)
        prompt = planner_template.substitute(input=objective, tools=self.systemState.get_current_tools())
        print(prompt)
        return OpenAIWrapper.generate(prompt)

    def think(self):
        thought_template = Template(OPENAI_THOUGHT_TEMPLATE)
        prompt = thought_template.substitute(current_step=self.systemState.get_current_step(),
                                             tools=self.systemState.get_current_tools(),
                                             memory=self.systemState.get_memory())
        action_inputs = OpenAIWrapper.generate(prompt)
        action = ast.literal_eval(action_inputs)
        return action['tool_name'], action['tool_input']

    def execute_action(self, tool_name: str, tool_input: str):
        tool = [t for t in self.systemState.tools if t.name == tool_name][0]
        return tool.func(tool_input)

    def refresh_plan(self, action_output: str):
        observation_template = Template(OPENAI_OBSERVATION_TEMPLATE)
        prompt = observation_template.substitute(current_step=self.systemState.get_current_step(),
                                                 action_output=action_output,
                                                 current_plan=self.systemState.get_current_plan(),
                                                 memory=self.systemState.get_memory())
        refreshed_plan = OpenAIWrapper.generate(prompt)
        return refreshed_plan

    def analyze_memory(self):
        analyze_result_template = Template(OPENAI_ANALYZE_MEMORY_TEMPLATE)
        prompt = analyze_result_template.substitute(memory=self.systemState.get_memory(),
                                                    task=self.systemState.get_objective())
        result = OpenAIWrapper.generate(prompt)
        return result

    def run_agent(self):
        # objective = "Research about the current state of OpenAI. Get an outline, search for more information if needed and colate everything together into a coherent essay."
        # objective = "Calculate the double of the age of Tom Cruise"

        # Initialize system state
        self.systemState.short_term_memory = []
        self.systemState.set_current_plan(self.prepare_plan(self.systemState.task))

        print(f"Objective: {self.systemState.task}\n")

        self.systemState.pretty_print_current_plan()

        while "END_PLAN" not in str(self.systemState.current_plan[0]):
            current_step = self.systemState.get_current_step()
            print(f"##### Execution Started #####")
            print(f"Executing Step: {self.systemState.get_current_step()}")

            # think
            print("\nTHINK: Keeping the current step in mind, choose the right tool from the list with the right input")
            tool_name, tool_input = self.think()
            print(f'Tool: {tool_name}, Tool inputs: {tool_input}')

            # act
            print("\nACT: Execute the selected tool with the input from the previous step")
            action_output = self.execute_action(tool_name, tool_input)
            print(f"Output of the current action: {action_output}")
            self.systemState.append_to_memory(current_step, action_output)

            # observe and refresh plan
            print(
                "\nOBSERVE: Based on the output of the action step, extract relevant information and refresh the current plan")
            refreshed_plan = self.refresh_plan(action_output)
            self.systemState.set_current_plan(refreshed_plan)
            self.systemState.pretty_print_current_plan()

            print(f"##### Execution Done #####\n\n")

        print("Analyzing memory to return the final result...")
        result = self.analyze_memory()
        print(f"FINAL RESULT: {result}")
