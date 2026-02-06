from transformers import pipeline
qa_model=pipeline("question-answering")

context="""The Sun is the center of our Solar System. 
It is a huge ball of hot gases.
Earth revolves around the Sun in 356 days."""

question="How many days does Earth take to revolve around the Sun?"

result=qa_model(question=question,context=context)

print("Answer",result["answer"])    