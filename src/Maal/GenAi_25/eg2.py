from transformers import pipeline
qa_model=pipeline("question-answering")

con=input("Enter Context:")

ques=input("Enter the Question:")


result=qa_model(question=ques,context=con)

print("Answer",result["answer"])