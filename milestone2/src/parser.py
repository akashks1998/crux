import pprint
from ply import yacc
import os
import sys
import time
from lexer import lexer
from lexer import tokens as lexTokens
from symbolTable import SymbolTable
import re

cnt=0
tokens = lexTokens
filename=""
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
        

scopeTableList = []
globalScopeTable = SymbolTable()
scopeTableList.append(globalScopeTable)

currentScopeTable = 0

class OBJ:
    data = None
    pass

def pushScope():
    global scopeTableList
    global currentScopeTable
    newScope = SymbolTable(parent=currentScopeTable)
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
    
    

def updateVar(identifier, val,scope):
    global scopeTableList
    global currentScopeTable
    scopeTableList[scope].update(identifier, val)
    

def checkVar(identifier,scopeId):
    global scopeTableList
    global currentScopeTable
    if scopeId == "global":
        if scopeTableList[0].lookUp(identifier):
            return scopeTableList[0].getDetail(identifier)
        return False

    if scopeId == "*":
        if scopeTableList[currentScopeTable].lookUp(identifier):
            return scopeTableList[currentScopeTable].getDetail(identifier)
        return False
    if scopeId=="**":
        scope=currentScopeTable

        while scope!=None:
            if scopeTableList[scope].lookUp(identifier):
                return {"var":scopeTableList[scope].getDetail(identifier), "scope":scope}
            scope=scopeTableList[scope].parent
        return False
    else:
        if scopeTableList[scopeId].lookUp(identifier):
            return scopeTableList[scopeId].getDetail(identifier)
        return False

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

def p_control_line(p):
    '''control_line : control_line control_line_stmt
                    | control_line_stmt
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)    

def p_include_control(p):
    '''include_control : HASHTAG INCLUDE
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_control_line_stmt(p):
    '''control_line_stmt : include_control LTCOMP STRING_L GTCOMP
                    | include_control STRING_L
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_program(p):
    '''program : control_line translation_unit
               | translation_unit
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_translation_unit(p):
    '''translation_unit : declaration_seq''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_declaration_seq(p):
    ''' declaration_seq : declaration_seq declaration
                        | declaration
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_error(p):
    print("Error: Line " + str(p.lineno) + ":" + filename.split('/')[-1])
    exit()

def p_empty(p): 
    'empty :' 
    p[0]=OBJ()
    p[0].data=None

