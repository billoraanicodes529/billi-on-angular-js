from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis")

sentences=[
    "This movie was amazing and inspring",
    "I did not like the food at the restaurant",
    "The whethter today is okay"
]

results = sentiment_analyzer(sentences)
for i, result in enumerate(results):

    print(f"Sentences:{sentences[i]}")
    print(f"Sentiment: {result['label']}")
    print(round(result['score'],3))
    print()