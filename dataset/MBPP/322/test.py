from program322 import driver
def test0():
  assert driver([12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54], [3, 11]) == "PASSED"

def test1():
  assert driver([1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5], [0]) == "PASSED"

def test2():
  assert driver([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], [1]) == "PASSED"

