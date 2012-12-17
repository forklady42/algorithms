"""Implementations of Prim's and Kruskal's algorithms for finding
the minimum spanning tree"""

import pylab
import networkx as nx
from heapq import heappush, heappop
from union_find import *

def prim(G, weight='weight'):
    
    #Arbitrary starting node
    s = G.nodes()[0]
    
    T = nx.Graph()
    T.add_node(s)
    
    vertex_heap = []
    
    for vertex in G[s]:
        heappush(vertex_heap, (G[s][vertex][weight], vertex))

    while T.nodes() != G.nodes():
        
        if len(vertex_heap) == 0:
            return "Error: graph not connected"
        
        (cost, u) = heappop(vertex_heap)
        if u not in T.nodes():
            for v in G[u]:
                if G[u][v][weight] == cost and v in T.nodes():
                    T.add_edge(u, v)
                    for nbr in G[u]:
                        if nbr not in T.nodes():
                            heappush(vertex_heap, (G[u][nbr][weight], nbr))
        
    return T

def kruskal():
    
    edges = G.edges().sort(key=lambda e: e[2]['weight'])
    
    T = nx.Graph()
    
    uf = unionFind()
    
    for i in edges:
        edge = uf.find(i)
    
    return T
    

if __name__=="__main__":
    G = nx.Graph()
    
    G.add_edge('s', 'a', weight = 2)
    G.add_edge('s', 'b', weight = 1)
    G.add_edge('a', 'b', weight = 3)
    G.add_edge('a', 't', weight = 1)
    G.add_edge('b', 't', weight = 3)
    G.add_edge('b', 'c', weight = 6)
    G.add_edge('s', 'c', weight = 2)
    
    H = nx.Graph()
    
    H.add_edge('a', 'b', weight = 1)
    H.add_edge('b', 'c', weight = 4)
    H.add_edge('c', 'e', weight = 2)
    H.add_edge('b', 'd', weight = 5)
    H.add_edge('a', 'd', weight = 7)
    H.add_edge('d', 'e', weight = 6)
    H.add_edge('e', 'b', weight = 3)
    
    print 'MST:', prim(H).edges()
    
    """
    #Test union find
    uf = unionFind()
    
    for v in H:
        uf.find(v)
    
    uf.union('a', 'b')
    uf.union('a', 'c')
    uf.union('b', 'd')
    
    print uf.parent_pointers
    """