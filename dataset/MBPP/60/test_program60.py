from program60 import driver
def test0():
  assert driver([2, 5, 6, 3, 7, 6, 5, 8], 8, 5) == "PASSED"

def test1():
  assert driver([-2, -1, 5, -1, 4, 0, 3], 7, 4) == "PASSED"

def test2():
  assert driver([9, 11, 13, 15, 18], 5, 1) == "PASSED"

