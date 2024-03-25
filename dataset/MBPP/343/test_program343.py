from program343 import driver
def test0():
  assert driver("python", [6, 0]) == "FAILED"

def test1():
  assert driver("program", [7, 0]) == "FAILED"

def test2():
  assert driver("python3.0", [6, 2]) == "FAILED"

