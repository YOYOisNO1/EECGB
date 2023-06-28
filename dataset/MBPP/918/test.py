from program918 import driver
def test0():
  assert driver([1, 2, 3], 3, 4, 4) == "PASSED"

def test1():
  assert driver([4, 5, 6, 7, 8, 9], 6, 9, 2) == "PASSED"

def test2():
  assert driver([4, 5, 6, 7, 8, 9], 6, 4, 1) == "PASSED"

