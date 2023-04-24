#!/usr/bin/python3
"""
    Using what I did in the task #0,
    extend your Python script to export data in the CSV format.
"""

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

    with open('{}.csv'.format(employee_id), 'w') as fil:
        for task in tasks:
            fil.write('"{}","{}","{}","{}"\n'
                      .format(employee_id, employee_name,
                              task.get('completed'), task.get('title')))
