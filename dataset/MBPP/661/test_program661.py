from program661 import driver
def test0():
  assert driver([100, 1000, 100, 1000, 1], 5, 2101) == "PASSED"

def test1():
  assert driver([3000, 2000, 1000, 3, 10], 5, 5013) == "PASSED"

def test2():
  assert driver([1, 2, 3, 4, 5, 6, 7, 8], 8, 27) == "PASSED"

