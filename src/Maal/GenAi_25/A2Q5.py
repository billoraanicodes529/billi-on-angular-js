from transformers import BertTokenizer

tokenizer=BertTokenizer.from_pretrained("bert-base-uncased")

text=input("Enter Sentence :\n")

tokens=tokenizer.tokenize(text.lower())

unique_words=[]

for word in tokens:
    if word not in unique_words:
        unique_words.append(word)

print("\n SummarizednmParagraph (After Removing Repeated Words):")

print(" ".join(unique_words))