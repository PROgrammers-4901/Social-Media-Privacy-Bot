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
    tfid_path = "pickle_dumps/tfid.pickle"
    svm_path = "pickle_dumps/svm.pickle"
    naive_path = "pickle_dumps/naive.pickle"

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

    response = {}

    if len(tweet_object) > 1:
        sums = 0
        temp = 0
        x = 0
        for item in range(0, len(tweet_object)):
            sums += int(predictions_NB[item])
            if x < probability[item][1]:
                x = probability[item][1]
                temp = tweet_object[item][0]
        spam_percentage = sums/len(tweet_object)

        response.update({
            'percentage': spam_percentage,
            'tweet_text': temp,
            'tweet_probability': x
        })

    
    else:
        for item in range(0, len(tweet_object)):
            tweet_text = tweet_object[item][0]
            prediction = predictions_SVM[item]
            tweet_probability = probability[item][prediction]
            response.update({item: {
                'tweet': tweet_text,
                'prediction': prediction,
                'probability': tweet_probability
            }})

    
    return json.dumps(response)



input_stuff = [["RT @odinodin: I just made a tool for inspecting data in a Reagent app as a tree structure, data-frisk.  https://t.co/wWQz9YInP3"],[r"Although you're fully capable of understanding both sides of a... More for Libra https://t.co/l0Toev12wH"],["WDW Canine Extravaganza 2016, Woodford Working Men's Club, WOODFORD Schedule – Sunday 29th… https://t.co/cyJII1qIzY https://t.co/REhua2Jxcg"]]

print(predict_text(input_stuff))