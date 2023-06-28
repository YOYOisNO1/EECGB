from program659 import driver
def test0():
  assert driver([10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20], [20, 30, -20, 60]) == "PASSED"

def test1():
  assert driver([-1, 1, -1, 8], [-1]) == "PASSED"

def test2():
  assert driver([1, 2, 3, 1, 2], [1, 2]) == "PASSED"

