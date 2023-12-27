from openai import OpenAI

client = OpenAI()


def openai_generate(input: str, system_message="You are an assistant who is always helpful, harmless and honest.",
                    model="gpt-3.5-turbo"):
    """
    Function to generate text using OpenAI models. Make sure to set OPENAI_API_KEY for this to work.

    :param input: Input prompt
    :param system_message: System message
    :param model: Model name according to the OpenAI documentation
    :return: Generated model using the specified model
    """
    completion = client.chat.completions.create(
        model=model,
        temperature=0,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": input}
        ]
    )

    return completion.choices[0].message.content
