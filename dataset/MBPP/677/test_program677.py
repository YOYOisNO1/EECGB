from program677 import driver
def test0():
  assert driver(60, 50, 90, False) == "PASSED"

def test1():
  assert driver(45, 75, 60, True) == "PASSED"

def test2():
  assert driver(30, 50, 100, True) == "PASSED"

