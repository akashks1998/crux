from lex import lexer

stri = input()
lexer.input(stri)

print('{:>12} {:>12} {:>12} {:>12}'.format('Type', 'Value', 'Lineno', 'Lexpos'))
for tok in lexer:
    print('{:>12} {:>12} {:>12} {:>12}'.format(tok.type, tok.value, tok.lineno, tok.lexpos))
