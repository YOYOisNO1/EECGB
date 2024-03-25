from program769 import driver
def test0():
  assert driver([10, 15, 20, 25, 30, 35, 40], [25, 40, 35], [10, 20, 30, 15]) == "PASSED"

def test1():
  assert driver([1, 2, 3, 4, 5], [6, 7, 1], [2, 3, 4, 5, 6, 7]) == "PASSED"

def test2():
  assert driver([1, 2, 3], [6, 7, 1], [2, 3, 6, 7]) == "PASSED"

