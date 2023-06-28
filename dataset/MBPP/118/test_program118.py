from program118 import driver
def test0():
  assert driver("python programming", ["python", "programming"]) == "PASSED"

def test1():
  assert driver("lists tuples strings", ["lists", "tuples", "strings"]) == "PASSED"

def test2():
  assert driver("write a program", ["write", "a", "program"]) == "PASSED"

