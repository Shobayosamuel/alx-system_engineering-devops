#!/usr/bin/python3
"""
    Using what I did in the task #0,
    extend your Python script to export data in the JSON format.
"""

import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = "{}/{}".format(base_url, employee_id)
    response = requests.get(url)
    employee_name = response.json().get('username')

    todos_url = "{}/todos".format(url)
    response = requests.get(todos_url)
    tasks = response.json()
    done_tasks_no = 0

    user_tasks = []
    for task in tasks:
        task_info = {
                "tasks": task.get('title'),
                "completed": task.get('completed'),
                "username": employee_name
                }
        user_tasks.append(task_info)

    user_tasks_json = {employee_id: user_tasks}
    with open('{}.json'.format(employee_id), 'w') as f:
        json.dump(user_tasks_json, f)
