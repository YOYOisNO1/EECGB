from program702 import driver
def test0():
  assert driver([1, 3, 4, 9, 10, 11, 12, 17, 20], 9, 4, 5) == "FAILED"

def test1():
  assert driver([1, 5, 6, 2, 8], 5, 2, 3) == "FAILED"

def test2():
  assert driver([1, 2, 3, 4, 5, 6], 6, 3, 2) == "FAILED"

