import pprint
from ply import yacc
import os
import sys
import time
from lexer import lexer
from lexer import tokens as lexTokens
from symbolTable import SymbolTable
import re
import inspect
import pickle

pp = pprint.PrettyPrinter(indent=4)
cnt=0
tokens = lexTokens
filename=""
error_line_offset=1
def f(p):
    global cnt
    p_name = sys._getframe(1).f_code.co_name
    cnt=cnt+1
    out = (p_name[2:],cnt)
    open('dot.gz','a').write("    "+str(cnt)+"[label="+p_name[2:]+"]")
    for each in range(len(p)-1):
        if( not isinstance(p[each + 1], OBJ) ):
            cnt=cnt+1
            open('dot.gz','a').write("    "+str(cnt)+"[label=\""+str(p[each+1]).replace('"',"")+"\"]")
            token = p[each + 1]
            p[each + 1] = OBJ()
            p[each + 1].data = token
            p[each+1].parse = (token, cnt)            
        open('dot.gz','a').write("    " + str(out[1])  +  " -> " + str(p[each+1].parse[1]))
    return out

FileName = '<given file>'
CodeFile = 'code.crux'
x86File = 'x86'
SymbolTableFileName = 'symbol.dump'
AddressFile = 'code2.crux'
        
labeldict = {}
scopeTableList = []
globalScopeTable = SymbolTable()
scopeTableList.append(globalScopeTable)
currentTmp=0
new_pointer_size = 4
currentScopeTable = 0

offsetList = [0]
offsetParent = [None]
currentOffset = 0

allowed_types={}
allowed_types["float"]=["int","float","char" ]
allowed_types["int"]=["float", "char","int"]
allowed_types["char"]=["int", "char"]
allowed_types["pointer"]=["int"]

operator_allowed={}
operator_allowed["+"]=["int","float","char"]
operator_allowed["-"]=["int","float","char"]
operator_allowed["*"]=["int","float","char"]
operator_allowed["/"]=["int","float","char"]
operator_allowed["%"]=["int"]
operator_allowed["||"]=["int"]
operator_allowed["&&"]=["int"]
operator_allowed["!"]=["int"]
operator_allowed["|"]=["int"]
operator_allowed["&"]=["int"]
operator_allowed["~"]=["int"]
operator_allowed["^"]=["int"]
operator_allowed[">"]=["int","float","char"]
operator_allowed[">="]=["int","float","char"]
operator_allowed["<"]=["int","float","char"]
operator_allowed["<="]=["int","float","char"]
operator_allowed["<<"]=["int"]
operator_allowed[">>"]=["int"]

def get_offset():
    global offsetList
    global currentOffset
    return offsetList[currentOffset]

def add_to_offset(val):
    global offsetList
    global currentOffset
    offsetList[currentOffset] = offsetList[currentOffset] + val 


def pushOffset():
    global offsetList
    global currentOffset
    global offsetParent
    newOffset = 0
    offsetList.append(newOffset)
    offsetParent.append(currentOffset)
    currentOffset = len(offsetList) - 1

def popOffset():
    global offsetList
    global currentOffset
    global offsetParent
    currentOffset = offsetParent[currentOffset]


def code(*rest):
    s = ""
    for r in rest:
        s = s + " " + str(r)
    print(s)

class OBJ:    
    def __init__(self):
        self.data = {}
        self.code = []
        self.place = "NOP"
    
    def __str__(self):
        return ( str(self.data) +  str(self.place))

def getnewlabel(s="label"):

    labeldict[s] = labeldict[s]+1 if s in labeldict.keys() else 0
    label = s + "#" + str(labeldict[s])
    return label

def getnewvar(type_, offset = None, size = None, base="rbp"):
    global currentTmp
    tmp = "tmp@" + str(currentTmp)
    # if tmp=="tmp@26":
        # print('caller name:', inspect.stack()[1][3])
    currentTmp = currentTmp + 1
    if offset == None:
        size = get_size(type_)
        add_to_offset(size)
        offset = get_offset()
    
    data = {"type" :  type_ , "class" : "temp", "size" : size, "offset" : offset , "base" : str(base)}
    pushVar(tmp, data)

    return tmp

def pushScope(type_ = None):
    global scopeTableList
    global currentScopeTable
    newScope = SymbolTable(parent=currentScopeTable, type_ = type_)
    scopeTableList.append(newScope)
    currentScopeTable = len(scopeTableList) - 1

def popScope():
    global scopeTableList
    global currentScopeTable
    currentScopeTable = scopeTableList[currentScopeTable].parent

def getParentScope(scopeId):
    global scopeTableList
    if(scopeId < len(scopeTableList)):
        return scopeTableList[scopeId].parent 
    else:
        return False


def pushVar(identifier, val,scope = None):
    global scopeTableList
    global currentScopeTable

    if scope == None:    
        if checkVar(identifier, currentScopeTable )==False:
            scopeTableList[currentScopeTable].insert(identifier,val)
            return True
        else:
            return False
    else:
        if checkVar(identifier, scope )==False:
            scopeTableList[scope].insert(identifier,val)
            return True
        else:
            return False
def popVar(identifier, scope):
    global scopeTableList
    scopeTableList[scope].delete(identifier)

def assigner(p,x):
    if isinstance(p[x].data,str):
        return p[x].data
    else:
        return p[x].data.copy()

def allowed_type(converted_from,converted_to):
    global allowed_types
    if converted_from==converted_to:
        return True
    if "|" in converted_from or "|" in converted_to:
        if "|" in converted_from and converted_from[-1]=='p' and (converted_to[-1]=="p" or converted_to in allowed_types["pointer"]):
            return True
        if "|" in converted_to and converted_to[-1]=='p' and (converted_from[-1]=="p" or converted_from in allowed_types["pointer"]):
            return True

        return False
    if converted_to not in allowed_types.keys():
        return False
    return (converted_from in allowed_types[converted_to])

def break_continue(l, a, b=""):
    # t = [quad("label", [a], "goto->"+a) if re.fullmatch('[ ]*break', i) else i for i in l]
    t = [quad("goto", [a], "goto->"+a) if re.fullmatch('[ ]*break', i) else i for i in l]
    # s = [quad("label", [b], "goto->"+b) if re.fullmatch('[ ]*continue', i) else i for i in t]
    s = [quad("goto", [b], "goto->"+b) if re.fullmatch('[ ]*continue', i) else i for i in t]
    return s if b!="" else t

def cast_string(place, converted_from,converted_to,t=None):
    return {"place":place,"code":[]}
    if converted_from==converted_to:
        return {"place":place,"code":[]}
    if allowed_type(converted_from,converted_to)==True:
        if t==None:
            t=getnewvar(converted_to)
        return {"place":t,"code":[ quad(converted_from+"_to_"+converted_to, [t, place, ''], t +" = " + converted_from+"_to_"+converted_to+"("+place+")") ]}
    return False

def op_allowed(op, typ):
    global operator_allowed
    if op not in operator_allowed.keys():
        return True
    return typ in operator_allowed[op]

def operator(op, op1 ,op2 ,typ=None):
    if (not op_allowed(op,op2.data["type"]) )or (not op_allowed(op,op2.data["type"])) :
        return False
    prec={
        "char":1,
        "int":2,
        "float":3
    }
    if op1.data["type"] == op2.data["type"]:
        if typ==None:
            typ=op1.data["type"]
        t=getnewvar(typ)
        return {"place":t,"code":[ quad( op , [t,op1.place,op2.place], t + " = " + op1.place + " " + op + " "+op2.place) ],"type":typ}
    elif prec[ op1.data["type"] ]>prec[ op2.data["type"] ]:
        y=cast_string( op2.place, op2.data["type"],op1.data["type"] )
        if typ==None:
            typ=op1.data["type"]
        t=getnewvar(typ)
        if y==False:
            return False
        return {"place":t,"code":y["code"]+[ quad( op , [t,op1.place,y["place"]], t +" = "+ op1.place+" "+ op +" "+ y["place"]) ],"type":typ}
    else:
        y=cast_string( op1.place, op1.data["type"],op2.data["type"] )
        if y==False:
            return False
        if typ==None:
            typ=op2.data["type"]
        t=getnewvar(typ)
        return {"place":t,"code":y["code"]+[ quad(op,[t,y["place"],op2.place],t +" = " + y["place"] +" "+op+" "+ op2.place) ],"type":typ}

def get_size(data_type, basic = True):
    data_type = data_type[:-1] if data_type[-1] == "|" else data_type
    size = {
        "int" : 4,
        "float" : 4,
        "char" : 1,
        "void" :  0
    }
    if("|" in data_type):
        if basic == True:
            basic_type = data_type.rstrip("r").rstrip("p").rstrip("|")
            if basic_type in size.keys():
                return 4
            get_class = checkVar(basic_type, "global")
            if get_class ==  False:
                print(" Error :: Class " + basic_type + " is not defined")
                exit()
            return 4
        else:
            return 4

    if data_type in size.keys():
        return size[data_type]

    # it has to be class
    get_class = checkVar(data_type, "global")
    if get_class ==  False:
        print(" Error :: Class " + data_type + " is not defined")
        exit()
    return get_class["size"]

def updateVar(identifier, val,scope=None):
    global scopeTableList
    global currentScopeTable

    if scope == None:    
        scopeTableList[currentScopeTable].update(identifier, val)
    else:
        scopeTableList[scope].update(identifier, val)

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
def retType(p,i,j):
    if "ret_type" in p[i].data.keys() and "ret_type" in p[j].data.keys():
        if p[i].data["ret_type"]==p[j].data["ret_type"]:
            p[0].data["ret_type"]=p[i].data["ret_type"]
        else:
            report_error(",Return type is not same",p.lineno(0))
    else:
        if "ret_type" in p[i].data.keys():
            p[0].data["ret_type"]=p[i].data["ret_type"]
        if "ret_type" in p[j].data.keys():
            p[0].data["ret_type"]=p[j].data["ret_type"]

def report_error(msg, line):
    global error_line_offset
    if line=="break" or line=="continue":
        print("Error : " + msg + ", Check your " + line + "s")
        exit()
    print("Error at line : " + str(line-error_line_offset) + " :: " + msg)
    exit()

start = 'program'

precedence = (
    ('left', 'PLUSOP', 'MINUSOP'),
    ('left', 'MULTOP', 'DIVOP', 'MODOP'),
    ('left', 'DPLUSOP', 'DMINUSOP'),
    ('left', 'DOT', 'ARROW'),
    ('left', 'LSHIFT', 'RSHIFT'),
    ('left', 'LTCOMP', 'LTECOMP'),
    ('left', 'GTCOMP', 'GTECOMP'), 
    ('left', 'LOWER'),
    ('left', 'HIGHER'),
)

