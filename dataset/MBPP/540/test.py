from program540 import driver
def test0():
  assert driver([1, 1, 2, 2, 7, 8, 4, 5, 1, 4], 10, 2) == "PASSED"

def test1():
  assert driver([1, 7, 9, 2, 3, 3, 1, 3, 3], 9, 3) == "PASSED"

def test2():
  assert driver([1, 2, 1, 2], 4, 0) == "PASSED"

