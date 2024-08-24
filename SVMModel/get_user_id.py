from requests_oauthlib import OAuth1Session

def get_user_id(consumer_key, consumer_secret, access_token, access_token_secret, params):
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    response = oauth.get(
        "https://api.twitter.com/2/users/by", params=params
    )

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    json_response = response.json()
    data = json_response.get('data', [])
    user_ids = [entry['id'] for entry in data]

    return user_ids
