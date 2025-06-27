from transformers import pipeline
import requests
from bs4 import BeautifulSoup

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def chunk_text(text,max_chunk_size=1024):
    return [text[i:i+max_chunk_size]for i in range(0,len(text),max_chunk_size)]

def summarize_text(text):
    chunks = chunk_text(text)
    summaries = []
    for chunk in chunks:
        try:
            summary = summarizer(chunk,max_length=100,min_length=30,do_sample=False)
            summaries.append(summary[0]['summary_text'])
        except Exception as e:
            print("Error while summarizing a chunk:",e)
    return "\n".join(summaries)

def get_text_from_file():
    file_path = input("Enter the path to the file: ")
    with open(file_path,'r',encoding='utf-8') as f:
        return f.read()
    
def get_text_from_link():
    url = input("Enter the URL of the webpage: ")
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    paragraphs = soup.find_all('p')
    return''.join([para.text for para in paragraphs])

def get_text_from_user():
    print("Enter/paste your text below (press ENTER twice to finish):")
    lines = []
    while True:
        line = input()
        if line == '':
            break
        lines.append(line)
    return '\n'.join(lines)

print("\n Choose the input type:")
print("1.Text file(.txt)")
print("2.Paste or type text")
print("3.Web link(URL)")

choice = input("Enter your choice (1/2/3):")

if choice == '1':
    input_text = get_text_from_file()
elif choice == '2':
    input_text = get_text_from_user()
elif choice == '3':
    input_text = get_text_from_link()
else:
    print("Invalid Choice.")
    exit()

print("\n Generated Summary:\n")
print(summarize_text(input_text))    