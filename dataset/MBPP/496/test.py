from program496 import driver
def test0():
  assert driver([25, 35, 22, 85, 14, 65, 75, 25, 58], 3, [14, 22, 25]) == "PASSED"

def test1():
  assert driver([25, 35, 22, 85, 14, 65, 75, 25, 58], 2, [14, 22]) == "PASSED"

def test2():
  assert driver([25, 35, 22, 85, 14, 65, 75, 22, 58], 5, [14, 22, 22, 25, 35]) == "PASSED"

