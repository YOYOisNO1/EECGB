from program775 import driver
def test0():
  assert driver([2, 1, 4, 3, 6, 7, 6, 3], True) == "PASSED"

def test1():
  assert driver([4, 1, 2], True) == "PASSED"

def test2():
  assert driver([1, 2, 3], False) == "PASSED"

