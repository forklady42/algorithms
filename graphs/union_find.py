class UnionFind():
    """Based on Josiah Carlson's Union Find data structure in the python
    cookbook. Used to implement Kruskal's algorithm."""
    
    def __init__(self):
        self.size = {}
        self.parent_pointers = {}
        
    def find(self, vertex):
        """Doubles as insert"""
        
        #Inserts new vertex
        if vertex not in self.parent_pointers:
            self.size[vertex] = 1
            self.parent_pointers[vertex] = vertex
            return vertex
            
        ancestors = [vertex]
        parent = self.parent_pointers[ancestors[-1]]
        
        while parent != ancestors[-1]:
            ancestors.append(parent)
            par = self.parent_pointers[parent]
            
        for i in ancestors:
            self.parent_pointers[i] = parent
            
        return parent
            
    def union(self, u, v):
        
        uset = self.find(u)
        vset = self.find(v)
        
        if uset != vset:
            uw = self.size[uset]
            vw = self.size[vset]
            dominate = u
            if uw < vw:
                uset, vset, uw, vw = vset, uset, vw, uw
                dominate = v
            self.size[uset] = uw + vw
            self.parent_pointers[vset] = uset
            
            return dominate
            