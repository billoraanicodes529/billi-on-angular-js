from transformers import pipeline

classifier=pipeline("zero-shot-classification")

text="The Indian cricket team won the match bt 5 wickets."
labels=["Sports","Polictics","Technology"]

result=classifier(text,candidate_labels=labels)

print(result)