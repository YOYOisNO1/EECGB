from program623 import driver
def test0():
  assert driver([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2, [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]) == "PASSED"

def test1():
  assert driver([10, 20, 30], 3, [1000, 8000, 27000]) == "PASSED"

def test2():
  assert driver([12, 15], 5, [248832, 759375]) == "PASSED"

