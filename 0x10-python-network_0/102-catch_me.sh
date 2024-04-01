#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response
curl -s -X POST -o /dev/null -w "%{http_code}" 0.0.0.0:5000/catch_me
