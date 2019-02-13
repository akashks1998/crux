python3 parser.py 0 ../tests/1.cpp >temp.gz&
sleep 1
sed '$d' temp.gz>temp1.gz
echo "}">>temp1.gz
mv temp1.gz temp.gz
dot -Tps temp.gz -o outfile.pdf
xdg-open outfile.pdf