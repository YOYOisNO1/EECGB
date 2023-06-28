from program951 import driver
def test0():
  assert driver([[2, 4], [6, 7], [5, 1]], [[5, 4], [8, 10], [8, 14]], [[5, 4], [8, 10], [8, 14]]) == "FAILED"

def test1():
  assert driver([[3, 5], [7, 8], [6, 2]], [[6, 5], [9, 11], [9, 15]], [[6, 5], [9, 11], [9, 15]]) == "FAILED"

def test2():
  assert driver([[4, 6], [8, 9], [7, 3]], [[7, 6], [10, 12], [10, 16]], [[7, 6], [10, 12], [10, 16]]) == "FAILED"

