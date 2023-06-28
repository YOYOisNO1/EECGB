from program144 import driver
def test0():
  assert driver([1, 8, 9, 15, 16], 5, 74) == "PASSED"

def test1():
  assert driver([1, 2, 3, 4], 4, 10) == "PASSED"

def test2():
  assert driver([1, 2, 3, 4, 5, 7, 9, 11, 14], 9, 188) == "PASSED"

