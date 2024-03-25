from program936 import driver
def test0():
  assert driver([[4, 3], [1, 9], [2, 10], [3, 2]], [1, 4, 2, 3], [[1, 9], [4, 3], [2, 10], [3, 2]]) == "FAILED"

def test1():
  assert driver([[5, 4], [2, 10], [3, 11], [4, 3]], [3, 4, 2, 3], [[3, 11], [4, 3], [2, 10], [3, 11]]) == "FAILED"

def test2():
  assert driver([[6, 3], [3, 8], [5, 7], [2, 4]], [2, 5, 3, 6], [[2, 4], [5, 7], [3, 8], [6, 3]]) == "FAILED"

