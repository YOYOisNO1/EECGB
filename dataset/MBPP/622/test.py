from program622 import driver
def test0():
  assert driver([1, 12, 15, 26, 38], [2, 13, 17, 30, 45], 5, 16.0) == "PASSED"

def test1():
  assert driver([2, 4, 8, 9], [7, 13, 19, 28], 4, 8.5) == "PASSED"

def test2():
  assert driver([3, 6, 14, 23, 36, 42], [2, 18, 27, 39, 49, 55], 6, 25.0) == "PASSED"

