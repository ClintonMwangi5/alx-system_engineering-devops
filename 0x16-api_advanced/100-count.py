#!/usr/bin/python3
"""
100-count
"""
import requests
from collections import defaultdict
import re

def count_words(subreddit, word_list, word_count=None, after=None):
    """Recursively counts occurrences of keywords in hot articles of a subreddit."""
    if word_count is None:
       word_count = defaultdict(int)

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User -Agent': 'Mozilla/5.0'}
    params = {'after': after}
    response = requests.get(url, headers=headers, params=params)

    # Check if the subreddit is valid
    if response.status_code != 200:
        return

    # Parse the JSON response
    data = response.json()
    posts = data.get('data', {}).get('children', [])

    # If no posts are found, return
    if not posts:
        return

    # Process each post
    for post in posts:
        title = post['data']['title'].lower()
        for word in word_list:
            # Use regex to find whole words only
            count = len(re.findall(r'\b' + re.escape(word.lower()) + r'\b', title))
            word_count[word.lower()] += count

    # Check for pagination and recurse if there are more posts
    after = data.get('data', {}).get('after')
    if after:
        return count_words(subreddit, word_list, word_count, after)

    # Print the results in the required format
    sorted_counts = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        if count > 0:
            print(f"{word}: {count}")

