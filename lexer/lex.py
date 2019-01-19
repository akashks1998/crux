import ply.lex as lex

# List of token names. 
tokens = (
        # Keywords
        'AND',
        'AND_EQ',
        'ASM',
        'AUTO',
        'BITAND',
        'BITOR',
        'BOOL',
        'BREAK',
        'CASE',
        'CATCH',
        'CHAR',
        'CHAR8_T',
        'CHAR16_T',
        'CHAR32_T',
        'CLASS',
        'COMPL',
        'CONST',
        'CONTINUE',
        'DEFAULT',
        'DELETE',
        'DO',
        'DOUBLE',
        'ELSE',
        'ENUM',
        'EXTERN',
        'FALSE',
        'FLOAT',
        'FOR',
        'GOTO',
        'IF',
        'INLINE',
        'INT',
        'LONG',
        'NAMESPACE',
        'NEW',
        'NOT',
        'NOT_EQ',
        'NULLPTR',
        'OR',
        'OR_EQ',
        'PRIVATE',
        'PROTECTED',
        'PUBLIC',
        'RETURN',
        'SHORT',
        'SIGNED',
        'SIZEOF',
        'STATIC',
        'SWITCH',
        'THIS',
        'THROW',
        'TRUE',
        'TRY',
        'TYPEDEF',
        'UNION',
        'UNSIGNED',
        'VIRTUAL',
        'VOID',
        'VOLATILE',
        'WHILE',
        'XOR',
        'XOR_EQ',

        #Non Keywords
        'ID',
        'NUMBER',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
)


# Regular expression rules for simple tokens

# Keywords
t_AND			= r'and'
t_AND_EQ		= r'and_eq'
t_ASM			= r'asm'
t_AUTO			= r'auto'
t_BITAND		= r'bitand'
t_BITOR			= r'bitor'
t_BOOL			= r'bool'
t_BREAK			= r'break'
t_CASE			= r'case'
t_CATCH			= r'catch'
t_CHAR			= r'char'
t_CHAR8_T		= r'char8_t'
t_CHAR16_T		= r'char16_t'
t_CHAR32_T		= r'char32_t'
t_CLASS			= r'class'
t_COMPL			= r'compl'
t_CONST			= r'const'
t_CONTINUE		= r'continue'
t_DEFAULT		= r'default'
t_DELETE		= r'delete'
t_DO			= r'do'
t_DOUBLE		= r'double'
t_ELSE			= r'else'
t_ENUM			= r'enum'
t_EXTERN		= r'extern'
t_FALSE			= r'false'
t_FLOAT			= r'float'
t_FOR			= r'for'
t_GOTO			= r'goto'
t_IF			= r'if'
t_INLINE		= r'inline'
t_INT			= r'int'
t_LONG			= r'long'
t_NAMESPACE		= r'namespace'
t_NEW			= r'new'
t_NOT			= r'not'
t_NOT_EQ		= r'not_eq'
t_NULLPTR		= r'nullptr'
t_OR			= r'or'
t_OR_EQ			= r'or_eq'
t_PRIVATE		= r'private'
t_PROTECTED		= r'protected'
t_PUBLIC		= r'public'
t_RETURN		= r'return'
t_SHORT			= r'short'
t_SIGNED		= r'signed'
t_SIZEOF		= r'sizeof'
t_STATIC		= r'static'
t_SWITCH		= r'switch'
t_THIS			= r'this'
t_THROW			= r'throw'
t_TRUE			= r'true'
t_TRY			= r'try'
t_TYPEDEF		= r'typedef'
t_UNION			= r'union'
t_UNSIGNED		= r'unsigned'
t_VIRTUAL		= r'virtual'
t_VOID			= r'void'
t_VOLATILE		= r'volatile'
t_WHILE			= r'while'
t_XOR			= r'xor'
t_XOR_EQ		= r'xor_eq'


# RegEx for simple tokens
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'

# RegEx id
def t_ID(t):
    r'\w+'
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

if __name__ == "__main__":
    input_code = input()
    lexer.input(input_code)

    print('{:>12} {:>12} {:>12} {:>12}'.format('Type', 'Value', 'Lineno', 'Lexpos'))
    for tok in lexer:
        print('{:>12} {:>12} {:>12} {:>12}'.format(tok.type, tok.value, tok.lineno, tok.lexpos))

