import streamlit as st
import pandas as pd
import numpy as np
from joblib import load
import re
def clean_text(text):
    text = text.lower()
    text = re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", text)
    return text

pipeline = load('pipeline_model.joblib')

st.title('Hate Speech Detection')
st.write('This is a simple web app to predict whether a tweet contains hate speech or not')

tweet_text = st.text_area('Enter the tweet text')

if st.button('Predict'):
    prediction = pipeline.predict([tweet_text])
    if prediction == 0:
        st.success('The tweet does not contain hate speech')
    else:
        st.error('The tweet contains hate speech')

