from preprocess_flask import *
import pickle
import json
import pandas as pd
import sklearn
from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer


#Loads pickle matrices/models and uses the inputted tweet object [[text],[text]..] to be predicted
#Returns 
def predict_text(tweet_object):
    tfid_path = "AI\\pickle_dumps\\tfid.pickle"
    svm_path = "AI\\pickle_dumps\\svm.pickle"
    naive_path = "AI\\pickle_dumps\\naive.pickle"

    tf_convert = pickle.load(open(tfid_path,'rb'))
    svm_model = pickle.load(open(svm_path,'rb'))
    naive_model = pickle.load(open(naive_path,'rb'))
    
    tweet_clean = preprocess(tweet_object)

    tweet_df = pd.DataFrame(tweet_clean,columns=['text'])
    print(tweet_df)
    input_tf = tf_convert.transform(tweet_df['text'])
    predictions_SVM = svm_model.predict(input_tf)
    predictions_NB = naive_model.predict(input_tf)

    print("Prediction NB:",predictions_NB)
    probability = naive_model.predict_proba(input_tf)

    json_send = {
        'tweets': tweet_object,
        'predictions': predictions_NB,
        'probability': probability
    }

    return json.dumps(json_send)



input_stuff = [["RT @odinodin: I just made a tool for inspecting data in a Reagent app as a tree structure, data-frisk.  https://t.co/wWQz9YInP3"],[r"Although you're fully capable of understanding both sides of a... More for Libra https://t.co/l0Toev12wH"],["WDW Canine Extravaganza 2016, Woodford Working Men's Club, WOODFORD Schedule – Sunday 29th… https://t.co/cyJII1qIzY https://t.co/REhua2Jxcg"]]

predict_text(input_stuff)