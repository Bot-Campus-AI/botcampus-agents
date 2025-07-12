
# 🧠 botcampus-agents

**BotCampus Agents** is a lightweight Python SDK to help learners and developers build simple AI agents using OpenAI and automation workflows.  
Built by [BotCampus AI](https://www.botcampus.ai) — designed for education, prototyping, and agent-driven learning.

---

##  Features

- ✅ Create OpenAI-powered AI agents with a few lines of code
- 🧩 Customize system prompts and models (GPT-4, GPT-3.5)
- 💡 Simple API for running conversational agents
- 🔒 Supports `.env`-based key management
- 🧪 Built for hands-on projects and educational workshops

---

## 📦 Installation

Clone the repo and install in editable mode:

```bash
git clone https://github.com/Bot-Campus-AI/botcampus-agents.git
cd botcampus-agents
pip install -e .
````

---

## 🔐 Setup

Create a `.env` file in the root:

```env
OPENAI_API_KEY=your_openai_key_here
```

---

## 🧪 Example

```python
from botcampus.agent import BotCampusAgent

agent = BotCampusAgent(system_prompt="You are a helpful assistant.")
response = agent.run("What's the capital of the UAE?")
print(response)
```

▶️ Run it:

```bash
python examples/simple_agent_demo.py
```

---

## 🧰 File Structure

```
botcampus/
│
├── agent.py            # Core BotCampusAgent class
├── memory.py           # (Coming soon) Memory manager
├── prompt_chain.py     # (Coming soon) Chaining prompts
├── utils.py            # Utilities
│
examples/
└── simple_agent_demo.py

tests/
└── test_agent.py
```

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 🙌 Credits

Created by the team at [BotCampus AI](https://www.botcampus.ai)
Empowering 1 million learners in AI by 2027 from Dubai.