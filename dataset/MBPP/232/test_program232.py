from program232 import driver
def test0():
  assert driver([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 2, [100, 90]) == "PASSED"

def test1():
  assert driver([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 5, [100, 90, 80, 70, 60]) == "PASSED"

def test2():
  assert driver([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 3, [100, 90, 80]) == "PASSED"

