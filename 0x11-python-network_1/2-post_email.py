#!/usr/bin/python3
"""sends a POST request with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
import urllib.request
from sys import argv
if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': argv[2]})
    data = data.encode('ascii')
    request = urllib.request.Request(argv[1], data)

    with urllib.request.urlopen(request) as response:
        email = response.read()
    print(email.decode('utf-8'))
