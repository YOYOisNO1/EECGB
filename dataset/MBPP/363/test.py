from program363 import driver
def test0():
  assert driver([[1, 3, 4], [2, 4, 6], [3, 8, 1]], 4, [[5, 7, 8], [6, 8, 10], [7, 12, 5]]) == "FAILED"

def test1():
  assert driver([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 8, [[9, 10, 11], [12, 13, 14], [15, 16, 17]]) == "FAILED"

def test2():
  assert driver([[11, 12, 13], [14, 15, 16], [17, 18, 19]], 9, [[20, 21, 22], [23, 24, 25], [26, 27, 28]]) == "FAILED"

