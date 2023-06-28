from program534 import driver
def test0():
  assert driver("python", "python programming language", [0, 6]) == "FAILED"

def test1():
  assert driver("programming", "python programming language", [7, 18]) == "FAILED"

def test2():
  assert driver("language", "python programming language", [19, 27]) == "FAILED"

