

# 🤖 The Chatbot Hub

> A comprehensive collection of chatbot implementations built with **Python**, **Streamlit**, **Google Gemini**, **LangChain**, and **Natural Language Processing**.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red)
![Gemini](https://img.shields.io/badge/Google-Gemini-blue)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## Overview

The Chatbot Hub is a collection of multiple chatbot architectures implemented in Python. Instead of demonstrating only one conversational agent, this project showcases how different chatbot technologies solve different real-world problems.

Each chatbot uses a different approach:

* Rule-Based Systems
* Keyword Matching
* Large Language Models (LLMs)
* Retrieval-Augmented Generation (RAG)
* Voice AI
* Multilingual Translation
* AI-powered Data Analysis

The application is built using **Streamlit**, allowing users to switch seamlessly between chatbot implementations from a single interface. 

---

# Repository Structure

```text
chatbots/
│
├── main.py                      # Main application
├── home.py                      # Landing page
│
├── rule_based_chatbot.py
├── keyword_based_chatbot.py
├── api_based_chatbot.py
├── rag_chatbot.py
├── data_analysis_chatbot.py
├── multi_lingual_chatbot.py
├── voice_chatbot.py
│
├── config.toml
├── requirements.txt
│
├── assets/
│
└── README.md
```

---

# Architecture

```text
                            User
                              │
                              ▼
                   Streamlit Web Interface
                              │
                ┌─────────────┼──────────────┐
                │             │              │
                ▼             ▼              ▼
        Navigation Menu   Session State   UI Components
                │
        Select Chatbot
                │
 ┌──────────────┼─────────────────────────────────────────────┐
 │              │              │            │                 │
 ▼              ▼              ▼            ▼                 ▼
Rule Bot   Keyword Bot     Gemini Bot   RAG Bot      Voice Assistant
 │              │              │            │                 │
Rules       Dictionary      Gemini API  FAISS          Speech Recognition
Matching    Matching            │        Embeddings           │
 │              │              │            │                 │
 └──────────────┴──────────────┴────────────┴─────────────────┘
                              │
                              ▼
                        Streamlit Output
```

---

# 🚀 Chatbots Included

---

# 1. 📊 Data Analysis Chatbot (`data_analysis_chatbot.py`)

An AI-powered data analysis assistant that enables users to upload CSV datasets, generate interactive visualizations, and ask natural language questions about their data. It combines traditional analytics libraries with Google's Gemini model to simplify exploratory data analysis. 

## ✨ Features

* 📁 CSV Upload & Preview

  * Upload datasets instantly
  * Automatic validation
  * Interactive dataframe preview

* 📊 Smart Chart Generator

  * Histogram
  * Bar Chart
  * Pie Chart
  * Scatter Plot
  * Line Plot
  * Box Plot

* 🤖 Gemini Chart Recommendation

  * AI suggests the best visualization
  * Explains why the chart is suitable

* 💬 Natural Language Visualization

  * Type:

    ```
    Show a scatter plot of Age vs Salary
    ```
  * AI automatically generates the requested chart.

* 📈 Correlation Heatmap

  * Detect relationships between numerical variables
  * Interactive statistical visualization

* 📊 Summary Statistics

  * Mean
  * Median
  * Standard Deviation
  * Missing values
  * Distribution insights

* 🧠 AI Dataset Analysis

  * Ask questions like:

    * Which column has the highest variance?
    * Explain this dataset.
    * Find interesting insights.

---

## ⚙️ How It Works

```text
CSV Upload
      │
      ▼
Pandas DataFrame
      │
      ├───────────────┐
      ▼               ▼
Statistics      Gemini Analysis
      │               │
      ▼               ▼
Charts      Chart Recommendation
      │               │
      └───────┬───────┘
              ▼
      Interactive Dashboard
```

---

## 🛠 Requirements

* Python 3.x
* Streamlit
* Pandas
* Plotly
* Matplotlib
* Seaborn
* Google Gemini API
* TOML

---

## ▶️ Usage

```bash
streamlit run data_analysis_chatbot.py
```

---

# 2. 🏥 AI-Powered Neurorehabilitation Assistant (`api_based_chatbot.py`)

A healthcare chatbot that assists patients and therapists by generating personalized neurorehabilitation plans using Google Gemini. The chatbot can process patient information manually or extract prescription details using OCR before generating structured recovery plans. 

---

## ✨ Features

### 📝 Patient Information Collection

Collects:

* Age
* Gender
* Diagnosis
* Injury date
* Symptoms
* Medical history
* Physical goals
* Current mobility
* Cognitive assessment
* Psychological assessment
* Family support
* Previous rehabilitation

---

### 📄 Prescription Upload

Users can upload:

* JPG
* PNG
* JPEG

The chatbot automatically extracts text using OCR.

---

### 🔒 Privacy Protection

Automatically removes sensitive information such as:

* Phone numbers
* Personal identifiers

before sending the prompt to Gemini.

---

### 🤖 AI Rehabilitation Planning

Generates a personalized rehabilitation plan covering:

#### Initial Phase (Weeks 1–2)

* Basic mobility
* Pain management
* Balance exercises

#### Intermediate Phase (Weeks 3–6)

* Strength training
* Functional activities
* Walking practice

#### Advanced Phase (Weeks 7–12)

* Independence training
* Advanced exercises
* Daily activity planning

---

### 📋 Comprehensive Clinical Assessment

Provides:

* Patient assessment
* Exercise schedule
* Safety precautions
* Recovery recommendations
* Lifestyle suggestions

---

### 🎨 Interactive Interface

* Gradient UI
* Lottie animations
* Upload preview
* OCR visualization
* Extracted text
* Redacted text
* AI response generation

---

## ⚙️ How It Works

```text
Patient Details
       │
       ▼
Prescription Upload
       │
       ▼
OCR (Tesseract)
       │
       ▼
Sensitive Data Redaction
       │
       ▼
Prompt Engineering
       │
       ▼
Google Gemini
       │
       ▼
Personalized
12-Week Recovery Plan
```

---

## 📥 Input Information

The chatbot expects:

1. Age
2. Gender
3. Diagnosis
4. Symptoms
5. Medical history
6. Physical goals
7. Mobility assessment
8. Cognitive assessment
9. Emotional status
10. Family support
11. Previous therapy
12. Rehabilitation devices

---

## 🛠 Requirements

* Python 3.x
* Streamlit
* Google Gemini
* Streamlit Lottie
* Pillow
* PyTesseract
* TOML

---

## Additional Requirements

### Tesseract OCR

Windows

```
C:\Program Files\Tesseract-OCR\tesseract.exe
```

Linux

```bash
sudo apt install tesseract-ocr
```

Mac

```bash
brew install tesseract
```

---

## ▶️ Usage

```bash
streamlit run api_based_chatbot.py
```

---

# 3. 📚 Document RAG Chatbot (`rag_chatbot.py`)

An intelligent Retrieval-Augmented Generation (RAG) chatbot that answers questions directly from uploaded PDF documents. Instead of relying solely on the LLM's pretrained knowledge, it retrieves relevant document chunks using semantic search and generates context-aware responses. 

## ✨ Features

* 📄 Upload PDF documents
* ✂️ Automatic text chunking
* 🧠 Google Gemini embeddings
* 🗂️ FAISS vector database
* 🔍 Semantic similarity search
* 💬 Context-aware question answering
* 📚 Displays retrieved document chunks
* ⚡ Fast retrieval pipeline

## ⚙️ How It Works

```text
Upload PDF
     │
     ▼
Extract Text
     │
     ▼
Chunk Document
     │
     ▼
Generate Embeddings
     │
     ▼
Store in FAISS
     │
     ▼
User Question
     │
     ▼
Similarity Search
     │
     ▼
Relevant Chunks
     │
     ▼
Gemini LLM
     │
     ▼
Answer
```

## 🛠 Requirements

* LangChain
* FAISS
* Google Gemini
* PyPDFLoader
* Streamlit

## ▶️ Usage

```bash
streamlit run rag_chatbot.py
```

---

# 4. 🌍 Multilingual Chatbot (`multi_lingual_chatbot.py`)

A multilingual translation assistant supporting numerous Indian languages with integrated text-to-speech. It translates user input using Google Translate and plays the translated audio using Google Text-to-Speech. 

## ✨ Features

* 🌐 Translation between 20+ Indian languages
* 🔊 Voice playback of translated text
* ⚡ Auto-play option
* 📝 Live translation preview
* 🎤 Audio generation using gTTS

## ⚙️ How It Works

```text
Input Text
     │
     ▼
Google Translate
     │
     ▼
Translated Text
     │
     ▼
Google Text-to-Speech
     │
     ▼
Audio Playback
```

## 🛠 Requirements

* googletrans
* gTTS
* Streamlit

## ▶️ Usage

```bash
streamlit run multi_lingual_chatbot.py
```

---

# 5. 🎙️ Voice Assistant (`voice_chatbot.py`)

A multimodal chatbot that supports both voice and text interactions. User speech is converted into text, processed by Gemini, and returned as both text and synthesized speech. 

## ✨ Features

* 🎤 Voice input
* ⌨️ Text input
* 🤖 Gemini-powered responses
* 🔊 Automatic speech synthesis
* 💬 Conversation history
* 🎨 Responsive Streamlit interface

## ⚙️ How It Works

```text
Voice/Text Input
      │
      ▼
Speech Recognition
      │
      ▼
Gemini API
      │
      ▼
Response
      │
      ▼
Google Text-to-Speech
      │
      ▼
Audio Output
```

## 🛠 Requirements

* SpeechRecognition
* gTTS
* Google Gemini
* Streamlit

## ▶️ Usage

```bash
streamlit run voice_chatbot.py
```

---

# 6. ❤️ HeartPedia Keyword-Based Chatbot (`keyword_based_chatbot.py`)

A lightweight medical information chatbot that provides educational explanations for predefined cardiovascular terms. It performs case-insensitive keyword matching against an internal dictionary to return curated content. 

## ✨ Features

* ❤️ Heart disease glossary
* 🔎 Case-insensitive keyword matching
* 📖 Educational definitions
* ⚡ Instant responses
* 🚫 Handles unknown terms gracefully

## ⚙️ How It Works

```text
User Input
     │
     ▼
Lowercase Conversion
     │
     ▼
Dictionary Lookup
     │
     ├── Match Found
     │       │
     │       ▼
     │  Return Definition
     │
     └── No Match
             │
             ▼
      "Keyword Not Found"
```

## ▶️ Usage

```bash
streamlit run keyword_based_chatbot.py
```

---

# 7. 🚆 Rule-Based Train Booking Chatbot (`rule_based_chatbot.py`)

A rule-driven chatbot that simulates an interactive train ticket booking system. It guides users through passenger selection, station choices, fare calculation, and a mock payment workflow using predefined conversational logic. 

## ✨ Features

* 🚉 Guided booking flow
* 👥 Passenger selection
* 📍 Source and destination selection
* 💰 Automatic fare calculation
* 💳 Simulated payment
* 🧾 Booking confirmation
* 🔄 Session state management

## ⚙️ How It Works

```text
Start Booking
      │
      ▼
Passenger Count
      │
      ▼
Departure Station
      │
      ▼
Destination Station
      │
      ▼
Fare Calculation
      │
      ▼
Payment Simulation
      │
      ▼
Booking Confirmation
```

## ▶️ Usage

```bash
streamlit run rule_based_chatbot.py
```

This format is much more consistent and gives each chatbot the same level of detail, making the README look polished and professional.


# Installation

```bash
git clone https://github.com/au01909/chatbots.git

cd chatbots

pip install -r requirements.txt
```

---

# Configure Gemini

Create a `config.toml`

```toml
[api_keys]
gemini = "YOUR_GEMINI_API_KEY"
```

The application expects the Gemini API key to be provided in this configuration file. 

---

# Run

```bash
streamlit run main.py
```

This launches the Chatbot Hub, where users can navigate between the Home page and the various chatbot implementations from a sidebar menu. 

---

# Learning Objectives

This repository demonstrates:

* Rule-Based Chatbots
* Keyword Matching
* Prompt Engineering
* Generative AI
* Retrieval-Augmented Generation
* Vector Databases
* Semantic Search
* OCR
* Speech Recognition
* Text-to-Speech
* Multilingual NLP
* AI-powered Data Analytics
* Streamlit Application Development

---

# Future Improvements

* Conversation memory across chatbots
* Multi-document RAG
* Streaming LLM responses
* Agentic workflows
* Authentication
* Chat history database
* Docker deployment
* Cloud hosting
* Model selection (Gemini, OpenAI, Claude, Ollama)
* Evaluation metrics
* Fine-tuned domain models

---

# License

This project is released under the MIT License.

---

