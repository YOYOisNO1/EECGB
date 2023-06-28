from program908 import driver
def test0():
  assert driver([-10, -1, 0, 3, 10, 11, 30, 50, 100], 9, 3) == "PASSED"

def test1():
  assert driver([1, 2, 3, 4, 5, 6, 7, 8], 8, -1) == "PASSED"

def test2():
  assert driver([0, 2, 5, 8, 17], 5, 0) == "PASSED"

