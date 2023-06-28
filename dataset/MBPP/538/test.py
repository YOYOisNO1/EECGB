from program538 import driver
def test0():
  assert driver("python 3.0", ['p', 'y', 't', 'h', 'o', 'n', '3', '.', '0']) == "FAILED"

def test1():
  assert driver("bigdata", ['b', 'i', 'g', 'd', 'a', 't', 'a']) == "FAILED"

def test2():
  assert driver("language", ['l', 'a', 'n', 'g', 'u', 'a', 'g', 'e']) == "FAILED"

