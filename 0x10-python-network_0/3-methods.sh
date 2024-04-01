#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept
url=$1; curl -s -i -X OPTIONS "$1"
