from program412 import driver
def test0():
  assert driver([1, 2, 3], [2]) == "PASSED"

def test1():
  assert driver([2, 4, 6], [2, 4, 6]) == "PASSED"

def test2():
  assert driver([10, 20, 3], [10, 20]) == "PASSED"

