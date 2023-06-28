from program576 import driver
def test0():
  assert driver([1, 4, 3, 5], [1, 2], 4, 2, False) == "PASSED"

def test1():
  assert driver([1, 2, 1], [1, 2, 1], 3, 3, True) == "PASSED"

def test2():
  assert driver([1, 0, 2, 2], [2, 2, 0], 4, 3, False) == "PASSED"

