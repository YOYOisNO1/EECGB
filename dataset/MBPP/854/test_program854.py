from program854 import driver
def test0():
  assert driver([25, 44, 68, 21, 39, 23, 89], [21, 25, 23, 44, 39, 68, 89]) == "PASSED"

def test1():
  assert driver([25, 35, 22, 85, 14, 65, 75, 25, 58], [14, 25, 22, 25, 35, 65, 75, 85, 58]) == "PASSED"

def test2():
  assert driver([4, 5, 6, 2], [2, 4, 6, 5]) == "PASSED"

