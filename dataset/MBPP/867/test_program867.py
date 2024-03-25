from program867 import driver
def test0():
  assert driver([1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 1) == "PASSED"

def test1():
  assert driver([1, 2, 3, 4, 5, 6, 7, 8], 8, 2) == "PASSED"

def test2():
  assert driver([1, 2, 3], 3, 2) == "PASSED"

