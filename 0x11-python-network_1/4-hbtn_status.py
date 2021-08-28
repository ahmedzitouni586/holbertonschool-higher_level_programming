#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""
if __name__ == '__main__':
    import requests
    resp = requests.get('https://intranet.hbtn.io/status')
    url = resp.text
    print("Body response:")
    print('\t- type: {}'.format(type(url)))
    print('\t- content: {}'.format(url))
