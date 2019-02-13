from ply import yacc
import os
import sys
import time
from lexer import lexer
from lexer import tokens as lexTokens

tokens = lexTokens

start = 'program'


def p_program(p):
    '''program : translation_unit

    '''
    p[0] = p[1]

def p_primary_expression(p):
    '''primary_expression : IDENTIFIER
                         | NUMBER
                         | STRING_LITERAL
                         | SCHAR
                         | LRPAREN expression RRPAREN

    '''


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


def p_argument_expression_list(p):
    '''argument_expression_list : assignment_expression
                               | argument_expression_list COMMA assignment_expression

    '''


def p_unary_expression(p):
    '''unary_expression : postfix_expression
                       | INC_OP unary_expression
                       | DEC_OP unary_expression
                       | unary_operator cast_expression
                       | SIZEOF unary_expression
                       | SIZEOF LRPAREN type_name RRPAREN

    '''


def p_unary_operator(p):
    '''unary_operator : BANDOP
                     | MULTOP
                     | PLUSOP
                     | MINUSOP
                     | BNOP
                     | NOTSYM

    '''


def p_cast_expression(p):
    '''cast_expression : unary_expression
                      | LRPAREN type_name RRPAREN cast_expression

    '''


def p_multiplicative_expression(p):
    '''multiplicative_expression : cast_expression
                                | multiplicative_expression MULTOP cast_expression
                                | multiplicative_expression DIVOP cast_expression
                                | multiplicative_expression MODOP cast_expression

    '''


def p_additive_expression(p):
    '''additive_expression : multiplicative_expression
                          | additive_expression PLUSOP multiplicative_expression
                          | additive_expression MINUSOP multiplicative_expression

    '''


def p_shift_expression(p):
    '''shift_expression : additive_expression
                       | shift_expression LEFT_OP additive_expression
                       | shift_expression RIGHT_OP additive_expression

    '''


def p_relational_expression(p):
    '''relational_expression : shift_expression
                            | relational_expression LTCOMP shift_expression
                            | relational_expression GTCOMP shift_expression
                            | relational_expression LE_OP shift_expression
                            | relational_expression GE_OP shift_expression

    '''


def p_equality_expression(p):
    '''equality_expression : relational_expression
                          | equality_expression EQ_OP relational_expression
                          | equality_expression NE_OP relational_expression

    '''


def p_and_expression(p):
    '''and_expression : equality_expression
                     | and_expression BANDOP equality_expression

    '''


def p_exclusive_or_expression(p):
    '''exclusive_or_expression : and_expression
                              | exclusive_or_expression XOROP and_expression

    '''


def p_inclusive_or_expression(p):
    '''inclusive_or_expression : exclusive_or_expression
                              | inclusive_or_expression BOROP exclusive_or_expression

    '''


def p_logical_and_expression(p):
    '''logical_and_expression : inclusive_or_expression
                             | logical_and_expression AND_OP inclusive_or_expression

    '''


def p_logical_or_expression(p):
    '''logical_or_expression : logical_and_expression
                            | logical_or_expression OR_OP logical_and_expression

    '''


def p_conditional_expression(p):
    '''conditional_expression : logical_or_expression
                             | logical_or_expression QUESMARK expression COLON conditional_expression

    '''


def p_assignment_expression(p):
    '''assignment_expression : conditional_expression
                            | unary_expression assignment_operator assignment_expression

    '''


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


def p_expression(p):
    '''expression : assignment_expression
                 | expression COMMA assignment_expression

    '''


def p_constant_expression(p):
    '''constant_expression : conditional_expression

    '''


def p_declaration(p):
    '''declaration : declaration_specifiers SEMICOLON
                  | declaration_specifiers init_declarator_list SEMICOLON

    '''


def p_declaration_specifiers(p):
    '''declaration_specifiers : storage_class_specifier
                             | storage_class_specifier declaration_specifiers
                             | type_specifier
                             | type_specifier declaration_specifiers
                             | type_qualifier
                             | type_qualifier declaration_specifiers

    '''


