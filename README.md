
# 🤖 botcampus-agents

**BotCampus Agents** is a lightweight Python SDK that helps learners, developers, and automation enthusiasts build **simple AI agents** using OpenAI and workflow orchestration tools like `n8n` or `Make`.

Built by [**BotCampus AI**](https://www.botcampus.ai) — designed for **education**, **agent prototyping**, and **agent-driven learning**.

---

## 🌍 Built in Dubai 🇦🇪

This project is proudly built and maintained in **Dubai** as part of the regional push to democratize AI access and foster innovation across MENA.

---

##  Features

- ✅ Modular Agent class structure
- 🔁 Works with OpenAI's GPT models
- 🔒 .env-based key management
- 📦 Simple to extend and integrate into automation workflows (e.g., n8n)
- 🧠 Ideal for education, experimentation, and rapid prototyping

---

## 🛠️ Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/Bot-Campus-AI/botcampus-agents.git
cd botcampus-agents
````

### 2. Set up the environment

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Add your `.env` file

Create a `.env` file in the root directory and include your OpenAI key:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxx
```

### 4. Run a demo

```bash
python -m examples.simple_agent_demo
```

---

## 📁 Project Structure

```
botcampus-agents/
│
├── botcampus/              # Core SDK logic (agent classes, handlers)
├── examples/               # Sample use cases and agent demos
├── tests/                  # Unit tests (coming soon)
├── .env                    # Environment variables (not checked in)
├── requirements.txt        # Python dependencies
├── setup.py                # Package setup
└── README.md
```

---

## 🧪 Sample Usage

```python
from botcampus.agent import BotCampusAgent

agent = BotCampusAgent(model="gpt-3.5-turbo")
response = agent.ask("What's the capital of UAE?")
print("🤖", response)
```

Expected Output:

```bash
🤖 The capital of the United Arab Emirates (UAE) is Abu Dhabi.
```

---

## 📦 Install as a package (optional)

Coming soon via PyPI...

---

## 🔖 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---

## 💼 Use Cases

* AI workshops and bootcamps
* Students learning prompt-driven development
* Educators building agent-based curricula
* Integrators using AI in automation workflows

---

## 📢 About BotCampus AI

**BotCampus AI** empowers learners with interactive and hands-on AI projects.
This project illustrates the capability to build fast, functional AI agents for real-world use cases.

**Contact Us:**

* 🌐 [www.botcampus.ai](https://www.botcampus.ai)
* 📧 [support@botcampus.ai](mailto:support@botcampus.ai)
* 🔗 [LinkedIn](https://www.linkedin.com/company/botcampusai)

---

🟦 **Built in Dubai • For the World**
