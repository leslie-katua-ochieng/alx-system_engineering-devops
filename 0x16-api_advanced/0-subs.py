#!/usr/bin/python3
""" defines advanced api usage """
import requests


def number_of_subscribers(subreddit):
    """ queries the Reddit API and returns the
    number of subscribers (not active users, total
    subscribers) for a given subreddit. If an invalid
    subreddit is given, the function returns 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16-advanced_api (by /Ade)"
    }
    subredit_resp = requests.get(url,
                                 allow_redirects=False,
                                 headers=headers).json().get("data")
    if subredit_resp:
        return subredit_resp.get("subscribers")
    return 0
