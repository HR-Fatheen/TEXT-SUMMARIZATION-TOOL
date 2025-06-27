# NLP Text Summarization Tool Using Hugging Face Transformers

## Internship Credentials

- *Intern Name*: Mohamed Fatheen H.R 
- *Intern ID*: CT06DG2241
- *Domain*: AI Developer Intern  
- *Company*: CodTech IT Solutions
- *Internship Duration*: 4 Weeks 
- *Mentor*: Neela Santosh Kumar

## Project Description

The Text Summarization Tool created during this internship is an intelligent application built with Natural Language Processing (NLP). Its job is to automatically produce short summaries from large texts. With so much information available online now, it’s easy to feel overwhelmed by long articles, reports, or documents. This project’s goal is to make that easier by offering a simple and effective tool that can turn lengthy content into just a few key sentences, emphasizing the most important parts.

It supports three input sources:
- 📁 Text files (.txt)
- 📝 Manual text input
- 🌐 Web page content via URLs

### Purpose

The main goal of this tool is to help people understand and access written information more easily. Whether it’s a long blog post, a Wikipedia article, or a document you upload, this tool pulls out the main points to make reading quicker and simpler. In real life, students, researchers, journalists, business people, and anyone who wants to get the gist of a big text without reading it all can benefit from this.

This fits with the bigger aim of NLP in AI: helping machines understand, process, and generate human language so that makes sense. The summarization model tries to imitate how people find meaning in what they read, making it easier to read smarter and make better decisions. 

## Project Motivation

In today’s world where data piles up fast, dealing with so much information is a real challenge. Reading through long documents or web pages can take a lot of time and energy. This summarization tool aims to solve that problem by reducing large chunks of text into short, useful summaries, thanks to advanced NLP models. I built this as a learning project during my internship, focusing on practical skills like using Hugging Face pipelines, basic web scraping, and writing interactive Python code.

### Coded Platform

This tool is built entirely with Python, using the Transformers library from Hugging Face. For summarization, it uses the popular BART model—specifically the facebook/bart-large-cnn version—which is highly regarded in the AI community for its ability to generate concise, human-like summaries.

The whole project runs in a virtual Python environment to keep dependencies tidy and avoid conflicts. The main libraries involved are:

- transformers – for loading and using the pre-trained summarization model.
- requests – to fetch HTML content from the web.
- beautifulsoup4 – to parse and extract readable content from web pages.
- torch – underlying deep learning computations (via the Transformers model).
- os and input() – to handle file paths and user inputs.

The script is executed via the command line, where the user is prompted to choose one of three input methods: uploading a text file, entering/pasting text manually, or providing a web URL.

## Features

- Summarize content from plain text files
- Extract and summarize paragraphs from any valid URL
- Accept direct user input via command-line
- Chunk long text into segments for model compatibility
- Powered by facebook/bart-large-cnn, one of the best pre-trained summarization models
- Tested with long Wikipedia articles and academic notes

## Project Structure

- project folder
- coding.py             # Main Python script for summarization 
- README.md             # Detailed documentation file (this file) 
- installation.txt      # Python dependencies 
- sample.txt            # Example input file 

## How It Works

When the program starts, the user selects the input source. Depending on the choice:

1. *Text File*: The file path is taken from the user. The .txt file is read and passed to the summarization function.
2. *Manual Input*: The user can paste or type text directly into the terminal, which is captured line by line until an empty line is entered.
3. *Web Link*: The user provides a URL. The script uses requests and BeautifulSoup to extract paragraph content (<p> tags) from the webpage.

After collecting the text, it’s preprocessed and split into smaller chunks to prevent token limits from being exceeded. Each chunk is then summarized using Hugging Face’s summarization pipeline. The individual summaries are combined to create the final result. 

The BART model performs abstractive summarization, which means it rewrites and paraphrases the content instead of just copying key sentences. It’s been fine-tuned on datasets like CNN/Daily Mail, making it especially good at summarizing news articles or similar long-form texts.

To handle lengthy articles, the script breaks down the input into manageable pieces and processes each separately, ensuring compatibility across different text sizes.

## Example Output

![Image](https://github.com/user-attachments/assets/2960dd92-a179-43d8-817b-8f28dd49951f)