def p_constant_expression(p): 
    '''constant_expression : conditional_expression''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    

def p_conditional_expression(p): 
    '''conditional_expression : logical_OR_expression 
                              | logical_OR_expression QUESMARK expression COLON conditional_expression 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_logical_OR_expression(p): 
    '''logical_OR_expression : logical_AND_expression 
                             | logical_OR_expression OROP logical_AND_expression 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_logical_AND_expression(p): 
    '''logical_AND_expression : inclusive_OR_expression %prec LOWER
                              | logical_AND_expression ANDOP inclusive_OR_expression %prec HIGHER
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_inclusive_OR_expression(p): 
    '''inclusive_OR_expression : exclusive_OR_expression %prec LOWER
                               | inclusive_OR_expression OROP exclusive_OR_expression %prec HIGHER
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_exclusive_OR_expression(p): 
    '''exclusive_OR_expression : AND_expression 
                               | exclusive_OR_expression XOROP AND_expression 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_AND_expression(p): 
    '''AND_expression : equality_expression 
                      | AND_expression BANDOP equality_expression 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_equality_expression(p): 
    '''equality_expression : relational_expression 
                           | equality_expression EQCOMP relational_expression 
                           | equality_expression NEQCOMP relational_expression 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_relational_expression(p): 
    '''relational_expression : shift_expression 
                             | relational_expression LTCOMP  shift_expression 
                             | relational_expression GTCOMP  shift_expression 
                             | relational_expression LTECOMP shift_expression 
                             | relational_expression GTECOMP shift_expression 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_shift_expression(p): 
    '''shift_expression : additive_expression 
                        | shift_expression LSHIFT additive_expression 
                        | shift_expression RSHIFT additive_expression 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_additive_expression(p): 
    '''additive_expression : multiplicative_expression 
                           | additive_expression PLUSOP multiplicative_expression 
                           | additive_expression MINUSOP multiplicative_expression 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_multiplicative_expression(p): 
    '''multiplicative_expression : pm_expression 
                                 | multiplicative_expression MULTOP pm_expression 
                                 | multiplicative_expression DIVOP pm_expression 
                                 | multiplicative_expression MODOP pm_expression 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_pm_expression(p): 
    '''pm_expression : cast_expression 
                     | pm_expression DOTSTAR cast_expression 
                     | pm_expression ARROWSTAR cast_expression 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_expression(p): 
    '''expression : assignment_expression 
                  | throw_expression
                  | expression COMMA assignment_expression 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_throw_expression(p): 
    '''throw_expression : THROW expression 
                        | THROW 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_assignment_expression(p): 
    '''assignment_expression : conditional_expression 
                             | unary_expression  assignment_operator assignment_expression 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_assignment_operator(p): 
    '''assignment_operator : EQUAL 
                           | MULTEQOP 
                           | DIVEQOP 
                           | MODEQOP 
                           | PLUSEQOP 
                           | MINUSEQOP 
                           | LSHIFTEQOP 
                           | RSHIFTEQOP 
                           | BANDEQOP 
                           | BOREQOP 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_unary_expression(p): 
    '''unary_expression : postfix_expression 
                        | DPLUSOP unary_expression 
                        | DMINUSOP unary_expression 
                        | unary1_operator cast_expression 
                        | unary2_operator cast_expression 
                        | SIZEOF  unary_expression 
                        | SIZEOF LPAREN type_name  RPAREN 
                        | allocation_expression 
                        | deallocation_expression 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_deallocation_expression(p): 
    '''deallocation_expression : DELETE cast_expression  ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

# New Allocation

def p_allocation_expression(p): 
    '''allocation_expression : NEW new_type_name new_initializer 
                             | NEW new_type_name 
                             | NEW LPAREN type_name  RPAREN  new_initializer 
                             | NEW LPAREN type_name  RPAREN 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_new_type_name(p): 
    '''new_type_name : type_specifier_ new_declarator 
                     | type_specifier_ 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_new_declarator(p): 
    '''new_declarator : new_declarator MULTOP
                      | MULTOP 
                      | new_declarator LSPAREN expression RSPAREN 
                      | LSPAREN expression RSPAREN 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_new_initializer(p): 
    '''new_initializer : LPAREN initializer_list  RPAREN 
                       | LPAREN  RPAREN 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_unary1_operator(p): 
    '''unary1_operator : PLUSOP 
                      | MINUSOP 
                      | NOTSYM 
                      | BNOP 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data = p[1].data

def p_unary2_operator(p): 
    '''unary2_operator : MULTOP 
                      | BANDOP 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data = p[1].data

def p_postfix_expression(p): 
    '''postfix_expression : primary_expression 
                          | postfix_expression     LSPAREN expression RSPAREN 
                          | postfix_expression     LPAREN expression_list  RPAREN  
                          | postfix_expression template_class_name  LPAREN expression_list  RPAREN 
                          | postfix_expression     LPAREN  RPAREN 
                          | postfix_expression     DOT name 
                          | postfix_expression     ARROW name 
                          | postfix_expression     DPLUSOP 
                          | postfix_expression     DMINUSOP 
    ''' 

                        #   | simple_type_name       LPAREN expression_list  RPAREN 
                        #   | simple_type_name       LPAREN  RPAREN 
    p[0] = OBJ() 
    p[0].parse=f(p)



def p_primary_expression0(p): 
    '''primary_expression : name   
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p) 
    # p[0].data = {"type" : p[1].data["type"]}

def p_primary_expression1(p): 
    '''primary_expression : literal           
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p) 
    # p[0].data = {"type" : p[1].data["type"]}

    
def p_primary_expression2(p): 
    '''primary_expression : THIS  
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p) 
    
    # p[0].data = {"type" : "class"} # use symbol table to determine


def p_primary_expression3(p): 
    '''primary_expression : LPAREN expression  RPAREN   
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p) 
    # p[0].data = {"type" : p[2].data["type"]}


   

def p_literal_string(p): 
    '''literal :  STRING_L ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data = {"type": "string", "value" : p[1].data}

