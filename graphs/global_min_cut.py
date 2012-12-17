"""Karger's algorithm for global min cut

Randomized recursive contraction speed up
"""

import pylab
import networkx as nx
from random import choice
from math import sqrt
from fordfulkerson import *
from copy import deepcopy

def global_min_cut(G):
    
    H = nx.MultiGraph()
    H.add_edges_from(G.edges(data=True))
    
    return _karger(H)

def _karger(G):
    
    #uf = UnionFind()
    
    V = len(G.nodes())
    
    if V <= 6:
        
        #Convert from MultiGraph to Graph
        H = nx.Graph()
        H.add_nodes_from(G)
        
        for (u, v, w) in G.edges(data=True):
            if H[u].has_key(v):
                H[u][v]['weight'] += w['weight']
            else:
                H.add_edge(u, v, weight=w['weight'])
                
        
        min = (float('inf'), None)
        for n in H.nodes():
            for n2 in H.nodes():
                if n != n2:
                    (capacity, aux) = FordFulkerson(H, n, n2)
                    if capacity < min[0]:
                        min = (capacity, (n, n2))
        (capacity, (n, n2)) = min
        
        (S, S2) =minCut(H, n, n2)
        
        return capacity, _get_children(H, S), _get_children(H, S2)
        
    H = deepcopy(G)
    while G.number_of_nodes() > (V/sqrt(2)):
        G = _merge(G)
    print "G:", len(G.edges())
    while H.number_of_nodes() > (V/sqrt(2)):
        H = _merge(H)
    print "H:", len(H.edges())
    if len(G.edges()) <= len(H.edges()):
        return _karger(G)
    return _karger(H)
    
    
def _contract(uf, G):
    
    (u,v) = choice(G.edges())
    
    H = nx.MultiGraph()
    H.add_edges_from(G.edges(data=True))
    
    dom = uf.union(u, v)
    if dom == u:
        nondom = v
    else:
        nondom = u
    
    print H.edges(data=True)
    for nbr in H[nondom]:
        if nbr != dom:
            H.add_edge(dom, nbr, weight = H[nondom][nbr][0]['weight']) #zero? huh????
    
    
    H.remove_node(nondom)
    print H.edges(data=True)
    
    return uf, H
    
def _merge(G):
    
    (u, v) = choice(G.edges())
    
    if len(G.edges(u)) > len(G.edges(v)):
        dom = u
        nondom = v
    else:
        dom = v
        nondom = u
        
    if G.node[dom].has_key('children'):
        G.node[dom]['children'].append(nondom)
    else:
        G.node[dom]['children'] = [nondom]
        
    for nbr in G[nondom]:
        if nbr != dom:
            G.add_edge(dom, nbr, weight = G[nondom][nbr][0]['weight'])
    
    G.remove_node(nondom)
    return G
    
def _get_children(G, S):
    
    children = set()
    for i in S:
        children.add(i)
        for nbr in G[i]:
            children.add(nbr)
    
    return children
    
    
if __name__ == "__main__":
    G = nx.Graph()
    
    G.add_edge('s', 'a', weight = 2)
    G.add_edge('s', 'b', weight = 1)
    G.add_edge('a', 'b', weight = 2)
    G.add_edge('a', 't', weight = 1)
    G.add_edge('b', 't', weight = 3)
    G.add_edge('b', 'c', weight = 6)
    G.add_edge('s', 'c', weight = 2)
    G.add_edge('c', 'e', weight = 9)
    G.add_edge('d', 'e', weight = 10)
    
    H = nx.MultiGraph()
    H.add_edges_from(G.edges(data=True)) 
    
    print global_min_cut(G)
    