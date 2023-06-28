from program38 import driver
def test0():
  assert driver([1, 3, 5, 7, 4, 1, 6, 8], 4) == "PASSED"

def test1():
  assert driver([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2) == "PASSED"

def test2():
  assert driver([1, 5, 7, 9, 10], 10) == "PASSED"

