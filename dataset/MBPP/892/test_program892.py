from program892 import driver
def test0():
  assert driver("python  program", "python program") == "PASSED"

def test1():
  assert driver("python   programming    language", "python programming language") == "PASSED"

def test2():
  assert driver("python                     program", "python program") == "PASSED"

