from program515 import driver
def test0():
  assert driver([3, 1, 7, 5], 4, 6, True) == "PASSED"

def test1():
  assert driver([1, 7], 2, 5, False) == "PASSED"

def test2():
  assert driver([1, 6], 2, 5, False) == "PASSED"

