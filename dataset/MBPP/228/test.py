from program228 import driver
def test0():
  assert driver(4, 1, 2, True) == "PASSED"

def test1():
  assert driver(17, 2, 4, True) == "PASSED"

def test2():
  assert driver(39, 4, 6, False) == "PASSED"

