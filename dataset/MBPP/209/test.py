from program209 import driver
def test0():
  assert driver([25, 44, 68, 21, 39, 23, 89], 21, [21, 25, 23, 44, 39, 68, 89]) == "PASSED"

def test1():
  assert driver([25, 44, 68, 21, 39, 23, 89], 110, [23, 25, 68, 44, 39, 110, 89]) == "PASSED"

def test2():
  assert driver([25, 44, 68, 21, 39, 23, 89], 500, [23, 25, 68, 44, 39, 500, 89]) == "PASSED"

