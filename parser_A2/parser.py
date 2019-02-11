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
                          | :: IDENTIFIER
                          | :: operator_function_id
                          | :: qualified_id
                          | ( expression )
                          | id_expression
    '''

def p_id_expression(p):
    '''id_expression : unqualified_id
                     | qualified_id
    '''
def p_unqualified_id(p):
    '''unqualified_id : IDENTIFIER
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
                          | typename ::opt nested_name_specifier IDENTIFIER ( expression_listopt )
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
########################################################################
########################## Key words ###################################
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
#################################### Expression and Statement ##########


def p_expression_list(p):
    '''expression_list : assignment_expression
                       | expression_list , assignment_expression
    '''


def p_pseudo_destructor_name(p):
    '''pseudo_destructor_name : ::opt nested_name_specifieropt type_name :: ~ type_name
                              | ::opt nested_name_specifier template template_id :: ~ type_name
                              | ::opt nested_name_specifieropt ~ type_name
    '''


def p_unary_expression(p):
    '''unary_expression : postfix_expression
                        | ++ cast_expression
                        | -- cast_expression
                        | unary_operator cast_expression
                        | sizeof unary_expression
                        | sizeof ( type_id )
                        | new_expression
                        | delete_expression
    '''


def p_unary_operator(p):
    '''unary_operator : * & + _ ! ~'''
def p_new_expression(p):
    '''new_expression : ::opt new new_placementopt new_type_id new_initializeropt
                      | ::opt new new_placementopt ( type_id ) new_initializeropt
    '''


def p_new_placement(p):
    '''new_placement : ( expression_list )'''
def p_new_type_id(p):
    '''new_type_id : type_specifier_seq new_declaratoropt'''
def p_new_declarator(p):
    '''new_declarator : ptr_operator new_declaratoropt
                      | direct_new_declarator
    '''


def p_direct_new_declarator(p):
    '''direct_new_declarator : [ expression ]
                             | direct_new_declarator [ constant_expression ]
    '''


def p_new_initializer(p):
    '''new_initializer : ( expression_listopt )'''
def p_delete_expression(p):
    '''delete_expression : ::opt delete cast_expression
                         | ::opt delete [ ] cast_expression
    '''


def p_cast_expression(p):
    '''cast_expression : unary_expression
                       | ( type_id ) cast_expression
    '''


def p_pm_expression(p):
    '''pm_expression : cast_expression
                     | pm_expression .* cast_expression
                     | pm_expression _>* cast_expression
    '''


def p_multiplicative_expression(p):
    '''multiplicative_expression : pm_expression
                                 | multiplicative_expression * pm_expression
                                 | multiplicative_expression / pm_expression
                                 | multiplicative_expression % pm_expression
    '''


def p_additive_expression(p):
    '''additive_expression : multiplicative_expression
                           | additive_expression + multiplicative_expression
                           | additive_expression _ multiplicative_expression
    '''


def p_shift_expression(p):
    '''shift_expression : additive_expression
                        | shift_expression << additive_expression
                        | shift_expression >> additive_expression
    '''


def p_relational_expression(p):
    '''relational_expression : shift_expression
                             | relational_expression < shift_expression
                             | relational_expression > shift_expression
                             | relational_expression <= shift_expression
                             | relational_expression >= shift_expression
    '''


def p_equality_expression(p):
    '''equality_expression : relational_expression
                           | equality_expression == relational_expression
                           | equality_expression != relational_expression
    '''


def p_and_expression(p):
    '''and_expression : equality_expression
                      | and_expression & equality_expression
    '''


def p_exclusive_or_expression(p):
    '''exclusive_or_expression : and_expression
                               | exclusive_or_expression ^ and_expression
    '''


def p_inclusive_or_expression(p):
    '''inclusive_or_expression : exclusive_or_expression
                               | inclusive_or_expression | exclusive_or_expression
    '''


def p_logical_and_expression(p):
    '''logical_and_expression : inclusive_or_expression
                              | logical_and_expression && inclusive_or_expression
    '''


def p_logical_or_expression(p):
    '''logical_or_expression : logical_and_expression
                             | logical_or_expression || logical_and_expression
    '''


def p_conditional_expression(p):
    '''conditional_expression : logical_or_expression
                              | logical_or_expression ? expression : assignment_expression
    '''


def p_assignment_expression(p):
    '''assignment_expression : conditional_expression
                             | logical_or_expression assignment_operator assignment_expression
                             | throw_expression
    '''


def p_assignment_operator(p):
    '''assignment_operator : = *= /= %= += _= >>= <<= &= ^= |='''


def p_expression(p):
    '''expression : assignment_expression
                  | expression , assignment_expression
    '''


def p_constant_expression(p):
    '''constant_expression : conditional_expression'''
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
    '''labeled_statement : IDENTIFIER : statement
                         | case constant_expression : statement
                         | default : statement
    '''


def p_expression_statement(p):
    '''expression_statement : expressionopt ;'''
def p_compound_statement(p):
    '''compound_statement : { statement_seqopt }'''
def p_statement_seq(p):
    '''statement_seq : statement
                     | statement_seq statement
    '''




def p_selection_statement(p):
    '''selection_statement : if ( condition ) statement
                           | if ( condition ) statement else statement
                           | switch ( condition ) statement
    '''


