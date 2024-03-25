from program131 import driver
def test0():
  assert driver("Python", "Python") == "PASSED"

def test1():
  assert driver("USA", "ASU") == "PASSED"

def test2():
  assert driver("ab", "ab") == "PASSED"

