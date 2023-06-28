from program193 import driver
def test0():
  assert driver([1, 3, 5, 2, 3, 5, 1, 1, 3], [1, 2, 3, 5]) == "FAILED"

def test1():
  assert driver([2, 3, 4, 4, 5, 6, 6, 7, 8, 8], [2, 3, 4, 5, 6, 7, 8]) == "FAILED"

def test2():
  assert driver([11, 12, 13, 11, 11, 12, 14, 13], [11, 12, 13, 14]) == "FAILED"