def p_init_declarator_list(p):
    '''init_declarator_list : init_declarator
                           | init_declarator_list COMMA init_declarator

    '''


def p_init_declarator(p):
    '''init_declarator : declarator
                      | declarator EQUAL initializer

    '''


def p_storage_class_specifier(p):
    '''storage_class_specifier : TYPEDEF
                              | EXTERN
                              | STATIC
                              | AUTO
                              | REGISTER

    '''


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


def p_struct_or_union_specifier(p):
    '''struct_or_union_specifier : struct_or_union IDENTIFIER LCPAREN struct_declaration_list RCPAREN
                                | struct_or_union LCPAREN struct_declaration_list RCPAREN
                                | struct_or_union IDENTIFIER

    '''


def p_struct_or_union(p):
    '''struct_or_union : STRUCT
                      | UNION
                      | CLASS

    '''


def p_struct_declaration_list(p):
    '''struct_declaration_list : struct_declaration
                              | struct_declaration_list struct_declaration

    '''


def p_struct_declaration(p):
    '''struct_declaration : specifier_qualifier_list struct_declarator_list SEMICOLON
    '''


def p_specifier_qualifier_list(p):
    '''specifier_qualifier_list : type_specifier specifier_qualifier_list
                               | type_specifier
                               | type_qualifier specifier_qualifier_list
                               | type_qualifier

    '''


def p_struct_declarator_list(p):
    '''struct_declarator_list : struct_declarator
                             | struct_declarator_list COMMA struct_declarator

    '''


def p_struct_declarator(p):
    '''struct_declarator : declarator
                        | COLON constant_expression
                        | declarator COLON constant_expression

    '''


def p_enum_specifier(p):
    '''enum_specifier : ENUM LCPAREN enumerator_list RCPAREN
                     | ENUM IDENTIFIER LCPAREN enumerator_list RCPAREN
                     | ENUM IDENTIFIER

    '''


def p_enumerator_list(p):
    '''enumerator_list : enumerator
                      | enumerator_list COMMA enumerator

    '''


def p_enumerator(p):
    '''enumerator : IDENTIFIER
                 | IDENTIFIER EQUAL constant_expression

    '''


def p_type_qualifier(p):
    '''type_qualifier : CONST
                     | VOLATILE

    '''


def p_declarator(p):
    '''declarator : pointer direct_declarator
                 | direct_declarator

    '''


def p_direct_declarator(p):
    '''direct_declarator : IDENTIFIER
                        | LRPAREN declarator RRPAREN
                        | direct_declarator LSPAREN constant_expression RSPAREN
                        | direct_declarator LSPAREN RSPAREN
                        | direct_declarator LRPAREN parameter_type_list RRPAREN
                        | direct_declarator LRPAREN identifier_list RRPAREN
                        | direct_declarator LRPAREN RRPAREN

    '''


def p_pointer(p):
    '''pointer : MULTOP
              | MULTOP type_qualifier_list
              | MULTOP pointer
              | MULTOP type_qualifier_list pointer

    '''


def p_type_qualifier_list(p):
    '''type_qualifier_list : type_qualifier
                          | type_qualifier_list type_qualifier

    '''


def p_parameter_type_list(p):
    '''parameter_type_list : parameter_list
                          | parameter_list COMMA ELLIPSIS

    '''


def p_parameter_list(p):
    '''parameter_list : parameter_declaration
                     | parameter_list COMMA parameter_declaration

    '''


def p_parameter_declaration(p):
    '''parameter_declaration : declaration_specifiers declarator
                            | declaration_specifiers abstract_declarator
                            | declaration_specifiers

    '''


def p_identifier_list(p):
    '''identifier_list : IDENTIFIER
                      | identifier_list COMMA IDENTIFIER

    '''


