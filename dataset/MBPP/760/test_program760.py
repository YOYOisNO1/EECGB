from program760 import driver
def test0():
  assert driver([1, 1, 1], 3, "YES") == "PASSED"

def test1():
  assert driver([1, 2, 1, 2], 4, "NO") == "PASSED"

def test2():
  assert driver([1, 2, 3, 4, 5], 5, "NO") == "PASSED"

