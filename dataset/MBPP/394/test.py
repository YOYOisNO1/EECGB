from program394 import driver
def test0():
  assert driver([1, 4, 5, 6, 1, 4], False) == "PASSED"

def test1():
  assert driver([1, 4, 5, 6], True) == "PASSED"

def test2():
  assert driver([2, 3, 4, 5, 6], True) == "PASSED"

