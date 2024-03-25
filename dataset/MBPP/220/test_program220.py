from program220 import driver
def test0():
  assert driver("Python language, Programming language.", 2, "Python:language: Programming language.") == "PASSED"

def test1():
  assert driver("a b c,d e f", 3, "a:b:c:d e f") == "PASSED"

def test2():
  assert driver("ram reshma,ram rahim", 1, "ram:reshma,ram rahim") == "PASSED"

