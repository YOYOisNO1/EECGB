from program308 import driver
def test0():
  assert driver([1, 2, 3, 4, 5, 6], [3, 6, 8, 9, 10, 6], 3, [60, 54, 50]) == "PASSED"

def test1():
  assert driver([1, 2, 3, 4, 5, 6], [3, 6, 8, 9, 10, 6], 4, [60, 54, 50, 48]) == "PASSED"

def test2():
  assert driver([1, 2, 3, 4, 5, 6], [3, 6, 8, 9, 10, 6], 5, [60, 54, 50, 48, 45]) == "PASSED"

