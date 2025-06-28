import json
import streamlit as st
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string
import nltk

# Setup tokenizer
tokenizer = RegexpTokenizer(r'\w+')

# Optional: download stopwords if not already available
try:
    stop_words = set(stopwords.words('english'))
except LookupError:
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

# Load FAQs
with open("faqs.json") as f:
    faqs = json.load(f)

questions = [item["question"] for item in faqs]
answers = [item["answer"] for item in faqs]

# Preprocessing function
def preprocess(text):
    tokens = tokenizer.tokenize(text.lower())
    return ' '.join([word for word in tokens if word not in stop_words and word not in string.punctuation])

processed_questions = [preprocess(q) for q in questions]

# TF-IDF vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(processed_questions)

# Chatbot function
def get_answer(user_input):
    user_input_processed = preprocess(user_input)
    user_vec = vectorizer.transform([user_input_processed])
    similarity = cosine_similarity(user_vec, X)
    best_match_index = similarity.argmax()
    best_score = similarity[0, best_match_index]

    if best_score > 0.3:
        return answers[best_match_index]
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

# Streamlit UI
st.title("📚 FAQ Chatbot")
st.write("Ask me a question related to the product or services!")

user_question = st.text_input("You:", "")

if user_question:
    response = get_answer(user_question)
    st.markdown(f"*Bot:* {response}")

