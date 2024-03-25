from program782 import driver
def test0():
  assert driver([1, 2, 4], 14) == "PASSED"

def test1():
  assert driver([1, 2, 1, 2], 15) == "PASSED"

def test2():
  assert driver([1, 7], 8) == "PASSED"

