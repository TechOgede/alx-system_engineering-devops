#!/usr/bin/python3
''' This module defines a function that
employs recursion to returns a list of the top ten titles
for the hot posts listed for a given subreddit
'''


def recurse(subreddit, hot_list=[], after=None):
    ''' Return list of titles of all hot articles oon a subreddit '''
    import requests

    REDDIT = 'https://www.reddit.com'
    url = f'{REDDIT}/r/{subreddit}/hot.json'

    if after:
        url = f'{REDDIT}/r/{subreddit}/hot.json?after={after}'

    headers = {"User-Agent": "Alx/1.0"}
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code != 200:
        return None
        
    data = res.json()
    
    for post in data.get('data').get('children'):
        hot_list.append(post.get('data').get('title'))

    next_page_marker = data.get('data').get('after')

    if not next_page_marker:
        return hot_list

    return recurse(subreddit, hot_list, next_page_marker)
