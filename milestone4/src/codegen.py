import pickle
import re
import operator

f = open("sym_table.obj", "rb")
scopeTableList = pickle.load(f)
currentScopeTable = 0
f = open("code.obj", "rb")
_3accode = pickle.load(f)
AddressFile = "adr"
FileName = ""
lineno=0
code = []

def checkVar(identifier,scopeId="**", search_in_class = False):
    global scopeTableList
    global currentScopeTable
    identifier = identifier if identifier.split('@')[0]=="tmp" else identifier.split('@')[0]
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

def loadAddr(reg, var):
    var = str(var)
    global code
    if "@" in var:
        info = checkVar(var, "all")["var"] if var.split('@')[0]=="tmp" else checkVar(var.split('@')[0], int(var.split('@')[1]))
        offset = info["offset"]
        base = info["base"]
        if base == "0":
            loadVar(reg,offset)
        elif base == "rbp":
            if "@" in str(offset):
                code.append("push %esi")
                loadVar("esi", offset)
                code.append("neg %esi")
                code.append("lea (%ebp, %esi, 1), %" + reg)
                code.append("pop %esi")
            else:
                code.append("lea " + str(-offset) + "(%ebp), %" + reg )
        else:
            print("error in load Addr")
            exit()
    else:
        print("Error in loading addr ")
        exit()


def loadVar(reg,var):
    global code
    var = str(var)
    if "@" in var:
        if var.split('@')[0]=="tmp":
            info = checkVar(var, "all")["var"]
        elif var.split('@')[0]=="gbl":
            code.append("mov $" + var + ", %" + reg)
            return
        else:
            info = checkVar(var.split('@')[0], int(var.split('@')[1]) )  
        
        offset = info["offset"]
        base = info["base"]
        type_=info["type"]
        if "@" in str(offset):
            # offset in variable
            r="esi"
            if str(base) == "0":
                loadVar(r,offset)
                if "|" in type_ or type_ in ["int", "float"]:
                    code.append("mov  (%"+r+"), %" + reg )
                elif type_ == "char":
                    code.append("movb (%"+r+"), %" + reg[1] + "l" )
                else:
                    print( " class error in load")
                    exit()
            elif str(base) == "rbp":
                loadVar(r,offset)
                if "|" in type_ or type_ in ["int", "float"]:
                    code.append("neg %"+r)
                    code.append("mov (%ebp , %"+ r + ", 1), %" + reg )
                elif type_ == "char":
                    code.append("neg %"+r)
                    code.append("movb (%ebp , %"+r + ", 1), %" +  reg[1] + "l" )
                else:
                    print( " class error in load")
                    exit()
            else:
                print("wrong base in load")
                exit()
        else:
            # offset is int
            if str(base) == "0":
                print("error : constant offset with base 0")
                exit()
            elif str(base) == "rbp":
                if "|" in type_ or type_ in ["int", "float"]:
                    code.append("mov " + str(-offset) + "(%ebp), %" + reg )
                elif type_ == "char":
                    code.append("movb " + str(-offset) + "(%ebp), %" +  reg[1] + "l" )
                else:
                    print( " class error in load")
                    exit()  
            else:
                print("wrong base in load")
                exit()         
    else:
        if var[0]=="'" and var[2]=="'" and len(var)==3:
            # this is char
            code.append("movb $"+str(ord( var[1]))+" , %" +  reg[1] + "l" )
        elif var.lstrip("-").isdigit():
            code.append("mov $"+var+" , %" + reg )
        else:
            print(var)
            print("Error in load")
            exit()


