from ply import yacc
import os,sys,time
from lexer import lexer
from lexer import tokens as lexTokens

tokens = lexTokens

def p_program(p):
    '''program : NUMBER '''
    p[0] = p[1]

if __name__ == "__main__":
    parser = yacc.yacc()
    parser.error = 0

    # start parsing with lexer from probQlexer
    p = parser.parse("34",lexer = lexer,debug=1)
    print(p)
    