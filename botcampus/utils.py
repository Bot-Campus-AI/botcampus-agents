from transformers import pipeline

# Replace this with real model calls via API or local inference
def call_model(prompt, model="gpt2", temperature=0.7):
    try:
        pipe = pipeline("text-generation", model=model)
        output = pipe(prompt, max_length=150, do_sample=True, temperature=temperature)
        return output[0]["generated_text"]
    except Exception as e:
        return f"Error calling model {model}: {str(e)}"
