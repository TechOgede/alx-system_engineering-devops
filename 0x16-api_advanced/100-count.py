#!/usr/bin/python3
''' This module defines a function that
employs recursion to count the number of times
a keyword appears in titles of hot articles for a given subreddit
'''


def count_words(subbreddit, word_list, counts={}, after=None):
    ''' Return list of titles of all hot articles oon a subreddit '''
    import requests

    REDDIT = 'https://www.reddit.com'
    url = f'{REDDIT}/r/{subbreddit}/hot.json'

    if after:
        url = url + f'?after={after}'

    headers = {"User-Agent": "Alx/1.0"}
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code != 200:
        return

    data = res.json()

    for post in data.get('data').get('children'):
        title = post.get('data').get('title').lower().split()
        for word in word_list:
            word = word.lower()
            if word in title:
                if counts.get(word):
                    counts[word] += 1
                else:
                    counts[word] = 1

    next_page_marker = data.get('data').get('after')

    if not next_page_marker:
        counts = dict(sorted(counts.items(), key=lambda x: (-x[1], x[0])))
        for key, value in counts.items():
            print(f'{key}: {value}')
        return

    return count_words(subbreddit, word_list, counts, next_page_marker)
