from program303 import driver
def test0():
  assert driver([1, 0, 2], 3, True) == "PASSED"

def test1():
  assert driver([1, 2, 0], 3, False) == "PASSED"

def test2():
  assert driver([1, 2, 1], 3, True) == "PASSED"