def p_program(p):
    '''program : translation_unit
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    for l in range(len(p)):
        p[0].code = p[0].code + p[l].code.copy()
    for i in p[0].code:
        if re.fullmatch('[ ]*break', i) != None:
            report_error("break should be inside for/do-while/while/switch-case !!", "break")
        elif re.fullmatch('[ ]*continue', i) != None:
            report_error("continue should be inside for/do-while/while !!", "continue")
    generate_code(p)

def p_translation_unit(p):
    '''translation_unit : declaration_seq''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    
    p[0].code = [quad("eq",["heap_ptr@0",str(get_offset()),""],"heap_ptr@0 = "+str(get_offset()))]+ p[1].code.copy()

def p_declaration_seq(p):
    ''' declaration_seq : declaration_seq declaration
                        | declaration
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    if len(p)==2:
        p[0].code=p[1].code.copy()
    else:
        p[0].code=p[1].code.copy()+p[2].code.copy()

def p_error(p):
    global error_line_offset
    print("Syntax Error: line " + str(p.lineno-error_line_offset) + ":" + filename.split('/')[-1], "near", p.value)
    exit()

# def p_empty(p): 
#     'empty :' 
#     p[0]=OBJ()
#     p[0].data=None

def p_conditional_expression(p): 
    '''conditional_expression : logical_OR_expression 
                              | logical_OR_expression QUESMARK expression COLON conditional_expression 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    if len(p)==2:
        p[0].data = assigner(p,1)
        p[0].place = p[1].place
        p[0].code = p[1].code 
    else:
        allowed_type = ["int", "char", "float"]
        if p[1].data["type"] not in allowed_type:
            report_error("Expected integer, char or float, found something else", p.lineno(0))
        if p[3].data["type"] != p[5].data["type"]:
            report_error("Type mismatch between two opearands", p.lineno(0))
        p[0].data = { "type" : p[3].data["type"] }
        p[0].place = getnewvar(p[3].data["type"])
        p[0].after=getnewlabel()
        p[0].else_=getnewlabel()
        t=cast_string(p[1].place,p[1].data["type"],"int")

        p[0].code = p[1].code + t["code"] + [ quad("ifz",[t["place"],p[0].else_,""],"if "+t["place"] +"==0: goto "+ p[0].else_) ]\
           + p[3].code+ [ quad("eq",[p[0].place,p[3].place],p[0].place + " = " + p[3].place)] +[ quad("label",[p[0].begin,"",""], p[0].begin+":") ]\
            + [ quad("label",[p[0].else_,"",""],p[0].else_+":") ]+ p[5].code+ [ quad("eq",[p[0].place, p[5].place],p[0].place + " = " + p[5].place) ]

        

def p_logical_OR_expression(p): 
    '''logical_OR_expression : logical_AND_expression 
                             | logical_OR_expression OROP logical_AND_expression 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

    if len(p)==2:
        p[0].data = assigner(p,1)
        p[0].place = p[1].place
        p[0].code = p[1].code 
    if len(p)==4:
        allowed_type = ["int", "char", "float"]
        if p[1].data["type"] in allowed_type and p[3].data["type"] in allowed_type:
            p[0].data = { "type" : "int" }
        else:
            report_error("Type not compatible with OR operation", p.lineno(0))
        p[0].place = getnewvar("int")
        t=cast_string(p[1].place,p[1].data["type"],"int")
        t1=cast_string(p[3].place,p[3].data["type"],"int")
        p[0].code = p[1].code + p[3].code + t["code"] +t1["code"]+ [ quad(str(p[2].data),[p[0].place, t["place"], t1["place"]],p[0].place + " = " + t["place"] + str(p[2].data) + t1["place"]) ]

   
def p_logical_AND_expression(p): 
    '''logical_AND_expression : inclusive_OR_expression %prec LOWER
                              | logical_AND_expression ANDOP inclusive_OR_expression %prec HIGHER
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    if len(p)==2:
        p[0].data = assigner(p,1)
        p[0].place = p[1].place
        p[0].code = p[1].code 
    if len(p)==4:
        allowed_type = ["int", "char", "float"]
        if p[1].data["type"] in allowed_type and p[3].data["type"] in allowed_type:
            p[0].data = {"type" : "int"}
        else:
            report_error("Type not compatible with AND operation", p.lineno(0))
        p[0].place = getnewvar("int")
        t=cast_string(p[1].place,p[1].data["type"],"int")
        t1=cast_string(p[3].place,p[3].data["type"],"int")
        p[0].code = p[1].code + p[3].code + t["code"] +t1["code"]+ [ quad(str(p[2].data),[p[0].place, t["place"], t1["place"]],p[0].place + " = " + t["place"] + str(p[2].data) + t1["place"]) ]



def p_inclusive_OR_expression(p): 
    '''inclusive_OR_expression : exclusive_OR_expression 
                               | inclusive_OR_expression BOROP exclusive_OR_expression 
    ''' 
    # this is bitwise or
    p[0] = OBJ() 
    p[0].parse=f(p)
    if len(p)==2:
        p[0].data = assigner(p,1)
        p[0].place = p[1].place
        p[0].code = p[1].code 
    if len(p)==4:
        if p[1].data["type"]=="int" and p[3].data["type"] =="int":
            p[0].data = {"type" : "int"}
        else:
            report_error("Type not compatible with bitwise or operation", p.lineno(1))
        p[0].place = getnewvar("int")
        p[0].code = p[1].code + p[3].code + [ quad(str(p[2].data),[p[0].place,p[1].place,p[3].place],p[0].place + " = " + p[1].place + str(p[2].data) + p[3].place) ]


def p_exclusive_OR_expression(p): 
    '''exclusive_OR_expression : AND_expression 
                               | exclusive_OR_expression XOROP AND_expression 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    if len(p)==2:
        p[0].data = assigner(p,1)
        p[0].place = p[1].place
        p[0].code = p[1].code 
    if len(p)==4:
        if p[1].data["type"]=="int" and p[3].data["type"] =="int":
            p[0].data = {"type" : "int"}
        else:
            report_error("Type not compatible with bitwise xor operation", p.lineno(1))
        p[0].place = getnewvar("int")
        p[0].code = p[1].code + p[3].code + [ quad(str(p[2].data),[p[0].place,p[1].place,p[3].place],p[0].place + " = " + p[1].place + str(p[2].data) + p[3].place) ]


def p_AND_expression(p): 
    '''AND_expression : equality_expression 
                      | AND_expression BANDOP equality_expression 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    if len(p)==2:
        p[0].data = assigner(p,1)
        p[0].place = p[1].place
        p[0].code = p[1].code 
    if len(p)==4:
        if p[1].data["type"]=="int" and p[3].data["type"] =="int":
            p[0].data = {"type" : "int"}
        else:
            report_error("Type not compatible with bitwise and operation", p.lineno(1))
        
        p[0].place = getnewvar("int")
        p[0].code = p[1].code + p[3].code + [ quad(str(p[2].data),[p[0].place,p[1].place,p[3].place],p[0].place + " = " + p[1].place + str(p[2].data) + p[3].place) ]

def p_equality_expression(p): 
    '''equality_expression : relational_expression 
                           | equality_expression EQCOMP relational_expression 
                           | equality_expression NEQCOMP relational_expression 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    if len(p)==2:
        p[0].data = assigner(p,1)
        p[0].place = p[1].place
        p[0].code = p[1].code  
    if len(p)==4:
        x=operator( p[2].data, p[1], p[3],"int" )
        if x==False:
            report_error("Type not compatible with relational operation", p.lineno(0))
        p[0].place = x["place"]
        p[0].code = p[1].code + p[3].code + x["code"]
        p[0].data["type"]="int"
    

def p_relational_expression(p): 
    '''relational_expression : shift_expression 
                             | relational_expression LTCOMP  shift_expression 
                             | relational_expression GTCOMP  shift_expression 
                             | relational_expression LTECOMP shift_expression 
                             | relational_expression GTECOMP shift_expression 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    if len(p)==2:
        p[0].data = assigner(p,1)
        p[0].place = p[1].place
        p[0].code = p[1].code
    if len(p)==4:
        allowed_type = ["int", "char", "float"]
        if p[1].data["type"] in allowed_type and p[3].data["type"] in allowed_type:
            p[0].data = {"type" : "int"}
        else:
            report_error("Type not compatible with relational operation", p.lineno(0))
        x=operator(p[2].data,p[1],p[3],"int")
        p[0].place = x["place"]
        p[0].code = p[1].code + p[3].code + x["code"]

def p_shift_expression(p): 
    '''shift_expression : additive_expression 
                        | shift_expression LSHIFT additive_expression 
                        | shift_expression RSHIFT additive_expression 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    if len(p)==2:
        p[0].data = assigner(p,1)
        p[0].place = p[1].place
        p[0].code = p[1].code
    if len(p)==4:
        allowed_type = ["int"]
        if p[1].data["type"] in allowed_type and p[3].data["type"] in allowed_type:
            p[0].data = {"type" : "int"}
        else:
            report_error(" Type not compatible with bitwise shift operation ", p.lineno(0))

        p[0].place = getnewvar("int")
        p[0].code = p[1].code + p[3].code + [ quad(str(p[2].data),[p[0].place,p[1].place,p[3].place],p[0].place + " = " + p[1].place + str(p[2].data) + p[3].place) ]

def p_additive_expression(p): 
    '''additive_expression : multiplicative_expression 
                           | additive_expression PLUSOP multiplicative_expression 
                           | additive_expression MINUSOP multiplicative_expression 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    if len(p)==2:
        p[0].data = assigner(p,1)
        p[0].place = p[1].place
        p[0].code = p[1].code
    if len(p)==4:
        allowed_type = ["int", "char", "float"]
        if "|" in p[1].data["type"] and p[1].data["type"][-1] == "p" and p[3].data["type"] == "int":
            tmp = getnewvar("int")
            code = [ quad("*",[tmp,p[3].place,str(get_size(p[1].data["type"][:-1].rstrip("|")))],tmp + " = " + p[3].place + " * " +  str(get_size(p[1].data["type"][:-1].rstrip("|")))) ]  
            place = getnewvar(p[1].data["type"])
            code = code + [ quad("int" +p[2].data,[place,p[1].place,tmp],place + " = " + p[1].place + " int" + p[2].data + " " + tmp) ]
            p[0].place = place
            p[0].code = p[1].code + p[3].code + code
            p[0].data["type"] = p[1].data["type"]
            return

        if p[1].data["type"] not in allowed_type or p[3].data["type"] not in allowed_type:
            report_error("Type not compatible with plus , minus operation", p.lineno(0))
        x=operator(p[2].data,p[1],p[3])
        p[0].place = x["place"]
        p[0].code = p[1].code + p[3].code + x["code"]
        p[0].data["type"]=x["type"]

