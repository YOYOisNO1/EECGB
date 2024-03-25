from program572 import driver
def test0():
  assert driver([1, 2, 3, 2, 3, 4, 5], [1, 4, 5]) == "PASSED"

def test1():
  assert driver([1, 2, 3, 2, 4, 5], [1, 3, 4, 5]) == "PASSED"

def test2():
  assert driver([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == "PASSED"

