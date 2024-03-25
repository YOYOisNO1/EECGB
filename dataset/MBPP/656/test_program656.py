from program656 import driver
def test0():
  assert driver([3, 2, 1], [2, 1, 3], 3, 0) == "PASSED"

def test1():
  assert driver([1, 2, 3], [4, 5, 6], 3, 9) == "PASSED"

def test2():
  assert driver([4, 1, 8, 7], [2, 3, 6, 5], 4, 6) == "PASSED"

