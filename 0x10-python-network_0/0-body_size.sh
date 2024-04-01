#!/bin/bash
read url
content_length=$(curl -sI "$url" | grep -i content-length | awk '{print $2}')
echo "$content_length"

