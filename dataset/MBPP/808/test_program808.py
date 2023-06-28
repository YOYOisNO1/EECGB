from program808 import driver
def test0():
  assert driver([10, 4, 5, 6, 8], 6, True) == "PASSED"

def test1():
  assert driver([1, 2, 3, 4, 5, 6], 7, False) == "PASSED"

def test2():
  assert driver([7, 8, 9, 44, 11, 12], 11, True) == "PASSED"

