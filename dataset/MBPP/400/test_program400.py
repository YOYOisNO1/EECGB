from program400 import driver
def test0():
  assert driver([[3, 4], [1, 2], [4, 3], [5, 6]], 3) == "PASSED"

def test1():
  assert driver([[4, 15], [2, 3], [5, 4], [6, 7]], 4) == "PASSED"

def test2():
  assert driver([[5, 16], [2, 3], [6, 5], [6, 9]], 4) == "PASSED"

