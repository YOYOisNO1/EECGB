from program8 import driver
def test0():
  assert driver([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]) == "PASSED"

def test1():
  assert driver([10, 20, 30], [100, 400, 900]) == "PASSED"

def test2():
  assert driver([12, 15], [144, 225]) == "PASSED"

