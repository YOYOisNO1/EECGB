from program469 import driver
def test0():
  assert driver([1, 5, 2, 3, 7, 6, 4, 5], 3, 10) == "PASSED"

def test1():
  assert driver([2, 4, 7, 5, 4, 3, 5], 2, 7) == "PASSED"

def test2():
  assert driver([10, 6, 8, 4, 2], 2, 2) == "PASSED"

