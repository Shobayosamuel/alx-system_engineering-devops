#!/usr/bin/python3
"""
    Using what I did in the task #0,
    extend your Python script to export data in the JSON format.
"""

import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)
    users = response.json()

    dictionary = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
                user_id)
        response = requests.get(url)
        tasks = response.json()
        dictionary[user_id] = []
        for task in tasks:
            dictionary[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            })
    with open("{}.json".format(user_id), 'w') as file:
        json.dump(dictionary, file)
