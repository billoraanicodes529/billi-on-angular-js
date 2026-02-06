from transformers import pipeline 

summarizer = pipeline("summarization")

article="""
Artificial Intelligence (AI) has rapidly transformed modern technology.
It is used in healthcare ,finance ,education, tranportation, and many more sectors.
AI system can analyzer large datasets,detect patterns,and make prediction faster than humans.
With advancemnets in machine learing and deep learning.AI is expert to bring even more automation and innovation.
However, ethical concerns such as bias, privacy, and job displacement must be ensure
reponsible and beneficial use of this technology."""

summary=summarizer(article, max_length=90, min_length=60)

print("=== 3-Line Summary ===")

print(summary[0]['summary_text'])