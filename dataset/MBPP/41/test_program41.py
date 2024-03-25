from program41 import driver
def test0():
  assert driver([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8, 10]) == "PASSED"

def test1():
  assert driver([10, 20, 45, 67, 84, 93], [10, 20, 84]) == "PASSED"

def test2():
  assert driver([5, 7, 9, 8, 6, 4, 3], [8, 6, 4]) == "PASSED"

