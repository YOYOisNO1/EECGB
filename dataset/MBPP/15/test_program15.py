from program15 import driver
def test0():
  assert driver("AbCd", ["bC", "d"]) == "PASSED"

def test1():
  assert driver("Python", ["y", "t", "h", "o", "n"]) == "PASSED"

def test2():
  assert driver("Programming", ["r", "o", "g", "r", "a", "m", "m", "i", "n", "g"]) == "PASSED"

