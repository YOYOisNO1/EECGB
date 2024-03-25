from program665 import driver
def test0():
  assert driver([1, 2, 3, 4], [2, 3, 4, 1]) == "PASSED"

def test1():
  assert driver([2, 3, 4, 1, 5, 0], [3, 4, 1, 5, 0, 2]) == "PASSED"

def test2():
  assert driver([5, 4, 3, 2, 1], [4, 3, 2, 1, 5]) == "PASSED"