def storeVar(reg,var):
    global code
    var = str(var)
    if "@" in var:
        info = checkVar(var, "all")["var"] if var.split('@')[0]=="tmp" else checkVar(var.split('@')[0], int(var.split('@')[1]))
        offset = info["offset"]
        base = info["base"]
        type_=info["type"]
        if "@" in str(offset):
            r="edi"
            # offset in variable
            if str(base) == "0":
                loadVar(r,offset)
                if "|" in type_ or type_ in ["int", "float"]:
                    code.append("mov %" + reg + ", (%"+r+")" )
                elif type_ == "char":
                    code.append("movb %" +  reg[1] + "l" + ", (%"+r+")" )
                else:
                    print( " class error in store")
                    exit()
            elif str(base) == "rbp":
                loadVar(r,offset)
                if "|" in type_ or type_ in ["int", "float"]:
                    code.append("neg %"+r) # check base
                    code.append("mov %" + reg + ", (%ebp , %"+r  + ", 1)" )
                elif type_ == "char":
                    code.append("neg %"+r)
                    code.append("movb %" +  reg[1] + "l" + ", (%ebp , %"+r  + ", 1)" )
                else:
                    print( " class error in store")
                    exit()
            else:
                print("wrong base in store")
                exit()      
        else:
            # offset is int
            if str(base) == "0":
                print("error : constant offset with base 0")
                exit()
            elif str(base) == "rbp":
                if "|" in type_ or type_ in ["int", "float"]:
                    code.append("mov %" + reg + " , " + str(-offset) + "(%ebp)" )
                elif type_ == "char":
                    code.append("movb %" +  reg[1] + "l" + " , " + str(-offset) + "(%ebp)" )
                else:
                    print( " class error in store")
                    exit()  
            else:
                print("wrong base in store")
                exit()         
    else:
        print("Error in storing")
        exit()

def movVar(offsetSrc, baseSrc, offsetDest, baseDest , size = 8):
    if size == 4:
        reg = "edx"
        mov = "mov"
    if size == 2:
        reg = "dx"
        mov = "movw"
    if size == 1:
        reg = "dl"
        mov = "movb"

    if baseSrc == "rbp":
        code.append("neg %" + offsetSrc)
        code.append( mov + " (%ebp, %" + offsetSrc + ",1) , %" + reg)
        code.append("neg %" + offsetSrc)
    if baseSrc == "0":
        code.append(mov + " (%" + offsetSrc + "), %" + reg )
    
    if baseDest == "rbp":
        code.append("neg %" + offsetDest)
        code.append(mov + " %" + reg + ", (%ebp, %" + offsetDest + ",1)")
        code.append("neg %" + offsetDest)
    if baseDest == "0":
        code.append(mov + " %" + reg + ", (%" + offsetDest + ")")
        
 

reg_used={"eax":[-1,None],
          "ebx":[-1,None],
          "ecx":[-1,None],
          "edx":[-1,None],
          "esi":[-1,None],
          "edi":[-1,None]
}

def getReg(reg=None,var=None,free=False):
    if free==True:
        if reg!=None:
            if reg_used[reg][1]!=None:
                storeVar(reg,reg_used[reg][1])
            reg_used[reg]=[-1,None]
        return reg
    if reg==None:
        r=min(reg_used.items(), key=operator.itemgetter(1))[0]
    else:
        r=reg
    x=reg_used[r][1]
    if var==None:
        reg_used[r]=[len(_3accode)+1,var]
    else:
        reg_used[r]=[lineno,var]
    if x!=None:
        storeVar(r,x)
    return r
    

