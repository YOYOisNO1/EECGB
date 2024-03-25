from program34 import driver
def test0():
  assert driver([1, 2, 3, 5], 4, 4) == "PASSED"

def test1():
  assert driver([1, 3, 4, 5], 4, 2) == "PASSED"

def test2():
  assert driver([1, 2, 3, 5, 6, 7], 5, 4) == "PASSED"

