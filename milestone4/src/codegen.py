import pickle
import re

f = open("sym_table.obj", "rb")
scopeTableList = pickle.load(f)
currentScopeTable = 0
f = open("code.obj", "rb")
code = pickle.load(f)

AddressFile = "adr"
FileName = ""

from symbolTable import SymbolTable


def checkVar(identifier,scopeId="**", search_in_class = False):
    global scopeTableList
    global currentScopeTable
    if scopeId == "global":
        if scopeTableList[0].lookUp(identifier):
            return scopeTableList[0].getDetail(identifier)
        return False
    if scopeId == "all":
        scope=0
        while scope<len(scopeTableList):
            symbol_table = scopeTableList[scope]
            if symbol_table.type_ == "class" and search_in_class == False:
                scope=scope+1
                continue
            if symbol_table.lookUp(identifier):
                return {"var":scopeTableList[scope].getDetail(identifier), "scope":scope}
            scope=scope+1
        return False
    if scopeId == "*":
        if scopeTableList[currentScopeTable].lookUp(identifier):
            return scopeTableList[currentScopeTable].getDetail(identifier)
        return False
    if scopeId=="**":
        scope=currentScopeTable

        while scope!=None:
            symbol_table = scopeTableList[scope]
            if symbol_table.type_ == "class" and search_in_class == False:
                scope=scopeTableList[scope].parent
                continue
            if symbol_table.lookUp(identifier):
                return {"var":scopeTableList[scope].getDetail(identifier), "scope":scope}
            scope=scopeTableList[scope].parent
        return False
    else:
        if scopeTableList[scopeId].lookUp(identifier):
            return scopeTableList[scopeId].getDetail(identifier)
        return False

def parsequad(q):
    return [i.strip() for i in q.split("$")[1:]]

def off(ar):
    l=[]
    for a in ar:
        if "@" in a:
            c = checkVar(a, "all")["var"] if a.split('@')[0]=="tmp" else checkVar(a.split('@')[0], int(a.split('@')[1]))
            if str(c["offset"])[0]!="-":
                if c["base"]=="rbp":
                    offset = "-"+str(c["offset"])
                else:
                    offset = "+"+str(c["offset"])
            else:
                if c["base"]=="rbp":
                    offset = "+"+str(c["offset"])[1:]
                else:
                    offset = "-"+str(c["offset"])[1:]
            t = c["base"]+offset if c["base"]=="rbp" else c["base"]+offset
            l.append("[" + t + "]")
        else:
            l.append(a)
    return l


def acode(ar):
    o = off(ar)
    return ' '.join(o) if o != [] else ''

def give_asm_op(inst_type):
    op_dict = {
        "int+" : "add",
        "int-" : "sub",
        "int/" : "idiv",
        "int*" : "imul",
        "and" : "and",
        "or" : "or",
    }
    return op_dict[inst_type]

def LoadVar(reg,var):
    code=[]
    if "@" in var:
        info = checkVar(var, "all")["var"] if var.split('@')[0]=="tmp" else checkVar(var.split('@')[0], int(var.split('@')[1]))
        offset = info["offset"]
        base = info["base"]
        if "@" in str(offset):
            # offset in variable
            pass
        else:
            # offset as integer
            if offset < 0:
                code = [ "mov "+reg+", ["+base+" + " + str(-offset) + "]" ]
            else:
                code = [ "mov "+reg+", ["+base+" - " + str(offset) + "]" ]
    else:
        code = [ "mov "+reg+", " + str(var) ]
    return code

def StoreVar(reg,var):
    code=[]
    if "@" in var:
        info = checkVar(var, "all")["var"] if var.split('@')[0]=="tmp" else checkVar(var.split('@')[0], int(var.split('@')[1]))
        offset = info["offset"]
        base = info["base"]
        if "@" in str(offset):
            # offset in variable
            pass
        else:
            # offset as integer
            if offset < 0:
                code = [ "mov ["+base+" + " + str(-offset) + "] , "+reg  ]
            else:
                code = [ "mov ["+base+"  " + str(-offset) + "] , "+reg  ]
    else:
        print("Error in storing as it is int instaid of variable")
        exit()
    return code

def gen_asm_for_one_line(quad):
    code = []
    if quad[0] in ["int+", "int-", "int/", "int*"]:
        # load 2 and 3rd in reg, do compute and store in 1st
        var = quad[2]
        code=code+ LoadVar("eax",var)
        var = quad[3]
        code=code+ LoadVar("ebx",var)
        code=code+[give_asm_op(quad[0]) +" eax , ebx"]
        code=code+StoreVar("eax",quad[1])

        print(code)
    

if __name__ == "__main__":
    afile = open(AddressFile,'w')
    afile.write("//Code For " + FileName + "\n")
    x=1
    for i in code:
        line=len(i) - len(i.lstrip(' '))
        # afile.write('{0:3}'.format(x) + ":: " + t*" " + acode(parsequad(i)) + "\n")
        # print(parsequad(i))
        gen_asm_for_one_line(parsequad(i))
        x=x+1
