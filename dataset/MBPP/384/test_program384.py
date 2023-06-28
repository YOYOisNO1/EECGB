from program384 import driver
def test0():
  assert driver(5, [1, 2, 3, 4, 3], 1) == "PASSED"

def test1():
  assert driver(7, [3, 1, 2, 5, 6, 2, 3], 1) == "PASSED"

def test2():
  assert driver(7, [3, 3, 6, 3, 7, 4, 9], 3) == "PASSED"

