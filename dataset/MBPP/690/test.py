from program690 import driver
def test0():
  assert driver([1, 1, 3, 4, 4, 5, 6, 7], [1, 3, 12, 16, 20, 30, 42]) == "PASSED"

def test1():
  assert driver([4, 5, 8, 9, 6, 10], [20, 40, 72, 54, 60]) == "PASSED"

def test2():
  assert driver([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 6, 12, 20, 30, 42, 56, 72, 90]) == "PASSED"

