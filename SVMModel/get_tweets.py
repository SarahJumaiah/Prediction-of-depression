# twitter_functions.py

import requests

bearer_token = "AAAAAAAAAAAAAAAAAAAAADritgEAAAAAI6cKZuokf%2FnTcN6wynvkfn7uFlM%3DlVvXE4gKQ2DQSpiwru4AYPe9nqrSxWEYIFQYRg8PHuZIt0dr2L"

def create_url(user_id):
    return "https://api.twitter.com/2/users/{}/tweets".format(user_id)

def get_params():
    return {"tweet.fields": "created_at", "max_results": 20}

def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserTweetsPython"
    return r

def get_user_tweets(user_id):
    url = create_url(user_id)
    params = get_params()
    response = requests.request("GET", url, auth=bearer_oauth, params=params)
    
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    
    json_response = response.json()
    tweet_texts = [entry['text'] for entry in json_response.get('data', [])]
    
    return tweet_texts
