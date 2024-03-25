from program161 import driver
def test0():
  assert driver([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8], [1, 3, 5, 7, 9, 10]) == "PASSED"

def test1():
  assert driver([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 3, 5, 7], [2, 4, 6, 8, 9, 10]) == "PASSED"

def test2():
  assert driver([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [5, 7], [1, 2, 3, 4, 6, 8, 9, 10]) == "PASSED"

