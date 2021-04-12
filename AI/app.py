import json
from predict import *
from flask import Flask
from flask_cors import CORS
from get_tweet import getTweet, getUser, getHashtag

app = Flask(__name__)
CORS(app)

@app.route('/tweet_id/<id>', methods=['GET'])
def tweet_by_id(id):
    get_tweet_text = getTweet(id)
    if get_tweet_text == None:
        return {
            'tweet': "",
            'prediction': -1, 
            'tweet_probability': "" 
        }
    return predict_text(get_tweet_text)

@app.route('/username/<username>', methods=['GET'])
def tweet_by_user(username):
    get_tweet_text = getUser(username)
    if get_tweet_text == None:
        return {
            'tweet': "",
            'prediction': -1, 
            'tweet_probability': "" 
        }
    return predict_text(get_tweet_text)

@app.route('/hashtag/<tag>', methods=['GET'])
def tweet_by_hashtag(tag):
    get_tweet_text = getHashtag(tag)
    if get_tweet_text == None:
        return {
            'tweet': "",
            'prediction': -1, 
            'tweet_probability': "" 
        }
    return predict_text(get_tweet_text)

