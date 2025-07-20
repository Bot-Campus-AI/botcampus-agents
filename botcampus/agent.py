import time
from .utils import call_model
from .memory import ChatMemory

class InterviewAgent:
    def __init__(self, model_name, role="General", temperature=0.7):
        self.model_name = model_name
        self.role = role
        self.temperature = temperature
        self.memory = ChatMemory()

    def ask(self, question):
        context = self.memory.get_context()
        prompt = f"Role: {self.role}\nContext: {context}\nQuestion: {question}"
        response = call_model(prompt, model=self.model_name, temperature=self.temperature)
        self.memory.update_memory(question, response)
        return response
