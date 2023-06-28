from program732 import driver
def test0():
  assert driver("Python language, Programming language.", "Python:language::Programming:language:") == "PASSED"

def test1():
  assert driver("a b c,d e f", "a:b:c:d:e:f") == "PASSED"

def test2():
  assert driver("ram reshma,ram rahim", "ram:reshma:ram:rahim") == "PASSED"

