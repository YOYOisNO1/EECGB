from program22 import driver
def test0():
  assert driver([1, 2, 3, 4, 4, 5], 4) == "PASSED"

def test1():
  assert driver([1, 2, 3, 4], -1) == "PASSED"

def test2():
  assert driver([1, 1, 2, 3, 3, 2, 2], 1) == "PASSED"

