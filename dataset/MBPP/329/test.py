from program329 import driver
def test0():
  assert driver([-1, -2, 3, -4, -5], 4) == "PASSED"

def test1():
  assert driver([1, 2, 3], 0) == "PASSED"

def test2():
  assert driver([1, 2, -3, -10, 20], 2) == "PASSED"

