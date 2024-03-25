from program850 import driver
def test0():
  assert driver(50, 60, 70, True) == "PASSED"

def test1():
  assert driver(90, 45, 45, True) == "PASSED"

def test2():
  assert driver(150, 30, 70, False) == "PASSED"

