from program230 import driver
def test0():
  assert driver("hello people", '@', "hello@people") == "PASSED"

def test1():
  assert driver("python program language", '$', "python$program$language") == "PASSED"

def test2():
  assert driver("blank space", '-', "blank-space") == "PASSED"

