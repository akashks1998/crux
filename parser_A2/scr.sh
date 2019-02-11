#!/bin/bash

while true
do
    ot=$(xclip -o)
    if [[ "$prev" !=  "$ot"  ]];
    then
        xclip -o > grammer.txt; python3 grammer.py
    fi
    prev=$ot
    sleep 5
done
