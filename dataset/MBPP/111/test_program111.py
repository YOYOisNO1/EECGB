from program111 import driver
def test0():
  assert driver([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]], [18, 12]) == "PASSED"

def test1():
  assert driver([[12, 5, 23, 25, 45], [7, 11, 5, 23, 28], [1, 5, 8, 18, 23, 16]], [5, 23]) == "PASSED"

def test2():
  assert driver([[2, 3, 4, 1], [4, 5], [6, 4, 8], [4, 5], [6, 8, 4]], [4]) == "PASSED"

