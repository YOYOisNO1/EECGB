from program969 import driver
def test0():
  assert driver([[5, 6], [5, 7], [6, 8], [6, 10], [7, 13]], [[5, 6, 7], [6, 8, 10], [7, 13]]) == "FAILED"

def test1():
  assert driver([[6, 7], [6, 8], [7, 9], [7, 11], [8, 14]], [[6, 7, 8], [7, 9, 11], [8, 14]]) == "FAILED"

def test2():
  assert driver([[7, 8], [7, 9], [8, 10], [8, 12], [9, 15]], [[7, 8, 9], [8, 10, 12], [9, 15]]) == "FAILED"

