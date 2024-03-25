from program579 import driver
def test0():
  assert driver([3, 4, 5, 6], [5, 7, 4, 10], [3, 6, 7, 10]) == "FAILED"

def test1():
  assert driver([1, 2, 3, 4], [7, 2, 3, 9], [1, 4, 7, 9]) == "FAILED"

def test2():
  assert driver([21, 11, 25, 26], [26, 34, 21, 36], [34, 36, 11, 25]) == "FAILED"

