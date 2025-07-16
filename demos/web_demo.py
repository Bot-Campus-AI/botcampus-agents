import os
import gradio as gr
from dotenv import load_dotenv

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")

agent = None
if openai_key:
    from botcampus.agent import BotCampusAgent
    agent = BotCampusAgent(system_prompt="""
    You are an expert career coach helping users prepare for interviews.
    Give relevant questions, sample answers, and actionable suggestions in a friendly, confident tone.
    """)

def respond(role, question):
    if not openai_key or agent is None:
        return """
        ⚠️ **OpenAI Key Not Found**  
        This demo is protected to avoid misuse of paid API usage.

        #### 👉 To use the AI Interview Coach:
        - Download the [GitHub Codebase](https://github.com/Bot-Campus-AI/botcampus-agents)
        - Add your own OpenAI API key in a `.env` file
        - Run it locally or on your own Hugging Face Space

        ---
        🔐 This demo is secure by design. No API key = no cost exposure.
        """

    context_prompt = f"[{role}] {question}"
    raw_response = agent.run(context_prompt)

    formatted = (
        raw_response
        .replace("**Question:", "<hr style='border:0;border-top:1px solid #444;margin:1.5em 0;'>"
                 "<div style='font-size:17px; font-weight:bold; color:#FFF;'>🧠 Question:")
        .replace("Sample Answer:", "<div style='margin-top:6px;'><span style='font-weight:bold; color:#FFF;'>📌 Sample Answer:</span>")
        .replace("Actionable Tip:", "</div><div style='margin-top:4px;'><span style='font-weight:bold; color:#00FFAA;'>✅ Actionable Tip:</span>")
        + "</div>"
    )
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
            question_input = gr.Textbox(
                lines=4,
                placeholder="Ask a question like: 'How to explain overfitting in interviews?'",
                label="Your Question"
            )
            clear_btn = gr.Button("Clear")
            submit_btn = gr.Button("Submit", variant="primary")

        with gr.Column(scale=1):
            output = gr.Markdown(label="Interview Coach Response")

    submit_btn.click(respond, inputs=[job_dropdown, question_input], outputs=output)
    clear_btn.click(lambda: "", None, [question_input])

if __name__ == "__main__":
    demo.launch()
