#!/bin/bash
#sends a request to a URL and displays the status code of the response
curl -s -w "%{http_code}" "$1"
