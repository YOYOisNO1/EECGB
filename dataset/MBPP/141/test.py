from program141 import driver
def test0():
  assert driver([15, 79, 25, 38, 69], [15, 25, 38, 69, 79]) == "PASSED"

def test1():
  assert driver([98, 12, 54, 36, 85], [12, 36, 54, 85, 98]) == "PASSED"

def test2():
  assert driver([41, 42, 32, 12, 23], [12, 23, 32, 41, 42]) == "PASSED"

