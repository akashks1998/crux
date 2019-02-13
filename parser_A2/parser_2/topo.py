#!python3.6
import re
from collections import deque

inp = open("parser.py", "r").read()

lst = inp.split('\ndef')
lt = [lst[i] for i in range(1, len(lst))]
idx = {}

def f(s, g):
    # print(s)
    s = re.sub('[ ][A-Z_]+(?=[ \n\'])', '', s)
    s = re.sub(r'[\n\|:]', '', s)
    s = re.sub(r'[ ]+', ' ', s)
    s = re.findall(r"\'\'\'.*\'\'\'", s, re.MULTILINE)
    # print(s)
    if(s):
        s = s[0]
        s = re.sub('\'', '', s)
        s = re.sub('[ ]+', ' ', s)
        s = re.sub('^[ ]*', '', s)
        s = re.sub('[ ]*$', '', s)
        s = s.split(' ')
        s = list(set(s))
        s.remove(g)
        return s
    return list(set(s))

cnt=0
req = [[] for i in range(len(lt))]
G = {}
node = [ '' for i in range(len(lt))]
for i in lt:
    g = re.findall(r'(?<=p_).*(?=\()', i)[0]
    node[cnt] = g
    idx[g] = cnt
    #print('---')
    #print(g)
    zx = f(lt[cnt], g)
    #print('splice : ' + str(cnt) + '\n' + lt[cnt] + '\n')
    if(zx and zx[0] != ''):
        req[cnt] = zx
    #print('req : ')
    #print(req[cnt])
    G[g] = req[cnt]
    cnt = cnt + 1

for i in node:
    print(i+' -> '+str(G[i]))

###
graph1 = {
    "a": ["b", "c", "d"],
    "b": [],
    "c": ["d"],
    "d": []
}

# 2 components
graph2 = {
    "a": ["b", "c", "d"],
    "b": [],
    "c": ["d"],
    "d": [],
    "e": ["g", "f", "q"],
    "g": [],
    "f": [],
    "q": []
}

# cycle
graph3 = {
    "a": ["b", "c", "d"],
    "b": [],
    "c": ["d", "e"],
    "d": [],
    "e": ["g", "f", "q"],
    "g": ["c"],
    "f": [],
    "q": []
}

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

# check how it works
print(topological(graph1))
print(topological(graph2))
topo = topological(G)
###
for i in topo:
    print(lt[idx[i]])