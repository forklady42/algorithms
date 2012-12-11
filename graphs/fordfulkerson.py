"""Edmonds Karp for max flow and min cut between two specified nodes"""

import pylab
import networkx as nx
from shortest_path import BFS
from Queue import Queue

def _createAux(G, capacity='weight'):
    
    aux = nx.DiGraph()
    aux.add_nodes_from(G)
    
    for u, v, cap in G.edges(data=True):
        aux.add_edge(u, v, cap, flow=0)
        aux.add_edge(v, u, cap, flow=0)
        
    return aux
    
def FordFulkerson(G, s, t, capacity='weight'):
    
    residual = _createAux(G)
    
    total_flow = 0
    
    while nx.has_path(residual, s, t):
        (len, path) = BFS(residual, s, t)
        
        path_min_cap = float('inf')
        
        u = path[0]
        for v in path[1:]:
            if residual[u][v][capacity] < path_min_cap:
                path_min_cap = residual[u][v][capacity]
            u = v
        
        total_flow += path_min_cap
        
        u = path[0]
        for v in path[1:]:
            residual[u][v][capacity] -= path_min_cap
            residual[u][v]['flow'] += path_min_cap
            
            residual[v][u]['flow'] -= path_min_cap
            
            if residual[u][v][capacity] == 0:
                residual.remove_edge(u, v)
                residual.remove_edge(v, u)
            u = v
            
    return total_flow, residual
    
    
def minCut(G, s, t, capacity='weight'):
    
    (cut_cap, residual) = FordFulkerson(G, s, t, capacity)
    [S, S_comp]= nx.connected_components(residual.to_undirected())
    
    return S, S_comp

if __name__=="__main__":
    G = nx.Graph()
    
    G.add_edge('s', 'a', weight = 2)
    G.add_edge('s', 'b', weight = 1)
    G.add_edge('a', 'b', weight = 2)
    G.add_edge('a', 't', weight = 1)
    G.add_edge('b', 't', weight = 3)
    G.add_edge('b', 'c', weight = 6)
    G.add_edge('s', 'c', weight = 2)
    
    print 'NX:', nx.max_flow(G, 's', 't', capacity='weight')
    print 'Max flow:', FordFulkerson(G, 's', 't')[0]
    print 'Min cut:', minCut(G, 's', 't')