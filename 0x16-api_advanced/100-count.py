#!/usr/bin/python3
'''Run the function count_words'''
import requests


def count_words(subreddit, word_list, count_dict=None):
    """
    Recursive function that queries the Reddit API and counts the number of
    occurrences of each word in a given list in the titles of all hot articles
    in the given subreddit.

    subreddit: str, name of subreddit to search
    word_list: list of str, words to search for in article titles
    count_dict: dict, dictionary to store the counts of each word

    Returns a sorted list of tuples, where each tuple contains a word and its
    count, sorted by count (descending) and then by word (ascending).
    """
    if count_dict is None:
        count_dict = {}

    url = 'https://www.reddit.com/r/{}/hot.json?limit=100'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return []

    titles = [post['data']['title'].lower() for post in response
              .json()['data']['children']]

    for word in word_list:
        if not word.isalpha():
            continue

        count = sum(1 for title in titles if title.count(word.lower()) > 0)

        if count > 0:
            if word.lower() in count_dict:
                count_dict[word.lower()] += count
            else:
                count_dict[word.lower()] = count

    next_page = response.json()['data']['after']
    if next_page is not None:
        count_words(subreddit, word_list, count_dict)

    return sorted([(word, count_dict[word]) for word in count_dict],
                  key=lambda x: (-x[1], x[0]))
