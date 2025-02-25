#!/usr/bin/python3
import requests


def recurse(subreddit, hot_list=[], after=None):
        """
        Recursively queries the Reddit API and returns a list of titles
        of all hot articles for a given subreddit.

        Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): Accumulator for the titles of hot articles.
        after (str): The "after" parameter for pagination (defaults to None).

        Returns:
            list: List of titles of hot articles, or None if the subreddit is invalid.
"""
url = f"https://www.reddit.com/r/{subreddit}/hot.json"
headers = {"User-Agent": "custom-user-agent"}
params = {"after": after, "limit": 100}  # Limit 100 items per request

try:
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)                                                 if response.status_code == 200:                                      data = response.json()
       posts = data.get("data", {}).get("children", [])                  after = data.get("data", {}).get("after", None)                                                                                     for post in posts:
           hot_list.append(post.get("data", {}).get("title", ""))                                                                          if after is not None:
        # Recursive call to fetch the next page
           return recurse(subreddit, hot_list, after)
       else:
            return hot_list
   else:
       return None
except Exception:
    return None
