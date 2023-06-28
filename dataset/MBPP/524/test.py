from program524 import driver
def test0():
  assert driver([1, 101, 2, 3, 100, 4, 5], 7, 106) == "PASSED"

def test1():
  assert driver([3, 4, 5, 10], 4, 22) == "PASSED"

def test2():
  assert driver([10, 5, 4, 3], 4, 10) == "PASSED"