def p_multiplicative_expression(p): 
    '''multiplicative_expression : cast_expression 
                                 | multiplicative_expression MULTOP cast_expression 
                                 | multiplicative_expression DIVOP cast_expression 
                                 | multiplicative_expression MODOP cast_expression 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    if len(p)==2:
        p[0].data = assigner(p,1)
        p[0].place = p[1].place
        p[0].code = p[1].code
    if len(p)==4:
        allowed_type = ["int", "char", "float"]
        if p[1].data["type"] not in allowed_type or p[3].data["type"] not in allowed_type:
            report_error("Type not compatible with mult, div operation", p.lineno(0))
        x=operator(p[2].data,p[1],p[3])
        p[0].place = x["place"]
        p[0].code = p[1].code + p[3].code + x["code"]
        p[0].data["type"]=x["type"]

def p_cast_expression(p): 
    '''cast_expression : unary_expression 
                       | LPAREN type_name  RPAREN  cast_expression 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)  

    if len(p)==2 :
        p[0].data = assigner(p,1)
        p[0].place = p[1].place
        p[0].code = p[1].code
    if len(p)==5:
        rex = r'\|p*a+$'
        x= re.fullmatch(rex, p[2].data["type"])
        if x!=None or not allowed_type(p[4].data["type"], p[2].data["type"]):
            report_error("Type casting to "+p[2].data["type"]+" is not allowed",p.lineno(0))
        p[0].data = {}
        p[0].data["type"]=p[2].data["type"]
        p[0].place=getnewvar(p[0].data["type"])
        p[0].code=p[4].code+[ quad(p[4].data["type"]+"_to_"+p[2].data["type"],[p[0].place,p[4].place,""],p[0].place+"="+ p[4].data["type"]+"_to_"+p[2].data["type"]+"("+p[4].place+")") ]

    

def p_expression(p): 
    '''expression : assignment_expression 
                  | expression COMMA assignment_expression %prec LOWER
    ''' 
                #   | throw_expression
    p[0] = OBJ() 
    p[0].parse=f(p)
    if len(p)==2:
        p[0].data = assigner(p,1) 
        p[0].place = p[1].place
        p[0].code = p[1].code 
    else:
        p[0].place = p[1].place
        p[0].code = p[1].code + p[2].code

# def p_throw_expression(p): 
#     '''throw_expression : THROW expression 
#                         | THROW 
#     ''' 
#     p[0] = OBJ() 
#     p[0].parse=f(p)

def p_assignment_expression(p): 
    '''assignment_expression : conditional_expression 
                             | unary_expression assignment_operator assignment_expression 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    place = p[1].place

    if len(p)==2:
        p[0].data = assigner(p,1)
        p[0].place = p[1].place
        p[0].code = p[1].code.copy() 
    else:
        p[0].place = p[1].place
        if "class_u" in p[1].data.keys() and p[1].data["class_u"] == "unary1":
            report_error("can not assign some value to a unary expresion other than *", p.lineno(0))

        t=cast_string(p[3].place,p[3].data["type"],p[1].data["type"])
        if t==False:
            report_error("Can't assign "+p[3].data["type"]+" to "+p[1].data["type"],p.lineno(1))
        if p[2].data == "=":
            p[0].code = p[3].code + p[1].code + t["code"] +[ quad("eq",[place,t["place"]],place + "=" + t["place"]) ]
        else:
            p[0].code = p[3].code + p[1].code + t["code"]+[ quad(p[3].data["type"] + p[2].data[0],[place,place,t["place"]],place + " = " + place + " " + p[3].data["type"] + p[2].data[0] + " " + t["place"]) ]

def p_assignment_operator(p): 
    '''assignment_operator : EQUAL 
                           | MULTEQOP 
                           | DIVEQOP 
                           | MODEQOP 
                           | PLUSEQOP 
                           | MINUSEQOP 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data=p[1].data

def p_unary_expression_0(p): 
    '''unary_expression : postfix_expression  ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

    p[0].data = assigner(p,1)
    if("|" in p[0].data["type"] and p[0].data["type"][-1] == "a"):
        if p[0].data["type"][ : - len(p[0].data["meta"]) ].rstrip("|") == p[0].data["element_type"]:
            pass
        else:
            report_error("Array not called upto end", p.lineno(0))
    p[0].place = p[1].place
    p[0].code = p[1].code 
    

def p_unary_expression(p): 
    '''unary_expression : DPLUSOP unary_expression 
                        | DMINUSOP unary_expression 
                        | SIZEOF LPAREN type_name  RPAREN 
                        | allocation_expression 
                        | deallocation_expression 
    ''' 
                        # | SIZEOF  unary_expression 
    p[0] = OBJ() 
    p[0].parse=f(p)


    if len(p)==2:
        p[0].data = assigner(p,1)
        p[0].place = p[1].place
        p[0].code = p[1].code 
    elif len(p)==3:
        p[0].data=assigner(p,2)
        p[0].place=p[2].place
        if op_allowed(p[1].data[0],p[2].data["type"]):
            p[0].code=p[2].code + [ quad( p[1].data, [p[2].place] , p[2].place + p[1].data )]
        else:
            report_error("This unary operation is not allowed with given type", p.lineno(1))
    elif len(p)==5:
        p[0].data["type"]="int"
        p[0].place=getnewvar("int")
        p[0].code=p[3].code+[quad("eq",[p[0].place,str(get_size(p[3].data["type"])),""],p[0].place+"= "+str(get_size(p[3].data["type"])))]

def p_postfix_expression_1(p): 
    '''postfix_expression : primary_expression ''' 

    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data = assigner(p,1)
    p[0].place = p[1].place
    p[0].code = p[1].code.copy()


def p_postfix_expression_2(p): 
    '''postfix_expression : postfix_expression LSPAREN expression RSPAREN  ''' 

    p[0] = OBJ() 
    p[0].parse=f(p)

    if( p[3].data["type"] != "int" ):
        report_error("Array index is not integer", p.lineno(3))
    type_last_char = p[1].data["type"][-1]
    if "|" in p[1].data["type"] and  type_last_char == "a":
        p[0].data = p[1].data.copy()
        to_add_var = getnewvar("int")
        index = p[1].data["index"]
        to_mult =  p[1].data["meta"][index] if ( index < len(p[1].data["meta"]) ) else 1
        to_add_var_temp  = getnewvar("int")
        to_add = to_add_var_temp + " * " + str(to_mult)
        p[0].code = p[1].code + p[3].code  + [ quad("+",[to_add_var_temp,p[1].data["to_add"],p[3].place],to_add_var_temp + " = " + p[1].data["to_add"] + " + " + p[3].place ) ] \
             + [ quad("*",[to_add_var,to_add_var_temp,str(to_mult)],to_add_var +  " = " +  to_add) ]
        p[0].place = p[1].place
        p[0].data["type"] =  p[1].data["type"][:-1]
        p[0].data["index"] = p[1].data["index"] + 1
        p[0].data["to_add"] = to_add_var

        if(p[1].data["type"][-2] == "p") or (p[1].data["type"][-2] == "|") :
            # end of array
            p[0].data = {"type": p[1].data["type"][:-1].rstrip("|")}
            array_offset = p[1].data["offset"]
            array_offset_var = getnewvar("int")
            new_temp = getnewvar("int")
            new_offset = getnewvar("int")
            final_var = getnewvar(p[1].data["type"], new_offset ,  p[1].data["size"] )
            p[0].code = p[0].code + [ quad("*",[new_temp,to_add_var,str(get_size(p[0].data["type"]))],new_temp + " = " + to_add_var + " * " + str(get_size(p[0].data["type"]))) ]  \
                 + [quad("eq", [array_offset_var, str(array_offset) ] , array_offset_var + " = " + str(array_offset) )] \
                 + [ quad("-",[new_offset, array_offset_var ,new_temp],new_offset + " = " + array_offset_var + " - " + new_temp)] 
            p[0].place = final_var
       
    elif "|" in p[1].data["type"] and type_last_char == "p":
        # address mod
        if(p[1].data["type"][-2] == "|"):
            p[0].data = {"type": p[1].data["type"][:-2]}
        else:
            p[0].data = {"type": p[1].data["type"][:-1]}

        actual_addr = getnewvar(p[1].data["type"])
        p[0].place = getnewvar(p[0].data["type"], actual_addr, get_size(p[0].data["type"]), 0) 
        p[0].code = p[1].code +  p[3].code  + [ quad("+",[actual_addr,p[1].place,p[3].place], actual_addr + " = " + p[1].place + " + " +  p[3].place) ] 

    else:
        report_error("Not a array or pointer", p.lineno(0))

def p_postfix_expression_3(p): 
    '''postfix_expression : postfix_expression  LPAREN expression_list  RPAREN 
                          | postfix_expression LPAREN  RPAREN 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

    # this must be a function call
    # first get function sig..
    try:
        func_sig_list = p[1].data["func_sig"]
        func_name = p[1].data["func_name"]
        detail_scope = p[1].data["detail_scope"]
    except:
        report_error("Calling function on non function type", p.lineno(1))

    if len(p)==5:
        expected_sig = func_name + "|" + p[3].data["type"] 
        expr_code = p[3].code
    else:
        expected_sig = func_name + "|"
        expr_code = []

    func_detail = checkVar(expected_sig, detail_scope)
    
    flag=0
    for fun in func_sig_list:
        if fun[0]==expected_sig:
            p[0].data = {"type" : fun[1]}            
            flag=1

    if flag==0:
        report_error("Function not declared", p.lineno(1))

    class_name = "" if "class_name" not in p[1].data.keys() else p[1].data["class_name"]
    code = [ ]
    if isinstance(p[3].place, list):
        for each in p[3].place:
            code.append( quad("PushParam",[each,"",""],"PushParam " + each) )

    if "class_obj" in p[1].data.keys():
        code.append( quad("PushParam",[p[1].data["class_obj"],"",""],"PushParam " + p[1].data["class_obj"]) )

    p[0].place = getnewvar(p[0].data["type"])
    p[0].code = p[1].code + expr_code + code + [ quad("Fcall",[p[0].place,(class_name  + ":" if class_name != "" else "") + expected_sig,""],p[0].place + " = " + "Fcall " + (class_name  + ":" if class_name != "" else "") + expected_sig) ]
    pop_params_code = [ quad("removeParams", [ str(func_detail["parameter_space"]),"", ""], "RemoveParams " + str(func_detail["parameter_space"]) ) ]
    p[0].code = p[0].code +  pop_params_code

def p_postfix_expression_5(p): 
    '''postfix_expression : postfix_expression template_class_name  LPAREN expression_list  RPAREN   ''' 

    p[0] = OBJ() 
    p[0].parse=f(p)


