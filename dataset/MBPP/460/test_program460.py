from program460 import driver
def test0():
  assert driver([[1, 2], [3, 4, 5], [6, 7, 8, 9]], [1, 3, 6]) == "PASSED"

def test1():
  assert driver([[1, 2, 3], [4, 5]], [1, 4]) == "PASSED"

def test2():
  assert driver([[9, 8, 1], [1, 2]], [9, 1]) == "PASSED"

