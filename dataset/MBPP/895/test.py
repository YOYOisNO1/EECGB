from program895 import driver
def test0():
  assert driver([1, 2, 9, 4, 5, 0, 4, 11, 6], 26) == "PASSED"

def test1():
  assert driver([1, 2, 9, 5, 6, 0, 5, 12, 7], 28) == "PASSED"

def test2():
  assert driver([1, 3, 10, 5, 6, 0, 6, 14, 21], 44) == "PASSED"

