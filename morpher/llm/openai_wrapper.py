from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

# Load OPENAI_API_KEY
load_dotenv()


class OpenAIWrapper(BaseModel):

    @staticmethod
    def generate(prompt: str,
                 system_message="You are an assistant who is always helpful, harmless and honest.",
                 model="gpt-3.5-turbo"):
        """
        Function to generate text using OpenAI models. Make sure to set OPENAI_API_KEY for this to work.

        :param prompt: Input prompt
        :param system_message: System message
        :param model: Model name according to the OpenAI documentation
        :return: Output from the model using the specified model
        """
        client = OpenAI()
        completion = client.chat.completions.create(
            model=model,
            temperature=0,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ]
        )

        return completion.choices[0].message.content
