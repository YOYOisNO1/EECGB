from program614 import driver
def test0():
  assert driver([[1, 3], [5, 6, 7], [2, 6]], 30) == "PASSED"

def test1():
  assert driver([[2, 4], [6, 7, 8], [3, 7]], 37) == "PASSED"

def test2():
  assert driver([[3, 5], [7, 8, 9], [4, 8]], 44) == "PASSED"

