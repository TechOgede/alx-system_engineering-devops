#!/usr/bin/python3
''' This scirpt fetches data from the api, jsonplaceholder.typicode.com '''


def main():
    ''' Driver function '''
    import requests
    import sys

    emp_id = sys.argv[1]
    url = f'https://jsonplaceholder.typicode.com/'

    user = f'{url}users/{emp_id}'
    res = requests.get(user)
    res = res.json()
    emp_name = res.get('name')

    todos = f'{url}todos?userId={emp_id}'
    tasks = requests.get(todos)
    tasks = tasks.json()
    total_tasks = len(tasks)
    compl_tasks = 0

    str_ = ""
    for task in tasks:
        if task.get('completed'):
            compl_tasks += 1
            str_ += f'\t{task.get("title")}\n'
    str_ = str_.rstrip()

    print('Employee {} is done with tasks({}/{}):'
          .format(emp_name, compl_tasks, total_tasks))

    print(str_)


if __name__ == '__main__':
    main()
