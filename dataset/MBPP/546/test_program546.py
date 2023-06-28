from program546 import driver
def test0():
  assert driver("hello world", 'l', 10) == "PASSED"

def test1():
  assert driver("language", 'g', 7) == "PASSED"

def test2():
  assert driver("little", 'y', None) == "PASSED"

