from program438 import driver
def test0():
  assert driver([[5, 6], [1, 2], [6, 5], [9, 1], [6, 5], [2, 1]], '3') == "PASSED"

def test1():
  assert driver([[5, 6], [1, 3], [6, 5], [9, 1], [6, 5], [2, 1]], '2') == "PASSED"

def test2():
  assert driver([[5, 6], [1, 2], [6, 5], [9, 2], [6, 5], [2, 1]], '4') == "PASSED"

