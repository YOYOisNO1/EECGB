from program485 import driver
def test0():
  assert driver([1, 232, 54545, 999991], 4, 54545) == "FAILED"

def test1():
  assert driver([1, 2, 3, 4, 5, 50], 6, 5) == "FAILED"

def test2():
  assert driver([1, 3, 7, 9, 45], 5, 9) == "FAILED"

