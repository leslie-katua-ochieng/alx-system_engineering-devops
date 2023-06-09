#!/usr/bin/python3
""" defines advanced api usage """
import requests


def top_ten(subreddit):
    """ queries the Reddit API and prints titles of
    the first 10 hot posts listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16-advanced_api (by /Ade)"
    }
    params = {"limit": 10}
    subredit_resp = requests.get(url,
                                 allow_redirects=False,
                                 headers=headers,
                                 params=params).json().get("data")
    if subredit_resp:
        childrens = subredit_resp.get("children")
        [print(children.get('data').get('title')) for children in childrens]
    else:
        print(None)
