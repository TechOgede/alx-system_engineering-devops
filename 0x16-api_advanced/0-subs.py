#!/usr/bin/python3
''' This module defines a function that returns the number of subscribers
on a subreddit
'''


def number_of_subscribers(subbreddit):
    ''' Returns the number of subs on a subreddit '''
    import requests

    url = f'https://reddit.com/r/{subbreddit}/about.json'
    headers = {"User-Agent": "Alx/1.0"}

    res = requests.get(url, headers=headers)
    data = res.json()

    if 'error' in data:
        return 0

    return data['data']['subscribers']
