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
        print("Usage python3 parser.py LTCOMPdebugGTCOMP LTCOMPmodeGTCOMP")
        exit()
    
    arglist = sys.argv
    debug = int(arglist[1])

    if(arglist[2]== "I"):
        while True:
            try:
                s = input('$ GTCOMP ')
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




def p_class_name(p):
    '''class_name : IDENTIFIER'''
def p_enum_name(p):
    '''enum_name : IDENTIFIER'''
def p_typedef_name(p):
    '''typedef_name : IDENTIFIER'''
def p_expression(p):
    '''expression : assignment_expression
                  | expression COMMA assignment_expression
    '''


def p_assignment_expression(p):
    '''assignment_expression : conditional_expression
                             | unary_expression  assignment_operator assignment_expression
    '''


def p_assignment_operator(p):
    '''assignment_operator : EQUAL
                           | *=
                           | /=
                           | %=
                           | +=
                           | _=
                           | <<=
                           | >>=
                           | &=
                           | ^=
                           | |=
    '''


def p_conditional_expression(p):
    '''conditional_expression : logical_OR_expression
                              | logical_OR_expression ? expression COLON conditional_expression
    '''


def p_logical_OR_expression(p):
    '''logical_OR_expression : logical_AND_expression
                             | logical_OR_expression || logical_AND_expression
    '''


def p_logical_AND_expression(p):
    '''logical_AND_expression : inclusive_OR_expression
                              | logical_AND_expression && inclusive_OR_expression
    '''


def p_inclusive_OR_expression(p):
    '''inclusive_OR_expression : exclusive_OR_expression
                               | inclusive_OR_expression | exclusive_OR_expression
    '''


def p_exclusive_OR_expression(p):
    '''exclusive_OR_expression : AND_expression
                               | exclusive_OR_expression ^ AND_expression
    '''


def p_AND_expression(p):
    '''AND_expression : equality_expression
                      | AND_expression & equality_expression
    '''


def p_equality_expression(p):
    '''equality_expression : relational_expression
                           | equality_expression EQCOMP relational_expression
                           | equality_expression NEQCOMP relational_expression
    '''


def p_relationa1_expression(p):
    '''relationa1_expression : shift_expression
                             | relational_expression <  shift_expression
                             | relational_expression >  shift_expression
                             | relational_expression <= shift_expression
                             | relational_expression >= shift_expression
    '''


def p_shift_expression(p):
    '''shift_expression : additive_expression
                        | shift_expression << additive_expression
                        | shift_expression >> additive_expression
    '''


def p_additive_expression(p):
    '''additive_expression : multiplicative_expression
                           | additive_expression + multiplicative_expression
                           | additive_expression _ multiplicative_expression
    '''


def p_multiplicative_expression(p):
    '''multiplicative_expression : pm_expression
                                 | multiplicative_expression * pm_expression
                                 | multiplicative_expression / pm_expression
                                 | multiplicative_expression % pm_expression
    '''


def p_pm_expression(p):
    '''pm_expression : cast_expression
                     | pm_expression .* cast_expression
                     | pm_expression _>* cast_expression
    '''


def p_cast_expression(p):
    '''cast_expression : unary_expression
                       | LPAREN type_name  RPAREN  cast_expression
    '''


def p_unary_expression(p):
    '''unary_expression : posfix_expression
                        | ++ unary_expression
                        | __ unary_expression
                        | unary_operator cast_expression
                        | sizeof  unary_expression
                        | sizeof LPAREN type_name  RPAREN
                        | allocation_expression
                        | deallocation_expression
    '''


def p_unary_operator(p):
    '''unary_operator : *
                      | &
                      | +
                      | _
                      | !
                      | ~
    '''


