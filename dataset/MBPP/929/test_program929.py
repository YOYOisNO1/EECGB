from program929 import driver
def test0():
  assert driver([2, 4, 5, 6, 2, 3, 4, 4, 7], 4, 3) == "PASSED"

def test1():
  assert driver([2, 4, 5, 6, 2, 3, 4, 4, 7], 2, 2) == "PASSED"

def test2():
  assert driver([2, 4, 7, 7, 7, 3, 4, 4, 7], 7, 4) == "PASSED"

