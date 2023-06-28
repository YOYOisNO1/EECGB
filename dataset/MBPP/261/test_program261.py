from program261 import driver
def test0():
  assert driver([10, 4, 6, 9], [5, 2, 3, 3], [2, 2, 2, 3]) == "FAILED"

def test1():
  assert driver([12, 6, 8, 16], [6, 3, 4, 4], [2, 2, 2, 4]) == "FAILED"

def test2():
  assert driver([20, 14, 36, 18], [5, 7, 6, 9], [4, 2, 6, 2]) == "FAILED"

