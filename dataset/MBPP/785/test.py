from program785 import driver
def test0():
  assert driver("(7, 8, 9)", [7, 8, 9]) == "FAILED"

def test1():
  assert driver("(1, 2, 3)", [1, 2, 3]) == "FAILED"

def test2():
  assert driver("(4, 5, 6)", [4, 5, 6]) == "FAILED"

