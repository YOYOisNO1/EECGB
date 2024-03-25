from program164 import driver
def test0():
  assert driver(36, 57, False) == "FAILED"

def test1():
  assert driver(2, 4, False) == "FAILED"

def test2():
  assert driver(23, 47, True) == "FAILED"

