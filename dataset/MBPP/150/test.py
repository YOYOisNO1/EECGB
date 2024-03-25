from program150 import driver
def test0():
  assert driver(1, 7, 3, True) == "PASSED"

def test1():
  assert driver(1, -3, 5, False) == "PASSED"

def test2():
  assert driver(3, 2, 5, False) == "PASSED"