class CodeGenerator:
    def __init__(self):
        code.append(".data")
        code.append('print_fmt_int:\n\t\t .string "%d\\n" ')
        code.append('print_fmt_char:\n\t\t .string "%c\\n" ')
        code.append('scan_fmt_int:\n\t\t .string "%d" ')
        code.append('scan_fmt_char:\n\t\t .string "%c" ')
        for j in scopeTableList[0].table.items():
            if isinstance(j[1], dict) and "base" in j[1].keys() and "offset" in j[1].keys():
                code.append(str(j[1]["offset"])+':\n\t\t .zero '+str(j[1]["size"])+' ')
        code.append(".text")
        code.append(".global main|")
        code.append(".type main|, @function") 

    def op_print_int(self, instr):
        to_print_int = instr[0]
        loadVar("eax",to_print_int)
        code.append("push %ebp")
        code.append("mov %esp,%ebp")
        code.append("push %eax")
        code.append("push $print_fmt_int")
        code.append("call printf")
        code.append("add  $8, %esp")
        code.append("mov %ebp, %esp")
        code.append("pop %ebp")
    
    def op_print_char(self, instr):
        to_print_int = instr[0]
        loadVar("eax",to_print_int)
        code.append("push %ebp")
        code.append("mov %esp,%ebp")
        code.append("push %eax")
        code.append("push $print_fmt_char")
        code.append("call printf")
        code.append("add  $8, %esp")
        code.append("mov %ebp, %esp")
        code.append("pop %ebp")
    def op_malloc(self, instr):
        to_malloc,size=instr
        code.append("push %ebp")
        code.append("mov %esp,%ebp")
        loadVar("edi", size)
        code.append("push %edi")
        code.append("call malloc")
        code.append("add $4, %esp")
        code.append("mov %ebp, %esp")
        code.append("pop %ebp")
        storeVar("eax",to_malloc)
        
    def op_free(self, instr):
        to_free=instr[0]
        code.append("push %ebp")
        code.append("mov %esp,%ebp")
        loadVar("edi", to_free)
        code.append("push %edi")
        code.append("call malloc")
        code.append("add $4, %esp")
        code.append("mov %ebp, %esp")
        code.append("pop %ebp")

    def op_scan_int(self, instr):
        to_scan_int = instr[0]
        loadAddr("eax",to_scan_int)
        code.append("push %ebp")
        code.append("mov %esp,%ebp")
        code.append("push %eax")
        code.append("push $scan_fmt_int")
        code.append("call scanf")
        code.append("add  $8, %esp")
        code.append("mov %ebp, %esp")
        code.append("pop %ebp")

    def op_scan_char(self, instr):
        to_scan_int = instr[0]
        loadAddr("eax",to_scan_int)
        code.append("push %ebp")
        code.append("mov %esp,%ebp")
        code.append("push %eax")
        code.append("push $scan_fmt_char")
        code.append("call scanf")
        code.append("add  $8, %esp")
        code.append("mov %ebp, %esp")
        code.append("pop %ebp")

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
        code.append("cmp %ebx, %eax")
        code.append("mov $0, %ecx")
        if comp == "<":
            code.append("setl %cl")
        elif comp == ">":
            code.append("setg %cl")
        elif comp == "<=":
            code.append("setle %cl")            
        elif comp == ">=":   
            code.append("setge %cl")            
        elif comp == "==":
            code.append("sete %cl")            
        elif comp == "!=":
            code.append("setne %cl")

        storeVar("ecx", out)
        
    def op_assign(self,instr):
        out , inp = instr
        if "@" in inp:
            if inp.split('@')[0] == "gbl":
                loadVar("eax",inp)
                storeVar("eax", out)
                return
            info = checkVar(inp, "all")["var"] if inp.split('@')[0]=="tmp" else checkVar(inp.split('@')[0], int(inp.split('@')[1]))
            type_ = info["type"]
            if "|" in type_ or type_ in ["int", "char", "float"]:
                loadVar("eax",inp)
                storeVar("eax", out)
            else:
                offset = info["offset"]
                base = info["base"]
                size = info["size"]
                inp = out
                info = checkVar(inp, "all")["var"] if inp.split('@')[0]=="tmp" else checkVar(inp.split('@')[0], int(inp.split('@')[1]))
                offset_d = info["offset"]
                base_d = info["base"]
                size_d = info["size"]

                loadVar("eax", offset)
                loadVar("ebx", offset_d)
                def add_to_offset(base,base_d, size):
                    if base == "0":
                        code.append("add $" + str(size) + ", %eax")
                    else:
                        code.append("sub $" + str(size) + ", %eax")
                    if base_d == "0":
                        code.append("add $" + str(size) + ", %ebx")
                    else:
                        code.append("sub $" + str(size) + ", %ebx")
                # if size % 4 == 0:
                #     for i in range(0, size, 4):
                #         movVar("eax", base, "ebx", base_d, 4)
                #         add_to_offset(base,base_d, 4)         
                # elif size % 2 == 0 :       
                #     for i in range(0, size % 4, 2 ):
                #         movVar("eax", base, "ebx", base_d, 2)
                #         add_to_offset(base,base_d, 2)
                # else:
                #     for i in range(0, size, 1 ):
                #         movVar("eax", base, "ebx", base_d, 1)
                #         add_to_offset(base,base_d, 1)
                for i in range(0, size, 1 ):
                    movVar("eax", base, "ebx", base_d, 1)
                    add_to_offset(base,base_d, 1)


        else:
            # it is constant assignment like a =1;
            info = checkVar(out, "all")["var"] if out.split('@')[0]=="tmp" else checkVar(out.split('@')[0], int(out.split('@')[1]))
            type_ = info["type"]
            if type_ == "char":
                code.append("mov $" + str(ord(inp[1])) + ",%eax")
                storeVar("eax", out)
            else:
                code.append("mov $" + inp + ", %eax")
                storeVar("eax", out)

    def op_label(self, instr):
        label = instr[0]
        code.append(str(label) + ":")

    def op_ifnz(self, instr):
        var = instr[0]
        label = instr[1]
        loadVar("eax", var)
        code.append("cmp $0 , %eax ")
        code.append("jne " + label)
    
    def op_ifz(self, instr):
        var = instr[0]
        label = instr[1]
        loadVar("eax", var)
        code.append("cmp $0 , %eax ")
        code.append("je " + label)

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
            offset = info["offset"]
            base = info["base"]
            size = info["size"]
            
            base_d = "0"
            loadVar("eax", offset)
            code.append("sub $" + str(size) + ", %esp")
            code.append("mov %esp, %ebx")
            def add_to_offset(base,base_d, size):
                if base == "0":
                    code.append("add $" + str(size) + ", %eax")
                else:
                    code.append("sub $" + str(size) + ", %eax")
                if base_d == "0":
                    code.append("add $" + str(size) + ", %ebx")
                else:
                    code.append("sub $" + str(size) + ", %ebx")

            for i in range(0, size, 1 ):
                movVar("eax", base, "ebx", base_d, 1)
                add_to_offset(base,base_d, 1)

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
        elif instr["ins"] =="ifnz":
            self.op_ifnz(instr["arg"])
        elif instr["ins"] =="ifz":
            self.op_ifz(instr["arg"])
        elif instr["ins"] =="lea":
            self.op_lea(instr["arg"])
        elif instr["ins"] in ["<",">","==","<=",">=","!="]:
            self.op_comp(instr["arg"],instr["ins"])
        elif instr["ins"] =="goto":
            self.op_goto(instr["arg"])
        elif instr["ins"] =="PushParam":
            self.op_pushParam(instr["arg"])
        elif instr["ins"] =="Fcall":
            self.op_fcall(instr["arg"])
        elif instr["ins"] =="BeginFunc":
            self.op_beginFunc(instr["arg"])
        elif instr["ins"]=="return":
            self.op_return(instr["arg"])
        elif instr["ins"]=="print_int":
            self.op_print_int(instr["arg"])
        elif instr["ins"]=="print_char":
            self.op_print_char(instr["arg"])
        elif instr["ins"]=="scan_int":
            self.op_scan_int(instr["arg"])
        elif instr["ins"]=="scan_char":
            self.op_scan_char(instr["arg"])
        elif instr["ins"]=="malloc":
            self.op_malloc(instr["arg"])
        elif instr["ins"]=="free":
            self.op_free(instr["arg"])


if __name__ == "__main__":
    afile = open(AddressFile,'w')
    afile.write("//Code For " + FileName + "\n")
    x86_compiler=CodeGenerator()
    for i in _3accode:
        lineno=lineno+1
        i=i.replace(' ','')
        z=[y for y in i.split("$") if y != '']
        x={"ins":z[1].strip(),"arg":z[2:-1]}
        currentScopeTable = int(z[-1])
        code.append("// " + i.split('$')[0])
        x86_compiler.gen_code(x)

    s_file = open('m.s', 'w')
    for c in code:
        c=c.replace('|','').replace('#', '').replace('@','')
        if c[-1]==':':
            s_file.write(c+ "\n")
        else:
            s_file.write("\t" + c + "\n")
