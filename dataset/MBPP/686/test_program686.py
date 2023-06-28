from program686 import driver
def test0():
  assert driver([4, 5, 4, 5, 6, 6, 5, 5, 4], "{4: 3, 5: 4, 6: 2}") == "PASSED"

def test1():
  assert driver([7, 8, 8, 9, 4, 7, 6, 5, 4], "{7: 2, 8: 2, 9: 1, 4: 2, 6: 1, 5: 1}") == "PASSED"

def test2():
  assert driver([1, 4, 3, 1, 4, 5, 2, 6, 2, 7], "{1: 2, 4: 2, 3: 1, 5: 1, 2: 2, 6: 1, 7: 1}") == "PASSED"

