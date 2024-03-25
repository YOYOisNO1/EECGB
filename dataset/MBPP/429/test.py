from program429 import driver
def test0():
  assert driver([10, 4, 6, 9], [5, 2, 3, 3], [0, 0, 2, 1]) == "FAILED"

def test1():
  assert driver([1, 2, 3, 4], [5, 6, 7, 8], [1, 2, 3, 0]) == "FAILED"

def test2():
  assert driver([8, 9, 11, 12], [7, 13, 14, 17], [0, 9, 10, 0]) == "FAILED"