def p_postfix_expression_6(p): 
    '''postfix_expression : postfix_expression DOT name  ''' 

    p[0] = OBJ() 
    p[0].parse=f(p)

    # post_fix must be a object and name should be a class member

    if "|" in p[1].data["type"]:
        report_error("request for member "+p[3].data+" in non-class type "+p[1].data["type"],p.lineno(0))

    details=checkVar(p[1].data["type"],"**")
    if details==False:
        report_error("request for member "+p[3].data+" in non-class type "+p[1].data["type"],p.lineno(0))
    if "class" in details["var"].keys() and details["var"]["class"]=="class":
        x=checkVar(p[3].data, details["var"]["scope"])
        if x!=False:
            p[0].data = x.copy()
            tmp_type = "int|p" if p[0].data["type"] == "function_upper" else p[0].data["type"] 
            if(p[0].data["type"] == "function_upper"):
                p[0].place = getnewvar(tmp_type)
                p[0].data["func_sig"] = x["func_sig"]
                p[0].data["detail_scope"] = details["var"]["scope"]
                p[0].data["func_name"] = p[3].data
                p[0].data["class_name"] = p[1].data["type"]
                p[0].data["class_obj"] = p[0].place 

                p[0].code = p[1].code + [ quad("load",[p[0].place,p[1].place,""],p[0].place + " = *(" +  p[1].place + ")") ]
            else:
                class_relative_offset = x["offset"]
                class_element_size = x["size"]
                to_check_var = p[1].place if p[1].place.split('@')[0]=="tmp" else p[1].place.split('@')[0]
                class_actual_offset = checkVar(to_check_var)["var"]["offset"]
                class_actual_base = checkVar(to_check_var)["var"]["base"]

                actual_offset = getnewvar("int|p")
            
                p[0].place = getnewvar(x["type"], actual_offset, class_element_size, class_actual_base)
                p[0].code = p[1].code + [ quad("+", [actual_offset, str(class_actual_offset), str(class_relative_offset) ] , actual_offset + " = " + str(class_actual_offset) + " + " + str(class_relative_offset)  ) ]

        else:
            report_error(p[3].data+" not in class "+p[1].data["type"], p.lineno(1))
    else:
        report_error(p[1].data["type"]+" is not a class",p.lineno(0))
    


def p_postfix_expression_7(p): 
    '''postfix_expression : postfix_expression ARROW name  ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
   

    if p[1].data["type"][-2:] != "|a" and p[1].data["type"][-2:] != "|p":
        report_error("request for member "+p[3].data+" in ptr to non-class type "+p[1].data["type"],p.lineno(0))

    details=checkVar(p[1].data["type"][:-2],"**")
    if details==False:
        report_error( p[3].data + " does not exist ",p.lineno(0))
    if "class" in details["var"].keys() and details["var"]["class"]=="class":
        x=checkVar(p[3].data, details["var"]["scope"])
        if x!=False:
            p[0].data=x.copy()
            tmp_type = "int|p" if p[0].data["type"] == "function_upper" else p[0].data["type"] 
            p[0].place = getnewvar(tmp_type)
            class_obj = getnewvar(details["var"]["type"])
            if(p[0].data["type"] == "function_upper"):
                p[0].data["func_sig"] = x["func_sig"]
                p[0].data["func_name"] = p[3].data
                p[0].data["detail_scope"] = details["var"]["scope"]
                p[0].data["class_name"] = p[1].data["type"][:-2]
                p[0].data["class_obj"] = class_obj
                p[0].code = p[1].code + [ quad("eq", [class_obj, p[1].place, ""], class_obj + " = " + p[1].place) ] 
            else:
                class_relative_offset = x["offset"]
                class_element_size = x["size"]
                
                class_actual_offset = p[1].place
                class_actual_base = 0
                actual_offset = getnewvar("int")
                p[0].place = getnewvar(x["type"], actual_offset, class_element_size, class_actual_base)
                p[0].code = p[1].code + [ quad("+", [actual_offset, str(class_actual_offset), str(class_relative_offset) ] , actual_offset + " = " + str(class_actual_offset) + " + " + str(class_relative_offset)  ) ]

        else:
            report_error(p[3].data+" not in class "+p[1].data["type"][:-2], p.lineno(1))
    else:
        report_error(p[1].data["type"][:-2] +" is not a class",p.lineno(0))
    # post_fix must be a object and name should be a class member

def p_postfix_expression_8(p): 
    '''postfix_expression : postfix_expression  DPLUSOP 
                          | postfix_expression  DMINUSOP 
    ''' 

    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data=assigner(p,1)
    p[0].place=getnewvar("int")
    if op_allowed(p[2].data[0],p[1].data["type"]):
        p[0].code=p[1].code + [ quad("eq", [ p[0].place, p[1].place ], p[0].place +  " =  " + p[1].place )] + [ quad( p[2].data, [p[1].place] , p[1].place + p[2].data )]
    else:
        report_error("This unary operation is not allowed with given type", p.lineno(1))
    p[0].data=assigner(p,1)

def p_primary_expression0(p): 
    '''primary_expression : name   
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p) 
    detail = checkVar(p[1].data)
    if detail ==  False:
        report_error( str(p[1].data) + " not declared" , p.lineno(1) )

    v_type = detail["var"]["type"]
    
    p[0].data = detail["var"].copy()
    
    if v_type=="function_upper":
        p[0].data["func_sig"] = detail["var"]["func_sig"]
        p[0].data["func_name"] = p[1].data
        p[0].data["detail_scope"] = detail["scope"]

    p[0].place = p[1].data + "@" + str(detail["scope"])
    p[0].code = [ "" ]

def p_primary_expression1(p): 
    ''' primary_expression : literal ''' 
    p[0] = OBJ() 
    p[0].parse=f(p) 
    p[0].data = assigner(p,1)
    p[0].place = getnewvar(p[0].data["type"])
    p[0].code = [ quad("eq" ,[p[0].place,str(p[1].data["value"]),""],p[0].place + " = " + str(p[1].data["value"])) ] 
    
    
def p_primary_expression2(p): 
    '''primary_expression : THIS  
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p) 

    detail = checkVar("this")
    if detail == False:
        report_error("wrong reference to THIS", p.lineno(0))

    p[0].data = detail["var"]
    p[0].place = "this"


def p_primary_expression3(p): 
    '''primary_expression : LPAREN expression  RPAREN   
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p) 
    p[0].data = {"type" : p[2].data["type"], "name" : None}
    p[0].place = p[2].place
    p[0].code = p[2].code


def p_unary_expression1(p): 
    '''unary_expression : unary1_operator cast_expression''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data = assigner(p,2)
    operator = ""
    if p[1].data == "&":
        if "|" in p[2].data["type"]:
            p[0].data["type"]=p[2].data["type"]+"p"
        else:
            p[0].data["type"]=p[2].data["type"]+"|p"

        p[0].place = getnewvar(p[0].data["type"])
        p[0].code = p[2].code + [ quad( "lea" , [p[0].place, p[2].place , ""], p[0].place + " = "+  p[1].data + " " + p[2].place ) ]    
    elif p[1].data in ["-", "+"] and p[2].data["type"] in ["int", "float"]:
        p[0].data["type"] = p[2].data["type"]
        if(p[1].data == "+") :
            p[0].code = p[2].code
            p[0].place = p[2].place
        else:
            p[0].place = getnewvar(p[2].data["type"])
            p[0].code = p[2].code + [ quad( "*", [ p[0].place, "-1" , p[2].place ] , p[0].place + " = " + " -1 * " + p[2].place  ) ] 

    elif p[1].data in ["!", "~"] and p[2].data["type"] in ["int"]:
        p[0].place = getnewvar(p[0].data["type"])
        p[0].code = p[2].code + [ quad( p[1].data , [p[0].place, p[2].place , ""], p[0].place + " = "+  p[1].data + " " + p[2].place ) ] 
    else:
        report_error("unary operation " + p[1].data + " is invalid with operand of type " + p[2].data["type"], p.lineno(0))

    
    p[0].data["class_u"] = "unary1"

def p_unary_expression2(p): 
    '''unary_expression : unary2_operator cast_expression 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
   
    if p[2].data["type"][-1] in ["a","p"]  and "|" in p[2].data["type"]:
        p[0].data["type"]=p[2].data["type"][:-1].rstrip("a").rstrip("|")
    else:
        report_error("Cannot dereference non-pointer element",p.lineno(0))
  
    p[0].place = getnewvar(p[0].data["type"], p[2].place , size = get_size(p[0].data["type"]), base = "0")

    p[0].code = p[2].code 
    p[0].data["class_u"] = "unary2"

def p_deallocation_expression(p): 
    '''deallocation_expression : DELETE IDENTIFIER
                              |  DELETE LSPAREN RSPAREN IDENTIFIER
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    if checkVar("dealloc|void|p","global")==False:
        report_error("STD lib not included", p.lineno(0))
    if(len(p) == 3):
        detail = checkVar(p[2].data)["var"]
        name = p[2].data
        if detail == False:
            report_error(p[2].data +" not defined", p.lineno(1))
        
    else:
        detail = checkVar(p[4].data)["var"]
        name = p[4].data
        if detail == False:
            report_error(p[2].data +" not defined", p.lineno(1))

    if "type" in detail.keys() and "|" in detail["type"] and detail["type"][-1] == "p":
        pass
    else:
        report_error("wrong specification of deallocate ", p.lineno(0))
    
    p[0].code = [ quad("PushParam", [name + "@" + str(currentScopeTable),"",""], "PushParam " + name + "@" + str(currentScopeTable)) ] + [quad("Fcall",["dealloc|void|p","",""],"Fcall dealloc|void|p")]
        
# New Allocation
# Extra * new_type_name me added hain
def p_allocation_expression1(p): 
    '''allocation_expression :  NEW LPAREN type_name RPAREN LSPAREN expression RSPAREN
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    if checkVar("alloc|int","global")==False:
        report_error("STD lib not included", p.lineno(0))
    if "|" in p[3].data["type"].rstrip("p").rstrip("|"):
        report_error("wrong type name for allocation", p.lineno(0))
    if "type" not in p[6].data.keys() or p[6].data["type"]!="int":
        report_error("Need int type for []", p.lineno(1))

    p[0].data["type"] = p[3].data["type"] + "p" if ("|" in p[3].data["type"]) else p[3].data["type"] + "|p"
    tpe = p[3].data["type"]
    tmp1 = getnewvar("int")
    p[0].place=getnewvar(p[0].data["type"])
    p[0].code = p[6].code + [quad("*",[tmp1,str(get_size(tpe)), p[6].place],tmp1 + " = " + str(get_size(tpe)) + "*" + p[6].place), quad("PushParam",[tmp1,"",""],"PushParam " + tmp1)  , quad("Fcall",["alloc|int",p[0].place],p[0].place + " = Fcall alloc|int")]


def p_allocation_expression0(p): 
    '''allocation_expression : NEW LPAREN type_name  RPAREN 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    if checkVar("alloc|int","global")==False:
        report_error("STD lib not included", p.lineno(0))
    if "|" in p[3].data["type"].rstrip("p").rstrip("|"):
        report_error("wrong type name for allocation", p.lineno(0))
    p[0].data = {"type" : p[3].data["type"] + "p"} if "|" in p[3].data["type"] else {"type" : p[3].data["type"] + "|p"}
    tpe = p[3].data["type"]
    p[0].place=getnewvar(p[0].data["type"])
    p[0].code = [quad("PushParam",[str(get_size(tpe)),"",""],"PushParam " + str(get_size(tpe))), quad("Fcall",["alloc|int",p[0].place],p[0].place + " = Fcall alloc|int") ]
    pop_params_code = [ quad("removeParams", [ str(4),"", ""], "RemoveParams " + str(4) ) ]
    p[0].code = p[0].code +  pop_params_code



def p_unary1_operator(p): 
    '''unary1_operator : PLUSOP 
                      | MINUSOP 
                      | NOTSYM 
                      | BNOP 
                      | BANDOP 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data = assigner(p,1)