def p_allocation_expression(p):
    '''allocation_expression : DOUBLECOLON new placement new_type_name new_initializer
                             | new placement new_type_name new_initializer
                             | DOUBLECOLON new new_type_name new_initializer
                             | new new_type_name new_initializer
                             | DOUBLECOLON new placement new_type_name
                             | new placement new_type_name
                             | DOUBLECOLON new new_type_name
                             | new new_type_name
                             | DOUBLECOLON new placement LPAREN type_name  RPAREN  new_initializer
                             | new placement LPAREN type_name  RPAREN  new_initializer
                             | DOUBLECOLON new LPAREN type_name  RPAREN  new_initializer
                             | new LPAREN type_name  RPAREN  new_initializer
                             | DOUBLECOLON new placement LPAREN type_name  RPAREN
                             | new placement LPAREN type_name  RPAREN
                             | DOUBLECOLON new LPAREN type_name  RPAREN
                             | new LPAREN type_name  RPAREN
    '''


def p_placement(p):
    '''placement : LPAREN expression_list  RPAREN'''
def p_new_type_name(p):
    '''new_type_name : type_specifier_list new_declarator
                     | type_specifier_list
    '''


def p_new_declarator(p):
    '''new_declarator : * cv_qualifier_list new_declarator
                      | * new_declarator
                      | * cv_qualifier_list
                      | *
                      | complete_class_name DOUBLECOLON * cv_qualifier_list new_declarator
                      | complete_class_name DOUBLECOLON * new_declarator
                      | complete_class_name DOUBLECOLON * cv_qualifier_list
                      | complete_class_name DOUBLECOLON *
                      | new_declarator LSPAREN expression RSPAREN
                      | LSPAREN expression RSPAREN
    '''


def p_new_initializer(p):
    '''new_initializer : LPAREN initializer_list  RPAREN
                       | LPAREN  RPAREN
    '''


def p_deallocation_expression(p):
    '''deallocation_expression : DOUBLECOLON delete cast_expression
                               | delete cast_expression
                               | DOUBLECOLON delete LSPAREN RSPAREN cast_expression
                               | delete LSPAREN RSPAREN cast_expression
    '''


def p_postfix_expression(p):
    '''postfix_expression : primary_expression
                          | postfix_expression     LSPAREN expression RSPAREN
                          | postfix_expression     LPAREN expression_list  RPAREN
                          | postfix_expression     LPAREN  RPAREN
                          | simple_type_name       LPAREN expression_list  RPAREN
                          | simple_type_name       LPAREN  RPAREN
                          | postfix_expression     . name
                          | postfix_expression     _> name
                          | postfix_expression     ++
                          | postfix_expression     __
    '''


def p_expression_list(p):
    '''expression_list : assignment_expression
                       | expression_list COMMA assignment_expression
    '''


def p_primary_expression(p):
    '''primary_expression : literal
                          | this
                          | DOUBLECOLON IDENTIFIER
                          | DOUBLECOLON operator_function_name
                          | DOUBLECOLON qualified_name
                          | LPAREN expression  RPAREN
                          | name
    '''


def p_name(p):
    '''name : IDENTIFIER
            | operator_function_name
            | conversion_function_name
            | ~ class_name
            | qualified_name
    '''


def p_qualified_name(p):
    '''qualified_name : qualified_class_name DOUBLECOLON name'''
def p_literal(p):
    '''literal : integer_constant
               | character_constant
               | floating_constant
               | string_literal
    '''


def p_declaration(p):
    '''declaration : decl_specifiers declarator_list SEMICOLON
                   | decl_specifiers SEMICOLON
                   | declarator_list SEMICOLON
                   | asm_declaration
                   | function_definition
                   | template_declaration
                   | linkage_specification
    '''


def p_decl_specifier(p):
    '''decl_specifier : storage_class_specifier
                      | type_specifier
                      | fct_specifier
                      | friend
                      | typedef
    '''


def p_decl_specifiers(p):
    '''decl_specifiers : decl_specifiers decl_specifier
                       | decl_specifier
    '''


def p_storage_class_specifier(p):
    '''storage_class_specifier : auto
                               | register
                               | static
                               | extern
    '''


def p_fct_specifier(p):
    '''fct_specifier : inline
                     | virtual
    '''


def p_type_specifier(p):
    '''type_specifier : simple_type_name
                      | class_specifier
                      | enum_specifier
                      | elaborated_type_specifier
                      | const
                      | volatile
    '''


