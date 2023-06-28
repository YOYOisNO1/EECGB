from program313 import driver
def test0():
  assert driver([-1, -2, 1, 2], 1) == "PASSED"

def test1():
  assert driver([3, 4, -5], 3) == "PASSED"

def test2():
  assert driver([-2, -3, 1], 1) == "PASSED"

