from program898 import driver
def test0():
  assert driver([1, 1, 3, 4, 4, 5, 6, 7], 2, [1, 4]) == "PASSED"

def test1():
  assert driver([0, 1, 2, 3, 4, 4, 4, 4, 5, 7], 4, [4]) == "PASSED"

def test2():
  assert driver([0, 0, 0, 0, 0], 5, [0]) == "PASSED"

