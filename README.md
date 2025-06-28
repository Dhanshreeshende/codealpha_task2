# 🤖 FAQ Chatbot – CodeAlpha Task 2

A simple chatbot built using NLP and Streamlit that responds to frequently asked questions using cosine similarity.

## 🚀 Features

- Preprocesses user input and FAQs using NLTK
- Uses TF-IDF and cosine similarity to find the closest matching question
- Displays the most relevant answer
- Clean and interactive chat UI using Streamlit

## 📦 Requirements

- Python 3.7+
- Streamlit
- Scikit-learn
- Numpy
- NLTK

## 🛠️ Installation

1. **Clone the repository:**
   git clone https://github.com/Dhanshreeshende/codealpha_task2.git
   cd codealpha_task2

2.**(Optional) Create a virtual environment:**
python -m venv venv
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate

3.**Install dependencies:**
pip install -r requirements.txt

**▶️ How to Run**
Run the chatbot using Streamlit:
streamlit run app.py


**✅ Task Completion**
This project is developed as part of my internship at CodeAlpha under Task 2: Chatbot for FAQs.
It demonstrates the use of Natural Language Processing (NLP) techniques to build a basic FAQ chatbot interface.

**📝 Notes**
You can add your own questions and answers in the faq_data.csv file.

Don't forget to download necessary NLTK data (e.g., punkt, stopwords) if running for the first time.

**📄 License**
This project is for educational purposes and part of an internship assignment. No commercial license is attached.



