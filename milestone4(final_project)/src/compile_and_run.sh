#!/bin/bash

if [[ "$#" != "1" ]];
then
    echo "Give filename args $#"
    exit -1
fi

python3 parser.py  $1  code.crux sym.dump
if [[ "$?" == "0" ]];then
    python3 codegen.py 
else
    exit -1
fi
if [[ "$?" == "0" ]];then
    gcc m.s -m32 -no-pie -o m.out
else
    exit -1
fi
if [[ "$?" == "0" ]];then
    ./m.out
else
    exit -1
fi

