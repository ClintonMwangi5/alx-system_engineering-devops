#!/usr/bin/python3
"""
1-main
"""
import sys
from 1-top_ten import top_ten

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
