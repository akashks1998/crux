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
    '''primary_expression : literal
                          | this
                          | :: identifier
                          | :: operator_function_id
                          | :: qualified_id
                          | ( expression )
                          | id_expression
    '''

def p_id_expression(p):
    '''id_expression : unqualified_id
                     | qualified_id
    '''
def p_id_expression(p):
    '''id_expression : unqualified_id
                     | qualified_id
    '''
def p_unqualified_id(p):
    '''unqualified_id : identifier
                      | operator_function_id
                      | conversion_function_id
                      | ~ class_name
                      | template_id
    '''

def p_qualified_id(p):
    '''qualified_id : nested_name_specifier templateopt unqualified_id'''

def p_nested_name_specifier(p):
    '''nested_name_specifier : class_or_namespace_name :: nested_name_specifieropt
                             | class_or_namespace_name :: template nested_name_specifier
    '''

def p_class_or_namespace_name(p):
    '''class_or_namespace_name : class_name
                               | namespace_name
    '''


def p_postfix_expression(p):
    '''postfix_expression : primary_expression
                          | postfix_expression [ expression ]
                          | postfix_expression ( expression_listopt )
                          | simple_type_specifier ( expression_listopt )
                          | typename ::opt nested_name_specifier identifier ( expression_listopt )
                          | typename ::opt nested_name_specifier templateopt template_id ( expression_listopt )
                          | postfix_expression . templateopt ::opt id_expression
                          | postfix_expression _> templateopt ::opt id_expression
                          | postfix_expression . pseudo_destructor_name
                          | postfix_expression _> pseudo_destructor_name
                          | postfix_expression ++
                          | postfix_expression __
                          | dynamic_cast < type_id > ( expression )
                          | static_cast < type_id > ( expression )
                          | reinterpret_cast < type_id > ( expression )
                          | const_cast < type_id > ( expression )
                          | typeid ( expression )
                          | typeid ( type_id )
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
