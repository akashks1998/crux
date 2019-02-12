def get_grammer_line(s):
    s = s.strip().replace('-','_').replace('::', ' DOUBLECOLON ')
    return s

inp = open("grammer.txt", "r").read()

inp = inp.strip().split('\n')
out = "def p_" 
out = out + inp[0].strip().replace('-','_') + "(p):\n"
l1 ="    \'\'\'" + inp[0].strip().replace('-','_') + " :"
sp = len(l1)
l1 = l1 + " " + get_grammer_line(inp[1])
out = out +l1

if(len(inp) == 2):
    print(out +  "\'\'\'")
    exit()

for each in inp[2:]:
    out = out + "\n" + " " * (sp-1) + "| " +  get_grammer_line(each)

out = out + "\n    \'\'\'\n\n"

open("grammer.txt","w").write("")

print(out)

# select unprocessed grammer and run xclip -o > grammer.txt; python3 grammer.py