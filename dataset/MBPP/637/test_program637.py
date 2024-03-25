from program637 import driver
def test0():
  assert driver(1500, 1200, False) == "PASSED"

def test1():
  assert driver(100, 100, True) == "PASSED"

def test2():
  assert driver(2000, 5000, False) == "PASSED"

