from program972 import driver
def test0():
  assert driver([3, 4], [5, 6], [3, 4, 5, 6]) == "PASSED"

def test1():
  assert driver([1, 2], [3, 4], [1, 2, 3, 4]) == "PASSED"

def test2():
  assert driver([4, 5], [6, 8], [4, 5, 6, 8]) == "PASSED"

