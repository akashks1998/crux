from ply import lex
import re
import sys

#Personal Groups

keywords = {
    'auto':'AUTO',
    'break':'BREAK',
    'case':'CASE',
    'catch':'CATCH',
    'char':'CHAR',
    'class':'CLASS',
    'const':'CONST',
    'continue':'CONTINUE',
    'default':'DEFAULT',
    'delete':'DELETE',
    'do':'DO',
    'double':'DOUBLE',
    'else':'ELSE',
    'enum':'ENUM',
    'extern':'EXTERN',
    'float':'FLOAT',
    'for':'FOR',
    'goto':'GOTO',
    'if':'IF',
    'int':'INT',
    'long':'LONG',
    'new':'NEW',
    'private': 'PRIVATE',
    'protected':'PROTECTED',
    'public' : 'PUBLIC',
    'register': 'REGISTER',
    'return':'RETURN',
    'short':'SHORT',
    'signed':'SIGNED',
    'sizeof':'SIZEOF',
    'static':'STATIC',
    'switch':'SWITCH',
    'struct' : 'STRUCT',
    'typedef':'TYPEDEF',
    'template' : 'TEMPLATE',
    'union':'UNION',
    'unsigned':'UNSIGNED',
    'void':'VOID',
    'volatile':'VOLATILE',
    'while':'WHILE'
}

# List of token names. 
tokens = [
        # id and no
        'IDENTIFIER',
        'NUMBER',

        'RIGHT_ASSIGN',
        'LEFT_ASSIGN',
        'ADD_ASSIGN',
        'SUB_ASSIGN',
        'MUL_ASSIGN',
        'DIV_ASSIGN',
        'MOD_ASSIGN',
        'AND_ASSIGN',
        'XOR_ASSIGN',
        'OR_ASSIGN',
        'RIGHT_OP',
        'LEFT_OP',
        'INC_OP',
        'DEC_OP',
        'PTR_OP',
        'AND_OP',
        'OR_OP',
        'LE_OP',
        'GE_OP',
        'EQ_OP',
        'NE_OP',
        'ELLIPSIS',


        'PLUSOP',
        'MINUSOP',
        'DIVOP',
        'MULTOP',
        'MODOP',
        'XOROP',
        'BOROP',
        'BANDOP',
        'BNOP',
        'GTCOMP',
        'LTCOMP',
        'EQUAL',
        'LRPAREN',
        'RRPAREN',
        'LCPAREN',
        'RCPAREN',
        'LSPAREN',
        'RSPAREN',
        'SQUOTE',
        'DQUOTE',
        'COMMA',
        'DOT',
        'SEMICOLON',
        'COLON',
        'SCHAR',
        'STRING_LITERAL',
        'HASHTAG',
        'NOTSYM',
        'QUESMARK',

       

] + list(keywords.values())

# Regular expression rules for simple tokens

# RegEx id
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = keywords.get(t.value, 'IDENTIFIER')
    return t

def t_NUMBER(t):
    #r'((\d+\.\d+[eE]([+-])?\d+)|(\d+[eE]([+-])?\d+)|(\d+\.\d+)|(\.\d+)|(\d+))'
    r'(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?'
    t.value=float(t.value)
    return t

t_ELLIPSIS = r'\.\.\.'
t_RIGHT_ASSIGN = r'>>='
t_LEFT_ASSIGN = r'<<='
t_ADD_ASSIGN = r'\+='
t_SUB_ASSIGN = r'-='
t_MUL_ASSIGN = r'\*='
t_DIV_ASSIGN = r'/='
t_MOD_ASSIGN = r'%='
t_AND_ASSIGN = r'&='
t_XOR_ASSIGN = r'^='
t_OR_ASSIGN = r'\|='
t_RIGHT_OP = r'>>'
t_LEFT_OP = r'<<'
t_INC_OP = r'\+\+'
t_DEC_OP = r'--'
t_PTR_OP = r'->'
t_AND_OP = r'&&'
t_OR_OP = r'\|\|'
t_LE_OP = r'<='
t_GE_OP = r'>='
t_EQ_OP = r'=='
t_NE_OP = r'!='

# Arithematic Operator
t_PLUSOP    = r'\+'
t_MINUSOP   = r'-'
t_DIVOP     = r'/'
t_MULTOP    = r'\*'
t_MODOP     = r'\%'
t_XOROP     = r'\^'

t_BOROP     = r'\|'
t_BANDOP    = r'\&'
t_BNOP      = r'\~'

# Comparison Operator

t_GTCOMP    = r'>'
t_LTCOMP    = r'<'
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

# Other
t_COMMA         = r','
t_DOT           = r'\.'
t_SEMICOLON     = r';'
t_COLON         = r':'
t_SCHAR         = r'\'.\''
t_STRING_LITERAL        = r'\".*\"'
t_HASHTAG       = r'\#'
t_NOTSYM        = r'\!'
t_QUESMARK       = r'\?'



# track line no.
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# comment
def t_COMMENT(t):
    r'( (//)[^\n\r]* ) |(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)'
    t.value = str(t.value)
    t.type = 'COMMENT'
    pass


# A STRING_LITERAL containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    tk = re.split('[ \t]', t.value)[0]
    print("Illegal token '%s'" % tk)
    t.lexer.skip(len(tk))

# Build the lexer
lexer = lex.lex(debug = 0)



def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1
    
if __name__ == "__main__":
    

    for arg in arglist[1:]:
        if arg.split('=')[0] == "--cfg" :
            cfg_file=arg.split('=')[1]
        elif arg.split('=')[0] == "--output" :
            output_file=arg.split('=')[1]
        else:
            input_file=arg

    color_dict={}
    with open(cfg_file, "r") as f:
        for line in f:
            if line:
                (key,val) = line.split(':')
                color_dict[str(key).strip()] = str(val).strip()

    

    lines=[]
    with open(input_file, "r") as f:
        for line in f:
            lines.append(line)
    code = ''.join(lines)
    #print(code)
    lexer.input(code)

    meta_bgcolor = color_dict.get("META_BGCOLOR", "#121e1f")
    bold_token = keywords
    code_out = "<html><body bgcolor=\"" + meta_bgcolor + "\"><div><pre>\n"
    cur=1
    prev=1
    for tok in lexer:
        line = tok.lineno
        if prev != line :
            cur=1
            code_out += "\n"*(line-prev)
            prev=line
        col = find_column(code, tok)
        bold = bold_token.get(tok.value, "")
        if bold != "":
            bold = "; font-weight: bold"
            keyword_def= color_dict.get("KEYWORDS", "rgb(170,170,170)")
            color = color_dict.get(str(tok.type), keyword_def)
        else:
            color = color_dict.get(str(tok.type), "rgb(170,170,170)")
        
        span = "<span style=\"color: " + color + bold + "\">"
        code_out = code_out + " "*(col-cur) + span + tok.value + "</span>"
        cur=col + len(str(tok.value))
    code_out = code_out + "\n</pre></div></body></html>"

    with open(output_file, "w") as f:
        f.write(code_out)
