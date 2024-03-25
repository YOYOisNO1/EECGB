from program831 import driver
def test0():
  assert driver([1, 1, 1, 1], 4, 6) == "PASSED"

def test1():
  assert driver([1, 5, 1], 3, 1) == "PASSED"

def test2():
  assert driver([3, 2, 1, 7, 8, 9], 6, 0) == "PASSED"

