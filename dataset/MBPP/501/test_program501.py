from program501 import driver
def test0():
  assert driver(2, 4, 2) == "PASSED"

def test1():
  assert driver(2, 8, 2) == "PASSED"

def test2():
  assert driver(12, 24, 6) == "FAILED"

