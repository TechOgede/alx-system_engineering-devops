#!/usr/bin/python3
''' This script gets info about employees and exports it to a CSV'''


def main():
    ''' Driver function '''
    import csv
    import requests
    import sys

    url = 'https://jsonplaceholder.typicode.com/'
    emp_id = sys.argv[1]

    user = requests.get(f'{url}users/{emp_id}')
    emp_name = user.json().get('username')

    todos = requests.get(f'{url}todos?userId={emp_id}')
    tasks = todos.json()

    data = []
    for task in tasks:
        line = []
        line.append(emp_id)
        line.append(emp_name)
        line.append(task.get('completed'))
        line.append(task.get('title'))
        data.append(line)

    file_path = f'{emp_id}.csv'

    with open(file_path, mode='w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(data)


if __name__ == '__main__':
    main()
