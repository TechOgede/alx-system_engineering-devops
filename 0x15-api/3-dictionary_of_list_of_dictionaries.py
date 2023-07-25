#!/usr/bin/python3
''' This script gets info about employees and exports it to as a JSON'''


def main():
    ''' Driver function '''
    import json
    import requests
    import sys

    url = 'https://jsonplaceholder.typicode.com/'

    users = requests.get(f'{url}users/')
    users_list = users.json()

    data = {}
    for user in users_list:
        todos = requests.get(f'{url}todos?userId={user.get("id")}')
        tasks = todos.json()

        tasks_list = []
        for task in tasks:
            tasks_dict = {}
            tasks_dict['username'] = user.get('username')
            tasks_dict['completed'] = task.get('completed')
            tasks_dict['task'] = task.get('title')
            tasks_list.append(tasks_dict)

        data[f'{user.get("id")}'] = tasks_list

    file_path = 'todo_all_employees.json'

    with open(file_path, 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    main()
