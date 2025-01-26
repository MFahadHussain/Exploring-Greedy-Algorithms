# kruskal_algorithm.py

from union_find import UnionFind

class Kruskal:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        """Add an edge to the graph."""
        self.edges.append((weight, u, v))

    def kruskal_mst(self):
        """Find the Minimum Spanning Tree (MST) using Kruskal's algorithm."""
        mst = []
        # Sort edges by weight
        self.edges.sort()
        
        # Initialize Union-Find data structure
        uf = UnionFind(self.vertices)
        
        for weight, u, v in self.edges:
            if uf.find(u) != uf.find(v):
                uf.union(u, v)
                mst.append((u, v, weight))
        
        return mst

if __name__ == "__main__":
    # Example graph (number of vertices)
    graph = Kruskal(4)
    graph.add_edge(0, 1, 10)
    graph.add_edge(0, 2, 6)
    graph.add_edge(0, 3, 5)
    graph.add_edge(1, 3, 15)
    graph.add_edge(2, 3, 4)
    
    mst = graph.kruskal_mst()
    print("Minimum Spanning Tree (MST):")
    for u, v, weight in mst:
        print(f"Edge: {u} - {v}, Weight: {weight}")
