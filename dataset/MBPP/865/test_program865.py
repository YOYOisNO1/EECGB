from program865 import driver
def test0():
  assert driver([1, 2, 3, 4, 5, 6, 7], 3, [3, 6, 9, 12, 15, 18, 21]) == "PASSED"

def test1():
  assert driver([1, 2, 3, 4, 5, 6, 7], 4, [4, 8, 12, 16, 20, 24, 28]) == "PASSED"

def test2():
  assert driver([1, 2, 3, 4, 5, 6, 7], 10, [10, 20, 30, 40, 50, 60, 70]) == "PASSED"

