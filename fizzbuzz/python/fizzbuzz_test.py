"""
Run via pytest
"""
from fizzbuzz import fizzbuzz

def test_one():
    assert fizzbuzz(1) == 1

def test_three():
    assert fizzbuzz(3) == 'fizz'

def test_five():
    assert fizzbuzz(5) == 'buzz'

def test_fifteen():
    assert fizzbuzz(15) == 'fizzbuzz'
