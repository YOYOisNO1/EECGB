from program559 import driver
def test0():
  assert driver([-2, -3, 4, -1, -2, 1, 5, -3], 8, 7) == "PASSED"

def test1():
  assert driver([-3, -4, 5, -2, -3, 2, 6, -4], 8, 8) == "PASSED"

def test2():
  assert driver([-4, -5, 6, -3, -4, 3, 7, -5], 8, 10) == "PASSED"

