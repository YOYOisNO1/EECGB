from program921 import driver
def test0():
  assert driver([10, 4, 5, 6, 7, 6, 8, 3, 4], 3, [[10, 4, 5], [6, 7, 6], [8, 3, 4]]) == "PASSED"

def test1():
  assert driver([1, 2, 3, 4, 5, 6, 7, 8, 9], 2, [[1, 2], [3, 4], [5, 6], [7, 8], [9]]) == "PASSED"

def test2():
  assert driver([11, 14, 16, 17, 19, 21, 22, 25], 4, [[11, 14, 16, 17], [19, 21, 22, 25]]) == "PASSED"

