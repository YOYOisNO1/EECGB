from program562 import driver
def test0():
  assert driver([[1], [1, 4], [5, 6, 7, 8]], 4) == "PASSED"

def test1():
  assert driver([[0, 1], [2, 2], [3, 2, 1]], 3) == "PASSED"

def test2():
  assert driver([[7], [22, 23], [13, 14, 15], [10, 20, 30, 40, 50]], 5) == "PASSED"

