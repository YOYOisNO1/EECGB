from program476 import driver
def test0():
  assert driver([1, 2, 3], 4) == "PASSED"

def test1():
  assert driver([-1, 2, 3, 4], 3) == "PASSED"

def test2():
  assert driver([2, 3, 6], 8) == "PASSED"

