#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a given letter.

Usage: ./8-json_api.py <letter>
  - The letter is sent as the value of the variable `q`.
  - If no letter is provided, sends `q=""`.
"""
#!/usr/bin/python3
""" search api module """


import requests
from sys import argv

if __name__ == "__main__":
    data = {"q": argv[1] if len(argv) == 2 else ""}
    response = requests.post('http://0.0.0.0:5000/search_user', data=data).json\
()
    try:
        if 'id' in response and 'name' in response:
                print("[{}] {}".format(response['id'], response['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
