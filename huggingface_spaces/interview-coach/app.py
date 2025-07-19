import gradio as gr
from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
    AutoModelForCausalLM,
)
import torch

# ==============================
# 1. Free Models Registry
# ==============================
FREE_MODELS = {
    "Flan-T5 Large": {
        "id": "google/flan-t5-large",
        "type": "seq2seq",
        "prompt_style": "plain"
    },
    "Mistral-7B Instruct": {
        "id": "mistralai/Mistral-7B-Instruct-v0.2",
        "type": "causal",
        "prompt_style": "chatml"
    },
    "TinyLlama-1.1B Chat": {
        "id": "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        "type": "causal",
        "prompt_style": "tinymix"
    },
    "Phi-2": {
        "id": "microsoft/phi-2",
        "type": "causal",
        "prompt_style": "plain"
    },
    "Zephyr-7B Alpha": {
        "id": "HuggingFaceH4/zephyr-7b-alpha",
        "type": "causal",
        "prompt_style": "zephyr"
    }
}

model_cache = {}

# ==============================
# 2. Prompt Formatter
# ==============================
def format_prompt(style, job_role, question, model_name):
    if style == "chatml":
        return f"<|user|>\n[{job_role}] {question}\n<|assistant|>"
    elif style == "zephyr":
        return f"<|system|>You are a helpful assistant for {job_role} interviews.\n<|user|>{question}\n<|assistant|>"
    elif style == "gemma":
        return f"<start_of_turn>user\n[{job_role}] {question}<end_of_turn>\n<start_of_turn>model\n"
    elif style == "tinymix":
        return f"Interview Question for {job_role}:\n{question}\nAnswer:"
    else:  # plain
        if model_name == "Flan-T5 Large":
            return f"Answer the following {job_role} interview question:\n{question}"
        return f"[{job_role}] {question}"

# ==============================
# 3. Model Inference
# ==============================
def load_model(model_name):
    if model_name in model_cache:
        return model_cache[model_name]

    model_info = FREE_MODELS[model_name]
    model_id = model_info["id"]
    model_type = model_info["type"]

    tokenizer = AutoTokenizer.from_pretrained(model_id)
    if model_type == "seq2seq":
        model = AutoModelForSeq2SeqLM.from_pretrained(model_id)
    else:
        model = AutoModelForCausalLM.from_pretrained(model_id)

    model.eval()
    model_cache[model_name] = (tokenizer, model, model_type)
    return tokenizer, model, model_type


def run_model(model_name, prompt):
    try:
        tokenizer, model, model_type = load_model(model_name)

        inputs = tokenizer(prompt, return_tensors="pt")
        with torch.no_grad():
            if model_type == "seq2seq":
                outputs = model.generate(**inputs, max_new_tokens=256)
            else:
                outputs = model.generate(
                    **inputs,
                    max_new_tokens=256,
                    pad_token_id=tokenizer.eos_token_id
                )
        return tokenizer.decode(outputs[0], skip_special_tokens=True)
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# ==============================
# 4. Gradio App
# ==============================
def generate_response(job_role, model_choice, question):
    info = FREE_MODELS[model_choice]
    prompt = format_prompt(info["prompt_style"], job_role, question, model_choice)
    return run_model(model_choice, prompt)


job_roles = [
    "Data Science", "Machine Learning",
    "AI Engineering", "Software Engineering", "Testing"
]

demo = gr.Interface(
    fn=generate_response,
    inputs=[
        gr.Dropdown(choices=job_roles, label="Select Job Role", value="Data Science"),
        gr.Dropdown(choices=list(FREE_MODELS.keys()), label="Select Model", value="Flan-T5 Large"),
        gr.Textbox(label="Your Question")
    ],
    outputs=gr.Textbox(label="AI Coach Response"),
    title="🧠 AI Interview Coach",
    description="Built with BotCampus Agent SDK 🇦🇪 — Free LLM powered Interview Assistant",
)

# ==============================
# 5. Launch
# ==============================
if __name__ == "__main__":
    demo.launch()