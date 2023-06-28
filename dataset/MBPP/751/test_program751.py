from program751 import driver
def test0():
  assert driver([1, 2, 3, 4, 5, 6], 0, True) == "PASSED"

def test1():
  assert driver([2, 3, 4, 5, 10, 15], 0, True) == "PASSED"

def test2():
  assert driver([2, 10, 4, 5, 3, 15], 0, False) == "PASSED"

