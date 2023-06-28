from program740 import driver
def test0():
  assert driver([1, 5, 7, 10, 13, 5], {1: 5, 7: 10, 13: 5}) == "PASSED"

def test1():
  assert driver([1, 2, 3, 4, 5, 6], {1: 2, 3: 4, 5: 6}) == "PASSED"

def test2():
  assert driver([7, 8, 9, 10, 11, 12], {7: 8, 9: 10, 11: 12}) == "PASSED"