def p_literal_number(p): 
    '''literal : NUMBER ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data = {"type": "number", "value" : p[1].data}

def p_literal_char(p): 
    '''literal : SCHAR ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data = {"type": "char", "value" : p[1].data}

def p_cast_expression(p): 
    '''cast_expression : unary_expression 
                       | LPAREN type_name  RPAREN  cast_expression 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)    

# used for abstract declaration of func, int objstore_destroy(struct objfs_state*, char[]);
# input                 abstract_class               abstract_type
# **[][5]               ppaA                         ["*", "*", "", "5"]
def p_abstract_declarator(p): 
    '''abstract_declarator : unary2_operator %prec LOWER
                           | unary2_operator abstract_declarator %prec LOWER
                           | LSPAREN constant_expression RSPAREN %prec HIGHER
                           | abstract_declarator LSPAREN constant_expression RSPAREN %prec HIGHER
                           | LSPAREN  RSPAREN %prec HIGHER
                           | abstract_declarator LSPAREN RSPAREN %prec HIGHER
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    def ok(s):
        rex = r'^p*(r|[aA]*)$'
        return re.fullmatch(rex, s)
    if len(p)==2:
        p[0].data = {"abstract_class" : "p" if (p[1].data == "*") else "r" , "abstract_type" : [p[1].data]}
    elif len(p)==3 and p[1].data=="[":
        p[0].data = {"abstract_class" : "a" , "abstract_type" : [""]}
    elif len(p)==4 and p[1].data=="[":
        p[0].data = {"abstract_class" : "A", "abstract_type" : [p[2].data]}
    elif len(p)==3:
        p[0].data = {
            "abstract_class" : ("p" if (p[1].data == "*") else "r") + p[2].data['abstract_class'],
            "abstract_type" : [p[1].data] + p[2].data["abstract_type"]
        }
    elif len(p)==4:
        p[0].data = {
            "abstract_class" : p[1].data["abstract_class"]+"a",
            "abstract_type" : p[1].data["abstract_type"]+[""]
        }
    else:
        p[0].data = {
            "abstract_class" : p[1].data["abstract_class"]+"A",
            "abstract_type" : p[1].data["abstract_type"]+[p[3].data]
        }
    err=ok(p[0].data["abstract_class"])
    if err == None:
        print("Syntax Error",p.lineno(1))
        exit()

        
def p_declarator0(p): 
    '''declarator : name ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data = {"name" : p[1].data, "type" : "", "meta" : []}
        
        
def p_declarator1(p): 
    '''declarator : unary2_operator declarator %prec HIGHER  ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

    p[0].data = {
        "name" : p[2].data["name"], 
        "type" : ("p" if (p[1].data == "*") else "r") + p[2].data['type'],
        "meta" : [p[1].data] + p[2].data["meta"] 
    }

        

   
        
