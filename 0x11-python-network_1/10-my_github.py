#!/usr/bin/python3
"""
10-my_github module
Usage: ./10-my_github.py <username> <password>
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    """
    Takes your Github credentials username and password and uses
    the GitHub API to display your id
    """

    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
