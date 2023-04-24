#!/usr/bin/python3
"""
Retrieves and displays information about a given employee's TODO list
progress using the JSONPlaceholder API.
"""

import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = "{}/{}".format(base_url, employee_id)
    response = requests.get(url)
    employee_name = response.json().get('name')

    todos_url = "{}/todos".format(url)
    response = requests.get(todos_url)
    tasks = response.json()
    done_tasks_no = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done_tasks_no += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, done_tasks_no, len(tasks)))

    for line in done_tasks:
        print("\t {}".format(line.get('title')))
