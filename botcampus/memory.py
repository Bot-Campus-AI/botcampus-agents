class ChatMemory:
    def __init__(self):
        self.history = []

    def update_memory(self, question, answer):
        self.history.append((question, answer))
        if len(self.history) > 10:
            self.history.pop(0)

    def get_context(self):
        return "\n".join([f"Q: {q}\nA: {a}" for q, a in self.history])
