from program197 import driver
def test0():
  assert driver([10, 4, 5, 6], [5, 6, 7, 5], [100000, 4096, 78125, 7776]) == "FAILED"

def test1():
  assert driver([11, 5, 6, 7], [6, 7, 8, 6], [1771561, 78125, 1679616, 117649]) == "FAILED"

def test2():
  assert driver([12, 6, 7, 8], [7, 8, 9, 7], [35831808, 1679616, 40353607, 2097152]) == "FAILED"

