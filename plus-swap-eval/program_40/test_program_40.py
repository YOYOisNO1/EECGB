import sys
sys.path.append('../')
from program_40 import triples_sum_to_zero
def test_1():
    assert triples_sum_to_zero([1, 3, 5, 0]) == False
def test_2():
    assert triples_sum_to_zero([1, 3, 5, -1]) == False
def test_3():
    assert triples_sum_to_zero([1, 3, -2, 1]) == True
def test_4():
    assert triples_sum_to_zero([1, 2, 3, 7]) == False
def test_5():
    assert triples_sum_to_zero([1, 2, 5, 7]) == False
def test_6():
    assert triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True
def test_7():
    assert triples_sum_to_zero([1]) == False
def test_8():
    assert triples_sum_to_zero([1, 3, 5, -100]) == False
def test_9():
    assert triples_sum_to_zero([100, 3, 5, -100]) == False