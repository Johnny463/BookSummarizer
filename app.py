from dotenv import load_dotenv
import os
from PyPDF2 import PdfReader
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain
from langchain.llms import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
import json
from utils import clean_text,create_pdf

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
llm = OpenAI(temperature=0)

def main():
    summary_list = []  # Initialize list to store summaries
    
    pdf_reader = PdfReader('crime-and-punishment.pdf')
    i = 6  # starting chapter 1
    j = 23
    while i < len(pdf_reader.pages):
        text = ""
        # Extracting text from pages
        for page in pdf_reader.pages[i:j]:
            text += page.extract_text()
                
        # Cleans text
        text = clean_text(text)         
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=0,
            length_function=len
        )
        chunks = text_splitter.split_text(text=text)
        docs = [Document(page_content=t) for t in chunks]
        chain = load_summarize_chain(llm, chain_type="map_reduce")
        summary = chain.run(docs)
        summary_list.append(summary)  # Append summary to list
        
        i += 16
        j += 16
        
    create_pdf('\n'.join(summary_list))  # Create PDF with all summaries
    
    # Dump summary list to JSON file
    with open("summary.json", "w") as f:
        json.dump(summary_list, f, indent=4)

if __name__ == "__main__":
    main()
