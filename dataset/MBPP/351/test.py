from program351 import driver
def test0():
  assert driver([0, 1, 2, 3, 4, 5], 6, 1, 0) == "PASSED"

def test1():
  assert driver([1, 2, 1, 3, 4], 5, 2, 1) == "PASSED"

def test2():
  assert driver([2, 3, 4, 3, 5, 7, 1, 2, 3, 5], 10, 2, 2) == "PASSED"

