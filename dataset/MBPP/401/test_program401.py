from program401 import driver
def test0():
  assert driver([[1, 3], [4, 5], [2, 9], [1, 10]], [[6, 7], [3, 9], [1, 1], [7, 3]], [[7, 10], [7, 14], [3, 10], [8, 13]]) == "FAILED"

def test1():
  assert driver([[2, 4], [5, 6], [3, 10], [2, 11]], [[7, 8], [4, 10], [2, 2], [8, 4]], [[9, 12], [9, 16], [5, 12], [10, 15]]) == "FAILED"

def test2():
  assert driver([[3, 5], [6, 7], [4, 11], [3, 12]], [[8, 9], [5, 11], [3, 3], [9, 5]], [[11, 14], [11, 18], [7, 14], [12, 17]]) == "FAILED"

