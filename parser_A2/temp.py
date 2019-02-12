











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


def p_init_declarator_list(p):
    '''init_declarator_list : init_declarator
                            | init_declarator_list , init_declarator
    '''


def p_init_declarator(p):
    '''init_declarator : declarator in'''
def p_declarator(p):
    '''declarator : direct_declarator
                  | ptr_operator declarator
    '''


def p_direct_declarator(p):
    '''direct_declarator : declarator_id
                         | direct_declarator ( parameter_declaration_clause ) cv_qualifier_seqopt exception_specificationopt
                         | direct_declarator [ constant_expressionopt ]
                         | ( declarator )
    '''


def p_ptr_operator(p):
    '''ptr_operator : * cv_qualifier_seqopt
                    | &
                    | ::opt nested_name_specifier * cv_qualifier_seqopt
    '''


def p_cv_qualifier_seq(p):
    '''cv_qualifier_seq : cv_qualifier cv_qualifier_seqopt'''
def p_cv_qualifier(p):
    '''cv_qualifier : const
                    | volatile
    '''


def p_declarator_id(p):
    '''declarator_id : ::opt id_expression
                     | ::opt nested_name_specifieropt type_name
    '''


def p_type_id(p):
    '''type_id : type_specifier_seq abstract_declaratoropt'''
def p_type_specifier_seq(p):
    '''type_specifier_seq : type_specifier type_specifier_seq
                          | type_specifier
    '''
def p_abstract_declarator(p):
    '''abstract_declarator : ptr_operator abstract_declaratoropt
                           | direct_abstract_declarator
    '''


def p_direct_abstract_declarator(p):
    '''direct_abstract_declarator : direct_abstract_declaratoropt ( parameter_declaration_clause ) cv_qualifier_seqopt exception_specificationopt
                                  | direct_abstract_declaratoropt
    '''



def p_direct_abstract_declaratoropt ( parameter_declaration_clause ) cv_qualifier_seqopt exception_specificationopt(p):
    '''direct_abstract_declaratoropt ( parameter_declaration_clause ) cv_qualifier_seqopt exception_specificationopt : direct_abstract_declaratoropt [ constant_expressionopt ]
                                                                                                                     | ( abstract_declarator )
    '''


def p_direct_abstract_declarator(p):
    '''direct_abstract_declarator : direct_abstract_declaratoropt ( parameter_declaration_clause ) cv_qualifier_seqopt exception_specificationopt
                                  | direct_abstract_declaratoropt [ constant_expressionopt ]
                                  | ( abstract_declarator )
    '''


def p_parameter_declaration_clause(p):
    '''parameter_declaration_clause : parameter_declaration_listopt ...opt
                                    | parameter_declaration_list , ...
    '''


def p_parameter_declaration_clause(p):
    '''parameter_declaration_clause : parameter_declaration_listopt ...opt
                                    | parameter_declaration_list , ...
    '''


def p_parameter_declaration_list(p):
    '''parameter_declaration_list : parameter_declaration
                                  | parameter_declaration_list , parameter_declaration
    '''


def p_parameter_declaration(p):
    '''parameter_declaration : decl_specifier_seq declarator
                             | decl_specifier_seq declarator = assignment_expression
                             | decl_specifier_seq abstract_declaratoropt
                             | decl_specifier_seq abstract_declaratoropt = assignment_expression
    '''




def p_function_definition(p):
    '''function_definition : decl_specifier_seqopt declarator ctor_initializeropt function_body
                           | decl_specifier_seqopt declarator function_try_block
    '''


def p_function_body(p):
    '''function_body : compound_statement'''
def p_initializer(p):
    '''initializer : = initializer_clause
                   | ( expression_list )
    '''

def p_initializer_clause(p):
    '''initializer_clause : assignment_expression
                          | { initializer_list ,opt }
                          | { }
    '''


def p_initializer_list(p):
    '''initializer_list : initializer_clause
                        | initializer_list , initializer_clause
    '''




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


def p_type_specifier_seq(p):
    '''type_specifier_seq : type_specifier type_specifier_seq
                          | type_specifier
    '''

def p_primary_expression(p):
    '''primary_expression : NUMBER
                          | STRING
                          | CHAR
                          | THIS
                          | DOUBLECOLON IDENTIFIER
                          | DOUBLECOLON operator_function_id
                          | DOUBLECOLON qualified_id
                          | LPAREN expression RPAREN
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
                      | BNOP class_name
                      | template_id
    '''

