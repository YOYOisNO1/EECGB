from program196 import driver
def test0():
  assert driver([[4, 5], [4], [8, 6, 7], [1], [3, 4, 6, 7]], 1, [[4, 5], [8, 6, 7], [3, 4, 6, 7]]) == "PASSED"

def test1():
  assert driver([[4, 5], [4, 5], [6, 7], [1, 2, 3], [3, 4, 6, 7]], 2, [[1, 2, 3], [3, 4, 6, 7]]) == "PASSED"

def test2():
  assert driver([[1, 4, 4], [4, 3], [8, 6, 7], [1], [3, 6, 7]], 3, [[4, 3], [1]]) == "PASSED"

