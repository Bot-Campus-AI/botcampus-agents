import openai
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

class BotCampusAgent:
    def __init__(self, system_prompt: str, model="gpt-3.5-turbo"):
        self.system_prompt = system_prompt
        self.model = model

    def run(self, user_input: str) -> str:
        try:
            response = client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": str(self.system_prompt)},
                    {"role": "user", "content": str(user_input)}
                ]
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"❌ Agent Error: {e}"
