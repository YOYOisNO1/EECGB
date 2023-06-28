from program173 import driver
def test0():
  assert driver("python  @#&^%$*program123", "pythonprogram123") == "PASSED"

def test1():
  assert driver("python %^$@!^&*()  programming24%$^^()    language", "pythonprogramming24language") == "PASSED"

def test2():
  assert driver("python   ^%&^()(+_)(_^&67)                  program", "python67program") == "PASSED"

