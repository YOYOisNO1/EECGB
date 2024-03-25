from program805 import driver
def test0():
  assert driver([[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]], [10, 11, 12]) == "PASSED"

def test1():
  assert driver([[3, 2, 1], [6, 5, 4], [12, 11, 10]], [12, 11, 10]) == "PASSED"

def test2():
  assert driver([[2, 3, 1]], [2, 3, 1]) == "PASSED"

