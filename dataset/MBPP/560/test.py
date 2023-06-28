from program560 import driver
def test0():
  assert driver([3, 4, 5, 6], [5, 7, 4, 10], [3, 4, 5, 6, 7, 10]) == "FAILED"

def test1():
  assert driver([1, 2, 3, 4], [3, 4, 5, 6], [1, 2, 3, 4, 5, 6]) == "FAILED"

def test2():
  assert driver([11, 12, 13, 14], [13, 15, 16, 17], [11, 12, 13, 14, 15, 16, 17]) == "FAILED"

