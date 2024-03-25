from program377 import driver
def test0():
  assert driver("aba", 'a', "b") == "PASSED"

def test1():
  assert driver("toggle", 'g', "tole") == "PASSED"

def test2():
  assert driver("aabbc", 'b', "aac") == "PASSED"

