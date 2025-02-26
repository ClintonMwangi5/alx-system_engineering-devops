#!/usr/bin/python3
"""
1-top_ten
"""
import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User -Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    # Check if the subreddit is valid
    if response.status_code != 200:
        print(None)
        return

    # Parse the JSON response
    data = response.json()
    posts = data.get('data', {}).get('children', [])

    # Print the titles of the first 10 hot posts
                                                                    for post in posts[:10]:
        print(post['data']['title'])