def p_unary2_operator(p): 
    '''unary2_operator : MULTOP 
                     
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data = assigner(p,1)



def p_literal_string(p): 
    '''literal :  STRING_L ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data = {"type": "char|p", "value" : p[1].data, "name" : None}

def p_literal_number(p): 
    '''literal : NUMBER ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data = {"type": "int", "value" : p[1].data, "name" : None}

def p_literal_decimal(p): 
    '''literal : DECIMAL ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data = {"type": "float", "value" : p[1].data, "name" : None}

def p_literal_char(p): 
    '''literal : SCHAR ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data = {"type": "char", "value" : p[1].data, "name" : None}


# used for abstract declaration of func, int objstore_destroy(struct objfs_state*, char[]);
# input                 type                            meta
# **[][5]               ppaa                         ["*", "*", "", "5"]

def p_abstract_declarator(p): 
    '''abstract_declarator : unary2_operator %prec LOWER
                           | unary2_operator abstract_declarator %prec LOWER
                           | LSPAREN NUMBER RSPAREN %prec HIGHER
                           | abstract_declarator LSPAREN NUMBER RSPAREN %prec HIGHER
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    def ok(s):
        rex = r'^p*(r|a*)$'
        return re.fullmatch(rex, s)
    if len(p)==2:
        p[0].data = {"type" : "p"  , "meta" : [] }
    elif len(p)==4 and p[1].data=="[":
        p[0].data = {"type" : "a", "meta" : [p[2].data]}
    elif len(p)==3:
        p[0].data = {
            "type" : "p" + p[2].data["type"],
            "meta" :  p[2].data["meta"]
        }
    else:
        p[0].data = {
            "type" : p[1].data["type"]+"a",
            "meta" : p[1].data["meta"]+[p[3].data]
        }
    
    err=ok(p[0].data["type"])
    if err == None:
        report_error("Type declaration is wrong", p.lineno(1))

        
def p_declarator_0(p): 
    '''declarator : name ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data = {"name" : assigner(p,1), "type" : "", "meta" : []}
        
        
def p_declarator_1(p): 
    '''declarator : unary2_operator declarator %prec HIGHER  ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

    p[0].data = {
        "name" : p[2].data["name"], 
        "type" : "p" + p[2].data['type'],
        "meta" : p[2].data["meta"] 
    }

              
def p_declarator_2(p): 
    '''declarator :  declarator LSPAREN NUMBER RSPAREN 
                  |  declarator LSPAREN  RSPAREN  
     ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    if len(p) == 5:
        p[0].data = {
            "name" : p[1].data["name"], 
            "type" : p[1].data['type'] + "a",
            "meta" : p[1].data["meta"] + [p[3].data] 
        }
    else:
        if len(p[1].data["meta"]) != 0:
            report_error("can not left array size empty", p.lineno(1))
        p[0].data = {
            "name" : p[1].data["name"], 
            "type" : p[1].data['type'] + "a",
            "meta" : p[1].data["meta"] + [1] 
        }

            

def p_arg_list(p):
    ''' arg_list : argument_declaration_list 
                  |
    '''

    global currentScopeTable
    p[0] = OBJ() 
    p[0].parse=f(p)

    function_name = p[-2].data["name"]

    return_decl = p[-2].data["type"]
    if re.fullmatch( r'^p*$', return_decl) == None:
        report_error("Given return type not allowed for function", p.lineno(1) )

    if(p[-2].data["type"] == ""):
        return_sig = p[-3].data["type"] 
    else:
        return_sig = p[-3].data["type"] + "|" + p[-2].data["type"]

    add_this = False
    try:
        if str(p[-4])=="::":
            add_this = True
    except:
        pass

    offset = - 8
    if add_this:
        # for class function call
        class_name = p[-6]
        class_detail = checkVar(class_name)
        if class_detail == False:
            report_error("Class " + class_name + " does not exist", p.lineno(0) )
        if "class" in class_detail["var"].keys() and class_detail["var"]["class"] == "class":
            pass
        else:
            report_error( class_name + " is not a class, give a class name", p.lineno(0))
        this_data = {"class": "simple", "type" : class_detail["var"]["type"] + "|p", "name" : "this" }
        this_data["offset"] = offset
        this_data["base"] = "rbp"
        this_data["size"] = 4
        offset = offset - 4
        pushVar("this", this_data)

    if len(p)==2:
        input_detail=p[1].data
        for each_p in p[1].data[1]:
            if "is_array" in each_p.keys():    
                updateVar(each_p["name"],each_p)
                array_addr_temp = getnewvar("int", offset, 4)
                offset = offset - 4
                each_p["offset"] = array_addr_temp
                each_p["base"] = 0
                p[0].code = p[0].code 
            else:
                each_p["offset"] = offset
                offset = offset - each_p["size"]
                updateVar(each_p["name"],each_p)

    else:
        input_detail=("",[])

    p[0].data = {
        "name" : function_name,
        "return_sig" : return_sig,
        "input_sig" : input_detail[0],
        "body_scope" : currentScopeTable,
        "declaration": True,
        "stack_space" : get_offset(),
        "parameter_space": (- offset - 8 ),
        "saved_register_space" : 40 , # r12 -r15, rbx
        "return_offset" : 4,
        "rbp_offset" : 0
    }

    parent=getParentScope(currentScopeTable)
    func_sig = function_name +"|" + input_detail[0]

    if checkVar(function_name,parent) is False:
        # this function is not seen 
        pushVar(func_sig, p[0].data, scope = parent)
        pushVar(function_name, {"type" : "function_upper", "func_sig" : [ (func_sig, return_sig) ]} ,  scope = parent )
    else:
        # this name is seen but may be overloaded
        x=checkVar(function_name, parent)
        if "func_sig" not in x.keys():
            report_error("Already decleared as a non function type",p.lineno(0))
        if (func_sig, return_sig) in x["func_sig"] :
            func_detail = checkVar(func_sig, parent)
            if return_sig != func_detail["return_sig"]:
                report_error("Return Type differs from function declaration", p.lineno(0))
            if func_detail["declaration"] == False:
                # function of same sig has been defined
                report_error("Redeclaration of function", p.lineno(0))
            else:
                # function definition to be entered
                updateVar(func_sig, p[0].data, scope = parent)

        else:
            pushVar(func_sig, p[0].data, scope = parent)
            detail = checkVar(function_name, parent)
            updateVar(function_name, {"type" : "function_upper", "func_sig" : detail["func_sig"] + [(func_sig, return_sig)]}, scope = parent )

def p_argument_declaration_list(p): 
    '''argument_declaration_list : argument_declaration 
                                 | argument_declaration COMMA argument_declaration_list 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)  
    if(len(p) == 2 ):
        p[0].data = ( p[1].data["type"], [p[1].data])
    else:
        p[0].data = ( p[1].data["type"] +  ","  + p[3].data[0] , [ p[1].data ] + p[3].data[1] )

def p_argument_declaration_1(p): 
    '''argument_declaration : type_specifier_ declarator   ''' 
    p[0] = OBJ()
    p[0].parse=f(p)

    each = p[2].data.copy()
    data = p[1].data.copy()
    if(each["type"] != ""):
        data["type"] = p[1].data["type"] + "|" +  each["type"]
    data["name"] = each["name"]
    data["meta"] = each["meta"]
        
    # handle array type
    if len(data["meta"]) != 0:
        element_type = data["type"].rstrip("a").rstrip("|")
        if(element_type == "void"):
            report_error("can not declare a array of type void", p.lineno(0))
        data["is_array"] = 1
        data["element_type"] = element_type
        data["index"] = 1
        data["to_add"] = "0"

        size = 1
        for n in data["meta"]:
            size = size * n

        data["size"] = get_size(element_type) * size
        data["base"] = "rbp"

        # check the basic data_type_exist or not
        get_size(element_type.rstrip("p").rstrip("|"))
        if pushVar(data["name"],data)==False:
            report_error("Redeclaration of variable", p.lineno(1))
    else:
        if(data["type"] == "void"):
            report_error("can not declare a variable of type void", p.lineno(0))
        basic_type = data["type"].rstrip("p").rstrip("|")
        get_size(basic_type)

        data["size"] = get_size(data["type"])
        data["base"] = "rbp"

        if pushVar(each["name"],data)==False:
            report_error("Redeclaration of variable", p.lineno(1))
               
    p[0].data = data

def p_name(p): 
    '''name : IDENTIFIER 
            | DOUBLEBNOP IDENTIFIER 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data = p[1].data if len(p) == 2 else "~~" + p[2].data


def p_template_class_name(p): 
    '''template_class_name : LTEMPLATE template_arg_list RTEMPLATE''' 
    p[0] = OBJ()
    p[0].parse=f(p)
    p[0].data=assigner(p,2)

def p_template_arg_list(p): 
    '''template_arg_list : type_name 
                         | template_arg_list COMMA type_name
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    if len(p)==2:
        p[0].data=[assigner(p,1)]
    else:
        p[0].data=assigner(p,1)
        p[0].data.append(p[3].data)

# input -> [class, type, template, template_list, type, meta, const]
def p_type_name(p): 
    '''type_name : type_specifier_ abstract_declarator 
                 | type_specifier_ 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    if len(p)==3:
        p[0].data = assigner(p,1)
        p[0].data["type"] = p[0].data["type"] + "|" + p[2].data["type"]
        p[0].data["meta"] = p[2].data["meta"]
    else:
        p[0].data = assigner(p,1)
        p[0].data["meta"] = []

def p_type_specifier_(p): 
    '''type_specifier_ : CONST type_specifier 
                       | type_specifier
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)  
    if len(p)==3:
        p[0].data = assigner(p,2)
        # p[0].data["const"]=1
    else:
        p[0].data = assigner(p,1)
        # p[0].data["const"]=0

# def p_typedef_declarator(p):
#     '''typedef_declarator : TYPEDEF type_specifier_ abstract_declarator IDENTIFIER SEMICOLON
#                           | TYPEDEF type_specifier_  IDENTIFIER SEMICOLON
#     '''
#     p[0] = OBJ() 
#     p[0].parse=f(p)

def p_type_specifier(p): 
    '''type_specifier : simple_type_name 
                      | complex_type_specifier  
    ''' 

    p[0] = OBJ()
    p[0].parse=f(p)
    p[0].data = assigner(p,1)

def p_simple_type_name(p): 
    '''simple_type_name : CHAR 
                        | INT  
                        | FLOAT  
                        | VOID
    ''' 
    p[0] = OBJ()
    p[0].parse=f(p)   
    p[0].data = { "class" : "simple", "type": p[1].data }

