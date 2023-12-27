import json
from string import Template

import requests
from pydantic import BaseModel

from morpher.prompts import ZEPHYR_STANDARD_TEMPLATE


class OllamaWrapper(BaseModel):

    @staticmethod
    def generate(prompt: str, model="zephyr-beta"):
        """
        Function to generate text for offline large language models using ollama. Make sure to run Ollama locally for this to work.

        :param prompt: Input prompt
        :param model: Ollama model name
        :return: Generated output using the specified model
        """
        url = "http://localhost:11434/api/generate"

        payload = json.dumps({
            "model": model,
            "prompt": Template(ZEPHYR_STANDARD_TEMPLATE).substitute(prompt=prompt),
            "stream": False
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        return json.loads(response.text)['response'].strip()
