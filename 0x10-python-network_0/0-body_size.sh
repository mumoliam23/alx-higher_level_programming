#!/bin/bash
#Use a URL, send a request to the url and get the response size
curl -sI "$url" | grep "Content-Length" | awk '{print $2}'


