from program521 import driver
def test0():
  assert driver(6, 8, 12, True) == "PASSED"

def test1():
  assert driver(6, 6, 12, False) == "PASSED"

def test2():
  assert driver(6, 15, 20, True) == "PASSED"