def p_declarator3(p): 
    '''declarator :  declarator LSPAREN constant_expression RSPAREN  ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data = {
        "name" : p[1].data["name"], 
        "type" : p[1].data['type'] + "a",
        "meta" : p[1].data["meta"] + [p[3].data] 
    }
        
        
def p_declarator4(p): 
    '''declarator : declarator LSPAREN RSPAREN  ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data = {
        "name" : p[1].data["name"], 
        "type" : p[1].data['type'] + "a",
        "meta" : p[1].data["meta"] + [""] 
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
        print("Error: given return type not allowed at line " + str(p.lineno(1)))
        exit()
    
    return_sig = p[-3].data["type"] + "|" + return_decl
    
    if len(p)==2:
        temp=p[1].data
    else:
        temp=("",[])
    input_sig = temp
    p[0].data = {
        "name" : function_name,
        "return_sig" : return_sig,
        "input" : input_sig,
        "body_scope" : currentScopeTable,
        "declaration": True,
        "string" :  temp[0]
    }
    parent=getParentScope(currentScopeTable)
    func_sig = function_name +"|" + temp[0]
    print("sd", func_sig)
    if checkVar(function_name,parent) is False:
        # this function is not seen 
        pushVar(func_sig, p[0].data, scope = parent)
        pushVar(function_name, [func_sig], scope = parent )
    else:
        # this name is seen but may be overloaded
        if func_sig in checkVar(function_name, parent) :
            func_detail = checkVar(func_sig, parent)
            if return_sig != func_detail["return_sig"]:
                print("Error: " + str(p.lineno(1)) + ": Return type of function "+function_name+" is not correct")
                exit()

            if func_detail["declaration"] == False:
                # function of same sig has been defined
                print("Error: " + str(p.lineno(1)) + ": Redeclaration of function "+ function_name)
                exit()
            else:
                # function definition to be entered
                updateVar(func_sig, p[0].data, scope = parent)

        else:
            pushVar(func_sig, p[0].data, scope = parent)
            updateVar(function_name, checkVar(function_name, parent) + [func_sig], scope = parent )



    


def p_argument_declaration_list(p): 
    '''argument_declaration_list : argument_declaration 
                                 | argument_declaration COMMA argument_declaration_list
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)  
    if(len(p) == 2 ):
        p[0].data = ( p[1].data["string"], [p[1].data])
    else:
        p[0].data = ( p[1].data["string"] + p[3].data[0] , [ p[1].data ] + p[3].data[1] )

def p_argument_declaration_1(p): 
    '''argument_declaration : type_specifier_ declarator   ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    type_info = {"specifier" : p[1].data, "declarator" : p[2].data }
    type_string = p[1].data["type"] + "|" + p[2].data["type"]
    p[0].data = {"name" : p[2].data["name"], "type" : type_info  , "init" : None, "string": type_string  }
    if pushVar(p[2].data["name"],p[0].data)==False:
        print("Error:"+ str(p.lineno(1))+" redeclaration of variable")
        exit()


def p_argument_declaration_2(p): 
    '''argument_declaration :  type_specifier_ declarator  EQUAL expression ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    type_info = {"specifier" : p[1].data, "declarator" : p[2].data }
    type_string = p[1].data["type"] + "|" + p[2].data["type"]
    p[0].data = {"name" : p[2].data["name"], "type" : type_info  , "init" : p[4], "string":type_string }


# these two can be removed, will be handled later if time permits
def p_argument_declaration_3(p): 
    '''argument_declaration : type_specifier_ abstract_declarator ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    # p[0].data = {"name" : , "type" : "meta": [] , "init" : }


def p_argument_declaration_4(p): 
    '''argument_declaration :  type_specifier_ ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    # p[0].data = {"name" : , "type" : "meta": [] , "init" : }


def p_name(p): 
    '''name : IDENTIFIER 
            | DOUBLEBNOP IDENTIFIER 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data = p[1].data if len(p) == 2 else "~~" + p[2].data



def p_operator_name(p): 
    '''operator_name : NEW 
                     | DELETE 
                     | PLUSOP 
                     | MINUSOP 
                     | MULTOP 
                     | DIVOP 
                     | MODOP 
                     | XOROP 
                     | BANDOP 
                     | BNOP 
                     | NOTSYM 
                     | EQUAL 
                     | LTCOMP 
                     | GTCOMP 
                     | PLUSEQOP 
                     | MINUSEQOP 
                     | MULTEQOP 
                     | DIVEQOP 
                     | MODEQOP 
                     | XOREQOP 
                     | BANDEQOP 
                     | LSHIFT 
                     | RSHIFT 
                     | RSHIFTEQOP 
                     | LSHIFTEQOP 
                     | EQCOMP 
                     | NEQCOMP 
                     | LTECOMP 
                     | GTECOMP 
                     | ANDOP 
                     | OROP 
                     | DPLUSOP 
                     | DMINUSOP 
                     | COMMA 
                     | ARROWSTAR 
                     | ARROW 
    ''' 
                    #  | LPAREN  RPAREN 
                    #  | LSPAREN RSPAREN 
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data = p[1].data

def p_template_class_name(p): 
    '''template_class_name : LTEMPLATE template_arg_list RTEMPLATE''' 
    p[0] = OBJ()
    p[0].parse=f(p)
    p[0].data=p[2].data

def p_template_arg_list(p): 
    '''template_arg_list : type_name 
                         | template_arg_list COMMA type_name
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    if len(p)==2:
        p[0].data=[p[1].data]
    else:
        p[0].data=p[1].data
        p[0].data.append(p[3].data)

# input -> [class, type, template, template_list, abstract_class, abstract_type, const]
def p_type_name(p): 
    '''type_name : type_specifier_ abstract_declarator 
                 | type_specifier_ 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    if len(p)==3:
        p[0].data = {**p[1].data, **p[2].data}
    else:
        p[0].data = p[1].data
        

def p_type_specifier_(p): 
    '''type_specifier_ : CONST type_specifier 
                       | type_specifier
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)  
    if len(p)==3:
        p[0].data = p[2].data
        p[0].data["const"]=1
    else:
        p[0].data = p[1].data
        p[0].data["const"]=0

def p_typedef_declarator(p):
    '''typedef_declarator : TYPEDEF type_specifier_ abstract_declarator IDENTIFIER SEMICOLON
                          | TYPEDEF type_specifier_  IDENTIFIER SEMICOLON
    '''
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_type_specifier(p): 
    '''type_specifier : simple_type_name 
                      | complex_type_specifier  
    ''' 
                    #   | class_define_specifier 
    p[0] = OBJ()
    p[0].parse=f(p)   
    p[0].data=p[1].data

def p_simple_type_name(p): 
    '''simple_type_name : CHAR 
                        | SHORT 
                        | INT 
                        | LONG 
                        | SIGNED 
                        | UNSIGNED 
                        | FLOAT 
                        | DOUBLE 
                        | VOID
                        | STRING
                        | AUTO

    ''' 
    p[0] = OBJ()
    p[0].parse=f(p)   
    p[0].data = { "class" : "simple","type": p[1].data, "template" : 0, "template_list": None }

# input                 class               type        template                    template_list
# class A<|int,char|>   "class"             A           1                           [int,char]             
def p_complex_type_specifier(p): 
    '''complex_type_specifier : class_key IDENTIFIER 
                                | class_key  IDENTIFIER template_class_name
                                | TYPE IDENTIFIER 
                                | TYPE IDENTIFIER template_class_name
                                 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
    p[0].data = { "class":p[1].data,"type": p[2].data, "template" : 0, "template_list": None}
    if len(p)==4:
        p[0].data["class"]=p[0].data["class"]
        p[0].data["template"]=1
        p[0].data["template_list"]=p[3].data

def p_pure_specifier(p): 
    '''pure_specifier :   EQUAL NUMBER''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_class_head(p): 
    '''class_head : class_key IDENTIFIER base_spec 
                  | class_key IDENTIFIER 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

# use for class inhertance

def p_base_spec(p): 
    '''base_spec : COLON base_list''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_base_list(p): 
    '''base_list : base_specifier
                 | base_list COMMA base_specifier 
    ''' 

    p[0] = OBJ() 
    p[0].parse=f(p)

def p_base_specifier(p): 
    '''base_specifier : class_key  IDENTIFIER 
                      | class_key  IDENTIFIER template_class_name
                      | IDENTIFIER 
                      | IDENTIFIER template_class_name
                      | access_specifier class_key IDENTIFIER
                      | access_specifier class_key IDENTIFIER template_class_name
    '''
                    #   | access_specifier  IDENTIFIER
                    #   | access_specifier  IDENTIFIER template_class_name 
 
    p[0] = OBJ() 
    p[0].parse=f(p) 

def p_class_key(p): 
    '''class_key : CLASS 
                 | STRUCT
    ''' 
    p[0] = OBJ()
    p[0].parse = f(p) 
    p[0].data = p[1].data

def p_class_define_specifier(p): 
    '''class_define_specifier : class_head LCPAREN member_list RCPAREN 
                       | class_head LCPAREN RCPAREN 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
 

def p_member_list(p):
    '''member_list : member_access_list
                   | access_list
                   | member_list access_list
    '''
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_access_specifier(p):
    '''access_specifier : PRIVATE
                        | PROTECTED
                        | PUBLIC
    '''
    p[0] = OBJ()    
    p[0].parse=f(p)

def p_access_list(p):
    '''access_list : access_specifier COLON member_access_list
                   | access_specifier COLON '''
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_member_access_list(p):
    '''member_access_list : member_declaration member_access_list
                          | member_declaration '''
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_member_declaration(p):
    '''member_declaration : type_specifier_ member_declarator_list SEMICOLON
                          | member_declarator_list SEMICOLON
                          | type_specifier_ SEMICOLON
                          | SEMICOLON
                          | function_definition
                          |  class_define_specifier SEMICOLON
    '''
                        #   | function_definition SEMICOLON
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_member_declarator_list(p): 
    '''member_declarator_list : member_declarator 
                              | member_declarator_list COMMA member_declarator 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p) 

def p_member_declarator(p): 
    '''member_declarator : declarator pure_specifier 
                         | declarator 
                         
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_function_definition(p): 
    '''function_definition : type_specifier_ declarator func_push_scope arg_list  RPAREN fct_body pop_scope 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

    function_name = p[2].data["name"]
    func_sig = function_name +"|" + p[4].data["string"]
    
    func_detail = checkVar(func_sig, "*")
    # updateVar(func_sig, func_detail)    


def p_function_decl(p): 
    '''function_decl : type_specifier_ declarator func_push_scope arg_list  RPAREN SEMICOLON pop_scope ''' 
    p[0] = OBJ()
    p[0].parse=f(p)

def p_func_push_scope(p):
    ''' func_push_scope : LPAREN '''
    pushScope()


def p_fct_body(p): 
    '''fct_body : compound_statement''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_compound_statement(p): 
    '''compound_statement : LCPAREN statement_list RCPAREN 
                          | LCPAREN RCPAREN 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_statement_list(p): 
    '''statement_list : statement 
                      | statement_list statement 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_statement(p): 
    '''statement : expression_statement 
                 | push_scope compound_statement pop_scope
                 | selection_statement 
                 | iteration_statement 
                 | jump_statement 
                 | declaration_statement 
                 | try_block 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_jump_statement(p): 
    '''jump_statement : BREAK SEMICOLON 
                      | CONTINUE SEMICOLON 
                      | RETURN expression SEMICOLON 
                      | RETURN SEMICOLON 
                      | GOTO IDENTIFIER SEMICOLON 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)
  

