#!/bin/bash
# send a GET request to an URL with curl, and display the body of the response
curl -s -i "url" | grep HTTP/1.1\ 200