# input                 class               type        template                    template_list
# class A<|int,char|>   "class"             A           1                           [int,char]             
def p_complex_type_specifier(p): 
    '''complex_type_specifier : class_key IDENTIFIER 
                                 
    ''' 
                                # | class_key  IDENTIFIER template_class_name
                                # | TYPE IDENTIFIER 
                                # | TYPE IDENTIFIER template_class_name

    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data = { "class":p[1].data,"type": p[2].data}
    if len(p)==4:
        p[0].data["class"]=p[0].data["class"]
        # p[0].data["template"]=1
        # p[0].data["template_list"]=p[3].data

def p_class_key(p): 
    '''class_key : CLASS 
                 | STRUCT
    ''' 
    p[0] = OBJ()
    p[0].parse = f(p) 
    p[0].data = "class"

def p_class_head(p): 
    '''class_head :  class_key IDENTIFIER 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data = {
        "class" : p[1].data,
        "type" : p[2].data,
    }

    pushVar(p[2].data + "@|@", "")

    pushOffset()

def p_class_function_specifier(p):
    ''' class_function_specifier : class_key IDENTIFIER change_scope DOUBLECOLON function_definition pop_scope '''
    p[0] = OBJ() 
    p[0].parse=f(p)

    p[0].code = p[5].code.copy()
    c = p[0].code[0].split("$")
    c[1] = p[2].data + ":" + c[1].strip()
    p[0].code[0] = " $ ".join(c)

    
def p_change_scope(p):
    ''' change_scope : '''
    class_name  = p[-1]
    p[0] = OBJ() 
    p[0].parse=f(p)

    class_detail = checkVar(class_name)
    if class_detail == False:
        report_error("Class " + class_name + " does not exist", p.lineno(0) )
    if "class" in class_detail["var"].keys() and class_detail["var"]["class"] == "class":
        pass
    else:
        report_error( class_name + " is not a class, give a class name", p.lineno(0))

    global currentScopeTable
    currentScopeTable = class_detail["var"]["scope"]
   


def p_class_define_specifier(p): 
    '''class_define_specifier : class_head push_class_scope LCPAREN member_list RCPAREN pop_scope ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data = assigner(p,1)
    p[0].data["scope"] = p[4].scope
    p[0].data["size"] = get_offset()

    if pushVar(p[0].data["type"], p[0].data)==False:
            report_error("Redeclaration of variable", p.lineno(1))

    p[0].code = []
    for each in p[4].code:
        if(len(each)) > 0:
            each[0] = p[0].data["type"] + ":" + each[0]
        p[0].code = p[0].code + each

    popOffset()
    

def p_member_list(p):
    '''member_list : member_access_list
    '''
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data = assigner(p,1)
    p[0].scope = currentScopeTable
    p[0].code = p[1].code.copy()


def p_member_access_list1(p):
    '''member_access_list : member_declaration member_access_list'''
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data = [assigner(p,1)] + assigner(p,2)
    p[0].code = [ p[1].code.copy() ] + p[2].code

def p_member_access_list2(p):
    '''member_access_list : member_declaration '''
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data = [assigner(p,1)]
    p[0].code = [ p[1].code.copy() ]  



def p_member_declaration_0(p):
    ''' member_declaration : type_specifier_ member_declarator_list SEMICOLON '''
    
    p[0] = OBJ()
    p[0].parse=f(p)
    decl_list = p[2].data
    p[0].data = {}
    for each in decl_list:
        data = p[1].data.copy()
        if(each["type"] != ""):
            data["type"] = p[1].data["type"] + "|" +  each["type"]
        data["name"] = each["name"]
        data["meta"] = each["meta"]
        
        # handle array type
        if len(data["meta"]) != 0:
            element_type = data["type"].rstrip("a").rstrip("|")
            if(element_type == "void"):
                report_error("can not declare a array of type void", p.lineno(0))
            data["is_array"] = 1
            data["element_type"] = element_type
            data["index"] = 1
            data["to_add"] = "0"

            size = 1
            for n in data["meta"]:
                size = size * n

            # check the basic data_type_exist or not
            if "|" in element_type:
                meta_ = checkVar(element_type.rstrip("p").rstrip("|") + "@|@")
                if  meta_ == False:
                    get_size(element_type.rstrip("p").rstrip("|"))
                else:
                    popVar(element_type.rstrip("p").rstrip("|") + "@|@" , meta_["scope"])
            else:
                get_size(element_type.rstrip("p").rstrip("|"))


            data["size"] = get_size(element_type, basic=False) * size
            add_to_offset(data["size"])
            data["offset"] = get_offset()
            data["base"] = "rbp"
            
            if pushVar(data["name"],data)==False:
                add_to_offset(-data["size"])
                report_error("Redeclaration of variable", p.lineno(1))
        else:
            if(data["type"] == "void"):
                report_error("can not declare a variable of type void", p.lineno(0))            
            
            basic_type = data["type"].rstrip("p").rstrip("|")
        
            # check the basic data_type_exist or not
            if "|" in data["type"]:
                meta_ = checkVar(basic_type + "@|@")
                if  meta_ == False:
                    get_size(basic_type)
                else:
                    popVar(basic_type+ "@|@" , meta_["scope"])
            else:
                get_size(basic_type)


            data["size"] = get_size(data["type"], basic = False)
            add_to_offset(data["size"])
            data["offset"] = get_offset()
            data["base"] = "rbp"
            
            if pushVar(each["name"],data)==False:
                report_error("Redeclaration of variable", p.lineno(1))
                    

def p_member_declaration_1(p):
    '''member_declaration :  function_decl 
    '''
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data = [assigner(p,1)]
    p[0].code = p[1].code.copy()



def p_member_declarator_list(p): 
    '''member_declarator_list : declarator 
                              | declarator COMMA member_declarator_list
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p) 
    if len(p)==4:
        p[0].data = [ p[1].data ] + p[3].data
    else:
        p[0].data = [ p[1].data ]


def p_function_definition(p): 
    '''function_definition : type_specifier_ declarator func_push_scope arg_list  RPAREN fct_body pop_scope 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    function_name = p[2].data["name"]
    func_sig = function_name +"|" + p[4].data["input_sig"]

        
    if p[4].data["return_sig"]=="void":
        if "ret_type" in p[6].data.keys() and p[6].data["ret_type"]!="":
            report_error("Return type is not same",p.lineno(0))
    elif "ret_type" in p[6].data.keys():
        if p[4].data["return_sig"]!=p[6].data["ret_type"]:
            report_error("Return type is not same",p.lineno(0))
    else:
        report_error("No return statement",p.lineno(0))
    func_detail = checkVar(func_sig, "*")
    func_detail['declaration'] = False
    func_detail["stack_space"] = get_offset()
    updateVar(func_sig, func_detail)    
    popOffset()
    p[0].code =[quad("label", [func_detail["name"] + "|" + func_detail["input_sig"], "", ""], func_detail["name"] + "|" + func_detail["input_sig"] + ":"), \
         quad("BeginFunc", [str(func_detail["stack_space"]), "", ""], "    BeginFunc " + str(func_detail["stack_space"]))] + p[4].code + \
             [ "    " + i for i in p[6].code] + [quad("EndFunc", ["","",""], "    EndFunc")]


def p_function_decl(p): 
    '''function_decl : type_specifier_ declarator func_push_scope arg_list  RPAREN SEMICOLON pop_scope ''' 
    p[0] = OBJ()
    p[0].parse=f(p)
    popOffset()


def p_func_push_scope(p):
    ''' func_push_scope : LPAREN '''
    global currentScopeTable 
    global scopeTableList
    if currentScopeTable == 0 or scopeTableList[currentScopeTable].type_ == "class" :
        pass
    else:
        report_error("Function can only be defined in global or class scope", p.lineno(0))

    pushScope()
    pushOffset()


def p_fct_body(p): 
    '''fct_body : compound_statement''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].code = p[1].code.copy()
    p[0].data=assigner(p,1)
    

def p_compound_statement(p): 
    '''compound_statement : LCPAREN statement_list RCPAREN 
                          | LCPAREN RCPAREN 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    if len(p) == 4:
        p[0].code = p[2].code
        p[0].place = p[2].place
        p[0].data=assigner(p,2)
    else:
        p[0].code = {}
        p[0].place = getnewvar("int")

def p_statement_list(p): 
    '''statement_list : statement 
                      | statement_list statement 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    if len(p) == 2:
        p[0].data=assigner(p,1)
        p[0].code = p[1].code
        p[0].place = p[1].place
    else:
        p[0].data = {}
        retType(p,1,2)
        p[0].code = p[1].code + p[2].code
        p[0].place = p[2].place


def p_statement(p): 
    '''statement : expression_statement 
                 | push_scope compound_statement pop_scope
                 | selection_statement 
                 | iteration_statement 
                 | jump_statement 
                 | declaration_statement 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    if len(p) == 2:
        p[0].data=assigner(p,1)
        p[0].code = p[1].code
        p[0].place = p[1].place
    else:
        p[0].data=assigner(p,2)
        p[0].code = p[2].code
        p[0].place = p[2].place

def p_jump_statement(p): 
    '''jump_statement : BREAK SEMICOLON 
                      | CONTINUE SEMICOLON 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].code = [p[1].data]

def p_jump_statement1(p):
    '''jump_statement : RETURN expression SEMICOLON 
                      | RETURN SEMICOLON 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    if len(p)==4:
        p[0].data["ret_type"]=p[2].data["type"]
        p[0].code=p[2].code+[quad("return", [p[2].place,"",""], "return "+p[2].place)]
    else:
        p[0].data["ret_type"]=""
        p[0].code=p[2].code+[quad("return", [], "return ")]

