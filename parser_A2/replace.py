import re
inp = open("parser.1.py", "r").read()
inp = str(inp)
a=[('LSHIFTEQOP', '<<='), ('RSHIFTEQOP', '>>='), ('LEFTQOP', '<<='), ('RIGHTQOP', '>>='), ('ARROWSTAR', '_>*'), ('BOREQOP', '|='), ('OROP', '||'), ('ANDOP', '&&'), ('PLUSEQOP', '+='), ('MODEQOP', '%='), ('MINUSEQOP', '_='), ('MULTEQOP', '*='), ('DIVEQOP', '/='), ('BANDEQOP', '&='), ('B_I_OR', '|='), ('B_E_OR', '^='), ('XOREQOP', '^='), ('DPLUSOP', '++'), ('DMINUSOP', '__'), ('EXPOP', '**'), ('LSHIFT', '<<'), ('RSHIFT', '>>'), ('LEFTSHIFT', '<<'), ('RIGHTLIFT', '>>'), ('CONDTIONAL', '?:'), ('MODQOP', '%='), ('EQCOMP', '=='), ('NEQCOMP', '!='), ('GTECOMP', '>='), ('LTECOMP', '<='), ('DOUBLECOLON', '::'), ('ARROW', '_>'), ('DOTSTAR', '.*'), ('PLUSOP', '+'), ('MINUSOP', '_'), ('DIVOP', '/'), ('MULTOP', '*'), ('MODOP', '%'), ('XOROP', '^'), ('BANDOP', '&'), ('BNOP', '~'), ('GTCOMP', '>'), ('LTCOMP', '<'), ('LRPAREN', '('), ('RRPAREN', ')'), ('LCPAREN', '{'), ('RCPAREN', '}'), ('LSPAREN', '['), ('RSPAREN', ']'), ('DOT', '.'), ('SEMICOLON', ';'), ('NOTSYM', '!'), ('QUESMARK', '?')]
for each in a:
    inp=inp.replace(" "+each[1] ," "+each[0])
print(inp)