def p_simple_type_name(p):
    '''simple_type_name : complete_class_name
                        | qualified_type_name
                        | char
                        | short
                        | int
                        | long
                        | signed
                        | unsigned
                        | float
                        | double
                        | void
    '''


def p_elaborated_type_specifier(p):
    '''elaborated_type_specifier : class_key IDENTIFIER
                                 | class_key class_name
                                 | enum enum_name
    '''


def p_class_key(p):
    '''class_key : class
                 | struct
                 | union
    '''


def p_qualified_type_name(p):
    '''qualified_type_name : typedef_name
                           | class_name DOUBLECOLON qualified_type_name
    '''


def p_complete_class_name(p):
    '''complete_class_name : qualified_class_name
                           | DOUBLECOLON qualified_class_name
    '''


def p_qualified_class_name(p):
    '''qualified_class_name : class_name
                            | class_name DOUBLECOLON qualified_class_name
    '''


def p_enum_specifier(p):
    '''enum_specifier : enum IDENTIFIER LCPAREN enum_list RCPAREN
                      | enum LCPAREN enum_list RCPAREN
                      | enum IDENTIFIER LCPAREN RCPAREN
                      | enum LCPAREN RCPAREN
    '''


def p_enum_list(p):
    '''enum_list : enumerator
                 | enum_list COMMA enumerator
    '''


def p_enumerator(p):
    '''enumerator : IDENTIFIER
                  | IDENTIFIER EQUAL constant_expression
    '''


def p_constant_expression(p):
    '''constant_expression : conditional_expression'''
def p_linkage_specification(p):
    '''linkage_specification : extern string_literal LCPAREN declaration_list RCPAREN
                             | extern string_literal LCPAREN RCPAREN
                             | extern string_literal declaration
    '''


def p_declaration_list(p):
    '''declaration_list : declaration
                        | declaration_list declaration
    '''


def p_asm_declaration(p):
    '''asm_declaration : asm LPAREN string_literal  RPAREN  SEMICOLON'''
def p_declarator_list(p):
    '''declarator_list : init_declarator
                       | declarator_list COMMA init_declarator
    '''


def p_init_declarator(p):
    '''init_declarator : declarator initializer
                       | declarator
    '''


def p_declarator(p):
    '''declarator : dname
                  | ptr_operator declarator
                  | declarator LPAREN argument_declaration_list  RPAREN  cv_qualifier_list
                  | declarator LPAREN argument_declaration_list  RPAREN
                  | declarator LSPAREN constant_expression RSPAREN
                  | declarator LSPAREN RSPAREN
                  | LPAREN declarator  RPAREN
    '''


def p_ptr_operator(p):
    '''ptr_operator : * cv_qualifier_list
                    | *
                    | & cv_qualifier_list
                    | &
                    | complete_class_name DOUBLECOLON * cv_qualifier_list
                    | complete_class_name DOUBLECOLON *
    '''


def p_cv_qualifier_list(p):
    '''cv_qualifier_list : cv_qualifier cv_qualifier_list
                         | cv_qualifier
    '''


def p_cv_qualifier(p):
    '''cv_qualifier : const
                    | volatile
    '''


def p_dname(p):
    '''dname : name
             | class_name
             | ~ class_name
             | typedef_name
             | qualified_type_name
    '''


def p_type_name(p):
    '''type_name : type_specifier_list abstract_declarator
                 | type_specifier_list
    '''


def p_type_specifier_list(p):
    '''type_specifier_list : type_specifier type_specifier_list
                           | type_specifier
    '''


def p_abstract_declarator(p):
    '''abstract_declarator : ptr_operator abstract_declarator
                           | ptr_operator
                           | abstract_declarator LPAREN argument_declaration_list  RPAREN  cv_qualifier_list
                           | LPAREN argument_declaration_list  RPAREN  cv_qualifier_list
                           | abstract_declarator LPAREN argument_declaration_list  RPAREN
                           | LPAREN argument_declaration_list  RPAREN
                           | abstract_declarator LSPAREN constant_expression RSPAREN
                           | LSPAREN constant_expression RSPAREN
                           | abstract_declarator LSPAREN RSPAREN
                           | LSPAREN RSPAREN
                           | LPAREN abstract_declarator  RPAREN
    '''


