#!/bin/bash

if [ -z "$1" ] || [ -z "$2" ]; then
 echo "Usage: $0 <url> <filename>"
 exit 1
fi

url=$1
filename=$2

if [ ! -f "$filename" ]; then
 echo "File not found: $filename"
 exit 1
fi

response=$(curl -s -X POST -H "Content-Type: application/json" --data @"$filename" "$url")

echo $response
