#!/usr/bin/python3
"""
Contains the top_ten function
"""
import requests


def top_ten(subreddit):
    """returns the title of the topten posts for a given subreddit"""
    if subreddit is None or not isinstance(subreddit, str):
        print('None')
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': '0x16-api_advanced:project:v1.0.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()['data']['children']
        for i in range(10):
            title = data[i]['data']['title']
            print(title)
    else:
        print('None')
