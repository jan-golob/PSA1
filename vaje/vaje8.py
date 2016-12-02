# -*- coding: utf-8 -*-
"""
Funkcije na grafih.

V ocenah časovne zahtevnosti je n število vozlišč v grafu,
m število povezav v grafu, d(u) pa število sosedov vozlišča u.
Pri tem predpostavljamo, da velja n = O(m)
(graf ima O(1) povezanih komponent).
"""
from vaje3 import Queue
from vaje5 import nothing

def BFS(G, root, visit = nothing):
    """
    Iskanje v širino iz vozlišča root.

    Spremenljivka visit določa funkcijo,
    ki se izvede ob obisku posameznega vozlišča.
    Kot vhod dobi trenutno vozlišče in njegovega predhodnika
    (oziroma None, če tega ni).
    Da se algoritem nadaljuje, mora vrniti True;
    če vrne False, se funkcija prekine in vrne False.
    Če iskanje pride do konca, funkcija vrne True.

    Časovna zahtevnost: O(m) + O(n) klicev funkcije visit
    """
    q = Queue()
    q.enqueue((root, None))
    visited = [False] * len(G)
    visited[root] = True
    while len(q) > 0:
        u, v = q.dequeue()
        if not visit(u, v):
            return False
        for w in G[u]:
            if visited[w]:
                continue
            visited[w] = True
            q.enqueue((w, u))
    return True

def dvodelen(G):
    n = len(G)
    sez = [None] * n
    def visit(u, v):
        if v is None:
            sez[u] = True
        else:
            sez[u] = not sez[v]
        for w in G[u]:
            if sez[w] is sez[u]:
                return False
            return True
    for u in range(n):
        if sez[u] is None:
            if not BFS(G, u, visit = visit):
                return False
    return sez

def stPoti(G, x, y):
    n = len(G)
    S = [0] * n
    nivo = [None] * n
    S[x], nivo[x] = 1, 0
    def visit(u, v):
        if u == y:
            return False
        for w in G[u]:
            if nivo[w] is None:
                nivo[w] = nivo[u] + 1
            if nivo[w] > nivo[u]:
                S[w] += S[u]
        return True
    BFS(G, x, visit = visit)
    return S[y]
