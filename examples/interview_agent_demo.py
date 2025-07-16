from botcampus.agent import BotCampusAgent

system_prompt = """
You are an expert career coach helping users prepare for job interviews.
Give relevant questions, smart sample answers, and actionable suggestions.
Be conversational, friendly, and helpful.
"""

agent = BotCampusAgent(system_prompt=system_prompt)

user_input = "I have an interview for a data science role at a startup. Can you help?"

response = agent.run(user_input)
print(f"🤖 Bot Response:\n{response}")
