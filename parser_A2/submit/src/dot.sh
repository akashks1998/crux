#!/bin/bash
python3 parser3.py $1 $2 $3
dot -Tps dot.gz -o out/outfile.ps
