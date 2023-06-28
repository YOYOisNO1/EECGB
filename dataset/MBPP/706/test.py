from program706 import driver
def test0():
  assert driver([11, 1, 13, 21, 3, 7], 6, [11, 3, 7, 1], 4, True) == "PASSED"

def test1():
  assert driver([1, 2, 3, 4, 5, 6], 6, [1, 2, 4], 3, True) == "PASSED"

def test2():
  assert driver([10, 5, 2, 23, 19], 5, [19, 5, 3], 3, False) == "PASSED"

