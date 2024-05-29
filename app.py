from dotenv import load_dotenv
import os
from utils import clean_text
from langchain.text_splitter import CharacterTextSplitter
from PyPDF2 import PdfReader
from langchain.docstore.document import Document
from langchain.document_loaders.pdf import PDFMinerLoader
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain
import textwrap

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

text_splitter = CharacterTextSplitter(separator="chapter", chunk_overlap=100, chunk_size=15000, is_separator_regex=False, keep_separator=True)
pdf_reader = PDFMinerLoader('crime-and-punishment.pdf')
docs = pdf_reader.load_and_split(text_splitter)

cleaned_docs = []
for ind, doc in enumerate(docs):
    cleaned_docs.append(Document(page_content=clean_text(doc.page_content), metadata=doc.metadata))

# Split the last chapter into two sections: chapter and epilogue
last_doc = cleaned_docs.pop()  # Remove the last document from the list
last_chapter, epilogue = last_doc.page_content.split('Epilogue')
cleaned_docs.append(Document(page_content=last_chapter, metadata=last_doc.metadata))
cleaned_docs.append(Document(page_content=f'Epilogue{epilogue}', metadata=last_doc.metadata))

# Define prompts for chapter summary and final summary
map_prompt = """Generate a summary of this chapter of book 'Crime and Punishment' by Fyodor Dostoevsky. It should be a 1 page summary so approximately 300 words. Do not miss important details.

{text}

CHAPTER SUMMARY:"""
MAP_PROMPT = PromptTemplate(template=map_prompt, input_variables=["text"])

combine_prompt = """Combine the below summaries of chapters of book 'Crime and Punishment' by Fyodor Dostoevsky to create a final summary of the book. It should be contain 20 pages so approximately 5500 words.

{text}

20 PAGE SUMMARY:"""
COMBINE_PROMPT = PromptTemplate(template=combine_prompt, input_variables=["text"])

# Initialize the OpenAI model
model = "gpt-3.5-turbo-1106"  # 16k context window
llm = ChatOpenAI(api_key=api_key, temperature=0, model_name=model, max_retries=5)

# Load the summarization chain
chain = load_summarize_chain(llm, chain_type="map_reduce", combine_prompt=COMBINE_PROMPT, map_prompt=MAP_PROMPT)

# Run the summarization chain on cleaned documents
result = chain.run(cleaned_docs)

# Print the final summary
print('\n'.join(textwrap.wrap(result, 80)))
