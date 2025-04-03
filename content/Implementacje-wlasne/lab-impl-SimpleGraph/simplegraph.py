from abcgraph import BaseGraph

class SimpleGraph[T](BaseGraph):
    """
    A simple graph class that implements the BaseGraph interface:
    1. The graph is undirected.
    2. The graph is unweighted.
    3. The graph is simple (no loops, no multiple edges).
    Implementation: adjacency list, key -> set of neighbors.
    """
    def __init__(self) -> None:
        super().__init__(allow_loops=False, allow_multiple_edges=False, is_directed=False)
        self._adjacency = {}
        self._edges = set()

    def has_node(self, node: T) -> bool:
        return node in self._adjacency

    def has_edge(self, u, v):
        return (v, u) in self._edges
    
    @property
    def nodes(self):
        return self._adjacency.keys()
    
 
    def neighbors(self, node):
        return self._adjacency[node]

    def add_node(self, node: T) -> None:
        if node not in self._adjacency:
            self._adjacency[node] = set()

    def add_edge(self, u: T, v: T, weight=None) -> None:
        if u == v:
            raise ValueError("Loops are not allowed in simple graphs.")
        if (u, v) in self._edges or (v, u) in self._edges:
            raise ValueError("Multiple edges are not allowed in simple graphs.")
        self.add_node(u)
        self.add_node(v)
        self._adjacency[u].add(v)
        self._edges.add((u, v))

    def remove_node(self, node):
        if node in self._adjacency:
            for neighbor in self._adjacency[node]:
                self._adjacency[neighbor].remove(node)
                self._edges.remove((neighbor, node))
            del self._adjacency[node]
            self._edges = {(u, v) for u, v in self._edges}

    def remove_edge(self, u, v):
        if (u, v) in self._edges:
            self._adjacency[u].remove(v)
            self._edges.remove((u, v))
    
    def __getitem__(self, node):
        return self._adjacency[node]
    
    def __len__(self):
        pass
    
    def __str__(self):
        return str(self._adjacency)
    

            
