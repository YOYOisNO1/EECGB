from program69 import driver
def test0():
  assert driver([2, 4, 3, 5, 7], [3, 7], False) == "PASSED"

def test1():
  assert driver([2, 4, 3, 5, 7], [4, 3], True) == "PASSED"

def test2():
  assert driver([2, 4, 3, 5, 7], [1, 6], False) == "PASSED"

