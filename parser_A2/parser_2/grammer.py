inp = open("2.y", "r").read()
inp = inp.strip().split('\n')
for each in inp[:]:
    each=each.strip()
    if each!='' and each[0]!=":" and each[0]!="|":
        print("\n    \'\'\'\n\n")
        print("def p_" + each+ "(p):")
        l1 ="    \'\'\'" + each+" "
        sp = len(l1)
    elif each!='':
        print(l1+each)
        l1=" " * (sp-1)
print("\n    \'\'\'\n\n")