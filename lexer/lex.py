from ply import *

# Token names.
tokens = (
        'ID',
        'PLUS',
        'MINUS',
        'TIMES',
        'DIVIDE',
)

# RegEx for simple tokens
t_ID        = r'\w+'
t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIVIDE    = r'/'

# RegEx id
def t_ID(t):
    r'\w+'
    return t

# track line no.
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignore
t_ignore = ' \t'

# Error handling
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build lexer
lexer = lex.lex()
