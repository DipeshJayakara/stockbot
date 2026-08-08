# Research Paper

## LLM for Market Success: Equity and Stock Market

### Publication Details

| Detail | Information |
|---|---|
| **Title** | LLM for Market Success: Equity and Stock Market |
| **Conference** | 2025 Third International Conference on Networks, Multimedia and Information Technology (NMITCON) |
| **Publisher** | IEEE |
| **Authors** | K. Lavanya, Gireesh Babu C N, Isha G Bhat, Dipesh Jayakara Poojary, Jovita Mariam V |
| **Institution** | BMS Institute of Technology & Management, Bengaluru, India |
| **Publication Year** | 2025 |
| **IEEE Xplore** | [View on IEEE Xplore](https://ieeexplore.ieee.org/document/11188052) |

---

## Abstract

This paper presents an intelligent equity research assistant that utilizes Large
Language Models (LLMs) to automate the search, summarization, and analysis of
financial information from web-based sources.

The system leverages FAISS for semantic similarity search and LangChain for
context-aware reasoning and question answering over financial documents.

The workflow includes document ingestion from URLs, content chunking,
embedding generation using HuggingFace, and indexing of document chunks for
semantic retrieval.

The prototype achieved an average response time of 1–3 seconds per query and
demonstrated high semantic relevance in retrieving financial information.

The proposed system aims to reduce manual effort and improve the speed and
efficiency of equity research for financial analysts.

---

## Keywords

- Large Language Models
- Equity Research
- FAISS
- Semantic Retrieval
- StockBot
- LangChain
- Natural Language Processing
- Financial Analysis

---

## Problem Statement

Traditional equity research requires analysts to collect, read, summarize,
and analyze large volumes of financial information from multiple sources.

The paper identifies the need for an end-to-end equity research system that
can automate:

1. Data ingestion from URLs
2. Content summarization
3. Text chunking
4. Embedding generation
5. Semantic retrieval
6. Context preparation
7. Financial question answering

---

## Proposed Solution

StockBot is an LLM-driven equity research assistant designed to provide an
automated workflow for processing financial information.

The system follows the pipeline:

URL Input
   ↓
Content Extraction
   ↓
Summarization
   ↓
Text Chunking
   ↓
Embedding Generation
   ↓
FAISS Vector Index
   ↓
Semantic Retrieval
   ↓
Context Formation
   ↓
Question Answering
   ↓
User Response

---

## Technology Stack

- Python
- Streamlit
- LangChain
- HuggingFace Transformers
- HuggingFace Embeddings
- FAISS
- Newspaper3k
- BART
- DistilBERT
- dotenv

---

## System Workflow

### 1. Data Collection

Users provide financial news article URLs through the Streamlit interface.
Newspaper3k extracts the article content.

If URL extraction fails, users can manually provide the article content.

### 2. Summarization

The BART `facebook/bart-large-cnn` model is used to summarize the
extracted articles.

### 3. Text Chunking

The combined content is divided into smaller chunks using
`RecursiveCharacterTextSplitter`.

### 4. Embedding Generation

HuggingFace Embeddings convert the text chunks into numerical vector
representations.

### 5. FAISS Indexing

FAISS stores and indexes the generated embeddings to support efficient
similarity-based retrieval.

### 6. Query Processing

When a user submits a question, the system performs semantic similarity
search and retrieves the top relevant documents.

### 7. Question Answering

The retrieved context is passed to the question-answering model, which
generates a context-aware response.

---

## Performance

According to the research evaluation:

| Process | Estimated Time |
|---|---:|
| Data Loading from URLs | 5–20 seconds per URL |
| Content Summarization | 10–30 seconds |
| Text Splitting | 2–5 seconds |
| Embedding Generation | 20–60 seconds |
| FAISS Index Saving | 1–3 seconds |
| Data Retrieval | < 1 second per query |
| Question Answering | 1–3 seconds per query |

---

## Manual Research vs StockBot

| Aspect | Manual Research | StockBot |
|---|---|---|
| Data Source | Manual search | Automatic URL parsing |
| Reading Time | 30–45 minutes | < 1 minute |
| Summarization | Manual | LLM-based |
| Search Method | Ctrl+F / Manual skim | Semantic search using FAISS |
| Q&A | Manual analysis | Instant response |
| Scalability | Low | High |
| Consistency | Varies | Reliable |

---

## Results

The prototype demonstrated that StockBot can significantly reduce the time
required for financial news research.

The system provides:

- Automated financial article processing
- Fast semantic retrieval
- Automated summarization
- Context-aware question answering
- Reduced manual research effort
- Scalable financial information processing

The paper reports that data retrieval and question answering achieved very
fast response times, while embedding generation and summarization required
more computational processing depending on the size of the input data.

---

## Future Work

The paper identifies several possible improvements:

- Multilingual support
- Domain-specific LLM fine-tuning
- Voice-based query interaction
- Embedding quantization
- Integration with live news feeds
- Further evaluation with financial professionals
- Validation in live-market environments

---

## Publication

This work was published at:

**2025 Third International Conference on Networks, Multimedia and
Information Technology (NMITCON)**

**IEEE**

### IEEE Xplore

[View the Published Paper](https://ieeexplore.ieee.org/document/11188052)

---

## Citation

```text
K. Lavanya, Gireesh Babu C N, Isha G Bhat, Dipesh Jayakara Poojary,
and Jovita Mariam V, "LLM for Market Success: Equity and Stock Market,"
2025 Third International Conference on Networks, Multimedia and
Information Technology (NMITCON), IEEE, 2025.
