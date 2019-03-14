from ply import lex
import re
import sys
lineno = 0
#Personal Groups

keywords = {
    'include':'INCLUDE',
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
    'float':'FLOAT',
    'for':'FOR',
    'goto':'GOTO',
    'if':'IF',
    'int':'INT',
    'long':'LONG',
    'new':'NEW',
    'return':'RETURN',
    'short':'SHORT',
    'signed':'SIGNED',
    'sizeof':'SIZEOF',
    'switch':'SWITCH',
    'struct' : 'STRUCT',
    'string' : 'STRING',
    'this':'THIS',
    'throw':'THROW',
    'try':'TRY',
    'typedef':'TYPEDEF',
    'type' : 'TYPE',
    'template' : 'TEMPLATE',
    'unsigned':'UNSIGNED',
    'void':'VOID',
    'while':'WHILE',
}

# List of token names. 
tokens = [
        # id and no
        'IDENTIFIER',
        'NUMBER',
        'DECIMAL',

        # arithematic operator
        'PLUSOP',
        'MINUSOP',
        'DIVOP',
        'MULTOP',
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
        'BNOP',
        'BOROP',

        #comparison operator, =
        'EQCOMP',
        'NEQCOMP',
        'GTCOMP',
        'GTECOMP',
        'LTCOMP',
        'LTECOMP',
        'EQUAL',

        # Parenthesis
        'LPAREN',
        'RPAREN',
        'LCPAREN',
        'RCPAREN',
        'LSPAREN',
        'RSPAREN',

        # OTHER
        'COMMA',
        'DOT',
        'SEMICOLON',
        'COLON',
        'DOUBLECOLON',
        'SCHAR',
        'STRING_L',
        'HASHTAG',
        'NOTSYM',
        'QUESMARK',
        'ARROW',
        'LSHIFTEQOP',
        'RSHIFTEQOP',
        'BOREQOP',
        'MODEQOP',
        'DPLUSOP',
        'LSHIFT',
        'RSHIFT',
        'DMINUSOP',
        'LTEMPLATE',
        'RTEMPLATE',

        # SPECIAL
        'DOUBLEBNOP'
        

] + list(keywords.values())

# Regular expression rules for simple tokens

# RegEx id
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = keywords.get(t.value, 'IDENTIFIER')
    return t

def t_DECIMAL(t):
    #r'((\d+\.\d+[eE]([+-])?\d+)|(\d+[eE]([+-])?\d+)|(\d+\.\d+)|(\.\d+)|(\d+))'
    r'(\d+\.\d+)([eE][-+]?\d+)?'
    t.value=float(t.value)
    return t

def t_NUMBER(t):
    #r'((\d+\.\d+[eE]([+-])?\d+)|(\d+[eE]([+-])?\d+)|(\d+\.\d+)|(\.\d+)|(\d+))'
    r'\d+([eE][-+]?\d+)?'
    t.value=int(t.value)
    return t

# Arithematic Operator
t_PLUSOP    = r'\+'
t_MINUSOP   = r'-'
t_DIVOP     = r'/'
t_MULTOP    = r'\*'
t_MODOP     = r'\%'
t_XOROP     = r'\^'

t_BOREQOP   = r'\|\='
t_OROP      = r'\|\|'
t_BANDOP    = r'\&'
t_BOROP     = r'\|'
t_ANDOP     = r'\&\&'

t_PLUSEQOP  = r'\+='
t_MODEQOP   = r'\%\='
t_MINUSEQOP = r'-='
t_MULTEQOP  = r'\*='
t_DIVEQOP   = r'/='
t_BANDEQOP  = r'\&\='

t_XOREQOP   = r'\^='
t_DPLUSOP   = r'\+\+'
t_DMINUSOP  = r'--'
t_BNOP      = r'\~'
t_LSHIFT    = r'\<\<'
t_RSHIFT    = r'\>\>'
t_LSHIFTEQOP= r'\<\<='
t_RSHIFTEQOP= r'\>\>='

t_LTEMPLATE = r'<\|'
t_RTEMPLATE = r'\|>'


# Comparison Operator
t_EQCOMP    = r'=='
t_NEQCOMP   = r'!='
t_GTCOMP    = r'>'
t_GTECOMP   = r'>='
t_LTCOMP    = r'<'
t_LTECOMP   = r'<='
t_EQUAL     = r'='

# Parenthesis
t_LPAREN   = r'\('
t_RPAREN   = r'\)'
t_LCPAREN   = r'\{'
t_RCPAREN   = r'\}'
t_LSPAREN   = r'\['
t_RSPAREN   = r'\]'

# Other
t_COMMA         = r','
t_DOT           = r'\.'
t_SEMICOLON     = r';'
t_COLON         = r':'
t_DOUBLECOLON   = r'::'
t_SCHAR         = r'\'.\''
t_STRING_L      = r'\".*\"'
t_HASHTAG       = r'\#'
t_NOTSYM        = r'\!'
t_QUESMARK      = r'\?'
t_ARROW         = r'-\>'
t_DOUBLEBNOP    = r'\~\~'


# track line no.
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    global lineno
    lineno = lineno + 1

# comment
def t_COMMENT(t):
    r'( (//)[^\n\r]* ) |(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)'
    t.value = str(t.value)
    t.type = 'COMMENT'
    pass


# A string containing ignored characters (spaces and tabs)
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
