from program310 import driver
def test0():
  assert driver("python 3.0", ['p', 'y', 't', 'h', 'o', 'n', '3', '.', '0']) == "FAILED"

def test1():
  assert driver("item1", ['i', 't', 'e', 'm', '1']) == "FAILED"

def test2():
  assert driver("15.10", ['1', '5', '.', '1', '0']) == "FAILED"

