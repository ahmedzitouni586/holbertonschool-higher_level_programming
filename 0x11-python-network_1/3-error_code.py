#!/usr/bin/python3
""" sends a request to the URL and displays the body of the response
(decoded in utf-8).
"""
import urllib.request
from sys import argv
if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
