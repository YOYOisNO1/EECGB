from program154 import driver
def test0():
  assert driver([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]], 0, [1, 4, 7]) == "PASSED"

def test1():
  assert driver([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]], 2, [3, 6, 9]) == "PASSED"

def test2():
  assert driver([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]], 3, [2, 2, 5]) == "PASSED"

