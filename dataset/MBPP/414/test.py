from program414 import driver
def test0():
  assert driver([1, 2, 3, 4, 5], [6, 7, 8, 9], False) == "PASSED"

def test1():
  assert driver([1, 2, 3], [4, 5, 6], False) == "PASSED"

def test2():
  assert driver([1, 4, 5], [1, 4, 5], True) == "PASSED"

