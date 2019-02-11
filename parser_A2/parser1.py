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

def p_expression_list(p):
    '''expression_list : assignment_expression
                       | expression_list , assignment_expression
    '''

