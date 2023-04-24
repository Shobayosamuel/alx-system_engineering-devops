#!/usr/bin/python3
"""
    Using what I did in the task #0,
    extend your Python script to export data in the JSON format.
"""

import requests
import json


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(base_url)
    users = response.json()

    all_tasks = {}
    for user in users:
        employee_id = user.get('id')
        employee_name = user.get('name')
        todos_url = "{}/{}/todos".format(base_url, employee_id)
        response = requests.get(todos_url)
        tasks = response.json()
        task_list = []
        for task in tasks:
            task_list.append({"username": employee_name,
                              "task": task.get('title'),
                              "completed": task.get('completed')})
        all_tasks[employee_id] = task_list

    with open('todo_all_employees.json', 'w') as f:
        json.dump(all_tasks, f)
