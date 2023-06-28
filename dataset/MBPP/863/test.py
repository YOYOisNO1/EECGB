from program863 import driver
def test0():
  assert driver([1, 2, 2, 3], 4, 3) == "PASSED"

def test1():
  assert driver([1, 9, 3, 10, 4, 20, 2], 7, 4) == "PASSED"

def test2():
  assert driver([36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42], 11, 5) == "PASSED"

