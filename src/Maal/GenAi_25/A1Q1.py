from transformers import pipeline
model = pipeline("text-generation")
output = model("I want to learn LLM ", max_length=30)
print(output[0]["generated_text"])