from program447 import driver
def test0():
  assert driver([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]) == "PASSED"

def test1():
  assert driver([10, 20, 30], [1000, 8000, 27000]) == "PASSED"

def test2():
  assert driver([12, 15], [1728, 3375]) == "PASSED"

