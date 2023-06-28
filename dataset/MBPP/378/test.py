from program378 import driver
def test0():
  assert driver([1, 2, 3, 4], [4, 1, 2, 3]) == "PASSED"

def test1():
  assert driver([0, 1, 2, 3], [3, 0, 1, 2]) == "PASSED"

def test2():
  assert driver([9, 8, 7, 1], [1, 9, 8, 7]) == "PASSED"

