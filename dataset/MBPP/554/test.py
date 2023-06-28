from program554 import driver
def test0():
  assert driver([1, 2, 3, 4, 5, 6], [1, 3, 5]) == "PASSED"

def test1():
  assert driver([10, 11, 12, 13], [11, 13]) == "PASSED"

def test2():
  assert driver([7, 8, 9, 1], [7, 9, 1]) == "PASSED"

