from program603 import driver
def test0():
  assert driver(10, [1, 2, 3, 5, 7]) == "PASSED"

def test1():
  assert driver(25, [1, 2, 3, 5, 7, 11, 13, 17, 23, 25]) == "PASSED"

def test2():
  assert driver(45, [1, 2, 3, 5, 7, 11, 13, 17, 23, 25, 29, 37, 41, 43]) == "PASSED"

