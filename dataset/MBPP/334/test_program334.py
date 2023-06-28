from program334 import driver
def test0():
  assert driver(1, 2, 3, False) == "PASSED"

def test1():
  assert driver(2, 3, 5, False) == "PASSED"

def test2():
  assert driver(7, 10, 5, True) == "PASSED"

