#!/usr/bin/python3
"""
takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
from sys import argv

if __name__ == '__main__':

    url = 'http://0.0.0.0:5000/search_user'

    if len(argv) > 1:
        q = argv[1]
    else:
        q = ''

    r = requests.post(url, data={'q': q})

    try:
        r = r.json()

        if not r:
            print('No result')
        else:
            print('[{}] {}'.format(r.get('id'), r.get('name')))

    except ValueError:
        print('Not a valid JSON')