def p_selection_statement_1(p): 
    '''selection_statement : IF LPAREN expression  RPAREN push_scope compound_statement pop_scope  ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)  
    info = checkVar(p[3].place)["var"]
    if info["type"] != "int":
        report_error("only boolean and int allowed in if expr", p.lineno(0))
    p[0].after = getnewlabel("single_if_after")
    p[0].data=assigner(p,6)
    p[0].code = p[3].code + [quad("ifnz", [p[3].place, p[0].after, p[3].place, p[0].after, ""], "ifnz " + p[3].place + " goto->" + p[0].after)] + p[6].code +  [quad("label", [p[0].after], p[0].after + " : ")]

def p_selection_statement_2(p): 
    '''selection_statement : IF LPAREN expression  RPAREN push_scope compound_statement pop_scope ELSE push_scope compound_statement pop_scope  ''' 
    p[0] = OBJ() 
    p[0].parse=f(p) 

    info = checkVar(p[3].place)["var"]
    if info["type"] != "int":
        report_error("only boolean and int allowed in if expr", p.lineno(0))

    p[0].before = getnewlabel("ifelse_before")
    p[0].else_ = getnewlabel("ifelse_else_")
    p[0].after = getnewlabel("ifelse_after")
    retType(p,6,10)
    l = [quad("ifnz",[p[3].place,  p[0].else_, ""],"ifnz " + p[3].place + " goto->" + p[0].else_)] + p[6].code + [quad("goto", [p[0].after,"",""], "goto->" + p[0].after)]
    p[0].code = p[3].code + [quad("label",[p[0].before,"",""],p[0].before + ":")] + ["    " + i for i in l] + [quad("label", [p[0].else_,"",""], p[0].else_ + ":")] \
         + ["    " + i for i in p[10].code] + [quad("label",[p[0].after,"",""],p[0].after + ":")]

def p_selection_statement_3(p): 
    '''selection_statement :  SWITCH LPAREN expression  RPAREN push_scope  LCPAREN labeled_statement_list RCPAREN pop_scope ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data=assigner(p,7)

    if p[3].data["type"] not in ["int", "char"]:
        report_error("switch case variable should be one of int/char", p.lineno(1))
    if len(set([t["value"] for t in p[7].code])) != len(p[7].code):
        report_error("same value not allowed in 2 case clauses", p.lineno(1))
    p[0].test = getnewlabel("switch_test")
    p[0].next = getnewlabel("switch_body")
    p[0].after = getnewlabel("switch_end")
    nextcode = []
    testcode = []

    place = p[3].place
    if p[3].data["type"] == "char":
        tmp = getnewvar("int")
        p[0].code = [quad("char_to_int",[tmp, place, ""],tmp + " = " + place)]
        place = tmp
    default_label = p[0].after
    for idx,v in enumerate([t["value"] for t in p[7].code]):
        if v == None:
            default_label = p[7].code[idx]["label"]
            continue
        if p[7].code[idx]["type"] =="char":
            tmp3 = getnewvar("char")
            tmp = getnewvar("int")
            tmp2 = getnewvar("int")
            testcode = testcode + [quad("eq", [tmp3, str(v),""], tmp3+" = "+str(v))] + [quad("char_to_int",[tmp,tmp3,""],tmp+" = char_to_int "+tmp3)] \
                + [quad("-",[tmp2,place,tmp],tmp2+" = "+place+" - "+tmp), quad("ifz",[tmp2, p[7].code[idx]["label"],""],"ifz "+tmp2+" goto->"+p[7].code[idx]["label"])]
        else:
            tmp = getnewvar("int")
            tmp2 = getnewvar("int")
            testcode = testcode + [quad("eq", [tmp, str(v),""], tmp+" = "+str(v))] + [quad("-",[tmp2,place,tmp],tmp2+" = "+place+" - "+tmp), quad("ifz",[tmp2, p[7].code[idx]["label"],""],"ifz "+tmp2+" goto->"+p[7].code[idx]["label"])]
    testcode = testcode + [quad("goto",[default_label],"goto->" + default_label)]
    for idx,c in enumerate(p[7].code):
        l = c["statement"]
        l = break_continue(l, p[0].after)
        nextcode = nextcode + [quad("label",[c["label"],"",""], c["label"] + ":")] + ["    " + i for i in l] # + ["    goto->"+p[0].after]
    p[0].code = p[3].code + [quad("label", [p[0].test,"",""], p[0].test + ":")] + ["    " + i for i in testcode ] + [quad("label",[p[0].next, "",""],p[0].next + ":")] + ["    " + i for i in nextcode ] + [quad("label",[p[0].after,"",""],p[0].after + ":")]

# def p_try_block(p): 
#     '''try_block : TRY push_scope compound_statement pop_scope CATCH  push_scope compound_statement pop_scope''' 
#     p[0] = OBJ() 
#     p[0].parse=f(p)
#     p[0].data = {}
#     retType(p, 3, 7 )

def p_labeled_statement_list(p): 
    '''labeled_statement_list : labeled_statement
                              | labeled_statement_list labeled_statement 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    if len(p)==2:
        p[0].data=assigner(p,1)
        p[0].code = [p[1].code.copy()]
    else:
        p[0].data = {}
        retType(p,1,2)
        p[0].code = p[1].code + [p[2].code.copy()]

def p_labeled_statement(p): 
    '''labeled_statement : CASE NUMBER COLON statement_list
                         | CASE SCHAR COLON statement_list
                         | DEFAULT COLON statement_list
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    label = getnewlabel()
    if len(p)==5:
        p[0].code = {
            "class" : "case", 
            "type" : "int" if isinstance(p[2].parse[0], int) else "char",
            "value" : p[2].data,
            "statement" : p[4].code,
            "label" : label
        }
    else:
        p[0].data=assigner(p,3)
        p[0].code = {
            "class" : "default", 
            "type" : None, 
            "value" : None,
            "statement" : p[3].code,
            "label" : label
        }

def p_iteration_statement_1(p): 
    '''iteration_statement : WHILE push_scope LPAREN expression  RPAREN  compound_statement pop_scope ''' 
    p[0] = OBJ() 
    p[0].parse=f(p) 
    p[0].begin = getnewlabel("while_begin")
    p[0].after = getnewlabel("while_after")
    p[0].data=assigner(p,6)
    l = p[4].code + [ quad("ifz",[p[4].place,p[0].after],"ifz " + p[4].place + " goto->" + p[0].after) ] + p[6].code + [ quad("goto",[p[0].begin],"goto->" + p[0].begin) ]
    l = break_continue(l, p[0].after, p[0].begin)
    p[0].code =  [quad("label",[p[0].begin,"",""],p[0].begin + " : ")] + ["    " + i for i in l] + [ quad("label", [p[0].after], p[0].after + " : ") ]

def p_iteration_statement_2(p): 
    '''iteration_statement : DO push_scope compound_statement WHILE LPAREN expression  RPAREN  SEMICOLON pop_scope  ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data=assigner(p,3)
    p[0].begin = getnewlabel("do_begin")
    p[0].after = getnewlabel("do_after")
    l = p[3].code + p[6].code + [ quad("ifnz", [p[6].place, p[0].begin, ""], "ifnotz " + p[6].place + " goto->" + p[0].begin) ]
    l = break_continue(l, p[0].after, p[0].begin)
    p[0].code =  [quad("label",[p[0].begin,"",""],p[0].begin + " : ")] + ["    " + i for i in l] + [ quad("label", [p[0].after], p[0].after + " : ") ]

def p_iteration_statement_3(p): 
    '''iteration_statement : FOR LPAREN push_scope for_init_statement expression SEMICOLON expression  RPAREN  compound_statement pop_scope  ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data=assigner(p,9)
    p[0].begin = getnewlabel("for_begin1")
    p[0].cont = getnewlabel("for_continue1")
    p[0].after = getnewlabel("for_after1")
    l = p[5].code + [ quad("ifz",[p[5].place, p[0].after],"ifz " + p[5].place + " goto->" + p[0].after) ] + p[9].code + p[7].code + [quad("goto", [p[0].begin], "goto->" + p[0].begin) ]
    l = break_continue(l, p[0].after, p[0].cont)
    p[0].code = p[4].code + [quad("label",[p[0].begin,"",""],p[0].begin + " : ")] + ["    " + i for i in l[:len(p[5].code + [ quad("ifz",[p[5].place, p[0].after],"ifz " + p[5].place + " goto->" + p[0].after) ] + p[9].code)]] 
    p[0].code = p[0].code + [ quad("label", [p[0].cont], p[0].cont + " : ")] + ["    " + i for i in l[len(p[5].code + [ quad("ifz",[p[5].place, p[0].after],"ifz " + p[5].place + " goto->" + p[0].after) ] + p[9].code):]] 
    p[0].code = p[0].code + [ quad("label", [p[0].after], p[0].after + " : ") ]

def p_iteration_statement_4(p): 
    '''iteration_statement : FOR LPAREN push_scope for_init_statement SEMICOLON expression  RPAREN  compound_statement pop_scope   ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data=assigner(p,8)
    p[0].begin = getnewlabel("for_begin2")
    p[0].cont = getnewlabel("for_continue2")
    p[0].after = getnewlabel("for_after2")
    l = p[8].code + p[6].code + [quad("goto", [p[0].begin], "goto->" + p[0].begin) ]
    l = break_continue(l, p[0].after, p[0].cont)
    p[0].code = p[4].code + [quad("label",[p[0].begin,"",""],p[0].begin + " : ")] + ["    " + i for i in l[:len(p[8].code)]] \
        + [ quad("label", [p[0].after], p[0].after + " : ") ] + ["    " + i for i in l[len(p[8].code):]] \
        + [ quad("label", [p[0].after], p[0].after + " : ") ]

def p_iteration_statement_5(p): 
    '''iteration_statement :  FOR LPAREN push_scope for_init_statement expression SEMICOLON  RPAREN  compound_statement pop_scope  ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].begin = getnewlabel("for_begin3")
    p[0].cont = p[0].begin
    p[0].after = getnewlabel("for_after3")
    p[0].data=assigner(p,8)
    l = p[5].code + [ quad("ifz",[p[5].place, p[0].after],"ifz " + p[5].place + " goto->" + p[0].after) ] + p[8].code + [quad("goto", [p[0].begin], "goto->" + p[0].begin) ]
    l = break_continue(l, p[0].after, p[0].cont)
    p[0].code = p[4].code + [quad("label",[p[0].begin,"",""],p[0].begin + " : ")] + ["    " + i for i in l] + [ quad("label", [p[0].after], p[0].after + " : ") ]

def p_iteration_statement_6(p): 
    '''iteration_statement :  FOR LPAREN push_scope for_init_statement SEMICOLON  RPAREN  compound_statement pop_scope  ''' 
    p[0] = OBJ() 
    p[0].parse=f(p) 
    p[0].data=assigner(p,7)
    p[0].begin = getnewlabel("for_begin4")
    p[0].cont = p[0].begin
    p[0].after = getnewlabel("for_after4")
    l = p[7].code + [quad("goto", [p[0].begin], "goto->" + p[0].begin) ]
    l = break_continue(l, p[0].after, p[0].cont)
    p[0].code = p[4].code + [quad("label",[p[0].begin,"",""],p[0].begin + " : ")] + ["    " + i for i in l] + [ quad("label", [p[0].after], p[0].after + " : ") ]


def p_for_init_statement(p): 
    '''for_init_statement : expression_statement 
                          | declaration_statement 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].code=p[1].code.copy()
    p[0].place=p[1].place


def p_expression_statement(p): 
    '''expression_statement : expression SEMICOLON 
                            | SEMICOLON
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].place = p[1].place
    p[0].code = p[1].code.copy()
    if len(p)==2:
        p[0].data = {}
    else:
        p[0].data = assigner(p,1)

