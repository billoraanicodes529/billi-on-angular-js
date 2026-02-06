from transformers import pipeline

sentiment=pipeline("sentiment-analysis")
text = "I Love using Ai tools, they are amazing!..."

result = sentiment(text)

print(result)