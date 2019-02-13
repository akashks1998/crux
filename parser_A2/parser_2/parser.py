from ply import yacc
import os
import sys
import time
from lexer import lexer
from lexer import tokens as lexTokens
cnt=0
tokens = lexTokens
start = 'program'
## Copy and paste the output in 
##### Compress
def data(p):
    global cnt
    p_name = sys._getframe(1).f_code.co_name
    if len(p)>2:
        cnt=cnt+1
        out = (p_name[2:],cnt)
        print(str(cnt)+"[label="+p_name[2:]+"]")
        for each in range(len(p)-1):
            if(type(p[each+1]) is not tuple):
                if p[each+1]!="{" and p[each+1]!="}" and p[each+1]!=")" and p[each+1]!="(" and p[each+1]!=';':
                    cnt=cnt+1
                    print(str(cnt)+"[label=\""+str(p[each+1])+"\"]")
                    p[each+1]=(p[each+1],cnt)
            if p[each+1][0]!="{" and p[each+1][0]!="}" and p[each+1][0]!=")" and p[each+1][0]!="(" and p[each+1][0]!=';':
                print(str(out[1])+" -- "+str(p[each+1][1]))
    else:
        out=p[1]
    return out
# Uncompress
# def data(p):
#     global cnt
#     p_name = sys._getframe(1).f_code.co_name
#     cnt=cnt+1
#     out = (p_name[2:],cnt)
#     print("    "+str(cnt)+"[label="+p_name[2:]+"]")
#     for each in range(len(p)-1):
#         if(type(p[each+1]) is not tuple):
#             cnt=cnt+1
#             print("    "+str(cnt)+"[label=\""+str(p[each+1])+"\"]")
#             p[each+1]=(p[each+1],cnt)
#         print("    "+str(out[1])+" -- "+str(p[each+1][1]))
#     return out
def p_program(p):
    '''program : translation_unit

    '''
    p[0]=data(p)

def p_primary_expression(p):
    '''primary_expression : IDENTIFIER
                         | NUMBER
                         | STRING_LITERAL
                         | SCHAR
                         | LRPAREN expression RRPAREN

    '''
    p[0]=data(p)


def p_postfix_expression(p):
    '''postfix_expression : primary_expression
                         | postfix_expression LSPAREN expression RSPAREN
                         | postfix_expression LRPAREN RRPAREN
                         | postfix_expression LRPAREN argument_expression_list RRPAREN
                         | postfix_expression DOT IDENTIFIER
                         | postfix_expression PTR_OP IDENTIFIER
                         | postfix_expression INC_OP
                         | postfix_expression DEC_OP

    '''
    p[0]=data(p)


def p_argument_expression_list(p):
    '''argument_expression_list : assignment_expression
                               | argument_expression_list COMMA assignment_expression

    '''
    p[0]=data(p)


def p_unary_expression(p):
    '''unary_expression : postfix_expression
                       | INC_OP unary_expression
                       | DEC_OP unary_expression
                       | unary_operator cast_expression
                       | SIZEOF unary_expression
                       | SIZEOF LRPAREN type_name RRPAREN

    '''
    p[0]=data(p)


def p_unary_operator(p):
    '''unary_operator : BANDOP
                     | MULTOP
                     | PLUSOP
                     | MINUSOP
                     | BNOP
                     | NOTSYM

    '''
    p[0]=data(p)


def p_cast_expression(p):
    '''cast_expression : unary_expression
                      | LRPAREN type_name RRPAREN cast_expression

    '''
    p[0]=data(p)


def p_multiplicative_expression(p):
    '''multiplicative_expression : cast_expression
                                | multiplicative_expression MULTOP cast_expression
                                | multiplicative_expression DIVOP cast_expression
                                | multiplicative_expression MODOP cast_expression

    '''
    p[0]=data(p)


def p_additive_expression(p):
    '''additive_expression : multiplicative_expression
                          | additive_expression PLUSOP multiplicative_expression
                          | additive_expression MINUSOP multiplicative_expression

    '''
    p[0]=data(p)


def p_shift_expression(p):
    '''shift_expression : additive_expression
                       | shift_expression LEFT_OP additive_expression
                       | shift_expression RIGHT_OP additive_expression

    '''
    p[0]=data(p)


