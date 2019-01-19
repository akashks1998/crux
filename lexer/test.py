from lex import lexer
a=10
lines=[]

while(1):
    try:
        line=input()
    except EOFError:
        break
    lines.append(line)
stri = '\n'.join(lines)

lexer.input(stri)

print('{:>{amt}} {:>{amt}} {:>{amt}} {:>{amt}}'.format('Type', 'Value', 'Lineno', 'Lexpos', amt=a))
for tok in lexer:
    print('{:>{amt}} {:>{amt}} {:>{amt}} {:>{amt}}'.format(tok.type, "'" + tok.value + "'", tok.lineno, tok.lexpos, amt=a))
