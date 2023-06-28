from program249 import driver
def test0():
  assert driver([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9], [1, 2, 8, 9]) == "PASSED"

def test1():
  assert driver([1, 2, 3, 5, 7, 8, 9, 10], [3, 5, 7, 9], [3, 5, 7, 9]) == "PASSED"

def test2():
  assert driver([1, 2, 3, 5, 7, 8, 9, 10], [10, 20, 30, 40], [10]) == "PASSED"

