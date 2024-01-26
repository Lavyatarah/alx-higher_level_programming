#!/bin/bash

if [ -z "$1" ]; then
 echo "Usage: $0 <url>"
 exit 1
fi

url=$1

response=$(curl -s -H "X-School-User-Id: 98" "$url")

echo $response
