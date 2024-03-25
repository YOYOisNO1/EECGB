from program119 import driver
def test0():
  assert driver([1, 1, 2, 2, 3], 5, 3) == "PASSED"

def test1():
  assert driver([1, 1, 3, 3, 4, 4, 5, 5, 7, 7, 8], 11, 8) == "PASSED"

def test2():
  assert driver([1, 2, 2, 3, 3, 4, 4], 7, 1) == "PASSED"

