from program777 import driver
def test0():
  assert driver([1, 2, 3, 1, 1, 4, 5, 6], 8, 21) == "PASSED"

def test1():
  assert driver([1, 10, 9, 4, 2, 10, 10, 45, 4], 9, 71) == "PASSED"

def test2():
  assert driver([12, 10, 9, 45, 2, 10, 10, 45, 10], 9, 78) == "PASSED"

