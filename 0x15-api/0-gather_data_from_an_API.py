#!/usr/bin/python3
"""
    Python script that, using this REST API, for a given
    employee ID, returns information about his/her TODO
    list progress.
"""
import sys
import requests


if __name__ == "__main__":
    employeeID = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = base_url + '/' + employeeID
    response = requests.get(url)
    employee_name = response.json().get('name')

    todos_url = url + '/todos'
    response = requests.get(todos_url)
    tasks = response.json()
    done_tasks_no = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done_tasks_no += 1
    print(f"Employee {employee_name} is done with tasks"
          f"({done_tasks_no}/{len(tasks)}):")

    for line in done_tasks:
        print("\t {}".format(line.get('title')))
