from program625 import driver
def test0():
  assert driver([1, 2, 3], [3, 2, 1]) == "PASSED"

def test1():
  assert driver([1, 2, 3, 4, 4], [4, 2, 3, 4, 1]) == "PASSED"

def test2():
  assert driver([4, 5, 6], [6, 5, 4]) == "PASSED"

