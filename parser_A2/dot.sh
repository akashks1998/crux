python3 parser2.py $1 tests/$2.cpp $3 
dot -Tps dot.gz -o outfile.ps
xdg-open outfile.ps