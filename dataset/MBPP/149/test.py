from program149 import driver
def test0():
  assert driver([1, 2, 3, 4, 5, 3, 2], 7, 6) == "PASSED"

def test1():
  assert driver([10, 9, 4, 5, 4, 8, 6], 7, 3) == "PASSED"

def test2():
  assert driver([1, 2, 3, 2, 3, 7, 2, 1], 8, 7) == "PASSED"

