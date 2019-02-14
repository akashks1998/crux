python3 parser2.py 0 tests/$1.cpp&
sleep 1
dot -Tps dot.gz -o outfile.ps
xdg-open outfile.ps