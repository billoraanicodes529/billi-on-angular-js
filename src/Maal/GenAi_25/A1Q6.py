from transformers import pipeline

grammar_corrector=pipeline("text2text-generation", model="grammarly/coedit-large")

sentence=input("Enter the sentence to correct grammar: ")

corrected=grammar_corrector(sentence)[0]['generated_text']

print("\n Original Sentence: ",sentence)
print("Corrected Sentence: ",corrected)