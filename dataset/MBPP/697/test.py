from program697 import driver
def test0():
  assert driver([1, 2, 3, 5, 7, 8, 9, 10], 3) == "PASSED"

def test1():
  assert driver([10, 15, 14, 13, -18, 12, -20], 5) == "PASSED"

def test2():
  assert driver([1, 2, 4, 8, 9], 3) == "PASSED"

