from program537 import driver
def test0():
  assert driver("ab ca bc ab", "ab") == "PASSED"

def test1():
  assert driver("ab ca bc", "None") == "PASSED"

def test2():
  assert driver("ab ca bc ca ab bc", "ca") == "PASSED"

