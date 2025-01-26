 # test_union_find.py

import pytest
from union_find import UnionFind

def test_union_find():
    uf = UnionFind(5)
    
    # Initially, each element is its own parent
    assert uf.find(0) == 0
    assert uf.find(1) == 1
    assert uf.find(2) == 2
    assert uf.find(3) == 3
    assert uf.find(4) == 4
    
    # Union some sets
    uf.union(0, 1)
    uf.union(2, 3)
    uf.union(3, 4)
    
    # After unions, they should be in the same set
    assert uf.find(0) == uf.find(1)
    assert uf.find(2) == uf.find(4)
    
    # Different sets should have different parents
    assert uf.find(0) != uf.find(2)
