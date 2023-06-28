from program184 import driver
def test0():
  assert driver([220, 330, 500], 200, True) == "PASSED"

def test1():
  assert driver([12, 17, 21], 20, False) == "PASSED"

def test2():
  assert driver([1, 2, 3, 4], 10, False) == "PASSED"

