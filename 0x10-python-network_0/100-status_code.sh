#!/bin/bash
#sends a request to a URL and displays the status code of the response
url=$1; curl -s -w'%{response_code}' "$1"
