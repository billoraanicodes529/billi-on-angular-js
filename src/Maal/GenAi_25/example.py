from transformers import pipeline
model = pipeline("text-generation")
prompt = input("Enter prompt")
output = model(prompt , max_length=30)
print(output[0]["generated_text"])