def p_argument_declaration_list(p):
    '''argument_declaration_list : arg_declaration_list ...
                                 | ...
                                 | 
                                 | arg_declaration_list COMMA ...
    '''


def p_arg_declaration_list(p):
    '''arg_declaration_list : argument_declaration
                            | arg_declaration_list COMMA argument_declaration
    '''


def p_argument_declaration(p):
    '''argument_declaration : decl_specifiers declarator
                            | decl_specifiers declaratorEQUAL expression
                            | decl_specifiers abstract_declarator
                            | decl_specifiers
                            | decl_specifiers abstract_declaratorEQUAL expression
                            | decl_specifiersEQUAL expression
    '''


def p_function_definition(p):
    '''function_definition : decl_specifiers declarator ctor_initializer fct_body
                           | declarator ctor_initializer fct_body
                           | decl_specifiers declarator fct_body
                           | declarator fct_body
    '''


def p_fct_body(p):
    '''fct_body : compound_statement'''
    
def p_initializer(p):
    '''initializer : EQUAL assignment_expression
                   | EQUAL LCPAREN initializer_list RCPAREN
                   | EQUAL LCPAREN initializer_list COMMA RCPAREN
                   | LPAREN expression_list  RPAREN
    '''


def p_initializer_list(p):
    '''initializer_list : assignment_expression
                        | initializer_list COMMA assignment_expression
                        | LCPAREN initializer_list RCPAREN
                        | LCPAREN initializer_list COMMA RCPAREN
    '''


def p_class_specifier(p):
    '''class_specifier : class_head LCPAREN member_list RCPAREN
                       | class_head LCPAREN RCPAREN
    '''

def p_class_head(p):
    '''class_head : class_key IDENTIFIER base_spec
                  | class_key base_spec
                  | class_key IDENTIFIER
                  | class_key
                  | class_key class_name base_spec
                  | class_key class_name
    '''

def p_member_list(p):
    '''member_list : member_declaration member_list
                   | member_declaration
                   | access_specifier COLON member_list
                   | access_specifier COLON
    '''

def p_member_declaration(p):
    '''member_declaration : decl_specifiers member_declarator_list SEMICOLON
                          | member_declarator_list SEMICOLON
                          | decl_specifiers SEMICOLON
                          | SEMICOLON
                          | function_definition SEMICOLON
                          | function_definition
                          | qualified_name SEMICOLON
    '''

def p_member_declarator_list(p):
    '''member_declarator_list : member_declarator
                              | member_declarator_list COMMA member_declarator
    '''

def p_member_declarator(p):
    '''member_declarator : declarator pure_specifier
                         | declarator
                         | IDENTIFIER COLON constant_expression
                         | COLON constant_expression
    '''

def p_pure_specifier(p):
    '''pure_specifier : EQUAL integer_constant'''

def p_base_spec(p):
    '''base_spec : COLON base_list'''

def p_base_list(p):
    '''base_list : base_specifier
                 | base_list COMMA base_specifier
    '''

def p_base_specifier(p):
    '''base_specifier : complete_class_name
                      | virtual access_specifier complete_class_name
                      | virtual complete_class_name
                      | access_specifier virtual complete_class_name
                      | access_specifier complete_class_name
    '''

def p_access_specifier(p):
    '''access_specifier : private
                        | protected
                        | public
    '''

def p_conversion_function_name(p):
    '''conversion_function_name : operator conversion_type_name'''

def p_conversion_type_name(p):
    '''conversion_type_name : type_specifier_list ptr_operator
                            | type_specifier_list
    '''

def p_ctor_initializer(p):
    '''ctor_initializer : COLON mem_initializer_list'''

def p_mem_initializer_list(p):
    '''mem_initializer_list : mem_initializer
                            | mem_initializer COMMA mem_initializer_list
    '''

def p_mem_initializer(p):
    '''mem_initializer : complete_class_name LPAREN expression_list  RPAREN
                       | complete_class_name LPAREN  RPAREN
                       | IDENTIFIER LPAREN expression_list  RPAREN
                       | IDENTIFIER LPAREN  RPAREN
    '''

