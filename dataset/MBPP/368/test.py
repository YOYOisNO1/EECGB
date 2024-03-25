from program368 import driver
def test0():
  assert driver([1, 3], 4, [[1, 3], [1, 3], [1, 3], [1, 3]]) == "FAILED"

def test1():
  assert driver([1, 2], 3, [[1, 2], [1, 2], [1, 2]]) == "FAILED"

def test2():
  assert driver([3, 4], 5, [[3, 4], [3, 4], [3, 4], [3, 4], [3, 4]]) == "FAILED"

