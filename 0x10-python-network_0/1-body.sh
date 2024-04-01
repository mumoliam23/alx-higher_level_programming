#!/bin/bash
# send a GET request to an URL with curl, and display the body of the response
url=$1; curl -sL "$1"
