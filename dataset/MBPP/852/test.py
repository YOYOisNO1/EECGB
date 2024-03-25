from program852 import driver
def test0():
  assert driver([1, -2, 3, -4], [1, 3]) == "PASSED"

def test1():
  assert driver([1, 2, 3, -4], [1, 2, 3]) == "PASSED"

def test2():
  assert driver([4, 5, -6, 7, -8], [4, 5, 7]) == "PASSED"

