#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL
and displays the body of the response.
"""

import requests
from sys import argv
if __name__ == '__main__':

    respp = requests.get(argv[1])
    if respp.status_code >= 400:
        print("Error code: {}".format(respp.status_code))
    else:
        print(respp.text)
