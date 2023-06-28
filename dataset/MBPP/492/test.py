from program492 import driver
def test0():
  assert driver([1, 2, 3, 5, 8], 6, False) == "PASSED"

def test1():
  assert driver([7, 8, 9, 10, 13], 10, True) == "PASSED"

def test2():
  assert driver([11, 13, 14, 19, 22, 36], 23, False) == "PASSED"

