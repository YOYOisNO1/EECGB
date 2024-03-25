from program128 import driver
def test0():
  assert driver(3, "python is a programming language", ["python", "programming", "language"]) == "PASSED"

def test1():
  assert driver(2, "writing a program", ["writing", "program"]) == "PASSED"

def test2():
  assert driver(5, "sorting list", ["sorting"]) == "PASSED"

