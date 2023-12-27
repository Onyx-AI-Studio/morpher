from morpher.agent import SystemState

# state = SystemState()
state = SystemState("Research about OpenAI")

# Test out the web_search tool
print(state.tools[0].func("Who is John Wick?"))
