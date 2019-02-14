#!python3.6
import re
from collections import deque

# inp = open("parser.py", "r").read()
# inp = open("parser2.py", "r").read()
inp = open("panda.py", "r").read()

lst = inp.split('\ndef')
lt = [lst[i] for i in range(1, len(lst))]
idx = {}

def f(s, g):
    # # print(s)
    #s = re.sub('[ ][A-Z]+(?=[ \n\'])', '', s)
    s = re.sub(r'[\n\|:]', '', s)
    s = re.sub(r'[ ]+', ' ', s)
    s = re.findall(r"\'\'\'.*\'\'\'", s, re.MULTILINE)
    # # print(s)
    if(s):
        s = s[0]
        s = re.sub('\'', '', s)
        s = re.sub('[ ]+', ' ', s)
        s = re.sub('^[ ]*', '', s)
        s = re.sub('[ ]*$', '', s)
        s = s.split(' ')
        s = list(set(s))
        try:
            s.remove(g)
        except:
            x=""
        return s
    return list(set(s))

cnt=0
req = [[] for i in range(len(lt))]
G = {}
node = [ '' for i in range(len(lt))]
for i in lt:
    g = re.findall(r'(?<=p_).*(?=\()', i)
    if(g):
        g = g[0]
    else:
        g = ""
    node[cnt] = g
    idx[g] = cnt
    ## print('---')
    ## print(g)
    zx = f(lt[cnt], g)
    ## print('splice : ' + str(cnt) + '\n' + lt[cnt] + '\n')
    if(zx and zx[0] != ''):
        req[cnt] = zx
    ## print('req : ')
    ## print(req[cnt])
    G[g] = req[cnt]
    cnt = cnt + 1

GRAY, BLACK = 0, 1

def topological(graph):
    order, enter, state = deque(), set(graph), {}

    def dfs(node):
        state[node] = GRAY
        for k in graph.get(node, ()):
            sk = state.get(k, None)
            if sk == GRAY: continue
            if sk == BLACK: continue
            enter.discard(k)
            dfs(k)
        order.appendleft(node)
        state[node] = BLACK

    while enter: dfs(enter.pop())
    return order


topo = topological(G)
###
f=open("t.gz","w")
f.write("digraph  g{\n")
f.write("rank1 [style=invisible];\nrank2 [style=invisible];\n")
for i in topo:
    try:
        for j in G[i]:
            f.write( "'" + i + "'" + " -> " + "'" + j + "'" + "\n")
    except:
        continue
stt = ""
for i in list(topo)[0:10]:
    stt = "'" + stt + "'" + " -> " + "'" +  i + "'"
stt=stt[4:] + " [style=invis];"
#stt = "program -> translation_unit -> throw_expression -> type_list -> declaration [style=invis];"
f.write("{\nrankdir = TD;\nrank2 ->" + stt+ "\n}")
f.write("}\n")
