# Library imports
import pandas as pd
import numpy as np
import spacy
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
import joblib
import string
from spacy.lang.en.stop_words import STOP_WORDS
from flask import Flask, request, jsonify, render_template
import nltk

# Load trained Pipeline
model = joblib.load('svm_pickle.pkl')

stopwords = list(STOP_WORDS)

# Create the app object
app = Flask(__name__)


# creating a function for data cleaning
from custom_tokenizer_function import CustomTokenizer


# Define predict function
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    new_review = [str(x) for x in request.form.values()]
#     data = pd.DataFrame(new_review)
#     data.columns = ['new_review']

    predictions = model.predict(new_review)[0]
    if predictions==1:
        return render_template('sentimen.html', prediction_text='Positif')
    else:
        return render_template('sentimen.html', prediction_text='Negatif')

# change page from navbar
@app.route('/second-page')
def second():
    return render_template('sentimen.html')

if __name__ == "__main__":
    app.run(debug=True)
