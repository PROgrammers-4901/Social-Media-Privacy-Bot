from preprocess import *
from IPython.display import display
import pandas as pd
import numpy as np
from keras.preprocessing.text import text_to_word_sequence

def stopwords(temp,stop_word):
    x_new = text_to_word_sequence(temp)    # tokenize text 
    clean = []
    for i in x_new:
        if i not in stop_word:
            clean.append(i)
    return " ".join(clean)

def main():

    stop_word = np.loadtxt("AI_Model_Resources\stopwords", dtype=str)
    train_data,train_labels,test_data,test_labels = preprocess()
    
    train_text = [temp[0] for temp in train_data]
    train_links = [temp[1] for temp in train_data]
    train_emojis = [temp[2] for temp in train_data]

    test_text = [temp[0] for temp in test_data]
    test_links = [temp[1] for temp in test_data]
    test_emojis = [temp[2] for temp in test_data]

    dframe = pd.DataFrame(data=[train_text,train_links,train_emojis,train_labels], index=["text","links","emojis","label"]).T
    dframe = dframe.append(pd.DataFrame(data=[test_text,test_links,test_emojis,test_labels], index=["text","links","emojis","label"]).T)

    dframe.loc[:,"text_stop"] = dframe.loc[:,"text"].apply(lambda x : stopwords(x, stop_word))

    if dframe["text_stop"].isnull().sum()>0:
        print("Empty text")
        dframe.dropna(subset=["text_w"], inplace=True)
    
    pd.set_option('display.max_columns', 30)

    print(dframe.shape)
    dframe.to_csv('dataframe w/o stopwords.csv')


if __name__ == "__main__":
    main()