from program55 import driver
def test0():
  assert driver(1, 5, 2, 16) == "PASSED"

def test1():
  assert driver(1, 5, 4, 256) == "PASSED"

def test2():
  assert driver(2, 6, 3, 486) == "PASSED"

