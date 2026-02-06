text=input("Enter a Paragraph: \n")

sentences=[s for s in text.split(".")if s.strip()]

summary=sentences[0]+"."

print("Number of sentences =", len(sentences))

print("Summmary=", summary)