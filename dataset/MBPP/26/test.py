from program26 import driver
def test0():
  assert driver([[4, 4], [4, 4, 4], [4, 4], [4, 4, 4, 4], [4]], 4, True) == "PASSED"

def test1():
  assert driver([[7, 7, 7], [7, 7]], 7, True) == "PASSED"

def test2():
  assert driver([[9, 9], [9, 9, 9, 9]], 7, False) == "PASSED"

