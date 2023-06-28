from program175 import driver
def test0():
  assert driver("(){}[]", True) == "PASSED"

def test1():
  assert driver("()[{)}", False) == "PASSED"

def test2():
  assert driver("()", True) == "PASSED"

