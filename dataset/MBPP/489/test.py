from program489 import driver
def test0():
  assert driver(5, [1, 2, 3, 4, 4], 2) == "PASSED"

def test1():
  assert driver(3, [5, 6, 5], 1) == "PASSED"

def test2():
  assert driver(4, [2, 7, 7, 7], 3) == "PASSED"