def p_type_name(p):
    '''type_name : specifier_qualifier_list
                | specifier_qualifier_list abstract_declarator

    '''


def p_abstract_declarator(p):
    '''abstract_declarator : pointer
                          | direct_abstract_declarator
                          | pointer direct_abstract_declarator

    '''


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


def p_initializer(p):
    '''initializer : assignment_expression
                  | LCPAREN initializer_list RCPAREN
                  | LCPAREN initializer_list COMMA RCPAREN

    '''


def p_initializer_list(p):
    '''initializer_list : initializer
                       | initializer_list COMMA initializer

    '''


def p_statement(p):
    '''statement : labeled_statement
                | compound_statement
                | expression_statement
                | selection_statement
                | iteration_statement
                | jump_statement

    '''


def p_labeled_statement(p):
    '''labeled_statement : IDENTIFIER COLON statement
                        | CASE constant_expression COLON statement
                        | DEFAULT COLON statement

    '''


def p_compound_statement(p):
    '''compound_statement : LCPAREN RCPAREN
                         | LCPAREN statement_list RCPAREN
                         | LCPAREN declaration_list RCPAREN
                         | LCPAREN declaration_list statement_list RCPAREN

    '''


def p_declaration_list(p):
    '''declaration_list : declaration
                       | declaration_list declaration

    '''


def p_statement_list(p):
    '''statement_list : statement
                     | statement_list statement

    '''


def p_expression_statement(p):
    '''expression_statement : SEMICOLON
                           | expression SEMICOLON

    '''


def p_selection_statement(p):
    '''selection_statement : IF LRPAREN expression RRPAREN statement
                          | IF LRPAREN expression RRPAREN statement ELSE statement
                          | SWITCH LRPAREN expression RRPAREN statement

    '''


def p_iteration_statement(p):
    '''iteration_statement : WHILE LRPAREN expression RRPAREN statement
                          | DO statement WHILE LRPAREN expression RRPAREN SEMICOLON
                          | FOR LRPAREN expression_statement expression_statement RRPAREN statement
                          | FOR LRPAREN expression_statement expression_statement expression RRPAREN statement

    '''


def p_jump_statement(p):
    '''jump_statement : GOTO IDENTIFIER SEMICOLON
                     | CONTINUE SEMICOLON
                     | BREAK SEMICOLON
                     | RETURN SEMICOLON
                     | RETURN expression SEMICOLON

    '''


def p_translation_unit(p):
    '''translation_unit : external_declaration
                       | translation_unit external_declaration

    '''


def p_external_declaration(p):
    '''external_declaration : function_definition
                           | declaration

    '''


def p_function_definition(p):
    '''function_definition : declaration_specifiers declarator declaration_list compound_statement
                          | declaration_specifiers declarator compound_statement
                          | declarator declaration_list compound_statement
                          | declarator compound_statement

    '''

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

# def p_final_class_list(p):
#     ''' final_class_list : class_list
#                          | PUBLIC COLON class_list PRIVATE COLON class_list
#                          | PRIVATE COLON class_list PUBLIC COLON class_list
#                          | PUBLIC COLON class_list 
#                          | PRIVATE COLON class_list
    
    
#     '''

# def p_class_list(p):
#     '''class_list : class_declaration
#                   | class_list class_declaration

#     '''


# def p_class_declaration(p):
#     '''class_declaration : specifier_qualifier_list struct_declarator_list SEMICOLON
#                          | function_definition
                         
#     '''

#######################################################################
 
if __name__ == "__main__": 
    parser = yacc.yacc() 
    parser.error = 0 
     
    if(len(sys.argv) != 3): 
        print("Usage python3 parser.py LTCOMPdebugGTCOMP LTCOMPmodeGTCOMP") 
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
        file_o = open(arglist[2],'r').read()
        p = parser.parse(file_o,lexer = lexer,debug=debug) 
        print(p) 
 
 
 
 

