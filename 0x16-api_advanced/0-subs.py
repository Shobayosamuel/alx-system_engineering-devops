#!/usr/bin/python3
import requests
'''Get the number of subscribers from a given subreddit'''


def number_of_subscribers(subreddit):
    '''
        return the number of subscribers from reddit api
    '''
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        body = response.json()
        subscribers = body['data']['subscribers']
        return subscribers
    else:
        return 0
