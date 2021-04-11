import requests
import os
import json

def getTweet(tweet_id):
    BEARER_TOKEN = r"AAAAAAAAAAAAAAAAAAAAEBCMgEAAAAA4mf%2FWbcvmcj7Mz3%2F66YsqZ7uAeA%3D1mhrSzcclXYcpmdKvPhrMqHKH4kk2uiSVv4Jci3fQQ30tSRgpf"

    headers = {
        'Authorization': f"Bearer {BEARER_TOKEN}",
    }
    
    raw = requests.get(f'https://api.twitter.com/2/tweets/{tweet_id}', headers=headers).text

    j_text = json.loads(raw)

    if not 'data' in j_text:
        return

    tweet = [j_text['data']['text']]
    return [tweet]

def getUser(username):
    username = username.strip('@ ')
    BEARER_TOKEN = os.environ.get('BEARER_TOKEN')

    headers = {
        'Authorization': f"Bearer {BEARER_TOKEN}",
    }
    
    user_data = requests.get(f'https://api.twitter.com/2/users/by/username/{username}', headers=headers)

    user_data = json.loads(user_data.text)
    if 'data' not in user_data:
        return None
    user_id = user_data['data']['id']

    params = {
        "max_results": 100
    }
    x = json.loads(requests.get(f'https://api.twitter.com/2/users/{user_id}/tweets', params=params, headers=headers).text)
    if 'data' not in x:
        return None
    tweets = []
    for item in x['data']:
        tweets.append([item['text']])
    
    return tweets

def getHashtag(tag):
    username = username.strip('#@ ')
    BEARER_TOKEN = os.environ.get('BEARER_TOKEN')
    tweets = []
    headers = {
        'Authorization': f"Bearer {BEARER_TOKEN}",
    }
    
    params = {
        'query': f"#{tag}",
        'max_results': 100
    }
    
    x = requests.get(f'https://api.twitter.com/2/tweets/search/recent', params=params, headers=headers)
    x = json.loads(x.text)
    if 'data' not in x:
        return None
    for item in x['data']:
        tweets.append([item['text']])
    if 'meta' in x:
        if 'next_token' in x['meta']:
            next_token = x['meta']['next_token']
        else:
            truthy = False
    else:
        truthy = False 
    while (truthy):
        if (len(tweets) > 4):
            truthy = False
        params.update({'next_token': next_token})
        x = requests.get(f'https://api.twitter.com/2/tweets/search/recent', params=params, headers=headers)
        x = json.loads(x.text)
        for item in x['data']:
            tweets.append([item['text']])
        if 'meta' in x:
            if 'next_token' in x['meta']:
                next_token = x['meta']['next_token']
            else:
                truthy = False
        else:
            truthy = False
    
    
    return tweets
