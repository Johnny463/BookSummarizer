from dotenv import load_dotenv
import os
from utils import clean_text, create_pdf
from PyPDF2 import PdfReader
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain
from langchain.llms import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
import json
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
llm = OpenAI(temperature=0)
def main():
    summary_ = ""
    pdf_reader = PdfReader('crime-and-punishment.pdf')
    count=0
    i=6 # starting chapter 1
    j=23
    while(count<49):
        text = ""
        #extracting text from 16 pages
        for page in pdf_reader.pages[i:j]:
                text += page.extract_text()
                
        #cleans text
        text=clean_text(text)         
        text_splitter = RecursiveCharacterTextSplitter(
                    chunk_size=1000,
                    chunk_overlap=0,
                    length_function=len
                    )
        chunks = text_splitter.split_text(text=text)
        docs = [Document(page_content=t) for t in chunks]
        chain = load_summarize_chain(llm, chain_type="map_reduce")
        summary = chain.run(docs)
        summary_=summary_+summary
        create_pdf(summary_)
        i=i+16
        j=j+16
        count=count+1
        if os.path.exists("summary.json"):
                with open("summary.json", "w") as f:
                      json.dump(summary_, f, indent=4)
if __name__ == "__main__":
      main()

