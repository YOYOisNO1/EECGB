from program4 import driver
def test0():
  assert driver([25, 35, 22, 85, 14, 65, 75, 22, 58], 3, [85, 75, 65]) == "PASSED"

def test1():
  assert driver([25, 35, 22, 85, 14, 65, 75, 22, 58], 2, [85, 75]) == "PASSED"

def test2():
  assert driver([25, 35, 22, 85, 14, 65, 75, 22, 58], 5, [85, 75, 65, 58, 35]) == "PASSED"

