#!/usr/bin/python3
"""Displays the X-Request-Id header variable of a request to a given URL.

Usage: ./1-hbtn_header.py <URL>
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    """takes in a URL, sends a request to the URL and displays
    the value of the X-Request-Id variable found in the header
    of the response"""
    with urllib.request.urlopen(argv[1]) as response:
        html_id = response.info().get('X-Request-Id')
        print(html_id)