def p_qualified_id(p):
    '''qualified_id : nested_name_specifier TEMPLATE unqualified_id
                    | nested_name_specifier  unqualified_id
    '''

def p_nested_name_specifier(p):
    '''nested_name_specifier : class_or_namespace_name DOUBLECOLON nested_name_specifier
                             | class_or_namespace_name DOUBLECOLON 
                             | class_or_namespace_name DOUBLECOLON TEMPLATE nested_name_specifier
    '''

def p_class_or_namespace_name(p):
    '''class_or_namespace_name : class_name
                               | namespace_name
    '''


def p_postfix_expression(p):
    '''postfix_expression : primary_expression
                          | postfix_expression LSPAREN expression RSPAREN
                          | postfix_expression LPAREN expression_list RPAREN
                          | postfix_expression LPAREN  RPAREN
                          | simple_type_specifier LPAREN expression_list RPAREN
                          | simple_type_specifier LPAREN RPAREN
                          | typename DOUBLECOLONopt nested_name_specifier IDENTIFIER LPAREN expression_list RPAREN
                          | typename DOUBLECOLONopt nested_name_specifier IDENTIFIER LPAREN  RPAREN
                          | typename DOUBLECOLONopt nested_name_specifier templateopt template_id LPAREN expression_list RPAREN
                          | typename DOUBLECOLONopt nested_name_specifier templateopt template_id LPARENRPAREN
                          | postfix_expression DOT pseudo_destructor_name
                          | postfix_expression ARROW pseudo_destructor_name
                          | postfix_expression UPLUSOP
                          | postfix_expression UMINUSOP
                          | dynamic_cast LTCOMP type_id GTCOMP LPAREN expression RPAREN
                          | static_cast LTCOMP type_id  LPAREN expression RPAREN
                          | reinterpret_cast LTCOMP type_id GTCOMP LPAREN expression RPAREN
                          | const_cast LTCOMP type_id GTCOMP LPAREN expression RPAREN
                          | typeid LPAREN expression RPAREN
                          | typeid LPAREN type_id RPAREN
    '''



def p_expression_list(p):
    '''expression_list : assignment_expression
                       | expression_list COMMA assignment_expression
    '''


def p_pseudo_destructor_name(p):
    '''pseudo_destructor_name : BNOP type_name
    '''


##################


def p_unary_expression(p):
    '''unary_expression : postfix_expression
                        | UPLUSOP cast_expression
                        | UMINUSOP cast_expression
                        | unary_operator cast_expression
                        | SIZEOF unary_expression
                        | SIZEOF LPAREN type_id RPAREN
                        | new_expression
                        | delete_expression
    '''


def p_unary_operator(p):
    '''unary_operator : MULTOP
                      | BANDOP
                      | PLUSOP
                      | MINUSOP
                      | NOTSYM 
                      | BNOP
    '''

def p_new_expression(p):
    '''new_expression : DOUBLECOLON NEW new_placement new_type_id new_initializer
                      | NEW new_placement new_type_id new_initializer
                      | NEW new_placement new_type_id 
                      | NEW new_type_id new_initializer
                      | NEW new_type_id
                      | DOUBLECOLON NEW new_placement new_type_id
                      | DOUBLECOLON NEW new_type_id new_initializer
                      | DOUBLECOLON NEW new_type_id 
                      | DOUBLECOLON NEW new_placement LPAREN type_id RPAREN new_initializer
                      | NEW new_placement LPAREN type_id RPAREN new_initializer
                      | NEW new_placement LPAREN type_id RPAREN 
                      | NEW LPAREN type_id RPAREN new_initializer
                      | NEW LPAREN type_id RPAREN
                      | DOUBLECOLON NEW new_placement LPAREN type_id RPAREN
                      | DOUBLECOLON NEW LPAREN type_id RPAREN new_initializer
                      | DOUBLECOLON NEW LPAREN type_id RPAREN 
    '''

def p_new_placement(p):
    '''new_placement : LRPAREN  expression_list RRPAREN'''
def p_new_type_id(p):
    '''new_type_id : type_specifier_seq new_declarator
                    | type_specifier_seq
    '''
def p_new_declarator(p):
    '''new_declarator : ptr_operator new_declarator
                      | ptr_operator
                      | direct_new_declarator
    '''


