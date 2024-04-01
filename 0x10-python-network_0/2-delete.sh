#!/bin/bash
# Sends a delete request to first-command line arg and displays the body of the response
url=$1; curl -sX DELETE "$1"
