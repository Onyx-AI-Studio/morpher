def ollama_generate(input: str, model="zephyr-beta"):
    """
    Function to generate text for offline large language models using ollama. Make sure to run Ollama locally for this to work.

    :param input: Input prompt
    :param model: Ollama model name
    :return: Generated output using the specified model
    """
    url = "http://localhost:11434/api/generate"

    payload = json.dumps({
        "model": model,
        "prompt": input,
        "stream": False
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return json.loads(response.text)['response'].strip()
