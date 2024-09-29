# Hate Speech Detection

Hate speech is understood as any verbal, written, or behavioral communication that uses derogatory or discriminatory language or attacks against a person or group, especially based on religion, ethnicity, nationality, race, color, ancestry, gender, or any other identity factor.

In this project, I built a hate speech detection model using Machine Learning techniques with Python. The model analyzes text data to identify whether a given statement contains hate speech.

## Project Overview

The main goal of this project is to build a machine learning model that can automatically detect hate speech in text. This was achieved using a pipeline that processes the text data, cleans it, and then classifies it using a Stochastic Gradient Descent (SGD) classifier.

### Model Pipeline

1. **Text Cleaning**: Removal of special characters, URLs, mentions, and converting text to lowercase.
2. **Vectorization**: Using `CountVectorizer` to transform text into a numerical format.
3. **TF-IDF Transformation**: Applying TF-IDF (Term Frequency-Inverse Document Frequency) to weigh the importance of words.
4. **Classification**: Using an SGD classifier for detecting hate speech.

## Usage

You can try the model directly in your browser through the Hugging Face Space:

[![Hate Speech Detection](https://img.shields.io/badge/🤗-Hugging%20Face%20Space-orange)](https://huggingface.co/spaces/zafermbilen/hate-speech-detection)

## Dataset

The dataset used to train the model can be found [here](https://github.com/amankharwal/Website-data/blob/master/hate%20speech.rar). It contains labeled examples of text, where each text is classified as hate speech or not.

