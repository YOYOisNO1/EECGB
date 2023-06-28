from program645 import driver
def test0():
  assert driver([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2, 665) == "FAILED"

def test1():
  assert driver([[6, 7, 8], [2, 4, 6], [9, 10, 20]], 1, 280) == "FAILED"

def test2():
  assert driver([[7, 8, 9], [3, 5, 7], [10, 11, 21]], 0, 210) == "FAILED"

