import pickle
import re

f = open("sym_table.obj", "rb")
scopeTableList = pickle.load(f)
currentScopeTable = 0
f = open("code.obj", "rb")
_3accode = pickle.load(f)
AddressFile = "adr"
FileName = ""

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

def loadAddr(reg, var):
    global code
    if "@" in var:
        info = checkVar(var, "all")["var"] if var.split('@')[0]=="tmp" else checkVar(var.split('@')[0], int(var.split('@')[1]))
        offset = info["offset"]
        base = info["base"]
        if "@" in str(offset):
            loadVar(reg,offset)
            code.append("lea " + "(%ebp , %" + reg + ", 1), " + "%" + reg )
        elif str(base) == "rbp":
            # offset as integer
            code.append("lea " + str(-offset) + "(%ebp), " + "%" + reg )
    else:
        print("Error in loading ")
        exit()

def loadVar(reg,var):
    global code
    if "@" in var:
        info = checkVar(var, "all")["var"] if var.split('@')[0]=="tmp" else checkVar(var.split('@')[0], int(var.split('@')[1]))
        offset = info["offset"]
        base = info["base"]
        type_ = info["type"]
        if "@" in str(offset):
            loadVar(reg,offset)
            if "|" in type_ or type_ in ["int", "float"]:
                code.append("mov "  + "(%ebp , %" + reg + ", 1), " + "%" + reg )
            elif type_ == "char":
                code.append("movb " + "(%ebp , %" + reg + ", 1), " + "%" + reg )
            else:
                print( " class error in store")
                exit()  
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
        if var[0]=="'" and var[2]=="'" and len(var)==3:
            code.append("mov $"+str(ord( var[1]))+" , %" + reg )
        else:
            code.append("mov $"+var+" , %" + reg )

