from program907 import driver
def test0():
  assert driver(10, [1, 3, 7, 9, 13, 15, 21, 25, 31, 33]) == "PASSED"

def test1():
  assert driver(5, [1, 3, 7, 9, 13]) == "PASSED"

def test2():
  assert driver(8, [1, 3, 7, 9, 13, 15, 21, 25]) == "PASSED"

