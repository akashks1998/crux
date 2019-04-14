#!/bin/bash

if [[ "$#" != "1" ]];
then
    echo "Give filename args $#"
    exit -1
fi

python3 parser.py  $1  code.crux sym.dump
python3 codegen.py 
gcc m.s -m32 -no-pie -o m.out
./m.out
