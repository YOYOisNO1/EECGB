from program733 import driver
def test0():
  assert driver([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5, 1) == "PASSED"

def test1():
  assert driver([2, 3, 5, 5, 6, 6, 8, 9, 9, 9], 5, 2) == "PASSED"

def test2():
  assert driver([2, 4, 1, 5, 6, 6, 8, 9, 9, 9], 6, 4) == "PASSED"

