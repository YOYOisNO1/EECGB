from program316 import driver
def test0():
  assert driver([2, 5, 5, 5, 6, 6, 8, 9, 9, 9], 5, 3) == "PASSED"

def test1():
  assert driver([2, 3, 5, 8, 6, 6, 8, 9, 9, 9], 9, 9) == "PASSED"

def test2():
  assert driver([2, 2, 1, 5, 6, 6, 6, 9, 9, 9], 6, 6) == "PASSED"

