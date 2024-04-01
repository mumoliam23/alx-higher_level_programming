#!/bin/bash
# takes in a URL, sends a POST request and displays body of the response
url=$1; curl -s -d 'email=test@gmail.com&subject=I will always be here for PLD' "$1"
