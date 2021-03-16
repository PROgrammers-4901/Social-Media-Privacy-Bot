import pickle
from sklearn import linear_model, preprocessing
from sklearn.feature_extraction.text import CountVectorizer
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
import json

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)
sheet = client.open("tweet_data").worksheets()[2] # Open the spreadhseet

train_text = sheet.col_values(4)
train_labels = sheet.col_values(2)
print(len(train_text))
sheet = client.open("tweet_data").sheet1 # Open the spreadhseet

train_text_2 = sheet.col_values(4)
train_labels_2 = sheet.col_values(2)
spam_count = len(train_text)
train_text += random.choices(train_text_2, k=spam_count)
train_labels += train_labels_2[:spam_count]


sheet = client.open("tweet_data").worksheets()[1] # Open the spreadhseet
test_text = sheet.col_values(4)
test_labels = sheet.col_values(2)

pickle_off = open("LR_Count_Vectors.sav","rb")
model = pickle.load(pickle_off)
print(type(model))
tweet =  ["You might think your practical approach to financial matters i... More for Virgo https://t.co/tKRGDUpf1V"]
encoder = preprocessing.LabelEncoder()
valid_tweet = encoder.fit_transform(tweet)
# valid_tweet = encoder.transform(valid_tweet)
print(valid_tweet)
print(model.predict(X=[1,valid_tweet]))