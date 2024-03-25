from program567 import driver
def test0():
  assert driver([1, 2, 4, 6, 8, 10, 12, 14, 16, 17], True) == "PASSED"

def test1():
  assert driver([1, 2, 4, 6, 8, 10, 12, 14, 20, 17], False) == "PASSED"

def test2():
  assert driver([1, 2, 4, 6, 8, 10, 15, 14, 20], False) == "PASSED"

