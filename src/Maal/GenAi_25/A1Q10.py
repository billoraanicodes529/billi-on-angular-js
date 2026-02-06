from transformers import pipeline

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-hi")

text=input("Enter text in English")

result=translator(text)

print("Translated Text Hindi :", result[0]['translation_text'])