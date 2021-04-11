from preprocess_flask import *
import pickle
import pandas as pd
import sklearn
from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer


#Loads pickle matrices/models and uses the inputted tweet object [[text],[text]..] to be predicted
#Returns 
def predict_text(tweet_object):
    tfid_path = "pickle_dumps/tfid.pickle"
    svm_path = "pickle_dumps/svm.pickle"

    tf_convert = pickle.load(open(tfid_path,'rb'))
    svm_model = pickle.load(open(svm_path,'rb'))
    tweet_clean = preprocess(tweet_object)

    tweet_df = pd.DataFrame(tweet_clean,columns=['text'])
    print(tweet_df)
    input_tf = tf_convert.transform(tweet_df['text'])
    predictions_SVM = svm_model.predict(input_tf)# Use accuracy_score function to get the accuracy
    
    print("Prediction:",predictions_SVM)
    print("Distance from Hyperplane",svm_model.decision_function(input_tf))

input_stuff = [["RT @odinodin: I just made a tool for inspecting data in a Reagent app as a tree structure, data-frisk.  https://t.co/wWQz9YInP3"],[r"Although you're fully capable of understanding both sides of a... More for Libra https://t.co/l0Toev12wH"],["WDW Canine Extravaganza 2016, Woodford Working Men's Club, WOODFORD Schedule – Sunday 29th… https://t.co/cyJII1qIzY https://t.co/REhua2Jxcg"]]

predict_text(input_stuff)