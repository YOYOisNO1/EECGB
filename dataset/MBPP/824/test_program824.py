from program824 import driver
def test0():
  assert driver([1, 3, 5, 2], [1, 3, 5]) == "PASSED"

def test1():
  assert driver([5, 6, 7], [5, 7]) == "PASSED"

def test2():
  assert driver([1, 2, 3, 4], [1, 3]) == "PASSED"

