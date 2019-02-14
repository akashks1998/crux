python3 parser2.py 0 $1 $2 >temp.gz&
sleep 1
sed '$d' temp.gz>temp1.gz
echo "}">>temp1.gz
mv temp1.gz temp.gz
dot -Tps temp.gz -o outfile.pdf
xdg-open outfile.pdf