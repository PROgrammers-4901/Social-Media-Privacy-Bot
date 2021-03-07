import json
from flask import Flask
from flask_cors import CORS
from get_tweet import getTweet, getUser, getHashtag

app = Flask(__name__)
CORS(app)

@app.route('/tweet_id/<id>', methods=['GET'])
def tweet_by_id(id):
    return getTweet(id).text

@app.route('/username/<username>', methods=['GET'])
def tweet_by_user(username):
    return getUser(username).text

@app.route('/hashtag/<tag>', methods=['GET'])
def tweet_by_hashtag(tag):
    return json.dumps(getHashtag(tag),indent=4)