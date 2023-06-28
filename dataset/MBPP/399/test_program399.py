from program399 import driver
def test0():
  assert driver([10, 4, 6, 9], [5, 2, 3, 3], [15, 6, 5, 10]) == "FAILED"

def test1():
  assert driver([11, 5, 7, 10], [6, 3, 4, 4], [13, 6, 3, 14]) == "FAILED"

def test2():
  assert driver([12, 6, 8, 11], [7, 4, 5, 6], [11, 2, 13, 13]) == "FAILED"

