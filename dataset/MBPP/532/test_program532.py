from program532 import driver
def test0():
  assert driver("abc", "cba", True) == "PASSED"

def test1():
  assert driver("test", "ttew", False) == "PASSED"

def test2():
  assert driver("xxyz", "yxzx", True) == "PASSED"

