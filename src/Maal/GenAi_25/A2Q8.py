from transformers import pipeline

summarizer=pipeline("summarization", model="facebook/bart-large-cnn")

print("Enter a story to summarize:")

story_text=input()

summary=summarizer(story_text, max_length=60, min_length=15)

print("\n--- Original story ---")

print(story_text)

print("\n ---- Summary ----")

print(summary[0]['summary_text'])