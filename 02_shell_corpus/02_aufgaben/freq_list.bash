#!/bin/bash

if [[ $# != 1 ]]; then
    echo "Usage $0 FILE" && exit 1
fi

cat $1 | tr -d "[:punct:]"  | tr -s " " "\n" | sort -f | uniq -ic | sort -nr #> freq.txt 
