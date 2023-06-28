from program205 import driver
def test0():
  assert driver([7, 8, 9, 1, 10, 7], [-8, -9, -10, -2, -11, -8]) == "FAILED"

def test1():
  assert driver([2, 4, 5, 6, 1, 7], [-3, -5, -6, -7, -2, -8]) == "FAILED"

def test2():
  assert driver([8, 9, 11, 14, 12, 13], [-9, -10, -12, -15, -13, -14]) == "FAILED"

