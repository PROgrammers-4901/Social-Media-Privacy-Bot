import requests
import os
import json

def getTweet(tweet_id):
    BEARER_TOKEN = os.environ.get('BEARER_TOKEN')

    headers = {
        'Authorization': f"Bearer {BEARER_TOKEN}",
    }
    
    return requests.get(f'https://api.twitter.com/2/tweets/{tweet_id}', headers=headers)


def getUser(username):
    BEARER_TOKEN = os.environ.get('BEARER_TOKEN')

    headers = {
        'Authorization': f"Bearer {BEARER_TOKEN}",
    }
    
    user_data = requests.get(f'https://api.twitter.com/2/users/by/username/{username}', headers=headers)

    user_data = json.loads(user_data.text)
    user_id = user_data['data']['id']

    params = {
        "max_results": 100
    }

    return requests.get(f'https://api.twitter.com/2/users/{user_id}/tweets', params=params, headers=headers)

def getHashtag(tag):
    BEARER_TOKEN = os.environ.get('BEARER_TOKEN')
    tweets = []
    truthy = True
    headers = {
        'Authorization': f"Bearer {BEARER_TOKEN}",
    }
    
    params = {
        'query': f"#{tag}",
        'max_results': 100
    }
    
    return requests.get(f'https://api.twitter.com/2/tweets/search/recent', params=params, headers=headers)
