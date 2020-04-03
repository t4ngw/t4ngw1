# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 20:07:40 2019

@author: t4ngw
"""

G = {'U':['V', 'X'],
     'V':['Y'],
     'X':['V'],
     'Y':['X'],
     'W':['Y', 'Z'],
     'Z':['Z']
     }

def DFS(G):
    for u in G.keys():
        G[u].append('white')
    global time
    time = 0
    for u in G:
        if 'white' in G[u]:
            DFS_VISIT(G, u)
    return G
def DFS_VISIT(G, u):
    global time
    global ud, uf
    time = time + 1
    ud = time
    G[u].append(ud)
    for i in range (len(G[u]) - 2, 0, -1):
        if 'white' in G[u]:
            G[u][i] = 'gray'
        else:
            continue
    for v in G[u]:
        if v != 'gray' and type(v) != int:
            if 'white' in G[v]:
                G[u].append(v)
                DFS_VISIT(G, v)
        else:
            continue
    time = time + 1

    uf = time
    G[u].append(uf)
    for i in range (len(G[u]) - 4, 0, -1):
        if 'gray' in G[u]:
            G[u][i] = 'black'
print(DFS(G))
                