from program481 import driver
def test0():
  assert driver([3, 34, 4, 12, 5, 2], 6, 9, True) == "PASSED"

def test1():
  assert driver([3, 34, 4, 12, 5, 2], 6, 30, False) == "PASSED"

def test2():
  assert driver([3, 34, 4, 12, 5, 2], 6, 15, True) == "PASSED"

