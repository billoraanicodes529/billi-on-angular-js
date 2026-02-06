from sentence_transformers import SentenceTransformer,util

import numpy as np

model=SentenceTransformer("all-MiniLM-L6-v2")

print("Enter the paragraph (press Enter twice to finish):")

lines=[]
while True:
    line=input()
    if line == "":
        break
    lines.append(line)

text ="\n".join(lines)

sentences = text.split("\n")

sentence_embeddings=model.encode(sentences)
paragraph_embedding=model.encode([text])

scores=util.cos_sim(sentence_embeddings,paragraph_embedding)

top_two=np.argsort(scores.flatten())[-2:]
summary=[sentences[i] for i in top_two]

print("\nSummary:")

print("".join(summary))