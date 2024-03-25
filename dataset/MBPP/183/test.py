from program183 import driver
def test0():
  assert driver([1, 5, 3, 4, 2], 5, 3, 2) == "PASSED"

def test1():
  assert driver([8, 12, 16, 4, 0, 20], 6, 4, 5) == "PASSED"

def test2():
  assert driver([2, 4, 1, 3, 4], 5, 2, 3) == "PASSED"

