from program635 import driver
def test0():
  assert driver([1, 3, 5, 7, 9, 2, 4, 6, 8, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == "PASSED"

def test1():
  assert driver([25, 35, 22, 85, 14, 65, 75, 25, 58], [14, 22, 25, 25, 35, 58, 65, 75, 85]) == "PASSED"

def test2():
  assert driver([7, 1, 9, 5], [1, 5, 7, 9]) == "PASSED"

