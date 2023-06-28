from program943 import driver
def test0():
  assert driver([1, 3, 5, 7, 9, 11], [0, 2, 4, 6, 8, 10], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == "PASSED"

def test1():
  assert driver([1, 3, 5, 6, 8, 9], [2, 5, 7, 11], [1, 2, 3, 5, 5, 6, 7, 8, 9, 11]) == "PASSED"

def test2():
  assert driver([1, 3, 7], [2, 4, 6], [1, 2, 3, 4, 6, 7]) == "PASSED"

