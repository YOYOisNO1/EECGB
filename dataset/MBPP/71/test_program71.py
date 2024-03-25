from program71 import driver
def test0():
  assert driver([5, 15, 37, 25, 79], [5, 15, 25, 37, 79]) == "PASSED"

def test1():
  assert driver([41, 32, 15, 19, 22], [15, 19, 22, 32, 41]) == "PASSED"

def test2():
  assert driver([99, 15, 13, 47], [13, 15, 47, 99]) == "PASSED"

