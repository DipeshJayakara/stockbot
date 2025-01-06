# LLM for Market Success: Equity and Stock Market

**StockEquityNavigator** is a Streamlit-based web application that allows users to interact with news articles by extracting and analyzing content from provided URLs. It leverages the `newspaper3k` library for data extraction, Hugging Face Transformers for question answering, and FAISS for vector storage and similarity search. Users can ask questions about the extracted content and receive relevant answers using AI-powered tools.

---

## Features

### ✅ Data Extraction from URLs
- Extracts textual content from news articles using the `newspaper3k` library.
- Allows users to manually input content if URLs fail to fetch data.

### ✅ AI-Powered Q&A
- Uses Hugging Face's **DistilBERT** model for question answering.
- Provides answers based on relevant content from the extracted articles.

### ✅ Efficient Vector Search
- Embeds text content using Hugging Face embeddings.
- Stores embeddings in a **FAISS** index for fast similarity-based search.

### ✅ Streamlit Interface
- Intuitive interface for users to process URLs, input questions, and view results.

### ✅ Persistent Storage
- Saves the FAISS index as a local file (`faiss_store_local.pkl`) for reuse across sessions.

---

## Installation

### Prerequisites
- Python 3.8 or later.
- A system with internet access for model downloads and library installations.

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/StockEquityNavigator.git
   cd StockEquityNavigator
   ```

2. **Install Dependencies**
   Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**
   - Create a `.env` file in the project root if required by specific configurations.

4. **Run the Application**
   Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

---

## How to Use

1. **Enter URLs**: Provide up to 3 news article URLs in the sidebar.
2. **Process Data**: Click "Process URLs" to extract content and build the FAISS index.
3. **Ask Questions**: Use the input field on the main page to ask questions about the processed articles.
4. **View Results**: The app displays the context and answers based on your query.

---

## Code Overview

### Key Components

#### Data Extraction:
- Utilizes `newspaper3k` to fetch article content from URLs.

#### Text Chunking:
- Splits text into manageable chunks using `RecursiveCharacterTextSplitter`.

#### Embedding & Search:
- Embeds text using Hugging Face embeddings and stores in a FAISS index for similarity search.

#### Q&A Pipeline:
- Uses Hugging Face's `pipeline` for generating answers based on the context.

---
