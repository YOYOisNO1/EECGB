from program610 import driver
def test0():
  assert driver([1, 1, 2, 3, 4, 4, 5, 1], 3, [1, 1, 3, 4, 4, 5, 1]) == "PASSED"

def test1():
  assert driver([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4], 4, [0, 0, 1, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]) == "PASSED"

def test2():
  assert driver([10, 10, 15, 19, 18, 18, 17, 26, 26, 17, 18, 10], 5, [10, 10, 15, 19, 18, 17, 26, 26, 17, 18, 10]) == "PASSED"