def p_selection_statement(p): 
    '''selection_statement : IF LPAREN expression  RPAREN push_scope compound_statement pop_scope
                           | IF LPAREN expression  RPAREN push_scope compound_statement pop_scope ELSE push_scope compound_statement pop_scope 
                           | SWITCH LPAREN expression  RPAREN push_scope  LCPAREN labeled_statement_list RCPAREN pop_scope
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)  
  

def p_try_block(p): 
    '''try_block : TRY push_scope compound_statement pop_scope CATCH  push_scope compound_statement pop_scope''' 
    p[0] = OBJ() 
    p[0].parse=f(p)


def p_labeled_statement_list(p): 
    '''labeled_statement_list : labeled_statement
                              | labeled_statement_list labeled_statement 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_labeled_statement(p): 
    '''labeled_statement : CASE constant_expression COLON statement_list
                         | DEFAULT COLON statement_list
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_iteration_statement(p): 
    '''iteration_statement : WHILE push_scope LPAREN expression  RPAREN  statement pop_scope 
                           | DO push_scope statement WHILE LPAREN expression  RPAREN  SEMICOLON pop_scope 
                           | FOR LPAREN push_scope for_init_statement expression SEMICOLON expression  RPAREN  compound_statement pop_scope 
                           | FOR LPAREN push_scope for_init_statement SEMICOLON expression  RPAREN  compound_statement pop_scope 
                           | FOR LPAREN push_scope for_init_statement expression SEMICOLON  RPAREN  compound_statement pop_scope 
                           | FOR LPAREN push_scope for_init_statement SEMICOLON  RPAREN  statement pop_scope 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p) 

