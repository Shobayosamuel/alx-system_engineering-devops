#!/usr/bin/python3
"""
Contains the top_ten function
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
        recursive function that queries the Reddit API and returns a list
        containing the titles of all hot articles for a given subreddit
    """
    if subreddit is None or not isinstance(subreddit, str):
        return None
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': '0x16-api_advanced:project:v1.0.0'}
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json()['data']
    posts = data['children']
    after = data['after']
    for post in posts:
        hot_list.append(post['data']['title'])
    if after:
        recurse(subreddit, hot_list, after)
    return hot_list
