from program57 import driver
def test0():
  assert driver([1, 2, 3], 3, 321) == "PASSED"

def test1():
  assert driver([4, 5, 6, 1], 4, 6541) == "PASSED"

def test2():
  assert driver([1, 2, 3, 9], 4, 9321) == "PASSED"

