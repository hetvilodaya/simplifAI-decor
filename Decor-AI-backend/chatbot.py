from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from dotenv import load_dotenv
from langchain.llms import HuggingFaceHub
from dotenv import *
from PyPDF2 import PdfReader
import spacy
from collections import Counter

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    #embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    #llm = HuggingFaceHub(repo_id="google/flan-t5-small", model_kwargs={"temperature":0.5, "max_length":512})
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

def process_pdf_documents(text):


    # get the text chunks
    text_chunks = get_text_chunks(text)

    # create vector store
    vectorstore = get_vectorstore(text_chunks)

    # create conversation chain
    conversation_chain = get_conversation_chain(vectorstore)
    return conversation_chain




if __name__ == '__main__':
    load_dotenv()
    pdf_docs = ['Interior-Design-Basics-red.pdf']  # Provide the paths to the PDF documents "path_to_pdf2.pdf"
    pdf_text = get_pdf_text(pdf_docs)
    conversation_chain = process_pdf_documents(pdf_text)

    while True:
        user_question = input("Enter your question (or 'exit' to quit): ")
        if user_question.lower() == 'exit':
            break

        response = conversation_chain({'question': user_question})
        chat_history = response['chat_history']

        for i, message in enumerate(chat_history):
            if i % 2 == 0:
                print(f"User: {message.content}")
            else:
                print(f"Bot: {message.content}")