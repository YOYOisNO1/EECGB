from program553 import driver
def test0():
  assert driver([4, 56], 4.56) == "PASSED"

def test1():
  assert driver([7, 256], 7.256) == "PASSED"

def test2():
  assert driver([8, 123], 8.123) == "PASSED"