def p_operator_function_name(p):
    '''operator_function_name : operator operator_name'''

def p_operator_name(p):
    '''operator_name : new
                     | delete
                     | +
                     | _
                     | *
                     | /
                     | %
                     | ^
                     | &
                     | |
                     | ~
                     | !
                     | EQUAL
                     | <
                     | >
                     | +=
                     | _=
                     | *=
                     | /=
                     | %=
                     | ^=
                     | &=
                     | ~=
                     | <<
                     | >>
                     | >>=
                     | <<=
                     | EQCOMP
                     | NEQCOMP
                     | <=
                     | >=
                     | &&
                     | ||
                     | ++
                     | __
                     | COMMA
                     | _>*
                     | _>
                     | LPAREN  RPAREN
                     | LSPAREN RSPAREN
    '''

def p_statement(p):
    '''statement : labeled_statement
                 | expression_statement
                 | compound_statement
                 | selection_statement
                 | iteration_statement
                 | jump_statement
                 | declaration_statement
                 | try_block
    '''

def p_labeled_statement(p):
    '''labeled_statement : IDENTIFIER COLON statement
                         | case constant_expression COLON statement
                         | default COLON statement
    '''

def p_expression_statement(p):
    '''expression_statement : expression SEMICOLON
                            | SEMICOLON
    '''

def p_compound_statement(p):
    '''compound_statement : LCPAREN statement_list RCPAREN
                          | LCPAREN RCPAREN
    '''

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement
    '''

def p_selection_statement(p):
    '''selection_statement : if LPAREN expression  RPAREN  statement
                           | if LPAREN expression  RPAREN  statement else statement
                           | switch LPAREN expression  RPAREN  statement
    '''

def p_iteration_statement(p):
    '''iteration_statement : while LPAREN expression  RPAREN  statement
                           | do statement while LPAREN expression  RPAREN  SEMICOLON
                           | for LPAREN for_init_statement expression SEMICOLON expression  RPAREN  statement
                           | for LPAREN for_init_statement SEMICOLON expression  RPAREN  statement
                           | for LPAREN for_init_statement expression SEMICOLON  RPAREN  statement
                           | for LPAREN for_init_statement SEMICOLON  RPAREN  statement
    '''

def p_for_init_statement(p):
    '''for_init_statement : expression_statement
                          | declaration_statement
    '''

def p_jump_statement(p):
    '''jump_statement : break SEMICOLON
                      | continue SEMICOLON
                      | return expression SEMICOLON
                      | return SEMICOLON
                      | goto IDENTIFIER SEMICOLON
    '''

def p_declaration_statement(p):
    '''declaration_statement : declaration'''

def p_template_declaration(p):
    '''template_declaration : template < template_argument_list > declaration'''

def p_template_argument_list(p):
    '''template_argument_list : template_argument
                              | template_argument_list COMMA template_argument
    '''

def p_template_argument(p):
    '''template_argument : type_argument
                         | argument_declaration
    '''

def p_type_argument(p):
    '''type_argument : class IDENTIFIER'''

def p_template_class_name(p):
    '''template_class_name : template_name < template_arg_list >'''

def p_template_arg_list(p):
    '''template_arg_list : template_arg
                         | template_arg_list COMMA template_arg
    '''

def p_template_arg(p):
    '''template_arg : expression
                    | type_name
    '''

def p_try_block(p):
    '''try_block : try compound_statement handler_list'''

def p_handler_list(p):
    '''handler_list : handler handler_list
                    | handler
    '''

def p_handler(p):
    '''handler : catch LPAREN exception_declaration  RPAREN  compound_statement'''

def p_exception_declaration(p):
    '''exception_declaration : type_specifier_list declarator
                             | type_specifier_list abstract_declarator
                             | type_specifier_list
                             | ...
    '''

def p_throw_expression(p):
    '''throw_expression : throw expression
                        | throw
    '''

def p_exception_specification(p):
    '''exception_specification : throw LPAREN type_list  RPAREN
                               | throw LPAREN  RPAREN
    '''

def p_type_list(p):
    '''type_list : type_name
                 | type_list COMMA type_name
    '''

