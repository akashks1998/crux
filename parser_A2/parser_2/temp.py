def p_class_specifier(p):
    '''class_specifier : class IDENTIFIER LCPAREN final_class_list RCPAREN
                        | class LCPAREN final_class_list RCPAREN
                        | class IDENTIFIER
    '''

def p_class(p):
    '''class : CLASS '''

def p_final_class_list(p):
    ''' final_class_list : class_list
                         | PUBLIC COLON class_list PRIVATE COLON class_list
                         | PRIVATE COLON class_list PUBLIC COLON class_list
                         | PUBLIC COLON class_list 
                         | PRIVATE COLON class_list
    
    
    '''

def p_class_list(p):
    '''class_list : class_declaration
                  | class_declaration_list class_declaration

    '''


def p_class_declaration(p):
    '''class_declaration : specifier_qualifier_list class_declarator_list SEMICOLON
                         | function_defination

    '''


def p_specifier_qualifier_list(p):
    '''specifier_qualifier_list : type_specifier specifier_qualifier_list
                               | type_specifier
                               | type_qualifier specifier_qualifier_list
                               | type_qualifier

    '''


def p_class_declarator_list(p):
    '''class_declarator_list : class_declarator
                             | class_declarator_list COMMA class_declarator

    '''


def p_class_declarator(p):
    '''class_declarator : declarator
                        | COLON constant_expression
                        | declarator COLON constant_expression

    '''