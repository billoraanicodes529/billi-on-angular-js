from transformers import pipeline

summarizer=pipeline("summarization", model="facebook/bart-large-cnn")

print("Enter chat conversation (Press ENTER twice to finish):")

chat_lines=[]
while True:
    line = input()
    if not line:
        break
    chat_lines.append(line)
    chat_text=" ".join(chat_lines)
    result=summarizer(chat_text,max_length=100, min_length=60, do_sample=False)[0]["summary_text"]
    print("\n Summary.")

    print(result )