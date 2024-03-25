from program605 import driver
def test0():
  assert driver(13, True) == "PASSED"

def test1():
  assert driver(7, True) == "PASSED"

def test2():
  assert driver(-1010, False) == "PASSED"

