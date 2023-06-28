from program974 import driver
def test0():
  assert driver([[2], [3, 9], [1, 6, 7]], 6) == "PASSED"

def test1():
  assert driver([[2], [3, 7], [8, 5, 6]], 10) == "PASSED"

def test2():
  assert driver([[3], [6, 4], [5, 2, 7]], 9) == "PASSED"

