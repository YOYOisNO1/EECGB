from program21 import driver
def test0():
  assert driver(4, 3, [3, 6, 9, 12]) == "PASSED"

def test1():
  assert driver(2, 5, [5, 10]) == "PASSED"

def test2():
  assert driver(9, 2, [2, 4, 6, 8, 10, 12, 14, 16, 18]) == "PASSED"

