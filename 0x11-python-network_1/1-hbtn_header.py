#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable
"""

import urllib.request
if __name__ == '__main__':
    from sys import argv
    with urllib.request.urlopen(argv[1]) as response:
        request_id = response.getheader("X-Request-Id")
    print(request_id)
