from program811 import driver
def test0():
  assert driver([[10, 4], [2, 5]], [[10, 4], [2, 5]], True) == "PASSED"

def test1():
  assert driver([[1, 2], [3, 7]], [[12, 14], [12, 45]], False) == "PASSED"

def test2():
  assert driver([[2, 14], [12, 25]], [[2, 14], [12, 25]], True) == "PASSED"

