# 🤖 Chatbots Repository

A collection of AI-powered chatbots built with Streamlit and Google Gemini API, each designed for specific use cases.

## 📋 Overview

This repository contains multiple chatbot applications that leverage the Google Gemini API to provide intelligent, context-aware responses for different domains. All applications are built using Python and Streamlit for a seamless web interface.

---

## 🚀 Chatbots Included

### 1. **Data Analysis Chatbot** (`data_analysis_chatbot.py`)

An interactive tool for exploring, visualizing, and analyzing CSV datasets using natural language queries.

#### Features:
- 📁 **CSV Upload & Preview**: Upload and preview datasets with instant validation
- 📊 **Smart Chart Generation**: Multiple chart types including:
  - Histograms
  - Bar Charts
  - Pie Charts
  - Line Plots
  - Scatter Plots
  - Box Plots
- 🧠 **AI Chart Suggestions**: Gemini provides intelligent recommendations for optimal chart types based on your data
- 🎨 **Natural Language Chart Requests**: Describe the chart you want in plain English, and the AI generates it
- 📈 **Correlation Heatmaps**: Visualize relationships between numeric variables
- 📊 **Summary Statistics**: View comprehensive statistical summaries of your data
- 💬 **Natural Language Queries**: Ask questions about your data and get AI-powered answers

#### Requirements:
- Python 3.x
- pandas
- matplotlib
- seaborn
- plotly
- google-generativeai
- streamlit
- toml

#### Usage:
```bash
streamlit run data_analysis_chatbot.py
```

---

### 2. **AI-Powered Neurorehabilitation Assistant** (`api_based_chatbot.py`)

A specialized chatbot designed for creating personalized neurorehabilitation plans using medical information and prescription analysis.

#### Features:
- 📝 **Patient Information Input**: Detailed text input for patient history and goals
- 🖼️ **Prescription Image Upload**: Upload prescription images for automatic text extraction
- 🔒 **Privacy Protection**: Automatic redaction of sensitive information (phone numbers, etc.)
- 🏥 **AI-Powered Plan Generation**: Creates detailed 12-week neurorehabilitation plans including:
  - Initial phase (weeks 1-2)
  - Intermediate phase (weeks 3-6)
  - Advanced phase (weeks 7-12)
- 📋 **Comprehensive Assessment**: Provides clinical assessments, exercise recommendations, and safety precautions
- 🎨 **Enhanced UI**: Animated interface with gradient text and Lottie animations
- 📖 **Information Form**: Built-in educational content about the chatbot's capabilities

#### Key Information Requested:
1. Age, Gender, and diagnosis/injury date
2. Current symptoms and medical history
3. Physical goals and activity level
4. Mobility assessment and aids used
5. Cognitive and neurological assessment
6. Psychological concerns
7. Support system availability
8. Previous rehabilitation history

#### Requirements:
- Python 3.x
- google-generativeai
- streamlit
- streamlit-lottie
- pytesseract
- Pillow
- toml
- Tesseract-OCR (Windows: `C:\Program Files\Tesseract-OCR\tesseract.exe`)

#### Usage:
```bash
streamlit run api_based_chatbot.py
```

---

## 🔧 Configuration

### API Key Setup

Both chatbots require a Google Gemini API key. Create a `config.toml` file in the project root:

```toml
[api_keys]
gemini = "your-api-key-here"
```

### Environment Requirements

- **Tesseract OCR** (for neurorehabilitation chatbot):
  - Windows: Install from [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)
  - Update the path in `api_based_chatbot.py` if installation path differs

### Lottie Animations

The neurorehabilitation chatbot uses JSON animation files:
- `assets/api_animation.json`
- `assets/apichatbot.json`

Ensure these files are present in the `assets/` directory.

---

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/au01909/chatbots.git
cd chatbots
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up configuration (see Configuration section above)

4. Run desired chatbot:
```bash
streamlit run data_analysis_chatbot.py
# or
streamlit run api_based_chatbot.py
```

---

## 🛠️ Technology Stack

- **Python 3.x**: Core programming language
- **Streamlit**: Web application framework
- **Google Gemini API**: AI model for intelligent responses
- **Pandas**: Data manipulation and analysis
- **Plotly**: Interactive data visualizations
- **Pillow & Pytesseract**: Image processing and OCR
- **Seaborn & Matplotlib**: Statistical visualizations

---

## 💡 Use Cases

### Data Analysis Chatbot
- Business Intelligence: Analyze sales and performance data
- Research: Explore survey responses and experimental data
- Education: Interactive data exploration for learning
- Prototyping: Quick data visualization without coding

### Neurorehabilitation Assistant
- Patient Recovery Planning: Personalized rehabilitation programs
- Therapy Management: Structured exercise schedules
- Medical Documentation: AI-assisted therapy plans
- Patient Education: Information about recovery phases

---

## 🔐 Privacy & Security

- **Sensitive Data Redaction**: Phone numbers and other sensitive information are automatically redacted from prescription images
- **Secure API Configuration**: API keys are stored in local config files (not tracked in git)
- **User Data**: Information provided to the chatbots is processed securely through Google's API

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs and issues
- Suggest new features
- Improve documentation
- Optimize code

Push improvements to the repository!

---

## 👨‍💻 Developer

**Deekshith B**  
[LinkedIn Profile](https://www.linkedin.com/in/deekshith2912/)

---

## 📝 License

Feel free to customize and use these chatbots for your needs.

---

## 🚦 Getting Started

1. Choose which chatbot fits your needs
2. Follow the installation steps
3. Configure your Gemini API key
4. Run the chatbot with Streamlit
5. Start exploring!

