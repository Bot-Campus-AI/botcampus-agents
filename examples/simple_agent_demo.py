from botcampus.agent import BotCampusAgent

agent = BotCampusAgent(system_prompt="You are a helpful AI agent for general knowledge.")

question = "What's the capital of the UAE?"
response = agent.run(question)

print("🤖 Bot Response:", response)
