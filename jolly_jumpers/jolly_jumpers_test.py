"""
Run via pytest
"""
from jolly_jumpers import successive_differences

def test_successive_differences_uniq():
    assert successive_differences([1, 2, 4, 7]) == set([1,2,3])

def test_successive_differences_overlap():
    assert successive_differences([1, 2, 3, 5]) == set([1,2])
