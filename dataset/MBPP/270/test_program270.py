from program270 import driver
def test0():
  assert driver([5, 6, 12, 1, 18, 8], 6, 30) == "PASSED"

def test1():
  assert driver([3, 20, 17, 9, 2, 10, 18, 13, 6, 18], 10, 26) == "PASSED"

def test2():
  assert driver([5, 6, 12, 1], 4, 12) == "PASSED"