def p_direct_new_declarator(p):
    '''direct_new_declarator : LSPAREN expression RSPAREN
                             | direct_new_declarator LSPAREN constant_expression RSPAREN
    '''


def p_new_initializer(p):
    '''new_initializer : LRPAREN  expression_list RRPAREN
                        |  LRPAREN   RRPAREN
    '''


def p_delete_expression(p):
    '''delete_expression : DOUBLECOLON delete cast_expression
                         | DELETE cast_expression
                         | DELETE LSPAREN RSPAREN cast_expression
                         | DOUBLECOLON DELETE LSPAREN RSPAREN cast_expression
    '''


####################

def p_cast_expression(p):
    '''cast_expression : unary_expression
                       | LRPAREN  type_id RRPAREN cast_expression
    '''


def p_pm_expression(p):
    '''pm_expression : cast_expression
                     | pm_expression DOTSTAR cast_expression
                     | pm_expression ARROWSTAR cast_expression
    '''

## SIMPLE ARITMETIC EXPR

def p_multiplicative_expression(p):
    '''multiplicative_expression : pm_expression
                                 | multiplicative_expression MULTOP pm_expression
                                 | multiplicative_expression DIVOP pm_expression
                                 | multiplicative_expression MODOP pm_expression
    '''


def p_additive_expression(p):
    '''additive_expression : multiplicative_expression
                           | additive_expression PLUSOP multiplicative_expression
                           | additive_expression MINUSOP multiplicative_expression
    '''


def p_shift_expression(p):
    '''shift_expression : additive_expression
                        | shift_expression LEFTSHIFT additive_expression
                        | shift_expression RIGHTSHIFT additive_expression
    '''


def p_relational_expression(p):
    '''relational_expression : shift_expression
                             | relational_expression LTCOMP shift_expression
                             | relational_expression GTCOMP shift_expression
                             | relational_expression LTECOMP shift_expression
                             | relational_expression GTECOMP shift_expression
    '''


def p_equality_expression(p):
    '''equality_expression : relational_expression
                           | equality_expression EQCOMP relational_expression
                           | equality_expression NEQCOMP relational_expression
    '''


def p_and_expression(p):
    '''and_expression : equality_expression
                      | and_expression BAND equality_expression
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
                              | logical_and_expression ANDOP inclusive_or_expression
    '''


def p_logical_or_expression(p):
    '''logical_or_expression : logical_and_expression
                             | logical_or_expression OROP logical_and_expression
    '''


def p_conditional_expression(p):
    '''conditional_expression : logical_or_expression
                              | logical_or_expression QUESMARK expression COLON assignment_expression
    '''


def p_assignment_expression(p):
    '''assignment_expression : conditional_expression
                             | logical_or_expression assignment_operator assignment_expression
                             | throw_expression
    '''


def p_assignment_operator(p):
    '''assignment_operator : EQUAL
                           | MULTEQOP 
                           | DIVEQOP
                           | MODQOP
                           | PLUSEQOP 
                           | MINUSEQOP
                           | LEFTQOP
                           | RIGHTQOP
                           | BANDEQOP
                           | B_I_OR
                           | B_E_OR
    '''


def p_expression(p):
    '''expression : assignment_expression
                  | expression COMMA assignment_expression
    '''


def p_constant_expression(p):
    '''constant_expression : conditional_expression'''
###########################################################################33
###############################################################################
############################################################################3
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
########################### OWN ################################################
def p_doublecolon_opt(p):
    '''doublecolon_opt : DOUBLECOLON'''
################################################################################
############################  Expressions   ####################################
################################################################################

def p_primary_expression(p):
    '''primary_expression : literal
                          | this
                          | DOUBLECOLON IDENTIFIER
                          | DOUBLECOLON operator_function_id
                          | DOUBLECOLON qualified_id
                          | LRPAREN  expression RRPAREN
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
                      | BNOP class_name
                      | template_id
    '''

def p_qualified_id(p):
    '''qualified_id : nested_name_specifier templateopt unqualified_id'''

def p_nested_name_specifier(p):
    '''nested_name_specifier : class_or_namespace_name DOUBLECOLON nested_name_specifieropt
                             | class_or_namespace_name DOUBLECOLON template nested_name_specifier
    '''

def p_class_or_namespace_name(p):
    '''class_or_namespace_name : class_name
                               | namespace_name
    '''


