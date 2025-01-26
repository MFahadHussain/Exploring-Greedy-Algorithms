# test_kruskal.py

import pytest
from kruskal_algorithm import Kruskal

def test_kruskal():
    graph = Kruskal(4)
    graph.add_edge(0, 1, 10)
    graph.add_edge(0, 2, 6)
    graph.add_edge(0, 3, 5)
    graph.add_edge(1, 3, 15)
    graph.add_edge(2, 3, 4)
    
    mst = graph.kruskal_mst()
    
    assert len(mst) == 3  # There should be 3 edges in the MST
    assert (0, 3, 5) in mst
    assert (2, 3, 4) in mst
    assert (0, 1, 10) in mst
