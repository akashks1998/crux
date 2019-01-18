from lex import lexer

stri = input()
lexer.input(stri)
a=8

print('{:>{amt}} {:>{amt}} {:>{amt}} {:>{amt}}'.format('Type', 'Value', 'Lineno', 'Lexpos', amt=a))
for tok in lexer:
    print('{:>{amt}} {:>{amt}} {:>{amt}} {:>{amt}}'.format(tok.type, "'" + tok.value + "'", tok.lineno, tok.lexpos, amt=a))
