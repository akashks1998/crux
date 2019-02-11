inp = open("grammer.txt", "r").read()

 
def get_name(i):
    name = (i.split(':')[0]).strip().replace('-','_')
    return name

inp = inp.split('\n')
out = "def p_" 
out = out + get_name(inp[0]) + "(p):\n"
l1 ="    \'\'\'" + get_name(inp[0]) + " :"
sp = len(l1)
l1 = l1 + " " + inp[1].strip().replace('-','_')
out = out +l1

if(len(inp) == 2):
    print(out +  "\'\'\'")
    exit()

for each in inp[2:]:
    out = out + "\n" + " " * (sp-1) + "| " +  each.strip().replace('-','_')

out = out + "\n    \'\'\'\n\n"

open("grammer.txt","w").write("")

print(out)

# select unprocessed grammer and run xclip -o > grammer.txt; python3 grammer.py