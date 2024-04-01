#!/bin/bash
# takes in a URL, sends a request to that URL, and displays size of the body of response in bytes
url=$1; curl -s "$url" | wc -c
