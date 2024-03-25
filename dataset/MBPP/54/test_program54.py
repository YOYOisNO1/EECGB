from program54 import driver
def test0():
  assert driver([1, 23, 4, 5, 6, 7, 8], [1, 4, 5, 6, 7, 8, 23]) == "PASSED"

def test1():
  assert driver([12, 9, 28, 33, 69, 45], [9, 12, 28, 33, 45, 69]) == "PASSED"

def test2():
  assert driver([8, 4, 14, 3, 2, 1], [1, 2, 3, 4, 8, 14]) == "PASSED"

