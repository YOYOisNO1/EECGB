from program586 import driver
def test0():
  assert driver([12, 10, 5, 6, 52, 36], 6, 2, [5, 6, 52, 36, 12, 10]) == "PASSED"

def test1():
  assert driver([1, 2, 3, 4], 4, 1, [2, 3, 4, 1]) == "PASSED"

def test2():
  assert driver([0, 1, 2, 3, 4, 5, 6, 7], 8, 3, [3, 4, 5, 6, 7, 0, 1, 2]) == "PASSED"