def storeVar(reg,var):
    global code
    if "@" in var:
        info = checkVar(var, "all")["var"] if var.split('@')[0]=="tmp" else checkVar(var.split('@')[0], int(var.split('@')[1]))
        offset = info["offset"]
        base = info["base"]
        type_=info["type"]
        if "@" in str(offset):
            # offset in variable
            loadVar("edi",offset)
            if "|" in type_ or type_ in ["int", "float"]:
                code.append("mov "  + "(%ebp , %edi"  + ", 1), " + "%" + reg )
            elif type_ == "char":
                code.append("movb " + "(%ebp , %edi" + ", 1), " + "%" + reg )
            else:
                print( " class error in store")
                exit()  
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
    
    def op_inc(self, instr):
        inp = instr[0]
        loadVar("eax", inp)
        code.append("inc  %eax")
        storeVar("eax", inp)

    def op_dec(self, instr):
        inp = instr[0]
        loadVar("eax", inp)
        code.append("dec  %eax")
        storeVar("eax", inp)

    def op_logical_dual(self, instr, lt):
        out , inp1, inp2 = instr
        def log_op(x):
            d = {
                    "&" : "and ",
                    "|" : "or ",
                    "^" : "xor ",
                    "&&": "and ",
                    "||": "or ",
            }
            return d[x]

        loadVar("eax", inp1)
        loadVar("ebx", inp2)
        code.append(log_op(lt) +  " %ebx, %eax")
        storeVar("eax", out)
        
    def op_unary(self, instr):
        out , inp = instr
        loadVar("eax", inp)
        code.append("not %eax")
        storeVar("eax", out)

    def op_comp(self, instr, comp ):
        out , inp1, inp2 = instr
        loadVar("eax", inp1)
        loadVar("ebx", inp2)
        code.append("cmp %eax, %ebx")
        if comp == "<":
            code.append("setl %ecx")
        elif comp == ">":
            code.append("setg %ecx")
        elif comp == "<=":
            code.append("setle %ecx")            
        elif comp == ">=":   
            code.append("setge %ecx")            
        elif comp == "==":
            code.append("sete %ecx")            
        elif comp == "!=":
            code.append("setne %ecx")

        storeVar("ecx", out)
        
    def op_assign(self,instr):
        out , inp = instr
        if "@" in inp:
            info = checkVar(inp, "all")["var"] if inp.split('@')[0]=="tmp" else checkVar(inp.split('@')[0], int(inp.split('@')[1]))
            type_ = info["type"]
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
                code.append("movb $" + str(ord(inp)) + ",%eax")
                storeVar("eax", out)
            else:
                code.append("mov $" + inp + ", %eax")
                storeVar("eax", out)

    def op_label(self, instr):
        label = instr[0]
        code.append(str(label) + ":")

    def op_if(self, instr):
        var = instr[0]
        label = instr[1]
        loadVar("eax", var)
        code.append("cmp $0 , %eax ")
        code.append("jne " + label)

    def op_goto(self, instr):
        label = instr[0]
        code.append("jmp " + label)
    
    def op_lea(self, instr):
        out , inp = instr
        loadAddr("eax", inp)
        storeVar("eax", out)
    
    def op_pushParam(self, instr):
        inp = instr[0]
        info = checkVar(inp, "all")["var"] if inp.split('@')[0]=="tmp" else checkVar(inp.split('@')[0], int(inp.split('@')[1]))
        if "|" in info["type"] and info["type"][-1] == "a":
            # this is array
            loadAddr("eax", inp)
            code.append("push %eax")
        elif "|" in info["type"]:
            # this is pointer
            loadVar("eax", inp)
            code.append("push %eax")
        elif info["type"] in ["int", "char", "float"]:
            loadVar("eax", inp)
            code.append("push %eax")
        else:
            # this is class
            # to do
            pass

    def op_fcall(self, instr):
        out, label = instr
        code.append("call " + label)
        storeVar("eax", out)
    
    def op_removeParam(self, instr):
        pop_size = instr[0]
        if not pop_size.isdigit():
            print(" pop size should be int")
            exit()

        code.append("add " + pop_size + " %esp")

    def op_beginFunc(self, instr):
        expand_size = instr[0]
        if not expand_size.isdigit():
            print(" expand size should be int")
            exit()
        code.append("push %ebp")
        code.append("mov %esp, %ebp")
        code.append("sub $" + expand_size + ", %esp")
        code.append("push %ebx")
        code.append("push %ecx")
        code.append("push %edx")
        code.append("push %esi")
        code.append("push %edi")

    def op_return(self, instr):
        ret_val = instr[0]
        loadVar("eax", ret_val)
        code.append("pop %ebx")
        code.append("pop %ecx")
        code.append("pop %edx")
        code.append("pop %esi")
        code.append("pop %edi")
        code.append("mov %ebp, %esp")
        code.append("pop %ebp")
        code.append("ret ")        

    
        


    def gen_code(self, instr):
        if(instr["ins"]=="+"):
            self.op_add(instr["arg"])
        elif instr["ins"] == "-":
                self.op_sub(instr["arg"])
        elif instr["ins"] == "*":
            self.op_mult(instr["arg"])
        elif instr["ins"] == "/":
            self.op_div(instr["arg"])
        elif instr["ins"] == "%":
            self.op_modulo(instr["arg"])
        elif instr["ins"] == "<<":
            self.op_lshift(instr["arg"])
        elif instr["ins"] == ">>":
            self.op_rshift(instr["arg"])
        elif instr["ins"] == "++":
            self.op_inc(instr["arg"])
        elif instr["ins"] == "--":
            self.op_dec(instr["arg"])
        elif instr["ins"] == "=":
            self.op_assign(instr["arg"])
        elif instr["ins"] in ["&&","||","|","&&"]:
            self.op_logical_dual(instr["arg"],instr["ins"])
        elif instr["ins"] in ["~","!"]:
            self.op_unary(instr["arg"])
        elif instr["ins"] =="label":
            self.op_label(instr["arg"])
        elif instr["ins"] =="lea":
            self.op_lea(instr["arg"])
        elif instr["ins"] in ["<",">","==","<=",">=","!="]:
            self.op_comp(instr["arg"],instr["ins"])
        elif instr["ins"] =="goto":
            self.op_lea(instr["arg"])
        elif instr["ins"] =="PushParam":
            self.op_pushParam(instr["arg"])
        elif instr["ins"] =="Fcall":
            self.op_fcall(instr["arg"])
        elif instr["ins"] =="BeginFunc":
            self.op_beginFunc(instr["arg"])
        elif instr["ins"]=="return":
            self.op_return(instr["arg"])


if __name__ == "__main__":
    afile = open(AddressFile,'w')
    afile.write("//Code For " + FileName + "\n")
    x86_compiler=CodeGenerator()
    code.append(".text")
    code.append(".global main|") 
    code.append(".type main|, @function") 
    for i in _3accode:
        i=i.replace(' ','')
        z=[y for y in i.split("$") if y != '']
        x={"ins":z[1].strip(),"arg":z[2:]}
        x86_compiler.gen_code(x)
    for c in code:
        c=c.replace('|','')
        if c[-1]==':':
            print(c)
        else:
            print("\t",c)
