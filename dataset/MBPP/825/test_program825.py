from program825 import driver
def test0():
  assert driver([2, 3, 8, 4, 7, 9], [0, 3, 5], [2, 4, 9]) == "PASSED"

def test1():
  assert driver([1, 2, 3, 4, 5], [1, 2], [2, 3]) == "PASSED"

def test2():
  assert driver([1, 0, 2, 3], [0, 1], [1, 0]) == "PASSED"

