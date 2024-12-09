import os
import pickle
import re
from newspaper import Article
from dotenv import load_dotenv
from transformers import pipeline
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document
import streamlit as st

# Load environment variables from .env file
load_dotenv()

# Set Streamlit page configuration
st.set_page_config(page_title="StockEquityNavigator", layout="wide")

# Initialize global variables
vector_store = None
file_path = "faiss_store_local.pkl"

# Use a smaller Hugging Face model for question-answering
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")


# Function to load and extract text content from URLs using newspaper3k
def load_data(urls):
    data = []
    for url in urls:
        if url:  # Ensure URL is not empty
            try:
                article = Article(url)
                article.download()
                article.parse()
                text_content = article.text
                # Split content into chunks
                chunks = get_text_chunks(text_content)
                for chunk in chunks:
                    data.append({"page_content": chunk, "metadata": {"source": url}})
            except Exception as e:
                st.warning(f"Error fetching {url}: {e}")
                manual_input = st.text_area(f"Please paste the content for {url} here:", key=f"manual_input_{url}")
                if manual_input:
                    chunks = get_text_chunks(manual_input)
                    for chunk in chunks:
                        data.append({"page_content": chunk, "metadata": {"source": url}})
    if not data:
        raise ValueError("No data loaded from URLs. Please check your input or manually input content.")
    return data


# Function to split text into chunks
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000,
                                                   chunk_overlap=400)  # Adjust chunk size and overlap for better context
    chunks = text_splitter.split_text(text)
    return chunks


# Function to generate embeddings and store in FAISS
def get_vector_store(text_chunks):
    embeddings = HuggingFaceEmbeddings()
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    return vector_store


# Function to handle user queries
def user_input(user_question):
    global vector_store
    if vector_store is not None:
        # Search for relevant documents in the vector store based on the user question
        docs = vector_store.similarity_search(user_question)

        # If documents are found, concatenate their content to form the context
        if docs:
            context = " ".join([doc.page_content for doc in docs])
            # Ensure that the context ends with a complete sentence or paragraph
            context = ensure_complete_context(context)
            # Clean up unwanted statements in the context
            context = clean_context(context)
        else:
            context = "No relevant documents found."

        # Display the context used for answering the question
        st.write("Context used for answering:")
        st.write(context)

        # Using the question-answering pipeline to get the answer
        try:
            result = qa_pipeline(question=user_question, context=context)
            answer = result.get("answer", "No answer found")
            return answer
        except Exception as e:
            st.error(f"Error with question-answering model: {e}")
            return "Error processing the question."
    else:
        return "Vector store is not available. Please process the URLs first."


# Function to ensure the context ends with a complete sentence
def ensure_complete_context(context):
    # Simple heuristic: Ensure the context ends with a complete sentence
    if not context:
        return context
    if context[-1] in ['.', '!', '?']:
        return context
    # If the context does not end with a punctuation mark, try to append a period
    return context + '.'


# Function to clean up unwanted statements from the context
def clean_context(context):
    # Define unwanted patterns or phrases
    unwanted_patterns = [
        r"\(You can now subscribe to our.*?\)",  # Subscription or advertisement patterns
        r"\b(Bloomberg|Reuters|ETMarkets|Subscribe|Privacy Policy|Terms of Use)\b",  # Common unwanted terms
        r"\b(https?://\S+)\b",  # URLs
    ]

    # Combine patterns into a single regex pattern
    combined_pattern = '|'.join(unwanted_patterns)

    # Remove unwanted patterns from the context
    cleaned_context = re.sub(combined_pattern, "", context, flags=re.IGNORECASE)
    cleaned_context = " ".join(cleaned_context.split())  # Remove extra spaces
    return cleaned_context


# Main function for Streamlit app
def main():
    global vector_store  # Access the global variable vector_store
    st.header("Chat with News Articles")  # Set the header of the Streamlit app

    # Collect URLs from user input in the sidebar with unique keys
    urls = [st.sidebar.text_input(f"URL {i + 1}", key=f"url_{i}") for i in range(3)]
    # This creates three text input fields in the sidebar for URL entries.

    # Button to process the URLs
    process_url_clicked = st.sidebar.button("Process URLs")
    # This creates a button in the sidebar that, when clicked, will process the URLs entered by the user.

    if process_url_clicked:  # Check if the "Process URLs" button was clicked
        try:
            with st.spinner("Processing..."):  # Show a spinner while processing
                data = load_data(urls)  # Load and process the data from the provided URLs
                text_chunks = [doc["page_content"] for doc in data]  # Extract text chunks from the loaded data
                vector_store = get_vector_store(text_chunks)  # Generate and store embeddings in FAISS

                # Save the vector store to a file
                with open(file_path, "wb") as f:
                    pickle.dump(vector_store, f)  # Serialize the vector store object to the file
                st.success("Processing complete. Vector store saved successfully.")
                # Display a success message to the user
        except ValueError as ve:
            st.error(f"ValueError: {str(ve)}")  # Display an error message if no data is loaded
        except Exception as e:
            st.error(f"Error processing URLs: {str(e)}")  # Display an error message for other exceptions

    # Input for user query
    user_question = st.text_input("Ask a Question from the URLs")
    # Create a text input field for the user to ask questions based on the processed URLs.

    if user_question:  # Check if the user has entered a question
        if os.path.exists(file_path):  # Check if the FAISS index file exists
            try:
                with open(file_path, "rb") as f:
                    vector_store = pickle.load(f)  # Load the vector store from the file
                    answer = user_input(user_question)  # Get the answer to the user's question
                    st.write("Reply: ", answer)  # Display the answer to the user
            except EOFError as e:
                st.error(f"Error loading FAISS index: End of file reached unexpectedly. {e}")
            except pickle.UnpicklingError as e:
                st.error(f"Error loading FAISS index: Pickle error. {e}")
            except Exception as e:
                st.error(f"Error loading FAISS index: {e}")
        else:
            st.error("FAISS index file not found. Please process the URLs first.")
            # Display an error message if the FAISS index file does not exist


if __name__ == "__main__":
    main()