def p_relational_expression(p):
    '''relational_expression : shift_expression
                            | relational_expression LTCOMP shift_expression
                            | relational_expression GTCOMP shift_expression
                            | relational_expression LE_OP shift_expression
                            | relational_expression GE_OP shift_expression

    '''
    p[0]=data(p)


def p_equality_expression(p):
    '''equality_expression : relational_expression
                          | equality_expression EQ_OP relational_expression
                          | equality_expression NE_OP relational_expression

    '''
    p[0]=data(p)


def p_and_expression(p):
    '''and_expression : equality_expression
                     | and_expression BANDOP equality_expression

    '''
    p[0]=data(p)


def p_exclusive_or_expression(p):
    '''exclusive_or_expression : and_expression
                              | exclusive_or_expression XOROP and_expression

    '''
    p[0]=data(p)


def p_inclusive_or_expression(p):
    '''inclusive_or_expression : exclusive_or_expression
                              | inclusive_or_expression BOROP exclusive_or_expression

    '''
    p[0]=data(p)


def p_logical_and_expression(p):
    '''logical_and_expression : inclusive_or_expression
                             | logical_and_expression AND_OP inclusive_or_expression

    '''
    p[0]=data(p)


def p_logical_or_expression(p):
    '''logical_or_expression : logical_and_expression
                            | logical_or_expression OR_OP logical_and_expression

    '''
    p[0]=data(p)


def p_conditional_expression(p):
    '''conditional_expression : logical_or_expression
                             | logical_or_expression QUESMARK expression COLON conditional_expression

    '''
    p[0]=data(p)


def p_assignment_expression(p):
    '''assignment_expression : conditional_expression
                            | unary_expression assignment_operator assignment_expression

    '''
    p[0]=data(p)


def p_assignment_operator(p):
    '''assignment_operator : EQUAL
                          | MUL_ASSIGN
                          | DIV_ASSIGN
                          | MOD_ASSIGN
                          | ADD_ASSIGN
                          | SUB_ASSIGN
                          | LEFT_ASSIGN
                          | RIGHT_ASSIGN
                          | AND_ASSIGN
                          | XOR_ASSIGN
                          | OR_ASSIGN

    '''
    p[0]=data(p)


def p_expression(p):
    '''expression : assignment_expression
                 | expression COMMA assignment_expression

    '''
    p[0]=data(p)


def p_constant_expression(p):
    '''constant_expression : conditional_expression

    '''
    p[0]=data(p)


def p_declaration(p):
    '''declaration : declaration_specifiers SEMICOLON
                  | declaration_specifiers init_declarator_list SEMICOLON

    '''
    p[0]=data(p)


def p_declaration_specifiers(p):
    '''declaration_specifiers : storage_class_specifier
                             | storage_class_specifier declaration_specifiers
                             | type_specifier
                             | type_specifier declaration_specifiers
                             | type_qualifier
                             | type_qualifier declaration_specifiers

    '''
    p[0]=data(p)


def p_init_declarator_list(p):
    '''init_declarator_list : init_declarator
                           | init_declarator_list COMMA init_declarator

    '''
    p[0]=data(p)


def p_init_declarator(p):
    '''init_declarator : declarator
                      | declarator EQUAL initializer

    '''
    p[0]=data(p)


def p_storage_class_specifier(p):
    '''storage_class_specifier : TYPEDEF
                              | EXTERN
                              | STATIC
                              | AUTO
                              | REGISTER

    '''
    p[0]=data(p)


def p_type_specifier(p):
    '''type_specifier : VOID
                     | CHAR
                     | SHORT
                     | INT
                     | LONG
                     | FLOAT
                     | DOUBLE
                     | SIGNED
                     | UNSIGNED
                     | struct_or_union_specifier
                     | enum_specifier
    '''
    p[0]=data(p)


def p_struct_or_union_specifier(p):
    '''struct_or_union_specifier : struct_or_union IDENTIFIER LCPAREN struct_declaration_list RCPAREN
                                | struct_or_union LCPAREN struct_declaration_list RCPAREN
                                | struct_or_union IDENTIFIER

    '''
    p[0]=data(p)


def p_struct_or_union(p):
    '''struct_or_union : STRUCT
                      | UNION

    '''
    p[0]=data(p)


def p_struct_declaration_list(p):
    '''struct_declaration_list : struct_declaration
                              | struct_declaration_list struct_declaration

    '''
    p[0]=data(p)


