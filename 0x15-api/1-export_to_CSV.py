#!/usr/bin/python3
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = f"{base_url}/{employee_id}"
    response = requests.get(url)
    employee_name = response.json().get('name')

    todos_url = f"{url}/todos"
    response = requests.get(todos_url)
    tasks = response.json()
    done_tasks_no = 0
    done_tasks = []
