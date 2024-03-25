from program46 import driver
def test0():
  assert driver([1, 5, 7, 9], True) == "PASSED"

def test1():
  assert driver([2, 4, 5, 5, 7, 9], False) == "PASSED"

def test2():
  assert driver([1, 2, 3], True) == "PASSED"

