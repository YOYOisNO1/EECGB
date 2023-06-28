from program471 import driver
def test0():
  assert driver([100, 10, 5, 25, 35, 14], 6, 11, 9) == "PASSED"

def test1():
  assert driver([1, 1, 1], 3, 1, 0) == "PASSED"

def test2():
  assert driver([1, 2, 1], 3, 2, 0) == "PASSED"

