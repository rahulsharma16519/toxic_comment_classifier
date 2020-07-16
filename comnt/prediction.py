import numpy as np
import pandas as pd
import pickle
import os
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

def comment_prediction(inp_str):
    path_str = os.getcwd()
    cv = pickle.load(open(os.path.join(path_str, 'count_vectorizer_words.pckl'), 'rb'))
    classifier = pickle.load(open(os.path.join(path_str, 'comment_filtering_LR.pckl'), 'rb'))
    corpus = []
    review = re.sub('[^a-zA-Z]', ' ', inp_str)
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    all_stopwords = stopwords.words('english')
    review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
    review = ' '.join(review)
    corpus.append(review)
    X = cv.transform(corpus).toarray()
    y_pred = classifier.predict(X)
    if y_pred == 1:
        return 'Toxic'
    else:
        return 'Non-Toxic'
