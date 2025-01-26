# examples.py

from kruskal_algorithm import Kruskal

def example_graph():
    """Example graph with 4 vertices and 5 edges."""
    graph = Kruskal(4)
    graph.add_edge(0, 1, 10)
    graph.add_edge(0, 2, 6)
    graph.add_edge(0, 3, 5)
    graph.add_edge(1, 3, 15)
    graph.add_edge(2, 3, 4)
    
    return graph

if __name__ == "__main__":
    graph = example_graph()
    mst = graph.kruskal_mst()
    
    print("Example Graph MST:")
    for u, v, weight in mst:
        print(f"Edge: {u} - {v}, Weight: {weight}")
