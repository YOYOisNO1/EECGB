from program31 import driver
def test0():
  assert driver([[1, 2, 6], [1, 3, 4, 5, 7, 8], [1, 3, 5, 6, 8, 9], [2, 5, 7, 11], [1, 4, 7, 8, 12]], 3, [5, 7, 1]) == "PASSED"

def test1():
  assert driver([[1, 2, 6], [1, 3, 4, 5, 7, 8], [1, 3, 5, 6, 8, 9], [2, 5, 7, 11], [1, 4, 7, 8, 12]], 1, [1]) == "PASSED"

def test2():
  assert driver([[1, 2, 6], [1, 3, 4, 5, 7, 8], [1, 3, 5, 6, 8, 9], [2, 5, 7, 11], [1, 4, 7, 8, 12]], 5, [6, 5, 7, 8, 1]) == "PASSED"

