#!/bin/bash
# send a GET request to an URL with curl, and display the body of the response
curl -s -i "url" | grep -q 200 && curl -s "$1"