def p_condition(p):
    '''condition : expression
                 | type_specifier_seq declarator = assignment_expression
    '''


def p_iteration_statement(p):
    '''iteration_statement : while ( condition ) statement
                           | do statement while ( expression ) ;
                           | for ( for_init_statement conditionopt ; expressionopt ) statement
    '''


def p_for_init_statement(p):
    '''for_init_statement : expression_statement
                          | simple_declaration
    '''


def p_jump_statement(p):
    '''jump_statement : break ;
                      | continue ;
                      | return expressionopt ;
                      | goto IDENTIFIER ;
    '''


def p_declaration_statement(p):
    '''declaration_statement : block_declaration'''
def p_declaration_seq(p):
    '''declaration_seq : declaration
                       | declaration_seq declaration
    '''


def p_declaration(p):
    '''declaration : block_declaration
                   | function_definition
                   | template_declaration
                   | explicit_instantiation
                   | explicit_specialization
                   | linkage_specification
                   | namespace_definition
    '''


def p_block_declaration(p):
    '''block_declaration : simple_declaration
                         | asm_definition
                         | namespace_alias_definition
                         | using_declaration
                         | using_directive
    '''


def p_simple_declaration(p):
    '''simple_declaration : decl_specifier_seqopt init_declarator_listopt ;'''
def p_decl_specifier(p):
    '''decl_specifier : storage_class_specifier
                      | type_specifier
                      | function_specifier
                      | friend
                      | typedef
    '''


def p_decl_specifier_seq(p):
    '''decl_specifier_seq : decl_specifier_seqopt decl_specifier'''
def p_storage_class_specifier(p):
    '''storage_class_specifier : auto
                               | register
                               | static
                               | extern
                               | mutable
    '''


def p_function_specifier(p):
    '''function_specifier : inline
                          | virtual
                          | explicit
    '''


def p_type_specifier(p):
    '''type_specifier : simple_type_specifier
                      | class_specifier
                      | enum_specifier
                      | elaborated_type_specifier
                      | cv_qualifier
    '''


def p_simple_type_specifier(p):
    '''simple_type_specifier : ::opt nested_name_specifieropt type_name
                             | ::opt nested_name_specifier templateopt template_id
                             | char
                             | wchar_t
                             | bool
                             | short
                             | int
                             | long
                             | signed
                             | unsigned
                             | float
                             | double
                             | void
    '''


def p_type_name(p):
    '''type_name : class_name
                 | enum_name
                 | typedef_name
    '''


def p_aborated_type_specifier(p):
    '''aborated_type_specifier : class_key ::opt nested_name_specifieropt IDENTIFIER
                               | enum ::opt nested_name_specifieropt IDENTIFIER
                               | typename ::opt nested_name_specifier IDENTIFIER
                               | typename ::opt nested_name_specifier templateopt template_id
    '''


def p_elaborated_type_specifier(p):
    '''elaborated_type_specifier : class_key ::opt nested_name_specifieropt IDENTIFIER
                                 | enum ::opt nested_name_specifieropt IDENTIFIER
                                 | typename ::opt nested_name_specifier IDENTIFIER
                                 | typename ::opt nested_name_specifier templateopt template_id
    '''



def p_enum_specifier(p):
    '''enum_specifier : enum identifieropt { enumerator_listopt }'''
def p_enumerator_list(p):
    '''enumerator_list : enumerator_definition
                       | enumerator_list , enumerator_definition
    '''


def p_enumerator_definition(p):
    '''enumerator_definition : enumerator
                             | enumerator = constant_expression
    '''


def p_enumerator(p):
    '''enumerator : IDENTIFIER'''


def p_namespace_definition(p):
    '''namespace_definition : named_namespace_definition
                            | unnamed_namespace_definition
    '''


def p_named_namespace_definition(p):
    '''named_namespace_definition : original_namespace_definition
                                  | extension_namespace_definition
    '''


def p_original_namespace_definition(p):
    '''original_namespace_definition : namespace IDENTIFIER { namespace_body }'''
def p_extension_namespace_definition(p):
    '''extension_namespace_definition : namespace original_namespace_name { namespace_body }'''
def p_unnamed_namespace_definition(p):
    '''unnamed_namespace_definition : namespace { namespace_body }'''
def p_namespace_body(p):
    '''namespace_body : declaration_seqopt'''

def p_namespace_alias_definition(p):
    '''namespace_alias_definition : namespace IDENTIFIER = qualified_namespace_specifier ;'''
def p_qualified_namespace_specifier(p):
    '''qualified_namespace_specifier : ::opt nested_name_specifieropt namespace_name'''
def p_using_declaration(p):
    '''using_declaration : using typenameopt ::opt nested_name_specifier unqualified_id ;
                         | using :: unqualified_id ;
    '''


def p_using_directive(p):
    '''using_directive : using namespace ::opt nested_name_specifieropt namespace_name ;'''
def p_asm_definition(p):
    '''asm_definition : asm ( string_literal ) ;'''
def p_linkage_specification(p):
    '''linkage_specification : extern string_literal { declaration_seqopt }
                             | extern string_literal declaration
    '''


#######################################################################
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

