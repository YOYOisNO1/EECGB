from program522 import driver
def test0():
  assert driver([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], 7) == "PASSED"

def test1():
  assert driver([1, 11, 2, 10, 4, 5, 2, 1], 6) == "PASSED"

def test2():
  assert driver([80, 60, 30, 40, 20, 10], 5) == "PASSED"

