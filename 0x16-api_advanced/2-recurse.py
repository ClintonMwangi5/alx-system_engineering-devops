#!/usr/bin/python3
"""
2-recurse
"""
import requests

def recurse(subreddit, hot_list=[]):
    """Recursively retrieves the titles of all hot articles for a given subreddit."""
   url = f'https://www.reddit.com/r/{subreddit}/hot.json'
   headers = {'User -Agent': 'Mozilla/5.0'}
   params = {'after': hot_list[-1] if hot_list else None}
                        response = requests.get(url, headers=headers, params=params)

   # Check if the subreddit is valid
   if response.status_code != 200:
       return None

   # Parse the JSON response
   data = response.json()
   posts = data.get('data', {}).get('children', [])

   # If no posts are found, return the current hot_list
   if not posts:
       return hot_list

   # Add the titles of the current posts to hot_list
   for post in posts:
       hot_list.append(post['data']['title'])

   # Check for pagination and recurse if there are more posts
   after = data.get('data', {}).get('after')
   if after:
      return recurse(subreddit, hot_list)

return hot_list
