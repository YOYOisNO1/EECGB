from program670 import driver
def test0():
  assert driver([-4, -3, -2, -1], True) == "PASSED"

def test1():
  assert driver([1, 2, 3], True) == "PASSED"

def test2():
  assert driver([3, 2, 1], False) == "PASSED"

