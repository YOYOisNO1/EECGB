from program314 import driver
def test0():
  assert driver([[1, 4, 5], [2, 0, 0]], 3, 7) == "PASSED"

def test1():
  assert driver([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], 5, 24) == "PASSED"

def test2():
  assert driver([[7, 9, 11, 15, 19], [21, 25, 28, 31, 32]], 5, 81) == "PASSED"

