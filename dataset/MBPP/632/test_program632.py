from program632 import driver
def test0():
  assert driver([1, 0, 2, 0, 3, 4], [1, 2, 3, 4, 0, 0]) == "PASSED"

def test1():
  assert driver([2, 3, 2, 0, 0, 4, 0, 5, 0], [2, 3, 2, 4, 5, 0, 0, 0, 0]) == "PASSED"

def test2():
  assert driver([0, 1, 0, 1, 1], [1, 1, 1, 0, 0]) == "PASSED"

