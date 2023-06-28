from program836 import driver
def test0():
  assert driver([-2, -3, 4, -1, -2, 1, 5, -3], 8, 5) == "PASSED"

def test1():
  assert driver([1, -2, 1, 1, -2, 1], 6, 2) == "PASSED"

def test2():
  assert driver([-1, -2, 3, 4, 5], 5, 3) == "PASSED"

