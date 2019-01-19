from ply import lex
from ply import yacc
import re

#Personal Groups
op='-+/*&|%!~^' # pattern to detect operators for separation b/n nos

# Token names.
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

        # id and no
        'ID',
        'NUMBER',

        # arithematic operator
        'PLUSOP',
        'MINUSOP',
        'DIVOP',
        'MULTOP',
        'BOROP',
        'OROP',
        'BANDOP',
        'ANDOP',
        'MODOP',
        'PLUSEQOP',
        'MINUSEQOP',
        'MULTEQOP',
        'DIVEQOP',
        'BANDEQOP',
        'XOROP',
        'XOREQOP',
        'UPLUSOP',
        'UMINUSOP',
        'EXPOP',
        'BNOP',

        #comparison operator, =
        'EQCOMP',
        'NEQCOMP',
        'GTCOMP',
        'GTECOMP',
        'LTCOMP',
        'LTECOMP',
        'EQUAL',

        # Parenthesis
        'LRPAREN',
        'RRPAREN',
        'LCPAREN',
        'RCPAREN',
        'LSPAREN',
        'RSPAREN',

        # Quotes
        'SQUOTE',
        'DQUOTE',

        # Comment
        'SLCOMMENT',
        'LMLCOMMENT',
        'RMLCOMMENT',
        'LDCOMMENT',
        'RDCOMMENT',
)

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



# RegEx id
def t_ID(t):
    r'[a-zA-Z_]\w+'
    return t

def t_NUMBER(t):
    #r'((\d+\.\d+[eE]([+-])?\d+)|(\d+[eE]([+-])?\d+)|(\d+\.\d+)|(\.\d+)|(\d+))'
    r'(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?'
    return t

# Arithematic Operator
t_PLUSOP    = r'\+'
t_MINUSOP   = r'-'
t_DIVOP     = r'/'
t_MULTOP    = r'\*'
t_BOROP     = r'\|'
t_OROP      = r'\|\|'
t_BANDOP    = r'\&'
t_ANDOP     = r'\&\&'
t_MODOP     = r'\%'
t_PLUSEQOP  = r'\+='
t_MINUSEQOP = r'-='
t_MULTEQOP  = r'\*='
t_DIVEQOP   = r'/='
t_BANDEQOP  = r'\&\='
t_XOROP     = r'\^'
t_XOREQOP   = r'\^='
t_UPLUSOP   = r'\+\+'
t_UMINUSOP  = r'--'
t_EXPOP     = r'\*\*'
t_BNOP      = r'\~'

# Comparison Operator
t_EQCOMP    = r'=='
t_NEQCOMP   = r'!='
t_GTCOMP    = r'>'
t_GTECOMP   = r'>='
t_LTCOMP    = r'<'
t_LTECOMP   = r'<='
t_EQUAL     = r'='

# Parenthesis
t_LRPAREN   = r'\('
t_RRPAREN   = r'\)'
t_LCPAREN   = r'\{'
t_RCPAREN   = r'\}'
t_LSPAREN   = r'\['
t_RSPAREN   = r'\]'

# Quotes
t_SQUOTE    = r'\''
t_DQUOTE    = r'\"'

# Comment
t_SLCOMMENT  = r'//'
t_LMLCOMMENT = r'/\*'
t_RMLCOMMENT = r'\*/'
t_LDCOMMENT  = r'/\*\*'
t_RDCOMMENT  = r'\*\*/'

# track line no.
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignore
t_ignore = ' \t'

# Error handling
def t_error(t):
    tk = re.split('[ \t]', t.value)[0]
    print("Illegal token '%s'" % tk)
    t.lexer.skip(len(tk))

# Build lexer
lexer = lex.lex()
