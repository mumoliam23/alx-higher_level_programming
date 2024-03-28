#!/bin/bash
# send a GET request to an URL with curl, and display the body of the response
curl -sX GET $1 -L
