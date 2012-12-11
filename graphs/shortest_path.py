"""Shortest path algorithms for both weighted and unweighted graphs"""

import pylab
import networkx as nx
from Queue import Queue, PriorityQueue
    
def BFS(G, s, t):
    
    for u in G.nodes():
        G.node[u]['dist'] = float('inf')
      
    G.node[s]['dist'] = 0
    
    nodeQ = Queue()
    nodeQ.put((0, s))
    
    while not nodeQ.empty():
        (dist, u) = nodeQ.get()
        
        if u == t:
            path = [t]
            v = u
            while v != s:
                v = G.node[v]['prev']
                path.insert(0,v)         #prepend is ugly. Better idea?
            return dist, path
            
        for v in G[u]:
            if dist + 1 < G.node[v]['dist']:
                G.node[v]['dist'] = dist + 1
                G.node[v]['prev'] = u
                nodeQ.put((dist+1, v))
                
    return "Error: target not in reach"
    
def dijkstra(G, s, t, weight='weight'):
    
    for u in G.nodes():
        G.node[u]['dist'] = float('inf')
    
    G.node[s]['dist'] = 0
    
    nodeQ = PriorityQueue()
    nodeQ.put((0, s))
    
    while not nodeQ.empty():
        (dist, u) = nodeQ.get()
        
        if u == t:
            path = [t]
            v = u
            while v != s:
                v = G.node[v]['prev']
                path.insert(0,v)
            return dist, path
        
        for v in G[u]:
            
            new_dist = dist + G[u][v][weight]
                
            if new_dist < G.node[v]['dist']:
                G.node[v]['dist'] = new_dist
                G.node[v]['previous'] = u
                nodeQ.put((new_dist, v))
            
    return "Error: target not in reach"
    
if __name__ == "__main__":
    
    Test = nx.Graph()
    
    Test.add_edge('s', 'a', weight = 2)
    Test.add_edge('s', 'b', weight = 1)
    Test.add_edge('a', 'b', weight = 2)
    Test.add_edge('a', 't', weight = 1)
    Test.add_edge('b', 't', weight = 3)
    Test.add_edge('b', 'c', weight = 6)
    Test.add_edge('s', 'c', weight = 2)
    
    print BFS(Test, 's', 't')
    print dijkstra(Test, 's', 't')