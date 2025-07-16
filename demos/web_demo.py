import os
import gradio as gr
from dotenv import load_dotenv
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from botcampus.agent import BotCampusAgent

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

# Load agent only if OpenAI key is present
agent = BotCampusAgent(system_prompt="""
You are an expert career coach helping users prepare for interviews.
Give relevant questions, sample answers, and actionable suggestions in a friendly, confident tone.
""") if openai_key else None

# Free model handler
FREE_MODELS = {
    "Flan-T5 Large": "google/flan-t5-large"
}

def run_free_model(model_choice, context_prompt):
    try:
        model_id = FREE_MODELS.get(model_choice)
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

        # Prompt tuning
        prompt = f"Answer this interview question for a {model_choice} role: {context_prompt}"

        inputs = tokenizer(prompt, return_tensors="pt")
        with torch.no_grad():
            outputs = model.generate(**inputs, max_new_tokens=256)
        decoded_output = tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Optional formatting
        formatted_output = (
            f"<div style='font-size:16px; color:#FFF;'>🧠 <strong>Answer:</strong><br>{decoded_output}</div>"
        )

        return formatted_output

    except Exception as e:
        return f"⚠️ Model Error: {str(e)}"


def respond(role, model_choice, question):
    context_prompt = f"Answer this interview question for a {role} role: {question}"
    print(f"[LOG] Respond triggered with role: {role}, model: {model_choice}, question: {question}")

    if model_choice == "OpenAI GPT-4":
        if not openai_key or agent is None:
            warning_msg = """
            ⚠️ **OpenAI Key Not Found**  
            This demo is protected to avoid misuse of paid API usage.

            #### 👉 To use the AI Interview Coach:
            - Download the [GitHub Codebase](https://github.com/Bot-Campus-AI/botcampus-agents)
            - Add your own OpenAI API key in a `.env` file
            - Run it locally or on your own Hugging Face Space

            ---
            🔐 This demo is secure by design. No API key = no cost exposure.
            """
            print(f"[LOG] {warning_msg}")
            return warning_msg
        raw_response = agent.run(context_prompt)
    else:
        raw_response = run_free_model(model_choice, context_prompt)

    formatted = (
        raw_response
        .replace("**Question:", "<hr style='border:0;border-top:1px solid #444;margin:1.5em 0;'>"
                 "<div style='font-size:17px; font-weight:bold; color:#FFF;'>🧠 Question:")
        .replace("Sample Answer:", "<div style='margin-top:6px;'><span style='font-weight:bold; color:#FFF;'>📌 Sample Answer:</span>")
        .replace("Actionable Tip:", "</div><div style='margin-top:4px;'><span style='font-weight:bold; color:#00FFAA;'>✅ Actionable Tip:</span>")
        + "</div>"
    )
    print("[LOG] Response formatted and returned")
    return formatted.strip()

# CSS Fixes
custom_css = """
#logo-image button, #logo-image .download, #logo-image .fullscreen {
    display: none !important;
}
.gr-dropdown .gr-box:hover,
.gr-dropdown .gr-box:focus {
    cursor: pointer !important;
}
#header-block {
    margin-bottom: 10px;
}
"""

with gr.Blocks(css=custom_css, theme=gr.themes.Soft()) as demo:
    with gr.Row(elem_id="header-block"):
        with gr.Column(scale=1, min_width=60):
            gr.HTML(
                '<img src="https://www.botcampus.ai/wp-content/uploads/2024/02/botcampus-R.webp" '
                'alt="BotCampus Logo" style="height:48px; pointer-events:none;" />',
                elem_id="logo-image"
            )
        with gr.Column(scale=9):
            gr.Markdown(
                "### 💬 AI Interview Coach  \n<span style='font-size:15px; color:#ccc;'>Built using the <strong>BotCampus Agent SDK</strong> 🇦🇪 <em>Made in Dubai</em></span>",
                elem_id="header-markdown"
            )

    with gr.Row():
        with gr.Column(scale=1):
            job_dropdown = gr.Dropdown(
                choices=["Data Science", "Software Testing", "DevOps", "Machine Learning", "Frontend", "Backend"],
                label="Select Job Role",
                value="Data Science"
            )
            model_dropdown = gr.Dropdown(
                choices=["OpenAI GPT-4"] + list(FREE_MODELS.keys()),
                label="Select Model",
                value="Flan-T5 Large"
            )
            question_input = gr.Textbox(
                lines=4,
                placeholder="Ask a question like: 'How to explain overfitting in interviews?'",
                label="Your Question"
            )
            clear_btn = gr.Button("Clear")
            submit_btn = gr.Button("Submit", variant="primary")

        with gr.Column(scale=1):
            output = gr.Markdown(label="Interview Coach Response")

    submit_btn.click(fn=respond, inputs=[job_dropdown, model_dropdown, question_input], outputs=output)
    clear_btn.click(lambda: "", None, [question_input])

if __name__ == "__main__":
    print("[LOG] Launching Gradio app")
    demo.launch()
