from program793 import driver
def test0():
  assert driver([1, 2, 3], 1, 3, 0) == "PASSED"

def test1():
  assert driver([1, 1, 1, 2, 3, 4], 1, 6, 2) == "PASSED"

def test2():
  assert driver([2, 3, 2, 3, 6, 8, 9], 3, 8, 3) == "PASSED"