def p_postfix_expression(p):
    '''postfix_expression : primary_expression
                          | postfix_expression LSPAREN expression RSPAREN
                          | postfix_expression LRPAREN  expression_listopt RRPAREN
                          | simple_type_specifier LRPAREN  expression_listopt RRPAREN
                          | typename doublecolon_opt nested_name_specifier IDENTIFIER LRPAREN  expression_listopt RRPAREN
                          | typename doublecolon_opt nested_name_specifier templateopt template_id LRPAREN  expression_listopt RRPAREN
                          | postfix_expression DOT  templateopt doublecolon_opt id_expression
                          | postfix_expression ARROW templateopt doublecolon_opt id_expression
                          | postfix_expression DOT  pseudo_destructor_name
                          | postfix_expression ARROW pseudo_destructor_name
                          | postfix_expression DPLUSOP
                          | postfix_expression DMINUSOP
                          | dynamic_cast LTCOMP type_id RTCOMP LRPAREN  expression RRPAREN
                          | static_cast LTCOMP type_id RTCOMP LRPAREN  expression RRPAREN
                          | reinterpret_cast LTCOMP type_id RTCOMP LRPAREN  expression RRPAREN
                          | const_cast LTCOMP type_id RTCOMP LRPAREN  expression RRPAREN
                          | typeid LRPAREN  expression RRPAREN
                          | typeid LRPAREN  type_id RRPAREN
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
                       | expression_list COMMA assignment_expression
    '''


def p_pseudo_destructor_name(p):
    '''pseudo_destructor_name : doublecolon_opt nested_name_specifieropt type_name DOUBLECOLON BNOP type_name
                              | doublecolon_opt nested_name_specifier template template_id DOUBLECOLON BNOP type_name
                              | doublecolon_opt nested_name_specifieropt BNOP type_name
    '''


def p_unary_expression(p):
    '''unary_expression : postfix_expression
                        | DPLUSOP cast_expression
                        | DMINUSOP cast_expression
                        | unary_operator cast_expression
                        | sizeof unary_expression
                        | sizeof LRPAREN  type_id RRPAREN
                        | new_expression
                        | delete_expression
    '''


def p_unary_operator(p):
    '''unary_operator : MULTOP BANDOP PLUSOP MINUSOP NOTSYM BNOP'''
def p_new_expression(p):
    '''new_expression : doublecolon_opt new new_placementopt new_type_id new_initializeropt
                      | doublecolon_opt new new_placementopt LRPAREN  type_id RRPAREN new_initializeropt
    '''


def p_new_placement(p):
    '''new_placement : LRPAREN  expression_list RRPAREN'''
def p_new_type_id(p):
    '''new_type_id : type_specifier_seq new_declaratoropt'''
def p_new_declarator(p):
    '''new_declarator : ptr_operator new_declaratoropt
                      | direct_new_declarator
    '''


def p_direct_new_declarator(p):
    '''direct_new_declarator : LSPAREN expression RSPAREN
                             | direct_new_declarator LSPAREN constant_expression RSPAREN
    '''


def p_new_initializer(p):
    '''new_initializer : LRPAREN  expression_listopt RRPAREN'''
def p_delete_expression(p):
    '''delete_expression : doublecolon_opt delete cast_expression
                         | doublecolon_opt delete LSPAREN RSPAREN cast_expression
    '''


def p_cast_expression(p):
    '''cast_expression : unary_expression
                       | LRPAREN  type_id RRPAREN cast_expression
    '''


def p_pm_expression(p):
    '''pm_expression : cast_expression
                     | pm_expression DOTSTAR cast_expression
                     | pm_expression ARROWSTAR cast_expression
    '''


def p_multiplicative_expression(p):
    '''multiplicative_expression : pm_expression
                                 | multiplicative_expression MULTOP pm_expression
                                 | multiplicative_expression DIVOP pm_expression
                                 | multiplicative_expression MODOP pm_expression
    '''


def p_additive_expression(p):
    '''additive_expression : multiplicative_expression
                           | additive_expression PLUSOP multiplicative_expression
                           | additive_expression MINUSOP multiplicative_expression
    '''


def p_shift_expression(p):
    '''shift_expression : additive_expression
                        | shift_expression LSHIFT additive_expression
                        | shift_expression RSHIFT additive_expression
    '''


