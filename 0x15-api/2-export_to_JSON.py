#!/usr/bin/python3
''' This script gets info about employees and exports it to as a JSON'''


def main():
    ''' Driver function '''
    import json
    import requests
    import sys

    url = 'https://jsonplaceholder.typicode.com/'
    emp_id = sys.argv[1]

    user = requests.get(f'{url}users/{emp_id}')
    emp_name = user.json().get('username')

    todos = requests.get(f'{url}todos?userId={emp_id}')
    tasks = todos.json()

    data = {}
    tasks_list = []
    for task in tasks:
        tasks_dict = {}
        tasks_dict['username'] = emp_name
        tasks_dict['completed'] = task.get('completed')
        tasks_dict['task'] = task.get('title')
        tasks_list.append(tasks_dict)

    data[f'{emp_id}'] = tasks_list

    file_path = f'{emp_id}.json'

    with open(file_path, 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    main()
