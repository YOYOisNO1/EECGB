from program926 import driver
def test0():
  assert driver(7, 2, 924) == "FAILED"

def test1():
  assert driver(3, 0, 2) == "FAILED"

def test2():
  assert driver(3, 1, 3) == "PASSED"

