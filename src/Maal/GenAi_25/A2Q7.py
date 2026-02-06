from transformers import pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

text_to_summarize=""""
AI is rapidly expanding feild that has revolutionized varoius aspects of
mordern life. It encomplete machine learning, deep learning, natural language
processing, and computers vision.AI system are designed to perform task that typically require
human intelligence, such as problem-solving , learning ,and understanding language.
From powering virtual assistance and desicion making and understanding.
"""

summary=summarizer(text_to_summarize, max_length=100, min_length=60, do_sample=False)

print("Original Text :\n",text_to_summarize)

print("\n Abstraction Summary: \n" , summary[0]['summary_text'])