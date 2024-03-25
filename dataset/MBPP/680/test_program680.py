from program680 import driver
def test0():
  assert driver([1, 2, 3, 4], True) == "PASSED"

def test1():
  assert driver([4, 3, 2, 1], False) == "PASSED"

def test2():
  assert driver([0, 1, 4, 9], True) == "PASSED"

