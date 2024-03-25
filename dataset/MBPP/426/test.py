from program426 import driver
def test0():
  assert driver([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 3, 5, 7, 9]) == "PASSED"

def test1():
  assert driver([10, 20, 45, 67, 84, 93], [45, 67, 93]) == "PASSED"

def test2():
  assert driver([5, 7, 9, 8, 6, 4, 3], [5, 7, 9, 3]) == "PASSED"

