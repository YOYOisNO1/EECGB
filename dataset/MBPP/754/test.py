from program754 import driver
def test0():
  assert driver([1, 1, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 7], [0, 1, 2, 3, 4, 5, 7], [1, 7]) == "PASSED"

def test1():
  assert driver([1, 1, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 6, 5], [0, 1, 2, 3, 4, 6, 7], [1, 6]) == "PASSED"

def test2():
  assert driver([1, 1, 3, 4, 6, 5, 6], [0, 1, 2, 3, 4, 5, 7], [0, 1, 2, 3, 4, 5, 7], [1, 5]) == "PASSED"

