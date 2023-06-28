from program600 import driver
def test0():
  assert driver(1, False) == "PASSED"

def test1():
  assert driver(2, True) == "PASSED"

def test2():
  assert driver(3, False) == "PASSED"

