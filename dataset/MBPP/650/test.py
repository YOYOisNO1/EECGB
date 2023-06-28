from program650 import driver
def test0():
  assert driver([1, 2, 3], [3, 2, 1], 3, 3, True) == "PASSED"

def test1():
  assert driver([1, 1, 1], [2, 2, 2], 3, 3, False) == "PASSED"

def test2():
  assert driver([8, 9], [4, 5, 6], 2, 3, False) == "PASSED"

