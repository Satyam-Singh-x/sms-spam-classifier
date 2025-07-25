📩 Email/SMS Spam Classifier
This is a machine learning web application built using Streamlit that classifies whether a given SMS or email message is Spam or Not Spam (Ham).

🔍 Features
Natural Language Processing with NLTK.

Trained using a Naive Bayes Classifier.

Clean, formal, and user-friendly interface.

Styled with custom Streamlit components for a professional look.

Deployed for easy access and testing.

Live demo link: https://sms-spam-classifier-bysatyam.streamlit.app/

⚙️ Tech Stack

Python 🐍

Pandas & Scikit-learn for model training

NLTK for text preprocessing

Streamlit for web deployment

📦 Dataset
The model is trained on the SMS Spam Collection Dataset from Kaggle.

Dataset link: https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset


📁 Files in this Repository

app.py : Streamlit app for classifying SMS messages as spam or ham

spam.ipynb: Jupyter Notebook containing data cleaning, EDA, text preprocessing, and model building

vectorizer.pkl :	Pickle file for the text vectorization model

model.pkl	: Trained  classification model stored as a pickle file

requirements.txt : List of dependencies for running the project




🚀 How to Run Locally

Clone the repo:

bash
git clone https://github.com/your-username/spam-classifier.git

cd spam-classifier

Install dependencies:

bash
pip install -r requirements.txt

Run the app:

bash
streamlit run app.py

📝 Note
Make sure the following lines are present in your app.py to download NLTK resources:

python

import nltk

nltk.download('punkt')

nltk.download('stopwords')


🙋‍♂️ Author Made with ❤️ by Satyam Singh

📫 singhsatyam.0912@gmail.com — https://www.linkedin.com/in/satyam-singh-61152a334

📄 License This project is licensed under the MIT License
