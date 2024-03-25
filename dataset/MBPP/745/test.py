from program745 import driver
def test0():
  assert driver(1, 22, [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]) == "PASSED"

def test1():
  assert driver(1, 15, [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15]) == "PASSED"

def test2():
  assert driver(20, 25, [22, 24]) == "PASSED"

