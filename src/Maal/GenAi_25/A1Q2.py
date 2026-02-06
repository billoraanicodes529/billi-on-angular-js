from transformers import pipeline 
generator=pipeline("text-generation",model="gpt2")
prompt="Machine Learning is"
result=generator(prompt,max_length=40,num_return_sequences=1)
print("Generated Output: ")
print(result[0]["generated_text"])