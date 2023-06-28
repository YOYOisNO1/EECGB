from program896 import driver
def test0():
  assert driver([[2, 5], [1, 2], [4, 4], [2, 3], [2, 1]], [[2, 1], [1, 2], [2, 3], [4, 4], [2, 5]]) == "FAILED"

def test1():
  assert driver([[9, 8], [4, 7], [3, 5], [7, 9], [1, 2]], [[1, 2], [3, 5], [4, 7], [9, 8], [7, 9]]) == "FAILED"

def test2():
  assert driver([[20, 50], [10, 20], [40, 40]], [[10, 20], [40, 40], [20, 50]]) == "FAILED"

