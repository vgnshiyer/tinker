import streamlit as st
import csv
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import HuggingFaceHub

def getCsvText(csvPath):
    text_data = ''
    with open(csvPath, 'r', encoding='utf-8', errors='replace') as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            text_data += ''.join(row) + '\n'
    return text_data

def get_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator='\n',
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(chunks):
    embeddings = HuggingFaceInstructEmbeddings(model_name='hkunlp/instructor-base')
    vector_store = FAISS.from_texts(texts=chunks, embedding=embeddings)
    return vector_store

def get_question(vector_store):
    llm = HuggingFaceHub(repo_id='google/flan-t5-small', huggingfacehub_api_token='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', model_kwargs={'temperature':0.2, 'max_length':512})
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(),
        memory=memory
    )
    return conversation_chain

def handle_user_question(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.write(response)

def main():
    st.set_page_config(page_title="CrimeLens", page_icon=":cop:", layout="wide")

    st.header("CrimeLens")
    user_question = st.text_input("Ask me anything related to crime in the US!")
    if user_question:
        handle_user_question(user_question)

    with st.sidebar:
        st.header("About CrimeLens")
        st.markdown("CrimeLens is a chatbot that answers questions about crime in the US. CrimeLens uses the [FBI Crime Data Explorer API](https://crime-data-explorer.fr.cloud.gov/api) to answer questions about crime in the US. CrimeLens is built with [Streamlit](https://streamlit.io/), a Python library for building data apps.")

    with st.spinner("Loading..."):
        # get csv
        raw_text = getCsvText('./homicide-data.csv')

        # get text chunks
        chunks = get_chunks(raw_text)

        # create vector store
        vector_store = get_vector_store(chunks)

        # get question
        st.session_state.conversation = get_question(vector_store)

if __name__ == "__main__":
    main()