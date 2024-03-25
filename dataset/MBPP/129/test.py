from program129 import driver
def test0():
  assert driver([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]], True) == "PASSED"

def test1():
  assert driver([[2, 7, 6], [9, 5, 1], [4, 3, 8]], True) == "PASSED"

def test2():
  assert driver([[2, 7, 6], [9, 5, 1], [4, 3, 7]], False) == "PASSED"