def p_declaration_statement(p): 
    '''declaration_statement : declaration''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].code=p[1].code.copy()
    p[0].data = assigner(p,1)


def p_declaration0(p):
    '''declaration : type_specifier_ declarator_list SEMICOLON ''' 
    global currentScopeTable
    p[0] = OBJ()
    p[0].parse=f(p)
    decl_list = p[2].data
    p[0].code=p[2].code.copy()
    p[0].data = {}
    for each in decl_list:
        data = p[1].data.copy()
        if(each["type"] != ""):
            data["type"] = p[1].data["type"] + "|" +  each["type"]
        data["name"] = each["name"]
        data["meta"] = each["meta"]
        
        # handle array type
        if len(data["meta"]) != 0:
            element_type = data["type"].rstrip("a").rstrip("|")
            if(element_type == "void"):
                report_error("can not declare a array of type void", p.lineno(0))
            data["is_array"] = 1
            data["element_type"] = element_type
            data["index"] = 1
            data["to_add"] = "0"

            size = 1
            for n in data["meta"]:
                size = size * n

            # check the basic data_type_exist or not
            get_size(element_type.rstrip("p").rstrip("|"))

            data["size"] = get_size(element_type) * size
            add_to_offset(data["size"])
            data["offset"] = get_offset()-data["size"] if (currentScopeTable==0) else get_offset() 
            data["base"] = "0" if (currentScopeTable==0) else  "rbp"
            if pushVar(data["name"],data)==False:
                add_to_offset(-data["size"])
                report_error("Redeclaration of variable", p.lineno(1))
        else:
            if(data["type"] == "void"):
                report_error("can not declare a variable of type void", p.lineno(0))
            basic_type = data["type"].rstrip("p").rstrip("|")
            get_size(basic_type)
            data["size"] = get_size(data["type"])
            add_to_offset(data["size"])
            data["offset"] = get_offset()-data["size"] if (currentScopeTable==0) else get_offset() 
            data["base"] = "0" if (currentScopeTable==0) else  "rbp"
            

            if pushVar(each["name"],data)==False:
                report_error("Redeclaration of variable", p.lineno(1))
            
            if "init_type" in each.keys():
                if  not allowed_type(each["init_type"],data["type"]):
                    report_error("type_mismatch in initialization", p.lineno(0))
                x=cast_string(each["place"],each["init_type"],data["type"])
                p[0].code=p[0].code + x["code"]+[ quad("eq",[each["name"]+ "@" + str(currentScopeTable), x["place"],""],each["name"]+ "@" + str(currentScopeTable) +" = "+ x["place"]) ]            




# def p_declaration1(p):
#     '''declaration :  asm_declaration  ''' 
        
#     p[0] = OBJ()
#     p[0].parse=f(p)


def p_declaration2(p):
    '''declaration :  function_definition 
                    | function_decl
    ''' 
    p[0] = OBJ()
    p[0].parse=f(p)
    p[0].code = p[1].code.copy()

def p_declaration3(p):
    '''declaration : class_define_specifier SEMICOLON ''' 
    p[0] = OBJ()
    p[0].parse=f(p)
    p[0].code = p[1].code.copy()


def p_declaration4(p):
    '''declaration :  class_function_specifier ''' 
    p[0] = OBJ()
    p[0].parse=f(p)
    p[0].code = p[1].code.copy()


# def p_declaration5(p):
#     '''declaration : typedef_declarator ''' 
#     p[0] = OBJ()
#     p[0].parse=f(p)

# def p_declaration6(p):
#     '''declaration :  template_declaration ''' 
#     p[0] = OBJ()
#     p[0].parse=f(p)

# def p_template_declaration(p): 
#     '''template_declaration : TEMPLATE LTEMPLATE template_argument_list RTEMPLATE declaration''' 
#     p[0] = OBJ() 
#     p[0].parse=f(p)

# def p_template_argument_list(p): 
#     '''template_argument_list : argument_declaration
#                               | template_argument_list COMMA argument_declaration
#     ''' 
#     p[0] = OBJ() 
#     p[0].parse=f(p)

def p_declarator_list(p): 
    '''declarator_list : init_declarator 
                       | declarator_list COMMA init_declarator 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

    if len(p) == 2 :
        p[0].data = [assigner(p,1)]
        p[0].code = p[1].code.copy()
        
    else:
        p[0].data = p[1].data + [ p[3].data ]
        p[0].code = p[1].code + p[3].code

def p_init_declarator(p): 
    '''init_declarator : declarator initializer 
                       | declarator 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data = assigner(p,1)
    if len(p) == 3:
        if len(p[0].data["meta"]) != 0:
            # its a array, can not be init
            report_error("Array can not be initialized while declaration", p.lineno(1))

        p[0].data["init_type"]=p[2].data["type"]
        p[0].data["place"] = p[2].place
        p[0].code = p[2].code.copy()

def p_initializer_1(p): 
    '''initializer :   EQUAL assignment_expression''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data=p[2].data.copy()
    p[0].place=p[2].place
    p[0].code=p[2].code.copy()


def p_expression_list(p): 
    '''expression_list : assignment_expression 
                       | expression_list COMMA assignment_expression 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p) 
    if len(p)==2:
        p[0].data = p[1].data.copy()
        p[0].place = [ p[1].place ] 
        p[0].code = p[1].code 
    else:
        p[0].data = {"type" : p[1].data["type"] + "," + p[3].data["type"]}
        p[0].place =  [ p[3].place ] +  p[1].place
        p[0].code = p[1].code + p[3].code

def p_push_scope(p):
    '''push_scope : '''
    pushScope()

def p_push_class_scope(p):
    '''push_class_scope : '''
    global currentScopeTable
    if currentScopeTable != 0:
        report_error("Class can only be defined in global scope", p.lineno(0))
    pushScope(type_ = "class")

def p_pop_scope(p):
    '''pop_scope : '''
    popScope()

def quad(op, a, statement):
    arg = [ a[i] if i<len(a) else "" for i in range(3) ]
    if op=="eq":
        if arg[0][0]=="*":
            op = "store"
            arg[0] = arg[0][1:].rstrip("(").lstrip(")")
        elif arg[1][0]=="*":
            op = "load"
            arg[1] = arg[1][1:].rstrip("(").lstrip(")")
        elif arg[1].isdigit():
            op = "=" 
        elif arg[1][0]=="'" and arg[1][2]=="'" and len(arg)==3:
            op = "="
        elif arg[1].isdecimal():
            op = "="
        elif arg[0].split('@')[0]=="tmp":
            c = checkVar(arg[0], "**")
            op = "=" # +("p" if "|" in  c["var"]["type"] else c["var"]["type"]) 
        else:
            c = checkVar(arg[0].split('@')[0], int(arg[0].split('@')[1]))
            op = "=" #+ ("p" if "|" in  c["type"] else c["type"]) 
    
    return " $ ".join([statement]+[op]+arg)

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

opr = []

def asm(ar):
    o = off(ar)
    return ' '.join(o) if o != [] else ''

def acode(ar):
    o = off(ar)
    return ' '.join(o) if o != [] else ''

def generate_code(p):
    afile = open(AddressFile,'w')
    cfile = open(CodeFile,'w')

    cod=[]
    for i in p[0].code:
        if re.fullmatch('[ ]*', i) == None:
            cod.append(i)

    cfile.write("//Code For " + FileName + "\n")
    x=1
    for i in cod:
        cfile.write('{0:3}'.format(x) + "::" + i.split('$')[0] + "\n")
        x=x+1

    x=1
    for i in cod:
        cfile.write('{0:3}'.format(x) + "::" + i + "\n")
        x=x+1

    f = open("code.obj", "wb")
    pickle.dump(cod,f)

    


def scope_table_graph(S):
    open('scope.gz','w').write("digraph ethane{ rankdir=LR {graph [ordering=\"out\"];node [fontsize=20 width=0.25 shape=box ]; ")
    cnt=0
    done = {}
    for s in S:
        if s.parent != None:
            label_child = pp.pformat(s.table)
            label_parent = pp.pformat(S[s.parent].table)
            if done.get(cnt, False)==False :
                done[cnt]=True
                sr = "\n" + str(cnt) + "[label=\"" + label_child + "\"]" + "\n"
                open('scope.gz', 'a').write(sr)
            if done.get(s.parent, False)==False :
                done[s.parent]=True
                sr = "\n" + str(s.parent) + "[label=\"" + label_parent + "\"]" + "\n"
                open('scope.gz', 'a').write(sr)
            sr = "\n" + str(s.parent) + " -> " + str(cnt) + "\n"
            open('scope.gz', 'a').write(sr)
        cnt=cnt+1
    open('scope.gz','a').write("\n}\n}\n")
def file_len(fname):
    with open(fname) as f:
        i=-1
        for i, l in enumerate(f):
            pass
    return i + 1
if __name__ == "__main__": 
    parser = yacc.yacc()
    parser.error = 0 

    if(len(sys.argv) != 4): 
        print("Usage python3 parser.py Inputfile OutputFile SymbolTableFile given #args : ", len(sys.argv) , sys.argv) 
        exit() 

    arglist = sys.argv 
    FileName = arglist[1]
    CodeFile = arglist[2]
    file1 = os.path.join(os.getcwd(), FileName)
    x=os.path.dirname(file1)
    fin = open(FileName, "r")
    data2 = fin.read()
    fin.close()
    if("#include<std.cpp>"==data2[:17]):
        error_line_offset=file_len("std.cpp")+1
        fout = open("temp.cpp", "w")
        fin = open("std.cpp", "r")
        fout.write("int heap_ptr;\n")
        fout.write(fin.read())
        fin.close()
        fout.write(data2[17:])
        fout.close()
        FileName="temp.cpp"
    else:
        fout = open("temp.cpp", "w")
        fout.write("int heap_ptr;\n")
        fout.write(data2)
        fout.close()
        FileName="temp.cpp"
    SymbolTableFileName = arglist[3]
    debug=0
    # debug = int(arglist[1])
    # filename = arglist[2]
    open('dot.gz','w').write("digraph ethane {graph [ordering=\"out\"];")
    file_o = open(FileName,'r').read()
    p = parser.parse(file_o,lexer = lexer,debug=debug,tracking=True)  
    open('dot.gz','a').write("\n}\n")
    scope_table_graph(scopeTableList)
    f = open(SymbolTableFileName, "w")
    ignore_key = ["is_array", "element_type", "index", "to_add"]
    for idx, table in  enumerate( scopeTableList):
        f.write("SCOPE START :: " + str(idx) + "\n")
        for key in table.table.keys():
            f.write("    " + str(key) + " , " )
            detail = table.table[key]
            if isinstance(detail,dict):
                for elem_key in detail.keys():
                    if elem_key not in ignore_key:
                        f.write("{ " + str(elem_key) + " : " + str(detail[elem_key]) + " } , " )
            f.write("\n")
        f.write("SCOPE END :: " + str(idx) + "\n\n")

    f.write("\n")
    f.write("SCOPE SCOPE RELATION ::  SCOPE NUMBER : PARENT NUMBER\n")
    for idx, table in  enumerate( scopeTableList):
        f.write("                       " + "        " + str(idx) + "             " +  str(table.parent) + "\n" )
    
    f = open("sym_table.obj", "wb")
    pickle.dump(scopeTableList,f)