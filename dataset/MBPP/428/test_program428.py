from program428 import driver
def test0():
  assert driver([12, 23, 4, 5, 3, 2, 12, 81, 56, 95], [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]) == "PASSED"

def test1():
  assert driver([24, 22, 39, 34, 87, 73, 68], [22, 24, 34, 39, 68, 73, 87]) == "PASSED"

def test2():
  assert driver([32, 30, 16, 96, 82, 83, 74], [16, 30, 32, 74, 82, 83, 96]) == "PASSED"

