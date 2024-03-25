from program890 import driver
def test0():
  assert driver([1, 2, 3, 4], [1, 2, 3], 3, 3) == "PASSED"

def test1():
  assert driver([2, 4, 6, 8, 10], [2, 4, 6, 8], 4, 4) == "PASSED"

def test2():
  assert driver([1, 3, 5, 7, 9, 11], [1, 3, 5, 7, 9], 5, 5) == "PASSED"

