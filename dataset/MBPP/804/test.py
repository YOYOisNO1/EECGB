from program804 import driver
def test0():
  assert driver([1, 2, 3], 3, True) == "PASSED"

def test1():
  assert driver([1, 2, 1, 4], 4, True) == "PASSED"

def test2():
  assert driver([1, 1], 2, False) == "PASSED"

