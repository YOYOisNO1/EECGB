from program338 import driver
def test0():
  assert driver("aba", 4) == "FAILED"

def test1():
  assert driver("abcab", 7) == "FAILED"

def test2():
  assert driver("abc", 3) == "FAILED"

