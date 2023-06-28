from program304 import driver
def test0():
  assert driver([1, 2, 3, 4, 5], [[0, 2], [0, 3]], 2, 1, 3) == "PASSED"

def test1():
  assert driver([1, 2, 3, 4], [[0, 1], [0, 2]], 1, 2, 3) == "PASSED"

def test2():
  assert driver([1, 2, 3, 4, 5, 6], [[0, 1], [0, 2]], 1, 1, 1) == "PASSED"

