from program648 import driver
def test0():
  assert driver([0, 1, 2, 3, 4, 5], [1, 0, 3, 2, 5, 4]) == "PASSED"

def test1():
  assert driver([5, 6, 7, 8, 9, 10], [6, 5, 8, 7, 10, 9]) == "PASSED"

def test2():
  assert driver([25, 35, 45, 55, 75, 95], [35, 25, 55, 45, 95, 75]) == "PASSED"

