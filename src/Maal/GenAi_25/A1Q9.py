from sentence_transformers import SentenceTransformer ,util

model=SentenceTransformer('all-MiniLM-L6-v2')

s1=input("Enter First prompt: ")
s2=input("Enter Second prompt: ")
emb1=model.encode(s1)
emb2=model.encode(s2)

similarity = util.cos_sim(emb1,emb2)
print("Similarity Score :" , similarity.item())
