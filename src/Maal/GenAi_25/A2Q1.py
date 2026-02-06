text="""Generative Ai creates new content such as text and images.
It learns patterns from data.It is used in Chatbots and image creation tools."""

sentences=text.split(".")
summary=sentences[0]+"."+sentences[1]+"."

print("Summmary:",summary)