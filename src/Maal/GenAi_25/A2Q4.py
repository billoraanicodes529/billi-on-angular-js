import torch
from transformers import BertTokenizer

import nltk

from nltk.corpus import stopwords

nltk.download('stopwords')

tokenizer=BertTokenizer.from_pretrained("bert-base-uncased")

text=input("Enter Sentence :\n")

tokens=tokenizer.tokenize(text.lower())

stop_words = set(stopwords.words('english'))

meaningful_words=[word for word in tokens if word not in stop_words]

print("\n Meaningful Words :")

print("".join(meaningful_words))