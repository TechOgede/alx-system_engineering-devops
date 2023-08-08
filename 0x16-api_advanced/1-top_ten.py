#!/usr/bin/python3
''' This module defines a function that prints the top ten titles
for the first 10 hot posts listed for a given  subreddit
'''


def top_ten(subbreddit):
    ''' Prints first 10 top hot posts on a subreddit '''
    import requests

    url = f'https://reddit.com/r/{subbreddit}/hot.json?limit=10'
    headers = {"User-Agent": "Alx/1.0"}

    res = requests.get(url, headers=headers)
    data = res.json()

    if 'error' in data or not data.get('data').get('children'):
        print(None)
        return

    for post in data.get('data').get('children'):
        print(post.get('data').get('title'))
