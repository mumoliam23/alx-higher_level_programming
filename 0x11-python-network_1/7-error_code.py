#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the
body of the response using requests
"""
import requests
from sys import argv

if __name__ == '__main__':
    response = requests.get(argv[1])
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
