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

code = []

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

def loadVar(reg,var):
    global code
    if "@" in var:
        info = checkVar(var, "all")["var"] if var.split('@')[0]=="tmp" else checkVar(var.split('@')[0], int(var.split('@')[1]))
        offset = info["offset"]
        base = info["base"]
        type_ = info["type"]
        if "@" in str(offset):
            # offset in variable
            pass
        elif str(base) == "rbp":
            # offset as integer
            if "|" in type_ or type_ in ["int", "float"]:
                code.append("mov " + str(-offset) + "(%ebp), " + "%" + reg )
            elif type_ == "char":
                code.append("movb " + str(-offset) + "(%ebp), " + "%" + reg )
            else:
                print( " class error in store")
                exit()  
    else:
        print("Error in loading ")
        exit()
    return code

def storeVar(reg,var):
    global code
    if "@" in var:
        info = checkVar(var, "all")["var"] if var.split('@')[0]=="tmp" else checkVar(var.split('@')[0], int(var.split('@')[1]))
        offset = info["offset"]
        base = info["base"]
        if "@" in str(offset):
            # offset in variable
            pass
        elif str(base) == "rbp":
            if "|" in type_ or type_ in ["int", "float"]:
                code.append("mov " + "%" + reg + " , " + str(-offset) + "(%ebp)" )
            elif type_ == "char":
                code.append("movb " + "%" + reg + " , " + str(-offset) + "(%ebp)" )
            else:
                print( " class error in store")
                exit()                


    else:
        print("Error in storing")
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


class CodeGenerator:
    def gen_start_template(self):
        print()
        print("section .text")
        print("global main")

    def op_add(self, instr):
        out , inp1, inp2 = instr
        loadVar("eax", inp1)
        loadVar("ebx", inp2)
        code.append("add %ebx, %eax")
        storeVar("eax", out)

    def op_sub(self, instr):
        out , inp1, inp2 = instr
        loadVar("eax", inp1)
        loadVar("ebx", inp2)
        code.append("sub %ebx, %eax")
        storeVar("eax", out)
        
    def op_mult(self, instr):
        out , inp1, inp2 = instr
        loadVar("eax", inp1)
        loadVar("ebx", inp2)
        code.append("imul %ebx, %eax")
        storeVar("eax", out)

    def op_div(self, instr):
        # idiv %ebx — divide the contents of EDX:EAX by the contents of EBX. Place the quotient in EAX and the remainder in EDX.
        out , inp1, inp2 = instr
        loadVar("eax", inp1)
        loadVar("ebx", inp2)
        code.append("mov $0, %edx")
        code.append("idiv %ebx")
        storeVar("eax", out)
    
    def op_modulo(self, instr):
        # idiv %ebx — divide the contents of EDX:EAX by the contents of EBX. Place the quotient in EAX and the remainder in EDX.
        out , inp1, inp2 = instr
        loadVar("eax", inp1)
        loadVar("ebx", inp2)
        code.append("mov $0, %edx")
        code.append("idiv %ebx")
        storeVar("edx", out)
    
    def op_lshift(self, instr):
        out , inp1, inp2 = instr
        loadVar("eax", inp1)
        loadVar("cl", inp2)
        code.append("shl %cl, %eax")
        storeVar("eax", out)

    def op_rshift(self, instr):
        out , inp1, inp2 = instr
        loadVar("eax", inp1)
        loadVar("cl", inp2)
        code.append("shr %cl, %eax")
        storeVar("eax", out)

    def op_assign(self,instr):
        out , inp = instr
        if "@" in inp:
            info = checkVar(inp, "all")["var"] if inp.split('@')[0]=="tmp" else checkVar(inp.split('@')[0], int(inp.split('@')[1]))
            type_ = info["type"]
            offset = info["offset"]
            base = info["base"]
            if "|" in type_ or type_ in ["int", "char", "float"]:
                loadVar("eax",inp)
                storeVar("eax", out)
            else:
                # it is a class assignment
                # do it later
                pass
        else:
            # it is constant assignment like a =1;
            info = checkVar(out, "all")["var"] if out.split('@')[0]=="tmp" else checkVar(out.split('@')[0], int(out.split('@')[1]))
            type_ = info["type"]
            if type_ == "char":
                code.append("movb $" + str(ord(inp)) + ", eax")
                storeVar("eax", out)
            else:
                code.append("mov $" + inp + ", eax")
                storeVar("eax", out)






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