def p_relational_expression(p):
    '''relational_expression : shift_expression
                             | relational_expression LTCOMP shift_expression
                             | relational_expression RTCOMP shift_expression
                             | relational_expression LTECOMP shift_expression
                             | relational_expression RTECOMP shift_expression
    '''


def p_equality_expression(p):
    '''equality_expression : relational_expression
                           | equality_expression EQCOMP relational_expression
                           | equality_expression NEQCOMP relational_expression
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
                              | logical_and_expression ANDOP inclusive_or_expression
    '''


def p_logical_or_expression(p):
    '''logical_or_expression : logical_and_expression
                             | logical_or_expression OROP logical_and_expression
    '''


def p_conditional_expression(p):
    '''conditional_expression : logical_or_expression
                              | logical_or_expression QUESMARK expression COLON assignment_expression
    '''


def p_assignment_expression(p):
    '''assignment_expression : conditional_expression
                             | logical_or_expression assignment_operator assignment_expression
                             | throw_expression
    '''


def p_assignment_operator(p):
    '''assignment_operator : NEQCOMP MULTEQOP DIVEQOP MODEQOP PLUSEQOP MINUSEQOP RSHIFTEQOP LSHIFTEQOP BANDEQOP XOREQOP BOREQOP'''


def p_expression(p):
    '''expression : assignment_expression
                  | expression COMMA assignment_expression
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
    '''labeled_statement : IDENTIFIER COLON statement
                         | case constant_expression COLON statement
                         | default COLON statement
    '''


def p_expression_statement(p):
    '''expression_statement : expressionopt SEMICOLON'''
def p_compound_statement(p):
    '''compound_statement : LCPAREN  statement_seqopt RCPAREN'''
def p_statement_seq(p):
    '''statement_seq : statement
                     | statement_seq statement
    '''




def p_selection_statement(p):
    '''selection_statement : if LRPAREN  condition RRPAREN statement
                           | if LRPAREN  condition RRPAREN statement else statement
                           | switch LRPAREN  condition RRPAREN statement
    '''


def p_condition(p):
    '''condition : expression
                 | type_specifier_seq declarator NEQCOMP assignment_expression
    '''


def p_iteration_statement(p):
    '''iteration_statement : while LRPAREN  condition RRPAREN statement
                           | do statement while LRPAREN  expression RRPAREN SEMICOLON
                           | for LRPAREN  for_init_statement conditionopt SEMICOLON expressionopt RRPAREN statement
    '''


def p_for_init_statement(p):
    '''for_init_statement : expression_statement
                          | simple_declaration
    '''


def p_jump_statement(p):
    '''jump_statement : break SEMICOLON
                      | continue SEMICOLON
                      | return expressionopt SEMICOLON
                      | goto IDENTIFIER SEMICOLON
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
    '''simple_declaration : decl_specifier_seqopt init_declarator_listopt SEMICOLON'''
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
    '''simple_type_specifier : doublecolon_opt nested_name_specifieropt type_name
                             | doublecolon_opt nested_name_specifier templateopt template_id
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
    '''aborated_type_specifier : class_key doublecolon_opt nested_name_specifieropt IDENTIFIER
                               | enum doublecolon_opt nested_name_specifieropt IDENTIFIER
                               | typename doublecolon_opt nested_name_specifier IDENTIFIER
                               | typename doublecolon_opt nested_name_specifier templateopt template_id
    '''


def p_elaborated_type_specifier(p):
    '''elaborated_type_specifier : class_key doublecolon_opt nested_name_specifieropt IDENTIFIER
                                 | enum doublecolon_opt nested_name_specifieropt IDENTIFIER
                                 | typename doublecolon_opt nested_name_specifier IDENTIFIER
                                 | typename doublecolon_opt nested_name_specifier templateopt template_id
    '''

def p_enum_specifier(p):
    '''enum_specifier : enum identifieropt LCPAREN  enumerator_listopt RCPAREN'''

def p_enumerator_list(p):
    '''enumerator_list : enumerator_definition
                       | enumerator_list COMMA enumerator_definition
    '''


def p_enumerator_definition(p):
    '''enumerator_definition : enumerator
                             | enumerator NEQCOMP constant_expression
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
    '''original_namespace_definition : namespace IDENTIFIER LCPAREN  namespace_body RCPAREN'''
