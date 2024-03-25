from program70 import driver
def test0():
  assert driver([[11, 22, 33], [44, 55, 66]], 3, "All tuples have same length") == "FAILED"

def test1():
  assert driver([[1, 2, 3], [4, 5, 6, 7]], 3, "All tuples do not have same length") == "FAILED"

def test2():
  assert driver([[1, 2], [3, 4]], 2, "All tuples have same length") == "FAILED"

