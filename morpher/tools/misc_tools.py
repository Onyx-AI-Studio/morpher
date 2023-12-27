from string import Template

from pydantic import BaseModel

from morpher.llm import OpenAIWrapper
from morpher.prompts import CALCULATOR_TEMPLATE, DEFAULT_TEMPLATE


class MiscTools(BaseModel):

    @staticmethod
    def meaning_of_life():
        """
        Mock tool to return a static response.

        :return: Static string.
        """
        return "42 is the answer to life, the universe, and everything."

    @staticmethod
    def calculator(input: str):
        """
        Calculates simple arithmetic operations using an LLM.

        :param input: Query to calculate.
        :return: Answer of the query as a string.
        """
        prompt_template = Template(CALCULATOR_TEMPLATE)
        prompt = prompt_template.substitute(task=input)
        result = OpenAIWrapper.generate(prompt)
        return result

    @staticmethod
    def default_tool(input: str):
        """
        Default tool to improve fault tolerance.

        :param input: Query as a string.
        :return: Answer to the query.
        """
        prompt_template = Template(DEFAULT_TEMPLATE)
        prompt = prompt_template.substitute(task=input, memory=get_memory())
        result = OpenAIWrapper.generate(prompt)
        return result
