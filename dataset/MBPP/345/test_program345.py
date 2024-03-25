from program345 import driver
def test0():
  assert driver([1, 1, 3, 4, 4, 5, 6, 7], [0, 2, 1, 0, 1, 1, 1]) == "PASSED"

def test1():
  assert driver([4, 5, 8, 9, 6, 10], [1, 3, 1, -3, 4]) == "PASSED"

def test2():
  assert driver([0, 1, 2, 3, 4, 4, 4, 4, 5, 7], [1, 1, 1, 1, 0, 0, 0, 1, 2]) == "PASSED"

