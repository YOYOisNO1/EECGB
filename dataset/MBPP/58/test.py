from program58 import driver
def test0():
  assert driver(1, -2, True) == "PASSED"

def test1():
  assert driver(3, 2, False) == "PASSED"

def test2():
  assert driver(-10, -10, False) == "PASSED"

