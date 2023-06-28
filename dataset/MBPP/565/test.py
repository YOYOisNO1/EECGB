from program565 import driver
def test0():
  assert driver("python", ['p', 'y', 't', 'h', 'o', 'n']) == "PASSED"

def test1():
  assert driver("Name", ['N', 'a', 'm', 'e']) == "PASSED"

def test2():
  assert driver("program", ['p', 'r', 'o', 'g', 'r', 'a', 'm']) == "PASSED"

