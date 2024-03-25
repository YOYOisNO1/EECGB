from program536 import driver
def test0():
  assert driver([1, 2, 3, 4, 5, 6, 7, 8, 9], 2, [1, 3, 5, 7, 9]) == "PASSED"

def test1():
  assert driver([10, 15, 19, 17, 16, 18], 3, [10, 17]) == "PASSED"

def test2():
  assert driver([14, 16, 19, 15, 17], 4, [14, 17]) == "PASSED"

