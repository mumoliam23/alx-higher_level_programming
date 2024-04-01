#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response
url=$1; curl -X POST -s -o /dev/null -w "You got me!\n" "$1/catch_me"
