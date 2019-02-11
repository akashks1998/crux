from ply import yacc
import os,sys,time
from lexer import lexer
from lexer import tokens as lexTokens

tokens = lexTokens

start = 'program'

def p_program(p):
    '''program : NUMBER 
        | STRING
    '''
    p[0] = p[1]

################################################################################
############################  Expressions   ####################################
################################################################################

def p_primary_expression(p):
    '''primary_expression :  literal
                          |  this
                          |  DL identifier
                          |  DL operator_function_id
                          |  qualified_id
                          | (expression)
    '''




# rule for empty
def p_empty(p):
    'empty :'
    pass



# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

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
    