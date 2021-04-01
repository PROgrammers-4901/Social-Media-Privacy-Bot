from preprocess import *
from IPython.display import display
import pandas as pd
import numpy as np
import sklearn
from sklearn import model_selection, preprocessing, linear_model, naive_bayes, metrics, svm
from sklearn.utils import class_weight
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from keras.preprocessing.text import text_to_word_sequence
import pickle

def stopwords(temp,stop_word):
    x_new = text_to_word_sequence(temp)    # tokenize text 
    clean = []
    for i in x_new:
        if i not in stop_word:
            clean.append(i)
    return " ".join(clean)

def seperate_lists(temp_list):

    return [temp[0] for temp in temp_list],[temp[1] for temp in temp_list],[temp[2] for temp in temp_list]

def main():

    stop_word = np.loadtxt("AI_Model_Resources\stopwords", dtype=str)
    
    train_data,train_labels,test_data,test_labels = preprocess()
    
    train_text, train_links,train_emojis = seperate_lists(train_data)
    test_text,test_links,test_emojis = seperate_lists(test_data)

    dframe = pd.DataFrame(data=[train_text,train_links,train_emojis,train_labels], index=["text","links","emojis","label"]).T
    dframe = dframe.append(pd.DataFrame(data=[test_text,test_links,test_emojis,test_labels], index=["text","links","emojis","label"]).T)
    
    dframe.loc[:,"text_stop"] = dframe.loc[:,"text"].apply(lambda x : stopwords(x, stop_word))

    if dframe["text_stop"].isnull().sum()>0:
        print("Empty text")
        dframe.dropna(subset=["text_w"], inplace=True)

    print(dframe.shape)
    
    # dframe.to_csv('dataframe_stopwords.csv')
    # print("counts after:")
    # print(dframe["label"].value_counts())

    #ML classic
    tr_x_sw, val_x_sw, y_tr_sw, y_val_sw = model_selection.train_test_split(dframe["text_stop"], dframe["label"], random_state=42, stratify=dframe["label"].values, test_size=0.2)

    # For Embeddings
    tr_x, val_x, y_tr, y_val = model_selection.train_test_split(dframe["text"], dframe["label"], random_state=42, stratify=dframe["label"], test_size=0.2)

    encoder = preprocessing.LabelEncoder()
    tr_y_sw = encoder.fit_transform(y_tr_sw)
    val_y_sw = encoder.transform(y_val_sw)
    tr_y = encoder.transform(y_tr)
    val_y = encoder.transform(y_val)
    
    # Compute the class weight with sklearn 
    class_weights = class_weight.compute_class_weight('balanced',np.unique(y_tr),y_tr)

    print(*[f'Class weight: {round(i[0],4)}\tclass: {i[1]}' for i in zip(class_weights, np.unique(y_tr))], sep='\n')

    labels = dframe["label"].unique()
    test=pd.DataFrame(data=np.transpose([labels,encoder.transform(labels)]), columns=["labels", "encoding"]).sort_values(by=["encoding"])
    labels=test.labels.tolist()
    if any([0,1]) in labels and len(labels)==2:
        labels[labels.index(0)] = "ham"
        labels[labels.index(1)] = "spam"

    df_results = pd.DataFrame()

    count_vect = CountVectorizer(analyzer='word', token_pattern=r'\w{1,}')
    count_vect.fit(dframe["text"]+"_stop")

    # transform the training and validation data using count vectorizer object
    xtrain_count =  count_vect.transform(tr_x_sw)
    xvalid_count =  count_vect.transform(val_x_sw)

    pickle.dump(count_vect, open(os.path.join("","AI_Model_Resources\models","count_vect_model.sav"), 'wb'))

if __name__ == "__main__":
    main()