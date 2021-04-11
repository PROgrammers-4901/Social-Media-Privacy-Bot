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

# The function to convert returns from above to list of lists format
	# STEPS
		# the list of lists looks like list[[item2, item2]] (i.e., exactly 2 items within each item)
		# parse the text for list of list components, appending a list[i][1] and list[i][2] for each
		# return the list of lists for processing