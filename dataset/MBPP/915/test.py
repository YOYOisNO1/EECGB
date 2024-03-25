from program915 import driver
def test0():
  assert driver([-1, 2, -3, 5, 7, 8, 9, -10], [2, 5, 7, 8, 9, -10, -3, -1]) == "PASSED"

def test1():
  assert driver([10, 15, 14, 13, -18, 12, -20], [10, 12, 13, 14, 15, -20, -18]) == "PASSED"

def test2():
  assert driver([-20, 20, -10, 10, -30, 30], [10, 20, 30, -30, -20, -10]) == "PASSED"

