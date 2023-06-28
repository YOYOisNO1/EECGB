from program629 import driver
def test0():
  assert driver([1, 2, 3, 4, 5], [2, 4]) == "PASSED"

def test1():
  assert driver([4, 5, 6, 7, 8, 0, 1], [4, 6, 8, 0]) == "PASSED"

def test2():
  assert driver([8, 12, 15, 19], [8, 12]) == "PASSED"

