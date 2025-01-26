# Pseudocode for Kruskal's Algorithm

1. **Sort** all edges in non-decreasing order of their weights.
2. Initialize an empty **MST**.
3. Initialize a **Union-Find** data structure for the vertices.
4. For each edge (u, v) in the sorted edges:
   - If `find(u)` is not equal to `find(v)`:
     - Add the edge (u, v) to the **MST**.
     - Union the sets containing u and v using the **Union-Find** data structure.
5. Return the **MST**.
