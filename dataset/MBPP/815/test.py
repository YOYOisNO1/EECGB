from program815 import driver
def test0():
  assert driver([1, 2, 0, 1, 0, 1, 2, 1, 1], 9, [0, 0, 1, 1, 1, 1, 1, 2, 2]) == "PASSED"

def test1():
  assert driver([1, 0, 0, 1, 2, 1, 2, 2, 1, 0], 10, [0, 0, 0, 1, 1, 1, 1, 2, 2, 2]) == "PASSED"

def test2():
  assert driver([2, 2, 1, 0, 0, 0, 1, 1, 2, 1], 10, [0, 0, 0, 1, 1, 1, 1, 2, 2, 2]) == "PASSED"

