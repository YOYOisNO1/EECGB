from program382 import driver
def test0():
  assert driver([8, 9, 10, 1, 2, 3, 4, 5, 6, 7], 3) == "PASSED"

def test1():
  assert driver([8, 9, 10, 2, 5, 6], 3) == "PASSED"

def test2():
  assert driver([2, 5, 6, 8, 9, 10], 0) == "PASSED"

