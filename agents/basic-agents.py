from praisonaiagents import Agent

agent = Agent(
    instructions="You are a helpful assistant",
    llm="deepseek-r1"
)

agent.start("Why sky is Blue?")