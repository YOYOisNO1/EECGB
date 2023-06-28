from program611 import driver
def test0():
  assert driver([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2, 19) == "PASSED"

def test1():
  assert driver([[6, 7, 8], [2, 4, 6], [9, 10, 20]], 1, 10) == "PASSED"

def test2():
  assert driver([[7, 8, 9], [3, 5, 7], [10, 11, 21]], 1, 11) == "PASSED"