def p_for_init_statement(p): 
    '''for_init_statement : expression_statement 
                          | declaration_statement 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_expression_statement(p): 
    '''expression_statement : expression SEMICOLON 
                            | SEMICOLON 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_declaration_statement(p): 
    '''declaration_statement : declaration''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_declaration0(p):
    '''declaration : type_specifier_ declarator_list SEMICOLON ''' 
                #    | type_specifier_ SEMICOLON
    p[0] = OBJ()
    p[0].parse=f(p)
    decl_list = p[2].data
    for each in decl_list:
        type_info = {"specifier" : p[1].data, "declarator" : each }
        type_string = p[1].data["type"] + "|" + each["type"]
        to_push  = {"name" : each["name"], "type" : type_info  , "init" : None, "string": type_string  }
        print("pushing", to_push["name"])
        if pushVar(each["name"],to_push)==False:
            print("Error:"+ str(p.lineno(1))+" redeclaration of variable")
            exit()


def p_declaration1(p):
    '''declaration :  asm_declaration  ''' 
        
    p[0] = OBJ()
    p[0].parse=f(p)


def p_declaration2(p):
    '''declaration :  function_definition 
                    | function_decl
    ''' 
    p[0] = OBJ()
    p[0].parse=f(p)

def p_declaration3(p):
    '''declaration : class_define_specifier SEMICOLON ''' 
    p[0] = OBJ()
    p[0].parse=f(p)


def p_declaration4(p):
    '''declaration :  template_declaration ''' 
    p[0] = OBJ()
    p[0].parse=f(p)


def p_declaration5(p):
    '''declaration : typedef_declarator ''' 
    p[0] = OBJ()
    p[0].parse=f(p)

def p_template_declaration(p): 
    '''template_declaration : TEMPLATE LTEMPLATE template_argument_list RTEMPLATE declaration''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_template_argument_list(p): 
    '''template_argument_list : argument_declaration
                              | template_argument_list COMMA argument_declaration
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_declarator_list(p): 
    '''declarator_list : init_declarator 
                       | declarator_list COMMA init_declarator 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

    if len(p) == 2 :
        p[0].data = [p[1].data]
    else:
        p[0].data = p[1].data + [ p[3].data ]

