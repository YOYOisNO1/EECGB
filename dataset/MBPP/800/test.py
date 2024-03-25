from program800 import driver
def test0():
  assert driver("python  program", "pythonprogram") == "PASSED"

def test1():
  assert driver("python   programming    language", "pythonprogramminglanguage") == "PASSED"

def test2():
  assert driver("python                     program", "pythonprogram") == "PASSED"

