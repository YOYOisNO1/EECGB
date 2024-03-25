from program306 import driver
def test0():
  assert driver([1, 101, 2, 3, 100, 4, 5], 7, 4, 6, 11) == "PASSED"

def test1():
  assert driver([1, 101, 2, 3, 100, 4, 5], 7, 2, 5, 7) == "PASSED"

def test2():
  assert driver([11, 15, 19, 21, 26, 28, 31], 7, 2, 4, 71) == "PASSED"