def p_init_declarator(p): 
    '''init_declarator : declarator initializer 
                       | declarator 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

    if len(p) == 2:
        p[0].data = p[1].data
    else:
        pass

def p_initializer(p): 
    '''initializer :   EQUAL assignment_expression 
                   |   EQUAL LCPAREN initializer_list RCPAREN 
                   |   EQUAL LCPAREN initializer_list COMMA RCPAREN 
                   | LPAREN expression_list  RPAREN 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p) 

def p_initializer_list(p): 
    '''initializer_list : assignment_expression 
                        | initializer_list COMMA assignment_expression 
                        | LCPAREN initializer_list RCPAREN 
                        | LCPAREN initializer_list COMMA RCPAREN 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_asm_declaration(p): 
    '''asm_declaration : ASM LPAREN STRING_L  RPAREN  SEMICOLON''' 
    p[0] = OBJ() 
    p[0].parse=f(p)

def p_expression_list(p): 
    '''expression_list : assignment_expression 
                       | expression_list COMMA assignment_expression 
    ''' 
    p[0] = OBJ() 
    p[0].parse=f(p) 

def p_push_scope(p):
    '''push_scope : '''
    pushScope()

def p_pop_scope(p):
    '''pop_scope : '''
    popScope()

def scope_table_graph(S):
    pp = pprint.PrettyPrinter(indent=4)
    open('scope.gz','w').write("digraph ethane{ rankdir=LR {graph [ordering=\"out\"];node [fontsize=20 width=0.25 shape=box ]; ")
    cnt=0
    done = {}
    for s in S:
        if s.parent != None:
            label_child = pp.pformat(s.table)
            label_parent = pp.pformat(S[s.parent])
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

if __name__ == "__main__": 
    parser = yacc.yacc()
    parser.error = 0 

    if(len(sys.argv) != 3): 
        print("Usage python3 parser.py arg1 arg2 #args : ", sys.argv) 
        exit() 

    arglist = sys.argv 
    filename = arglist[2]
    debug = int(arglist[1])
    open('dot.gz','w').write("digraph ethane {graph [ordering=\"out\"];")
    file_o = open(arglist[2],'r').read()
    p = parser.parse(file_o,lexer = lexer,debug=debug,tracking=True)  
    open('dot.gz','a').write("\n}\n")
    scope_table_graph(scopeTableList)
