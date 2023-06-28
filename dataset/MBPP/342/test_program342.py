from program342 import driver
def test0():
  assert driver([[3, 6, 8, 10, 15], [1, 5, 12], [4, 8, 15, 16], [2, 6]], [4, 6]) == "FAILED"

def test1():
  assert driver([[2, 3, 4, 8, 10, 15], [1, 5, 12], [7, 8, 15, 16], [3, 6]], [4, 7]) == "FAILED"

def test2():
  assert driver([[4, 7, 9, 11, 16], [2, 6, 13], [5, 9, 16, 17], [3, 7]], [5, 7]) == "FAILED"

