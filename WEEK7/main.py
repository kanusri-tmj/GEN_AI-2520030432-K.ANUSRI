import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "distilgpt2"

print("Loading model...")

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

prompt = "The sun rises in the"

inputs = tokenizer(prompt, return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs)

logits = outputs.logits[:, -1, :]

probabilities = torch.softmax(logits, dim=-1)

top_k = 5

top_probs, top_indices = torch.topk(probabilities, top_k)

print("\nPrompt:", prompt)
print("\nTop 5 next-token candidates:")
print("-" * 40)

for i in range(top_k):
    token_id = top_indices[0][i].item()
    token = tokenizer.decode([token_id])
    probability = top_probs[0][i].item()

    print(f"{i + 1}. Token: {token!r} | Probability: {probability:.4f}")

print("\nExperiment completed successfully!")