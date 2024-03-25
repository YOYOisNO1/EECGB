from program904 import driver
def test0():
  assert driver(13.5, False) == "PASSED"

def test1():
  assert driver(0.0, True) == "PASSED"

def test2():
  assert driver(-9.0, False) == "PASSED"

