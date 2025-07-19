import gradio as gr
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

FREE_MODELS = {
    "Flan-T5 Large": "google/flan-t5-large"
}

def run_free_model(model_choice, context_prompt):
    try:
        model_id = FREE_MODELS.get(model_choice)
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

        inputs = tokenizer(context_prompt, return_tensors="pt")
        with torch.no_grad():
            outputs = model.generate(**inputs, max_new_tokens=256)
        decoded_output = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return decoded_output
    except Exception as e:
        return f"⚠️ Model Error: {str(e)}"

def generate_response(job_role, model_choice, question):
    prompt = f"[{job_role}] {question}"
    return run_free_model(model_choice, prompt)

job_roles = ["Data Science", "Machine Learning", "AI Engineering", "Software Engineering", "Testing"]
model_options = list(FREE_MODELS.keys())

demo = gr.Interface(
    fn=generate_response,
    inputs=[
        gr.Dropdown(choices=job_roles, label="Select Job Role", value="Data Science"),
        gr.Dropdown(choices=model_options, label="Select Model", value="Flan-T5 Large"),
        gr.Textbox(label="Your Question")
    ],
    outputs=gr.Textbox(label="AI Coach Response"),
    title="🧠 AI Interview Coach",
    description="Built with BotCampus Agent SDK 🇦🇪 — Free LLM powered Interview Assistant"
)

if __name__ == "__main__":
    demo.launch()
