#!/usr/bin/python3
''' This module defines a function that
employs recursion to returns a list of the top ten titles
for the hot posts listed for a given subreddit
'''


def recurse(subbreddit, hot_list=[], after=None):
    ''' Return list of titles of all hot articles oon a subreddit '''
    import requests

    url = f'https://reddit.com/r/{subbreddit}/hot.json'

    if after:
        url = f'https://reddit.com/r/{subbreddit}/hot.json?after={after}'

    headers = {"User-Agent": "Alx/1.0"}
    res = requests.get(url, allow_redirects=False, headers=headers)
    data = res.json()

    if 'error' in data or not data.get('data').get('children'):
        return None

    for post in data.get('data').get('children'):
        hot_list.append(post.get('data').get('title'))

    next_page_marker = data.get('data').get('after')

    if not next_page_marker:
        return hot_list

    return recurse(subbreddit, hot_list, next_page_marker)
