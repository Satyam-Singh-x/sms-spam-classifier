import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []

    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)
tfidf=pickle.load(open('vectorizer.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))
import streamlit as st

# Custom title using HTML and CSS
import streamlit as st

st.set_page_config(page_title="Spam Classifier", layout="centered")

st.markdown("""
    <style>
    body {
        background-color: #ffffff;
    }
    .main {
        background-color: #ffffff;
        padding: 2rem;
    }
    .title {
        text-align: center;
        font-family: 'Georgia', serif;
        font-size: 36px;
        font-weight: bold;
        color: #f5f5dc; /* Beige-white text */
        background-color: #2c3e50; /* Dark blue-grey background for contrast */
        padding: 1rem;
        border-radius: 10px;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    </style>
    <div class="title">Email / SMS Spam Classifier</div>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Spam Classifier", layout="centered")

input_sms=st.text_area('Enter The SMS/Email Here')
# Button with CSS
st.markdown("""
    <style>
    .stTextArea textarea {
        font-size: 16px;
        text-align: center;
    }
    div.stButton > button {
        display: block;
        margin: 20px auto;
        width: 50%;
        background-color: #f5f5dc;
        color: black;
        font-size: 18px;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px;
        border: none;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #e6e6d1;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

if st.button('Predict'):
    # 1. preprocess
    transform_sms = transform_text(input_sms)
    # vectorize
    vector_input = tfidf.transform([transform_sms])

    # predict
    result = model.predict(vector_input)[0]
    # display
    if result == 1:
        st.text('Spam')
    else:
        st.text('Not Spam')



