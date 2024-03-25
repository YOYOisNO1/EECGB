from program250 import driver
def test0():
  assert driver([10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2], 4, 0) == "PASSED"

def test1():
  assert driver([10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2], 10, 3) == "PASSED"

def test2():
  assert driver([10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2], 8, 4) == "PASSED"