def p_struct_declaration(p):
    '''struct_declaration : specifier_qualifier_list struct_declarator_list SEMICOLON
    '''
    p[0]=data(p)


def p_specifier_qualifier_list(p):
    '''specifier_qualifier_list : type_specifier specifier_qualifier_list
                               | type_specifier
                               | type_qualifier specifier_qualifier_list
                               | type_qualifier

    '''
    p[0]=data(p)


def p_struct_declarator_list(p):
    '''struct_declarator_list : struct_declarator
                             | struct_declarator_list COMMA struct_declarator

    '''
    p[0]=data(p)


def p_struct_declarator(p):
    '''struct_declarator : declarator
                        | COLON constant_expression
                        | declarator COLON constant_expression

    '''
    p[0]=data(p)


def p_enum_specifier(p):
    '''enum_specifier : ENUM LCPAREN enumerator_list RCPAREN
                     | ENUM IDENTIFIER LCPAREN enumerator_list RCPAREN
                     | ENUM IDENTIFIER

    '''
    p[0]=data(p)


def p_enumerator_list(p):
    '''enumerator_list : enumerator
                      | enumerator_list COMMA enumerator

    '''
    p[0]=data(p)


def p_enumerator(p):
    '''enumerator : IDENTIFIER
                 | IDENTIFIER EQUAL constant_expression

    '''
    p[0]=data(p)


def p_type_qualifier(p):
    '''type_qualifier : CONST
                     | VOLATILE

    '''
    p[0]=data(p)


def p_declarator(p):
    '''declarator : pointer direct_declarator
                 | direct_declarator

    '''
    p[0]=data(p)


def p_direct_declarator(p):
    '''direct_declarator : IDENTIFIER
                        | LRPAREN declarator RRPAREN
                        | direct_declarator LSPAREN constant_expression RSPAREN
                        | direct_declarator LSPAREN RSPAREN
                        | direct_declarator LRPAREN parameter_type_list RRPAREN
                        | direct_declarator LRPAREN identifier_list RRPAREN
                        | direct_declarator LRPAREN RRPAREN

    '''
    p[0]=data(p)


def p_pointer(p):
    '''pointer : MULTOP
              | MULTOP type_qualifier_list
              | MULTOP pointer
              | MULTOP type_qualifier_list pointer

    '''
    p[0]=data(p)


def p_type_qualifier_list(p):
    '''type_qualifier_list : type_qualifier
                          | type_qualifier_list type_qualifier

    '''
    p[0]=data(p)


def p_parameter_type_list(p):
    '''parameter_type_list : parameter_list
                          | parameter_list COMMA ELLIPSIS

    '''
    p[0]=data(p)


def p_parameter_list(p):
    '''parameter_list : parameter_declaration
                     | parameter_list COMMA parameter_declaration

    '''
    p[0]=data(p)


def p_parameter_declaration(p):
    '''parameter_declaration : declaration_specifiers declarator
                            | declaration_specifiers abstract_declarator
                            | declaration_specifiers

    '''
    p[0]=data(p)


def p_identifier_list(p):
    '''identifier_list : IDENTIFIER
                      | identifier_list COMMA IDENTIFIER

    '''
    p[0]=data(p)


def p_type_name(p):
    '''type_name : specifier_qualifier_list
                | specifier_qualifier_list abstract_declarator

    '''
    p[0]=data(p)


def p_abstract_declarator(p):
    '''abstract_declarator : pointer
                          | direct_abstract_declarator
                          | pointer direct_abstract_declarator

    '''
    p[0]=data(p)


def p_direct_abstract_declarator(p):
    '''direct_abstract_declarator : LRPAREN abstract_declarator RRPAREN
                                 | LSPAREN RSPAREN
                                 | LSPAREN constant_expression RSPAREN
                                 | direct_abstract_declarator LSPAREN RSPAREN
                                 | direct_abstract_declarator LSPAREN constant_expression RSPAREN
                                 | LRPAREN RRPAREN
                                 | LRPAREN parameter_type_list RRPAREN
                                 | direct_abstract_declarator LRPAREN RRPAREN
                                 | direct_abstract_declarator LRPAREN parameter_type_list RRPAREN

    '''
    p[0]=data(p)


