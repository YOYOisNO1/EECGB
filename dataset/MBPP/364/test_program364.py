from program364 import driver
def test0():
  assert driver("0001010111", 2) == "FAILED"

def test1():
  assert driver("001", 1) == "FAILED"

def test2():
  assert driver("010111011", 2) == "FAILED"

