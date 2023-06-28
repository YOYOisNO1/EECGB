from program142 import driver
def test0():
  assert driver([1, 2, 3, 4, 5, 6, 7, 8], [2, 2, 3, 1, 2, 6, 7, 9], [2, 1, 3, 1, 2, 6, 7, 9], 3) == "PASSED"

def test1():
  assert driver([1, 2, 3, 4, 5, 6, 7, 8], [2, 2, 3, 1, 2, 6, 7, 8], [2, 1, 3, 1, 2, 6, 7, 8], 4) == "PASSED"

def test2():
  assert driver([1, 2, 3, 4, 2, 6, 7, 8], [2, 2, 3, 1, 2, 6, 7, 8], [2, 1, 3, 1, 2, 6, 7, 8], 5) == "PASSED"