def p_extension_namespace_definition(p):
    '''extension_namespace_definition : namespace original_namespace_name LCPAREN  namespace_body RCPAREN'''
def p_unnamed_namespace_definition(p):
    '''unnamed_namespace_definition : namespace LCPAREN  namespace_body RCPAREN'''
def p_namespace_body(p):
    '''namespace_body : declaration_seqopt'''

def p_namespace_alias_definition(p):
    '''namespace_alias_definition : namespace IDENTIFIER NEQCOMP qualified_namespace_specifier SEMICOLON'''
def p_qualified_namespace_specifier(p):
    '''qualified_namespace_specifier : doublecolon_opt nested_name_specifieropt namespace_name'''
def p_using_declaration(p):
    '''using_declaration : using typenameopt doublecolon_opt nested_name_specifier unqualified_id SEMICOLON
                         | using DOUBLECOLON unqualified_id SEMICOLON
    '''


def p_using_directive(p):
    '''using_directive : using namespace doublecolon_opt nested_name_specifieropt namespace_name SEMICOLON'''
def p_asm_definition(p):
    '''asm_definition : asm LRPAREN  string_literal RRPAREN SEMICOLON'''
def p_linkage_specification(p):
    '''linkage_specification : extern string_literal LCPAREN  declaration_seqopt RCPAREN
                             | extern string_literal declaration
    '''


def p_init_declarator_list(p):
    '''init_declarator_list : init_declarator
                            | init_declarator_list COMMA init_declarator
    '''


def p_init_declarator(p):
    '''init_declarator : declarator in'''
def p_declarator(p):
    '''declarator : direct_declarator
                  | ptr_operator declarator
    '''


def p_direct_declarator(p):
    '''direct_declarator : declarator_id
                         | direct_declarator LRPAREN  parameter_declaration_clause RRPAREN cv_qualifier_seqopt exception_specificationopt
                         | direct_declarator LSPAREN constant_expressionopt RSPAREN
                         | LRPAREN  declarator RRPAREN
    '''


def p_ptr_operator(p):
    '''ptr_operator : MULTOP cv_qualifier_seqopt
                    | BAND
                    | doublecolon_opt nested_name_specifier MULTOP cv_qualifier_seqopt
    '''


def p_cv_qualifier_seq(p):
    '''cv_qualifier_seq : cv_qualifier cv_qualifier_seqopt'''
def p_cv_qualifier(p):
    '''cv_qualifier : const
                    | volatile
    '''


def p_declarator_id(p):
    '''declarator_id : doublecolon_opt id_expression
                     | doublecolon_opt nested_name_specifieropt type_name
    '''


def p_type_id(p):
    '''type_id : type_specifier_seq abstract_declaratoropt'''
    
def p_type_specifier_seq(p):
    '''type_specifier_seq : type_specifier type_specifier_seqopt'''

def p_direct_abstract_declarator(p):
    '''direct_abstract_declarator : direct_abstract_declaratoropt LRPAREN  parameter_declaration_clause RRPAREN cv_qualifier_seqopt exception_specificationopt
                                  | direct_abstract_declaratoropt LSPAREN constant_expressionopt RSPAREN
                                  | LRPAREN  abstract_declarator RRPAREN
    '''

def p_parameter_declaration_list(p):
    '''parameter_declaration_list : parameter_declaration
                                  | parameter_declaration_list COMMA parameter_declaration
    '''


def p_parameter_declaration(p):
    '''parameter_declaration : decl_specifier_seq declarator
                             | decl_specifier_seq declarator NEQCOMP assignment_expression
                             | decl_specifier_seq abstract_declaratoropt
                             | decl_specifier_seq abstract_declaratoropt NEQCOMP assignment_expression
    '''




def p_function_definition(p):
    '''function_definition : decl_specifier_seqopt declarator ctor_initializeropt function_body
                           | decl_specifier_seqopt declarator function_try_block
    '''


def p_function_body(p):
    '''function_body : compound_statement'''
def p_initializer(p):
    '''initializer : NEQCOMP initializer_clause
                   | LRPAREN  expression_list RRPAREN
    '''

def p_initializer_clause(p):
    '''initializer_clause : assignment_expression
                          | LCPAREN  initializer_list COMMAopt RCPAREN
                          | LCPAREN  RCPAREN
    '''


def p_initializer_list(p):
    '''initializer_list : initializer_clause
                        | initializer_list COMMA initializer_clause
    '''




