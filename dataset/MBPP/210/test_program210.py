from program210 import driver
def test0():
  assert driver("ABCDEFabcdef123450", True) == "PASSED"

def test1():
  assert driver("*&%@#!}{", False) == "PASSED"

def test2():
  assert driver("HELLOhowareyou98765", True) == "PASSED"

