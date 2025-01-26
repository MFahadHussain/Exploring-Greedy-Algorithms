# union_find.py

class UnionFind:
    def __init__(self, n):
        """Initialize the Union-Find data structure."""
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        """Find the root of the set containing x."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        """Union the sets containing x and y."""
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            # Union by rank (attach the smaller tree to the larger tree)
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
