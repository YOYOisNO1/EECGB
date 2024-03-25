from program408 import driver
def test0():
  assert driver([1, 3, 7], [2, 4, 6], 2, [[1, 2], [1, 4]]) == "PASSED"

def test1():
  assert driver([1, 3, 7], [2, 4, 6], 1, [[1, 2]]) == "PASSED"

def test2():
  assert driver([1, 3, 7], [2, 4, 6], 7, [[1, 2], [1, 4], [3, 2], [1, 6], [3, 4], [3, 6], [7, 2]]) == "PASSED"

