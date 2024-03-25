from program10 import driver
def test0():
  assert driver([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 2, [10, 20]) == "PASSED"

def test1():
  assert driver([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 5, [10, 20, 20, 40, 50]) == "PASSED"

def test2():
  assert driver([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 3, [10, 20, 20]) == "PASSED"

