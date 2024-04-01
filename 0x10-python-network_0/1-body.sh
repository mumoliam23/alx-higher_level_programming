#!/bin/bash
# send a GET request to an URL with curl, and display the body of the response
url=$1; curl -s -w "%{http_code}" "url" | grep -q 200 && curl -s "url"
