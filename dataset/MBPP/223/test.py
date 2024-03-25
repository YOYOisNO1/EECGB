from program223 import driver
def test0():
  assert driver([1, 2, 3, 3, 3, 3, 10], 7, 3, True) == "PASSED"

def test1():
  assert driver([1, 1, 2, 4, 4, 4, 6, 6], 8, 4, False) == "PASSED"

def test2():
  assert driver([1, 1, 1, 2, 2], 5, 1, True) == "PASSED"

