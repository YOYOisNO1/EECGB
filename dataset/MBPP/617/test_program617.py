from program617 import driver
def test0():
  assert driver(3, 4, 11, 3.5) == "PASSED"

def test1():
  assert driver(3, 4, 0, 0.0) == "PASSED"

def test2():
  assert driver(11, 14, 11, 1.0) == "PASSED"