def p_initializer(p):
    '''initializer : assignment_expression
                  | LCPAREN initializer_list RCPAREN
                  | LCPAREN initializer_list COMMA RCPAREN

    '''
    p[0]=data(p)


def p_initializer_list(p):
    '''initializer_list : initializer
                       | initializer_list COMMA initializer

    '''
    p[0]=data(p)


def p_statement(p):
    '''statement : labeled_statement
                | compound_statement
                | expression_statement
                | selection_statement
                | iteration_statement
                | jump_statement

    '''
    p[0]=data(p)


def p_labeled_statement(p):
    '''labeled_statement : IDENTIFIER COLON statement
                        | CASE constant_expression COLON statement
                        | DEFAULT COLON statement

    '''
    p[0]=data(p)


def p_compound_statement(p):
    '''compound_statement : LCPAREN RCPAREN
                         | LCPAREN statement_list RCPAREN
                         | LCPAREN declaration_list RCPAREN
                         | LCPAREN declaration_list statement_list RCPAREN

    '''
    p[0]=data(p)


def p_declaration_list(p):
    '''declaration_list : declaration
                       | declaration_list declaration

    '''
    p[0]=data(p)


def p_statement_list(p):
    '''statement_list : statement
                     | statement_list statement

    '''
    p[0]=data(p)


def p_expression_statement(p):
    '''expression_statement : SEMICOLON
                           | expression SEMICOLON

    '''
    p[0]=data(p)


def p_selection_statement(p):
    '''selection_statement : IF LRPAREN expression RRPAREN statement
                          | IF LRPAREN expression RRPAREN statement ELSE statement
                          | SWITCH LRPAREN expression RRPAREN statement

    '''
    p[0]=data(p)


def p_iteration_statement(p):
    '''iteration_statement : WHILE LRPAREN expression RRPAREN statement
                          | DO statement WHILE LRPAREN expression RRPAREN SEMICOLON
                          | FOR LRPAREN expression_statement expression_statement RRPAREN statement
                          | FOR LRPAREN expression_statement expression_statement expression RRPAREN statement

    '''
    p[0]=data(p)


def p_jump_statement(p):
    '''jump_statement : GOTO IDENTIFIER SEMICOLON
                     | CONTINUE SEMICOLON
                     | BREAK SEMICOLON
                     | RETURN SEMICOLON
                     | RETURN expression SEMICOLON

    '''
    p[0]=data(p)


def p_translation_unit(p):
    '''translation_unit : external_declaration
                       | translation_unit external_declaration

    '''
    p[0]=data(p)


def p_external_declaration(p):
    '''external_declaration : function_definition
                           | declaration
    '''
    p[0]=data(p)


def p_function_definition(p):
    '''function_definition : declaration_specifiers declarator declaration_list compound_statement
                          | declaration_specifiers declarator compound_statement
                          | declarator declaration_list compound_statement
                          | declarator compound_statement

    '''
    p[0]=data(p)

def p_error(p): 
    print("Syntax error in input!")
    print(p)
     
#######################################################################
    
# def p_class_specifier(p):
#     '''class_specifier : class IDENTIFIER LCPAREN final_class_list RCPAREN
#                         | class LCPAREN final_class_list RCPAREN
#                         | class IDENTIFIER
#     '''

# def p_class(p):
#     '''class : CLASS '''
# def p_access_specifier(p): 
#     '''access_specifier : PRIVATE 
#                         | PROTECTED 
#                         | PUBLIC 
#     ''' 
# def p_final_class_list(p):
#     ''' final_class_list : access_specifier COLON class_list 
#                          | access_specifier COLON class_list final_class_list
    
    
#     '''

# def p_class_list(p):
#     '''class_list : class_declaration
#                   | class_list class_declaration
#                   | function_definition
#     '''


# def p_class_declaration(p):
#     '''class_declaration : specifier_qualifier_list struct_declarator_list SEMICOLON
                         
#     '''

#######################################################################
 
if __name__ == "__main__": 
    parser = yacc.yacc() 
    parser.error = 0 
    if(len(sys.argv) != 3): 
        print("Usage python3 parser.py LTCOMPdebugGTCOMP LTCOMPmodeGTCOMP") 
        exit() 
    print("graph ethane {")
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
        file_o = open(arglist[2],'r').read()
        p = parser.parse(file_o,lexer = lexer,debug=debug) 
        print(p) 
 
 
 

