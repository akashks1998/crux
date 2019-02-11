from ply import yacc
import os,sys,time
from lexer import lexer
from lexer import tokens as lexTokens

tokens = lexTokens

start = 'program'

def p_program(p):
    '''program : NUMBER '''
    p[0] = p[1]



# rule for empty
def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
########################################################################
########################## Key words #######################################
def p_typedef_name(p):
    'typedef_name : IDENTIFIER'
    p[0]=p[1]
def p_namespace_name(p):
    '''namespace_name : original_namespace_name
                      | namespace_alias'''
    p[0]=p[1]
def p_original_namespace_name(p):
    'original_namespace_name : IDENTIFIER'
    p[0]=p[1]
def p_namespace_alias(p):
    'namespace_alias : IDENTIFIER'
    p[0]=p[1]
def p_class_name(p):
    '''class_name : IDENTIFIER
                  | template_name'''
    p[0]=p[1]
def p_enum_name(p):
    'enum_name : IDENTIFIER'
    p[0]=p[1]
def p_template_name(p):
    'template_name : IDENTIFIER'
    p[0]=p[1]

########################################################################

if __name__ == "__main__":
    parser = yacc.yacc()
    parser.error = 0
    
    if(len(sys.argv) != 3):
        print("Usage python3 parser.py <debug> <mode>")
        exit()
    
    arglist = sys.argv
    debug = int(arglist[1])

    if(arglist[2]== "I"):
        while True:
            try:
                s = input('$ > ')
                if(s=="end"):
                    break
            except EOFError:
                break
            if not s:
                continue
            result = parser.parse(s,lexer = lexer,debug=debug)
            print(result)
    else:
        p = parser.parse("34",lexer = lexer,debug=debug)
        print(p)
    